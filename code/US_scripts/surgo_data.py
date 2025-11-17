import pandas as pd
import geopandas as gpd
from functools import reduce

pd.options.display.float_format = '{:.2f}'.format

def printdf(df: pd.DataFrame, num_rows: int=5, ignore_geometry: bool = True):
    if hasattr(df, 'geometry') and ignore_geometry:
        df = df[[col for col in df.columns if col!='geometry']]
    print(df.head(num_rows).to_string())

# region Resources
# [1] SSURGO v2.3.2 Metadata Tables and Columns: https://www.nrcs.usda.gov/sites/default/files/2022-08/SSURGO-Metadata-Tables-and-Columns-Report.pdf
# [2] SSURGO v2.3.2 Metadata Table Column Descriptions: https://www.nrcs.usda.gov/sites/default/files/2022-08/SSURGO-Metadata-Table-Column-Descriptions-Report.pdf
# [3] GAEZ v4 Model Documentation: https://openknowledge.fao.org/items/039f7ec9-98af-49e1-8d24-850122c69bef
# [4] gSSURGO Value Added Look Up Table 'Valu1' Metadata: https://www.nrcs.usda.gov/sites/default/files/2022-08/gSSURGO%20Value%20Added%20Look%20Up%20Valu1%20Table%20Column%20Descriptions.pdf
# [5] gSSURGO data c/o Box: https://www.nrcs.usda.gov/resources/data-and-reports/gridded-soil-survey-geographic-gssurgo-database
# endregion

# region Data at a glance

# Load main datasets
gdb_file = 'data/gSSURGO_CONUS.gdb'  # downloaded from [5]
layers = gpd.list_layers(gdb_file)

map_units = gpd.read_file(gdb_file, layer="mapunit")
components = gpd.read_file(gdb_file, layer="component")  # p. 31 of [1] and p. 35 of [2]
horizons = gpd.read_file(gdb_file, layer="chorizon")  # p. 5 of [1] and p. 5 of [2]

# Uniqueness
ids_cols = ['mukey', 'cokey', 'chkey']

map_units.filter(ids_cols).nunique()
components.filter(ids_cols).nunique()
horizons.filter(ids_cols).nunique()
# endregion

# region Attributes

# GAEZ methodology for soil qualities
gaez_attributes_sq1or2 = [  # nutrient availability (low inputs) / retention (high inputs)
    'texture_usda', 'pH',  # either
    'total_exchangeable_bases_cmolkg', 'organic_carbon_%',  # low inputs
    'base_saturation_%', 'cec_soil_cmolkg', 'cec_clay_cmolkg'  # high inputs
]
gaez_attributes_sq3 = [  # rooting conditions
    'texture_usda', 'gravel_%',  # measured
    'obstacles_yn', 'gelic_yn', 'vetric_yn', 'petric_yn', 'reference_soil_depth_cm', 'soil_phase'   # derived from other attributes?
]
gaez_attributes_sq4 = [  # oxygen availability
    'reference_drainage_class', 'soil_phase'  # derived from other attributes?
]
gaez_attributes_sq5 = [  # presence of salinity and sodicity
    'ec_dSm', 'esp_%',  # measured
    'soil_phase'  # derived from other attributes?
]
gaez_attributes_sq6 = [  # presence of lime and gypsum
    'caco3_%', 'gypsum_%',  # measured
    'soil_phase'  # derived from other attributes?
]
gaez_attributes_sq7 = [  # workability
    'texture_usda', 'gravel_%',  # measured
    'vetric_yn', 'reference_soil_depth_cm', 'soil_phase'  # derived from other attributes?
]

gaez_attributes_for_wgtavg = [
    'rooting_limit_cm', 'topsoil_thickness_cm'  # derived from other attributes?
]

# all attributes among all soil qualities (SQ)
gaez_attributes = list(set(gaez_attributes_sq1or2 + gaez_attributes_sq3 + gaez_attributes_sq4 +
                       gaez_attributes_sq5 + gaez_attributes_sq6 + gaez_attributes_sq7 + gaez_attributes_for_wgtavg))

# other attributes of interest
other_site_attributes = [  # these may also be pulled/updated from external bioclimatic (WorldClim) and topography datasets (SRTM)
    'slope', 'aspect_deg', 'elevation_m', 'geomorphology',
    'albedo_ratio', 'temperature_degC', 'precipitation_mm', 'frost_free_days'
]

all_attributes = gaez_attributes + other_site_attributes
print("Soil and site attributes for model:", all_attributes)
# todo: are there other attributes of interest that are not listed here?


# In data:
soil_attributes_in_tables = {
    'component': {
        'drainagecl': 'reference_drainage_class',
        'slope_r': 'slope',
        'elev_r': 'elevation_m',
        'aspectrep': 'aspect_deg',
        'geomdesc': 'geomorphology',
        'albedodry_r': 'albedo_ratio',
        'airtempa_r': 'temperature_degC',
        'map_r': 'precipitation_mm',
        'ffd_r': 'frost_free_days'
    },
    'chorizon': {
        'hzname': 'horizon_name',
        'hzdept_r': 'top_of_horizon_depth_cm',
        'hzdepb_r': 'bottom_of_horizon_depth_cm',
        'caco3_r': 'caco3_%',
        'cec7_r': 'cec_soil_cmolkg',  # given in meq/100g units, which is equivalent to cmol/kg
        'claytotal_r': 'clay_%',  # needed to calculate cec_clay
        'ec_r': 'ec_dSm',
        'sar_r': 'sar',  # needed to calculated esp
        'gypsum_r': 'gypsum_%',
        'ph1to1h2o_r': 'pH',
        'sumbases_r': 'total_exchangeable_bases_cmolkg',
    },
    'chtexture': {
        'texcl': 'texture_usda',
        'chtgkey': 'chtgkey'  # needed to merge with chtexturegrp
    },
    'chtexturegrp': {
        'rvindicator': 'representative_yn',  # needed to reduce dimensionality of dataset
        'chtgkey': 'chtgkey'  # needed to merge with chtexture
    },
    'chfrags': {
        'fragvol_r': 'fragment_vol_%_by_size',  # needed to calculate gravel_%
        'fragsize_r': 'fragment_size_mm'  # needed to interpret fragment volume
    }
}
# endregion

# region Load and clean attribute data
def load_attributes_from_table(table_name):
    soil_attributes = soil_attributes_in_tables[table_name]
    columns_to_pull = ids_cols + list(soil_attributes.keys())
    data = gpd.read_file(gdb_file, layer=table_name, columns=columns_to_pull)
    data = data.filter(columns_to_pull)
    data.rename(columns=soil_attributes, inplace=True)
    return data

# Site attributes:
site_attributes = load_attributes_from_table('component')
# todo: seems that most of the time values (other than reference drainage class) appear once per map unit (mukey), so:
#       can missing data for slope, aspect, albedo, temp, precip, and frost free days be imputed from components in same map unit?
#       what to do in cases where these values differ for components in same map unit (e.g. mukey == 74983)?
#       how to impute missing data for reference drainage class and geomorphology, which do appear more specific to component than map unit?

# Soil attributes:
chtexture_datasets = [load_attributes_from_table(name) for name in ['chtexture', 'chtexturegrp']]
chtexture = reduce(lambda df1, df2: pd.merge(df1, df2, on=['chtgkey'], how='outer'), chtexture_datasets)

chtexture['representative_bool'] = chtexture['representative_yn'] == "Yes"
chtexture['num_rep_flags'] = chtexture.groupby('chkey')['representative_bool'].transform('sum')
chtexture = pd.concat([
    chtexture[chtexture['representative_yn'] == "Yes"],  # filter to representative textures,
    chtexture[chtexture['num_rep_flags'] == 0]  # but keep components that have no representative texture
    ])
chtexture['texture_usda'] = chtexture['texture_usda'].str.replace(" ", "").str.lower()  # standardize values
chtexture['texture_usda'] = chtexture['texture_usda'].str.replace(r'fine|very|coarse', '', regex=True)  # remove modifiers not used in GAEZ
chtexture['texture_usda'].unique()  # class 'heavy clay (Ch)' not represented in data (pg. 83 of [3])
chtexture.drop_duplicates(subset=['chkey', 'texture_usda'], inplace=True)  # remove duplicates based on simplified texture classes
chtexture = chtexture.sample(frac=1, random_state=12).reset_index(drop=True)  # choose random obs of remaining duplicates (differentation bw categories may be coarse enough that choice does not matter)
chtexture.drop_duplicates(subset=['chkey'], inplace=True)
# todo: confirm approach to reduce data to one texture observation per component is appropriate
# todo: is it also interesting to include sand, clay, silt fractions individually, too?


chfrag = load_attributes_from_table('chfrags')
chfrag.drop_duplicates(inplace=True)
chfrag = chfrag.groupby('chkey')['fragment_vol_%_by_size'].sum().rename('gravel_%').reset_index()
# todo: was it correct to sum fragvol by component?
#       it appears that fragment volume is given for different fragment sizes,
#       but results (n=34) in some total gravel percents greater than 100%


chorizon = load_attributes_from_table('chorizon')

chorizon['cec_clay_cmolkg'] = chorizon['cec_soil_cmolkg']/chorizon['clay_%'] * 100
# todo: is this the correct way to derive clay CEC from soil CEC and clay fraction?
#       when clay_% equals 0 this equation doesn't make sense b/c it assumes that clay is the only contributor to CEC in soil, disregarding the role of organic matter?
#       so, should it be dependent on fraction of organic carbon too?
#       and, should ignore observations where cec_soil > 0 but clay_% == 0 and cec_clay = inf?

chorizon['base_saturation_%'] = chorizon['total_exchangeable_bases_cmolkg'] / chorizon['cec_soil_cmolkg'] * 100
# todo: is this the correct way to derive base saturation from CEC and TEB?
#       how to interpret values > 100%?
#       if CEC soil == 0 does BS just equal TEB? or 0% or 100%

chorizon['esp_%'] = (100 * (-0.0126 + 0.01475 * chorizon['sar'])) / (1 + (-0.0126 + 0.01475 * chorizon['sar']))
# todo: is this the correct way to derive ESP from SAR? the correct cofficients to use?
#       how to interpret esp_% values < 0%? censor to zero?
# Richards (1954). Diagnosis and Improvement of Saline and Alkali Soils. p. 26
# https://books.google.com/books?hl=en&lr=&id=MMYc9CcSwzAC
# ESR = -0.0126 + 0.01475 * SAR
# ESP = (ESR * 100) / (1 + ESR)

horizon_id_cols = ['horizon_name', 'top_of_horizon_depth_cm', 'bottom_of_horizon_depth_cm']
soil_attributes = reduce(lambda df1, df2: pd.merge(df1, df2, on=['chkey'], how='outer'),
                         [chorizon, chtexture, chfrag])
soil_attributes = soil_attributes.filter(ids_cols + horizon_id_cols + gaez_attributes)
soil_attributes.sort_values(['cokey', 'top_of_horizon_depth_cm'], inplace=True)
printdf(soil_attributes.describe(), 15)
# todo: some values are outside of logical range (e.g. >100%, inf), see specific questions above on how to resolve these

# Master dataset, site and soil attributes
data = soil_attributes.merge(site_attributes, how='left', on='cokey')
printdf(data)

print("Attributes not found in data:", set(all_attributes) - set(data.columns))
# todo: how to derive these from gSSURGO data?
#       {'topsoil_thickness_cm', 'soil_phase', 'organic_carbon_%', 'petric_yn', 'gelic_yn', 'vetric_yn', 'reference_soil_depth_cm', 'obstacles_yn', 'rooting_limit_cm'}
#       SOC (g/m2) and root zone depth (cm) are in valu1 table [4], which are weighted averages of components by map unit so:
#       how to derive this information on a per component basis? or is it appropriate to assume all components in map unit share same values?
# valu1 = gpd.read_file(gdb_file, layer="valu1")

# endregion

# region Investigate geometry
print(layers[layers['geometry_type'].notnull()])
# of all layers with geometry MUPOLYGON appears to be the only one that maps to key in data and is complete
# there are a total of 319,598 polygons (vs 320,070 unique map units in tables)
mapunit_polys = gpd.read_file(gdb_file, layer="MUPOLYGON", rows=50)  # load a subset
printdf(mapunit_polys)
# todo: is there latitude/longitude for components?
#       otherwise how did slope, elev, aspect, temp, precip, etc. get measured for each component? see components table above
#       these also seem to relate to variables in 'components' table of NASIS data - so can we take point data from there?

# endregion

# region Investigate missingness

# Prevalence of missing data
non_null_percents = (~data.isnull()).sum()/len(data)
print(non_null_percents)

print("Missingness > 25%:\n", non_null_percents[non_null_percents < 0.75])
# todo: is there a better/other way to derive/measure these variables, in particular, as the ones with the most missingness?
#       e.g. aspect_deg can be taken from a DEM
#       if the are missing, are they irrelevant to that soil?


# Subset: complete data on all (known) attributes
total_components_raw = data['cokey'].nunique()
data_complete_attributes = data.dropna(axis='rows', how='any',
                                       subset=set(all_attributes).intersection(set(data.columns)))
n_components_complete_attributes = data_complete_attributes['cokey'].nunique()

# Subset: complete data on SQ1/2 (nutrient availability) attributes
# todo: however missing any data on organic carbon!
data_sq1or2_attributes = data.dropna(axis='rows', how='any',
                                       subset=set(gaez_attributes_sq1or2).intersection(set(data.columns)))
n_components_sq1or2_attributes = data_sq1or2_attributes['cokey'].nunique()

# Subset: complete data on all (known) attributes and no gaps in depth up to 112 cm
def filter_data_by_depth(df, max_depth):
    max_depth = 112
    complete_depths = df.groupby('cokey').filter(
        lambda df: (df.top_of_horizon_depth_cm.notna().all()) & (df.bottom_of_horizon_depth_cm.notna().all()))
    complete_depths = complete_depths.groupby('cokey').filter(
        lambda df: (df.top_of_horizon_depth_cm.min() == 0) & (df.bottom_of_horizon_depth_cm.max() >= max_depth))
    complete_depths = complete_depths.groupby('cokey').filter(
        lambda df: ~((df.top_of_horizon_depth_cm.shift(-1) - df.bottom_of_horizon_depth_cm) > 0).any())
    return complete_depths

data_complete = filter_data_by_depth(data_complete_attributes, 112)
n_components_complete = data_complete['cokey'].nunique()

data_complete_sq1or2 = filter_data_by_depth(data_sq1or2_attributes, 112)
n_components_complete_sq1or2 = data_complete_sq1or2['cokey'].nunique()

# Summarize
list_of_samples_sizes = [total_components_raw, n_components_complete_attributes, n_components_sq1or2_attributes,
                     n_components_complete, n_components_complete_sq1or2]
print(pd.DataFrame({
    'subset': ['raw', 'complete_attributes', 'complete_sq1or2_attributes', 'complete_with_depth', 'complete_sq1or2_with_depth'],
    'n_components': list_of_samples_sizes,
    'pct_of_raw': [round( n / total_components_raw * 100, 1) for n in list_of_samples_sizes]
}))
# endregion
