"""
Service layer for GAEZ API - orchestrates soil quality calculations.
"""

import sys
from pathlib import Path
from typing import Optional, Tuple, Dict, Any
import logging
from datetime import datetime
import time
import math

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, box


def _safe_float(value, default: float = 0.0) -> float:
    """
    Safely convert a value to float, handling NaN and None values.

    Args:
        value: Value to convert (can be NaN, None, or numeric)
        default: Default value to return if value is NaN or None

    Returns:
        Float value, or default if value is NaN/None
    """
    if value is None:
        return default
    try:
        float_val = float(value)
        if math.isnan(float_val) or math.isinf(float_val):
            return default
        return float_val
    except (TypeError, ValueError):
        return default

# Add parent directory to path to import GAEZ modules
sys.path.insert(0, str(Path(__file__).parent.parent))

import GAEZ_SSURGO_data
import GAEZ_SQI_functions
import GAEZ_US_phase_calc
import GAEZ_crop_req
import GAEZ_soil_data_processing

from .models import (
    CalculationRequest,
    CalculationResponse,
    SoilQualityIndices,
    DataSources,
    CropInfo,
    CalculationMetadata,
    Location,
    CropListResponse,
    CropListItem
)

logger = logging.getLogger(__name__)


# Crop ID to name mapping (from GAEZ documentation)
CROP_NAMES = {
    '1': 'Wheat',
    '2': 'Rice',
    '3': 'Barley',
    '4': 'Maize',
    '5': 'Sorghum',
    '6': 'Millet',
    '7': 'Rye',
    '8': 'Oat',
    '9': 'White Potato',
    '10': 'Sweet Potato',
    '11': 'Cassava',
    '12': 'Sugar Beet',
    '13': 'Sugarcane',
    '14': 'Oil Palm',
    '15a': 'Soybean (Rain-fed)',
    '15b': 'Soybean (Irrigated)',
    '16': 'Phaseolus Bean',
    '17': 'Chickpea',
    '18': 'Cowpea',
    '19': 'Groundnut',
    '20': 'Rapeseed',
    '21': 'Sunflower',
    '22': 'Banana/Plantain',
    '23': 'Citrus',
    '24': 'Date Palm',
    '25': 'Grapes',
    '26': 'Cacao',
    '27': 'Coffee',
    '28': 'Tea',
    '29': 'Cotton',
    '30': 'Alfalfa',
    '31': 'Onion',
    '32': 'Tomato',
    '33': 'Vegetables',
    '34a': 'Olive (Rain-fed)',
    '34b': 'Olive (Irrigated)',
    '35': 'Tobacco',
    '36': 'Jatropha',
    '37': 'Coconut',
    '38': 'Spring Wheat',
    '39': 'Winter Wheat',
    '40': 'Humid Maize',
    '41': 'Dry Maize',
    '42': 'Wetland Rice',
    '43': 'Dryland Rice',
    '44': 'Forage Crops',
    '45': 'Fiber Crops',
    '46': 'Agave',
    '47': 'Yam',
    '48': 'Taro',
    '49': 'Buckwheat'
}

# Depth weight type descriptions
DEPTH_DESCRIPTIONS = {
    1: 'Shallow rooting (0-30 cm)',
    2: 'Moderate rooting (0-60 cm)',
    3: 'Deep rooting (0-100 cm)',
    4: 'Very deep rooting (0-150 cm)'
}


class GAEZCalculationError(Exception):
    """Base exception for GAEZ calculation errors."""
    pass


class SSURGODataError(GAEZCalculationError):
    """Exception for SSURGO data retrieval errors."""
    pass


class CalculationServiceError(GAEZCalculationError):
    """Exception for calculation service errors."""
    pass


class GAEZCalculationService:
    """
    Service for orchestrating GAEZ soil quality index calculations.
    Integrates SSURGO data retrieval, user data processing, and SQI calculations.
    """

    def __init__(self):
        """Initialize the GAEZ calculation service."""
        self.api_version = "0.1.0"
        logger.info("GAEZCalculationService initialized")

    def calculate_soil_quality(self, request: CalculationRequest) -> CalculationResponse:
        """
        Main orchestration method for soil quality calculations.

        Args:
            request: CalculationRequest with location, crop, and optional user data

        Returns:
            CalculationResponse with SQI scores and metadata

        Raises:
            GAEZCalculationError: If calculation fails
        """
        start_time = time.time()

        try:
            logger.info(f"Starting calculation for crop {request.crop_id} at "
                       f"({request.location.latitude}, {request.location.longitude})")

            # Step 1: Fetch SSURGO data
            ssurgo_data, mukey_info = self._fetch_ssurgo_data(
                request.location,
                request.ssurgo_database,
                request.ssurgo_resolution
            )

            if ssurgo_data is None or len(ssurgo_data) == 0:
                raise SSURGODataError(
                    f"No SSURGO data available for location "
                    f"({request.location.latitude}, {request.location.longitude})"
                )

            # Step 2: Classify soil phases
            logger.info("Classifying soil phases")
            ssurgo_with_phases = GAEZ_US_phase_calc.classify_gaez_v4_phases(ssurgo_data)

            # Step 3: Integrate user data if provided
            working_data = ssurgo_with_phases.copy()
            data_sources_info = {
                'ssurgo_used': True,
                'ssurgo_component': mukey_info.get('component_name'),
                'ssurgo_map_unit': mukey_info.get('mukey'),
                'user_plot_data_used': False,
                'user_site_data_used': False,
                'user_lab_data_used': False,
                'horizons_count': len(ssurgo_with_phases)
            }

            if request.user_data:
                working_data, data_sources_info = self._integrate_user_data(
                    working_data,
                    request.user_data,
                    data_sources_info
                )

            # Step 4: Determine depth weight type
            depth_weight_type = self._get_depth_weight_type(
                request.crop_id,
                request.depth_weight_type
            )

            # Step 5: Calculate SQI scores
            logger.info(f"Calculating SQI scores for crop {request.crop_id}")
            sqi_results = GAEZ_SQI_functions.gaez_sqi_ratings(
                map_data=working_data,
                CROP_ID=request.crop_id,
                inputLevel=request.input_level.value,
                depthWt_type=depth_weight_type
            )

            if sqi_results is None or len(sqi_results) == 0:
                raise CalculationServiceError("SQI calculation returned no results")

            # Step 6: Extract results (using first row if multiple components)
            sqi_row = sqi_results.iloc[0]

            soil_quality_indices = SoilQualityIndices(
                SQ1=_safe_float(sqi_row.get('SQ1')),
                SQ2=_safe_float(sqi_row.get('SQ2')),
                SQ3=_safe_float(sqi_row.get('SQ3')),
                SQ4=_safe_float(sqi_row.get('SQ4')),
                SQ5=_safe_float(sqi_row.get('SQ5')),
                SQ6=_safe_float(sqi_row.get('SQ6')),
                SQ7=_safe_float(sqi_row.get('SQ7')),
                SR=_safe_float(sqi_row.get('SR'))
            )

            # Step 7: Build response
            processing_time = time.time() - start_time

            crop_info = CropInfo(
                crop_id=request.crop_id,
                crop_name=CROP_NAMES.get(request.crop_id, f"Crop {request.crop_id}"),
                input_level=request.input_level.value,
                depth_weight_type=depth_weight_type,
                rooting_depth_description=DEPTH_DESCRIPTIONS[depth_weight_type]
            )

            metadata = CalculationMetadata(
                calculation_timestamp=datetime.utcnow().isoformat() + 'Z',
                api_version=self.api_version,
                gaez_version="4.0",
                processing_time_seconds=round(processing_time, 3)
            )

            response = CalculationResponse(
                status="success",
                location=request.location,
                crop_info=crop_info,
                soil_quality_indices=soil_quality_indices,
                data_sources=DataSources(**data_sources_info),
                metadata=metadata,
                message=self._generate_result_message(sqi_results, data_sources_info)
            )

            logger.info(f"Calculation completed successfully in {processing_time:.2f}s")
            return response

        except Exception as e:
            logger.error(f"Calculation failed: {str(e)}", exc_info=True)
            raise

    def _fetch_ssurgo_data(
        self,
        location: Location,
        database: str = 'gssurgo',
        resolution: int = 30
    ) -> Tuple[Optional[pd.DataFrame], Dict[str, Any]]:
        """
        Fetch SSURGO data for a point location.

        Args:
            location: Geographic coordinates
            database: SSURGO database identifier
            resolution: Spatial resolution in meters

        Returns:
            Tuple of (DataFrame with soil data, dict with mukey info)
        """
        try:
            logger.info(f"Fetching SSURGO data from {database} at resolution {resolution}m")

            # Create point geometry and small buffer for AOI
            point = Point(location.longitude, location.latitude)
            aoi_gdf = gpd.GeoDataFrame(
                {'geometry': [point.buffer(0.001)]},  # Small buffer (~100m)
                crs="EPSG:4326"
            )

            # Fetch mukey raster
            try:
                mukey_raster = GAEZ_SSURGO_data.mukey_wcs(
                    aoi=aoi_gdf,
                    db=database,
                    res=resolution
                )
            except Exception as e:
                logger.error(f"Failed to fetch mukey raster: {str(e)}")
                raise SSURGODataError(f"Cannot retrieve SSURGO data: {str(e)}")

            # Extract unique mukeys from raster
            import numpy as np
            raster_data = mukey_raster.read(1)  # Read first band as numpy array
            mukeys = np.unique(raster_data[raster_data > 0]).tolist()

            # Close the rasterio dataset to free resources
            mukey_raster.close()

            if not mukeys:
                raise SSURGODataError("No valid SSURGO map units found at location")

            logger.info(f"Found {len(mukeys)} map unit(s): {mukeys}")

            # Fetch component-horizon data for mukeys
            ssurgo_data = GAEZ_SSURGO_data.ssurgo_gaez_data(mukeys)

            if ssurgo_data is None or len(ssurgo_data) == 0:
                raise SSURGODataError("No component data available for map units")

            # Get info about the dominant component
            mukey_info = {
                'mukey': str(mukeys[0]) if mukeys else None,
                'component_name': ssurgo_data.iloc[0].get('compname', 'Unknown') if len(ssurgo_data) > 0 else None,
                'total_components': len(ssurgo_data['cokey'].unique()) if 'cokey' in ssurgo_data.columns else 0
            }

            logger.info(f"Retrieved {len(ssurgo_data)} horizons from {mukey_info['total_components']} component(s)")

            return ssurgo_data, mukey_info

        except SSURGODataError:
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching SSURGO data: {str(e)}", exc_info=True)
            raise SSURGODataError(f"Failed to retrieve SSURGO data: {str(e)}")

    def _integrate_user_data(
        self,
        ssurgo_data: pd.DataFrame,
        user_data,
        data_sources_info: Dict[str, Any]
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """
        Integrate user-provided plot, site, and lab data with SSURGO data.

        Args:
            ssurgo_data: DataFrame with SSURGO soil data
            user_data: UserData object with optional plot/site/lab data
            data_sources_info: Dict tracking data sources used

        Returns:
            Tuple of (updated DataFrame, updated data_sources_info)
        """
        working_data = ssurgo_data.copy()

        try:
            # Process plot data (field measurements)
            if user_data.plot_data and len(user_data.plot_data) > 0:
                logger.info(f"Integrating {len(user_data.plot_data)} user plot data horizons")
                plot_df = self._convert_plot_data_to_df(user_data.plot_data)
                working_data = GAEZ_soil_data_processing.process_plot_data(
                    plot_data=plot_df,
                    map_data=working_data
                )
                data_sources_info['user_plot_data_used'] = True
                data_sources_info['horizons_count'] = len(working_data)

            # Process site data (site characteristics)
            if user_data.site_data:
                logger.info("Integrating user site data")
                site_df = self._convert_site_data_to_df(user_data.site_data)
                working_data = GAEZ_soil_data_processing.process_site_data(
                    site_data=site_df,
                    map_data=working_data
                )
                data_sources_info['user_site_data_used'] = True

            # Process lab data (laboratory measurements)
            if user_data.lab_data and len(user_data.lab_data) > 0:
                logger.info(f"Integrating {len(user_data.lab_data)} user lab data samples")
                lab_df = self._convert_lab_data_to_df(user_data.lab_data)
                working_data = GAEZ_soil_data_processing.process_lab_data(
                    lab_data=lab_df,
                    map_data=working_data
                )
                data_sources_info['user_lab_data_used'] = True

        except Exception as e:
            logger.warning(f"Error integrating user data: {str(e)}")
            # Continue with SSURGO data only
            logger.info("Continuing calculation with SSURGO data only")

        return working_data, data_sources_info

    def _convert_plot_data_to_df(self, plot_data: list) -> pd.DataFrame:
        """Convert API plot data models to DataFrame format expected by GAEZ functions."""
        records = []
        for horizon in plot_data:
            record = {
                'hzdept': horizon.top_depth,
                'hzdepb': horizon.bottom_depth,
            }
            # Add optional fields if provided
            if horizon.sand_pct is not None:
                record['sandtotal'] = horizon.sand_pct
            if horizon.silt_pct is not None:
                record['silttotal'] = horizon.silt_pct
            if horizon.clay_pct is not None:
                record['claytotal'] = horizon.clay_pct
            if horizon.organic_matter_pct is not None:
                record['om'] = horizon.organic_matter_pct
            if horizon.organic_carbon_pct is not None:
                record['OC'] = horizon.organic_carbon_pct
            if horizon.ph is not None:
                record['ph'] = horizon.ph
            if horizon.cec_soil is not None:
                record['cecs'] = horizon.cec_soil
            if horizon.base_saturation is not None:
                record['BS'] = horizon.base_saturation
            if horizon.ec is not None:
                record['ec'] = horizon.ec
            if horizon.esp is not None:
                record['ESP'] = horizon.esp
            if horizon.caco3_pct is not None:
                record['caco3'] = horizon.caco3_pct
            if horizon.gypsum_pct is not None:
                record['gypsum'] = horizon.gypsum_pct
            if horizon.bulk_density is not None:
                record['DB'] = horizon.bulk_density
            if horizon.coarse_fragments_pct is not None:
                record['CF'] = horizon.coarse_fragments_pct

            records.append(record)

        return pd.DataFrame(records)

    def _convert_site_data_to_df(self, site_data) -> pd.DataFrame:
        """Convert API site data model to DataFrame format expected by GAEZ functions."""
        record = {}

        if site_data.drainage_class is not None:
            record['drainage_cl'] = site_data.drainage_class
        if site_data.slope_pct is not None:
            record['slope'] = site_data.slope_pct
        if site_data.elevation_m is not None:
            record['elevation'] = site_data.elevation_m
        if site_data.water_table_depth_cm is not None:
            record['wt_depth'] = site_data.water_table_depth_cm
        if site_data.bedrock_depth_cm is not None:
            record['bedrock_depth'] = site_data.bedrock_depth_cm
        if site_data.cemented_layer_depth_cm is not None:
            record['cemented_depth'] = site_data.cemented_layer_depth_cm
        if site_data.flooding_frequency is not None:
            record['flooding_freq'] = site_data.flooding_frequency
        if site_data.ponding_frequency is not None:
            record['ponding_freq'] = site_data.ponding_frequency

        return pd.DataFrame([record])

    def _convert_lab_data_to_df(self, lab_data: list) -> pd.DataFrame:
        """Convert API lab data models to DataFrame format expected by GAEZ functions."""
        records = []
        for sample in lab_data:
            record = {
                'sample_id': sample.sample_id,
                'depth': sample.depth_cm,
            }

            # Map lab data fields to GAEZ column names
            if sample.ph_h2o is not None:
                record['ph'] = sample.ph_h2o
            if sample.organic_carbon_pct is not None:
                record['OC'] = sample.organic_carbon_pct
            if sample.cec_cmol_kg is not None:
                record['cecs'] = sample.cec_cmol_kg
            if sample.base_saturation_pct is not None:
                record['BS'] = sample.base_saturation_pct
            if sample.ec_ds_m is not None:
                record['ec'] = sample.ec_ds_m
            if sample.esp_pct is not None:
                record['ESP'] = sample.esp_pct
            if sample.caco3_pct is not None:
                record['caco3'] = sample.caco3_pct
            if sample.gypsum_pct is not None:
                record['gypsum'] = sample.gypsum_pct
            if sample.sand_pct is not None:
                record['sandtotal'] = sample.sand_pct
            if sample.silt_pct is not None:
                record['silttotal'] = sample.silt_pct
            if sample.clay_pct is not None:
                record['claytotal'] = sample.clay_pct
            if sample.bulk_density_g_cm3 is not None:
                record['DB'] = sample.bulk_density_g_cm3

            records.append(record)

        return pd.DataFrame(records)

    def _get_depth_weight_type(self, crop_id: str, requested_type: Optional[int]) -> int:
        """
        Determine depth weight type for crop.

        Args:
            crop_id: GAEZ crop identifier
            requested_type: User-requested depth type (optional)

        Returns:
            Depth weight type (1-4)
        """
        if requested_type is not None:
            logger.info(f"Using user-specified depth weight type: {requested_type}")
            return requested_type

        # Get default from GAEZ lookup
        try:
            from GAEZ_SQI_functions import GAEZ_DEPTH_WEIGHT_LOOKUP
            default_type = GAEZ_DEPTH_WEIGHT_LOOKUP.get(crop_id, 3)  # Default to deep (3)
            logger.info(f"Using default depth weight type for crop {crop_id}: {default_type}")
            return default_type
        except Exception:
            logger.warning(f"Could not find depth weight for crop {crop_id}, using default (3)")
            return 3

    def _generate_result_message(
        self,
        sqi_results: pd.DataFrame,
        data_sources_info: Dict[str, Any]
    ) -> Optional[str]:
        """Generate informative message about calculation results."""
        messages = []

        # Report on data sources used
        if data_sources_info.get('user_plot_data_used'):
            messages.append("User plot data integrated into calculations")
        if data_sources_info.get('user_site_data_used'):
            messages.append("User site data integrated into calculations")
        if data_sources_info.get('user_lab_data_used'):
            messages.append("User lab data integrated into calculations")

        # Report on soil rating quality
        if len(sqi_results) > 0:
            sr = _safe_float(sqi_results.iloc[0].get('SR'))
            if sr >= 80:
                quality = "Excellent"
            elif sr >= 60:
                quality = "Good"
            elif sr >= 40:
                quality = "Moderate"
            elif sr >= 20:
                quality = "Poor"
            else:
                quality = "Very Poor"
            messages.append(f"Overall soil suitability: {quality} (SR={sr:.1f})")

        return "; ".join(messages) if messages else None

    def get_available_crops(self) -> CropListResponse:
        """
        Get list of available crops with their default parameters.

        Returns:
            CropListResponse with crop information
        """
        try:
            from GAEZ_SQI_functions import GAEZ_DEPTH_WEIGHT_LOOKUP
        except Exception:
            GAEZ_DEPTH_WEIGHT_LOOKUP = {}

        crops = []
        for crop_id, crop_name in sorted(CROP_NAMES.items()):
            default_depth = GAEZ_DEPTH_WEIGHT_LOOKUP.get(crop_id, 3)
            crops.append(CropListItem(
                crop_id=crop_id,
                crop_name=crop_name,
                default_depth_weight=default_depth,
                depth_description=DEPTH_DESCRIPTIONS[default_depth]
            ))

        return CropListResponse(
            status="success",
            crops=crops,
            total_count=len(crops)
        )
