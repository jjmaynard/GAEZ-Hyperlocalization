# -----------------------------------------------------------------------------------------------------
# Function to GAEZ Soil Quality Indides
import pandas as pd
import numpy as np
import rasterio

# import local functions
import GAEZ_SQI_functions
import gaez_config


def process_plot_data(plot_data, map_data):
    """
    Process user-provided plot data to clean, reformat, and interpolate soil properties,
    then update the 'map_data' DataFrame with the calculated soil property columns and drainage class.
    
    Parameters:
        plot_data (DataFrame): User-provided soil profile data containing columns such as 
                               'texture', 'bottom', 'rfv_class', 'bedrock_depth', 'longitude', 
                               and 'latitude'.
        map_data (DataFrame): Existing soil data that will be updated with new columns.
    
    Returns:
        DataFrame: The updated 'map_data' DataFrame with added soil property information.
    """
    if plot_data is not None:
        # -----------------------------------------------
        # Load and clean up the user data
        soil_df = plot_data[['texture', 'bottom', 'rfv_class']].copy()
        soil_df.columns = ["soilHorizon", "horizonDepth", "rfvDepth"]
        soil_df = soil_df.dropna(how='all')
        soil_df['bottom'] = soil_df.horizonDepth
        soil_df = soil_df.where(pd.notnull(soil_df), None)
        
        # Create a 'top' column from horizon depths
        top = []
        hzIdx = len(soil_df) - 1
        top.append(0)
        for i in range(0, hzIdx + 1):
            if i < hzIdx:
                top.append(int(soil_df.horizonDepth.iloc[i]))
        soil_df['top'] = top
        soil_df = soil_df.set_index('horizonDepth')
        
        # Determine bedrock depth; default to 200 if not provided
        bedrock = plot_data['bedrock_depth'].iloc[0]
        if np.isnan(bedrock):
            bedrock = 200
        
        # Drop rows where all horizon variables are missing
        soil_df_slice = soil_df.dropna(how='all', subset=['soilHorizon', 'rfvDepth'])
        if soil_df_slice.empty:
            soil_df_slice = None
        else:
            soil_df_slice['index'] = soil_df_slice.index
            soil_df_slice = soil_df_slice.reset_index(drop=True)
            soil_df_slice = soil_df_slice.set_index('index')
        
        if soil_df_slice is not None:
            # If the recorded bedrock is shallower than the lowest measured horizon, adjust the bottom depth.
            if bedrock is not None and soil_df_slice.bottom.iloc[-1] > bedrock:
                soil_df_slice.bottom.iloc[-1] = bedrock
                soil_df.bottom.iloc[soil_df_slice.index[-1]] = bedrock
                soil_df = soil_df.reset_index(drop=True)
                # Infill missing horizons (if a gap exists between 'top' and 'bottom')
                for j in range(len(soil_df)):
                    if j == len(soil_df) - 1:
                        break
                    if soil_df.top.iloc[j + 1] > soil_df.bottom.iloc[j]:
                        layer_add = pd.DataFrame(
                            [[None, None, None, soil_df.top.iloc[j + 1], soil_df.bottom.iloc[j]]],
                            columns=['soilHorizon', 'rfvDepth', 'lab_Color', 'bottom', 'top']
                        )
                        soil_df = pd.concat([soil_df, layer_add], axis=0)
                        soil_df = soil_df.sort_values('top', ascending=True)
                        soil_df = soil_df.reset_index(drop=True)
                soil_df = soil_df.where(pd.notnull(soil_df), None)
            
            # Create an index list of soil slices (depths) where user data exists
            soil_df_slice = soil_df_slice.reset_index(drop=True)
            pedon_slice_index = []
            for i in range(len(soil_df_slice)):
                for j in range(int(soil_df_slice.top.iloc[i]), int(soil_df_slice.bottom.iloc[i])):
                    pedon_slice_index.append(j)
            pedon_slice_index = [x for x in pedon_slice_index if x < 200]
            
            # Convert soil properties to lists
            soilHorizon = soil_df.soilHorizon.tolist()
            rfvDepth = soil_df.rfvDepth.tolist()
            horizonDepthB = [int(x) for x in soil_df.bottom.tolist()]
            horizonDepthT = [int(x) for x in soil_df.top.tolist()]
            
            # Generate user-specified percent sand, clay, and rfv distributions using helper functions
            spt, cpt, p_cfg = [], [], []
            p_sandpct_intpl, p_claypct_intpl, p_cfg_intpl = [], [], []
            for i in range(len(soilHorizon)):
                spt.append(getSand(soilHorizon[i]))
                cpt.append(getClay(soilHorizon[i]))
                p_cfg.append(getCF_fromClass(rfvDepth[i]))
            for i in range(len(soilHorizon)):
                for j in range(horizonDepthT[i], horizonDepthB[i]):
                    p_sandpct_intpl.append(spt[i])
                    p_claypct_intpl.append(cpt[i])
                    p_cfg_intpl.append(p_cfg[i])
            
            # Create a DataFrame for the bottom depth of the profile
            p_bottom_depth = pd.DataFrame([[-999, "sample_pedon", soil_df_slice.bottom.iloc[-1]]],
                                          columns=["cokey", "compname", "bottom_depth"])
            
            p_sandpct_intpl = pd.Series(p_sandpct_intpl)
            p_claypct_intpl = pd.Series(p_claypct_intpl)
            p_cfg_intpl = pd.Series(p_cfg_intpl)
            
            # Ensure each interpolated property series has exactly 200 rows
            for series in [(p_sandpct_intpl, 'sand'), (p_claypct_intpl, 'clay'), (p_cfg_intpl, 'rfv')]:
                s, name = series
                if len(s) > 200:
                    s = s.iloc[0:200].reset_index(drop=True)
                else:
                    Na_add = 200 - len(s)
                    s = pd.concat([s, pd.Series([np.nan] * Na_add)]).reset_index(drop=True)
                if name == 'sand':
                    p_sandpct_intpl = s
                elif name == 'clay':
                    p_claypct_intpl = s
                else:
                    p_cfg_intpl = s
            
            p_compname = pd.Series(["sample_pedon"] * len(p_sandpct_intpl))
            p_hz_data = pd.concat([p_compname, p_sandpct_intpl, p_claypct_intpl, p_cfg_intpl], axis=1)
            p_hz_data.columns = ["compname", "sandpct_intpl", "claypct_intpl", "rfv_intpl"]
            
            # Drop completely empty columns and select only the rows corresponding to the profile depth
            p_hz_data = p_hz_data.loc[:, ~p_hz_data.isnull().all()]
            p_hz_data = p_hz_data[p_hz_data.index.isin(pedon_slice_index)]
            
            p_bottom = int(p_bottom_depth["bottom_depth"].iloc[0])
            snd_d, hz_depb = agg_data_layer_SQI(data=p_hz_data["sandpct_intpl"], bottom=p_bottom, depth=True)
            cly_d = agg_data_layer_SQI(data=p_hz_data["claypct_intpl"], bottom=p_bottom)
            rf_d = agg_data_layer_SQI(data=p_hz_data["rfv_intpl"], bottom=p_bottom)
            
            # Determine soil textural class for each layer using the gettt function
            txt_d = []
            for l in range(len(snd_d)):
                text_T = gettt(row=None, sand=snd_d.iloc[l],
                               silt=(100 - (snd_d.iloc[l] + cly_d.iloc[l])),
                               clay=cly_d.iloc[l])
                txt_d.append(text_T.lower())
            txt_d = pd.Series(txt_d)
            txt_d.index = snd_d.index
            
            # Map textural class to additional identifiers using helper functions
            txt_id = pd.Series([getTXT_id(txt_d.iloc[l]) for l in range(len(txt_d))], index=snd_d.index)
            txt_grp = pd.Series([getTextGroup(txt_d.iloc[l]) for l in range(len(txt_d))], index=snd_d.index)
            txt_grp_id = pd.Series([getTextGroup_id(txt_d.iloc[l]) for l in range(len(txt_d))], index=snd_d.index)
            
            p_hz_data = pd.concat([hz_depb, txt_d, txt_id, txt_grp, txt_grp_id, rf_d], axis=1)
            p_hz_data.columns = ["BotDep", "text_class", "text_class_id", "PSCL", "PSCL_ID", "CFRAG"]
            
            # Adjust the depth intervals to match the provided 'map_data' DataFrame.
            depths_wise = len(map_data.index)
            depths_pedon = len(p_hz_data.index)
            if depths_wise > depths_pedon:
                map_data = map_data.iloc[0:depths_pedon, :]
            elif depths_wise < depths_pedon:
                p_hz_data = p_hz_data.iloc[0:depths_wise, :]
            
            # Update the 'map_data' DataFrame with the new soil properties
            map_data = map_data.assign(
                text_class=p_hz_data['text_class'].values,
                text_class_id=p_hz_data['text_class_id'].values,
                PSCL=p_hz_data['PSCL'].values,
                CFRAG=p_hz_data['CFRAG'].values,
                REF_DEPTH=bedrock
            )
            
            # Recalculate soil drainage class by retrieving slope data from a DEM
            olm_250_slope = "/vsicurl/https://s3.eu-central-1.wasabisys.com/openlandmap/layers250m/dtm_slope_merit.dem_m_250m_s0..0cm_2017_v1.0.tif"
            coords = [(plot_data['longitude'].iloc[0], plot_data['latitude'].iloc[0])]
            with rasterio.open(olm_250_slope) as ds:
                for val in rasterio.sample.sample_gen(ds, coords):
                    slope = val  # Use the retrieved slope value as needed
        
        else:
            # If no valid soil slice data exists, return the unmodified map_data
            pass
    
    return map_data


def process_site_data(site_data, map_data):
    """
    Process site-level data to update the 'map_data' DataFrame with site-specific attributes.

    Parameters:
        site_data (DataFrame): DataFrame containing site-level data with columns such as 
                               'latitude', 'longitude', and 'bedrock_depth'.
        map_data (DataFrame): Existing DataFrame representing map data that will be updated 
                              with the processed site information.

    Returns:
        DataFrame: The updated 'map_data' DataFrame with site attributes incorporated.
    """
    if site_data is not None:
        # Extract site coordinates and bedrock depth
        latitude = site_data['latitude'].iloc[0]
        longitude = site_data['longitude'].iloc[0]
        bedrock = site_data['bedrock_depth'].iloc[0]
        if np.isnan(bedrock):
            bedrock = 200  # default value if bedrock depth is not provided

        # Update map_data with site-level attributes
        map_data = map_data.assign(
            latitude=latitude,
            longitude=longitude,
            bedrock_depth=bedrock
        )

        # Retrieve slope data from a DEM file (for example, using OpenLandMap's 250m slope dataset)
        olm_250_slope = "/vsicurl/https://s3.eu-central-1.wasabisys.com/openlandmap/layers250m/dtm_slope_merit.dem_m_250m_s0..0cm_2017_v1.0.tif"
        coords = [(longitude, latitude)]
        with rasterio.open(olm_250_slope) as ds:
            for val in rasterio.sample.sample_gen(ds, coords):
                slope = val[0]  # Assume the sample returns an array; extract the first element

        # Update map_data with the retrieved slope value
        map_data = map_data.assign(slope=slope)
    
    return map_data


def process_lab_data(lab_data, map_data):
    """
    Process laboratory data to clean, reformat, and interpolate lab measurements,
    then update the 'map_data' DataFrame with lab-derived soil properties.
    
    Parameters:
        lab_data (DataFrame): DataFrame containing lab data with columns such as
                              'OC', 'pH', 'TEB', 'BS', 'ECEC', 'CECc', 'ESP', 'bottom', 'texture',
                              and 'bedrock_depth'.
        map_data (DataFrame): Existing DataFrame representing map data that will be updated
                              with lab soil property information.
    
    Returns:
        DataFrame: The updated 'map_data' DataFrame with added lab soil property information.
    """
    if lab_data is not None:
        # -------------------------------
        # Load and clean up the lab data
        lab_df = lab_data[['OC', 'pH', 'TEB', 'BS', 'ECEC', 'CECc', 'ESP', 'bottom', 'texture']].copy()
        lab_df.columns = ['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP', 'bottom', 'texture']
        lab_df = lab_df.dropna(how='all')
        lab_df = lab_df.where(pd.notnull(lab_df), None)
        
        # Create 'top' column from the bottom depths
        top = []
        hzIdx = len(lab_df.bottom) - 1
        top.append(0)
        for i in range(0, hzIdx + 1):
            if i < hzIdx:
                top.append(int(lab_df.bottom.iloc[i]))
        lab_df['top'] = top
        
        # Create a depth index and set it as the DataFrame index
        lab_df['depth_index'] = lab_df.bottom
        lab_df = lab_df.set_index('depth_index')
        
        # Set bedrock depth (default to 200 if not provided)
        bedrock = lab_data['bedrock_depth'].iloc[0]
        if np.isnan(bedrock):
            bedrock = 200
        
        # Drop rows where all key lab measurements are missing
        lab_df_slice = lab_df.dropna(how='all', subset=['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP', 'texture'])
        if lab_df_slice.empty:
            lab_df_slice = None
        else:
            lab_df_slice['index'] = lab_df_slice.index
            lab_df_slice = lab_df_slice.reset_index(drop=True)
            lab_df_slice = lab_df_slice.set_index('index')
        
        if lab_df_slice is not None:
            # Adjust the lowest horizon if its bottom exceeds the bedrock depth
            if bedrock is not None and lab_df_slice.bottom.iloc[-1] > bedrock:
                lab_df_slice.bottom.iloc[-1] = bedrock
                lab_df.bottom.iloc[lab_df_slice.index[-1]] = bedrock
                lab_df = lab_df.reset_index(drop=True)
                # Infill missing horizons between recorded depths
                for j in range(len(lab_df)):
                    if j == len(lab_df) - 1:
                        break
                    if lab_df.top.iloc[j + 1] > lab_df.bottom.iloc[j]:
                        layer_add = pd.DataFrame(
                            [[None, None, None, None, None, None, None, lab_df.top.iloc[j + 1], None, lab_df.bottom.iloc[j]]]
                        )
                        layer_add.columns = ['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP', 'top', 'texture', 'bottom']
                        lab_df = pd.concat([lab_df, layer_add], axis=0)
                        lab_df = lab_df.sort_values('top', ascending=True)
                        lab_df = lab_df.reset_index(drop=True)
                lab_df = lab_df.where(pd.notnull(lab_df), None)
            
            # Create an index list of depth slices where lab data exist
            lab_df_slice = lab_df_slice.reset_index(drop=True)
            pedon_slice_index = []
            for i in range(len(lab_df_slice)):
                for j in range(int(lab_df_slice.top.iloc[i]), int(lab_df_slice.bottom.iloc[i])):
                    pedon_slice_index.append(j)
            pedon_slice_index = [x for x in pedon_slice_index if x < 200]
            
            # Convert lab properties to lists
            OC = lab_df.OC.tolist()
            pH_vals = lab_df.pH.tolist()
            TEB = lab_df.TEB.tolist()
            BS = lab_df.BS.tolist()
            CECs = lab_df.CECs.tolist()
            CECc = lab_df.CECc.tolist()
            ESP = lab_df.ESP.tolist()
            
            horizonDepthB = [int(x) for x in lab_df.bottom.tolist()]
            horizonDepthT = [int(x) for x in lab_df.top.tolist()]
            
            # Interpolate lab data: generate a distribution over each depth interval
            p_OC_intpl = []
            p_pH_intpl = []
            p_TEB_intpl = []
            p_BS_intpl = []
            p_CECs_intpl = []
            p_CECc_intpl = []
            p_ESP_intpl = []
            
            for i in range(len(OC)):
                for j in range(horizonDepthT[i], horizonDepthB[i]):
                    p_OC_intpl.append(OC[i])
                    p_pH_intpl.append(pH_vals[i])
                    p_TEB_intpl.append(TEB[i])
                    p_BS_intpl.append(BS[i])
                    p_CECs_intpl.append(CECs[i])
                    p_CECc_intpl.append(CECc[i])
                    p_ESP_intpl.append(ESP[i])
            
            # Create a DataFrame for bottom depth information
            p_bottom_depth = pd.DataFrame([[-999, "sample_pedon", lab_df_slice.bottom.iloc[-1]]],
                                          columns=["cokey", "compname", "bottom_depth"])
            
            # Convert interpolated lists to Series
            p_OC_intpl = pd.Series(p_OC_intpl)
            p_pH_intpl = pd.Series(p_pH_intpl)
            p_TEB_intpl = pd.Series(p_TEB_intpl)
            p_BS_intpl = pd.Series(p_BS_intpl)
            p_CECs_intpl = pd.Series(p_CECs_intpl)
            p_CECc_intpl = pd.Series(p_CECc_intpl)
            p_ESP_intpl = pd.Series(p_ESP_intpl)
            
            # Ensure each interpolated series has exactly 200 values
            def adjust_series(s):
                if len(s) > 200:
                    return s.iloc[0:200].reset_index(drop=True)
                else:
                    Na_add = 200 - len(s)
                    pd_add = pd.Series([np.nan] * Na_add)
                    return pd.concat([s, pd_add]).reset_index(drop=True)
            
            p_OC_intpl = adjust_series(p_OC_intpl)
            p_pH_intpl = adjust_series(p_pH_intpl)
            p_TEB_intpl = adjust_series(p_TEB_intpl)
            p_BS_intpl = adjust_series(p_BS_intpl)
            p_CECs_intpl = adjust_series(p_CECs_intpl)
            p_CECc_intpl = adjust_series(p_CECc_intpl)
            p_ESP_intpl = adjust_series(p_ESP_intpl)
            
            p_compname_lab = pd.Series(["sample_pedon"] * len(p_OC_intpl))
            p_lab_data = pd.concat([p_compname_lab, p_OC_intpl, p_pH_intpl, p_TEB_intpl, p_BS_intpl,
                                    p_CECs_intpl, p_CECc_intpl, p_ESP_intpl], axis=1)
            p_lab_data.columns = ["compname", "OC_intpl", "pH_intpl", "TEB_intpl", "BS_intpl", 
                                   "CECs_intpl", "CECc_intpl", "ESP_intpl"]
            
            # Drop columns that are completely empty and keep only rows corresponding to lab data depth
            p_lab_data = p_lab_data.loc[:, ~p_lab_data.isnull().all()]
            p_lab_data = p_lab_data[p_lab_data.index.isin(pedon_slice_index)]
            
            # Get the bottom depth as an integer
            p_bottom = int(p_bottom_depth["bottom_depth"].astype(int).iloc[0])
            
            # Aggregate lab data over depth using a helper function (assumed defined elsewhere)
            oc_d, hz_depb = agg_data_layer_SQI(data=p_lab_data["OC_intpl"], bottom=p_bottom, depth=True)
            ph_d = agg_data_layer_SQI(data=p_lab_data["pH_intpl"], bottom=p_bottom)
            teb_d = agg_data_layer_SQI(data=p_lab_data["TEB_intpl"], bottom=p_bottom)
            bs_d = agg_data_layer_SQI(data=p_lab_data["BS_intpl"], bottom=p_bottom)
            cecs_d = agg_data_layer_SQI(data=p_lab_data["CECs_intpl"], bottom=p_bottom)
            cecc_d = agg_data_layer_SQI(data=p_lab_data["CECc_intpl"], bottom=p_bottom)
            esp_d = agg_data_layer_SQI(data=p_lab_data["ESP_intpl"], bottom=p_bottom)
            
            p_lab_data = pd.concat([hz_depb, oc_d, ph_d, teb_d, bs_d, cecs_d, cecc_d, esp_d], axis=1)
            p_lab_data.columns = ["BotDep", "OC", "pH", "TEB", "BS", "CECs", "CECc", "ESP"]
            
            # Adjust the depth intervals of lab data to match map_data
            depths_wise = len(map_data.index)
            depths_pedon = len(p_lab_data.index)
            if depths_wise > depths_pedon:
                map_data = map_data.iloc[0:depths_pedon, :]
            elif depths_wise < depths_pedon:
                p_lab_data = p_lab_data.iloc[0:depths_wise, :]
            
            # Update map_data with lab soil properties
            map_data = map_data.assign(
                ORGC=p_lab_data['OC'].values,
                PHAQ=p_lab_data['pH'].values,
                TEB=p_lab_data['TEB'].values,
                BSAT=p_lab_data['BS'].values,
                CECS=p_lab_data['CECs'].values,
                CECc=p_lab_data['CECc'].values,
                ESP=p_lab_data['ESP'].values
            )
    
    return map_data
