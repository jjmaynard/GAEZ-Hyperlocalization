"""
Test suite for GAEZ Soil Quality Index API.

Run with:
    pytest code/US_scripts/api/test_api.py -v
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
import numpy as np

from .main import app
from .models import (
    CalculationRequest,
    Location,
    InputLevel,
    PlotDataHorizon,
    SiteData,
    LabData,
    UserData
)
from .service import GAEZCalculationService


# Create test client
client = TestClient(app)


@pytest.fixture
def mock_ssurgo_data():
    """Mock SSURGO data DataFrame."""
    return pd.DataFrame({
        'mukey': ['2494182'] * 4,
        'cokey': ['12345'] * 4,
        'compname': ['Holdrege silt loam'] * 4,
        'hzdept': [0, 15, 30, 60],
        'hzdepb': [15, 30, 60, 100],
        'sandtotal': [25.0, 23.0, 22.0, 24.0],
        'silttotal': [55.0, 54.0, 52.0, 50.0],
        'claytotal': [20.0, 23.0, 26.0, 26.0],
        'om': [3.0, 2.0, 1.0, 0.5],
        'OC': [1.74, 1.16, 0.58, 0.29],
        'ph': [6.5, 6.8, 7.0, 7.2],
        'cecs': [18.0, 20.0, 22.0, 22.0],
        'BS': [85.0, 88.0, 90.0, 92.0],
        'ec': [0.3, 0.3, 0.3, 0.3],
        'ESP': [1.0, 1.0, 1.0, 1.0],
        'caco3': [0.0, 0.0, 0.5, 1.0],
        'gypsum': [0.0, 0.0, 0.0, 0.0],
        'DB': [1.35, 1.42, 1.48, 1.50],
        'CF': [2.0, 3.0, 5.0, 8.0],
        'texture_cl': ['SiL', 'SiL', 'SiCL', 'SiCL'],
        'drainage_cl': ['well drained'] * 4
    })


@pytest.fixture
def mock_phase_data(mock_ssurgo_data):
    """Mock SSURGO data with phases classified."""
    df = mock_ssurgo_data.copy()
    df['phase_ids_list'] = [[]] * len(df)
    df['il'] = [100.0] * len(df)
    df['swr'] = [100.0] * len(df)
    df['roots'] = [100.0] * len(df)
    df['vertic'] = [100.0] * len(df)
    df['gelic'] = [100.0] * len(df)
    return df


@pytest.fixture
def mock_sqi_results():
    """Mock SQI calculation results."""
    return pd.DataFrame({
        'SQ1': [75.0],
        'SQ2': [80.0],
        'SQ3': [85.0],
        'SQ4': [90.0],
        'SQ5': [95.0],
        'SQ6': [100.0],
        'SQ7': [88.0],
        'SR': [68.5]
    })


# ============================================================================
# Health Check Tests
# ============================================================================

def test_health_check():
    """Test health check endpoint returns 200."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data['status'] in ['healthy', 'unhealthy']
    assert 'version' in data
    assert 'services' in data


def test_root_endpoint():
    """Test root endpoint returns API information."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'version' in data


# ============================================================================
# Crops Endpoint Tests
# ============================================================================

def test_list_crops():
    """Test crops listing endpoint."""
    response = client.get("/api/v1/crops")
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'success'
    assert 'crops' in data
    assert 'total_count' in data
    assert data['total_count'] > 0
    assert len(data['crops']) == data['total_count']

    # Check first crop structure
    crop = data['crops'][0]
    assert 'crop_id' in crop
    assert 'crop_name' in crop
    assert 'default_depth_weight' in crop
    assert 'depth_description' in crop


# ============================================================================
# Request Validation Tests
# ============================================================================

def test_calculate_missing_required_fields():
    """Test that missing required fields return 422 validation error."""
    response = client.post("/api/v1/calculate", json={})
    assert response.status_code == 422


def test_calculate_invalid_latitude():
    """Test that invalid latitude returns validation error."""
    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 95.0, "longitude": -100.0},
        "crop_id": "4",
        "input_level": "L"
    })
    assert response.status_code == 422


def test_calculate_invalid_longitude():
    """Test that invalid longitude returns validation error."""
    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 41.0, "longitude": -200.0},
        "crop_id": "4",
        "input_level": "L"
    })
    assert response.status_code == 422


def test_calculate_invalid_input_level():
    """Test that invalid input level returns validation error."""
    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 41.0, "longitude": -100.0},
        "crop_id": "4",
        "input_level": "X"  # Invalid
    })
    assert response.status_code == 422


def test_plot_data_texture_validation():
    """Test that texture percentages must sum to 100."""
    request_data = {
        "location": {"latitude": 41.2, "longitude": -101.6},
        "crop_id": "4",
        "input_level": "L",
        "user_data": {
            "plot_data": [
                {
                    "horizon_id": "Ap",
                    "top_depth": 0,
                    "bottom_depth": 25,
                    "sand_pct": 50.0,
                    "silt_pct": 30.0,
                    "clay_pct": 25.0  # Sum = 105
                }
            ]
        }
    }
    response = client.post("/api/v1/calculate", json=request_data)
    assert response.status_code == 422


def test_plot_data_depth_validation():
    """Test that bottom_depth must be greater than top_depth."""
    request_data = {
        "location": {"latitude": 41.2, "longitude": -101.6},
        "crop_id": "4",
        "input_level": "L",
        "user_data": {
            "plot_data": [
                {
                    "horizon_id": "Ap",
                    "top_depth": 25,
                    "bottom_depth": 25,  # Equal to top_depth
                    "sand_pct": 33.3,
                    "silt_pct": 33.3,
                    "clay_pct": 33.4
                }
            ]
        }
    }
    response = client.post("/api/v1/calculate", json=request_data)
    assert response.status_code == 422


# ============================================================================
# Model Validation Tests
# ============================================================================

def test_location_model_valid():
    """Test Location model with valid data."""
    location = Location(latitude=41.2, longitude=-101.6)
    assert location.latitude == 41.2
    assert location.longitude == -101.6


def test_location_model_invalid_latitude():
    """Test Location model rejects invalid latitude."""
    with pytest.raises(Exception):
        Location(latitude=95.0, longitude=-101.6)


def test_plot_data_model_valid():
    """Test PlotDataHorizon model with valid data."""
    horizon = PlotDataHorizon(
        horizon_id="Ap",
        top_depth=0,
        bottom_depth=25,
        sand_pct=33.3,
        silt_pct=33.3,
        clay_pct=33.4
    )
    assert horizon.top_depth == 0
    assert horizon.bottom_depth == 25


def test_plot_data_model_texture_sum():
    """Test PlotDataHorizon validates texture sum."""
    with pytest.raises(Exception):
        PlotDataHorizon(
            horizon_id="Ap",
            top_depth=0,
            bottom_depth=25,
            sand_pct=50.0,
            silt_pct=30.0,
            clay_pct=25.0  # Sum = 105
        )


# ============================================================================
# Service Layer Tests
# ============================================================================

@patch('api.service.GAEZ_SSURGO_data')
@patch('api.service.GAEZ_US_phase_calc')
@patch('api.service.GAEZ_SQI_functions')
def test_calculation_service_basic(
    mock_sqi,
    mock_phase,
    mock_ssurgo,
    mock_ssurgo_data,
    mock_phase_data,
    mock_sqi_results
):
    """Test GAEZCalculationService with mocked dependencies."""
    # Setup mocks
    mock_ssurgo.mukey_wcs.return_value = np.array([[2494182]])
    mock_ssurgo.ssurgo_gaez_data.return_value = mock_ssurgo_data
    mock_phase.classify_gaez_v4_phases.return_value = mock_phase_data
    mock_sqi.gaez_sqi_ratings.return_value = mock_sqi_results

    # Create service and request
    service = GAEZCalculationService()
    request = CalculationRequest(
        location=Location(latitude=41.2042, longitude=-101.6353),
        crop_id="4",
        input_level=InputLevel.LOW
    )

    # Execute calculation
    response = service.calculate_soil_quality(request)

    # Verify response
    assert response.status == "success"
    assert response.soil_quality_indices.SR == 68.5
    assert response.data_sources.ssurgo_used is True
    assert response.crop_info.crop_id == "4"


@patch('api.service.GAEZ_SSURGO_data')
def test_calculation_service_no_ssurgo_data(mock_ssurgo):
    """Test service handles missing SSURGO data."""
    from .service import SSURGODataError

    # Mock no SSURGO data available
    mock_ssurgo.mukey_wcs.return_value = np.array([[0]])  # No valid mukeys
    mock_ssurgo.ssurgo_gaez_data.return_value = None

    service = GAEZCalculationService()
    request = CalculationRequest(
        location=Location(latitude=41.2042, longitude=-101.6353),
        crop_id="4",
        input_level=InputLevel.LOW
    )

    # Should raise SSURGODataError
    with pytest.raises(SSURGODataError):
        service.calculate_soil_quality(request)


def test_service_get_depth_weight_type():
    """Test depth weight type determination."""
    service = GAEZCalculationService()

    # Test with explicit depth type
    depth = service._get_depth_weight_type("4", 2)
    assert depth == 2

    # Test with auto-determination (maize should be 3)
    depth = service._get_depth_weight_type("4", None)
    assert depth in [1, 2, 3, 4]  # Should return valid depth type


def test_service_convert_plot_data():
    """Test conversion of API plot data to DataFrame."""
    service = GAEZCalculationService()

    plot_data = [
        PlotDataHorizon(
            horizon_id="Ap",
            top_depth=0,
            bottom_depth=25,
            sand_pct=45.0,
            silt_pct=35.0,
            clay_pct=20.0,
            ph=6.5
        )
    ]

    df = service._convert_plot_data_to_df(plot_data)

    assert len(df) == 1
    assert df.iloc[0]['hzdept'] == 0
    assert df.iloc[0]['hzdepb'] == 25
    assert df.iloc[0]['sandtotal'] == 45.0
    assert df.iloc[0]['ph'] == 6.5


def test_service_convert_site_data():
    """Test conversion of API site data to DataFrame."""
    service = GAEZCalculationService()

    site_data = SiteData(
        drainage_class="well drained",
        slope_pct=2.5,
        elevation_m=850
    )

    df = service._convert_site_data_to_df(site_data)

    assert len(df) == 1
    assert df.iloc[0]['drainage_cl'] == "well drained"
    assert df.iloc[0]['slope'] == 2.5
    assert df.iloc[0]['elevation'] == 850


def test_service_convert_lab_data():
    """Test conversion of API lab data to DataFrame."""
    service = GAEZCalculationService()

    lab_data = [
        LabData(
            sample_id="Lab-001",
            depth_cm=15,
            ph_h2o=6.5,
            organic_carbon_pct=1.86,
            cec_cmol_kg=18.5
        )
    ]

    df = service._convert_lab_data_to_df(lab_data)

    assert len(df) == 1
    assert df.iloc[0]['sample_id'] == "Lab-001"
    assert df.iloc[0]['depth'] == 15
    assert df.iloc[0]['ph'] == 6.5
    assert df.iloc[0]['OC'] == 1.86


# ============================================================================
# Integration Tests (with mocked SSURGO)
# ============================================================================

@patch('api.service.GAEZ_SSURGO_data')
@patch('api.service.GAEZ_US_phase_calc')
@patch('api.service.GAEZ_SQI_functions')
def test_calculate_endpoint_basic(
    mock_sqi,
    mock_phase,
    mock_ssurgo,
    mock_ssurgo_data,
    mock_phase_data,
    mock_sqi_results
):
    """Test /api/v1/calculate endpoint with basic request."""
    # Setup mocks
    mock_ssurgo.mukey_wcs.return_value = np.array([[2494182]])
    mock_ssurgo.ssurgo_gaez_data.return_value = mock_ssurgo_data
    mock_phase.classify_gaez_v4_phases.return_value = mock_phase_data
    mock_sqi.gaez_sqi_ratings.return_value = mock_sqi_results

    # Make request
    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",
        "input_level": "L"
    })

    assert response.status_code == 200
    data = response.json()

    assert data['status'] == 'success'
    assert 'soil_quality_indices' in data
    assert data['soil_quality_indices']['SR'] == 68.5
    assert data['crop_info']['crop_name'] == 'Maize'
    assert data['data_sources']['ssurgo_used'] is True


@patch('api.service.GAEZ_SSURGO_data')
@patch('api.service.GAEZ_US_phase_calc')
@patch('api.service.GAEZ_SQI_functions')
@patch('api.service.GAEZ_soil_data_processing')
def test_calculate_endpoint_with_user_data(
    mock_processing,
    mock_sqi,
    mock_phase,
    mock_ssurgo,
    mock_ssurgo_data,
    mock_phase_data,
    mock_sqi_results
):
    """Test /api/v1/calculate endpoint with user data."""
    # Setup mocks
    mock_ssurgo.mukey_wcs.return_value = np.array([[2494182]])
    mock_ssurgo.ssurgo_gaez_data.return_value = mock_ssurgo_data
    mock_phase.classify_gaez_v4_phases.return_value = mock_phase_data

    # Mock data processing to return modified data
    mock_processing.process_plot_data.return_value = mock_phase_data
    mock_processing.process_site_data.return_value = mock_phase_data
    mock_processing.process_lab_data.return_value = mock_phase_data

    mock_sqi.gaez_sqi_ratings.return_value = mock_sqi_results

    # Make request with user data
    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",
        "input_level": "I",
        "user_data": {
            "plot_data": [
                {
                    "horizon_id": "Ap",
                    "top_depth": 0,
                    "bottom_depth": 25,
                    "sand_pct": 45.0,
                    "silt_pct": 35.0,
                    "clay_pct": 20.0,
                    "ph": 6.5
                }
            ],
            "site_data": {
                "drainage_class": "well drained",
                "slope_pct": 2.5
            }
        }
    })

    assert response.status_code == 200
    data = response.json()

    assert data['status'] == 'success'
    assert data['data_sources']['user_plot_data_used'] is True
    assert data['data_sources']['user_site_data_used'] is True


@patch('api.service.GAEZ_SSURGO_data')
def test_calculate_endpoint_ssurgo_error(mock_ssurgo):
    """Test /api/v1/calculate endpoint handles SSURGO errors."""
    # Mock SSURGO error
    mock_ssurgo.mukey_wcs.side_effect = Exception("SSURGO service unavailable")

    response = client.post("/api/v1/calculate", json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",
        "input_level": "L"
    })

    # Should return error response
    assert response.status_code in [404, 500]
    data = response.json()
    assert 'detail' in data or 'message' in data


# ============================================================================
# Edge Cases and Error Handling
# ============================================================================

def test_depth_weight_type_bounds():
    """Test depth_weight_type accepts valid range 1-4."""
    # Valid values
    for dwt in [1, 2, 3, 4]:
        request = CalculationRequest(
            location=Location(latitude=41.0, longitude=-100.0),
            crop_id="4",
            input_level=InputLevel.LOW,
            depth_weight_type=dwt
        )
        assert request.depth_weight_type == dwt

    # Invalid value should fail validation
    with pytest.raises(Exception):
        CalculationRequest(
            location=Location(latitude=41.0, longitude=-100.0),
            crop_id="4",
            input_level=InputLevel.LOW,
            depth_weight_type=5  # Invalid
        )


def test_multiple_lab_samples():
    """Test request can include multiple lab samples."""
    request_data = {
        "location": {"latitude": 41.2, "longitude": -101.6},
        "crop_id": "4",
        "input_level": "H",
        "user_data": {
            "lab_data": [
                {
                    "sample_id": "Lab-001",
                    "depth_cm": 15,
                    "ph_h2o": 6.5,
                    "organic_carbon_pct": 1.86
                },
                {
                    "sample_id": "Lab-002",
                    "depth_cm": 45,
                    "ph_h2o": 6.8,
                    "organic_carbon_pct": 0.95
                }
            ]
        }
    }

    # Should pass validation
    request = CalculationRequest(**request_data)
    assert len(request.user_data.lab_data) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
