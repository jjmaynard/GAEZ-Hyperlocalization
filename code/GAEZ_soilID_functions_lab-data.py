import os, random, collections, operator
import csv, math, struct, sys
import scipy.stats
import colour
import math
from math import radians, cos, sin, asin, sqrt
import json

import numpy as np
import pandas as pd
import skimage
import re
import urllib.request, urllib.error, urllib.parse
from scipy.spatial import distance
from scipy.interpolate import CubicSpline
from sklearn.utils import validation
from sklearn.metrics import pairwise
from sklearn.metrics.pairwise import euclidean_distances
from scipy.sparse import issparse

from pandas.io.json import json_normalize
#from skimage import color
from collections import OrderedDict
from collections import Counter
import MySQLdb
import io

from osgeo import gdal, ogr
from osgeo.gdalconst import *
import geopandas as gpd
import shapely
from shapely.geometry import Point, Polygon, shape, LinearRing
import rasterio

#####################################################################################################
#                                       back-end functions                                            #
#####################################################################################################
def getDataStore_Connection():
    try:
        HOST = '127.0.0.1'
        USER = 'root'
        PASSWORD = 'root'
        DATABASE = 'apex'
        conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE)
        return conn
    except Exception as err:
        print(err)
        sys.exit(str(err))

# def findSoilLocation(lon, lat):
# 
#     drv_h = ogr.GetDriverByName("ESRI Shapefile")
#     ds_in_h = drv_h.Open("C:/LandPKS_API_SoilID-master/global/HWSD_global_noWater_no_country.shp", 0)
#     lyr_in_h = ds_in_h.GetLayer(0)
# 
#     drv_us = ogr.GetDriverByName("ESRI Shapefile")
#     ds_in_us = drv_us.Open("C:/LandPKS_API_SoilID-master/global/SoilID_US_Areas.shp", 0)
#     lyr_in_us = ds_in_us.GetLayer(0)
# 
#     geo_rf = lyr_in_h.GetSpatialRef()
#     pt_rf = ogr.osr.SpatialReference()
#     pt_rf.ImportFromEPSG(4326)
#     ctran = ogr.osr.CoordinateTransformation(pt_rf, geo_rf)
# 
#     #Transform coordinate system of input point
#     [lon, lat, z] = ctran.TransformPoint(lon, lat)
# 
#     pt = ogr.Geometry(ogr.wkbPoint)
#     pt.SetPoint_2D(0, lon, lat)
# 
#     #filter layers using point
#     lyr_in_h.SetSpatialFilter(pt)
#     lyr_in_us.SetSpatialFilter(pt)
# 
#     if len(lyr_in_h) == 0 and len(lyr_in_us) == 0:
#         pointer = None
#     elif len(lyr_in_us) != 0:
#         pointer = 'US'
#     else:
#         pointer = "Global"
#     return pointer
# 
# def saveModelOutput(plot_id, model_version, result_blob, soilIDRank_output_pd, mucompdata_cond_prob):
# 
#     try:
#         conn = getDataStore_Connection()
#         cur = conn.cursor()
# 
#         plot_id = plot_id
#         result_blob = result_blob
# 
#         sql = "INSERT INTO landpks_soil_model (plot_id, model_version, result_blob, soilIDRank_output_pd, mucompdata_cond_prob) VALUES (%s, %s, %s, %s, %s)"
#         cur.execute(sql, (plot_id, model_version, result_blob, soilIDRank_output_pd, mucompdata_cond_prob))
#         conn.commit()
#         #return True
#     except Exception as err:
#         print(err)
#         conn.rollback()
#         #conn.close()
#         return None
#     finally:
#         conn.close()
# 
# def saveSoilGridsOutput(plot_id, model_version, soilgrids_blob):
# 
#     try:
#         conn = getDataStore_Connection()
#         cur = conn.cursor()
# 
#         plot_id = plot_id
#         soilgrids_blob = soilgrids_blob
# 
#         sql = "INSERT INTO landpks_soil_model (plot_id, model_version, soilgrids_blob) VALUES (%s, %s, %s)"
#         cur.execute(sql, (plot_id, model_version, soilgrids_blob))
#         conn.commit()
#         #return True
#     except Exception as err:
#         print(err)
#         conn.rollback()
#         #conn.close()
#         return None
#     finally:
#         conn.close()
#         
# def saveRankOutput(record_id, model_version, rank_blob):
# 
#     try:
#         conn = getDataStore_Connection()
#         cur = conn.cursor()
# 
#         sql = "UPDATE landpks_soil_model SET soilrank = %s WHERE ID = %s AND model_version = %s"
# 
#         cur.execute(sql, (rank_blob, record_id, model_version))
#         conn.commit()
#     except Exception as err:
#         print(err)
#         conn.rollback()
#         #conn.close()
#         return None
#     finally:
#         conn.close()
# 
# def loadModelOutput(plot_id, model_version):
#     try:
#         conn = getDataStore_Connection()
#         cur = conn.cursor()
# 
#         sql = "SELECT ID, result_blob, soilIDRank_output_pd, mucompdata_cond_prob FROM  landpks_soil_model WHERE plot_id =  %s AND model_version = %s order by ID desc LIMIT 1" % (
#             plot_id, model_version)
#         cur.execute(sql)
#         results = cur.fetchall()
#         for row in results:
#             modelRun = [row[0], row[1], row[2], row[3]]
#         return modelRun
#     except Exception as err:
#         print(err)
#         return None
#     finally:
#         conn.close()

def getWISE30sec_data(MUGLB_NEW_Select):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT MUGLB_NEW, COMPID, id, MU_GLOBAL, NEWSUID, SCID, PROP, CLAF,  PRID, Layer, TopDep, BotDep,  CFRAG,  SDTO,  STPC,  CLPC, CECS, PHAQ, ELCO, SU_name, FAO_SYS FROM  wise_soil_data WHERE MUGLB_NEW IN (' + ','.join(map(str, MUGLB_NEW_Select)) + ')'  
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['MUGLB_NEW',  'COMPID', 'id', 'MU_GLOBAL', 'NEWSUID', 'SCID', 'PROP', 'CLAF',  'PRID', 'Layer', 'TopDep', 'BotDep',  'CFRAG',  'SDTO',  'STPC',  'CLPC', 'CECS', 'PHAQ', 'ELCO', 'SU_name', 'FAO_SYS']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None

def getWISE30sec_comp_data(COMPID):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        COMPID_List = [COMPID]
        sql = 'SELECT MUGLB_NEW, COMPID, id, MU_GLOBAL, NEWSUID, SU_name, SCID, PROP, CLAF,  PRID, Layer, TopDep, BotDep, Drain, DrainNum, CFRAG, SDTO, STPC, CLPC, PSCL, PSCL_ID, BULK, TAWC, ORGC, TOTN, CECS, CECc, ECEC, TEB, BSAT, ALSA, ESP, PHAQ, TCEQ, GYPS, ELCO, PHASE1, PHASE2, ROOTS, IL, SWR, ADD_PROP, T_DC, S_DC, T_BULK_DEN, T_REF_BULK, S_BULK_DEN, S_REF_BULK, text_class, text_class_id, REF_DEPTH FROM  wise_soil_data WHERE COMPID IN (' + ','.join(map(str, COMPID_List)) + ')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['MUGLB_NEW', 'COMPID', 'id', 'MU_GLOBAL', 'NEWSUID', 'SU_name', 'SCID', 'PROP', 'CLAF',  'PRID', 'Layer', 'TopDep', 'BotDep', 'Drain', 'DrainNum', 'CFRAG', 'SDTO', 'STPC', 'CLPC', 'PSCL', 'PSCL_ID', 'BULK', 'TAWC', 'ORGC', 'TOTN', 'CECS', 'CECc', 'ECEC', 'TEB', 'BSAT', 'ALSA', 'ESP', 'PHAQ', 'TCEQ', 'GYPS', 'ELCO', 'PHASE1', 'PHASE2', 'ROOTS', 'IL', 'SWR', 'ADD_PROP', 'T_DC', 'S_DC', 'T_BULK_DEN', 'T_REF_BULK', 'S_BULK_DEN', 'S_REF_BULK','text_class', 'text_class_id', 'REF_DEPTH']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()

# Module IV (Agro-edaphic suitability)
### Calculations are crop/LUT specific and are performed for rainfed systems only
# In the GAEZ approach, land qualities are assessed in several steps involving specific procedures. The land qualities related to climate and climate‐soil interactions (flooding regimes, soil erosion and soil nutrient maintenance) are treated separate from those land qualities specifically related to soil properties and conditions as reflected in the Harmonized World Soil Database and the GAEZ terrain-slope database.

### Land Qualities:
  # 1. Climate regime (temperature, moisture, radiation) -- [Climatic suitability classification]
  # 2. Flooding regime -- [Moisture regime analysis of water collecting sites]
  # 3. Soil erosion -- [Assessment of sustainable use of sloping terrain]
  # 4. Soil nutrient maintenance -- [Fallow period requirement assessment]
  # 5. Soil physical and chemical properties -- [Soil suitability classification]

## Soil Qualities
# Soil quality will be calculated at each soil depth and averaged using appropriate depth weights.
# Standard GAEZ depth weights: 
# Depth  |  # of layers  | Weighting Factors
# 120    |      6        | 2, 1.5 , 1, .75, .5, .25
# 100    |      5        | 1.75, 1.5 , 1, .5, .25
# 80     |      4        | 1.75, 1.25 , .75, .25
# 60     |      3        | 1.5, 1, .5
# 40     |      2        | 1.25, .75
# 20     |      1        | 1

# Profile
def getGAEZ_profile_req(CROP_ID, Input_Level_List):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT CROP_ID, CROP, input_level, SQI_code, score, property_value, property, unit, property_id, property_text FROM  GAEZ_profile_req_rf WHERE CROP_ID=\'' + CROP_ID + '\' AND input_level IN ('  + ','.join(map(str, Input_Level_List)) + ')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 'property_value', 'property', 'unit', 'property_id', 'property_text']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()

# Texture
def getGAEZ_texture_req(CROP_ID, Input_Level_List):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT CROP_ID, CROP, input_level, SQI_code, score, text_class_id, text_class FROM  GAEZ_text_req_rf WHERE CROP_ID=\'' + CROP_ID + '\' AND input_level IN ('  + ','.join(map(str, Input_Level_List)) + ')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 'text_class_id', 'text_class']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()

# # Terrain
# def getGAEZ_terrain_req(CROP_ID, Input_Level_List):
#     try:
#         conn = getDataStore_Connection()
#         cur = conn.cursor()
#         sql = 'SELECT CROP_ID, CROP, crop_group, input_level, FM_class, slope_class, slope_class_id, rating, rating_text FROM  GAEZ_terrain_req_rf WHERE CROP_ID=\'' + CROP_ID + '\' AND input_level IN ('  + ','.join(map(str, Input_Level_List)) + ')'
#         cur.execute(sql)
#         results = cur.fetchall()
#         data = pd.DataFrame(list(results))
#         data.columns = ['CROP_ID', 'CROP', 'crop_group', 'input_level', 'FM_class', 'slope_class', 'slope_class_id', 'rating', 'rating_text']
#         return data
#         conn.close()
#     except Exception as err:
#         print(err)
#         return None
#     finally:
#         conn.close()
        
# Phase
def getGAEZ_phase_req(CROP_ID, Input_Level_List):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT CROP_ID, CROP, input_level, SQI_code, property, phase_id, phase, score FROM  GAEZ_phase_req_rf WHERE CROP_ID=\'' + CROP_ID + '\' AND input_level IN ('  + ','.join(map(str, Input_Level_List)) + ')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'property', 'phase_id', 'phase', 'score']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()
        
# Drainage
def getGAEZ_drainage_req(CROP_ID, Input_Level_List):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT CROP_ID, CROP, input_level, SQI_code, PSCL, PSCL_ID, DrainNum, Drain, score FROM  GAEZ_drainage_req_rf WHERE CROP_ID=\'' + CROP_ID + '\' AND input_level IN ('  + ','.join(map(str, Input_Level_List)) + ')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'PSCL', 'PSCL_ID', 'DrainNum', 'Drain', 'score']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()
        
# Drainage class
def get_drainage_class(slope, histic, saturation, shallow, hardpan, vertic):
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        sql = 'SELECT PSCL_ID, Drain, DrainNum FROM  soil_drainage_class_requirements WHERE (Slope_l<=' + str(slope[0]) + ' AND Slope_h>' + str(slope[0]) + ') AND Histic=\'' + histic + '\' AND (Saturation=\'' + saturation + '\' OR Saturation=\'Any\') AND (Vertic=\'' + vertic + '\' OR Vertic=\'Any\') AND (Shallow=\'' + shallow + '\' OR Shallow=\'Any\') AND (Hardpan=\'' + hardpan + '\' OR Hardpan=\'Any\')'
        cur.execute(sql)
        results = cur.fetchall()
        data = pd.DataFrame(list(results))
        data.columns = ['PSCL_ID', 'Drain', 'DrainNum']
        return data
        conn.close()
    except Exception as err:
        print(err)
        return None
    finally:
        conn.close()  
  
# -----------------------------------------------------------------------------------------------------
#Function to GAEZ Soil Quality Indides
def GAEZ_SQI(COMPID, CROP_ID, inputLevel, depthWt_type=1, plot_data=None, site_data=None, lab_data=None):
    data = getWISE30sec_comp_data(COMPID)

## ---------------------------------------------------------------------------------------------------------------------
    def agg_data_layer_SQI(data, bottom, sd=2, depth=False):
        if np.isnan(bottom) or bottom == 0:
            data_d = pd.Series([np.nan])
            
            d_lyrs = pd.Series([np.nan])
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 0 and bottom < 21:
            data_d = pd.Series([round(pd.Series.mean(data[0:21]), sd)])
            data_d = data_d.rename(index={0:'sl1'})
            d_lyrs = pd.Series([21]).rename(index={0:'sl1'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >=21 and bottom < 41:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:bottom]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2'})
            d_lyrs = pd.Series([20, bottom]).rename(index={0:'sl1', 1:'sl2'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 41 and bottom < 61:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:40]), sd), round(pd.Series.mean(data[40:bottom]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2', 2:'sl3'})
            d_lyrs = pd.Series([20, 40, bottom]).rename(index={0:'sl1', 1:'sl2', 2:'sl3'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 61 and bottom < 81:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:40]), sd),  round(pd.Series.mean(data[40:60]), sd), round(pd.Series.mean(data[60:bottom]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4'})
            d_lyrs = pd.Series([20, 40, 60, bottom]).rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 81 and bottom < 101:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:40]), sd),  round(pd.Series.mean(data[40:60]), sd), round(pd.Series.mean(data[60:80]), sd), round(pd.Series.mean(data[80:bottom]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5'})
            d_lyrs = pd.Series([20, 40, 60, 80, bottom]).rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 101 and bottom < 120:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:40]), sd), round(pd.Series.mean(data[40:60]), sd), round(pd.Series.mean(data[60:80]), sd), round(pd.Series.mean(data[80:100]), sd), round(pd.Series.mean(data[100:bottom]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5', 5:'sl6'})
            d_lyrs = pd.Series([20, 40, 60, 80, 100, bottom]).rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5', 5:'sl6'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
        elif bottom >= 120:
            data_d = pd.Series([round(pd.Series.mean(data[0:20]), sd), round(pd.Series.mean(data[20:40]), sd), round(pd.Series.mean(data[40:60]), sd), round(pd.Series.mean(data[60:80]), sd), round(pd.Series.mean(data[80:100]), sd), round(pd.Series.mean(data[100:120]), sd)])
            data_d = data_d.rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5', 5:'sl6'})
            d_lyrs = pd.Series([20, 40, 60, 80, 100, 120]).rename(index={0:'sl1', 1:'sl2', 2:'sl3',3:'sl4', 4:'sl5', 5:'sl6'})
            if depth is True:
                return data_d, d_lyrs
            else:
                return data_d
                


    def gettt(row, sand=None, silt=None, clay=None):
        if sand is not None and silt is not None and clay is not None:
            sand = sand
            silt = silt
            clay = clay
        else:
            sand = row['sandtotal_r']
            silt = row['silttotal_r']
            clay = row['claytotal_r']

        if (silt + 1.5 * clay) < 15:
            return "Sand"
        elif (silt + 1.5 * clay) >= 15 and (silt + 2.0 * clay) < 30:
            return "Loamy sand"
        elif (clay >= 7) and (clay <= 20) and (sand > 52) and ((silt + 2.0 * clay) >= 30):
            return "Sandy loam"
        elif (clay < 7) and (silt < 50) and ((silt + 2.0 * clay) >= 30):
            return "Sandy loam"
        elif (clay >= 7) and (clay <= 27) and (silt >= 28) and (silt < 50) and (sand <= 52):
            return "Loam"
        elif ((silt >= 50) and (clay >= 12) and (clay < 27)) or ((silt >= 50) and (silt < 80) and (clay < 12)):
            return "Silt loam"
        elif (silt >= 80) and (clay < 12):
            return "Silt"
        elif (clay >= 20) and (clay < 35) and (silt < 28) and (sand > 45):
            return "Sandy clay loam"
        elif (clay >= 27) and (clay < 40) and (sand > 20) and (sand <= 45):
            return "Clay loam"
        elif (clay >= 27) and (clay < 40) and (sand <= 20):
            return "Silty clay loam"
        elif (clay >= 35) and (sand >= 45):
            return "Sandy clay"
        elif (clay >= 40) and (silt >= 40):
            return "Silty clay"
        elif (clay >= 40) and (sand <= 45) and (silt < 40):
            return "Clay"
    def getTextGroup(field):
        if field is None:
            return(np.nan)
        else:
            lfield = field.lower()
            if (lfield == "sand") or (lfield == "loamy sand") or (lfield == "sandy loam"):
                return 'C'
            elif (lfield == "sandy clay loam") or (lfield == "loam") or (lfield == "clay loam") or (lfield == "silt loam") or (lfield == "silt") or (lfield == "silty clay loam"):
                return 'M'
            elif (lfield == "sandy clay") or (lfield == "silty clay") or (lfield == "clay"):
                return 'F'    
    def getTextGroup_id(field):
        if field is None:
            return(np.nan)
        else:
            lfield = field.lower()
            if (lfield == "sand") or (lfield == "loamy sand") or (lfield == "sandy loam"):
                return 1
            elif (lfield == "sandy clay loam") or (lfield == "loam") or (lfield == "clay loam") or (lfield == "silt loam") or (lfield == "silt") or (lfield == "silty clay loam"):
                return 2
            elif (lfield == "sandy clay") or (lfield == "silty clay") or (lfield == "clay"):
                return 3 
    def getSand(field):
        if field is None:
            return(np.nan)
        else:
            lfield = field.lower()
            if lfield == "sand":
                return 92.0
            elif lfield == "loamy sand":
                return 80.0
            elif lfield == "sandy loam":
                return 61.5
            elif lfield == "sandy clay loam":
                return 62.5
            elif lfield == "loam":
                return 37.5
            elif lfield == "silt":
                return 10.0
            elif lfield == "silt loam":
                return 25.0
            elif lfield == "silty clay loam":
                return 10.0
            elif lfield == "clay loam":
                return 32.5
            elif lfield == "sandy clay":
                return 55.0
            elif lfield == "silty clay":
                return 10.0
            elif lfield == "clay":
                return 22.5

    def getClay(field):
        if field is None:
            return(np.nan)
        else:
            lfield = field.lower()
            if lfield == "sand":
                return 5.0
            elif lfield == "loamy sand":
                return 7.5
            elif lfield == "sandy loam":
                return 10.0
            elif lfield == "sandy clay loam":
                return 27.5
            elif lfield == "loam":
                return 17.0
            elif lfield == "silt":
                return 6.0
            elif lfield == "silt loam":
                return 13.5
            elif lfield == "silty clay loam":
                return 33.5
            elif lfield == "clay loam":
                return 33.5
            elif lfield == "sandy clay":
                return 45.0
            elif lfield == "silty clay":
                return 50.0
            elif lfield == "clay":
                return 70.0
    def getCF_fromClass(cf):
        if cf == "0-1%":
            return 0
        elif cf == "1-15%":
            return 8
        elif cf == "15-35%":
            return 25
        elif cf == "35-60%":
            return 48
        elif cf == ">60%":
            return 80
        else:
            return np.nan

    def getSlope_fromClass(sc):
        if sc == "flat 0-2%":
            return 1
        elif sc == "gentle 3-5%":
            return 4
        elif sc == "moderate 6-10%":
            return 8
        elif sc == "rolling 11-15%":
            return 13
        elif sc == "hilly 16-30%":
            return 23
        elif sc == "steep 31-60%":
            return 45
        elif sc == "verysteep 60-100%":
            return 80
        else:
            return np.nan
            
    def getTXT_id(texture):
        lfield = texture.lower()
        if lfield == "sand":
            return 12
        elif lfield == "loamy sand":
            return 11
        elif lfield == "sandy loam":
            return 10
        elif lfield == "sandy clay loam":
            return 9
        elif lfield == "loam":
            return 8
        elif lfield == "silt":
            return 5
        elif lfield == "silt loam":
            return 6
        elif lfield == "silty clay loam":
            return 3
        elif lfield == "clay loam":
            return 4
        elif lfield == "sandy clay":
            return 7
        elif lfield == "silty clay":
            return 2
        elif lfield == "clay":
            return 1

        # Standard GAEZ depth weights:
          # Depth  |  # of layers  | Weighting Factors
          # 120    |      6        | 2, 1.5 , 1, .75, .5, .25
          # 100    |      5        | 1.75, 1.5 , 1, .5, .25
          # 80     |      4        | 1.75, 1.25 , .75, .25
          # 60     |      3        | 1.5, 1, .5
          # 40     |      2        | 1.25, .75
          # 20     |      1        | 1
    def calc_depth_wts(depths, depthWt_type):        
        if depthWt_type == 1:
            if depths == 6:
                wts = [2, 1.5, 1.0, 0.75, 0.5, 0.25]
            elif depths ==5:
                wts = [1.75, 1.5, 1.0, 0.5, 0.25]
            elif depths ==4:
                wts = [1.75, 1.25, 0.75, 0.25]
            elif depths ==3:
                wts = [1.5, 1.0, 0.5]
            elif depths ==2:
                wts = [1.25, 0.75]
            elif depths ==1:
                wts = [1]
            return wts
                
        elif depthWt_type == 2:   
            if depths == 6:
                wts = [4.8, 0.4, 0.2, 0.2, 0.2, 0.2]
            elif depths ==5:
                wts = [4, 0.4, 0.2, 0.2, 0.2]
            elif depths ==4:
                wts = [3.2, 0.4, 0.2, 0.2]
            elif depths ==3:
                wts = [2.4, 0.4, 0.2]
            elif depths ==2:
                wts = [1.6, 0.4]
            elif depths ==1:
                wts = [1]
            return wts   

    if plot_data is not None:
        #------------------------------------------------------------------------------------------------
        #------ Load in user data --------#
        # cleanup the arrays
        soil_df = plot_data[['texture', 'bottom', 'rfv_class']]
        soil_df.columns = ["soilHorizon", "horizonDepth", "rfvDepth"]
        soil_df = soil_df.dropna(how='all')
        soil_df['bottom'] = soil_df.horizonDepth
        soil_df = soil_df.where((pd.notnull(soil_df)), None)
        top = []
        hzIdx = len(soil_df.horizonDepth) - 1
        top.append(0)
        for i in range(0, hzIdx + 1):
            if i < hzIdx:
                top.append(int(soil_df.horizonDepth[i]))
        soil_df['top'] = top
        soil_df = soil_df.set_index('horizonDepth')
        bedrock = plot_data['bedrock_depth'][0]
        if np.isnan(bedrock):
            bedrock = 120
        else:
            bedrock = bedrock
    
        #Drop rows where all horizon variables are missing
        soil_df_slice = soil_df.dropna(how='all', subset=['soilHorizon', 'rfvDepth'])

        if soil_df_slice.empty:
            soil_df_slice = None
        else:
            soil_df_slice['index'] = soil_df_slice.index
            soil_df_slice = soil_df_slice.reset_index(drop=True)
            soil_df_slice = soil_df_slice.set_index('index')

        if soil_df_slice is not None:
            #If bedrock has been recorded and the lowest soil depth associated with data is greater than bedrock, then change lowest soil depth to bedrock depth
            if bedrock is not None and soil_df_slice.bottom.iloc[-1] > bedrock:
                soil_df_slice.bottom.iloc[-1] = bedrock
                soil_df.bottom[soil_df_slice.index[-1]] = bedrock
                soil_df = soil_df.reset_index(drop=True)
                #This will create a depth gap that needs to be infilled with NaN or None
                #Infill missing horizons
                for j in range(len(soil_df)):
                    if j == len(soil_df) - 1:
                        break
                    if (soil_df.top[j + 1] > soil_df.bottom[j]):
                        layer_add = pd.DataFrame([None, None, None, soil_df.top[j + 1], soil_df.bottom[j]]).T
                        layer_add.columns = ['soilHorizon', 'rfvDepth', 'lab_Color', 'bottom', 'top']
                        soil_df = pd.concat([soil_df, layer_add], axis=0)
                        soil_df = soil_df.sort_values(['top'], ascending = True)
                        soil_df = soil_df.reset_index(drop=True)
                soil_df = soil_df.where((pd.notnull(soil_df)), None)

            #Create index list of soil slices where user data exists
            soil_df_slice = soil_df_slice.reset_index(drop=True)
            pedon_slice_index = []
            for i in range(len(soil_df_slice)):
                for j in range(int(soil_df_slice.top[i]), int(soil_df_slice.bottom[i])):
                    pedon_slice_index.append(j)
            pedon_slice_index = [x for x in pedon_slice_index if x < 120]
  
            #Soil properties to lists
            soilHorizon = soil_df.soilHorizon.tolist()
            rfvDepth = soil_df.rfvDepth.tolist()
            horizonDepthB = soil_df.bottom.tolist()
            horizonDepthT = soil_df.top.tolist()
            horizonDepthB = [int(x) for x in horizonDepthB]
            horizonDepthT = [int(x) for x in horizonDepthT]


            #Format and generate user data
            #Generate user specified percent clay, sand, and rfv distributions
            spt = []
            cpt = []
            p_cfg = []
            p_sandpct_intpl =[]
            p_claypct_intpl = []
            p_cfg_intpl =[]

            for i in range(len(soilHorizon)):
                spt.append(getSand(soilHorizon[i]))
                cpt.append(getClay(soilHorizon[i]))
                p_cfg.append(getCF_fromClass(rfvDepth[i]))

            for i in range(len(soilHorizon)):
                for j in range(horizonDepthT[i], horizonDepthB[i]):
                    p_sandpct_intpl.append(spt[i])
                    p_claypct_intpl.append(cpt[i])
                    p_cfg_intpl.append(p_cfg[i])

            #Length of interpolated texture and RF depth
            p_bottom_depth = pd.DataFrame([-999, "sample_pedon", soil_df_slice.bottom.iloc[-1]]).T
            p_bottom_depth.columns = ["cokey", "compname", "bottom_depth"]

            p_sandpct_intpl = pd.Series(p_sandpct_intpl)
            p_claypct_intpl = pd.Series(p_claypct_intpl)
            p_cfg_intpl = pd.Series(p_cfg_intpl)

            #Adjust depth interval of user data
            if len(p_sandpct_intpl) > 120:
                p_sandpct_intpl = p_sandpct_intpl[0:120]
                p_sandpct_intpl = p_sandpct_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_sandpct_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_sandpct_intpl = pd.concat([p_sandpct_intpl, pd_add])
                p_sandpct_intpl = p_sandpct_intpl.reset_index(drop=True)

            if len(p_claypct_intpl) > 120:
                p_claypct_intpl = p_claypct_intpl[0:120]
                p_claypct_intpl = p_claypct_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_claypct_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_claypct_intpl = pd.concat([p_claypct_intpl, pd_add])
                p_claypct_intpl = p_claypct_intpl.reset_index(drop=True)

            if len(p_cfg_intpl) > 120:
                p_cfg_intpl = p_cfg_intpl[0:120]
                p_cfg_intpl = p_cfg_intpl.reset_index(drop=True)
            elif (len(p_cfg_intpl) < 120) and (len(p_cfg_intpl) > 0):
                Na_add = 120 - len(p_cfg_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_cfg_intpl = pd.concat([p_cfg_intpl, pd_add])
                p_cfg_intpl = p_cfg_intpl.reset_index(drop=True)

            p_compname = pd.Series("sample_pedon", index = np.arange(len(p_sandpct_intpl)))
            p_hz_data = pd.concat([p_compname, p_sandpct_intpl, p_claypct_intpl, p_cfg_intpl], axis=1)
            p_hz_data.columns = ["compname", "sandpct_intpl", "claypct_intpl", "rfv_intpl"]

            #Drop empty data columns
            p_hz_data = p_hz_data.loc[:, ~p_hz_data.isnull().all()]
            #Drop empty depth slices
            p_hz_data = p_hz_data[p_hz_data.index.isin(pedon_slice_index)]
            #list of user entered variables to match against
            p_hz_data_names = p_hz_data.columns.tolist()
            p_bottom = p_bottom_depth["bottom_depth"].astype(int).iloc[0]
            snd_d, hz_depb = agg_data_layer_SQI(data=p_hz_data["sandpct_intpl"], bottom = p_bottom, depth=True)
            cly_d = agg_data_layer_SQI(data=p_hz_data["claypct_intpl"], bottom = p_bottom)
            rf_d = agg_data_layer_SQI(data=p_hz_data["rfv_intpl"], bottom = p_bottom)
            
            txt_d = []
            for l in range(len(snd_d)):
                text_T = gettt(row=None, sand = snd_d[l],silt = (100-(snd_d[l]+cly_d[l])), clay = cly_d[l])
                txt_d.append(text_T.lower())
            txt_d = pd.Series(txt_d)
            txt_d.index = snd_d.index
            
            txt_id = []
            for l in range(len(txt_d)):
                txd_id_T = getTXT_id(txt_d[l])
                txt_id.append(txd_id_T)
            txt_id = pd.Series(txt_id)
            txt_id.index = snd_d.index

            txt_grp = []
            for l in range(len(txt_d)):
                txd_grp_T = getTextGroup(txt_d[l])
                txt_grp.append(txd_grp_T)
            txt_grp = pd.Series(txt_grp)
            txt_grp.index = snd_d.index

            txt_grp_id = []
            for l in range(len(txt_d)):
                txd_grp_id_T = getTextGroup_id(txt_d[l])
                txt_grp_id.append(txd_grp_id_T)
            txt_grp_id = pd.Series(txt_grp_id)
            txt_grp_id.index = snd_d.index
            
            
            p_hz_data = pd.concat([hz_depb, txt_d, txt_id, txt_grp, txt_grp_id, rf_d], axis=1)
            p_hz_data.columns = ["BotDep", "text_class", "text_class_id", "PSCL", "PSCL_ID", "CFRAG"]
            
            # This assumes that all depths start from the top and are consecutive
            #****** Need to fix how WISE and LandPKS data are integrated when they differ in the depths****************
            #depth of WISE dataset
            depths_wise = len(data.index)
            #depths of user data
            depths_pedon = len(p_hz_data.index)
            
            if depths_wise > depths_pedon:
                data = data.iloc[0:depths_pedon, :]
            elif depths_wise < depths_pedon:
                p_hz_data = p_hz_data.iloc[0:depths_wise, :]
            else:
                data = data
          
            data = data.assign(text_class=p_hz_data['text_class'].values)
            data = data.assign(text_class_id=p_hz_data['text_class_id'].values)
            data = data.assign(PSCL=p_hz_data['PSCL'].values)
            data = data.assign(CFRAG=p_hz_data['CFRAG'].values)
            data = data.assign(REF_DEPTH=bedrock)
            
            #Recalculate soil drainage class
            #Load in user entered slope class or DEM slope
            olm_250_slope = "/vsicurl/https://s3.eu-central-1.wasabisys.com/openlandmap/layers250m/dtm_slope_merit.dem_m_250m_s0..0cm_2017_v1.0.tif"
            coords = [(plot_data['longitude'][0], plot_data['latitude'][0])]
            with rasterio.open(olm_250_slope) as ds:
              for val in rasterio.sample.sample_gen(ds, coords):
                  slope = val

        else:
            data = data

    depths = len(data.index)

    if site_data is not None:
        #------------------------------------------------------------------------------------------------
        #------ Load in user data --------# slope, flooding, cracks, is_compaction_layer, bedrock_depth
        # cleanup the arrays

        site_df = site_data[['slope', 'flooding', 'cracks', 'is_compaction_layer', 'bedrock_depth']]
        site_df.columns = ['slope', 'flooding', 'cracks', 'is_compaction_layer', 'bedrock_depth']
        if type(site_df['slope'].all())=='float':
            slope = site_df['slope'].values
        elif type(site_df['slope'].all())=='str':
            slope = []
            for i in range(len(site_df['slope'])):
                slope.append(getSlope_fromClass(site_df['slope'][i]))
        if site_df['cracks'].any == 'Yes' and data['PSCL'].values.any == 'F':
            vertic = 'Yes'
        else:
            vertic = 'No'
        if site_df['flooding'].any == 'Frequent':
            saturation = 'Yes'
        else:
            saturation = 'No'
        if site_df['is_compaction_layer'].any == 'Yes':
            hardpan = 'Yes'
        else:
            hardpan = 'No'
        if site_df['bedrock_depth'].values.any() <= 50:
            shallow = 'Yes'
        else:
            shallow = 'No'            
        histic = "No"
        
      #Calculate drainage class based on site data
        drainage_lookup = get_drainage_class(slope, histic, saturation, shallow, hardpan, vertic)
        PSCL_ID_max = p_hz_data['PSCL_ID'].max()
        site_drainage_class = drainage_lookup.query('PSCL_ID ==' + str(PSCL_ID_max))

        data = data.assign(Drain=pd.Series(np.repeat(site_drainage_class['Drain'].values, len(data))))
        data = data.assign(DrainNum=pd.Series(np.repeat(site_drainage_class['DrainNum'].values, len(data))))
        
      #Petric/Vertic: modify data for petric (cemented layer = [hardpan]) or vertic (cracking and clay). 
        # Petric soil properties are assigned a value of 1 in the ADD_PROP data column. Petric feres to petric Calcisols adn petric Gypsisols
        # Vertic soil properties are assigned a value of 3 in the ADD_PROP data column
        
        # It is difficult to determine if a hardpan is from CaCO3 or CaSO4. But in cases where no hardpan is identified and HWSD indicates petric properties, we can remove this designation. Other hardpans will be accounted for by other measurements.
        if hardpan == 'No' and data.ADD_PROP[0] == 1:
            data = data.assign(ADD_PROP=pd.Series(np.repeat(0, len(data))))
        
        # Vertic is less limiting than petric and gelic so only modify if ADD_PROP=0
        if vertic == 'Yes' and data.ADD_PROP[0] == 0:
            data = data.assign(ADD_PROP=pd.Series(np.repeat(3, len(data))))
        
        # Currently no check for gelic.
        
      #Phase data
        #If coarse fragments are >= 35, then == Phase: Skeletic, Gravelly, Concretionary
        if data['CFRAG'].max() >= 35 and data.PHASE1[0] == 0:
            data = data.assign(PHASE1=pd.Series(np.repeat(20, len(data))))
        elif data['CFRAG'].max() >= 35 and data.PHASE2[0] == 0:
            data = data.assign(PHASE2=pd.Series(np.repeat(20, len(data))))


    if lab_data is not None:
        #------------------------------------------------------------------------------------------------
        #------ Load in user data --------# slope, flooding, cracks, is_compaction_layer, bedrock_depth
        # cleanup the arrays
        lab_df = lab_data[['OC', 'pH', 'TEB', 'BS', 'ECEC', 'CECc', 'ESP', 'bottom', 'texture']]
        lab_df.columns = ['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP', 'bottom', 'texture']

        lab_df = lab_df.dropna(how='all')
        lab_df = lab_df.where((pd.notnull(lab_df)), None)

        top = []
        hzIdx = len(lab_df.bottom) - 1
        top.append(0)
        for i in range(0, hzIdx + 1):
            if i < hzIdx:
                top.append(int(lab_df.bottom[i]))
        lab_df['top'] = top
        lab_df['depth_index'] = lab_df.bottom
        lab_df = lab_df.set_index('depth_index')
        bedrock = lab_data['bedrock_depth'][0]
        if np.isnan(bedrock):
            bedrock = 120
        else:
            bedrock = bedrock

        #Drop rows where all horizon variables are missing
        lab_df_slice = lab_df.dropna(how='all', subset=['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP', 'texture'])

        if soil_df_slice.empty:
            soil_df_slice = None
        else:
            lab_df_slice['index'] = lab_df_slice.index
            lab_df_slice = lab_df_slice.reset_index(drop=True)
            lab_df_slice = lab_df_slice.set_index('index')

        if lab_df_slice is not None:
            #If bedrock has been recorded and the lowest soil depth associated with data is greater than bedrock, then change lowest soil depth to bedrock depth
            if bedrock is not None and lab_df_slice.bottom.iloc[-1] > bedrock:
                lab_df_slice.bottom.iloc[-1] = bedrock
                lab_df.bottom[lab_df_slice.index[-1]] = bedrock
                lab_df = lab_df.reset_index(drop=True)
                #This will create a depth gap that needs to be infilled with NaN or None
                #Infill missing horizons
                for j in range(len(lab_df)):
                    if j == len(lab_df) - 1:
                        break
                    if (lab_df.top[j + 1] > lab_df.bottom[j]):
                        layer_add = pd.DataFrame([None, None, None,None, None, None,None, None,None, lab_df.top[j + 1], lab_df.bottom[j]]).T
                        layer_add.columns = ['OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP',  'bottom', 'texture', 'bottom', 'top']
                        lab_df = pd.concat([lab_df, layer_add], axis=0)
                        lab_df = lab_df.sort_values(['top'], ascending = True)
                        lab_df = lab_df.reset_index(drop=True)
                lab_df = lab_df.where((pd.notnull(lab_df)), None)

            #Create index list of soil slices where user data exists
            lab_df_slice = lab_df_slice.reset_index(drop=True)
            pedon_slice_index = []
            for i in range(len(lab_df_slice)):
                for j in range(int(lab_df_slice.top[i]), int(lab_df_slice.bottom[i])):
                    pedon_slice_index.append(j)
            pedon_slice_index = [x for x in pedon_slice_index if x < 120]
  
            #Soil properties to lists
            soilHorizon = soil_df.soilHorizon.tolist()
            rfvDepth = soil_df.rfvDepth.tolist()
            
            OC = lab_df.OC.tolist()
            pH = lab_df.pH.tolist()
            TEB = lab_df.TEB.tolist()
            BS = lab_df.BS.tolist()
            CECs = lab_df.CECs.tolist()
            CECc = lab_df.CECc.tolist()
            ESP = lab_df.ESP.tolist()


            horizonDepthB = lab_df.bottom.tolist()
            horizonDepthB = [int(x) for x in horizonDepthB]            
            horizonDepthT = lab_df.top.tolist()
            horizonDepthT = [int(x) for x in horizonDepthT]


            #Format and generate user data
            #Generate user specified distributions

            p_OC_intpl = []
            p_pH_intpl = []
            p_TEB_intpl = []
            p_BS_intpl = []
            p_CECs_intpl = []
            p_CECc_intpl = []
            p_ESP_intpl = []

            for i in range(len(soilHorizon)):
                for j in range(horizonDepthT[i], horizonDepthB[i]):
                    p_OC_intpl.append(OC[i])
                    p_pH_intpl.append(pH[i])
                    p_TEB_intpl.append(TEB[i])
                    p_BS_intpl.append(BS[i])
                    p_CECs_intpl.append(CECs[i])
                    p_CECc_intpl.append(CECc[i])
                    p_ESP_intpl.append(ESP[i])



            #Length of interpolated texture and RF depth
            p_bottom_depth = pd.DataFrame([-999, "sample_pedon", soil_df_slice.bottom.iloc[-1]]).T
            p_bottom_depth.columns = ["cokey", "compname", "bottom_depth"]

            p_OC_intpl = pd.Series(p_OC_intpl)
            p_pH_intpl = pd.Series(p_pH_intpl)
            p_TEB_intpl = pd.Series(p_TEB_intpl)
            p_BS_intpl = pd.Series(p_BS_intpl)
            p_CECs_intpl = pd.Series(p_CECs_intpl)
            p_CECc_intpl = pd.Series(p_CECc_intpl)
            p_ESP_intpl = pd.Series(p_ESP_intpl)


            #Adjust depth interval of user data
            if len(p_OC_intpl) > 120:
                p_OC_intpl = p_OC_intpl[0:120]
                p_OC_intpl = p_OC_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_OC_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_OC_intpl = pd.concat([p_OC_intpl, pd_add])
                p_OC_intpl = p_OC_intpl.reset_index(drop=True)

            if len(p_pH_intpl) > 120:
                p_pH_intpl = p_pH_intpl[0:120]
                p_pH_intpl = p_pH_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_pH_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_pH_intpl = pd.concat([p_pH_intpl, pd_add])
                p_pH_intpl = p_pH_intpl.reset_index(drop=True)
                
            if len(p_pH_intpl) > 120:
                p_pH_intpl = p_pH_intpl[0:120]
                p_pH_intpl = p_pH_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_pH_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_pH_intpl = pd.concat([p_pH_intpl, pd_add])
                p_pH_intpl = p_pH_intpl.reset_index(drop=True)

            if len(p_BS_intpl) > 120:
                p_BS_intpl = p_BS_intpl[0:120]
                p_BS_intpl = p_BS_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_BS_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_BS_intpl = pd.concat([p_BS_intpl, pd_add])
                p_BS_intpl = p_BS_intpl.reset_index(drop=True)

            if len(p_CECs_intpl) > 120:
                p_CECs_intpl = p_CECs_intpl[0:120]
                p_CECs_intpl = p_CECs_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_CECs_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_CECs_intpl = pd.concat([p_CECs_intpl, pd_add])
                p_CECs_intpl = p_CECs_intpl.reset_index(drop=True)
                
            if len(p_CECc_intpl) > 120:
                p_CECc_intpl = p_CECc_intpl[0:120]
                p_CECc_intpl = p_CECc_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_CECc_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_CECc_intpl = pd.concat([p_CECc_intpl, pd_add])
                p_CECc_intpl = p_CECc_intpl.reset_index(drop=True)

            if len(p_ESP_intpl) > 120:
                p_ESP_intpl = p_ESP_intpl[0:120]
                p_ESP_intpl = p_ESP_intpl.reset_index(drop=True)
            else:
                Na_add = 120 - len(p_ESP_intpl)
                pd_add = pd.Series(np.nan, index = np.arange(Na_add))
                p_ESP_intpl = pd.concat([p_ESP_intpl, pd_add])
                p_ESP_intpl = p_ESP_intpl.reset_index(drop=True)

         
            p_compname_lab = pd.Series("sample_pedon", index = np.arange(len(p_OC_intpl)))
            p_lab_data = pd.concat([p_compname_lab, p_OC_intpl, p_pH_intpl,  p_TEB_intpl, p_BS_intpl, p_CECs_intpl, p_CECc_intpl, p_ESP_intpl], axis=1)
            p_lab_data.columns = ["compname", 'OC_intpl', 'pH_intpl',  'TEB_intpl', 'BS_intpl', 'CECs_intpl', 'CECc_intpl', 'ESP_intpl']

            #Drop empty data columns
            p_lab_data = p_lab_data.loc[:, ~p_lab_data.isnull().all()]
            #Drop empty depth slices
            p_lab_data = p_lab_data[p_lab_data.index.isin(pedon_slice_index)]
            #list of user entered variables to match against
            p_lab_data_names = p_lab_data.columns.tolist()
            p_bottom = p_bottom_depth["bottom_depth"].astype(int).iloc[0]
            
            
            oc_d, hz_depb = agg_data_layer_SQI(data=p_lab_data["OC_intpl"], bottom = p_bottom, depth=True)
            ph_d = agg_data_layer_SQI(data=p_lab_data["pH_intpl"], bottom = p_bottom)
            teb_d = agg_data_layer_SQI(data=p_lab_data["TEB_intpl"], bottom = p_bottom)
            bs_d = agg_data_layer_SQI(data=p_lab_data["BS_intpl"], bottom = p_bottom)
            cecs_d = agg_data_layer_SQI(data=p_lab_data["CECs_intpl"], bottom = p_bottom)
            cecc_d = agg_data_layer_SQI(data=p_lab_data["CECc_intpl"], bottom = p_bottom)
            esp_d = agg_data_layer_SQI(data=p_lab_data["ESP_intpl"], bottom = p_bottom)


            p_lab_data = pd.concat([hz_depb, oc_d, ph_d, teb_d, bs_d, cecs_d, cecc_d, esp_d], axis=1)
            p_lab_data.columns = ["BotDep", 'OC', 'pH', 'TEB', 'BS', 'CECs', 'CECc', 'ESP']
            
            # This assumes that all depths start from the top and are consecutive
            #****** Need to fix how WISE and LandPKS data are integrated when they differ in the depths****************
            #depth of WISE dataset
            depths_wise = len(data.index)
            #depths of user data
            depths_pedon = len(p_lab_data.index)
            
            if depths_wise > depths_pedon:
                data = data.iloc[0:depths_pedon, :]
            elif depths_wise < depths_pedon:
                p_lab_data = p_lab_data.iloc[0:depths_wise, :]
            else:
                data = data
          
            data = data.assign(ORGC=p_lab_data['OC'].values)
            data = data.assign(PHAQ=p_lab_data['pH'].values)
            data = data.assign(TEB=p_lab_data['TEB'].values)
            data = data.assign(BSAT=p_lab_data['BS'].values)
            data = data.assign(CECS=p_lab_data['CECs'].values)
            data = data.assign(CECc=p_lab_data['CECc'].values)
            data = data.assign(ESP=p_lab_data['ESP'].values)


  # ------------------------------------------------------------------------------------
  # S0 No constraint (100%)
  # S1 Slight constraint (90%)
  # S2 Moderate constraint (70%)
  # S3 Severe constraint (50%)
  # S4 Very severe constraint (30%)
  # N  Not suitable (<10%)
  
  # determine possible input_level codes
    if inputLevel == 'L':
        Input_Level_List = ['1','3', '4']
    elif inputLevel == 'I':
        Input_Level_List = ['2','3', '4']
    elif inputLevel == 'H':
        Input_Level_List = ['4','5']
    else:
        return 'Please enter `inputLevel`'
        
         
          
          
  # Load in crop and input specific property requirements
    #Texture requirements based on crop and input level
    texture_req = getGAEZ_texture_req(CROP_ID, Input_Level_List)
    #Property requirements based on crop and input level
    property_req = getGAEZ_profile_req(CROP_ID, Input_Level_List)
    #Phase requirements based on crop and input level
    phase_req = getGAEZ_phase_req(CROP_ID, Input_Level_List)    
    #Drainage requirements based on crop and input level
    drainage_req = getGAEZ_drainage_req(CROP_ID, Input_Level_List)    

  # SQI 1
    if inputLevel == 'H':
        SQ1_score = 'NA'
    else:
        SQ1_scores = []
        for s in range(len(data.index)):
            layer = data.loc[s]
          #oc score
            sq1_oc_req = property_req.query('SQI_code == 1 & property == \'oc\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            oc = layer.ORGC
            oc_score = None
            i=0
            n = len(sq1_oc_req.property_value)-1
            while oc_score == None:
                if oc >= sq1_oc_req.property_value[i] or i == n:
                    oc_score = sq1_oc_req.score[i]
                else:
                    oc_score = None
                    i = i + 1
          #ph score
            sq1_ph_req = property_req.query('SQI_code == 1 & property == \'ph\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            ph = layer.PHAQ
            ph_score = None
            j = 0
            n = len(sq1_ph_req.property_value)-1
            while ph_score == None:
                if ph >= sq1_ph_req.property_value[j] or j == n:
                    ph_score = sq1_ph_req.score[j]
                else:
                    ph_score = None
                    j = j + 1
          #texture score
            text_class_id = str(layer.text_class_id)
            sq1_text_req = texture_req.query('SQI_code == 1 & text_class_id ==' + text_class_id).reset_index(drop=True)
            txt_score = sq1_text_req.score[0]
          
          #For topsoil only
            #add TEB score and combine property layer scores
            if s == 0:
                sq1_teb_req = property_req.query('SQI_code == 1 & property == \'teb\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
                teb = layer.TEB
                teb_score = None
                k=0
                n = len(sq1_teb_req.property_value)-1
                while teb_score == None:
                    if teb >= sq1_teb_req.property_value[k] or k == n:
                        teb_score = sq1_teb_req.score[k]
                    else:
                        teb_score = None
                        k = k + 1
                scores_top = pd.DataFrame(data={'oc': [oc_score], 'ph': [ph_score], 'teb': [teb_score], 'txt': [txt_score]}).T
                min = np.argmin(scores_top)
                topsoil_lowVal = scores_top.iloc[min, 0]
                topsoil_lowProp = scores_top.index[min]
                topsoil_high_mean = scores_top.loc[scores_top.index != topsoil_lowProp, :].mean()
                SQ1_scores.append(np.mean([topsoil_lowVal,topsoil_high_mean]))
            else:
                #combine property layer scores
                scores_bottom = pd.DataFrame(data={'oc': [oc_score], 'ph': [ph_score],  'txt': [txt_score]}).T
                min = np.argmin(scores_bottom)
                subsoil_lowVal = scores_bottom.iloc[min, 0]
                subsoil_lowProp = scores_bottom.index[min]
                subsoil_high_mean = scores_bottom.loc[scores_bottom.index != subsoil_lowProp, :].mean()
                SQ1_scores.append(np.mean([subsoil_lowVal,subsoil_high_mean]))
        
        depths = len([item for item in SQ1_scores if str(item) != 'nan'])
        wts = calc_depth_wts(depths, depthWt_type) 
        SQ1_score = np.nanmean([a * b for a, b in zip(SQ1_scores, wts)])

  # SQI 2  
    SQ2_scores = []
    for s in range(len(data.index)):
        layer = data.loc[s]
      #bs score
        sq2_bs_req = property_req.query('SQI_code == 2 & property == \'bs\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        bs = layer.BSAT
        bs_score = None
        t=0
        n = len(sq2_bs_req.property_value)-1
        while bs_score == None:
            if bs >= sq2_bs_req.property_value[t] or t == n:
                bs_score = sq2_bs_req.score[t]
            else:
                bs_score = None
                t = t + 1
      #texture score: texture score is only included in the 'High Input' class.
        if inputLevel == 'H':
            text_class_id = str(layer.text_class_id)
            sq2_text_req = texture_req.query('SQI_code == 2 & text_class_id ==' + text_class_id).reset_index(drop=True)
            txt_score = sq2_text_req.score[0]      
        else:
            txt_score = None

      #For topsoil:
      #add CECS score, then combine property layer scores
        if s == 0:
          #cecs score
            sq2_cecs_req = property_req.query('SQI_code == 2 & property == \'cecs\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecs = layer.CECS
            cecs_score = None
            l=0
            n = len(sq2_cecs_req.property_value)-1
            while cecs_score == None:
                if cecs >= sq2_cecs_req.property_value[l] or l == n:
                    cecs_score = sq2_cecs_req.score[l]
                else:
                    cecs_score = None
                    l = l + 1
            if inputLevel == 'H':
                scores_top = pd.DataFrame(data={'bs': [bs_score], 'cecs': [cecs_score], 'txt': [txt_score]}).T
            else:
                scores_top = pd.DataFrame(data={'bs': [bs_score], 'cecs': [cecs_score]}).T
            min = np.argmin(scores_top)
            topsoil_lowVal = scores_top.iloc[min, 0]
            topsoil_lowProp = scores_top.index[min]
            topsoil_high_mean = scores_top.loc[scores_top.index != topsoil_lowProp, :].mean()
            SQ2_scores.append(np.mean([topsoil_lowVal,topsoil_high_mean]))

      #For subsoil:
      #add CECc score and pH score, then combine property layer scores
        else:
          #ph score
            sq2_ph_req = property_req.query('SQI_code == 2 & property == \'ph\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            ph = layer.PHAQ
            ph_score = None
            j = 0
            n = len(sq2_ph_req.property_value)-1
            while ph_score == None:
                if ph >= sq2_ph_req.property_value[j] or j == n:
                    ph_score = sq2_ph_req.score[j]
                else:
                    ph_score = None
                    j = j + 1
          #cecc score
            sq2_cecc_req = property_req.query('SQI_code == 2 & property == \'cecc\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecc = layer.CECc
            cecc_score = None
            m=0
            n = len(sq2_cecc_req.property_value)-1
            while cecc_score == None:
                if cecc >= sq2_cecc_req.property_value[m] or m == n:
                    cecc_score = sq2_cecc_req.score[m]
                else:
                    cecc_score = None
                    m = m + 1
                    
            if inputLevel == 'H':
                scores_bottom = pd.DataFrame(data={'bs': [bs_score], 'cecc': [cecc_score], 'ph': [ph_score],  'txt': [txt_score]}).T
            else:
                scores_bottom = pd.DataFrame(data={'bs': [bs_score], 'cecc': [cecc_score], 'ph': [ph_score]}).T
            min = np.argmin(scores_bottom)
            subsoil_lowVal = scores_bottom.iloc[min, 0]
            subsoil_lowProp = scores_bottom.index[min]
            subsoil_high_mean = scores_bottom.loc[scores_bottom.index != subsoil_lowProp, :].mean()
            SQ2_scores.append(np.mean([subsoil_lowVal,subsoil_high_mean])) 

    depths = len([item for item in SQ2_scores if str(item) != 'nan'])
    wts = calc_depth_wts(depths, depthWt_type)        
    SQ2_score = np.nanmean([a * b for a, b in zip(SQ2_scores, wts)])

    
  # SQI 3  
    SQ3_scores = []
    
  #profile properties
    # soil depth
    sq3_rd_req = property_req.query('SQI_code == 3 & property == \'rd\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    rd = data.REF_DEPTH[0]
    sq3_rd_score = None
    j = 0
    n = len(sq3_rd_req.property_value)-1
    while sq3_rd_score == None:
        if rd >= sq3_rd_req.property_value[j] or j == n:
            sq3_rd_score = sq3_rd_req.score[j]
        else:
            sq3_rd_score = None
            j = j + 1
    
    # surface/subsurface degree of compactness
    sq3_db_req = property_req.query('SQI_code == 3 & property == \'db\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
    db_t = data.T_DC[0]
    sq3_dbT_score = None
    j = 0
    n = len(sq3_db_req.property_value)-1
    while sq3_dbT_score == None:
        if db_t <= sq3_db_req.property_value[j] or j == n:
            sq3_dbT_score = sq3_db_req.score[j]
        else:
            sq3_dbT_score = None
            j = j + 1
    
    db_s = data.S_DC[0]
    sq3_dbS_score = None
    j = 0
    n = len(sq3_db_req.property_value)-1
    while sq3_dbS_score == None:
        if db_s <= sq3_db_req.property_value[j] or j == n:
            sq3_dbS_score = sq3_db_req.score[j]
        else:
            sq3_dbS_score = None
            j = j + 1
            
  #veric/gelic/petric
    # The petric condition ratings are not found in the soil profile ratings but is found in the phase rating table (Phase number for petric = 3)
    ADD_PROP = data.ADD_PROP[0] # ADD_PROP = 0: None; ADD_PROP = 1: Petric; ADD_PROP = 2: Gelic; ADD_PROP = 3: Vertic;
    
    #Vertic properties
    
    if ADD_PROP == 3:
        sq3_ver_req = property_req.query('SQI_code == 3 & property == \'ver\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        sq3_ver_score = sq3_ver_req.score[0] 
    else:
        sq3_ver_score = 100

    #Gelic properties
    if ADD_PROP == 2:
        sq3_gel_req = property_req.query('SQI_code == 3 & property == \'gel\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        sq3_gel_score = sq3_gel_req.score[0] 
    else:
        sq3_gel_score = 100
    
    #Petric properties
    if ADD_PROP == 1:
        sq3_pet_req = phase_req.query('SQI_code == 3 & property == \'PHASE\' & phase_id == 3').reset_index(drop=True)
        sq3_pet_score = sq3_pet_req.score[0] 
    else:
        sq3_pet_score = 100
      
  #phases
    phase1 = data.PHASE1[0]
    if phase1 == 0:
        sq3_phase1_score = 100
    else:
        sq3_phase1_req = phase_req.query('SQI_code == 3 & property == \'PHASE\' & phase_id ==' + str(phase1)).reset_index(drop=True)
        sq3_phase1_score = sq3_phase1_req.score[0] 
    
    phase2 = data.PHASE2[0]
    if phase2 == 0:
        sq3_phase2_score = 100
    else:
        sq3_phase2_req = phase_req.query('SQI_code == 3 & property == \'PHASE\' & phase_id ==' + str(phase2)).reset_index(drop=True)
        sq3_phase2_score = sq3_phase2_req.score[0]  

  #roots
    roots = data.ROOTS[0]
    sq3_roots_req = phase_req.query('SQI_code == 3 & property == \'ROOTS\' & phase_id ==' + str(roots)).reset_index(drop=True)
    sq3_roots_score = sq3_roots_req.score[0]
    
  #Impermeable layer
    il = data.IL[0]
    sq3_il_req = phase_req.query('SQI_code == 3 & property == \'IL\' & phase_id ==' + str(il)).reset_index(drop=True)
    sq3_il_score = sq3_il_req.score[0]
    
  #soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
     #texture score
        text_class_id = str(layer.text_class_id)
        sq3_text_req = texture_req.query('SQI_code == 3 & text_class_id ==' + text_class_id).reset_index(drop=True)
        sq3_txt_score = sq3_text_req.score[0]   

     #cf score
        sq3_cf_req = property_req.query('SQI_code == 3 & property == \'cf\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        cf = layer.CFRAG
        sq3_cf_score = None
        t=0
        n = len(sq3_cf_req.property_value)-1
        while sq3_cf_score == None:
            if cf >= sq3_cf_req.property_value[t] or t == n:
                sq3_cf_score = sq3_cf_req.score[t]
            else:
                sq3_cf_score = None
                t = t + 1  

        if s == 0:
            sq3_scores_pd = pd.DataFrame(data={'txt': [sq3_txt_score], 'cf': [sq3_cf_score], 'db': [sq3_dbT_score],  'ver': [sq3_ver_score], 'gel': [sq3_gel_score], 'pet': [sq3_pet_score], 'phase1': [sq3_phase1_score], 'phase2': [sq3_phase2_score], 'roots': [sq3_roots_score],'il': [sq3_il_score]}).T
        else:
            sq3_scores_pd = pd.DataFrame(data={'txt': [sq3_txt_score], 'cf': [sq3_cf_score], 'db': [sq3_dbS_score],  'ver': [sq3_ver_score], 'gel': [sq3_gel_score], 'pet': [sq3_pet_score], 'phase1': [sq3_phase1_score], 'phase2': [sq3_phase2_score], 'roots': [sq3_roots_score],'il': [sq3_il_score]}).T
        min = np.argmin(sq3_scores_pd)
        sq3_scores_lowProp = sq3_scores_pd.index[min]
        sq3_scores_lowVal = sq3_scores_pd.iloc[min, 0]
        SQ3_scores.append(sq3_rd_score*(sq3_scores_lowVal/100))
        
    depths = len([item for item in SQ3_scores if str(item) != 'nan'])
    wts = calc_depth_wts(depths, depthWt_type)        
    SQ3_score = np.nanmean([a * b for a, b in zip(SQ3_scores, wts)])
    
  # SQI 4  
  
  #SWR
    swr = data.SWR[0]
    sq4_swr_req = phase_req.query('SQI_code == 4 & property == \'SWR\' & phase_id ==' + str(swr)).reset_index(drop=True)
    sq4_swr_score = sq4_swr_req.score[0]
    
  #Impermeable layer
    il = data.IL[0]
    sq4_il_req = phase_req.query('SQI_code == 4 & property == \'IL\' & phase_id ==' + str(il)).reset_index(drop=True)
    sq4_il_score = sq4_il_req.score[0]
  
  #Drainage
    drain_id = data.DrainNum[0]
    pscl_id = data['PSCL_ID'].max()
    sq4_drain_req = drainage_req.query('SQI_code == 4 & PSCL_ID == \'' + str(pscl_id) + '\' & DrainNum ==' + str(drain_id)).reset_index(drop=True)
    sq4_drain_score = sq4_drain_req.score[0]

  #phases
    phase1 = data.PHASE1[0]
    if phase1 == 0:
        sq4_phase1_score = 100
    else:
        sq4_phase1_req = phase_req.query('SQI_code == 4 & property == \'PHASE\' & phase_id ==' + str(phase1)).reset_index(drop=True)
        if len(sq4_phase1_req) == 0:
            sq4_phase1_score = 100
        else:
            sq4_phase1_score = sq4_phase1_req.score[0] 
    
    phase2 = data.PHASE2[0]
    if phase2 == 0:
        sq4_phase2_score = 100
    else:
        sq4_phase2_req = phase_req.query('SQI_code == 4 & property == \'PHASE\' & phase_id ==' + str(phase2)).reset_index(drop=True)
        if len(sq4_phase2_req) == 0:
            sq4_phase2_score = 100
        else:
            sq4_phase2_score = sq4_phase2_req.score[0] 
           
    sq4_scores_pd = pd.DataFrame(data={'swr': [sq4_swr_score],'il': [sq4_il_score], 'drain': [sq4_drain_score], 'phase1': [sq4_phase1_score], 'phase2': [sq4_phase2_score]}).T
    min = np.argmin(sq4_scores_pd)
    sq4_scores_lowProp = sq4_scores_pd.index[min]
    sq4_scores_lowVal = sq4_scores_pd.iloc[min, 0]
    SQ4_score = sq4_scores_lowVal

  # SQI 5
    SQ5_scores = []
  #phases
    phase1 = data.PHASE1[0]
    if phase1 == 0:
        sq5_phase1_score = 100
    else:
        sq5_phase1_req = phase_req.query('SQI_code == 5 & property == \'PHASE\' & phase_id ==' + str(phase1)).reset_index(drop=True)
        if len(sq5_phase1_req) == 0:
            sq5_phase1_score = 100
        else:
            sq5_phase1_score = sq5_phase1_req.score[0]
    phase2 = data.PHASE2[0]
    if phase2 == 0:
        sq5_phase2_score = 100
    else:
        sq5_phase2_req = phase_req.query('SQI_code == 5 & property == \'PHASE\' & phase_id ==' + str(phase2)).reset_index(drop=True)
        if len(sq5_phase2_req) == 0:
            sq5_phase2_score = 100
        else:
            sq5_phase2_score = sq5_phase2_req.score[0]
          
  #soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
    #check for missing data at each depth and remove depths with missing data from final score
        esp = layer.ESP
        ec = layer.ELCO
        if np.isnan(esp) or np.isnan(ec):
            SQ5_scores.append(float("NaN"))
        else:
            #esp score
            sq5_esp_req = property_req.query('SQI_code == 5 & property == \'esp\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
            sq5_esp_score = None
            t=0
            n = len(sq5_esp_req.property_value)-1
            while sq5_esp_score == None:
                if esp <= sq5_esp_req.property_value[t] or t == n:
                    sq5_esp_score = sq5_esp_req.score[t]
                else:
                    sq5_esp_score = None
                    t = t + 1 
            #ec score
            sq5_ec_req = property_req.query('SQI_code == 5 & property == \'ec\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
            sq5_ec_score = None
            t=0
            n = len(sq5_ec_req.property_value)-1
            while sq5_ec_score == None:
                if ec <= sq5_ec_req.property_value[t] or t == n:
                    sq5_ec_score = sq5_ec_req.score[t]
                else:
                    sq5_ec_score = None
                    t = t + 1
            esp_ec_score = sq5_ec_score * (sq5_esp_score/100)
            sq5_scores_pd = pd.DataFrame(data={'esp_ec': [esp_ec_score], 'phase1': [sq5_phase1_score], 'phase2': [sq5_phase2_score]}).T
            sq5_min = np.argmin(sq5_scores_pd)
            sq5_scores_lowVal = sq5_scores_pd.iloc[sq5_min, 0]
            SQ5_scores.append(sq5_scores_lowVal)
            
    depths = len([item for item in SQ5_scores if str(item) != 'nan'])
    wts = calc_depth_wts(depths, depthWt_type)        
    SQ5_score = np.nanmean([a * b for a, b in zip(SQ5_scores, wts)])


  # SQI 6
    SQ6_scores = []
  #phases
    phase1 = data.PHASE1[0]
    if phase1 == 0:
        sq6_phase1_score = 100
    else:
        sq6_phase1_req = phase_req.query('SQI_code == 6 & property == \'PHASE\' & phase_id ==' + str(phase1)).reset_index(drop=True)
        if len(sq6_phase1_req) == 0:
            sq6_phase1_score = 100
        else:
            sq6_phase1_score = sq6_phase1_req.score[0]
    
    phase2 = data.PHASE2[0]
    if phase2 == 0:
        sq6_phase2_score = 100
    else:
        sq6_phase2_req = phase_req.query('SQI_code == 6 & property == \'PHASE\' & phase_id ==' + str(phase2)).reset_index(drop=True)
        if len(sq6_phase2_req) == 0:
            sq6_phase2_score = 100
        else:
            sq6_phase2_score = sq6_phase2_req.score[0]
          
  #soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
    #ccb score
        sq6_ccb_req = property_req.query('SQI_code == 6 & property == \'ca\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        ccb = layer.TCEQ
        sq6_ccb_score = None
        t=0
        n = len(sq6_ccb_req.property_value)-1
        while sq6_ccb_score == None:
            if ccb <= sq6_ccb_req.property_value[t] or t == n:
                sq6_ccb_score = sq6_ccb_req.score[t]
            else:
                sq6_ccb_score = None
                t = t + 1 
    #gyp score
        sq6_gyp_req = property_req.query('SQI_code == 6 & property == \'gy\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        gyp = layer.GYPS
        sq6_gyp_score = None
        t=0
        n = len(sq6_gyp_req.property_value)-1
        while sq6_gyp_score == None:
            if gyp <= sq6_gyp_req.property_value[t] or t == n:
                sq6_gyp_score = sq6_gyp_req.score[t]
            else:
                sq6_gyp_score = None
                t = t + 1
        ccb_gyp_score = sq6_gyp_score * (sq6_ccb_score/100)
        sq6_scores_pd = pd.DataFrame(data={'ccb_gyp': [ccb_gyp_score], 'phase1': [sq6_phase1_score], 'phase2': [sq6_phase2_score]}).T
        sq6_min = np.argmin(sq6_scores_pd)
        sq6_scores_lowVal = sq6_scores_pd.iloc[sq6_min, 0]
        SQ6_scores.append(sq6_scores_lowVal)
        
    depths = len([item for item in SQ6_scores if str(item) != 'nan'])
    wts = calc_depth_wts(depths, depthWt_type)        
    SQ6_score = np.nanmean([a * b for a, b in zip(SQ6_scores, wts)])    
    
  # SQI 7  
    SQ7_scores = []
  #profile properties
    # soil depth
    sq7_rd_req = property_req.query('SQI_code == 7 & property == \'rd\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    rd = data.REF_DEPTH[0]
    sq7_rd_score = None
    j = 0
    n = len(sq7_rd_req.property_value)-1
    while sq7_rd_score == None:
        if rd >= sq7_rd_req.property_value[j] or j == n:
            sq7_rd_score = sq7_rd_req.score[j]
        else:
            sq7_rd_score = None
            j = j + 1
    
    # surface/subsurface degree of compactness
    sq7_db_req = property_req.query('SQI_code == 7 & property == \'db\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
    db_t = data.T_DC[0]
    sq7_dbT_score = None
    j = 0
    n = len(sq7_db_req.property_value)-1
    while sq7_dbT_score == None:
        if db_t <= sq7_db_req.property_value[j] or j == n:
            sq7_dbT_score = sq7_db_req.score[j]
        else:
            sq7_dbT_score = None
            j = j + 1
    
    db_s = data.S_DC[0]
    sq7_dbS_score = None
    j = 0
    n = len(sq7_db_req.property_value)-1
    while sq7_dbS_score == None:
        if db_s <= sq7_db_req.property_value[j] or j == n:
            sq7_dbS_score = sq7_db_req.score[j]
        else:
            sq7_dbS_score = None
            j = j + 1
            
  #veric/gelic/petric
    ADD_PROP = data.ADD_PROP[0]
    #Vertic properties
    sq7_ver_req = property_req.query('SQI_code == 7 & property == \'ver\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    if ADD_PROP == 3:
        sq7_ver_score = sq7_ver_req.score[0] 
    else:
        sq7_ver_score = 100

    #Gelic properties
    sq7_gel_req = property_req.query('SQI_code == 7 & property == \'gel\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    if ADD_PROP == 2:
        sq7_gel_score = sq7_gel_req.score[0] 
    else:
        sq7_gel_score = 100
    
    #Petric properties
    if ADD_PROP == 1:
        sq7_pet_req = phase_req.query('SQI_code == 7 & property == \'PHASE\' & phase_id == 3').reset_index(drop=True)
        sq7_pet_score = sq7_pet_req.score[0] 
    else:
        sq7_pet_score = 100
      
  #phases
    phase1 = data.PHASE1[0]
    if phase1 == 0:
        sq7_phase1_score = 100
    else:
        sq7_phase1_req = phase_req.query('SQI_code == 7 & property == \'PHASE\' & phase_id ==' + str(phase1)).reset_index(drop=True)
        sq7_phase1_score = sq7_phase1_req.score[0] 
    
    phase2 = data.PHASE2[0]
    if phase2 == 0:
        sq7_phase2_score = 100
    else:
        sq7_phase2_req = phase_req.query('SQI_code == 7 & property == \'PHASE\' & phase_id ==' + str(phase2)).reset_index(drop=True)
        sq7_phase2_score = sq7_phase2_req.score[0]  

  #roots
    roots = data.ROOTS[0]
    sq7_roots_req = phase_req.query('SQI_code == 7 & property == \'ROOTS\' & phase_id ==' + str(roots)).reset_index(drop=True)
    sq7_roots_score = sq7_roots_req.score[0]
    
  #Impermeable layer
    il = data.IL[0]
    sq7_il_req = phase_req.query('SQI_code == 7 & property == \'IL\' & phase_id ==' + str(il)).reset_index(drop=True)
    sq7_il_score = sq7_il_req.score[0]
    
  #soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
     #texture score
        text_class_id = str(layer.text_class_id)
        sq7_text_req = texture_req.query('SQI_code == 3 & text_class_id ==' + text_class_id).reset_index(drop=True)
        sq7_txt_score = sq7_text_req.score[0]   

    #cf score
        sq7_cf_req = property_req.query('SQI_code == 7 & property == \'cf\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        cf = layer.CFRAG
        sq7_cf_score = None
        t=0
        n = len(sq7_cf_req.property_value)-1
        while sq7_cf_score == None:
            if cf >= sq7_cf_req.property_value[t] or t == n:
                sq7_cf_score = sq7_cf_req.score[t]
            else:
                sq7_cf_score = None
                t = t + 1  

        if s == 0:
            sq7_scores_pd = pd.DataFrame(data={'rd': [sq7_rd_score], 'txt': [sq7_txt_score], 'cf': [sq7_cf_score], 'db': [sq7_dbT_score],  'ver': [sq7_ver_score], 'gel': [sq7_gel_score], 'pet': [sq7_pet_score], 'phase1': [sq7_phase1_score], 'phase2': [sq7_phase2_score], 'roots': [sq7_roots_score],'il': [sq7_il_score]}).T
        else:
            sq7_scores_pd = pd.DataFrame(data={'rd': [sq7_rd_score], 'txt': [sq7_txt_score], 'cf': [sq7_cf_score], 'db': [sq7_dbS_score],  'ver': [sq7_ver_score], 'gel': [sq7_gel_score], 'pet': [sq7_pet_score], 'phase1': [sq7_phase1_score], 'phase2': [sq7_phase2_score], 'roots': [sq7_roots_score],'il': [sq7_il_score]}).T
        sq7_min = np.argmin(sq7_scores_pd)
        sq7_scores_lowVal = sq7_scores_pd.iloc[sq7_min, 0]
        sq7_scores_lowProp = sq7_scores_pd.index[sq7_min]
        sq7_scores_high_mean = sq7_scores_pd.loc[sq7_scores_pd.index != sq7_scores_lowProp, :].mean()
        SQ7_scores.append(np.mean([sq7_scores_lowVal,sq7_scores_high_mean]))
  
    depths = len([item for item in SQ7_scores if str(item) != 'nan'])
    wts = calc_depth_wts(depths, depthWt_type)        
    SQ7_score = np.nanmean([a * b for a, b in zip(SQ7_scores, wts)])
    
    #Soil Rating
    #Low input farming:
    if inputLevel == 'L':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score],'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score]})
        group_scores = group_scores.reset_index(drop=True)
        group_scores_min = np.argmin(group_scores)
        group_scores_scores_lowVal = group_scores.iloc[0, group_scores_min]
        SR = SQ1_score * (SQ3_score/100) * (group_scores_scores_lowVal/100)
    elif inputLevel == 'I':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score],'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score]})
        group_scores = group_scores.reset_index(drop=True)
        group_scores_min = np.argmin(group_scores)
        group_scores_lowVal = group_scores.iloc[0, group_scores_min]
        SR = 0.5 * (SQ1_score + SQ2_score)  * (SQ3_score/100) * (group_scores_lowVal/100)
    elif inputLevel == 'H':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score],'SQ7': [SQ7_score]})
        group_scores = group_scores.reset_index(drop=True)
        group_scores_min = np.argmin(group_scores)
        group_scores_scores_lowVal = group_scores.iloc[0, group_scores_min]
        SR = SQ2_score * (SQ3_score/100) * (group_scores_scores_lowVal/100)
    SQI_scores = pd.DataFrame(data={'SQ1': [SQ1_score],'SQ2': [SQ2_score],'SQ3': [SQ3_score],'SQ4': [SQ4_score],'SQ5': [SQ5_score], 'SQ6': [SQ6_score],'SQ7': [SQ7_score], 'SR': [SR], 'Input Level': inputLevel, 'Soil Tax': data.SU_name[0]})
    return(SQI_scores)    

