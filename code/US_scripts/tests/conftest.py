"""
Pytest configuration and shared fixtures for GAEZ US Scripts tests.

This module provides reusable test fixtures for creating mock data
and setting up test environments.
"""

import pytest
import numpy as np
import pandas as pd
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_soil_horizon_data():
    """
    Create sample soil horizon data for testing.

    Returns a DataFrame with representative soil properties
    for a typical soil profile with 3 horizons.
    """
    data = {
        'cokey': ['12345', '12345', '12345'],
        'hzdept_r': [0, 15, 50],
        'hzdepb_r': [15, 50, 100],
        'sandtotal_r': [45.0, 50.0, 55.0],
        'silttotal_r': [35.0, 30.0, 25.0],
        'claytotal_r': [20.0, 20.0, 20.0],
        'om_r': [2.5, 1.5, 0.8],
        'soc': [1.45, 0.87, 0.46],  # Organic carbon (om/1.724)
        'ph': [6.5, 6.8, 7.0],
        'cec': [15.0, 14.0, 13.0],
        'teb': [12.0, 11.5, 11.0],
        'bs': [80.0, 82.0, 85.0],  # Base saturation
        'cecs': [15.0, 14.0, 13.0],  # CEC soil
        'cecc': [75.0, 70.0, 65.0],  # CEC clay
        'ec': [0.5, 0.4, 0.3],
        'esp': [2.0, 1.8, 1.5],
        'caco3': [0.0, 1.0, 2.0],
        'gypsum': [0.0, 0.0, 0.0],
        'db': [1.25, 1.35, 1.45],  # Bulk density
        'fragvol': [5.0, 8.0, 10.0],  # Coarse fragments
        'texture_class_id': ['7', '7', '7'],  # Loam
        'rd': [200.0, 200.0, 200.0],  # Rooting depth
        'vertic': [0, 0, 0],
        'gelic': [0, 0, 0],
        'roots': [0, 0, 0],
        'il': [0, 0, 0],
        'swr': [0, 0, 0],
        'drain_id': [3, 3, 3],  # Well drained
        'pscl_id': ['2', '2', '2'],  # Medium texture
        'phase_ids_list': [[0], [0], [0]]
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_crop_requirements():
    """
    Create sample crop requirement data for testing SQI calculations.

    Returns a dictionary with profile, texture, phase, and drainage requirements.
    """
    profile_req = pd.DataFrame({
        'SQI_code': [1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2,
                     3, 3, 3, 3,
                     5, 5, 5, 5,
                     6, 6, 6, 6,
                     7, 7],
        'property': ['oc', 'oc', 'ph', 'ph', 'teb', 'teb',
                     'bs', 'bs', 'cecs', 'cecs', 'ph', 'ph', 'cecc', 'cecc',
                     'db', 'db', 'cf', 'cf',
                     'esp', 'esp', 'ec', 'ec',
                     'ca', 'ca', 'gy', 'gy',
                     'rd', 'rd'],
        'property_value': [0.5, 2.0, 5.5, 7.5, 5, 15,
                          20, 80, 5, 20, 5.5, 7.5, 20, 80,
                          1.2, 1.8, 10, 40,
                          5, 20, 2, 8,
                          5, 20, 2, 10,
                          30, 100],
        'score': [40, 100, 60, 100, 60, 100,
                  50, 100, 60, 100, 60, 100, 60, 100,
                  100, 60, 100, 50,
                  100, 60, 100, 50,
                  100, 70, 100, 60,
                  60, 100]
    })

    texture_req = pd.DataFrame({
        'SQI_code': [1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2,
                     3, 3, 3, 3, 3],
        'text_class_id': ['5', '7', '9', '11', '12',
                          '5', '7', '9', '11', '12',
                          '5', '7', '9', '11', '12'],
        'score': [85, 95, 90, 80, 75,
                  90, 95, 92, 85, 80,
                  90, 95, 93, 88, 82]
    })

    phase_req = pd.DataFrame({
        'SQI_code': [3, 3, 3, 3, 3,
                     4, 4,
                     5, 5, 5,
                     6, 6, 6],
        'property': ['phase', 'roots', 'il', 'vertic', 'gelic',
                     'phase', 'phase',
                     'phase', 'phase', 'phase',
                     'phase', 'phase', 'phase'],
        'phase_id': [0, 0, 0, 0, 0,
                     0, 1,
                     0, 1, 2,
                     0, 1, 2],
        'score': [100, 100, 100, 100, 100,
                  100, 90,
                  100, 85, 70,
                  100, 90, 75]
    })

    drainage_req = pd.DataFrame({
        'SQI_code': [4, 4, 4],
        'PSCL_ID': ['1', '2', '3'],
        'DrainNum': [3, 3, 3],
        'score': [95, 95, 95]
    })

    return {
        'profile': profile_req,
        'texture': texture_req,
        'phase': phase_req,
        'drainage': drainage_req
    }


@pytest.fixture
def sample_constraint_curve_data():
    """
    Create sample constraint curve data for interpolation testing.

    Returns a DataFrame with property values and scores for testing
    the constraint_curve function.
    """
    return pd.DataFrame({
        'property_value': [0, 20, 40, 60, 80, 100],
        'score': [20, 40, 70, 85, 95, 100]
    })


@pytest.fixture
def sample_depth_weights():
    """
    Create sample depth weights for a 3-horizon profile.
    """
    return pd.Series([0.15, 0.35, 0.50])


@pytest.fixture
def mock_gaez_config(tmp_path, monkeypatch):
    """
    Create mock configuration with temporary file paths.

    This fixture creates temporary CSV files and patches the
    gaez_config module to use them.
    """
    # Create temporary directory
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Create empty CSV files
    csv_files = {
        'profile_req_url': data_dir / "GAEZ_profile_req_rf.csv",
        'phase_req_url': data_dir / "GAEZ_phase_req_rf.csv",
        'drainage_req_url': data_dir / "GAEZ_drainage_req_rf.csv",
        'texture_req_url': data_dir / "GAEZ_text_req_rf.csv",
        'terrain_req_url': data_dir / "GAEZ_terrain_req_rf.csv"
    }

    for csv_file in csv_files.values():
        csv_file.touch()

    # Patch gaez_config
    import gaez_config
    for key, path in csv_files.items():
        monkeypatch.setattr(gaez_config, key, str(path))

    return csv_files


@pytest.fixture
def sample_ssurgo_response():
    """
    Create a mock SSURGO API response for testing data retrieval functions.
    """
    return {
        'Table': [
            {
                'mukey': '123456',
                'cokey': '12345',
                'compname': 'Test Soil',
                'comppct_r': 85,
                'hzdept_r': 0,
                'hzdepb_r': 15,
                'sandtotal_r': 45.0,
                'silttotal_r': 35.0,
                'claytotal_r': 20.0,
                'om_r': 2.5,
                'ph1to1h2o_r': 6.5,
                'cec7_r': 15.0,
                'ec_r': 0.5,
                'sar_r': 1.0,
                'caco3_r': 0.0,
                'gypsum_r': 0.0,
                'dbthirdbar_r': 1.25,
                'fragvol': 5.0
            }
        ]
    }


@pytest.fixture
def parametrize_crop_ids():
    """
    Provide a list of valid GAEZ crop IDs for parametrized tests.
    """
    return ['1', '4', '15a', '26', '34a', '49b']


@pytest.fixture
def parametrize_input_levels():
    """
    Provide valid input levels for parametrized tests.
    """
    return ['L', 'I', 'H']


@pytest.fixture
def parametrize_depth_weight_types():
    """
    Provide valid depth weight types for parametrized tests.
    """
    return [1, 2, 3, 4]


# Utility functions for tests

def assert_score_in_range(score, min_val=0, max_val=100):
    """
    Assert that a score is within the valid range [0, 100].

    Args:
        score: The score value to check
        min_val: Minimum valid value (default: 0)
        max_val: Maximum valid value (default: 100)
    """
    assert min_val <= score <= max_val, f"Score {score} not in range [{min_val}, {max_val}]"


def assert_weights_sum_to_one(weights, tolerance=1e-6):
    """
    Assert that weights sum to 1.0 (within tolerance).

    Args:
        weights: Series or array of weights
        tolerance: Acceptable deviation from 1.0
    """
    total = weights.sum()
    assert abs(total - 1.0) < tolerance, f"Weights sum to {total}, not 1.0"


# Make utility functions available to all tests
pytest.assert_score_in_range = assert_score_in_range
pytest.assert_weights_sum_to_one = assert_weights_sum_to_one
