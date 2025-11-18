"""
Example usage scripts for GAEZ Soil Quality Index API.

Run these examples after starting the API server:
    python -m api.main
"""

import requests
import json
from typing import Dict, Any


# API base URL (adjust if running on different host/port)
API_BASE_URL = "http://localhost:8000"


def example_1_basic_calculation():
    """
    Example 1: Basic soil quality calculation using only SSURGO data.

    This is the simplest use case - provide only location and crop information.
    The API will automatically retrieve SSURGO data for the location.
    """
    print("\n" + "="*80)
    print("Example 1: Basic Calculation (SSURGO only)")
    print("="*80)

    # Define request
    request_data = {
        "location": {
            "latitude": 41.2042,
            "longitude": -101.6353  # Nebraska
        },
        "crop_id": "4",  # Maize
        "input_level": "L"  # Low input
    }

    print("\nRequest:")
    print(json.dumps(request_data, indent=2))

    # Make API call
    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json=request_data
    )

    if response.status_code == 200:
        result = response.json()
        print("\nResponse:")
        print(f"Status: {result['status']}")
        print(f"\nCrop: {result['crop_info']['crop_name']}")
        print(f"Input Level: {result['crop_info']['input_level']}")
        print(f"\nSSURGO Component: {result['data_sources']['ssurgo_component']}")
        print(f"Map Unit: {result['data_sources']['ssurgo_map_unit']}")

        print("\nSoil Quality Indices:")
        sqi = result['soil_quality_indices']
        print(f"  SQ1 (Nutrient Availability):  {sqi['SQ1']:.1f}")
        print(f"  SQ2 (Nutrient Retention):     {sqi['SQ2']:.1f}")
        print(f"  SQ3 (Rooting Conditions):     {sqi['SQ3']:.1f}")
        print(f"  SQ4 (Oxygen Availability):    {sqi['SQ4']:.1f}")
        print(f"  SQ5 (Salinity/Sodicity):      {sqi['SQ5']:.1f}")
        print(f"  SQ6 (Lime/Gypsum):            {sqi['SQ6']:.1f}")
        print(f"  SQ7 (Workability):            {sqi['SQ7']:.1f}")
        print(f"  SR  (Overall Rating):         {sqi['SR']:.1f}")

        print(f"\nMessage: {result.get('message', 'N/A')}")
        print(f"Processing Time: {result['metadata']['processing_time_seconds']:.2f}s")
    else:
        print(f"\nError {response.status_code}:")
        print(json.dumps(response.json(), indent=2))


def example_2_with_field_data():
    """
    Example 2: Enhanced calculation with user field measurements.

    Provide soil horizon data from field observations to override SSURGO values
    for specific properties while still using SSURGO for missing data.
    """
    print("\n" + "="*80)
    print("Example 2: Calculation with Field Measurements")
    print("="*80)

    request_data = {
        "location": {
            "latitude": 41.2042,
            "longitude": -101.6353
        },
        "crop_id": "4",  # Maize
        "input_level": "I",  # Intermediate input
        "user_data": {
            "plot_data": [
                {
                    "horizon_id": "Ap",
                    "top_depth": 0,
                    "bottom_depth": 25,
                    "sand_pct": 45.0,
                    "silt_pct": 35.0,
                    "clay_pct": 20.0,
                    "ph": 6.5,
                    "organic_matter_pct": 3.2,
                    "bulk_density": 1.35
                },
                {
                    "horizon_id": "Bt1",
                    "top_depth": 25,
                    "bottom_depth": 60,
                    "sand_pct": 40.0,
                    "silt_pct": 32.0,
                    "clay_pct": 28.0,
                    "ph": 6.8,
                    "organic_matter_pct": 1.8,
                    "bulk_density": 1.45
                }
            ],
            "site_data": {
                "drainage_class": "well drained",
                "slope_pct": 2.5,
                "elevation_m": 850
            }
        }
    }

    print("\nRequest includes:")
    print(f"  - {len(request_data['user_data']['plot_data'])} field-measured horizons")
    print(f"  - Site characteristics (drainage, slope, elevation)")

    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json=request_data
    )

    if response.status_code == 200:
        result = response.json()
        print("\nData Sources Used:")
        ds = result['data_sources']
        print(f"  SSURGO: {ds['ssurgo_used']}")
        print(f"  User plot data: {ds['user_plot_data_used']}")
        print(f"  User site data: {ds['user_site_data_used']}")
        print(f"  Horizons analyzed: {ds['horizons_count']}")

        print("\nSoil Quality Indices:")
        sqi = result['soil_quality_indices']
        print(f"  Overall Rating (SR): {sqi['SR']:.1f}")
        print(f"\nMessage: {result.get('message', 'N/A')}")
    else:
        print(f"\nError {response.status_code}:")
        print(json.dumps(response.json(), indent=2))


def example_3_with_lab_data():
    """
    Example 3: High input calculation with laboratory analysis data.

    Use laboratory test results for precise chemical and physical properties.
    """
    print("\n" + "="*80)
    print("Example 3: Calculation with Laboratory Data")
    print("="*80)

    request_data = {
        "location": {
            "latitude": 35.2271,
            "longitude": -80.8431  # North Carolina
        },
        "crop_id": "29",  # Cotton
        "input_level": "H",  # High input
        "user_data": {
            "lab_data": [
                {
                    "sample_id": "Lab-2025-001",
                    "depth_cm": 15,
                    "ph_h2o": 6.5,
                    "organic_carbon_pct": 1.86,
                    "total_nitrogen_pct": 0.15,
                    "available_p_ppm": 25.0,
                    "available_k_ppm": 180.0,
                    "cec_cmol_kg": 18.5,
                    "base_saturation_pct": 85.0,
                    "ec_ds_m": 0.5,
                    "sand_pct": 55.0,
                    "silt_pct": 30.0,
                    "clay_pct": 15.0,
                    "bulk_density_g_cm3": 1.40
                },
                {
                    "sample_id": "Lab-2025-002",
                    "depth_cm": 45,
                    "ph_h2o": 6.8,
                    "organic_carbon_pct": 0.95,
                    "cec_cmol_kg": 16.2,
                    "base_saturation_pct": 88.0,
                    "sand_pct": 50.0,
                    "silt_pct": 28.0,
                    "clay_pct": 22.0
                }
            ],
            "site_data": {
                "drainage_class": "moderately well drained",
                "slope_pct": 1.5
            }
        }
    }

    print("\nRequest includes:")
    print(f"  - {len(request_data['user_data']['lab_data'])} laboratory samples")
    print(f"  - Site characteristics")

    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json=request_data
    )

    if response.status_code == 200:
        result = response.json()
        print("\nCrop Information:")
        print(f"  Crop: {result['crop_info']['crop_name']}")
        print(f"  Input Level: {result['crop_info']['input_level']}")
        print(f"  Rooting Depth: {result['crop_info']['rooting_depth_description']}")

        print("\nData Integration:")
        ds = result['data_sources']
        print(f"  Lab data used: {ds['user_lab_data_used']}")
        print(f"  Site data used: {ds['user_site_data_used']}")

        sqi = result['soil_quality_indices']
        print("\nKey Indices for High Input:")
        print(f"  SQ2 (Nutrient Retention): {sqi['SQ2']:.1f}")
        print(f"  SQ3 (Rooting Conditions): {sqi['SQ3']:.1f}")
        print(f"  SQ7 (Workability):        {sqi['SQ7']:.1f}")
        print(f"  SR  (Overall Rating):     {sqi['SR']:.1f}")
    else:
        print(f"\nError {response.status_code}:")
        print(json.dumps(response.json(), indent=2))


def example_4_compare_crops():
    """
    Example 4: Compare suitability for different crops at same location.

    Evaluate multiple crops to determine which is best suited for the location.
    """
    print("\n" + "="*80)
    print("Example 4: Compare Multiple Crops")
    print("="*80)

    location = {
        "latitude": 42.0308,
        "longitude": -93.6319  # Iowa
    }

    crops_to_test = [
        ("4", "Maize"),
        ("15a", "Soybean"),
        ("1", "Wheat"),
        ("5", "Sorghum")
    ]

    print(f"\nLocation: ({location['latitude']}, {location['longitude']})")
    print("Input Level: Intermediate\n")

    results = []

    for crop_id, crop_name in crops_to_test:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/calculate",
            json={
                "location": location,
                "crop_id": crop_id,
                "input_level": "I"
            }
        )

        if response.status_code == 200:
            result = response.json()
            sr = result['soil_quality_indices']['SR']
            results.append((crop_name, sr, result))
            print(f"{crop_name:20s} SR: {sr:5.1f}")
        else:
            print(f"{crop_name:20s} Error: {response.status_code}")

    if results:
        # Sort by SR descending
        results.sort(key=lambda x: x[1], reverse=True)
        print(f"\nBest suited crop: {results[0][0]} (SR={results[0][1]:.1f})")


def example_5_list_crops():
    """
    Example 5: List all available crops.

    Get information about all supported crops and their default parameters.
    """
    print("\n" + "="*80)
    print("Example 5: List Available Crops")
    print("="*80)

    response = requests.get(f"{API_BASE_URL}/api/v1/crops")

    if response.status_code == 200:
        result = response.json()
        print(f"\nTotal crops available: {result['total_count']}\n")

        # Print first 15 crops
        print("Sample Crops:")
        print(f"{'ID':<6} {'Name':<25} {'Default Rooting'}")
        print("-" * 70)
        for crop in result['crops'][:15]:
            print(f"{crop['crop_id']:<6} {crop['crop_name']:<25} {crop['depth_description']}")

        print("\n... and more. See /api/v1/crops for complete list.")
    else:
        print(f"Error {response.status_code}:")
        print(response.json())


def example_6_health_check():
    """
    Example 6: Check API health status.

    Verify that the API and its dependencies are functioning correctly.
    """
    print("\n" + "="*80)
    print("Example 6: Health Check")
    print("="*80)

    response = requests.get(f"{API_BASE_URL}/health")

    if response.status_code == 200:
        result = response.json()
        print(f"\nAPI Status: {result['status']}")
        print(f"Version: {result['version']}")
        print(f"Timestamp: {result['timestamp']}")

        print("\nService Status:")
        for service, status in result['services'].items():
            status_icon = "✓" if status == "available" else "✗"
            print(f"  {status_icon} {service}: {status}")
    else:
        print(f"Error {response.status_code}")


def example_7_error_handling():
    """
    Example 7: Error handling demonstration.

    Show how to handle various error conditions.
    """
    print("\n" + "="*80)
    print("Example 7: Error Handling")
    print("="*80)

    # Test 1: Invalid coordinates (ocean location - no SSURGO data)
    print("\nTest 1: Location with no SSURGO data (ocean)")
    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json={
            "location": {"latitude": 25.0, "longitude": -80.0},  # Atlantic Ocean
            "crop_id": "4",
            "input_level": "L"
        }
    )
    if response.status_code != 200:
        error = response.json()
        print(f"  Expected Error: {error['error_code']}")
        print(f"  Message: {error['message']}")

    # Test 2: Invalid texture percentages
    print("\nTest 2: Invalid soil texture (doesn't sum to 100)")
    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json={
            "location": {"latitude": 41.2042, "longitude": -101.6353},
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
                        "clay_pct": 25.0  # Sum = 105, should be 100
                    }
                ]
            }
        }
    )
    if response.status_code != 200:
        error = response.json()
        print(f"  Expected Error: Validation error")
        print(f"  Message: {error.get('detail', 'Validation failed')}")

    # Test 3: Invalid coordinates
    print("\nTest 3: Invalid latitude (out of range)")
    response = requests.post(
        f"{API_BASE_URL}/api/v1/calculate",
        json={
            "location": {"latitude": 95.0, "longitude": -100.0},  # Invalid latitude
            "crop_id": "4",
            "input_level": "L"
        }
    )
    if response.status_code != 200:
        error = response.json()
        print(f"  Expected Error: Validation error")
        print(f"  Message: Latitude must be between -90 and 90")


def run_all_examples():
    """Run all example functions."""
    print("\n" + "="*80)
    print("GAEZ Soil Quality Index API - Example Usage")
    print("="*80)
    print(f"\nAPI Base URL: {API_BASE_URL}")
    print("\nNote: Make sure the API server is running:")
    print("  python -m api.main")

    # Check if API is available
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=2)
        if response.status_code != 200:
            print("\n⚠ WARNING: API health check failed!")
            return
    except requests.exceptions.RequestException:
        print("\n⚠ ERROR: Cannot connect to API server!")
        print("Please start the server first: python -m api.main")
        return

    # Run examples
    example_1_basic_calculation()
    example_2_with_field_data()
    example_3_with_lab_data()
    example_4_compare_crops()
    example_5_list_crops()
    example_6_health_check()
    example_7_error_handling()

    print("\n" + "="*80)
    print("All examples completed!")
    print("="*80)


if __name__ == "__main__":
    run_all_examples()
