# Standard Libraries
import os
import random
import csv
import math
import struct
import sys
import json
import re
import io
import collections
from collections import OrderedDict, Counter
import urllib.request, urllib.error, urllib.parse

# Third-Party Libraries
import scipy.stats
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import colour
import skimage
import MySQLdb
from osgeo import gdal, ogr
from osgeo.gdalconst import *
import geopandas as gpd
import shapely
from shapely.geometry import Point, Polygon, shape, LinearRing
from scipy.spatial import distance
from scipy.interpolate import CubicSpline
from scipy.sparse import issparse
from sklearn.utils import validation
from sklearn.metrics import pairwise
from sklearn.metrics.pairwise import euclidean_distances

# local functions
from code import GAEZ_soilID_local_functions as loc_func

# Uncomment if needed
# from skimage import color



"""
Module IV: Agro-edaphic suitability

This module performs crop/LUT specific calculations for rainfed systems following the GAEZ approach. The land qualities are assessed in several steps involving specific procedures. The land qualities related to climate and climate-soil interactions (such as flooding regimes, soil erosion, and soil nutrient maintenance) are treated separately from those land qualities specifically related to soil properties and conditions, as reflected in the Harmonized World Soil Database and the GAEZ terrain-slope database.

Land Qualities:
  1. Climate regime (temperature, moisture, radiation) - Climatic suitability classification
  2. Flooding regime - Moisture regime analysis of water collecting sites
  3. Soil erosion - Assessment of sustainable use of sloping terrain
  4. Soil nutrient maintenance - Fallow period requirement assessment
  5. Soil physical and chemical properties - Soil suitability classification


Soil Qualities:

Soil quality will be calculated at each soil depth and averaged using appropriate depth weights.

Standard GAEZ Depth Weights:
----------------------------
Depth (cm)  |  # of Layers  |  Weighting Factors
----------- | ------------- | ------------------------
120         |       6       |  2, 1.5, 1, 0.75, 0.5, 0.25
100         |       5       |  1.75, 1.5, 1, 0.5, 0.25
80          |       4       |  1.75, 1.25, 0.75, 0.25
60          |       3       |  1.5, 1, 0.5
40          |       2       |  1.25, 0.75
20          |       1       |  1
"""

       
  
# -----------------------------------------------------------------------------------------------------
#Function to GAEZ Soil Quality Indices
def GAEZ_SQI(COMPID, CROP_ID, inputLevel, depthWt_type=1, plot_data=None):
    data = getWISE30sec_comp_data(COMPID)

    if plot_data is not None:
        #------------------------------------------------------------------------------------------------
        #------ Load in user data --------#
        # cleanup the arrays
        # Rename the columns directly when subsetting and combine some steps
        soil_df = plot_data[['texture', 'bottom', 'rfv_class']].rename(columns={"texture": "soilHorizon", "bottom": "horizonDepth", "rfv_class": "rfvDepth"}).dropna(how='all')
        
        # Add the 'bottom' column as a copy of 'horizonDepth'
        soil_df['bottom'] = soil_df['horizonDepth']
        
        # Create the 'top' column using a list comprehension with a condition
        soil_df['top'] = [0] + [int(depth) for depth in soil_df['horizonDepth'].iloc[:-1]]
        
        # Set 'horizonDepth' as the index
        soil_df.set_index('horizonDepth', inplace=True)
        
        # Handle the bedrock value
        bedrock = plot_data['bedrock_depth'][0]
        if np.isnan(bedrock):
            bedrock = 120

        # Drop rows with all NaN in 'soilHorizon' and 'rfvDepth' and reset the index if not empty
        soil_df_slice = soil_df.dropna(how='all', subset=['soilHorizon', 'rfvDepth'])
        if not soil_df_slice.empty:
            soil_df_slice.reset_index(inplace=True)

        if soil_df_slice is not None:
            #If bedrock has been recorded and the lowest soil depth associated with data is greater than bedrock, then change lowest soil depth to bedrock depth
            if bedrock is not None and soil_df_slice.bottom.iloc[-1] > bedrock:
                soil_df_slice.bottom.iloc[-1] = bedrock
                soil_df.bottom[soil_df_slice.index[-1]] = bedrock
                soil_df.reset_index(drop=True, inplace=True)
                
                # Identify and fill in missing horizons
                missing_horizons = [j for j in range(len(soil_df) - 1) if soil_df.top[j + 1] > soil_df.bottom[j]]
                for j in missing_horizons:
                    layer_add = pd.DataFrame([[None, None, None, soil_df.top[j + 1], soil_df.bottom[j]]], 
                                             columns=['soilHorizon', 'rfvDepth', 'lab_Color', 'bottom', 'top'])
                    soil_df = pd.concat([soil_df, layer_add], axis=0)
                    
                soil_df.sort_values(['top'], ascending=True, inplace=True)
                soil_df.reset_index(drop=True, inplace=True)
                soil_df.where(pd.notnull(soil_df), None, inplace=True)

            #Create index list of soil slices where user data exists
            
            # Reset index of soil_df_slice
            soil_df_slice.reset_index(drop=True, inplace=True)
            
            # Create index list of soil slices where user data exists
            pedon_slice_index = [j for i in range(len(soil_df_slice)) 
                                 for j in range(int(soil_df_slice.top[i]), int(soil_df_slice.bottom[i])) 
                                 if j < 120]
            
            # Convert soil properties to lists
            soilHorizon = soil_df.soilHorizon.tolist()
            rfvDepth = soil_df.rfvDepth.tolist()
            
            # Convert 'bottom' and 'top' columns to integer lists
            horizonDepthB = soil_df.bottom.astype(int).tolist()
            horizonDepthT = soil_df.top.astype(int).tolist()

            #Format and generate user data
            # Generate user-specified percent clay, sand, and rfv distributions
            spt = [getSand(soil) for soil in soilHorizon]
            cpt = [getClay(soil) for soil in soilHorizon]
            p_cfg = [getCF_fromClass(rfv) for rfv in rfvDepth]
            
            p_sandpct_intpl = [sand for sand, top, bottom in zip(spt, horizonDepthT, horizonDepthB) for _ in range(top, bottom)]
            p_claypct_intpl = [clay for clay, top, bottom in zip(cpt, horizonDepthT, horizonDepthB) for _ in range(top, bottom)]
            p_cfg_intpl = [cfg for cfg, top, bottom in zip(p_cfg, horizonDepthT, horizonDepthB) for _ in range(top, bottom)]


            # Length of interpolated texture and RF depth
            p_bottom_depth = pd.DataFrame({
                "cokey": [-999],
                "compname": ["sample_pedon"],
                "bottom_depth": [soil_df_slice.bottom.iloc[-1]]
            })
            
            p_sandpct_intpl = pd.Series(p_sandpct_intpl)
            p_claypct_intpl = pd.Series(p_claypct_intpl)
            p_cfg_intpl = pd.Series(p_cfg_intpl)


            #Adjust depth interval of user data
            def adjust_length(series, target_length=120):
                # If the series is longer than the target length, truncate it
                if len(series) > target_length:
                    return series.iloc[:target_length].reset_index(drop=True)
                # If the series is shorter than the target length, pad it with NaN
                elif len(series) < target_length:
                    pd_add = pd.Series([np.nan] * (target_length - len(series)))
                    return pd.concat([series, pd_add]).reset_index(drop=True)
                return series

            p_sandpct_intpl = adjust_length(p_sandpct_intpl)
            p_claypct_intpl = adjust_length(p_claypct_intpl)
            p_cfg_intpl = adjust_length(p_cfg_intpl)

            # Create a DataFrame with specified columns
            p_hz_data = pd.DataFrame({
                "compname": ["sample_pedon"] * len(p_sandpct_intpl),
                "sandpct_intpl": p_sandpct_intpl,
                "claypct_intpl": p_claypct_intpl,
                "rfv_intpl": p_cfg_intpl
            })
            
            # Drop empty data columns
            p_hz_data.dropna(axis=1, how='all', inplace=True)
            
            # Drop empty depth slices
            p_hz_data = p_hz_data[p_hz_data.index.isin(pedon_slice_index)]
            
            p_bottom = p_bottom_depth["bottom_depth"].astype(int).iloc[0]
            snd_d, hz_depb = agg_data_layer_SQI(data=p_hz_data["sandpct_intpl"], bottom=p_bottom, depth=True)
            cly_d = agg_data_layer_SQI(data=p_hz_data["claypct_intpl"], bottom=p_bottom)
            
            txt_d = [gettt(row=None, sand=s, silt=(100 - (s + c)), clay=c).lower() for s, c in zip(snd_d, cly_d)]
            txt_id = [getTXT_id(t) for t in txt_d]
            txt_grp = [getTextGroup(t) for t in txt_d]
            rf_d = agg_data_layer_SQI(data=p_hz_data["rfv_intpl"], bottom=p_bottom)
            
            # Concatenate results into the final DataFrame
            p_hz_data = pd.concat([hz_depb, pd.Series(txt_d, name="text_class"), pd.Series(txt_id, name="text_class_id"), pd.Series(txt_grp, name="PSCL"), rf_d], axis=1)
            p_hz_data.columns = ["BotDep", "text_class", "text_class_id", "PSCL", "CFRAG"]


            # This assumes that all depths start from the top and are consecutive
            #****** Need to fix how WISE and LandPKS data are integrated when they differ in the depths****************
            #depth of WISE dataset
            # Determine the lengths of both datasets
            depths_wise = len(data.index)
            depths_pedon = len(p_hz_data.index)
            
            # Truncate or expand data based on the depth comparison
            if depths_wise > depths_pedon:
                data = data.iloc[:depths_pedon, :]
            elif depths_wise < depths_pedon:
                p_hz_data = p_hz_data.iloc[:depths_wise, :]
            
            # Update data with the information from p_hz_data
            data.update(p_hz_data[['text_class', 'text_class_id', 'PSCL', 'CFRAG']])
            data['REF_DEPTH'] = bedrock

        else:
            data = data

    depths = len(data.index)
  # S0 No constraint (100%)
  # S1 Slight constraint (90%)
  # S2 Moderate constraint (70%)
  # S3 Severe constraint (50%)
  # S4 Very severe constraint (30%)
  # N  Not suitable (<10%)
  
  # determine possible input_level codes
    input_level_mapping = {
    'L': ['1', '3', '4'],
    'I': ['2', '3', '4'],
    'H': ['4', '5']
    }
    
    Input_Level_List = input_level_mapping.get(inputLevel)
    
    if Input_Level_List is None:
        return 'Please enter `inputLevel`'

 """
Standard GAEZ depth weights:
  Depth  |  # of layers  | Weighting Factors
  120    |      6        | 2, 1.5 , 1, .75, .5, .25
  100    |      5        | 1.75, 1.5 , 1, .5, .25
  80     |      4        | 1.75, 1.25 , .75, .25
  60     |      3        | 1.5, 1, .5
  40     |      2        | 1.25, .75
  20     |      1        | 1
"""
    depth_wt_mapping = {
    (1, 6): [2, 1.5, 1.0, 0.75, 0.5, 0.25],
    (1, 5): [1.75, 1.5, 1.0, 0.5, 0.25],
    (1, 4): [1.75, 1.25, 0.75, 0.25],
    (1, 3): [1.5, 1.0, 0.5],
    (1, 2): [1.25, 0.75],
    (1, 1): [1],
    (2, 6): [4.8, 0.4, 0.2, 0.2, 0.2, 0.2],
    (2, 5): [4, 0.4, 0.2, 0.2, 0.2],
    (2, 4): [3.2, 0.4, 0.2, 0.2],
    (2, 3): [2.4, 0.4, 0.2],
    (2, 2): [1.6, 0.4],
    (2, 1): [1]
    }
    
    wts = depth_wt_mapping.get((depthWt_type, depths))
    
    if wts is None:
        return 'Input data missing'


"""
Posssible 'requirement_type' inputs:
  1. 'profile'
  2. 'texture'
  3. 'terrain'
  4. 'phase'
  5. 'drainage'
"""
  # Load in crop and input specific property requirements
    #Texture requirements based on crop and input level
    texture_req = getGAEZ_requirements(CROP_ID, Input_Level_List, requirement_type = 'texture')
    #Property requirements based on crop and input level
    property_req = getGAEZ_profile_req(CROP_ID, Input_Level_List, requirement_type = 'profile')
    #Phase requirements based on crop and input level
    phase_req = getGAEZ_phase_req(CROP_ID, Input_Level_List, requirement_type = 'phase')    
    #Drainage requirements based on crop and input level
    drainage_req = getGAEZ_drainage_req(CROP_ID, Input_Level_List, requirement_type = 'drainage')    

    # calculate SQI 1-7
    SQ1_score = calculate_SQ1(data, property_req, texture_req, inputLevel, wts)
    SQ2_score = calculate_SQ2(data, property_req, texture_req, inputLevel, wts)
    SQ3_score = calculate_SQ3(data, property_req, texture_req, phase_req, wts)
    SQ4_score = calculate_SQ4(data, phase_req, drainage_req)
    SQ5_score = calculate_SQ5(data, phase_req, property_req, wts)
    SQ6_score = calculate_SQ6(data, phase_req, property_req, wts)
    SQ7_score = calculate_SQ7(data, phase_req, property_req, texture_req, wts)
    
    #Soil Rating    
    SQI_scores = calculate_soil_rating(SQ1_score, SQ2_score, SQ3_score, SQ4_score, SQ5_score, SQ6_score, SQ7_score, inputLevel, SU_name)
    return(SQI_scores)    

