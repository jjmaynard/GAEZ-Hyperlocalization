




#####################################################################################################
#                                       back-end database functions                                 #
#####################################################################################################
def get_datastore_connection(host='127.0.0.1', user='root', password='root', database='apex'):
    """
    Establishes a connection to a MySQL database.
    
    Parameters:
        host (str): The host address of the database.
        user (str): The username for authentication.
        password (str): The password for authentication.
        database (str): The name of the database to connect to.
        
    Returns:
        Connection object if successful, None if an error occurs.
    """
    try:
        import MySQLdb
        conn = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
        return conn
    except Exception as err:
        print(f"Error while connecting to the database: {err}")
        return None


def getWISE30sec_data(MUGLB_NEW_Select):
    """
    Retrieves specific data from the 'wise_soil_data' table based on the given selection criteria.
    
    Parameters:
        MUGLB_NEW_Select (list): List of values to filter the data.
        
    Returns:
        Pandas DataFrame containing the filtered data, or None if an error occurs.
    """
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        
        # Define the SQL query using parameterized placeholders
        placeholders = ', '.join(['%s'] * len(MUGLB_NEW_Select))
        sql = f'SELECT MUGLB_NEW, COMPID, id, MU_GLOBAL, NEWSUID, SCID, PROP, CLAF, PRID, Layer, TopDep, BotDep, CFRAG, SDTO, STPC, CLPC, CECS, PHAQ, ELCO, SU_name, FAO_SYS FROM wise_soil_data WHERE MUGLB_NEW IN ({placeholders})'
        
        # Execute the query
        cur.execute(sql, MUGLB_NEW_Select)
        results = cur.fetchall()
        
        # Define the column names
        columns = ['MUGLB_NEW', 'COMPID', 'id', 'MU_GLOBAL', 'NEWSUID', 'SCID', 'PROP', 'CLAF', 'PRID', 'Layer', 'TopDep', 'BotDep', 'CFRAG', 'SDTO', 'STPC', 'CLPC', 'CECS', 'PHAQ', 'ELCO', 'SU_name', 'FAO_SYS']
        
        # Convert the results to a DataFrame
        data = pd.DataFrame(list(results), columns=columns)
        
        return data
    except Exception as err:
        print(f"Error while retrieving data: {err}")
        return None
    finally:
        # Ensure the connection is closed
        conn.close()

        return None

def getWISE30sec_comp_data(COMPID):
    """
    Retrieves specific data from the 'wise_soil_data' table based on the given COMPID.
    
    Parameters:
        COMPID: The COMPID value to filter the data.
        
    Returns:
        Pandas DataFrame containing the filtered data, or None if an error occurs.
    """
    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        
        # Define the SQL query using parameterized placeholders
        sql = ('SELECT MUGLB_NEW, COMPID, id, MU_GLOBAL, NEWSUID, SU_name, SCID, PROP, CLAF, PRID, Layer, TopDep, BotDep, Drain, DrainNum, '
               'CFRAG, SDTO, STPC, CLPC, PSCL, BULK, TAWC, ORGC, TOTN, CECS, CECc, ECEC, TEB, BSAT, ALSA, ESP, PHAQ, TCEQ, GYPS, ELCO, '
               'PHASE1, PHASE2, ROOTS, IL, SWR, ADD_PROP, T_DC, S_DC, T_BULK_DEN, T_REF_BULK, S_BULK_DEN, S_REF_BULK, text_class, text_class_id, REF_DEPTH '
               'FROM wise_soil_data WHERE COMPID = %s')
        
        # Execute the query
        cur.execute(sql, (COMPID,))
        results = cur.fetchall()
        
        # Define the column names
        columns = ['MUGLB_NEW', 'COMPID', 'id', 'MU_GLOBAL', 'NEWSUID', 'SU_name', 'SCID', 'PROP', 'CLAF', 'PRID', 'Layer', 'TopDep', 'BotDep', 'Drain', 'DrainNum', 'CFRAG', 'SDTO', 'STPC', 'CLPC', 'PSCL', 'BULK', 'TAWC', 'ORGC', 'TOTN', 'CECS', 'CECc', 'ECEC', 'TEB', 'BSAT', 'ALSA', 'ESP', 'PHAQ', 'TCEQ', 'GYPS', 'ELCO', 'PHASE1', 'PHASE2', 'ROOTS', 'IL', 'SWR', 'ADD_PROP', 'T_DC', 'S_DC', 'T_BULK_DEN', 'T_REF_BULK', 'S_BULK_DEN', 'S_REF_BULK', 'text_class', 'text_class_id', 'REF_DEPTH']
        
        # Convert the results to a DataFrame
        data = pd.DataFrame(list(results), columns=columns)
        
        return data
    except Exception as err:
        print(f"Error while retrieving data: {err}")
        return None
    finally:
        # Ensure the connection is closed
        conn.close()



def getGAEZ_requirements(CROP_ID, Input_Level_List, requirement_type):
    """
    Retrieves specific requirements from the GAEZ database based on the given CROP_ID, input levels, and requirement type.
    
    Parameters:
        CROP_ID: The ID of the crop to filter the data.
        Input_Level_List (list): List of input levels to filter the data.
        requirement_type (str): Type of requirement to retrieve. Must be one of ['profile', 'texture', 'terrain', 'phase', 'drainage'].

    Returns:
        Pandas DataFrame containing the filtered data, or None if an error occurs.
    """
    # Define the table and columns based on the requirement type
    if requirement_type == 'profile':
        table_name = 'GAEZ_profile_req_rf'
        columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 'property_value', 'property', 'unit', 'property_id', 'property_text']
    elif requirement_type == 'texture':
        table_name = 'GAEZ_text_req_rf'
        columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 'text_class_id', 'text_class']
    elif requirement_type == 'terrain':
        table_name = 'GAEZ_terrain_req_rf'
        columns = ['CROP_ID', 'CROP', 'crop_group', 'input_level', 'FM_class', 'slope_class', 'slope_class_id', 'rating', 'rating_text']
    elif requirement_type == 'phase':
        table_name = 'GAEZ_phase_req_rf'
        columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'property', 'phase_id', 'phase', 'score']
    elif requirement_type == 'drainage':
        table_name = 'GAEZ_drainage_req_rf'
        columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'PSCL_HWSD', 'DrainNum', 'Drain', 'score']
    else:
        print("Invalid requirement type.")
        return None

    try:
        conn = getDataStore_Connection()
        cur = conn.cursor()
        
        # Define the SQL query using parameterized placeholders
        placeholders = ', '.join(['%s'] * len(Input_Level_List))
        sql = f'SELECT {", ".join(columns)} FROM {table_name} WHERE CROP_ID = %s AND input_level IN ({placeholders})'
        
        # Execute the query
        cur.execute(sql, [CROP_ID] + Input_Level_List)
        results = cur.fetchall()
        
        # Convert the results to a DataFrame
        data = pd.DataFrame(list(results), columns=columns)
        
        return data
    except Exception as err:
        print(f"Error while retrieving data: {err}")
        return None
    finally:
        # Ensure the connection is closed
        conn.close()



#####################################################################################################
#                                back-end data processing functions                                 #
#####################################################################################################

def agg_data_layer_SQI(data, bottom, sd=2, depth=False):
    if np.isnan(bottom) or bottom == 0:
        return (pd.Series([np.nan]), pd.Series([np.nan])) if depth else pd.Series([np.nan])

    depth_intervals = [20, 40, 60, 80, 100, 120]
    data_d, d_lyrs = [], []

    for i, interval in enumerate(depth_intervals):
        if bottom <= interval:
            data_d.append(round(data[0:bottom].mean(), sd))
            d_lyrs.append(bottom)
            break
        else:
            data_d.append(round(data[0:interval].mean(), sd))
            d_lyrs.append(interval)
            data = data[interval:]
            bottom -= interval

    index_labels = [f'sl{i+1}' for i in range(len(data_d))]
    data_d = pd.Series(data_d, index=index_labels)
    d_lyrs = pd.Series(d_lyrs, index=index_labels)

    return (data_d, d_lyrs) if depth else data_d

def gettt(row, sand=None, silt=None, clay=None):
    if sand is None or silt is None or clay is None:
        sand, silt, clay = row['sandtotal_r'], row['silttotal_r'], row['claytotal_r']

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

def getTextGroup(field):
    if field is None:
        return np.nan
    texture_group_map = {
        'C': ["sand", "loamy sand", "sandy loam"],
        'M': ["sandy clay loam", "loam", "clay loam", "silt loam", "silt", "silty clay loam"],
        'F': ["sandy clay", "silty clay", "clay"]
    }
    return next((key for key, value in texture_group_map.items() if field.lower() in value), np.nan)

def get_property_by_texture(texture, property_map):
    if texture is None:
        return np.nan
    return property_map.get(texture.lower(), np.nan)

def getSand(field):
    sand_map = {
        "sand": 92.0, "loamy sand": 80.0, "sandy loam": 61.5, "sandy clay loam": 62.5,
        "loam": 37.5, "silt": 10.0, "silt loam": 25.0, "silty clay loam": 10.0,
        "clay loam": 32.5, "sandy clay": 55.0, "silty clay": 10.0, "clay": 22.5
    }
    return get_property_by_texture(field, sand_map)

def getClay(field):
    clay_map = {
        "sand": 5.0, "loamy sand": 7.5, "sandy loam": 10.0, "sandy clay loam": 27.5,
        "loam": 17.0, "silt": 6.0, "silt loam": 13.5, "silty clay loam": 33.5,
        "clay loam": 33.5, "sandy clay": 45.0, "silty clay": 50.0, "clay": 70.0
    }
    return get_property_by_texture(field, clay_map)

def getCF_fromClass(cf):
    cf_map = {"0-1%": 0, "1-15%": 8, "15-35%": 25, "35-60%": 48, ">60%": 80}
    return cf_map.get(cf, np.nan)

def getTXT_id(texture):
    texture_id_map = {
        "sand": 12, "loamy sand": 11, "sandy loam": 10, "sandy clay loam": 9,
        "loam": 8, "silt": 5, "silt loam": 6, "silty clay loam": 3,
        "clay loam": 4, "sandy clay": 7, "silty clay": 2, "clay": 1
    }
    return get_property_by_texture(texture, texture_id_map) 


#####################################################################################################
#                                SQI functions                                 #
#####################################################################################################

def calculate_SQ1(data, property_req, texture_req, inputLevel, wts):
    if inputLevel == 'H':
        return 'NA'

    SQ1_scores = []
    sq1_oc_req = property_req.query('SQI_code == 1 & property == "oc"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    sq1_ph_req = property_req.query('SQI_code == 1 & property == "ph"').sort_values(by='property_value', ascending=False).reset_index(drop=True)

    for s, layer in data.iterrows():
        # oc score
        oc = layer.ORGC
        oc_score = next((score for score, value in zip(sq1_oc_req['score'], sq1_oc_req['property_value']) if oc >= value), sq1_oc_req['score'].iloc[-1])

        # ph score
        ph = layer.PHAQ
        ph_score = next((score for score, value in zip(sq1_ph_req['score'], sq1_ph_req['property_value']) if ph >= value), sq1_ph_req['score'].iloc[-1])

        # texture score
        text_class_id = str(layer.text_class_id)
        txt_score = texture_req.query(f'SQI_code == 1 & text_class_id == {text_class_id}')['score'].iloc[0]

        # For topsoil only
        if s == 0:
            sq1_teb_req = property_req.query('SQI_code == 1 & property == "teb"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            teb = layer.TEB
            teb_score = next((score for score, value in zip(sq1_teb_req['score'], sq1_teb_req['property_value']) if teb >= value), sq1_teb_req['score'].iloc[-1])
            scores_top = [oc_score, ph_score, teb_score, txt_score]
        else:
            # Combine property layer scores
            scores_bottom = [oc_score, ph_score, txt_score]
        
        scores = scores_top if s == 0 else scores_bottom
        min_score = min(scores)
        high_mean = (sum(scores) - min_score) / (len(scores) - 1)
        SQ1_scores.append(np.mean([min_score, high_mean]))

    return np.mean([a * b for a, b in zip(SQ1_scores, wts)])


def calculate_SQ2(data, property_req, texture_req, wts, inputLevel):
    SQ2_scores = []
    for s in range(len(data.index)):
        layer = data.loc[s]
        # bs score
        sq2_bs_req = property_req.query('SQI_code == 2 & property == \'bs\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        bs = layer.BSAT
        bs_score = None
        t = 0
        n = len(sq2_bs_req.property_value) - 1
        while bs_score is None:
            if bs >= sq2_bs_req.property_value[t] or t == n:
                bs_score = sq2_bs_req.score[t]
            else:
                bs_score = None
                t = t + 1
        # texture score: texture score is only included in the 'High Input' class.
        if inputLevel == 'H':
            text_class_id = str(layer.text_class_id)
            sq2_text_req = texture_req.query('SQI_code == 2 & text_class_id ==' + text_class_id).reset_index(drop=True)
            txt_score = sq2_text_req.score[0]
        else:
            txt_score = None

        # For topsoil:
        # add CECS score, then combine property layer scores
        if s == 0:
            # cecs score
            sq2_cecs_req = property_req.query('SQI_code == 2 & property == \'cecs\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecs = layer.CECS
            cecs_score = None
            l = 0
            n = len(sq2_cecs_req.property_value) - 1
            while cecs_score is None:
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
            SQ2_scores.append(np.mean([topsoil_lowVal, topsoil_high_mean]))

        # For subsoil:
        # add CECc score and pH score, then combine property layer scores
        else:
            # ph score
            sq2_ph_req = property_req.query('SQI_code == 2 & property == \'ph\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            ph = layer.PHAQ
            ph_score = None
            j = 0
            n = len(sq2_ph_req.property_value) - 1
            while ph_score is None:
                if ph >= sq2_ph_req.property_value[j] or j == n:
                    ph_score = sq2_ph_req.score[j]
                else:
                    ph_score = None
                    j = j + 1
            # cecc score
            sq2_cecc_req = property_req.query('SQI_code == 2 & property == \'cecc\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecc = layer.CECc
            cecc_score = None
            m = 0
            n = len(sq2_cecc_req.property_value) - 1
            while cecc_score is None:
                if cecc >= sq2_cecc_req.property_value[m] or m == n:
                    cecc_score = sq2_cecc_req.score[m]
                else:
                    cecc_score = None
                    m = m + 1

            if inputLevel == 'H':
                scores_bottom = pd.DataFrame(data={'bs': [bs_score], 'cecc': [cecc_score], 'ph': [ph_score], 'txt': [txt_score]}).T
            else:
                scores_bottom = pd.DataFrame(data={'bs': [bs_score], 'cecc': [cecc_score], 'ph': [ph_score]}).T
            min = np.argmin(scores_bottom)
            subsoil_lowVal = scores_bottom.iloc[min, 0]
            subsoil_lowProp = scores_bottom.index[min]
            subsoil_high_mean = scores_bottom.loc[scores_bottom.index != subsoil_lowProp, :].mean()
            SQ2_scores.append(np.mean([subsoil_lowVal, subsoil_high_mean]))

    SQ2_score = np.mean([a * b for a, b in zip(SQ2_scores, wts)])
    return SQ2_score

def calculate_SQ3(data, property_req, texture_req, phase_req, wts):
    SQ3_scores = []
    
    # profile properties
    # soil depth
    sq3_rd_req = property_req.query('SQI_code == 3 & property == \'rd\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    rd = data.REF_DEPTH[0]
    sq3_rd_score = None
    j = 0
    n = len(sq3_rd_req.property_value)-1
    while sq3_rd_score is None:
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
    while sq3_dbT_score is None:
        if db_t <= sq3_db_req.property_value[j] or j == n:
            sq3_dbT_score = sq3_db_req.score[j]
        else:
            sq3_dbT_score = None
            j = j + 1
    
    db_s = data.S_DC[0]
    sq3_dbS_score = None
    j = 0
    n = len(sq3_db_req.property_value)-1
    while sq3_dbS_score is None:
        if db_s <= sq3_db_req.property_value[j] or j == n:
            sq3_dbS_score = sq3_db_req.score[j]
        else:
            sq3_dbS_score = None
            j = j + 1
            
    # veric/gelic/petric
    ADD_PROP = data.ADD_PROP[0]
    # Vertic properties
    sq3_ver_req = property_req.query('SQI_code == 3 & property == \'ver\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    if ADD_PROP == 3:
        sq3_ver_score = sq3_ver_req.score[0] 
    else:
        sq3_ver_score = 100

    # Gelic properties
    sq3_gel_req = property_req.query('SQI_code == 3 & property == \'gel\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    if ADD_PROP == 2:
        sq3_gel_score = sq3_gel_req.score[0] 
    else:
        sq3_gel_score = 100
    
    # phases
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

    # roots
    roots = data.ROOTS[0]
    sq3_roots_req = phase_req.query('SQI_code == 3 & property == \'ROOTS\' & phase_id ==' + str(roots)).reset_index(drop=True)
    sq3_roots_score = sq3_roots_req.score[0]
    
    # Impermeable layer
    il = data.IL[0]
    sq3_il_req = phase_req.query('SQI_code == 3 & property == \'IL\' & phase_id ==' + str(il)).reset_index(drop=True)
    sq3_il_score = sq3_il_req.score[0]
    
    # soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
        # texture score
        text_class_id = str(layer.text_class_id)
        sq3_text_req = texture_req.query('SQI_code == 3 & text_class_id ==' + text_class_id).reset_index(drop=True)
        sq3_txt_score = sq3_text_req.score[0]   

        # cf score
        sq3_cf_req = property_req.query('SQI_code == 3 & property == \'cf\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        cf = layer.CFRAG
        sq3_cf_score = None
        t = 0
        n = len(sq3_cf_req.property_value)-1
        while sq3_cf_score is None:
            if cf >= sq3_cf_req.property_value[t] or t == n:
                sq3_cf_score = sq3_cf_req.score[t]
            else:
                sq3_cf_score = None
                t = t + 1  

        if s == 0:
            sq3_scores_pd = pd.DataFrame(data={'txt': [sq3_txt_score], 'cf': [sq3_cf_score], 'db': [sq3_dbT_score], 'ver': [sq3_ver_score], 'gel': [sq3_gel_score], 'phase1': [sq3_phase1_score], 'phase2': [sq3_phase2_score], 'roots': [sq3_roots_score],'il': [sq3_il_score]}).T
        else:
            sq3_scores_pd = pd.DataFrame(data={'txt': [sq3_txt_score], 'cf': [sq3_cf_score], 'db': [sq3_dbS_score], 'ver': [sq3_ver_score], 'gel': [sq3_gel_score], 'phase1': [sq3_phase1_score], 'phase2': [sq3_phase2_score], 'roots': [sq3_roots_score],'il': [sq3_il_score]}).T
        min = np.argmin(sq3_scores_pd)
        sq3_scores_lowProp = sq3_scores_pd.index[min]
        sq3_scores_lowVal = sq3_scores_pd.iloc[min, 0]
        SQ3_scores.append(sq3_rd_score*(sq3_scores_lowVal/100)) 

    SQ3_score = np.mean([a * b for a, b in zip(SQ3_scores, wts)])
    return SQ3_score


def calculate_SQ4(data, phase_req, drainage_req):
    # SWR
    swr = data.SWR[0]
    sq4_swr_req = phase_req.query('SQI_code == 4 & property == \'SWR\' & phase_id ==' + str(swr)).reset_index(drop=True)
    sq4_swr_score = sq4_swr_req.score[0]

    # Impermeable layer
    il = data.IL[0]
    sq4_il_req = phase_req.query('SQI_code == 4 & property == \'IL\' & phase_id ==' + str(il)).reset_index(drop=True)
    sq4_il_score = sq4_il_req.score[0]

    # Drainage
    drain_id = data.DrainNum[0]
    pscl = data.PSCL[0]
    sq4_drain_req = drainage_req.query('SQI_code == 4 & PSCL_HWSD == \'' + str(pscl) + '\' & DrainNum ==' + str(drain_id)).reset_index(drop=True)
    sq4_drain_score = sq4_drain_req.score[0]

    # Phases
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
    
    return SQ4_score


def calculate_SQ5(data, phase_req, property_req, wts):
    SQ5_scores = []
    # Phases
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

    # Soil layer properties
    for s in range(len(data.index)):
        layer = data.loc[s]
        # ESP score
        sq5_esp_req = property_req.query('SQI_code == 5 & property == \'esp\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        esp = layer.ESP
        sq5_esp_score = None
        t = 0
        n = len(sq5_esp_req.property_value) - 1
        while sq5_esp_score == None:
            if esp <= sq5_esp_req.property_value[t] or t == n:
                sq5_esp_score = sq5_esp_req.score[t]
            else:
                sq5_esp_score = None
                t = t + 1
        # EC score
        sq5_ec_req = property_req.query('SQI_code == 5 & property == \'ec\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        ec = layer.ELCO
        sq5_ec_score = None
        t = 0
        n = len(sq5_ec_req.property_value) - 1
        while sq5_ec_score == None:
            if ec <= sq5_ec_req.property_value[t] or t == n:
                sq5_ec_score = sq5_ec_req.score[t]
            else:
                sq5_ec_score = None
                t = t + 1
        esp_ec_score = sq5_ec_score * (sq5_esp_score / 100)
        sq5_scores_pd = pd.DataFrame(data={'esp_ec': [esp_ec_score], 'phase1': [sq5_phase1_score], 'phase2': [sq5_phase2_score]}).T
        sq5_min = np.argmin(sq5_scores_pd)
        sq5_scores_lowVal = sq5_scores_pd.iloc[sq5_min, 0]
        SQ5_scores.append(sq5_scores_lowVal)

    SQ5_score = np.mean([a * b for a, b in zip(SQ5_scores, wts)])
    return SQ5_score

def calculate_SQ6(data, phase_req, property_req, wts):
    SQ6_scores = []
    # Phases
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

    # Soil layer properties
    for s in range(len(data.index)):
        layer = data.loc[s]
        # CCB score
        sq6_ccb_req = property_req.query('SQI_code == 6 & property == \'ca\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        ccb = layer.TCEQ
        sq6_ccb_score = None
        t = 0
        n = len(sq6_ccb_req.property_value) - 1
        while sq6_ccb_score == None:
            if ccb <= sq6_ccb_req.property_value[t] or t == n:
                sq6_ccb_score = sq6_ccb_req.score[t]
            else:
                sq6_ccb_score = None
                t = t + 1
        # GYP score
        sq6_gyp_req = property_req.query('SQI_code == 6 & property == \'gy\'').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        gyp = layer.GYPS
        sq6_gyp_score = None
        t = 0
        n = len(sq6_gyp_req.property_value) - 1
        while sq6_gyp_score == None:
            if gyp <= sq6_gyp_req.property_value[t] or t == n:
                sq6_gyp_score = sq6_gyp_req.score[t]
            else:
                sq6_gyp_score = None
                t = t + 1
        ccb_gyp_score = sq6_gyp_score * (sq6_ccb_score / 100)
        sq6_scores_pd = pd.DataFrame(data={'ccb_gyp': [ccb_gyp_score], 'phase1': [sq6_phase1_score], 'phase2': [sq6_phase2_score]}).T
        sq6_min = np.argmin(sq6_scores_pd)
        sq6_scores_lowVal = sq6_scores_pd.iloc[sq6_min, 0]
        SQ6_scores.append(sq6_scores_lowVal)

    SQ6_score = np.mean([a * b for a, b in zip(SQ6_scores, wts)])
    return SQ6_score


def calculate_SQ7(data, phase_req, property_req, texture_req, wts):
    SQ7_scores = []
    # Profile properties
    # Soil depth
    sq7_rd_req = property_req.query('SQI_code == 7 & property == \'rd\'').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    rd = data.REF_DEPTH[0]
    sq7_rd_score = None
    j = 0
    n = len(sq7_rd_req.property_value) - 1
    while sq7_rd_score == None:
        if rd >= sq7_rd_req.property_value[j] or j == n:
            sq7_rd_score = sq7_rd_req.score[j]
        else:
            sq7_rd_score = None
            j = j + 1
    
    # Surface/subsurface degree of compactness
    # ... Rest of the code as provided ...

    # Soil layer properties        
    for s in range(len(data.index)):
        layer = data.loc[s]
        # Texture score
        text_class_id = str(layer.text_class_id)
        sq7_text_req = texture_req.query('SQI_code == 3 & text_class_id ==' + text_class_id).reset_index(drop=True)
        sq7_txt_score = sq7_text_req.score[0]
        # ... Rest of the code as provided ...

        # Scores calculation
        if s == 0:
            sq7_scores_pd = pd.DataFrame(data={'rd': [sq7_rd_score], 'txt': [sq7_txt_score], 'cf': [sq7_cf_score], 'db': [sq7_dbT_score],  'ver': [sq7_ver_score], 'gel': [sq7_gel_score], 'phase1': [sq7_phase1_score], 'phase2': [sq7_phase2_score], 'roots': [sq7_roots_score],'il': [sq7_il_score]}).T
        else:
            sq7_scores_pd = pd.DataFrame(data={'rd': [sq7_rd_score], 'txt': [sq7_txt_score], 'cf': [sq7_cf_score], 'db': [sq7_dbS_score],  'ver': [sq7_ver_score], 'gel': [sq7_gel_score], 'phase1': [sq7_phase1_score], 'phase2': [sq7_phase2_score], 'roots': [sq7_roots_score],'il': [sq7_il_score]}).T
        sq7_min = np.argmin(sq7_scores_pd)
        sq7_scores_lowVal = sq7_scores_pd.iloc[sq7_min, 0]
        sq7_scores_lowProp = sq7_scores_pd.index[sq7_min]
        sq7_scores_high_mean = sq7_scores_pd.loc[sq7_scores_pd.index != sq7_scores_lowProp, :].mean()
        SQ7_scores.append(np.mean([sq7_scores_lowVal, sq7_scores_high_mean]))

    SQ7_score = np.mean([a * b for a, b in zip(SQ7_scores, wts)])
    return SQ7_score

def calculate_soil_rating(SQ1_score, SQ2_score, SQ3_score, SQ4_score, SQ5_score, SQ6_score, SQ7_score, inputLevel, SU_name):
    # Create a DataFrame for the relevant scores based on the input level
    if inputLevel == 'L':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score], 'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score]})
        SR = SQ1_score * (SQ3_score / 100) * (group_scores.min(axis=1) / 100)
    elif inputLevel == 'I':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score], 'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score]})
        SR = 0.5 * (SQ1_score + SQ2_score) * (SQ3_score / 100) * (group_scores.min(axis=1) / 100)
    elif inputLevel == 'H':
        group_scores = pd.DataFrame(data={'SQ4': [SQ4_score], 'SQ7': [SQ7_score]})
        SR = SQ2_score * (SQ3_score / 100) * (group_scores.min(axis=1) / 100)
    else:
        raise ValueError("Invalid input level. Choose from 'L', 'I', or 'H'.")

    # Collect all the scores into a DataFrame
    SQI_scores = pd.DataFrame(data={'SQ1': [SQ1_score], 'SQ2': [SQ2_score], 'SQ3': [SQ3_score], 'SQ4': [SQ4_score],
                                    'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score], 'SR': [SR],
                                    'Input Level': [inputLevel], 'Soil Tax': [SU_name]})

    return SQI_scores

#####################################################################################################
#          Unused functions from SoilID API. Saved here for possible future use.                    #
#####################################################################################################


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
