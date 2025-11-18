"""
Pydantic models for GAEZ API request/response validation.
"""

from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum


class InputLevel(str, Enum):
    """Agricultural input levels."""
    LOW = "L"
    INTERMEDIATE = "I"
    HIGH = "H"


class Location(BaseModel):
    """Geographic location specification."""
    latitude: float = Field(..., ge=-90, le=90, description="Latitude in decimal degrees")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude in decimal degrees")

    @field_validator('latitude', 'longitude')
    @classmethod
    def validate_coordinates(cls, v, info):
        if v is None:
            raise ValueError(f"{info.field_name} cannot be None")
        return v


class PlotDataHorizon(BaseModel):
    """User-provided plot/field measurements for a soil horizon."""
    horizon_id: str = Field(..., description="Unique identifier for the horizon")
    top_depth: float = Field(..., ge=0, description="Top depth of horizon in cm")
    bottom_depth: float = Field(..., gt=0, description="Bottom depth of horizon in cm")

    # Texture
    sand_pct: Optional[float] = Field(None, ge=0, le=100, description="Sand percentage")
    silt_pct: Optional[float] = Field(None, ge=0, le=100, description="Silt percentage")
    clay_pct: Optional[float] = Field(None, ge=0, le=100, description="Clay percentage")

    # Chemistry
    organic_matter_pct: Optional[float] = Field(None, ge=0, le=100, description="Organic matter %")
    organic_carbon_pct: Optional[float] = Field(None, ge=0, le=100, description="Organic carbon %")
    ph: Optional[float] = Field(None, ge=0, le=14, description="pH value")
    cec_soil: Optional[float] = Field(None, ge=0, description="CEC of soil (cmol/kg)")
    base_saturation: Optional[float] = Field(None, ge=0, le=100, description="Base saturation %")
    ec: Optional[float] = Field(None, ge=0, description="Electrical conductivity (dS/m)")
    esp: Optional[float] = Field(None, ge=0, le=100, description="Exchangeable sodium %")
    caco3_pct: Optional[float] = Field(None, ge=0, le=100, description="Calcium carbonate %")
    gypsum_pct: Optional[float] = Field(None, ge=0, le=100, description="Gypsum %")

    # Physical properties
    bulk_density: Optional[float] = Field(None, ge=0, description="Bulk density (g/cm³)")
    coarse_fragments_pct: Optional[float] = Field(None, ge=0, le=100, description="Coarse fragments %")

    @model_validator(mode='after')
    def validate_depth_order(self):
        if self.bottom_depth <= self.top_depth:
            raise ValueError("bottom_depth must be greater than top_depth")
        return self

    @model_validator(mode='after')
    def validate_texture_sum(self):
        if all(v is not None for v in [self.sand_pct, self.silt_pct, self.clay_pct]):
            total = self.sand_pct + self.silt_pct + self.clay_pct
            if not (99 <= total <= 101):  # Allow small rounding errors
                raise ValueError(f"Sand + Silt + Clay must sum to 100, got {total}")
        return self


class SiteData(BaseModel):
    """User-provided site characteristics."""
    drainage_class: Optional[str] = Field(None, description="USDA drainage class")
    slope_pct: Optional[float] = Field(None, ge=0, le=100, description="Slope percentage")
    elevation_m: Optional[float] = Field(None, description="Elevation in meters")
    water_table_depth_cm: Optional[float] = Field(None, ge=0, description="Water table depth in cm")

    # Phases/restrictions
    has_bedrock: Optional[bool] = Field(None, description="Presence of bedrock restriction")
    bedrock_depth_cm: Optional[float] = Field(None, ge=0, description="Depth to bedrock in cm")
    has_cemented_layer: Optional[bool] = Field(None, description="Presence of cemented layer")
    cemented_layer_depth_cm: Optional[float] = Field(None, ge=0, description="Depth to cemented layer in cm")
    flooding_frequency: Optional[str] = Field(None, description="Flooding frequency class")
    ponding_frequency: Optional[str] = Field(None, description="Ponding frequency class")


class LabData(BaseModel):
    """Laboratory analysis results."""
    sample_id: str = Field(..., description="Laboratory sample identifier")
    depth_cm: float = Field(..., ge=0, description="Sample depth in cm")

    # Chemical analysis
    ph_h2o: Optional[float] = Field(None, ge=0, le=14, description="pH in water")
    ph_cacl2: Optional[float] = Field(None, ge=0, le=14, description="pH in CaCl2")
    organic_carbon_pct: Optional[float] = Field(None, ge=0, description="Organic carbon %")
    total_nitrogen_pct: Optional[float] = Field(None, ge=0, description="Total nitrogen %")
    available_p_ppm: Optional[float] = Field(None, ge=0, description="Available phosphorus (ppm)")
    available_k_ppm: Optional[float] = Field(None, ge=0, description="Available potassium (ppm)")
    cec_cmol_kg: Optional[float] = Field(None, ge=0, description="CEC (cmol/kg)")
    base_saturation_pct: Optional[float] = Field(None, ge=0, le=100, description="Base saturation %")
    ec_ds_m: Optional[float] = Field(None, ge=0, description="Electrical conductivity (dS/m)")
    sar: Optional[float] = Field(None, ge=0, description="Sodium adsorption ratio")
    esp_pct: Optional[float] = Field(None, ge=0, le=100, description="Exchangeable sodium %")
    caco3_pct: Optional[float] = Field(None, ge=0, le=100, description="Calcium carbonate %")
    gypsum_pct: Optional[float] = Field(None, ge=0, le=100, description="Gypsum %")

    # Particle size analysis
    sand_pct: Optional[float] = Field(None, ge=0, le=100, description="Sand %")
    silt_pct: Optional[float] = Field(None, ge=0, le=100, description="Silt %")
    clay_pct: Optional[float] = Field(None, ge=0, le=100, description="Clay %")

    # Physical properties
    bulk_density_g_cm3: Optional[float] = Field(None, ge=0, description="Bulk density (g/cm³)")


class UserData(BaseModel):
    """Container for all user-provided data."""
    plot_data: Optional[List[PlotDataHorizon]] = Field(None, description="Field measurements by horizon")
    site_data: Optional[SiteData] = Field(None, description="Site characteristics")
    lab_data: Optional[List[LabData]] = Field(None, description="Laboratory analysis results")


class CalculationRequest(BaseModel):
    """Main request for soil quality index calculation."""
    location: Location = Field(..., description="Geographic coordinates")
    crop_id: str = Field(..., description="GAEZ crop identifier (e.g., '4' for maize)")
    input_level: InputLevel = Field(..., description="Agricultural input level (L/I/H)")
    depth_weight_type: Optional[int] = Field(
        None,
        ge=1,
        le=4,
        description="Rooting depth type (1=shallow, 2=moderate, 3=deep, 4=very deep). Auto-determined if not provided."
    )
    user_data: Optional[UserData] = Field(None, description="Optional user-provided soil and site data")
    ssurgo_database: Optional[Literal["gssurgo", "pr_ssurgo", "hi_ssurgo"]] = Field(
        "gssurgo",
        description="SSURGO database to query (gssurgo for continental US, pr_ssurgo for Puerto Rico, hi_ssurgo for Hawaii)"
    )
    ssurgo_resolution: Optional[int] = Field(
        30,
        ge=10,
        le=1000,
        description="Spatial resolution for SSURGO data in meters"
    )


class SoilQualityIndices(BaseModel):
    """Calculated soil quality index scores."""
    SQ1: float = Field(..., description="Nutrient Availability (low input)")
    SQ2: float = Field(..., description="Nutrient Retention (high input)")
    SQ3: float = Field(..., description="Rooting Conditions")
    SQ4: float = Field(..., description="Oxygen Availability")
    SQ5: float = Field(..., description="Salinity & Sodicity")
    SQ6: float = Field(..., description="Lime & Gypsum")
    SQ7: float = Field(..., description="Workability")
    SR: float = Field(..., description="Overall Soil Rating (0-100)")


class DataSources(BaseModel):
    """Information about data sources used in calculation."""
    ssurgo_used: bool = Field(..., description="Whether SSURGO data was used")
    ssurgo_component: Optional[str] = Field(None, description="SSURGO component name")
    ssurgo_map_unit: Optional[str] = Field(None, description="SSURGO map unit key")
    user_plot_data_used: bool = Field(False, description="Whether user plot data was integrated")
    user_site_data_used: bool = Field(False, description="Whether user site data was integrated")
    user_lab_data_used: bool = Field(False, description="Whether user lab data was integrated")
    horizons_count: int = Field(..., description="Number of soil horizons analyzed")


class CropInfo(BaseModel):
    """Crop-specific calculation parameters."""
    crop_id: str = Field(..., description="GAEZ crop identifier")
    crop_name: Optional[str] = Field(None, description="Crop common name")
    input_level: str = Field(..., description="Input level used (L/I/H)")
    depth_weight_type: int = Field(..., description="Rooting depth type applied (1-4)")
    rooting_depth_description: str = Field(..., description="Rooting depth category")


class CalculationMetadata(BaseModel):
    """Metadata about the calculation."""
    calculation_timestamp: str = Field(..., description="ISO 8601 timestamp of calculation")
    api_version: str = Field(..., description="API version")
    gaez_version: str = Field("4.0", description="GAEZ methodology version")
    processing_time_seconds: float = Field(..., description="Calculation processing time")


class CalculationResponse(BaseModel):
    """Response containing soil quality indices and metadata."""
    status: Literal["success", "error"] = Field(..., description="Calculation status")
    location: Location = Field(..., description="Location coordinates")
    crop_info: CropInfo = Field(..., description="Crop calculation parameters")
    soil_quality_indices: SoilQualityIndices = Field(..., description="Calculated SQI scores")
    data_sources: DataSources = Field(..., description="Data sources used")
    metadata: CalculationMetadata = Field(..., description="Calculation metadata")
    message: Optional[str] = Field(None, description="Additional information or warnings")


class ErrorResponse(BaseModel):
    """Error response structure."""
    status: Literal["error"] = "error"
    error_code: str = Field(..., description="Error code identifier")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class CropListItem(BaseModel):
    """Information about an available crop."""
    crop_id: str = Field(..., description="GAEZ crop identifier")
    crop_name: str = Field(..., description="Crop common name")
    default_depth_weight: int = Field(..., description="Default rooting depth type")
    depth_description: str = Field(..., description="Rooting depth category")


class CropListResponse(BaseModel):
    """Response containing list of available crops."""
    status: Literal["success"] = "success"
    crops: List[CropListItem] = Field(..., description="List of available crops")
    total_count: int = Field(..., description="Total number of crops available")


class HealthResponse(BaseModel):
    """Health check response."""
    status: Literal["healthy", "unhealthy"] = Field(..., description="Service health status")
    version: str = Field(..., description="API version")
    timestamp: str = Field(..., description="Current server timestamp")
    services: Dict[str, str] = Field(..., description="Status of dependent services")
