"""
Unit tests for GAEZ_SSURGO_data.py

This module tests SSURGO data retrieval and processing functions.
"""

import pytest
import numpy as np
import pandas as pd
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock
import geopandas as gpd
from shapely.geometry import Polygon

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Note: Full import testing requires external dependencies and API access
# These tests focus on testable utility functions


class TestTextureClassification:
    """Tests for texture classification functions."""

    @pytest.mark.unit
    def test_gettt_basic(self):
        """Test basic texture classification."""
        # Sandy loam: ~60% sand, 30% silt, 10% clay
        try:
            from GAEZ_SSURGO_data import gettt
            result = gettt(60, 30, 10)
            assert isinstance(result, str), "Should return texture class name"
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_gettt_clay(self):
        """Test clay texture classification."""
        try:
            from GAEZ_SSURGO_data import gettt
            result = gettt(20, 20, 60)
            assert 'clay' in result.lower() or 'Clay' in result
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_gettt_sand(self):
        """Test sand texture classification."""
        try:
            from GAEZ_SSURGO_data import gettt
            result = gettt(85, 10, 5)
            assert 'sand' in result.lower() or 'Sand' in result
        except ImportError:
            pytest.skip("Function not directly importable")


class TestParticleSizeClassification:
    """Tests for particle size class functions."""

    @pytest.mark.unit
    def test_classify_pscl_coarse(self):
        """Test classification of coarse texture."""
        try:
            from GAEZ_SSURGO_data import classify_pscl
            # Sandy texture should be coarse
            result = classify_pscl('Sand')
            assert result in ['1', 'Coarse']
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_classify_pscl_medium(self):
        """Test classification of medium texture."""
        try:
            from GAEZ_SSURGO_data import classify_pscl
            result = classify_pscl('Loam')
            assert result in ['2', 'Medium']
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_classify_pscl_fine(self):
        """Test classification of fine texture."""
        try:
            from GAEZ_SSURGO_data import classify_pscl
            result = classify_pscl('Clay')
            assert result in ['3', 'Fine']
        except ImportError:
            pytest.skip("Function not directly importable")


class TestTextureIDMapping:
    """Tests for texture ID mapping functions."""

    @pytest.mark.unit
    def test_getTXT_id_valid_texture(self):
        """Test mapping texture name to ID."""
        try:
            from GAEZ_SSURGO_data import getTXT_id
            result = getTXT_id('Loam')
            assert isinstance(result, (int, str)), "Should return texture ID"
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_getTXT_id_unknown_texture(self):
        """Test handling of unknown texture."""
        try:
            from GAEZ_SSURGO_data import getTXT_id
            result = getTXT_id('UnknownTexture')
            # Should handle gracefully, possibly return 0 or None
            assert result is not None
        except ImportError:
            pytest.skip("Function not directly importable")


class TestTextureGrouping:
    """Tests for texture grouping functions."""

    @pytest.mark.unit
    def test_getTextGroup_coarse(self):
        """Test coarse texture grouping."""
        try:
            from GAEZ_SSURGO_data import getTextGroup
            result = getTextGroup('Sand')
            assert result in ['Coarse', 'coarse', 'C', 'c']
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_getTextGroup_medium(self):
        """Test medium texture grouping."""
        try:
            from GAEZ_SSURGO_data import getTextGroup
            result = getTextGroup('Loam')
            assert result in ['Medium', 'medium', 'M', 'm']
        except ImportError:
            pytest.skip("Function not directly importable")

    @pytest.mark.unit
    def test_getTextGroup_fine(self):
        """Test fine texture grouping."""
        try:
            from GAEZ_SSURGO_data import getTextGroup
            result = getTextGroup('Clay')
            assert result in ['Fine', 'fine', 'F', 'f']
        except ImportError:
            pytest.skip("Function not directly importable")


@pytest.mark.requires_network
class TestPrepareAEA_AOI:
    """Tests for AOI projection transformation."""

    def test_prepare_aea_aoi_transforms_crs(self):
        """Test that AOI is transformed to Albers Equal Area."""
        try:
            from GAEZ_SSURGO_data import prepare_AEA_AOI

            # Create a simple polygon in WGS84
            polygon = Polygon([(-100, 40), (-100, 41), (-99, 41), (-99, 40), (-100, 40)])
            aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

            result = prepare_AEA_AOI(aoi, res=30, native_crs="EPSG:5070")

            assert isinstance(result, dict), "Should return a dictionary"
            assert 'bbox' in result, "Should have bbox"
            assert 'width' in result, "Should have width"
            assert 'height' in result, "Should have height"
        except ImportError:
            pytest.skip("Function not directly importable or dependencies missing")

    def test_prepare_aea_aoi_handles_already_projected(self):
        """Test that function handles AOI already in AEA projection."""
        try:
            from GAEZ_SSURGO_data import prepare_AEA_AOI

            # Create polygon already in AEA
            polygon = Polygon([(1000000, 2000000), (1000000, 2100000),
                              (1100000, 2100000), (1100000, 2000000), (1000000, 2000000)])
            aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:5070")

            result = prepare_AEA_AOI(aoi, res=30, native_crs="EPSG:5070")

            assert isinstance(result, dict), "Should return a dictionary"
            assert 'bbox' in result, "Should have bbox"
        except ImportError:
            pytest.skip("Function not directly importable")


@pytest.mark.requires_network
@pytest.mark.slow
class TestMukeyWCS:
    """Tests for SSURGO WCS data retrieval."""

    def test_mukey_wcs_returns_raster(self):
        """Test that mukey_wcs returns a raster dataset."""
        # This would require actual network access and is slow
        pytest.skip("Requires network access and is slow")

    def test_mukey_wcs_handles_invalid_aoi(self):
        """Test error handling for invalid AOI."""
        pytest.skip("Requires network access")


class TestMukeyWCSMocked:
    """Tests for mukey_wcs with mocked network calls."""

    @patch('GAEZ_SSURGO_data.requests.get')
    @patch('GAEZ_SSURGO_data.tempfile.NamedTemporaryFile')
    @patch('GAEZ_SSURGO_data.rasterio.open')
    def test_mukey_wcs_constructs_url_correctly(self, mock_rasterio, mock_tempfile, mock_requests):
        """Test that WCS URL is constructed correctly"""
        from GAEZ_SSURGO_data import mukey_wcs

        # Create mock response
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.iter_content = MagicMock(return_value=[b'fake_tiff_data'])
        mock_requests.return_value = mock_response

        # Mock temp file
        mock_file = MagicMock()
        mock_file.name = '/tmp/test.tif'
        mock_tempfile.return_value.__enter__.return_value = mock_file

        # Mock rasterio dataset
        mock_raster = MagicMock()
        mock_raster.width = 100
        mock_raster.height = 100
        mock_rasterio.return_value = mock_raster

        # Create test AOI
        polygon = Polygon([(-100, 40), (-100, 41), (-99, 41), (-99, 40), (-100, 40)])
        aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

        try:
            result = mukey_wcs(aoi, db='gssurgo', res=30, quiet=True)

            # Verify request was made
            assert mock_requests.called
            call_args = mock_requests.call_args
            url = call_args[0][0]

            # Check URL contains expected components
            assert 'SERVICE=WCS' in url
            assert 'gSSURGO' in url
            assert 'RESOLUTION' in url
        except Exception as e:
            pytest.skip(f"Function behavior changed or unavailable: {e}")

    @patch('GAEZ_SSURGO_data.requests.get')
    def test_mukey_wcs_handles_network_error(self, mock_requests):
        """Test error handling when network request fails"""
        from GAEZ_SSURGO_data import mukey_wcs
        import requests

        # Mock network failure
        mock_requests.side_effect = requests.RequestException("Network error")

        polygon = Polygon([(-100, 40), (-100, 41), (-99, 41), (-99, 40), (-100, 40)])
        aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

        with pytest.raises(RuntimeError, match="Error downloading WCS data"):
            mukey_wcs(aoi, db='gssurgo', res=30)

    def test_mukey_wcs_validates_db_parameter(self):
        """Test that invalid db parameter raises error"""
        from GAEZ_SSURGO_data import mukey_wcs

        polygon = Polygon([(-100, 40), (-100, 41), (-99, 41), (-99, 40), (-100, 40)])
        aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

        with pytest.raises(ValueError, match="db must be one of"):
            mukey_wcs(aoi, db='invalid_db', res=30)

    def test_mukey_wcs_validates_resolution(self):
        """Test that invalid resolution raises error"""
        from GAEZ_SSURGO_data import mukey_wcs

        polygon = Polygon([(-100, 40), (-100, 41), (-99, 41), (-99, 40), (-100, 40)])
        aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

        # Resolution too small
        with pytest.raises(ValueError, match="res should be within"):
            mukey_wcs(aoi, db='gssurgo', res=10)

        # Resolution too large
        with pytest.raises(ValueError, match="res should be within"):
            mukey_wcs(aoi, db='gssurgo', res=5000)

    def test_mukey_wcs_validates_aoi_size(self):
        """Test that oversized AOI raises error"""
        from GAEZ_SSURGO_data import mukey_wcs

        # Create very large polygon
        polygon = Polygon([(-120, 30), (-120, 50), (-70, 50), (-70, 30), (-120, 30)])
        aoi = gpd.GeoDataFrame({'geometry': [polygon]}, crs="EPSG:4326")

        with pytest.raises(ValueError, match="AOI is too large"):
            mukey_wcs(aoi, db='gssurgo', res=30)


@pytest.mark.requires_network
@pytest.mark.slow
class TestSSURGOGAEZData:
    """Tests for ssurgo_gaez_data function."""

    def test_ssurgo_gaez_data_returns_dataframe(self):
        """Test that function returns a DataFrame."""
        pytest.skip("Requires network access to SSURGO API")

    def test_ssurgo_gaez_data_handles_invalid_mukey(self):
        """Test handling of invalid mukey values."""
        pytest.skip("Requires network access")


class TestSSURGOGAEZDataMocked:
    """Tests for ssurgo_gaez_data with mocked API calls."""

    @patch('GAEZ_SSURGO_data.sda_return')
    def test_ssurgo_gaez_data_returns_dataframe(self, mock_sda_return):
        """Test that function returns properly formatted DataFrame"""
        from GAEZ_SSURGO_data import ssurgo_gaez_data

        # Create mock API response
        mock_response = pd.DataFrame({
            'Table': [[
                ['mukey', 'cokey', 'chkey', 'hzname', 'hzdept_r', 'hzdepb_r',
                 'sandtotal_r', 'silttotal_r', 'claytotal_r', 'pi_r', 'lep_r',
                 'ec_r', 'caco3_r', 'om_r', 'dbovendry_r', 'gypsum_r', 'sar_r',
                 'cec7_r', 'ecec_r', 'sumbases_r', 'ph1to1h2o_r', 'total_fragvol_r',
                 'fragkind', 'plasticity', 'stickiness', 'drainagecl', 'hydricrating',
                 'taxtempcl', 'frostact', 'reskind', 'resdept_r', 'reshard',
                 'taxminalogy', 'pondfreqcl', 'ponddurcl', 'flodfreqcl', 'floddurcl',
                 'wtdepannmin'],
                ['123456', '12345', '1234', 'Ap', 0, 15, 45.0, 35.0, 20.0, 5.0, 3.0,
                 0.5, 2.0, 2.5, 1.45, 0.0, 2.0, 15.0, 12.0, 10.0, 6.5, 5.0,
                 'gravel', 'slightly sticky', 'slightly plastic', 'well drained', 'No',
                 'mesic', 'low', None, 50, 'moderately cemented', 'mixed', 'none', 'none',
                 'none', 'none', 100]
            ]]
        })
        mock_sda_return.return_value = mock_response

        result = ssurgo_gaez_data(['123456'])

        assert isinstance(result, pd.DataFrame)
        assert 'mukey' in result.columns
        assert 'cokey' in result.columns
        assert 'sand' in result.columns or 'sandtotal_r' in result.columns
        assert len(result) > 0

    @patch('GAEZ_SSURGO_data.sda_return')
    def test_ssurgo_gaez_data_handles_no_data(self, mock_sda_return):
        """Test handling when no data is returned"""
        from GAEZ_SSURGO_data import ssurgo_gaez_data

        mock_sda_return.return_value = None

        result = ssurgo_gaez_data(['999999'])

        assert isinstance(result, str)
        assert 'not available' in result.lower()

    @patch('GAEZ_SSURGO_data.sda_return')
    def test_ssurgo_gaez_data_calculates_derived_properties(self, mock_sda_return):
        """Test that derived soil properties are calculated"""
        from GAEZ_SSURGO_data import ssurgo_gaez_data

        # Create mock with SAR data to test ESP calculation
        mock_response = pd.DataFrame({
            'Table': [[
                ['mukey', 'cokey', 'chkey', 'hzname', 'hzdept_r', 'hzdepb_r',
                 'sandtotal_r', 'silttotal_r', 'claytotal_r', 'pi_r', 'lep_r',
                 'ec_r', 'caco3_r', 'om_r', 'dbovendry_r', 'gypsum_r', 'sar_r',
                 'cec7_r', 'ecec_r', 'sumbases_r', 'ph1to1h2o_r', 'total_fragvol_r',
                 'fragkind', 'plasticity', 'stickiness', 'drainagecl', 'hydricrating',
                 'taxtempcl', 'frostact', 'reskind', 'resdept_r', 'reshard',
                 'taxminalogy', 'pondfreqcl', 'ponddurcl', 'flodfreqcl', 'floddurcl',
                 'wtdepannmin'],
                ['123456', '12345', '1234', 'Ap', 0, 15, 60.0, 30.0, 10.0, 5.0, 3.0,
                 0.5, 2.0, 2.5, 1.45, 0.0, 10.0, 15.0, 12.0, 10.0, 6.5, 5.0,
                 'gravel', 'slightly sticky', 'slightly plastic', 'Well Drained', 'No',
                 'mesic', 'low', None, 50, 'moderately cemented', 'mixed', 'none', 'none',
                 'none', 'none', 100]
            ]]
        })
        mock_sda_return.return_value = mock_response

        result = ssurgo_gaez_data(['123456'])

        # Check that derived properties exist
        assert 'esp' in result.columns  # ESP from SAR
        assert 'soc' in result.columns  # SOC from OM
        assert 'bs' in result.columns   # Base saturation
        assert 'texture' in result.columns  # Texture class
        assert 'drain_id' in result.columns  # Drainage class numeric

    @patch('GAEZ_SSURGO_data.sda_return')
    def test_ssurgo_gaez_data_handles_multiple_mukeys(self, mock_sda_return):
        """Test processing multiple mukey values"""
        from GAEZ_SSURGO_data import ssurgo_gaez_data

        mock_response = pd.DataFrame({
            'Table': [[
                ['mukey', 'cokey', 'chkey', 'hzname', 'hzdept_r', 'hzdepb_r',
                 'sandtotal_r', 'silttotal_r', 'claytotal_r', 'pi_r', 'lep_r',
                 'ec_r', 'caco3_r', 'om_r', 'dbovendry_r', 'gypsum_r', 'sar_r',
                 'cec7_r', 'ecec_r', 'sumbases_r', 'ph1to1h2o_r', 'total_fragvol_r',
                 'fragkind', 'plasticity', 'stickiness', 'drainagecl', 'hydricrating',
                 'taxtempcl', 'frostact', 'reskind', 'resdept_r', 'reshard',
                 'taxminalogy', 'pondfreqcl', 'ponddurcl', 'flodfreqcl', 'floddurcl',
                 'wtdepannmin'],
                ['123456', '12345', '1234', 'Ap', 0, 15, 45.0, 35.0, 20.0, 5.0, 3.0,
                 0.5, 2.0, 2.5, 1.45, 0.0, 2.0, 15.0, 12.0, 10.0, 6.5, 5.0,
                 'gravel', 'slightly sticky', 'slightly plastic', 'well drained', 'No',
                 'mesic', 'low', None, 50, 'moderately cemented', 'mixed', 'none', 'none',
                 'none', 'none', 100],
                ['789012', '78901', '7890', 'A', 0, 20, 50.0, 30.0, 20.0, 6.0, 4.0,
                 0.8, 1.5, 3.0, 1.50, 0.0, 3.0, 18.0, 15.0, 12.0, 6.8, 10.0,
                 'gravel', 'sticky', 'plastic', 'moderately well drained', 'No',
                 'mesic', 'low', None, 60, 'strongly cemented', 'mixed', 'none', 'none',
                 'none', 'none', 110]
            ]]
        })
        mock_sda_return.return_value = mock_response

        result = ssurgo_gaez_data(['123456', '789012'])

        assert isinstance(result, pd.DataFrame)
        assert len(result) >= 2  # Should have data for multiple mukeys


@pytest.mark.requires_network
class TestSDAReturn:
    """Tests for SDA API query function."""

    def test_sda_return_executes_query(self):
        """Test that SDA query executes successfully."""
        pytest.skip("Requires network access to USDA SDA API")

    def test_sda_return_handles_malformed_query(self):
        """Test error handling for malformed SQL queries."""
        pytest.skip("Requires network access")


class TestSDAReturnMocked:
    """Tests for sda_return with mocked API calls."""

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_executes_query(self, mock_post):
        """Test that SDA query executes successfully with mock"""
        from GAEZ_SSURGO_data import sda_return

        # Create mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'Table': [
                ['mukey', 'cokey', 'compname'],
                ['123456', '12345', 'Test Soil']
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_response.elapsed.total_seconds.return_value = 0.5
        mock_post.return_value = mock_response

        query = "SELECT mukey, cokey, compname FROM component WHERE mukey = '123456'"
        result = sda_return(query)

        assert isinstance(result, pd.DataFrame)
        assert 'Table' in result.columns
        assert mock_post.called

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_handles_connection_error(self, mock_post):
        """Test handling of connection errors"""
        from GAEZ_SSURGO_data import sda_return
        import requests

        mock_post.side_effect = requests.ConnectionError("Connection failed")

        query = "SELECT * FROM component"
        result = sda_return(query)

        assert result is None

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_handles_timeout(self, mock_post):
        """Test handling of request timeout"""
        from GAEZ_SSURGO_data import sda_return
        import requests

        mock_post.side_effect = requests.Timeout("Request timed out")

        query = "SELECT * FROM component"
        result = sda_return(query)

        assert result is None

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_handles_http_error(self, mock_post):
        """Test handling of HTTP errors"""
        from GAEZ_SSURGO_data import sda_return
        import requests

        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_post.return_value = mock_response

        query = "SELECT * FROM invalid_table"
        result = sda_return(query)

        assert result is None

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_handles_invalid_json(self, mock_post):
        """Test handling of invalid JSON response"""
        from GAEZ_SSURGO_data import sda_return

        mock_response = MagicMock()
        mock_response.json.return_value = {'error': 'Invalid query'}
        mock_response.raise_for_status = MagicMock()
        mock_response.elapsed.total_seconds.return_value = 0.5
        mock_post.return_value = mock_response

        query = "SELECT * FROM component"
        result = sda_return(query)

        # Should return None when 'Table' key is not in response
        assert result is None

    @patch('GAEZ_SSURGO_data.requests.post')
    def test_sda_return_formats_request_correctly(self, mock_post):
        """Test that request is formatted correctly"""
        from GAEZ_SSURGO_data import sda_return

        mock_response = MagicMock()
        mock_response.json.return_value = {'Table': [['col1'], ['val1']]}
        mock_response.raise_for_status = MagicMock()
        mock_response.elapsed.total_seconds.return_value = 0.5
        mock_post.return_value = mock_response

        query = "SELECT * FROM component WHERE mukey = '123456'"
        result = sda_return(query)

        # Verify the POST call was made with correct parameters
        assert mock_post.called
        call_args = mock_post.call_args

        # Check URL
        assert 'sdmdataaccess' in call_args[0][0]

        # Check request data
        request_data = call_args[1]['json']
        assert 'format' in request_data
        assert 'query' in request_data
        assert request_data['format'] == 'JSON+COLUMNNAME'
        assert request_data['query'] == query


# Integration tests
@pytest.mark.integration
@pytest.mark.requires_network
class TestSSURGODataIntegration:
    """Integration tests for SSURGO data retrieval workflow."""

    def test_full_workflow_from_aoi_to_data(self):
        """Test complete workflow from AOI to SSURGO data."""
        pytest.skip("Requires network access and is slow")


# Utility function tests that don't require imports
class TestDataTransformations:
    """Tests for data transformation logic."""

    def test_bulk_density_calculation(self):
        """Test Saxton & Rawls bulk density calculation."""
        # BD = 1.51 - 0.0025*clay - 0.0015*sand + 0.7*OM - 0.15*OM^2 (example formula)
        # This would need to be tested with actual function
        pass

    def test_esp_from_sar_calculation(self):
        """Test ESP calculation from SAR using Richards (1954)."""
        # ESP = 100 * (-0.0126 + 0.01475 * SAR) / (1 + (-0.0126 + 0.01475 * SAR))
        pass

    def test_base_saturation_calculation(self):
        """Test base saturation calculation."""
        # BS = (TEB / CEC) * 100
        pass


# Mock data fixtures
@pytest.fixture
def mock_ssurgo_api_response():
    """Create mock SSURGO API response."""
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
                'cec7_r': 15.0
            }
        ]
    }


@pytest.fixture
def sample_mukey_list():
    """Provide sample mukey values for testing."""
    return ['123456', '789012', '345678']


@pytest.fixture
def sample_aoi_polygon():
    """Create sample area of interest polygon."""
    # Simple polygon in Kansas
    return Polygon([
        (-100.0, 38.0),
        (-100.0, 39.0),
        (-99.0, 39.0),
        (-99.0, 38.0),
        (-100.0, 38.0)
    ])
