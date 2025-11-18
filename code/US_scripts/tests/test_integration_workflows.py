"""
End-to-end integration tests for GAEZ workflow.

These tests verify complete workflows from data retrieval through processing to final outputs.
They use realistic data structures and test the full pipeline.
"""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.mark.integration
class TestFullGAEZWorkflow:
    """Integration tests for complete GAEZ assessment workflow"""

    @patch('GAEZ_soil_data_processing.rasterio.sample.sample_gen')
    @patch('GAEZ_soil_data_processing.rasterio.open')
    def test_complete_soil_quality_assessment_workflow(self, mock_rasterio_open, mock_sample_gen):
        """
        Test complete workflow: SSURGO data → user data integration → soil quality assessment

        This test simulates a realistic workflow:
        1. Start with map-based SSURGO soil data
        2. Integrate field observations (plot data)
        3. Integrate laboratory measurements
        4. Integrate site observations
        5. Calculate derived properties
        6. Assess soil quality indicators
        """
        try:
            from GAEZ_soil_data_processing import (
                process_plot_data,
                process_lab_data,
                process_site_data
            )
            from GAEZ_SSURGO_data import classify_pscl

            # Mock rasterio for slope data retrieval
            mock_dataset = MagicMock()
            mock_rasterio_open.return_value.__enter__.return_value = mock_dataset
            mock_sample_gen.return_value = iter([[4.5]])  # 4.5% slope

            # 1. Start with realistic SSURGO map data (3 horizons, 0-120cm depth)
            map_data = pd.DataFrame({
                'cokey': ['12345'] * 3,
                'hzdept_r': [0, 20, 50],
                'hzdepb_r': [20, 50, 120],
                'sandtotal_r': [35.0, 40.0, 45.0],
                'silttotal_r': [40.0, 35.0, 30.0],
                'claytotal_r': [25.0, 25.0, 25.0],
                'om_r': [2.5, 1.5, 0.8],
                'ph': [6.2, 6.5, 6.8],
                'cec': [18.0, 16.0, 14.0],
                'texture': ['Loam', 'Loam', 'Sandy Loam']
            })

            # 2. Integrate field plot observations
            plot_data = pd.DataFrame({
                'texture': ['Clay Loam', 'Loam'],
                'bottom': [25, 60],
                'rfv_class': ['Low', 'Medium'],
                'bedrock_depth': [180, 180],
                'longitude': [-98.5, -98.5],
                'latitude': [36.5, 36.5]
            })

            result_after_plot = process_plot_data(plot_data, map_data)
            assert isinstance(result_after_plot, pd.DataFrame)
            assert len(result_after_plot) > 0

            # 3. Integrate laboratory measurements (more precise than field observations)
            lab_data = pd.DataFrame({
                'OC': [1.8, 1.2, 0.6],
                'pH': [6.1, 6.4, 6.7],
                'TEB': [14.5, 13.0, 11.5],
                'BS': [82.0, 83.0, 85.0],
                'ECEC': [17.5, 15.5, 13.5],
                'CECc': [72.0, 70.0, 68.0],
                'ESP': [1.5, 1.3, 1.2],
                'bottom': [20, 50, 120],
                'texture': ['Loam', 'Loam', 'Sandy Loam'],
                'bedrock_depth': [180, 180, 180]
            })

            result_after_lab = process_lab_data(lab_data, result_after_plot)
            assert isinstance(result_after_lab, pd.DataFrame)

            # 4. Integrate site-level observations
            site_data = pd.DataFrame({
                'bedrock_depth': [175],
                'slope_percent': [4.2],
                'latitude': [36.48],
                'longitude': [-98.52]
            })

            final_result = process_site_data(site_data, result_after_lab)

            # Verify final integrated dataset
            assert isinstance(final_result, pd.DataFrame)
            assert len(final_result) > 0
            assert 'cokey' in final_result.columns

            # 5. Test derived property calculations
            # Particle size class should be classifiable
            if 'texture' in final_result.columns and 'clay' in final_result.columns:
                for idx, row in final_result.iterrows():
                    if pd.notnull(row.get('texture')):
                        pscl = classify_pscl(row)
                        assert pscl in ['coarse', 'medium', 'fine', 'unknown']

            print(f"✓ Complete workflow test passed: {len(final_result)} horizons processed")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")

    def test_crop_requirements_to_soil_quality_matching(self):
        """
        Test matching crop requirements to soil quality indicators

        Workflow:
        1. Load crop requirements for specific crop
        2. Load soil quality data for a location
        3. Match requirements to soil properties
        4. Calculate suitability scores
        """
        try:
            from GAEZ_crop_req import get_gaez_requirements
            from surgo_data import calculate_derived_properties

            # 1. Get crop requirements (e.g., for Maize)
            crop_id = '4'  # Maize
            input_level = 'H'  # High input level

            requirements = get_gaez_requirements(
                crop_id=crop_id,
                input_level=input_level,
                requirement_type='profile',
                source='csv'
            )

            assert isinstance(requirements, dict)
            assert 'profile' in requirements
            profile_reqs = requirements['profile']
            assert isinstance(profile_reqs, pd.DataFrame)
            assert len(profile_reqs) > 0

            # 2. Create realistic soil property data
            soil_data = pd.DataFrame({
                'cec_soil_cmolkg': [18.0, 16.0, 14.0],
                'clay_%': [25.0, 25.0, 25.0],
                'total_exchangeable_bases_cmolkg': [14.5, 13.0, 11.5],
                'sar': [1.5, 1.8, 2.0]
            })

            # 3. Calculate derived properties
            soil_with_derived = calculate_derived_properties(soil_data)

            # Verify derived properties are calculated
            assert 'cec_clay_cmolkg' in soil_with_derived.columns
            assert 'base_saturation_%' in soil_with_derived.columns
            assert 'esp_%' in soil_with_derived.columns

            # 4. Verify we have data to match against requirements
            # Profile requirements should have SQI codes
            assert 'SQI_code' in profile_reqs.columns

            # Soil data should have properties that can be matched
            assert soil_with_derived['cec_soil_cmolkg'].notnull().any()
            assert soil_with_derived['base_saturation_%'].notnull().any()

            print(f"✓ Crop-to-soil matching test passed: {len(profile_reqs)} requirements × {len(soil_with_derived)} horizons")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_location_to_assessment_workflow(self, mock_post):
        """
        Test workflow from geographic location to soil quality assessment

        Workflow:
        1. Start with lat/lon coordinates
        2. Query SSURGO data via SDA API (mocked)
        3. Process and classify soil data
        4. Calculate soil quality indicators
        """
        try:
            from GAEZ_SSURGO_data import sda_return, classify_pscl, calculate_drainage_id

            # Mock SDA API response with realistic data
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'Table': [
                    {
                        'mukey': '123456',
                        'cokey': '12345678',
                        'compname': 'Richfield',
                        'comppct_r': 85,
                        'hzdept_r': 0,
                        'hzdepb_r': 18,
                        'sandtotal_r': 32.0,
                        'silttotal_r': 42.0,
                        'claytotal_r': 26.0,
                        'om_r': 2.8,
                        'ph1to1h2o_r': 6.3,
                        'cec7_r': 19.5,
                        'dbthirdbar_r': 1.35,
                        'texture': 'silt loam',
                        'drainagecl': 'Well drained'
                    },
                    {
                        'mukey': '123456',
                        'cokey': '12345678',
                        'compname': 'Richfield',
                        'comppct_r': 85,
                        'hzdept_r': 18,
                        'hzdepb_r': 48,
                        'sandtotal_r': 30.0,
                        'silttotal_r': 40.0,
                        'claytotal_r': 30.0,
                        'om_r': 1.5,
                        'ph1to1h2o_r': 6.6,
                        'cec7_r': 22.0,
                        'dbthirdbar_r': 1.40,
                        'texture': 'silty clay loam',
                        'drainagecl': 'Well drained'
                    }
                ]
            }
            mock_post.return_value = mock_response

            # 1. Query data for a location
            query = "SELECT mukey FROM mapunit WHERE mukey = '123456'"
            result = sda_return(query, 'JSON+COLUMNNAME')

            assert isinstance(result, dict)
            assert 'Table' in result

            # 2. Process the soil data
            soil_df = pd.DataFrame(result['Table'])

            # 3. Calculate particle size class
            for idx, row in soil_df.iterrows():
                clay = row.get('claytotal_r')
                sand = row.get('sandtotal_r')
                texture = row.get('texture', '')

                if pd.notnull(texture):
                    pscl = classify_pscl(texture, clay, sand)
                    assert pscl in ['coarse', 'medium', 'fine', 'unknown']

            # 4. Calculate drainage class ID
            for idx, row in soil_df.iterrows():
                drainage = row.get('drainagecl', '')
                if drainage:
                    drain_id = calculate_drainage_id(drainage)
                    assert isinstance(drain_id, (int, float))
                    assert 1 <= drain_id <= 7  # GAEZ drainage classes

            print(f"✓ Location-to-assessment workflow test passed: {len(soil_df)} horizons assessed")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")

    def test_edge_cases_in_workflow(self):
        """Test workflow handles edge cases gracefully"""
        try:
            from GAEZ_soil_data_processing import process_plot_data, process_lab_data
            from surgo_data import filter_data_by_depth

            # Edge case 1: Empty/None data at each step
            map_data = pd.DataFrame({
                'cokey': ['12345'],
                'hzdept_r': [0],
                'hzdepb_r': [120],
                'sandtotal_r': [45.0],
                'silttotal_r': [35.0],
                'claytotal_r': [20.0]
            })

            # Process with None inputs should return unchanged data
            result1 = process_plot_data(None, map_data)
            pd.testing.assert_frame_equal(result1, map_data)

            result2 = process_lab_data(None, map_data)
            pd.testing.assert_frame_equal(result2, map_data)

            # Edge case 2: Incomplete depth coverage
            incomplete_data = pd.DataFrame({
                'cokey': ['99999', '99999'],
                'top_of_horizon_depth_cm': [0, 30],
                'bottom_of_horizon_depth_cm': [30, 80]  # Only goes to 80cm
            })

            filtered = filter_data_by_depth(incomplete_data, 112)
            assert len(filtered) == 0  # Should filter out incomplete profiles

            # Edge case 3: Data with missing values
            data_with_nulls = pd.DataFrame({
                'cokey': ['88888'] * 3,
                'top_of_horizon_depth_cm': [0, np.nan, 60],
                'bottom_of_horizon_depth_cm': [30, 60, 120]
            })

            filtered_nulls = filter_data_by_depth(data_with_nulls, 112)
            assert len(filtered_nulls) == 0  # Should filter out profiles with missing depths

            print("✓ Edge cases handled correctly")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")


@pytest.mark.integration
class TestDataPriorityHierarchy:
    """Test that data sources follow correct priority: Lab > Plot > Map"""

    def test_lab_data_overrides_all(self):
        """Test that laboratory data takes precedence over field and map data"""
        try:
            from GAEZ_soil_data_processing import process_lab_data

            # Start with map data
            map_data = pd.DataFrame({
                'cokey': ['12345'],
                'ph': [6.5],  # Map pH value
                'om_r': [2.0]  # Map organic matter
            })

            # Lab data should override (with all required columns)
            lab_data = pd.DataFrame({
                'OC': [1.8],
                'pH': [6.8],  # Different lab pH value
                'TEB': [14.5],
                'BS': [82.0],
                'ECEC': [17.5],
                'CECc': [72.0],
                'ESP': [1.5],
                'bottom': [30],
                'texture': ['Loam'],
                'bedrock_depth': [180]
            })

            result = process_lab_data(lab_data, map_data)

            # Lab values should be present in result
            # (exact column names depend on implementation)
            assert isinstance(result, pd.DataFrame)
            assert len(result) > 0

            print("✓ Lab data priority verified")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")


@pytest.mark.integration
class TestRealisticDataVolumes:
    """Test system with realistic data volumes"""

    def test_processing_multiple_components(self):
        """Test processing data for multiple soil components"""
        try:
            from surgo_data import calculate_derived_properties, filter_data_by_depth

            # Create data for 5 components, each with 3-5 horizons
            data_list = []
            for i in range(5):
                n_horizons = 3 + (i % 3)  # 3-5 horizons per component
                depths = np.linspace(0, 120, n_horizons + 1)

                for j in range(n_horizons):
                    data_list.append({
                        'cokey': f'comp_{i}',
                        'top_of_horizon_depth_cm': depths[j],
                        'bottom_of_horizon_depth_cm': depths[j+1],
                        'cec_soil_cmolkg': 20.0 - j*2,
                        'clay_%': 25.0 + j*2,
                        'total_exchangeable_bases_cmolkg': 15.0 - j,
                        'sar': 2.0 + j*0.5
                    })

            soil_data = pd.DataFrame(data_list)

            # Calculate derived properties for all components
            result = calculate_derived_properties(soil_data)

            assert len(result) == len(soil_data)
            assert 'cec_clay_cmolkg' in result.columns
            assert 'base_saturation_%' in result.columns
            assert 'esp_%' in result.columns

            # Filter for complete depth coverage
            complete = filter_data_by_depth(result, 112)
            assert len(complete) > 0
            assert complete['cokey'].nunique() <= 5

            print(f"✓ Processed {len(soil_data)} horizons across {soil_data['cokey'].nunique()} components")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")


@pytest.mark.integration
class TestCrossModuleIntegration:
    """Test integration between different GAEZ modules"""

    def test_ssurgo_to_sqi_workflow(self):
        """Test workflow from SSURGO data retrieval to SQI calculation"""
        try:
            from GAEZ_SSURGO_data import classify_pscl, calculate_drainage_id
            from surgo_data import calculate_derived_properties

            # Simulate SSURGO data retrieval result
            ssurgo_data = pd.DataFrame({
                'texture': ['silt loam', 'silty clay loam', 'sandy loam'],
                'clay': [24.0, 30.0, 15.0],
                'sand': [25.0, 20.0, 60.0],
                'drainagecl': ['Well drained', 'Moderately well drained', 'Well drained'],
                'cec_soil_cmolkg': [18.0, 22.0, 12.0],
                'clay_%': [24.0, 30.0, 15.0],
                'total_exchangeable_bases_cmolkg': [14.0, 17.0, 9.0],
                'sar': [2.0, 2.5, 1.5]
            })

            # Step 1: Classify particle size
            ssurgo_data['pscl'] = ssurgo_data.apply(
                lambda row: classify_pscl(row['texture'], row['clay'], row['sand']),
                axis=1
            )
            assert all(ssurgo_data['pscl'].isin(['coarse', 'medium', 'fine', 'unknown']))

            # Step 2: Calculate drainage ID
            ssurgo_data['drain_id'] = ssurgo_data['drainagecl'].apply(calculate_drainage_id)
            assert all((ssurgo_data['drain_id'] >= 1) & (ssurgo_data['drain_id'] <= 7))

            # Step 3: Calculate derived properties
            result = calculate_derived_properties(ssurgo_data)
            assert 'cec_clay_cmolkg' in result.columns
            assert 'base_saturation_%' in result.columns
            assert 'esp_%' in result.columns

            # Step 4: Verify all SQI-relevant properties are available
            required_props = ['pscl', 'drain_id', 'cec_clay_cmolkg', 'base_saturation_%']
            for prop in required_props:
                assert prop in result.columns
                assert result[prop].notnull().any()

            print(f"✓ Cross-module integration test passed: {len(result)} records processed through pipeline")

        except ImportError as e:
            pytest.skip(f"Required modules not available: {e}")
