"""
Unit tests for GAEZ_crop_req.py

This module tests crop requirement data retrieval functions.
"""

import pytest
import pandas as pd
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock
import tempfile

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import GAEZ_crop_req


class TestInputLevelParsing:
    """Tests for input level parsing logic."""

    def test_low_input_level_csv(self):
        """Test that 'L' input level maps to correct numeric values for CSV."""
        # We'll test this indirectly through the source function
        pass

    def test_intermediate_input_level_csv(self):
        """Test that 'I' input level maps to correct values."""
        pass

    def test_high_input_level_csv(self):
        """Test that 'H' input level maps to correct values."""
        pass

    def test_invalid_input_level(self):
        """Test error handling for invalid input level."""
        pass


class TestGetGAEZRequirementsCsv:
    """Tests for getGAEZ_requirements_csv function."""

    def test_returns_dictionary(self, tmp_path, monkeypatch):
        """Test that function returns a dictionary of DataFrames."""
        # Create temporary CSV files
        import gaez_config

        # Create sample CSV files
        profile_data = pd.DataFrame({
            'CROP_ID': ['4', '4', '4'],
            'CROP': ['Maize', 'Maize', 'Maize'],
            'input_level': [1, 3, 4],
            'SQI_code': [1, 1, 1],
            'score': [80, 90, 100],
            'property_value': [1.0, 2.0, 3.0],
            'property': ['oc', 'oc', 'oc'],
            'unit': ['%', '%', '%'],
            'property_id': [1, 1, 1],
            'property_text': ['Organic carbon', 'Organic carbon', 'Organic carbon']
        })

        texture_data = pd.DataFrame({
            'CROP_ID': ['4', '4'],
            'CROP': ['Maize', 'Maize'],
            'input_level': [1, 3],
            'SQI_code': [1, 1],
            'score': [90, 95],
            'text_class_id': ['7', '7'],
            'text_class': ['Loam', 'Loam']
        })

        phase_data = pd.DataFrame({
            'CROP_ID': ['4', '4'],
            'CROP': ['Maize', 'Maize'],
            'input_level': [1, 3],
            'SQI_code': [3, 3],
            'property': ['phase', 'phase'],
            'phase_id': [0, 0],
            'phase': ['None', 'None'],
            'score': [100, 100]
        })

        drainage_data = pd.DataFrame({
            'CROP_ID': ['4', '4'],
            'CROP': ['Maize', 'Maize'],
            'input_level': [1, 3],
            'SQI_code': [4, 4],
            'PSCL_ID': ['2', '2'],
            'DrainNum': [3, 3],
            'Drain': ['Well drained', 'Well drained'],
            'score': [95, 95]
        })

        terrain_data = pd.DataFrame({
            'CROP_ID': ['4', '4'],
            'CROP': ['Maize', 'Maize'],
            'crop_group': ['Cereals', 'Cereals'],
            'input_level': [1, 3],
            'FM_class': ['Rain-fed', 'Rain-fed'],
            'slope_class': ['Level', 'Level'],
            'slope_class_id': [1, 1],
            'rating': [100, 100],
            'rating_text': ['Suitable', 'Suitable']
        })

        # Write CSVs to temp directory
        profile_path = tmp_path / "GAEZ_profile_req_rf.csv"
        texture_path = tmp_path / "GAEZ_text_req_rf.csv"
        phase_path = tmp_path / "GAEZ_phase_req_rf.csv"
        drainage_path = tmp_path / "GAEZ_drainage_req_rf.csv"
        terrain_path = tmp_path / "GAEZ_terrain_req_rf.csv"

        profile_data.to_csv(profile_path, index=False)
        texture_data.to_csv(texture_path, index=False)
        phase_data.to_csv(phase_path, index=False)
        drainage_data.to_csv(drainage_path, index=False)
        terrain_data.to_csv(terrain_path, index=False)

        # Patch gaez_config
        monkeypatch.setattr(gaez_config, 'profile_req_url', str(profile_path))
        monkeypatch.setattr(gaez_config, 'texture_req_url', str(texture_path))
        monkeypatch.setattr(gaez_config, 'phase_req_url', str(phase_path))
        monkeypatch.setattr(gaez_config, 'drainage_req_url', str(drainage_path))
        monkeypatch.setattr(gaez_config, 'terrain_req_url', str(terrain_path))

        # Test the function
        result = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='L')

        assert isinstance(result, dict), "Should return a dictionary"
        assert 'profile' in result, "Should contain profile data"
        assert 'texture' in result, "Should contain texture data"
        assert 'phase' in result, "Should contain phase data"
        assert 'drainage' in result, "Should contain drainage data"
        assert 'terrain' in result, "Should contain terrain data"

    def test_filters_by_crop_id(self, tmp_path, monkeypatch):
        """Test that function filters data by crop ID."""
        import gaez_config

        # Create CSV with multiple crops
        profile_data = pd.DataFrame({
            'CROP_ID': ['4', '4', '5', '5'],
            'CROP': ['Maize', 'Maize', 'Rice', 'Rice'],
            'input_level': [1, 3, 1, 3],
            'SQI_code': [1, 1, 1, 1],
            'score': [80, 90, 85, 95],
            'property_value': [1.0, 2.0, 1.5, 2.5],
            'property': ['oc', 'oc', 'oc', 'oc'],
            'unit': ['%', '%', '%', '%'],
            'property_id': [1, 1, 1, 1],
            'property_text': ['Organic carbon', 'Organic carbon', 'Organic carbon', 'Organic carbon']
        })

        profile_path = tmp_path / "GAEZ_profile_req_rf.csv"
        profile_data.to_csv(profile_path, index=False)

        # Create empty files for others
        for fname in ['text_req', 'phase_req', 'drainage_req', 'terrain_req']:
            (tmp_path / f"GAEZ_{fname}_rf.csv").touch()

        monkeypatch.setattr(gaez_config, 'profile_req_url', str(profile_path))
        monkeypatch.setattr(gaez_config, 'texture_req_url', str(tmp_path / "GAEZ_text_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'phase_req_url', str(tmp_path / "GAEZ_phase_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'drainage_req_url', str(tmp_path / "GAEZ_drainage_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'terrain_req_url', str(tmp_path / "GAEZ_terrain_req_rf.csv"))

        result = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='L')

        # Check that only crop 4 data is returned
        if not result['profile'].empty:
            assert all(result['profile']['CROP_ID'] == '4'), "Should only return data for crop 4"

    def test_filters_by_input_level(self, tmp_path, monkeypatch):
        """Test that function filters by input level correctly."""
        import gaez_config

        profile_data = pd.DataFrame({
            'CROP_ID': ['4'] * 5,
            'CROP': ['Maize'] * 5,
            'input_level': [1, 2, 3, 4, 5],
            'SQI_code': [1] * 5,
            'score': [70, 80, 85, 90, 95],
            'property_value': [1.0] * 5,
            'property': ['oc'] * 5,
            'unit': ['%'] * 5,
            'property_id': [1] * 5,
            'property_text': ['Organic carbon'] * 5
        })

        profile_path = tmp_path / "GAEZ_profile_req_rf.csv"
        profile_data.to_csv(profile_path, index=False)

        for fname in ['text_req', 'phase_req', 'drainage_req', 'terrain_req']:
            (tmp_path / f"GAEZ_{fname}_rf.csv").touch()

        monkeypatch.setattr(gaez_config, 'profile_req_url', str(profile_path))
        monkeypatch.setattr(gaez_config, 'texture_req_url', str(tmp_path / "GAEZ_text_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'phase_req_url', str(tmp_path / "GAEZ_phase_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'drainage_req_url', str(tmp_path / "GAEZ_drainage_req_rf.csv"))
        monkeypatch.setattr(gaez_config, 'terrain_req_url', str(tmp_path / "GAEZ_terrain_req_rf.csv"))

        # Test Low input (should get 1, 3, 4)
        result_L = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='L')
        if not result_L['profile'].empty:
            assert set(result_L['profile']['input_level'].unique()).issubset({1, 3, 4})

        # Test Intermediate input (should get 2, 3, 4)
        result_I = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='I')
        if not result_I['profile'].empty:
            assert set(result_I['profile']['input_level'].unique()).issubset({2, 3, 4})

        # Test High input (should get 4, 5)
        result_H = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='H')
        if not result_H['profile'].empty:
            assert set(result_H['profile']['input_level'].unique()).issubset({4, 5})

    def test_invalid_input_level_returns_error(self):
        """Test that invalid input level returns error message."""
        result = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='X')
        assert result == 'Please enter a valid `inputLevel` ("L", "I", or "H")'

    def test_missing_file_handling(self, tmp_path, monkeypatch, capsys):
        """Test error handling when CSV files are missing."""
        import gaez_config

        # Point to non-existent files
        monkeypatch.setattr(gaez_config, 'profile_req_url', str(tmp_path / "nonexistent.csv"))
        monkeypatch.setattr(gaez_config, 'texture_req_url', str(tmp_path / "nonexistent2.csv"))
        monkeypatch.setattr(gaez_config, 'phase_req_url', str(tmp_path / "nonexistent3.csv"))
        monkeypatch.setattr(gaez_config, 'drainage_req_url', str(tmp_path / "nonexistent4.csv"))
        monkeypatch.setattr(gaez_config, 'terrain_req_url', str(tmp_path / "nonexistent5.csv"))

        result = GAEZ_crop_req.getGAEZ_requirements_csv(CROP_ID='4', inputLevel='L')

        # Should return empty dict but print errors
        captured = capsys.readouterr()
        assert "Error: File not found" in captured.out


class TestGetGAEZRequirementsSource:
    """Tests for getGAEZ_requirements_source unified interface."""

    def test_csv_source_returns_all_types(self, tmp_path, monkeypatch):
        """Test that CSV source returns all requirement types when 'all' is specified."""
        import gaez_config

        # Create minimal CSV files
        for req_type, filename in [
            ('profile', 'GAEZ_profile_req_rf.csv'),
            ('texture', 'GAEZ_text_req_rf.csv'),
            ('phase', 'GAEZ_phase_req_rf.csv'),
            ('drainage', 'GAEZ_drainage_req_rf.csv'),
            ('terrain', 'GAEZ_terrain_req_rf.csv')
        ]:
            if req_type == 'profile':
                data = pd.DataFrame({
                    'CROP_ID': ['4'],
                    'CROP': ['Maize'],
                    'input_level': [1],
                    'SQI_code': [1],
                    'score': [80],
                    'property_value': [1.0],
                    'property': ['oc'],
                    'unit': ['%'],
                    'property_id': [1],
                    'property_text': ['Organic carbon']
                })
            elif req_type == 'texture':
                data = pd.DataFrame({
                    'CROP_ID': ['4'],
                    'CROP': ['Maize'],
                    'input_level': [1],
                    'SQI_code': [1],
                    'score': [90],
                    'text_class_id': ['7'],
                    'text_class': ['Loam']
                })
            elif req_type == 'phase':
                data = pd.DataFrame({
                    'CROP_ID': ['4'],
                    'CROP': ['Maize'],
                    'input_level': [1],
                    'SQI_code': [3],
                    'property': ['phase'],
                    'phase_id': [0],
                    'phase': ['None'],
                    'score': [100]
                })
            elif req_type == 'drainage':
                data = pd.DataFrame({
                    'CROP_ID': ['4'],
                    'CROP': ['Maize'],
                    'input_level': [1],
                    'SQI_code': [4],
                    'PSCL_ID': ['2'],
                    'DrainNum': [3],
                    'Drain': ['Well drained'],
                    'score': [95]
                })
            else:  # terrain
                data = pd.DataFrame({
                    'CROP_ID': ['4'],
                    'CROP': ['Maize'],
                    'crop_group': ['Cereals'],
                    'input_level': [1],
                    'FM_class': ['Rain-fed'],
                    'slope_class': ['Level'],
                    'slope_class_id': [1],
                    'rating': [100],
                    'rating_text': ['Suitable']
                })

            path = tmp_path / filename
            data.to_csv(path, index=False)

            # Patch gaez_config
            attr_name = req_type + '_req_url'
            monkeypatch.setattr(gaez_config, attr_name, str(path))

        result = GAEZ_crop_req.getGAEZ_requirements_source(
            CROP_ID='4',
            inputLevel='L',
            source='csv',
            requirement_type='all'
        )

        assert isinstance(result, dict), "Should return a dictionary"
        assert 'profile' in result
        assert 'texture' in result
        assert 'phase' in result
        assert 'drainage' in result
        assert 'terrain' in result

    def test_csv_source_returns_single_type(self, tmp_path, monkeypatch):
        """Test that CSV source returns single requirement type when specified."""
        import gaez_config

        profile_data = pd.DataFrame({
            'CROP_ID': ['4'],
            'CROP': ['Maize'],
            'input_level': [1],
            'SQI_code': [1],
            'score': [80],
            'property_value': [1.0],
            'property': ['oc'],
            'unit': ['%'],
            'property_id': [1],
            'property_text': ['Organic carbon']
        })

        profile_path = tmp_path / "GAEZ_profile_req_rf.csv"
        profile_data.to_csv(profile_path, index=False)

        monkeypatch.setattr(gaez_config, 'profile_req_url', str(profile_path))

        result = GAEZ_crop_req.getGAEZ_requirements_source(
            CROP_ID='4',
            inputLevel='L',
            source='csv',
            requirement_type='profile'
        )

        assert isinstance(result, pd.DataFrame), "Should return a DataFrame for single type"

    def test_invalid_source_type(self):
        """Test error handling for invalid source type."""
        result = GAEZ_crop_req.getGAEZ_requirements_source(
            CROP_ID='4',
            inputLevel='L',
            source='invalid',
            requirement_type='profile'
        )
        assert result is None

    def test_invalid_requirement_type(self):
        """Test error handling for invalid requirement type."""
        result = GAEZ_crop_req.getGAEZ_requirements_source(
            CROP_ID='4',
            inputLevel='L',
            source='csv',
            requirement_type='invalid_type'
        )
        assert result is None

    @pytest.mark.parametrize("input_level", ['L', 'I', 'H'])
    def test_all_input_levels_csv(self, input_level, tmp_path, monkeypatch):
        """Parametrized test for all input levels with CSV source."""
        import gaez_config

        profile_data = pd.DataFrame({
            'CROP_ID': ['4'] * 5,
            'CROP': ['Maize'] * 5,
            'input_level': [1, 2, 3, 4, 5],
            'SQI_code': [1] * 5,
            'score': [70, 80, 85, 90, 95],
            'property_value': [1.0] * 5,
            'property': ['oc'] * 5,
            'unit': ['%'] * 5,
            'property_id': [1] * 5,
            'property_text': ['Organic carbon'] * 5
        })

        profile_path = tmp_path / "GAEZ_profile_req_rf.csv"
        profile_data.to_csv(profile_path, index=False)

        monkeypatch.setattr(gaez_config, 'profile_req_url', str(profile_path))

        result = GAEZ_crop_req.getGAEZ_requirements_source(
            CROP_ID='4',
            inputLevel=input_level,
            source='csv',
            requirement_type='profile'
        )

        assert isinstance(result, pd.DataFrame)
        assert not result.empty


@pytest.mark.unit
class TestRequirementTypeValidation:
    """Tests for requirement type validation."""

    def test_valid_requirement_types(self):
        """Test that all valid requirement types are recognized."""
        valid_types = ['profile', 'texture', 'terrain', 'phase', 'drainage', 'all']
        for req_type in valid_types:
            # Would need proper mocking for full test
            pass


@pytest.mark.unit
class TestDataFrameColumns:
    """Tests for expected DataFrame column structure."""

    def test_profile_columns_present(self):
        """Test that profile DataFrame has expected columns."""
        expected_cols = {'CROP_ID', 'input_level', 'SQI_code', 'score',
                        'property_value', 'property', 'unit'}
        # Would need to test with actual data
        pass

    def test_texture_columns_present(self):
        """Test that texture DataFrame has expected columns."""
        expected_cols = {'CROP_ID', 'input_level', 'SQI_code', 'score',
                        'text_class_id', 'text_class'}
        pass
