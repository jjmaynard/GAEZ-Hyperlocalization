#----------------------------------------------------------------------------------------------------
#                                Crop requirement functions                                 
#----------------------------------------------------------------------------------------------------

import pandas as pd
import os
import sys

# set system path
sys.path.append('/mnt/c/R_Drive/Data_Files/LPKS_Data/R_Projects/GAEZ-Hyperlocalization/code')
import gaez_config

def getGAEZ_requirements(CROP_ID, inputLevel, requirement_type):
    """
    Retrieves specific requirements from the GAEZ database based on the given CROP_ID, input levels, and requirement type.
    
    Parameters:
        CROP_ID: The ID of the crop to filter the data.
        inputLevel (str): Management input level: lwo: 'L', intermediate: 'I', or high: 'H'
        requirement_type (str): Type of requirement to retrieve. Must be one of ['profile', 'texture', 'terrain', 'phase', 'drainage'].

    Returns:
        Pandas DataFrame containing the filtered data, or None if an error occurs.
    """
    # Define Input Level: creates a list of input levels to filter the data.
    if inputLevel == 'L':
        Input_Level_List = ['1','3', '4']
    elif inputLevel == 'I':
        Input_Level_List = ['2','3', '4']
    elif inputLevel == 'H':
        Input_Level_List = ['4','5']
    else:
        return 'Please enter `inputLevel`'

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
        columns = ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'PSCL_ID', 'DrainNum', 'Drain', 'score']
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


#----------------------------------------------------------------------------------------------------
# csv version

def getGAEZ_requirements_csv(CROP_ID, inputLevel):
    """
    Loads and filters GAEZ CSV files based on CROP_ID (string) and input level (character). Need to
    define csv file paths in gaez_config.py file.

    Parameters:
        CROP_ID (str): The crop ID to filter.
        inputLevel (str): Input level identifier ('L', 'I', or 'H').

    Returns:
        dict: Dictionary containing filtered DataFrames for each dataset.
    """
    # Define file paths
    csv_files = {
        "profile": gaez_config.profile_req_url,
        "phase": gaez_config.phase_req_url,
        "drainage": gaez_config.drainage_req_url,
        "texture": gaez_config.texture_req_url,
        "terrain": gaez_config.terrain_req_url
    }

    # Define input levels: create a list of integer input levels to filter the data.
    if inputLevel == 'L':
        Input_Level_List = [1, 3, 4]
    elif inputLevel == 'I':
        Input_Level_List = [2, 3, 4]
    elif inputLevel == 'H':
        Input_Level_List = [4, 5]
    else:
        return 'Please enter a valid `inputLevel` ("L", "I", or "H")'

    # Define required columns for each dataset
    required_columns = {
        "profile": {"CROP_ID", "input_level", "SQI_code", "score", "property_value", "property", "unit", "property_id", "property_text"},
        "phase": {"CROP_ID", "input_level", "SQI_code", "property", "phase_id", "phase", "score"},
        "drainage": {"CROP_ID", "input_level", "SQI_code", "PSCL_ID", "DrainNum", "Drain", "score"},
        "texture": {"CROP_ID", "input_level", "SQI_code", "score", "text_class_id", "text_class"},
        "terrain": {"CROP_ID", "crop_group", "input_level", "FM_class", "slope_class", "slope_class_id", "rating", "rating_text"}
    }

    # Dictionary to store filtered DataFrames
    dataframes = {}

    # Load and filter each dataset
    for key, path in csv_files.items():
        if os.path.exists(path):  # Check if file exists
            try:
                # Load CSV with specified data types
                df = pd.read_csv(path, dtype={"CROP_ID": str, "input_level": int})

                # Check for missing columns
                missing_cols = required_columns[key] - set(df.columns)
                if missing_cols:
                    raise ValueError(f"CSV file '{key}' is missing required columns: {missing_cols}")

                # Filter the DataFrame by checking if "CROP_ID" matches and "input_level" is in the Input_Level_List
                filtered_df = df[(df["CROP_ID"] == CROP_ID) & (df["input_level"].isin(Input_Level_List))]

                # Store the filtered DataFrame in the dictionary
                dataframes[key] = filtered_df

                print(f"Loaded and filtered '{key}' data successfully.")

            except Exception as err:
                print(f"Error loading '{key}': {err}")
        else:
            print(f"Error: File not found - {path}")

    return dataframes


def getGAEZ_requirements_source(CROP_ID, inputLevel, source, requirement_type='all'):
    """
    Retrieves GAEZ requirements from either a database or CSV files based on the given CROP_ID,
    input level, and requirement type. If requirement_type is "all", returns a dictionary of DataFrames.
    
    Parameters:
        CROP_ID (str): The crop ID to filter the data.
        inputLevel (str): Management input level: low ('L'), intermediate ('I'), or high ('H').
        requirement_type (str): Requirement type to retrieve. Must be one of 
                                ['profile', 'texture', 'terrain', 'phase', 'drainage'] or "all".
        source (str): Source of the data: either 'database' or 'csv'.
    
    Returns:
        If requirement_type is not "all":
            A DataFrame containing the filtered data for the specified requirement type,
            or None if an error occurs.
        If requirement_type is "all":
            A dict with keys as requirement types and values as DataFrames.
    """
    # Define input levels: create a list to filter the data.
    if inputLevel == 'L':
        if source == 'database':
            Input_Level_List = ['1', '3', '4']
        else:
            Input_Level_List = [1, 3, 4]
    elif inputLevel == 'I':
        if source == 'database':
            Input_Level_List = ['2', '3', '4']
        else:
            Input_Level_List = [2, 3, 4]
    elif inputLevel == 'H':
        if source == 'database':
            Input_Level_List = ['4', '5']
        else:
            Input_Level_List = [4, 5]
    else:
        return 'Please enter a valid `inputLevel` ("L", "I", or "H")'
    
    # Define the metadata for each requirement type
    req_types = {
        "profile": {
            "table": "GAEZ_profile_req_rf",
            "columns": ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 
                        'property_value', 'property', 'unit', 'property_id', 'property_text'],
            "csv_key": "profile"
        },
        "texture": {
            "table": "GAEZ_text_req_rf",
            "columns": ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'score', 
                        'text_class_id', 'text_class'],
            "csv_key": "texture"
        },
        "terrain": {
            "table": "GAEZ_terrain_req_rf",
            "columns": ['CROP_ID', 'CROP', 'crop_group', 'input_level', 'FM_class', 
                        'slope_class', 'slope_class_id', 'rating', 'rating_text'],
            "csv_key": "terrain"
        },
        "phase": {
            "table": "GAEZ_phase_req_rf",
            "columns": ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'property', 
                        'phase_id', 'phase', 'score'],
            "csv_key": "phase"
        },
        "drainage": {
            "table": "GAEZ_drainage_req_rf",
            "columns": ['CROP_ID', 'CROP', 'input_level', 'SQI_code', 'PSCL_ID', 
                        'DrainNum', 'Drain', 'score'],
            "csv_key": "drainage"
        }
    }
    
    # Determine which requirement types to process
    if requirement_type.lower() != "all":
        if requirement_type not in req_types:
            print("Invalid requirement type.")
            return None
        req_to_process = {requirement_type: req_types[requirement_type]}
    else:
        req_to_process = req_types
    
    # Prepare output container
    output = {}

    if source.lower() == 'database':
        # Database approach
        try:
            conn = getDataStore_Connection()
            cur = conn.cursor()
            
            for rtype, specs in req_to_process.items():
                table_name = specs["table"]
                columns = specs["columns"]
                # Create placeholders for input levels; using %s placeholders.
                placeholders = ', '.join(['%s'] * len(Input_Level_List))
                sql = f'SELECT {", ".join(columns)} FROM {table_name} ' \
                      f'WHERE CROP_ID = %s AND input_level IN ({placeholders})'
                
                params = [CROP_ID] + Input_Level_List
                cur.execute(sql, params)
                results = cur.fetchall()
                df = pd.DataFrame(list(results), columns=columns)
                output[rtype] = df
                print(f"Retrieved {rtype} data successfully from database.")
            
            if requirement_type.lower() != "all":
                return output[requirement_type]
            else:
                return output
        except Exception as err:
            print(f"Error while retrieving data from database: {err}")
            return None
        finally:
            conn.close()
    
    elif source.lower() == 'csv':
        # CSV approach: define CSV file paths (assumed to be in a gaez_config module)
        import gaez_config  # Ensure you have a gaez_config.py with these variables defined
        csv_files = {
            "profile": gaez_config.profile_req_url,
            "phase": gaez_config.phase_req_url,
            "drainage": gaez_config.drainage_req_url,
            "texture": gaez_config.texture_req_url,
            "terrain": gaez_config.terrain_req_url
        }
        
        # Define required columns for each dataset (as sets)
        required_columns = {
            "profile": {"CROP_ID", "input_level", "SQI_code", "score", "property_value", 
                        "property", "unit", "property_id", "property_text"},
            "phase": {"CROP_ID", "input_level", "SQI_code", "property", "phase_id", "phase", "score"},
            "drainage": {"CROP_ID", "input_level", "SQI_code", "PSCL_ID", "DrainNum", "Drain", "score"},
            "texture": {"CROP_ID", "input_level", "SQI_code", "score", "text_class_id", "text_class"},
            "terrain": {"CROP_ID", "crop_group", "input_level", "FM_class", "slope_class", "slope_class_id", "rating", "rating_text"}
        }
        
        for rtype, specs in req_to_process.items():
            path = csv_files[specs["csv_key"]]
            # If path is a tuple, extract its first element.
            if isinstance(path, tuple):
                path = path[0]
            if os.path.exists(path):
                try:
                    # For CSV, input_level is assumed numeric
                    df = pd.read_csv(path, dtype={"CROP_ID": str, "input_level": int})
                    
                    # Check for missing required columns
                    missing_cols = required_columns[specs["csv_key"]] - set(df.columns)
                    if missing_cols:
                        raise ValueError(f"CSV file '{rtype}' is missing required columns: {missing_cols}")
                    
                    # Filter the DataFrame
                    filtered_df = df[(df["CROP_ID"] == CROP_ID) & (df["input_level"].isin(Input_Level_List))]
                    output[rtype] = filtered_df
                    print(f"Loaded and filtered '{rtype}' data successfully from CSV.")
                except Exception as err:
                    print(f"Error loading '{rtype}' from CSV: {err}")
            else:
                print(f"Error: CSV file not found - {path}")
        
        if requirement_type.lower() != "all":
            return output[requirement_type]
        else:
            return output
    else:
        print("Invalid source type. Please specify 'database' or 'csv'.")
        return None
