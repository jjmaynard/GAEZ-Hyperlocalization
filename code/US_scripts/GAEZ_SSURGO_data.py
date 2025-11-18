# SSURGO Data Processing Functions

import os
import tempfile
import requests
import rasterio
import pandas as pd
import numpy as np
from rasterio.errors import RasterioError
import geopandas as gpd
from shapely.geometry import box, mapping
from pyproj import Transformer
import logging


# A simplified specification dictionary analogous to .mukey.spec in soilDB
_mukey_spec = {
    "gssurgo": {
        "crs": "EPSG:5070",
        "res": 30,
        "dsn": "gSSURGO",
        "na": -9999,          # placeholder NA flag
        "desc": "SSURGO data",
        "vintage": "2020"
    },
    "pr_ssurgo": {
        "crs": "EPSG:32161",
        "res": 30,
        "dsn": "PR_SSURGO",
        "na": -9999,
        "desc": "PR_SSURGO data",
        "vintage": "2020"
    },
    "hi_ssurgo": {
        "crs": "EPSG:6628",
        "res": 30,
        "dsn": "HI_SSURGO",
        "na": -9999,
        "desc": "HI_SSURGO data",
        "vintage": "2020"
    }
    # Additional database specifications can be added as needed.
}


def prepare_AEA_AOI(aoi, res, native_crs):
    """
    Prepare an Albers Equal-Area (AEA) AOI by ensuring the input AOI is in the native CRS,
    then computing its bounding box and pixel dimensions given a resolution.
    
    Parameters
    ----------
    aoi : GeoDataFrame or shapely.geometry (Polygon)
        The area of interest.
    res : int or float
        Resolution in meters.
    native_crs : str
        The target CRS (e.g. "EPSG:5070").
    
    Returns
    -------
    dict
        A dictionary with keys:
          - bbox: [minx, miny, maxx, maxy]
          - width: number of pixels in x-direction (float)
          - height: number of pixels in y-direction (float)
    """
    # If aoi is not a GeoDataFrame, try to wrap it in one.
    if not isinstance(aoi, gpd.GeoDataFrame):
        aoi = gpd.GeoDataFrame({'geometry': [aoi]}, crs="EPSG:4326")
    
    # Reproject AOI to native CRS if necessary.
    if aoi.crs.to_string() != native_crs:
        aoi = aoi.to_crs(native_crs)
    
    # Get bounding box
    minx, miny, maxx, maxy = aoi.total_bounds
    width = (maxx - minx) / res
    height = (maxy - miny) / res
    
    return {"bbox": [minx, miny, maxx, maxy], "width": width, "height": height}


def mukey_wcs(aoi, db='gssurgo', res=30, quiet=False):
    """
    Mimics soilDB::mukey.wcs by constructing a WCS request URL for fetching SSURGO data.
    Downloads the resulting GeoTIFF, opens it as a raster, and returns the raster.
    
    Parameters
    ----------
    aoi : GeoDataFrame, shapely.geometry, or similar
        The area of interest. This function will reproject it as needed.
    db : str, optional
        Database identifier. Allowed choices: "gnatsgo", "gssurgo", "rss", "statsgo", "pr_ssurgo", "hi_ssurgo".
        (Default "gssurgo")
    res : int or float, optional
        Resolution in meters. For gssurgo, should be between 30 and 3000. (Default 30)
    quiet : bool, optional
        If True, suppress informational messages. (Default False)
    
    Returns
    -------
    rasterio.DatasetReader or similar
        The downloaded and processed raster. If an error occurs, an exception is raised.
    """
    db = db.lower()
    allowed_dbs = ["gnatsgo", "gssurgo", "rss", "statsgo", "pr_ssurgo", "hi_ssurgo"]
    if db not in allowed_dbs:
        raise ValueError(f"db must be one of: {', '.join(allowed_dbs)}")
    
    var_spec = _mukey_spec[db]
    native_crs = var_spec["crs"]
    
    # Check resolution ranges
    if db in ["gnatsgo", "gssurgo", "rss", "statsgo"]:
        if res < 30 or res > 3000:
            raise ValueError("For gssurgo (and similar), res should be within 30 <= res <= 3000 meters")
    elif db == "rss":
        if res < 10 or res > 1000:
            raise ValueError("For rss, res should be within 10 <= res <= 1000 meters")
    
    # Prepare the AOI in native CRS and compute its dimensions
    wcs_geom = prepare_AEA_AOI(aoi, res, native_crs)
    width_px = wcs_geom["width"]
    height_px = wcs_geom["height"]
    
    if round(width_px) == 1 and round(height_px) == 1:
        raise ValueError("WCS requests for a 1x1 pixel image are not supported; try a smaller resolution.")
    
    max_img_dim = 5000
    if width_px > max_img_dim or height_px > max_img_dim:
        raise ValueError(f"AOI is too large: {width_px:.0f}x{height_px:.0f} pixels requested (max {max_img_dim}x{max_img_dim} pixels).")
    
    bbox = wcs_geom["bbox"]
    xmin, ymin, xmax, ymax = bbox
    # Calculate expected xmax and ymax based on pixel counts and resolution
    xmax2 = xmin + res * width_px
    ymax2 = ymin + res * height_px
    
    base_url = "http://casoilresource.lawr.ucdavis.edu/cgi-bin/mapserv?"
    service_url = "map=/soilmap2/website/wcs/mukey.map&SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage"
    
    # Construct the WCS URL
    url = (f"{base_url}{service_url}&COVERAGEID={var_spec['dsn']}"
           f"&FORMAT=image/tiff&GEOTIFF:COMPRESSION=DEFLATE"
           f"&SUBSETTINGCRS={native_crs}&FORMAT=GEOTIFF_FLOAT"
           f"&SUBSET=x({xmin},{xmax2})&SUBSET=y({ymin},{ymax2})"
           f"&RESOLUTION=x({res})&RESOLUTION=y({res})")
    
    if not quiet:
        print("Constructed WCS Request URL:")
        print(url)
    
    # Download the GeoTIFF from the URL to a temporary file.
    try:
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as tmp_file:
            tmp_filename = tmp_file.name
            response = requests.get(url, stream=True)
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                tmp_file.write(chunk)
    except requests.RequestException as e:
        raise RuntimeError(f"Error downloading WCS data: {e}")
    
    # Open the downloaded file as a raster using rasterio.
    try:
        raster = rasterio.open(tmp_filename)
    except RasterioError as e:
        os.remove(tmp_filename)
        raise RuntimeError(f"Error opening downloaded GeoTIFF: {e}")
    
    # Optionally, check the dimensions
    expected_cols = round((xmax2 - xmin) / res)
    expected_rows = round((ymax2 - ymin) / res)
    if raster.width != expected_cols or raster.height != expected_rows:
        print(f"Warning: Expected dimensions ({expected_cols} cols x {expected_rows} rows), but got ({raster.width} x {raster.height}).")
    
    # In a full implementation, you might process the raster further (e.g., reclassify NAs)
    # For now, we simply return the raster object.
    
    # Optionally, remove the temporary file after use
    # os.remove(tmp_filename)
    
    return raster


def getTextGroup(field):
    if field is None:
        return np.nan
    texture_group_map = {
        'C': ["sand", "loamy sand", "sandy loam"],
        'M': ["sandy clay loam", "loam", "clay loam", "silt loam", "silt", "silty clay loam"],
        'F': ["sandy clay", "silty clay", "clay"]
    }
    return next((key for key, value in texture_group_map.items() if field.lower() in value), np.nan)


def gettt(sand, silt=None, clay=None, row=None):
    """
    Determine USDA texture class from sand, silt, and clay percentages.

    Can be called in two ways:
    1. gettt(sand, silt, clay) - direct values
    2. gettt(row=dataframe_row) - extract from row
    """
    # Handle row-based call
    if row is not None and isinstance(row, (dict, pd.Series)):
        sand = row['sand']
        silt = row['silt']
        clay = row['clay']
    # Handle positional arguments (sand, silt, clay)
    elif silt is None or clay is None:
        # If called with a single argument that's a row-like object
        if hasattr(sand, '__getitem__'):
            row = sand
            sand = row['sand']
            silt = row['silt']
            clay = row['clay']
        else:
            raise ValueError("Must provide either (sand, silt, clay) or row parameter")

    silt_clay = silt + 1.5 * clay
    silt_2_clay = silt + 2.0 * clay

    if silt_clay < 15:
        return "Sand"
    elif silt_clay < 30:
        return "Loamy sand"
    elif (clay >= 7 and clay <= 20 and sand > 52 and silt_2_clay >= 30) or (clay < 7 and silt < 50 and silt_2_clay >= 30):
        return "Sandy loam"
    elif clay >= 7 and clay <= 27 and silt >= 28 and silt < 50 and sand <= 52:
        return "Loam"
    elif (silt >= 50 and clay >= 12 and clay < 27) or (silt >= 50 and silt < 80 and clay < 12):
        return "Silt loam"
    elif silt >= 80 and clay < 12:
        return "Silt"
    elif clay >= 20 and clay < 35 and silt < 28 and sand > 45:
        return "Sandy clay loam"
    elif clay >= 27 and clay < 40 and sand > 20 and sand <= 45:
        return "Clay loam"
    elif clay >= 27 and clay < 40 and sand <= 20:
        return "Silty clay loam"
    elif clay >= 35 and sand >= 45:
        return "Sandy clay"
    elif clay >= 40 and silt >= 40:
        return "Silty clay"
    elif clay >= 40 and sand <= 45 and silt < 40:
        return "Clay"
    else:
        return None  # Default case if no condition is met


def get_property_by_texture(texture, property_map):
    if texture is None:
        return np.nan
    return property_map.get(texture.lower(), np.nan)

def getTXT_id(texture):
    texture_id_map = {
        "sand": 12, "loamy sand": 11, "sandy loam": 10, "sandy clay loam": 9,
        "loam": 8, "silt": 5, "silt loam": 6, "silty clay loam": 3,
        "clay loam": 4, "sandy clay": 7, "silty clay": 2, "clay": 1
    }
    return get_property_by_texture(texture, texture_id_map) 


def classify_pscl(texture_or_row, clay=None, sand=None):
    """
    Classify particle size class (coarse/medium/fine) from texture.

    Can be called in two ways:
    1. classify_pscl(texture_name) - from texture string
    2. classify_pscl(row) - extract from row with 'texture', 'clay', 'sand' columns
    """
    # Initialize has_values flag
    has_values = False

    # Handle row-based call
    if isinstance(texture_or_row, (dict, pd.Series)):
        row = texture_or_row
        clay = row.get('clay', 0) if pd.notnull(row.get('clay')) else 0
        sand = row.get('sand', 0) if pd.notnull(row.get('sand')) else 0
        texture = row['texture'].lower().strip() if pd.notnull(row.get('texture')) else ''
        # Row-based calls always have values
        has_values = True
    # Handle texture string call
    elif isinstance(texture_or_row, str):
        texture = texture_or_row.lower().strip()
        # Track if clay and sand were provided
        has_values = (clay is not None) or (sand is not None)
        # If clay and sand not provided, set to 0
        if clay is None:
            clay = 0
        if sand is None:
            sand = 0
    else:
        return 'unknown'

    # Texture class groups from FAO definitions
    coarse_textures = ['sand', 'loamy sand', 'sandy loam']
    medium_textures = [
        'sandy loam', 'loam', 'sandy clay loam',
        'silt loam', 'silt', 'silty clay loam', 'clay loam'
    ]
    fine_textures = ['clay', 'silty clay', 'sandy clay', 'clay loam', 'silty clay loam']

    # If no numeric values provided, classify purely by texture group
    if not has_values:
        if texture in fine_textures:
            return '3'
        elif texture in medium_textures:
            return '2'
        elif texture in coarse_textures:
            return '1'
        else:
            return 'unknown'

    # --- Primary Rules with numeric thresholds ---
    if texture in fine_textures:
        if clay > 35:
            return '3'
        # Fallback: maybe medium?
        elif clay < 35 and sand < 65 or (sand <= 82 and clay >= 18):
            return '2'
        else:
            return '3'  # Default for fine textures

    if texture in medium_textures:
        if clay < 35 and sand < 65 or (sand <= 82 and clay >= 18):
            return '2'
        # Fallback: maybe fine?
        elif clay > 35:
            return '3'
        else:
            return '2'  # Default for medium textures

    if texture in coarse_textures:
        if clay < 18 and sand > 65:
            return '1'
        # Fallback: maybe medium?
        elif clay < 35 and sand < 65 or (sand <= 82 and clay >= 18):
            return '2'
        else:
            return '1'  # Default for coarse textures

    return 'unknown'


def ssurgo_gaez_data(mukey_list):
    """
    Extracts combined component-horizon data for the given list of mukey values
    using the sda_return() function.
    
    Args:
        mukey_list (list): List of mukey values (integers or strings) to filter by.
    
    External Functions:
        sda_return (function): A function that executes the SQL query against the Soil Data Access API.
    
    Returns:
        pd.DataFrame: Combined data as a DataFrame, or a string error message if no data are returned.
    """
    # Convert each mukey value to an ASCII string and join them with commas
    mukey_str = ",".join([str(val).encode("ascii", "ignore").decode("utf-8") for val in mukey_list])
    
    # Build the SQL query string (as a multi-line string)
    query = f"""
    SELECT
        comp.mukey,
        comp.cokey,
        ch.chkey,
        ch.hzname,
        ch.hzdept_r,
        ch.hzdepb_r,
        ch.sandtotal_r,
        ch.silttotal_r,
        ch.claytotal_r,
        ch.pi_r,
        ch.lep_r,
        ch.ec_r,
        ch.caco3_r,
        ch.om_r,
        ch.dbovendry_r,
        ch.gypsum_r,
        ch.sar_r,
        ch.cec7_r,
        ch.ecec_r,
        ch.sumbases_r,
        ch.ph1to1h2o_r,
        frag.total_fragvol_r,
        frag.fragkind,
        cons.plasticity,
        cons.stickiness,
        comp.drainagecl,
        comp.hydricrating,
        comp.taxtempcl,
        comp.frostact,
        corestr.reskind,
        corestr.resdept_r,
        corestr.reshard,
        cotax.taxminalogy,
        cm.pondfreqcl,
        cm.ponddurcl,
        cm.flodfreqcl,
        cm.floddurcl,
        muagg.wtdepannmin
    FROM CHORIZON ch
    LEFT JOIN COMPONENT comp
         ON ch.cokey = comp.cokey
    LEFT JOIN (
         SELECT chkey, SUM(f.fragvol_r) AS total_fragvol_r, f.fragkind
         FROM CHFRAGS f
         GROUP BY chkey, f.fragkind
    ) AS frag
         ON ch.chkey = frag.chkey
    LEFT JOIN CHCONSISTENCE cons
         ON ch.chkey = cons.chkey
    LEFT JOIN CORESTRICTIONS corestr
         ON comp.cokey = corestr.cokey
    LEFT JOIN COTAXFMMIN cotax
         ON comp.cokey = cotax.cokey
    LEFT JOIN (
         SELECT 
              cokey,
              MAX(monthseq) AS max_month,
              MAX(pondfreqcl) AS pondfreqcl,
              MAX(ponddurcl) AS ponddurcl,
              MAX(flodfreqcl) AS flodfreqcl,
              MAX(floddurcl) AS floddurcl
         FROM COMONTH
         GROUP BY cokey
    ) AS cm
         ON comp.cokey = cm.cokey
    LEFT JOIN MUAGGATT muagg
         ON comp.mukey = muagg.mukey
    WHERE comp.mukey IN ({mukey_str})
    ORDER BY comp.mukey, comp.cokey, ch.hzdept_r;
    """
    
    # Clean the query by removing extra whitespace/newlines
    query_clean = " ".join(query.split())
    
    # Execute the query using sda_return (assumed to be defined elsewhere)
    result = sda_return(query_clean)
    
    if result is None:
        return "SSURGO not available in this area"
    else:
        # Assume result is returned in a column named "Table" containing a nested list,
        # where the first sub-list is the header row.
        raw = result["Table"].iloc[0]
        header = raw[0]
        data = raw[1:]
        df_out = pd.DataFrame(data, columns=header)
        df_out["fragvol"] = pd.to_numeric(df_out["total_fragvol_r"], errors="coerce")
        # Group by chkey and concatenate all fragkind values (separated by a space)
        frag_agg = df_out.groupby('chkey')['fragkind'].apply(lambda x: " ".join(x.dropna())).reset_index()
        # Merge the aggregated fragkind back into the main DataFrame (dropping the original fragkind column)
        df_out = df_out.drop(columns=['fragkind', 'total_fragvol_r']).drop_duplicates(subset=['chkey'])
        df_out = df_out.merge(frag_agg, on='chkey', how='left')
        df_out.rename(columns={"sandtotal_r": "sand", "silttotal_r": "silt", "claytotal_r": "clay",
        "pi_r": "pi", "lep_r": "lep", "ec_r": "ec", "caco3_r": "caco3", "om_r": "om",
        "dbovendry_r": "db_measured", "sandtotal_r": "sand", "gypsum_r": "gypsum", "sar_r": "sar",
        "cec7_r": "cecs", "ecec_r": "ecec", "sumbases_r": "teb", "ph1to1h2o_r": "ph", "resdept_r": "rd"},
        inplace=True)
        cols_to_convert = [
            "hzdept_r", "hzdepb_r", "sand", "silt", "clay", "pi", "lep",
            "ec", "caco3", "om", "db_measured", "gypsum", "sar", "cecs",
            "ecec", "teb", "ph", "wtdepannmin", "rd"
        ]

        # Bulk density lookup table (g/cm³) based on Saxton and Rawls (2006) pedotransfer equations using soil texture and 1% OM
        bulk_density_lookup = {
            "Sand": 1.51,
            "Loamy sand": 1.53,
            "Sandy loam": 1.56,
            "Loam": 1.55,
            "Silt loam": 1.50,
            "Silt": 1.55,
            "Sandy clay loam": 1.57,
            "Clay loam": 1.47,
            "Silty clay loam": 1.38,
            "Sandy clay": 1.51,
            "Silty clay": 1.28,
            "Clay": 1.37
        }

        # Drainage class number lookup table (lowercase keys, reverse scale)
        ssurgo_drainage_to_numeric = {
            'very poorly drained': 1,
            'poorly drained': 2,
            'somewhat poorly drained': 3,
            'moderately well drained': 4,
            'well drained': 5,
            'somewhat excessively drained': 6,
            'excessively drained': 7
        }

        # PSCL numver lookup table
        pscl_to_numeric = {
            'c': 1,        # coarse
            'm': 2,        # medium
            'f': 3,        # fine
            'unknown': 0   # fallback
        }

        for col in cols_to_convert:
            df_out[col] = pd.to_numeric(df_out[col], errors='coerce')
        df_out['esp'] = (100 * (-0.0126 + 0.01475 * df_out['sar'])) / (1 + (-0.0126 + 0.01475 * df_out['sar']))
        df_out['soc'] = df_out['om'] * 0.58
        df_out['bs'] = df_out['teb'] / df_out['cecs'] * 100
        df_out['cecc'] = df_out['cecs'] / df_out['clay'] * 100
        df_out['texture'] = df_out.apply(gettt, axis=1)
        df_out['texture_class_id'] = df_out['texture'].apply(getTXT_id)
        df_out['db_ref'] = df_out['texture'].map(bulk_density_lookup)
        df_out['db'] = df_out['db_measured'] / df_out['db_ref']
        df_out['drainagecl'] = df_out['drainagecl'].str.lower().str.strip()
        df_out['drain_id'] = df_out['drainagecl'].map(ssurgo_drainage_to_numeric)
        df_out['pscl'] = df_out.apply(classify_pscl, axis=1) 
        df_out['pscl_id'] = df_out['pscl'].map(pscl_to_numeric)
        return df_out


# SDA = Soil Data Access
def sda_return(propQry):
    """
    Queries data from the USDA's Soil Data Mart (SDM) Tabular Service and returns
    it as a pandas DataFrame.
    """
    base_url = "https://sdmdataaccess.sc.egov.usda.gov/tabular/post.rest"
    request_data = {"format": "JSON+COLUMNNAME", "query": propQry}
    result = None

    try:
        response = requests.post(base_url, json=request_data, timeout=6)
        logging.info(f"{round(response.elapsed.total_seconds(), 2)}: {base_url}")
        response.raise_for_status()
        result = response.json()

        # If dictionary key "Table" is found, normalize the data and return as DataFrame
        result = pd.json_normalize(result) if "Table" in result else None

    except requests.ConnectionError as err:
        logging.error(f"USDA service: failed to connect: {err}")
    except requests.Timeout:
        logging.error("USDA service: timed out")
    except requests.RequestException as err:
        logging.error(f"USDA service: error: {err}")

    return result

