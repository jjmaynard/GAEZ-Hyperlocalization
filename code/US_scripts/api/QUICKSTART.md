# GAEZ API Quick Start Guide

Get started with the GAEZ Soil Quality Index API in 5 minutes.

## Installation

### 1. Install Dependencies

```bash
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts
pip install -r api/requirements.txt
```

### 2. Start the API Server

```bash
# Simple start
python run_api.py

# Or with custom options
python run_api.py --port 8080 --reload
```

The server will start on `http://localhost:8000`

## Your First API Call

### Using curl

```bash
curl -X POST "http://localhost:8000/api/v1/calculate" \
  -H "Content-Type: application/json" \
  -d '{
    "location": {"latitude": 41.2042, "longitude": -101.6353},
    "crop_id": "4",
    "input_level": "L"
  }'
```

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/calculate",
    json={
        "location": {"latitude": 41.2042, "longitude": -101.6353},
        "crop_id": "4",  # Maize
        "input_level": "L"  # Low input
    }
)

result = response.json()
print(f"Soil Rating: {result['soil_quality_indices']['SR']}")
```

## Explore the API

### Interactive Documentation

Open your browser to:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Try the API directly from the browser!

### List Available Crops

```bash
curl http://localhost:8000/api/v1/crops
```

### Check API Health

```bash
curl http://localhost:8000/health
```

## Run Examples

We've included comprehensive examples:

```bash
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts
python -m api.examples
```

This will run 7 example scenarios demonstrating all API features.

## Next Steps

1. **Read the Full Documentation**: See `api/README.md`
2. **Try with Your Data**: Add user soil data to requests
3. **Test Different Crops**: Use `/api/v1/crops` to see all options
4. **Run Tests**: `pytest api/test_api.py -v`

## Common Issues

### Port Already in Use

If port 8000 is already in use:

```bash
python run_api.py --port 8080
```

### Import Errors

Make sure you're in the correct directory:

```bash
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts
python run_api.py
```

### SSURGO Data Not Available

Some locations (oceans, non-US) don't have SSURGO data. Try a location in the continental US:

```python
# Nebraska (has SSURGO data)
{"latitude": 41.2042, "longitude": -101.6353}

# Iowa (has SSURGO data)
{"latitude": 42.0308, "longitude": -93.6319}
```

## API Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/calculate` | POST | Calculate soil quality indices |
| `/api/v1/crops` | GET | List available crops |
| `/health` | GET | Check API health |
| `/docs` | GET | Interactive API documentation |

## Example Request/Response

**Request:**
```json
{
  "location": {"latitude": 41.2042, "longitude": -101.6353},
  "crop_id": "4",
  "input_level": "L"
}
```

**Response:**
```json
{
  "status": "success",
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
  "crop_info": {
    "crop_id": "4",
    "crop_name": "Maize"
  },
  "data_sources": {
    "ssurgo_used": true,
    "ssurgo_component": "Holdrege silt loam"
  }
}
```

## Support

- **Documentation**: `/api/v1/docs`
- **GitHub**: https://github.com/jjmaynard/GAEZ-Hyperlocalization
- **Issues**: https://github.com/jjmaynard/GAEZ-Hyperlocalization/issues

Happy soil quality assessment! 🌱
