# GAEZ Soil Quality Index API

A flexible REST API for calculating crop-specific soil quality indices and suitability ratings using the FAO GAEZ v4 methodology adapted for the United States.

## Features

- **Automatic SSURGO Integration**: Just provide lat/lon coordinates - the API automatically retrieves soil data
- **Flexible Input Options**: Enhance calculations with user-provided field measurements, lab data, or site characteristics
- **46+ Crops Supported**: Comprehensive crop database from wheat and maize to specialty crops
- **7 Soil Quality Indices**: Complete soil assessment (SQ1-SQ7) plus overall rating (SR)
- **3 Input Levels**: Low, Intermediate, and High agricultural input scenarios

## Quick Start

### Installation

```bash
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts
pip install -r api/requirements.txt
```

### Running the API Server

```bash
# Development mode with auto-reload
python -m api.main

# Or using uvicorn directly
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Endpoint**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## API Endpoints

### 1. Calculate Soil Quality Indices

**POST** `/api/v1/calculate`

Calculate crop-specific soil quality indices for a location.

#### Minimum Request (SSURGO-only mode)

```bash
curl -X POST "http://localhost:8000/api/v1/calculate" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "latitude": 41.2042,
      "longitude": -101.6353
    },
    "crop_id": "4",
    "input_level": "L"
  }'
```

#### Enhanced Request with User Data

```bash
curl -X POST "http://localhost:8000/api/v1/calculate" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {
      "latitude": 41.2042,
      "longitude": -101.6353
    },
    "crop_id": "4",
    "input_level": "H",
    "depth_weight_type": 3,
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
          "organic_matter_pct": 1.8
        }
      ],
      "site_data": {
        "drainage_class": "well drained",
        "slope_pct": 2.5,
        "elevation_m": 850
      },
      "lab_data": [
        {
          "sample_id": "Lab-001",
          "depth_cm": 15,
          "ph_h2o": 6.5,
          "organic_carbon_pct": 1.86,
          "cec_cmol_kg": 18.5,
          "base_saturation_pct": 85.0
        }
      ]
    }
  }'
```

#### Response

```json
{
  "status": "success",
  "location": {
    "latitude": 41.2042,
    "longitude": -101.6353
  },
  "crop_info": {
    "crop_id": "4",
    "crop_name": "Maize",
    "input_level": "H",
    "depth_weight_type": 3,
    "rooting_depth_description": "Deep rooting (0-100 cm)"
  },
  "soil_quality_indices": {
    "SQ1": 72.5,
    "SQ2": 78.3,
    "SQ3": 85.0,
    "SQ4": 90.0,
    "SQ5": 95.0,
    "SQ6": 100.0,
    "SQ7": 88.0,
    "SR": 65.8
  },
  "data_sources": {
    "ssurgo_used": true,
    "ssurgo_component": "Holdrege silt loam",
    "ssurgo_map_unit": "2494182",
    "user_plot_data_used": true,
    "user_site_data_used": true,
    "user_lab_data_used": true,
    "horizons_count": 2
  },
  "metadata": {
    "calculation_timestamp": "2025-11-18T12:34:56Z",
    "api_version": "0.1.0",
    "gaez_version": "4.0",
    "processing_time_seconds": 2.345
  },
  "message": "User plot data integrated; User site data integrated; User lab data integrated; Overall soil suitability: Good (SR=65.8)"
}
```

### 2. List Available Crops

**GET** `/api/v1/crops`

Get list of all supported crops with their default parameters.

```bash
curl "http://localhost:8000/api/v1/crops"
```

#### Response

```json
{
  "status": "success",
  "crops": [
    {
      "crop_id": "1",
      "crop_name": "Wheat",
      "default_depth_weight": 3,
      "depth_description": "Deep rooting (0-100 cm)"
    },
    {
      "crop_id": "4",
      "crop_name": "Maize",
      "default_depth_weight": 3,
      "depth_description": "Deep rooting (0-100 cm)"
    }
  ],
  "total_count": 46
}
```

### 3. Health Check

**GET** `/health`

Check API health status and service availability.

```bash
curl "http://localhost:8000/health"
```

## Request Parameters

### Location (Required)

```json
{
  "latitude": 41.2042,   // -90 to 90
  "longitude": -101.6353 // -180 to 180
}
```

### Crop ID (Required)

Common crop IDs:
- `"1"`: Wheat
- `"2"`: Rice
- `"4"`: Maize
- `"5"`: Sorghum
- `"11"`: Cassava
- `"13"`: Sugarcane
- `"15a"`: Soybean (Rain-fed)
- `"22"`: Banana/Plantain
- `"23"`: Citrus
- `"29"`: Cotton

See `/api/v1/crops` for complete list.

### Input Level (Required)

- `"L"`: Low input (subsistence farming)
- `"I"`: Intermediate input
- `"H"`: High input (commercial farming with fertilizers)

### Depth Weight Type (Optional)

- `1`: Shallow rooting (0-30 cm) - e.g., onions, leafy vegetables
- `2`: Moderate rooting (0-60 cm) - e.g., rice, potatoes
- `3`: Deep rooting (0-100 cm) - e.g., wheat, maize (default for most crops)
- `4`: Very deep rooting (0-150 cm) - e.g., sugarcane, alfalfa

Auto-determined from crop if not specified.

### SSURGO Database (Optional)

- `"gssurgo"`: Continental US (default)
- `"pr_ssurgo"`: Puerto Rico
- `"hi_ssurgo"`: Hawaii

### User Data (Optional)

#### Plot Data (Field Measurements)

Array of soil horizons with measurements:

```json
{
  "horizon_id": "Ap",
  "top_depth": 0,          // cm
  "bottom_depth": 25,      // cm
  "sand_pct": 45.0,        // 0-100
  "silt_pct": 35.0,        // 0-100
  "clay_pct": 20.0,        // 0-100 (must sum to 100)
  "ph": 6.5,               // 0-14
  "organic_matter_pct": 3.2,    // 0-100
  "organic_carbon_pct": 1.86,   // 0-100
  "bulk_density": 1.35,         // g/cm³
  "cec_soil": 18.5,            // cmol/kg
  "base_saturation": 85.0,      // 0-100
  "ec": 0.5,                    // dS/m
  "esp": 2.0,                   // 0-100
  "caco3_pct": 0.0,            // 0-100
  "gypsum_pct": 0.0,           // 0-100
  "coarse_fragments_pct": 5.0   // 0-100
}
```

#### Site Data (Site Characteristics)

```json
{
  "drainage_class": "well drained",
  "slope_pct": 2.5,                    // 0-100
  "elevation_m": 850,
  "water_table_depth_cm": 150,         // cm
  "has_bedrock": false,
  "bedrock_depth_cm": null,
  "has_cemented_layer": false,
  "cemented_layer_depth_cm": null,
  "flooding_frequency": "none",
  "ponding_frequency": "none"
}
```

#### Lab Data (Laboratory Analysis)

Array of lab samples:

```json
{
  "sample_id": "Lab-001",
  "depth_cm": 15,
  "ph_h2o": 6.5,                // pH in water
  "ph_cacl2": 6.0,              // pH in CaCl2
  "organic_carbon_pct": 1.86,
  "total_nitrogen_pct": 0.15,
  "available_p_ppm": 25.0,
  "available_k_ppm": 180.0,
  "cec_cmol_kg": 18.5,
  "base_saturation_pct": 85.0,
  "ec_ds_m": 0.5,
  "sar": 1.2,
  "esp_pct": 2.0,
  "caco3_pct": 0.0,
  "gypsum_pct": 0.0,
  "sand_pct": 45.0,
  "silt_pct": 35.0,
  "clay_pct": 20.0,
  "bulk_density_g_cm3": 1.35
}
```

## Soil Quality Indices

### SQ1: Nutrient Availability (Low Input)

Evaluates soil's natural nutrient supply based on:
- Organic carbon (OC)
- pH
- Total Exchangeable Bases (TEB)
- Texture class

**Score Range**: 0-100 (higher is better)

### SQ2: Nutrient Retention (High Input)

Evaluates soil's ability to retain added nutrients:
- Base Saturation (BS)
- CEC of soil and clay
- pH
- Texture class

**Score Range**: 0-100 (higher is better)

### SQ3: Rooting Conditions

Evaluates physical conditions for root growth:
- Soil depth
- Vertic properties
- Gelic conditions
- Bulk density
- Coarse fragments
- Root restrictions

**Score Range**: 0-100 (higher is better)

### SQ4: Oxygen Availability

Evaluates aeration and drainage:
- Drainage class
- Impermeable layers
- Soil phases

**Score Range**: 0-100 (higher is better)

### SQ5: Salinity & Sodicity

Evaluates salt and sodium constraints:
- Electrical Conductivity (EC)
- Exchangeable Sodium Percentage (ESP)
- Saline/sodic phases

**Score Range**: 0-100 (higher is better, 100 = no salinity issues)

### SQ6: Lime & Gypsum

Evaluates calcium carbonate and gypsum content:
- CaCO₃ percentage
- Gypsum percentage
- Related soil phases

**Score Range**: 0-100 (higher is better, 100 = no excess lime/gypsum)

### SQ7: Workability

Evaluates ease of tillage and management:
- Texture
- Bulk density
- Coarse fragments
- Vertic properties
- Soil phases

**Score Range**: 0-100 (higher is better)

### SR: Overall Soil Rating

Combined rating based on input level:

**Low Input (L)**:
```
SR = SQ1 × (SQ3/100) × (min(SQ4,SQ5,SQ6,SQ7)/100)
```

**Intermediate Input (I)**:
```
SR = 0.5×(SQ1+SQ2) × (SQ3/100) × (min(SQ4,SQ5,SQ6,SQ7)/100)
```

**High Input (H)**:
```
SR = SQ2 × (SQ3/100) × (min(SQ4,SQ7)/100)
```

**Interpretation**:
- **80-100**: Excellent suitability
- **60-79**: Good suitability
- **40-59**: Moderate suitability
- **20-39**: Poor suitability
- **0-19**: Very poor suitability

## Python Client Examples

### Basic Usage

```python
import requests

# Simple calculation with SSURGO data only
response = requests.post(
    "http://localhost:8000/api/v1/calculate",
    json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",  # Maize
        "input_level": "L"
    }
)

result = response.json()
print(f"Soil Rating: {result['soil_quality_indices']['SR']}")
print(f"Component: {result['data_sources']['ssurgo_component']}")
```

### With User Data

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/calculate",
    json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",
        "input_level": "H",
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
                    "organic_matter_pct": 3.2
                }
            ],
            "site_data": {
                "drainage_class": "well drained",
                "slope_pct": 2.5
            }
        }
    }
)

result = response.json()

# Print all SQI scores
sqi = result['soil_quality_indices']
print(f"SQ1 (Nutrient Availability): {sqi['SQ1']}")
print(f"SQ2 (Nutrient Retention): {sqi['SQ2']}")
print(f"SQ3 (Rooting Conditions): {sqi['SQ3']}")
print(f"SQ4 (Oxygen Availability): {sqi['SQ4']}")
print(f"SQ5 (Salinity/Sodicity): {sqi['SQ5']}")
print(f"SQ6 (Lime/Gypsum): {sqi['SQ6']}")
print(f"SQ7 (Workability): {sqi['SQ7']}")
print(f"Overall Rating: {sqi['SR']}")
```

### List Available Crops

```python
import requests

response = requests.get("http://localhost:8000/api/v1/crops")
crops = response.json()

for crop in crops['crops'][:10]:  # First 10 crops
    print(f"{crop['crop_id']}: {crop['crop_name']} - {crop['depth_description']}")
```

## Error Handling

### Error Response Format

```json
{
  "status": "error",
  "error_code": "SSURGO_DATA_ERROR",
  "message": "No SSURGO data available for location (45.0, -95.0)",
  "details": {
    "exception_type": "SSURGODataError"
  }
}
```

### Common Error Codes

- **`SSURGO_DATA_ERROR`** (404): No SSURGO data at location
- **`CALCULATION_ERROR`** (500): Error during SQI calculation
- **`SERVICE_ERROR`** (500): Service configuration error
- **`INTERNAL_ERROR`** (500): Unexpected error

### Example Error Handling

```python
import requests

try:
    response = requests.post(
        "http://localhost:8000/api/v1/calculate",
        json={
            "location": {"latitude": 41.2042, "longitude": -101.6353},
            "crop_id": "4",
            "input_level": "L"
        }
    )
    response.raise_for_status()
    result = response.json()

except requests.exceptions.HTTPError as e:
    error = e.response.json()
    print(f"Error {error['error_code']}: {error['message']}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

## Data Priority

When both SSURGO and user data are provided:

1. **User plot data** takes priority for horizon-level soil properties
2. **User lab data** takes priority for chemical analyses
3. **User site data** takes priority for drainage, slope, restrictions
4. **SSURGO data** fills in any missing parameters

This allows you to:
- Override specific SSURGO values with field measurements
- Supplement incomplete field data with SSURGO estimates
- Gradually improve accuracy as more user data becomes available

## Production Deployment

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY code/US_scripts /app
RUN pip install -r api/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables

```bash
# Optional configuration
export GAEZ_API_HOST="0.0.0.0"
export GAEZ_API_PORT="8000"
export GAEZ_LOG_LEVEL="INFO"
```

### Security Considerations

- Configure CORS appropriately for production
- Implement rate limiting
- Add authentication/authorization if needed
- Use HTTPS in production
- Validate and sanitize all user inputs (already implemented via Pydantic)

## Performance

- Typical response time: 2-5 seconds
- SSURGO data retrieval: ~1-2 seconds (cached by USDA)
- SQI calculation: ~0.5-1 second
- User data integration adds minimal overhead

## Limitations

- SSURGO data only available for US, Puerto Rico, and Hawaii
- Requires internet connection for SSURGO data retrieval
- Resolution limited by SSURGO (30m for gSSURGO)
- Some crop-specific parameters may need calibration for local conditions

## Support

For issues, questions, or contributions:
- GitHub: https://github.com/jjmaynard/GAEZ-Hyperlocalization
- Documentation: See `/docs` endpoint or browse to http://localhost:8000/docs

## License

MIT License - See project repository for details
