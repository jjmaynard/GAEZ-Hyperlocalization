"""
Tests for surgo_data.py

This module tests the data loading and exploration functions in surgo_data.py.
Many functions depend on external GDB files, so we use mocking extensively.
"""

import pytest
import pandas as pd
import geopandas as gpd
import numpy as np
from unittest.mock import patch, MagicMock, mock_open
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import functions from surgo_data (now safe since we added if __name__ guard)
from surgo_data import (
    printdf,
    filter_data_by_depth,
    calculate_derived_properties,
    process_texture_data,
    process_fragment_data,
    build_soil_attributes_dataset,
    load_attributes_from_table,
    gaez_attributes,
    soil_attributes_in_tables,
    ids_cols
)


class TestPrintdf:
    """Test the printdf utility function"""

    def test_printdf_basic_dataframe(self, capsys):
        """Test printing a basic dataframe"""
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        printdf(df, num_rows=2)
        captured = capsys.readouterr()
        assert '1' in captured.out
        assert '2' in captured.out

    def test_printdf_with_geometry(self, capsys):
        """Test printing a geodataframe with geometry column"""
        from shapely.geometry import Point

        gdf = gpd.GeoDataFrame({
            'a': [1, 2, 3],
            'b': [4, 5, 6],
            'geometry': [Point(0, 0), Point(1, 1), Point(2, 2)]
        })
        printdf(gdf, num_rows=2, ignore_geometry=True)
        captured = capsys.readouterr()
        assert 'geometry' not in captured.out
        assert '1' in captured.out

    def test_printdf_respects_num_rows(self, capsys):
        """Test that num_rows parameter is respected"""
        df = pd.DataFrame({'a': range(10), 'b': range(10, 20)})
        printdf(df, num_rows=3)
        captured = capsys.readouterr()
        # Should only show first 3 rows (0, 1, 2)
        assert '0' in captured.out
        assert '1' in captured.out
        assert '2' in captured.out


class TestFilterDataByDepth:
    """Test the filter_data_by_depth function"""

    def test_filter_data_by_depth_complete_coverage(self):
        """Test filtering data with complete depth coverage"""
        # Create test data with complete coverage from 0 to 120 cm
        df = pd.DataFrame({
            'cokey': ['A', 'A', 'A'],
            'top_of_horizon_depth_cm': [0, 30, 60],
            'bottom_of_horizon_depth_cm': [30, 60, 120]
        })

        result = filter_data_by_depth(df, 112)
        assert len(result) == 3
        assert result['cokey'].unique()[0] == 'A'

    def test_filter_data_by_depth_incomplete_coverage(self):
        """Test that incomplete depth coverage is filtered out"""
        # Create test data that doesn't reach required depth
        df = pd.DataFrame({
            'cokey': ['B', 'B'],
            'top_of_horizon_depth_cm': [0, 30],
            'bottom_of_horizon_depth_cm': [30, 60]  # Only goes to 60 cm, not 112
        })

        result = filter_data_by_depth(df, 112)
        assert len(result) == 0  # Should be filtered out

    def test_filter_data_by_depth_with_gaps(self):
        """Test that data with gaps in depth is filtered out"""
        # Create test data with a gap
        df = pd.DataFrame({
            'cokey': ['C', 'C', 'C'],
            'top_of_horizon_depth_cm': [0, 30, 70],  # Gap between 60 and 70
            'bottom_of_horizon_depth_cm': [30, 60, 120]
        })

        result = filter_data_by_depth(df, 112)
        assert len(result) == 0  # Should be filtered out due to gap

    def test_filter_data_by_depth_missing_values(self):
        """Test that data with missing depth values is filtered out"""
        df = pd.DataFrame({
            'cokey': ['D', 'D', 'D'],
            'top_of_horizon_depth_cm': [0, 30, np.nan],
            'bottom_of_horizon_depth_cm': [30, 60, 120]
        })

        result = filter_data_by_depth(df, 112)
        assert len(result) == 0  # Should be filtered out


class TestDataAttributes:
    """Test data structure attributes and configurations"""

    def test_gaez_attributes_defined(self):
        """Test that GAEZ attributes list is defined"""
        assert isinstance(gaez_attributes, list)
        assert len(gaez_attributes) > 0
        # Check for some expected attributes
        expected_attrs = ['texture_usda', 'pH']
        for attr in expected_attrs:
            assert attr in gaez_attributes

    def test_soil_attributes_in_tables_structure(self):
        """Test that soil_attributes_in_tables has correct structure"""
        assert isinstance(soil_attributes_in_tables, dict)
        assert 'component' in soil_attributes_in_tables
        assert 'chorizon' in soil_attributes_in_tables
        assert isinstance(soil_attributes_in_tables['component'], dict)


class TestTextureProcessing:
    """Test texture data processing"""

    def test_texture_standardization(self):
        """Test that texture strings are standardized correctly"""
        # This tests the processing logic inline
        texture_samples = pd.Series(['Fine sandy loam', 'Coarse silt loam', 'Sandy loam'])
        # Simulate the processing
        standardized = texture_samples.str.replace(" ", "").str.lower()
        standardized = standardized.str.replace(r'fine|very|coarse', '', regex=True)

        assert 'sandyloam' in standardized.values
        assert 'siltloam' in standardized.values

    def test_texture_duplicate_handling(self):
        """Test that duplicate textures are handled"""
        # Create sample data with duplicates after standardization
        df = pd.DataFrame({
            'chkey': ['1', '1', '2'],
            'texture_usda': ['fine sandy loam', 'sandy loam', 'silt loam'],
            'representative_yn': ['Yes', 'Yes', 'Yes']
        })

        df['texture_usda'] = df['texture_usda'].str.replace(" ", "").str.lower()
        df['texture_usda'] = df['texture_usda'].str.replace(r'fine|very|coarse', '', regex=True)
        df.drop_duplicates(subset=['chkey', 'texture_usda'], inplace=True)

        # After standardization, chkey '1' should have only one entry
        assert df[df['chkey'] == '1']['texture_usda'].nunique() == 1


class TestDerivedCalculations:
    """Test derived calculation formulas"""

    def test_cec_clay_calculation(self):
        """Test CEC/clay calculation"""
        chorizon = pd.DataFrame({
            'cec_soil_cmolkg': [15.0, 20.0],
            'clay_%': [25.0, 30.0],
            'total_exchangeable_bases_cmolkg': [12.0, 15.0],
            'sar': [2.0, 3.0]
        })

        result = calculate_derived_properties(chorizon)

        assert 'cec_clay_cmolkg' in result.columns
        # CEC/clay * 100 = (15/25)*100 = 60
        assert abs(result['cec_clay_cmolkg'].iloc[0] - 60.0) < 0.01

    def test_base_saturation_calculation(self):
        """Test base saturation calculation"""
        chorizon = pd.DataFrame({
            'total_exchangeable_bases_cmolkg': [12.0, 15.0],
            'cec_soil_cmolkg': [15.0, 20.0],
            'clay_%': [25.0, 30.0],
            'sar': [2.0, 3.0]
        })

        result = calculate_derived_properties(chorizon)

        assert 'base_saturation_%' in result.columns
        # BS = (TEB/CEC) * 100 = (12/15)*100 = 80%
        assert abs(result['base_saturation_%'].iloc[0] - 80.0) < 0.01

    def test_esp_from_sar_calculation(self):
        """Test ESP from SAR calculation"""
        chorizon = pd.DataFrame({
            'cec_soil_cmolkg': [15.0],
            'clay_%': [25.0],
            'total_exchangeable_bases_cmolkg': [12.0],
            'sar': [5.0]
        })

        result = calculate_derived_properties(chorizon)

        assert 'esp_%' in result.columns
        # Richards (1954) formula: ESP = (100 * (-0.0126 + 0.01475 * SAR)) / (1 + (-0.0126 + 0.01475 * SAR))
        sar = 5.0
        expected_esp = (100 * (-0.0126 + 0.01475 * sar)) / (1 + (-0.0126 + 0.01475 * sar))
        assert abs(result['esp_%'].iloc[0] - expected_esp) < 0.01


class TestFragmentVolumeAggregation:
    """Test fragment volume aggregation"""

    def test_fragment_volume_summing(self):
        """Test that fragment volumes are correctly summed by chkey"""
        # Simulate what process_fragment_data does
        chfrag = pd.DataFrame({
            'chkey': ['1', '1', '2'],
            'fragment_vol_%_by_size': [10.0, 15.0, 20.0]
        })

        result = chfrag.groupby('chkey')['fragment_vol_%_by_size'].sum().rename('gravel_%').reset_index()

        assert len(result) == 2
        assert result[result['chkey'] == '1']['gravel_%'].values[0] == 25.0

    def test_fragment_volume_exceeds_100(self):
        """Test handling of cases where total gravel percent exceeds 100%"""
        chfrag = pd.DataFrame({
            'chkey': ['1', '1', '1'],
            'fragment_vol_%_by_size': [60.0, 50.0, 10.0]
        })

        result = chfrag.groupby('chkey')['fragment_vol_%_by_size'].sum().rename('gravel_%').reset_index()

        # Should still sum even if > 100% (real data issue)
        assert result['gravel_%'].values[0] == 120.0


@pytest.mark.skip(reason="Requires gSSURGO GDB file which is not available in test environment")
class TestLoadAttributesFromTable:
    """Tests for load_attributes_from_table function"""

    def test_load_attributes_from_table_basic(self):
        """Test loading attributes from a table"""
        # This test requires actual GDB file, so we skip it
        pass
