#----------------------------------------------------------------------------------------------------
#                                SQI functions                                 
#----------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import math
from scipy.interpolate import PchipInterpolator, interp1d
import sys

# set system path
sys.path.append('/mnt/c/R_Drive/Data_Files/LPKS_Data/R_Projects/GAEZ-Hyperlocalization/code')
import gaez_config
from gaez_config import hz_names
import GAEZ_soil_data_processing
import GAEZ_crop_req


def constraint_curve(x, data, sort_data=True):
    """
    Interpolates a constraint 'score' based on a soil property value using either a
    shape-preserving spline (for monotonic functions) or linear interpolation
    (for bell-/U-shaped functions).

    Parameters
    ----------
    x : float or array-like
        The property value(s) to evaluate.

    data : pandas.DataFrame
        DataFrame with:
          - 'property_value': independent variable (e.g. clay %)
          - 'score': dependent variable (constraint score)

    sort_data : bool, optional
        Sorts by 'property_value' if True (default = True)

    Returns
    -------
    float or np.ndarray
        Interpolated score(s); scalar if x is scalar, array otherwise.
    """
    if data.empty:
        raise ValueError("DataFrame 'data' is empty.")
    if len(data) < 2:
        raise ValueError("DataFrame 'data' must have at least two rows.")
    if not {'property_value', 'score'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'property_value' and 'score' columns.")

    if sort_data:
        data = data.sort_values(by='property_value', ascending=True).drop_duplicates(subset='property_value')

    x_vals = data['property_value'].values
    y_vals = data['score'].values

    # Check for curve shape
    diffs = np.diff(y_vals)
    increasing = np.all(diffs >= 0)
    decreasing = np.all(diffs <= 0)

    # Use monotonic PCHIP for increasing or decreasing
    if increasing or decreasing:
        interp_func = PchipInterpolator(x_vals, y_vals)
    else:
        # Bell-shaped or irregular: use linear interpolation
        interp_func = interp1d(x_vals, y_vals, kind='linear', fill_value='extrapolate')

    # Clamp input x to range
    x_arr = np.atleast_1d(x).astype(float)
    lower_prop, upper_prop = x_vals[0], x_vals[-1]
    lower_score, upper_score = y_vals[0], y_vals[-1]

    result = np.empty_like(x_arr)

    result[x_arr < lower_prop] = lower_score
    result[x_arr > upper_prop] = upper_score

    in_range = (x_arr >= lower_prop) & (x_arr <= upper_prop)
    result[in_range] = interp_func(x_arr[in_range])

    return result.item() if np.isscalar(x) else result


def get_depth_weight_type(CROP_ID):
    """
    Returns the depth weight type (1–4) for a given GAEZ crop ID.

    Parameters
    ----------
    CROP_ID : str
        The crop ID from the GAEZ dataset. Can include letter suffixes (e.g., '15a', '34a').

    Returns
    -------
    int
        Depth weight type (1=shallow, 2=moderate, 3=deep, 4=very deep).
    
    Raises
    ------
    KeyError
        If CROP_ID is not in the lookup table.
    """
    GAEZ_DEPTH_WEIGHT_LOOKUP = {
        '1': 3, '2': 2, '3': 2, '4': 3, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '10': 2,
        '11': 2, '12': 1, '13': 4, '14': 1, '15a': 1, '15b': 1, '15c': 1, '15d': 1,
        '16': 2, '17': 2, '18': 2, '19': 2, '20': 2, '21': 2, '22': 2, '23': 2, '24': 2,
        '25': 3, '26': 4, '27': 4, '28': 3, '29': 2, '30': 3, '31': 1, '32': 4, '33': 4,
        '34a': 4, '34b': 4, '35': 2, '36': 1, '37': 3, '38': 4, '39': 1, '40': 1,
        '41': 1, '42': 4, '43': 4, '44': 4, '45': 4, '46': 4, '47': 3, '48': 3,
        '49a': 4, '49b': 4
    }

    try:
        return GAEZ_DEPTH_WEIGHT_LOOKUP[str(CROP_ID)]
    except KeyError:
        raise KeyError(f"CROP_ID '{CROP_ID}' not found in GAEZ_DEPTH_WEIGHT_LOOKUP.")


def cumulative_weight(d, depthWt_type):
    """
    Returns the cumulative weight fraction at depth d (in cm) using a normalized exponential decay curve.
    
    The decay constant varies by rooting depth class (depthWt_type):
      1 = Shallow rooting (fast decay)
      2 = Moderate rooting
      3 = Deep rooting
      4 = Very deep rooting (slow decay)
    
    Parameters
    ----------
    d : float
        Depth in cm (0–200).
    depthWt_type : int
        1–4 indicating rooting depth class.
    
    Returns
    -------
    float
        The cumulative fraction of weight at depth d.
    """
    max_depth = 200  # cm

    # Define decay constant k for each type
    k_values = {
        1: 0.10,   # shallow
        2: 0.05,   # moderate
        3: 0.03,   # deep
        4: 0.015   # very deep
    }

    if depthWt_type not in k_values:
        raise ValueError("depthWt_type must be 1 (shallow), 2 (moderate), 3 (deep), or 4 (very deep)")

    k = k_values[depthWt_type]

    # Handle bounds
    if d <= 0:
        return 0.0
    elif d >= max_depth:
        return 1.0

    # Normalized exponential cumulative weight
    numerator = 1 - math.exp(-k * d)
    denominator = 1 - math.exp(-k * max_depth)
    return numerator / denominator


def calculate_depth_weights(data, top_col=hz_names.top_col_name, bottom_col=hz_names.bottom_col_name, depthWt_type=2):
    """
    Compute normalized depth weights for a soil profile using cumulative weighting based on rooting depth class.

    Each row in the input DataFrame represents a soil horizon with top and bottom depths (in cm). 
    The weight for each horizon is calculated using the cumulative weight function:
    
        weight = f(bottom) - f(top)
    
    where f(depth) is a normalized exponential cumulative function that depends on rooting depth class.

    The resulting weights are then normalized so that their sum equals 1 across all horizons in the profile.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame with columns specifying the top and bottom depths of each soil horizon (in cm).
    top_col : str, optional
        Name of the column containing the top depths. Defaults to `hz_names.top_col_name`.
    bottom_col : str, optional
        Name of the column containing the bottom depths. Defaults to `hz_names.bottom_col_name`.
    depthWt_type : int, optional
        Rooting depth class that determines the shape of the cumulative weight curve:
            1 = Shallow rooting (rapid decay, e.g., leafy vegetables)
            2 = Moderate rooting (e.g., rice, legumes, soybean)
            3 = Deep rooting (e.g., wheat, maize, sunflower)
            4 = Very deep rooting (slow decay, e.g., pasture, cassava, oil palm)

    Returns
    -------
    pandas.Series
        A Series of normalized weights (summing to 1) for each horizon.
    """
    # Compute raw weight for each horizon by applying the cumulative_weight function
    raw_weights = data.apply(
        lambda row: (cumulative_weight(row[bottom_col], depthWt_type) - cumulative_weight(row[top_col], depthWt_type))
                    if row[bottom_col] > row[top_col] else 0,
        axis=1
    )

    # Normalize the weights
    total = raw_weights.sum()
    if total > 0:
        norm_weights = raw_weights / total
    else:
        norm_weights = raw_weights
    return norm_weights


def calculate_SQ1(data, profile_req, texture_req, inputLevel, wts):
    if inputLevel == 'H':
        return 'NA'

    SQ1_scores = []
    sq1_oc_req = profile_req.query('SQI_code == 1 & property == "oc"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    sq1_ph_req = profile_req.query('SQI_code == 1 & property == "ph"').sort_values(by='property_value', ascending=False).reset_index(drop=True)

    for s, layer in data.iterrows():
        # oc score
        oc = layer.soc
        oc_score = constraint_curve(oc, sq1_oc_req[['score', 'property_value']])

        # ph score
        ph = layer.ph
        ph_score = constraint_curve(ph, sq1_ph_req[['score', 'property_value']])
        
        # texture score
        text_class_id = str(layer['texture_class_id'])
        txt_score = texture_req.query(f'SQI_code == 1 & text_class_id == "{text_class_id}"')['score'].iloc[0]

        # For topsoil only
        if s == 0:
            sq1_teb_req = profile_req.query('SQI_code == 1 & property == "teb"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            teb = layer.teb
            teb_score = constraint_curve(teb, sq1_teb_req[['score', 'property_value']])
            scores_top = [oc_score, ph_score, teb_score, txt_score]
        else:
            # Combine property layer scores
            scores_bottom = [oc_score, ph_score, txt_score]
        
        scores = scores_top if s == 0 else scores_bottom
        min_score = min(scores)
        high_mean = (sum(scores) - min_score) / (len(scores) - 1)
        SQ1_scores.append(np.mean([min_score, high_mean]))

    return np.mean([a * b for a, b in zip(SQ1_scores, wts)])


def calculate_SQ2(data, profile_req, texture_req, inputLevel, wts):
    """
    Calculate Soil Quality Index 2 (SQ2) score for a given soil profile.

    SQ2 evaluates the topsoil and subsoil separately based on base saturation (BS),
    effective cation exchange capacity (CECS/CECc), pH, and optionally texture class.

    Parameters:
        data (DataFrame): Soil horizon data with properties like 'b', 'cecs', 'cecc', 'ph', and 'texture_class_id'.
        profile_req (DataFrame): Table of constraint curve definitions for SQI_code 2.
        texture_req (DataFrame): Table of texture class scores for SQI_code 2.
        inputLevel (str): Indicates input data type ('H' = high input; includes texture scoring).
        wts (list or float): Weight(s) for each soil layer. Can be a list (one per layer) or scalar (same for all).

    Returns:
        float: Computed SQ2 score for the profile.
    """
    SQ2_scores = []

    # Ensure iloc-based access and reset index for safety
    data = data.reset_index(drop=True)

    for i in range(len(data)):
        layer = data.iloc[i]

        # BS score
        bs_req = profile_req.query('SQI_code == 2 & property == "bs"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        bs_score = constraint_curve(layer.bs, bs_req[['score', 'property_value']])

        # Texture score only for high input level
        if inputLevel == 'H':
            text_class_id = str(layer['texture_class_id'])
            txt_score = texture_req.query(f'SQI_code == 2 & text_class_id == "{text_class_id}"')['score'].iloc[0]
        else:
            txt_score = None

        # Topsoil (i == 0)
        if i == 0:
            cecs_req = profile_req.query('SQI_code == 2 & property == "cecs"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecs_score = constraint_curve(layer.cecs, cecs_req[['score', 'property_value']])

            score_dict = {'bs': bs_score, 'cecs': cecs_score}
            if inputLevel == 'H':
                score_dict['txt'] = txt_score

        else:  # Subsoil
            ph_req = profile_req.query('SQI_code == 2 & property == "ph"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            ph_score = constraint_curve(layer.ph, ph_req[['score', 'property_value']])

            cecc_req = profile_req.query('SQI_code == 2 & property == "cecc"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
            cecc_score = constraint_curve(layer.cecc, cecc_req[['score', 'property_value']])

            score_dict = {'bs': bs_score, 'cecc': cecc_score, 'ph': ph_score}
            if inputLevel == 'H':
                score_dict['txt'] = txt_score

        scores_df = pd.DataFrame(score_dict, index=['score']).T
        min_idx = np.argmin(scores_df['score'].values)
        low_val = scores_df.iloc[min_idx, 0]
        high_mean = scores_df.drop(scores_df.index[min_idx]).mean().values[0]
        SQ2_scores.append(np.mean([low_val, high_mean]))

    # Handle weights if a single float is passed
    if isinstance(wts, (float, np.float64)):
        wts = [wts] * len(SQ2_scores)

    return np.sum([score * weight for score, weight in zip(SQ2_scores, wts)])


def calculate_SQ3(data, profile_req, texture_req, phase_req, wts):
    """
    Calculate Soil Quality Index 3 (SQ3) for a given soil profile.

    SQ3 integrates both profile-level and horizon-level properties including:
    - Root depth (rd)
    - Vertic and gelic properties
    - Phase conditions (general, roots, impermeable layer)
    - Texture, coarse fragments, bulk density compactness (per layer)

    Parameters:
        data (DataFrame): Soil profile data with attributes like 'rd', 'vertic', 'gelic', 'roots', 'il',
                          'DB_DC', 'CFRAG', 'texture_class_id', and 'phase_ids_list'.
        profile_req (DataFrame): Constraint curve table for profile and horizon properties (SQI_code 3).
        texture_req (DataFrame): Texture score table (SQI_code 3).
        phase_req (DataFrame): Phase and root condition scores (SQI_code 3).
        wts (list or float): Weight(s) for each soil layer. Can be a list or scalar.

    Returns:
        float: Computed SQ3 score for the soil profile.
    """

    SQ3_scores = []

    # Ensure safe row access
    data = data.reset_index(drop=True)

    # --- Profile-level properties ---
    rd = data['rd'].iloc[0]
    # Fill NaN with 200 (no restriction)
    if pd.isna(rd):
        rd = 200
    sq3_rd_req = profile_req.query('SQI_code == 3 & property == "rd"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    sq3_rd_score = constraint_curve(rd, sq3_rd_req[['score', 'property_value']])

    # Vertic
    vertic = data['vertic'].iloc[0]
    sq3_ver_req = profile_req.query('SQI_code == 3 & property == "ver"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    sq3_ver_score = sq3_ver_req['score'].iloc[0] if vertic == 1 else 100

    # Gelic
    gelic = data['gelic'].iloc[0]
    sq3_gel_req = profile_req.query('SQI_code == 3 & property == "gel"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    sq3_gel_score = sq3_gel_req['score'].iloc[0] if gelic == 1 else 100

    # --- Phase-based properties ---
    data_exploded = data.explode("phase_ids_list")
    phase_ids_list = data_exploded["phase_ids_list"].astype(int)

    if phase_ids_list.nunique() == 1 and phase_ids_list.iloc[0] == 0:
        sq3_phase_score = 100
    else:
        sq3_phase_req = phase_req.query(
            'SQI_code == 3 & property == "phase" & phase_id in @phase_ids_list'
        )
        sq3_phase_score = sq3_phase_req["score"].min() if not sq3_phase_req.empty else 100

    # Roots
    roots = data['roots'].iloc[0]
    sq3_roots_req = phase_req.query(f'SQI_code == 3 & property == "roots" & phase_id == {roots}').reset_index(drop=True)
    sq3_roots_score = sq3_roots_req['score'].iloc[0] if not sq3_roots_req.empty else 100

    # Impermeable layer
    il = data['il'].iloc[0]
    sq3_il_req = phase_req.query(f'SQI_code == 3 & property == "il" & phase_id == {il}').reset_index(drop=True)
    sq3_il_score = sq3_il_req['score'].iloc[0] if not sq3_il_req.empty else 100

    # --- Layer-based properties ---
    for s in range(len(data)):
        layer = data.iloc[s]

        # Texture
        text_class_id = str(layer['texture_class_id'])
        sq3_text_req = texture_req.query(f'SQI_code == 3 & text_class_id == {text_class_id}').reset_index(drop=True)
        sq3_txt_score = sq3_text_req['score'].iloc[0] if not sq3_text_req.empty else 100

        # Compactness (bulk density)
        db_dc = layer['db']
        sq3_db_req = profile_req.query('SQI_code == 3 & property == "db"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        sq3_db_score = constraint_curve(db_dc, sq3_db_req[['score', 'property_value']])

        # Coarse fragments
        cf = layer['fragvol']
        # Fill NaN with 0 (no fragments)
        if pd.isna(cf):
            cf = 0
        sq3_cf_req = profile_req.query('SQI_code == 3 & property == "cf"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        sq3_cf_score = constraint_curve(cf, sq3_cf_req[['score', 'property_value']])

        # Combine all relevant scores into a DataFrame
        score_dict = {
            'txt': sq3_txt_score,
            'cf': sq3_cf_score,
            'db': sq3_db_score,
            'ver': sq3_ver_score,
            'gel': sq3_gel_score,
            'phase': sq3_phase_score,
            'roots': sq3_roots_score,
            'il': sq3_il_score
        }

        score_df = pd.DataFrame(score_dict, index=['score']).T
        min_idx = np.argmin(score_df['score'].values)
        low_val = score_df.iloc[min_idx, 0]
        high_mean = score_df.drop(score_df.index[min_idx]).mean().values[0]

        # Multiply by depth modifier (rd)
        SQ3_scores.append(sq3_rd_score * (np.mean([low_val, high_mean]) / 100))

    # Handle scalar weight
    if isinstance(wts, (float, np.float64)):
        wts = [wts] * len(SQ3_scores)

    return np.sum([score * weight for score, weight in zip(SQ3_scores, wts)])



def calculate_SQ4(data, phase_req, drainage_req):
    """
    Calculate Soil Quality Index 4 (SQ4), which focuses on physical constraints related to 
    water movement, impermeability, surface phases, and drainage.

    Parameters:
        data (DataFrame): Profile-level data with fields including:
            - 'swr': surface water retention phase id
            - 'il': impermeable layer phase id
            - 'drain_id': drainage class code
            - 'pscl_id': particle size class code
            - 'phase_ids_list': list of general phase IDs
        phase_req (DataFrame): Phase-based score reference table (SQI_code == 4).
        drainage_req (DataFrame): Drainage score table by drain_id and PSCL_ID.

    Returns:
        float: SQ4 score (0-100).
    """
    data = data.reset_index(drop=True)

    # SWR
    swr = data['swr'].iloc[0]
    swr_req = phase_req.query(f'SQI_code == 4 & property == "SWR" & phase_id == {swr}').reset_index(drop=True)
    swr_score = swr_req['score'].iloc[0] if not swr_req.empty else 100

    # Impermeable layer
    il = data['il'].iloc[0]
    il_req = phase_req.query(f'SQI_code == 4 & property == "il" & phase_id == {il}').reset_index(drop=True)
    il_score = il_req['score'].iloc[0] if not il_req.empty else 100

    # Drainage
    drain_id = data['drain_id'].iloc[0]
    pscl_id = data['pscl_id'].iloc[0]
    drain_req = drainage_req.query(f'SQI_code == 4 & PSCL_ID == "{pscl_id}" & DrainNum == {drain_id}').reset_index(drop=True)
    drain_score = drain_req['score'].iloc[0] if not drain_req.empty else 100

    # General phase from exploded list
    phase_ids_list = data.explode("phase_ids_list")["phase_ids_list"].astype(int)
    if phase_ids_list.nunique() == 1 and phase_ids_list.iloc[0] == 0:
        phase_score = 100
    else:
        phase_req_filtered = phase_req.query('SQI_code == 4 & property == "phase" & phase_id in @phase_ids_list')
        phase_score = phase_req_filtered["score"].min() if not phase_req_filtered.empty else 100

    # Combine and find the most limiting factor
    scores = pd.DataFrame({
        'swr': [swr_score],
        'il': [il_score],
        'drain': [drain_score],
        'phase': [phase_score]
    }).T

    min_idx = np.argmin(scores[0].values)
    low_score = scores.iloc[min_idx, 0]

    return low_score



def calculate_SQ5(data, phase_req, profile_req, wts):
    """
    Calculate Soil Quality Index 5 (SQ5), focusing on chemical constraints
    from salinity (ec), sodicity (esp), and surface phases.

    Parameters:
        data (DataFrame): Soil horizon data with columns:
            - 'esp': Exchangeable Sodium Percentage
            - 'ec': Electrical Conductivity
            - 'phase_ids_list': list of phase IDs for the profile
        phase_req (DataFrame): Phase score table (SQI_code == 5).
        profile_req (DataFrame): Property score table for ESP and EC (SQI_code == 5).
        wts (list or float): Layer weights. Can be a list (1 per layer) or a scalar (uniform).

    Returns:
        float: SQ5  score (0-100).
    """
    SQ5_scores = []
    data = data.reset_index(drop=True)

    # --- Phase Score (Profile-level) ---
    data_exploded = data.explode("phase_ids_list")
    phase_ids_list = data_exploded["phase_ids_list"].astype(int)

    if phase_ids_list.nunique() == 1 and phase_ids_list.iloc[0] == 0:
        phase_score = 100
    else:
        phase_req_filtered = phase_req.query('SQI_code == 5 & property == "phase" & phase_id in @phase_ids_list')
        phase_score = phase_req_filtered["score"].min() if not phase_req_filtered.empty else 100

    # --- Layer-level Scoring ---
    for i in range(len(data)):
        layer = data.iloc[i]

        # ESP score
        esp = layer['esp']
        esp_req = profile_req.query('SQI_code == 5 & property == "esp"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        esp_score = constraint_curve(esp, esp_req[['score', 'property_value']])

        # EC score
        ec = layer['ec']
        ec_req = profile_req.query('SQI_code == 5 & property == "ec"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        ec_score = constraint_curve(ec, ec_req[['score', 'property_value']])

        # Combine EC and ESP
        esp_ec_score = ec_score * (esp_score / 100)

        # Combine with phase score
        scores_df = pd.DataFrame({
            'esp_ec': [esp_ec_score],
            'phase': [phase_score]
        }).T

        min_idx = np.argmin(scores_df[0].values)
        low_val = scores_df.iloc[min_idx, 0]
        SQ5_scores.append(low_val)

    # Handle scalar weight
    if isinstance(wts, (float, np.float64)):
        wts = [wts] * len(SQ5_scores)

    return np.sum([score * weight for score, weight in zip(SQ5_scores, wts)])


def calculate_SQ6(data, phase_req, profile_req, wts):
    """
    Calculate Soil Quality Index 6 (SQ6), which focuses on chemical constraints 
    related to calcium carbonate and gypsum presence, as well as phase-related limitations.

    Parameters:
        data (DataFrame): Soil horizon data with columns:
            - 'TCEQ': Total carbonate equivalent (used for calcium constraint)
            - 'GYPS': Gypsum percentage
            - 'phase_ids_list': list of phase IDs affecting soil chemistry
        phase_req (DataFrame): Phase-based constraint scores for SQI_code == 6.
        profile_req (DataFrame): Profile constraint curves for calcium and gypsum (SQI_code == 6).
        wts (list or float): Weight(s) for each soil layer. Can be a list (one per layer) or scalar (same for all).

    Returns:
        float: SQ6 score (0-100).
    """
    SQ6_scores = []
    data = data.reset_index(drop=True)

    # --- Phase Score (Profile-level) ---
    data_exploded = data.explode("phase_ids_list")
    phase_ids_list = data_exploded["phase_ids_list"].astype(int)

    if phase_ids_list.nunique() == 1 and phase_ids_list.iloc[0] == 0:
        phase_score = 100
    else:
        phase_req_filtered = phase_req.query('SQI_code == 6 & property == "phase" & phase_id in @phase_ids_list')
        phase_score = phase_req_filtered["score"].min() if not phase_req_filtered.empty else 100

    # --- Layer-level Scoring ---
    for i in range(len(data)):
        layer = data.iloc[i]

        # Calcium carbonate (ccb)
        ccb = layer['caco3']
        ccb_req = profile_req.query('SQI_code == 6 & property == "ca"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        ccb_score = constraint_curve(ccb, ccb_req[['score', 'property_value']])

        # Gypsum (gyp)
        gyp = layer['gypsum']
        gyp_req = profile_req.query('SQI_code == 6 & property == "gy"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        gyp_score = constraint_curve(gyp, gyp_req[['score', 'property_value']])

        # Combined gypsum-calcium penalty
        ccb_gyp_score = gyp_score * (ccb_score / 100)

        # Combine with phase
        score_df = pd.DataFrame({
            'ccb_gyp': [ccb_gyp_score],
            'phase': [phase_score]
        }).T

        min_idx = np.argmin(score_df[0].values)
        low_val = score_df.iloc[min_idx, 0]
        SQ6_scores.append(low_val)

    # Handle scalar weight
    if isinstance(wts, (float, np.float64)):
        wts = [wts] * len(SQ6_scores)

    return np.sum([score * weight for score, weight in zip(SQ6_scores, wts)])


def calculate_SQ7(data, phase_req, profile_req, texture_req, wts):
    """
    Calculate Soil Quality Index 7 (SQ7), focusing on physical and morphological constraints
    such as rooting depth, coarse fragments, compactness, and restrictive layers.

    Parameters:
        data (DataFrame): Soil profile data with columns including:
            - 'rd', 'vertic', 'gelic', 'roots', 'il', 'db', 'fragvol', 'texture_class_id',
              and 'phase_ids_list'.
        phase_req (DataFrame): Phase-based scores for SQI_code == 7.
        profile_req (DataFrame): Constraint curves for RD, DB, CF, etc. (SQI_code == 7).
        texture_req (DataFrame): Texture class scores for SQI_code == 7.
        wts (list or float): Layer weights.

    Returns:
        float: SQ7 score (0-100).
    """
    SQ7_scores = []
    data = data.reset_index(drop=True)

    # --- Profile-level scores ---
    rd = data['rd'].iloc[0]
    # Fill NaN with 200 (no restriction)
    if pd.isna(rd):
        rd = 200
    rd_req = profile_req.query('SQI_code == 7 & property == "rd"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    rd_score = constraint_curve(rd, rd_req[['score', 'property_value']])

    vertic = data['vertic'].iloc[0]
    ver_req = profile_req.query('SQI_code == 7 & property == "ver"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    ver_score = ver_req['score'].iloc[0] if vertic == 1 else 100

    gelic = data['gelic'].iloc[0]
    gel_req = profile_req.query('SQI_code == 7 & property == "gel"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
    gel_score = gel_req['score'].iloc[0] if gelic == 1 else 100

    roots = data['roots'].iloc[0]
    roots_req = phase_req.query(f'SQI_code == 7 & property == "roots" & phase_id == {roots}').reset_index(drop=True)
    roots_score = roots_req['score'].iloc[0] if not roots_req.empty else 100

    il = data['il'].iloc[0]
    il_req = phase_req.query(f'SQI_code == 7 & property == "il" & phase_id == {il}').reset_index(drop=True)
    il_score = il_req['score'].iloc[0] if not il_req.empty else 100

    phase_ids_list = data.explode("phase_ids_list")["phase_ids_list"].astype(int)
    if phase_ids_list.nunique() == 1 and phase_ids_list.iloc[0] == 0:
        phase_score = 100
    else:
        phase_req_filtered = phase_req.query('SQI_code == 7 & property == "phase" & phase_id in @phase_ids_list')
        phase_score = phase_req_filtered["score"].min() if not phase_req_filtered.empty else 100

    # --- Layer-level scoring ---
    for i in range(len(data)):
        layer = data.iloc[i]

        text_class_id = str(layer['texture_class_id'])
        txt_req = texture_req.query(f'SQI_code == 7 & text_class_id == {text_class_id}').reset_index(drop=True)
        txt_score = txt_req['score'].iloc[0] if not txt_req.empty else 100

        db_dc = data['db'].iloc[0]
        db_req = profile_req.query('SQI_code == 7 & property == "db"').sort_values(by='property_value', ascending=True).reset_index(drop=True)
        db_score = constraint_curve(db_dc, db_req[['score', 'property_value']])

        cf = layer['fragvol']
        # Fill NaN with 0 (no fragments)
        if pd.isna(cf):
            cf = 0
        cf_req = profile_req.query('SQI_code == 7 & property == "cf"').sort_values(by='property_value', ascending=False).reset_index(drop=True)
        cf_score = constraint_curve(cf, cf_req[['score', 'property_value']])

        score_dict = {
            'rd': rd_score, 'txt': txt_score, 'cf': cf_score, 'db': db_score,
            'ver': ver_score, 'gel': gel_score, 'phase': phase_score,
            'roots': roots_score, 'il': il_score
        }

        score_df = pd.DataFrame(score_dict, index=['score']).T
        min_idx = np.argmin(score_df['score'].values)
        low_val = score_df.iloc[min_idx, 0]
        high_mean = score_df.drop(score_df.index[min_idx]).mean().values[0]
        SQ7_scores.append(np.mean([low_val, high_mean]))

    if isinstance(wts, (float, np.float64)):
        wts = [wts] * len(SQ7_scores)

    return np.sum([score * weight for score, weight in zip(SQ7_scores, wts)])


def calculate_soil_rating(SQ1_score, SQ2_score, SQ3_score, SQ4_score, SQ5_score, SQ6_score, SQ7_score, inputLevel, cokey):
    """
    Calculate final Soil Rating (SR) by combining relevant SQI scores depending on input level.

    Parameters:
        SQ1_score to SQ7_score (float): Individual SQI scores.
        inputLevel (str): One of 'L' (low), 'I' (intermediate), or 'H' (high) input level.
        cokey (str or int): Component key for identification.

    Returns:
        DataFrame: A summary table of all SQI scores and the final SR value.
    """
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

    SQI_scores = pd.DataFrame({
        'SQ1': [SQ1_score], 'SQ2': [SQ2_score], 'SQ3': [SQ3_score], 'SQ4': [SQ4_score],
        'SQ5': [SQ5_score], 'SQ6': [SQ6_score], 'SQ7': [SQ7_score], 'SR': SR,
        'Input Level': [inputLevel], 'cokey': [cokey]
    })

    return SQI_scores


def gaez_sqi_ratings(map_data, CROP_ID, inputLevel, depthWt_type=1, plot_data=None, site_data=None, lab_data=None):
    """
    Main function to compute GAEZ Soil Quality Indices (SQI1–SQI7) and final Soil Rating (SR)
    for a given crop and input level, using map-derived and optionally user-provided soil data.

    Parameters:
        map_data (DataFrame): Horizon-level or profile-level soil data for a single map unit or location.
        CROP_ID (str or int): Identifier for the target crop to retrieve crop-specific SQI requirements.
        inputLevel (str): One of 'L', 'I', or 'H' indicating input level (Low, Intermediate, High).
        depthWt_type (int): Method for calculating depth weights (default = 1).
        plot_data (DataFrame, optional): User-measured profile data to override `map_data`.
        site_data (DataFrame, optional): User-recorded site characteristics (e.g., slope).
        lab_data (DataFrame, optional): User soil lab test data to enhance or override `map_data`.

    Returns:
        DataFrame: A single-row DataFrame containing:
            - Individual SQI scores (SQ1–SQ7)
            - Final soil rating (SR)
            - Input level and cokey (component key) for traceability
    
    # ------------------------------------------------------------------------------------
    # S0 No constraint (100%)
    # S1 Slight constraint (90%)
    # S2 Moderate constraint (70%)
    # S3 Severe constraint (50%)
    # S4 Very severe constraint (30%)
    # N  Not suitable (<10%)
    """
    # Integrate user-provided field/lab/site data if available
    map_data = GAEZ_soil_data_processing.process_plot_data(plot_data, map_data)
    map_data = GAEZ_soil_data_processing.process_site_data(site_data, map_data)
    map_data = GAEZ_soil_data_processing.process_lab_data(lab_data, map_data)

    # Handle missing values with sensible defaults to prevent NaN propagation in SQ3 and SQ7
    # rd (restrictive depth): NaN indicates no restriction → default to 200 cm (deep soil)
    # fragvol (coarse fragments): NaN indicates negligible fragments → default to 0%
    if 'rd' in map_data.columns:
        map_data['rd'] = map_data['rd'].fillna(200)
    if 'fragvol' in map_data.columns:
        map_data['fragvol'] = map_data['fragvol'].fillna(0)

    # Load crop requirement tables (based on input level and crop ID)
    crop_reqs = GAEZ_crop_req.getGAEZ_requirements_source(CROP_ID=CROP_ID, inputLevel=inputLevel, source='csv', requirement_type='all')
    profile_req = crop_reqs.get("profile")
    phase_req = crop_reqs.get("phase")
    drainage_req = crop_reqs.get("drainage")
    texture_req = crop_reqs.get("texture")
    terrain_req = crop_reqs.get("terrain")  # Not yet used

    # Calculate horizon depth weights
    wts = calculate_depth_weights(map_data, top_col=hz_names.top_col_name, bottom_col=hz_names.bottom_col_name, depthWt_type=depthWt_type)

    # Compute each Soil Quality Index (SQ1–SQ7)
    sqi1 = calculate_SQ1(map_data, profile_req, texture_req, inputLevel, wts)
    sqi2 = calculate_SQ2(map_data, profile_req, texture_req, inputLevel, wts)
    sqi3 = calculate_SQ3(map_data, profile_req, texture_req, phase_req, wts)
    sqi4 = calculate_SQ4(map_data, phase_req, drainage_req)
    sqi5 = calculate_SQ5(map_data, phase_req, profile_req, wts)
    sqi6 = calculate_SQ6(map_data, phase_req, profile_req, wts)
    sqi7 = calculate_SQ7(map_data, phase_req, profile_req, texture_req, wts)

    # Final soil rating using most limiting scores and logic by inputLevel
    cokey_val = map_data['cokey'].iloc[0] if 'cokey' in map_data.columns else 'unknown'
    gaez_sqi_scores = calculate_soil_rating(sqi1, sqi2, sqi3, sqi4, sqi5, sqi6, sqi7, inputLevel, cokey=cokey_val)

    return gaez_sqi_scores
