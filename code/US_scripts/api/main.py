"""
FastAPI application for GAEZ Soil Quality Index API.

This API provides crop-specific soil quality assessments based on:
- SSURGO spatial data (automatic retrieval by lat/lon)
- Optional user-provided field measurements, lab data, and site characteristics
"""

import logging
from typing import Dict, Any
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn

from .models import (
    CalculationRequest,
    CalculationResponse,
    ErrorResponse,
    CropListResponse,
    HealthResponse
)
from .service import (
    GAEZCalculationService,
    GAEZCalculationError,
    SSURGODataError,
    CalculationServiceError
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="GAEZ Soil Quality Index API",
    description="""
    API for calculating crop-specific soil quality indices and suitability ratings
    using the FAO GAEZ v4 methodology adapted for the United States.

    ## Features

    - **Automatic SSURGO Data Retrieval**: Provide only lat/lon coordinates
    - **Flexible Input Options**: Optionally enhance calculations with:
        - Field measurements (soil horizons)
        - Laboratory test results
        - Site characteristics
    - **46+ Crops Supported**: From wheat and maize to specialty crops
    - **7 Soil Quality Indices**: Comprehensive soil assessment (SQ1-SQ7)
    - **3 Input Levels**: Low, Intermediate, and High agricultural inputs

    ## Calculation Methodology

    The API calculates 7 soil quality indices:
    - **SQ1**: Nutrient Availability (low input systems)
    - **SQ2**: Nutrient Retention (high input systems)
    - **SQ3**: Rooting Conditions
    - **SQ4**: Oxygen Availability
    - **SQ5**: Salinity & Sodicity
    - **SQ6**: Lime & Gypsum
    - **SQ7**: Workability

    Final **Soil Rating (SR)** is calculated based on input level:
    - Low: SR = SQ1 × (SQ3/100) × (min(SQ4-7)/100)
    - Intermediate: SR = 0.5×(SQ1+SQ2) × (SQ3/100) × (min(SQ4-7)/100)
    - High: SR = SQ2 × (SQ3/100) × (min(SQ4,SQ7)/100)
    """,
    version="0.1.0",
    contact={
        "name": "GAEZ Hyperlocalization Project",
        "url": "https://github.com/jjmaynard/GAEZ-Hyperlocalization",
    },
    license_info={
        "name": "MIT",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add GZip compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Initialize service
calculation_service = GAEZCalculationService()


@app.exception_handler(GAEZCalculationError)
async def gaez_calculation_exception_handler(request: Request, exc: GAEZCalculationError):
    """Handle GAEZ calculation errors."""
    logger.error(f"GAEZ calculation error: {str(exc)}")

    error_code = "CALCULATION_ERROR"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if isinstance(exc, SSURGODataError):
        error_code = "SSURGO_DATA_ERROR"
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, CalculationServiceError):
        error_code = "SERVICE_ERROR"

    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(
            status="error",
            error_code=error_code,
            message=str(exc),
            details={"exception_type": type(exc).__name__}
        ).model_dump()
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected errors."""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            status="error",
            error_code="INTERNAL_ERROR",
            message="An unexpected error occurred",
            details={"error": str(exc)}
        ).model_dump()
    )


@app.get("/", include_in_schema=False)
async def root():
    """Redirect to API documentation."""
    return {
        "message": "GAEZ Soil Quality Index API",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json"
    }


@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    """
    Health check endpoint to verify API status.

    Returns service health status and version information.
    """
    try:
        # Test basic imports
        import GAEZ_SSURGO_data
        import GAEZ_SQI_functions
        ssurgo_status = "available"
    except Exception as e:
        logger.error(f"SSURGO module check failed: {e}")
        ssurgo_status = "unavailable"

    try:
        import GAEZ_crop_req
        crop_req_status = "available"
    except Exception as e:
        logger.error(f"Crop requirements module check failed: {e}")
        crop_req_status = "unavailable"

    all_healthy = ssurgo_status == "available" and crop_req_status == "available"

    return HealthResponse(
        status="healthy" if all_healthy else "unhealthy",
        version="0.1.0",
        timestamp=datetime.utcnow().isoformat() + 'Z',
        services={
            "ssurgo_data": ssurgo_status,
            "crop_requirements": crop_req_status,
            "sqi_calculations": "available"
        }
    )


@app.get("/api/v1/crops", response_model=CropListResponse, tags=["Crops"])
async def list_crops():
    """
    Get list of available crops with their default rooting depth parameters.

    Returns information about all 46+ crops supported by the GAEZ system,
    including crop IDs, names, and default depth weight types.
    """
    try:
        return calculation_service.get_available_crops()
    except Exception as e:
        logger.error(f"Error listing crops: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve crop list: {str(e)}"
        )


@app.post(
    "/api/v1/calculate",
    response_model=CalculationResponse,
    tags=["Calculations"],
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Calculation completed successfully"},
        400: {"model": ErrorResponse, "description": "Invalid request parameters"},
        404: {"model": ErrorResponse, "description": "No SSURGO data available for location"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def calculate_soil_quality(request: CalculationRequest):
    """
    Calculate crop-specific soil quality indices for a location.

    ## Input Options

    ### Minimum Required (SSURGO-only mode):
    ```json
    {
      "location": {"latitude": 41.2, "longitude": -101.6},
      "crop_id": "4",
      "input_level": "L"
    }
    ```

    ### Enhanced with User Data:
    ```json
    {
      "location": {"latitude": 41.2, "longitude": -101.6},
      "crop_id": "4",
      "input_level": "H",
      "user_data": {
        "plot_data": [
          {
            "horizon_id": "Ap",
            "top_depth": 0,
            "bottom_depth": 25,
            "sand_pct": 45,
            "silt_pct": 35,
            "clay_pct": 20,
            "ph": 6.5,
            "organic_matter_pct": 3.2
          }
        ],
        "site_data": {
          "drainage_class": "well drained",
          "slope_pct": 2.5
        },
        "lab_data": [
          {
            "sample_id": "Lab-001",
            "depth_cm": 15,
            "ph_h2o": 6.5,
            "organic_carbon_pct": 1.86,
            "cec_cmol_kg": 18.5
          }
        ]
      }
    }
    ```

    ## Output

    Returns 7 soil quality indices (SQ1-SQ7) plus overall soil rating (SR),
    along with metadata about data sources used and calculation parameters.

    ## Data Priority

    When user data is provided:
    1. User plot/lab data takes priority over SSURGO for soil properties
    2. User site data takes priority for drainage, slope, restrictions
    3. SSURGO data fills in any missing parameters

    ## Error Handling

    - **404**: No SSURGO data available for the specified location
    - **400**: Invalid coordinates, crop_id, or malformed user data
    - **500**: Calculation error or service unavailable
    """
    try:
        logger.info(f"Received calculation request for crop {request.crop_id} "
                   f"at ({request.location.latitude}, {request.location.longitude})")

        result = calculation_service.calculate_soil_quality(request)
        return result

    except SSURGODataError as e:
        logger.warning(f"SSURGO data not found: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except GAEZCalculationError as e:
        logger.error(f"Calculation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid request: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@app.post(
    "/api/v1/calculate/batch",
    tags=["Calculations"],
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    include_in_schema=False
)
async def calculate_batch():
    """Batch calculation endpoint (not yet implemented)."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Batch calculations not yet implemented"
    )


def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """
    Run the API server.

    Args:
        host: Host to bind to
        port: Port to listen on
        reload: Enable auto-reload for development
    """
    uvicorn.run(
        "api.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    run_server(reload=True)
