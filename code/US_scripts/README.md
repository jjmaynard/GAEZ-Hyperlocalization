# GAEZ-US Scripts Documentation

This folder contains a Python implementation of the **GAEZ (Global Agro-Ecological Zones) methodology** adapted for **US SSURGO (Soil Survey Geographic Database)** soil data. The system calculates soil quality indices and suitability ratings for agricultural crops.

## Overview

The codebase implements the FAO GAEZ v4 framework to assess soil suitability for different crops using seven Soil Quality Indices (SQI1-SQI7) that evaluate different soil constraints.

## Core Files

### 1. `GAEZ_SQI_functions.py` - Soil Quality Index Calculations

Main module containing all SQI calculation functions.

#### Key Functions

- **`constraint_curve()`**: Interpolates constraint scores using PCHIP (monotonic) or linear interpolation
- **`cumulative_weight()`**: Calculates depth weights using normalized exponential decay curves
- **`calculate_depth_weights()`**: Computes normalized depth weights for soil profiles based on rooting depth class
  - 1 = Shallow rooting
  - 2 = Moderate rooting
  - 3 = Deep rooting
  - 4 = Very deep rooting

#### Seven SQI Calculators

| Function | SQI | Description | Key Properties |
|----------|-----|-------------|----------------|
| `calculate_SQ1()` | SQ1 | **Nutrient availability** (low input) | Organic carbon, pH, texture, total exchangeable bases |
| `calculate_SQ2()` | SQ2 | **Nutrient retention** (high input) | Base saturation, CEC (soil & clay), pH, texture |
| `calculate_SQ3()` | SQ3 | **Rooting conditions** | Root depth, texture, coarse fragments, bulk density, vertic/gelic properties, phases |
| `calculate_SQ4()` | SQ4 | **Oxygen availability** | Drainage, surface water retention, impermeable layers, phases |
| `calculate_SQ5()` | SQ5 | **Salinity/sodicity** | Electrical conductivity (EC), exchangeable sodium percentage (ESP), phases |
| `calculate_SQ6()` | SQ6 | **Calcium carbonate/gypsum** | CaCO3 and gypsum content, phases |
| `calculate_SQ7()` | SQ7 | **Workability** | Rooting depth, texture, coarse fragments, bulk density, phases |

#### Main Entry Point

**`gaez_sqi_ratings()`**: Orchestrates the entire workflow
- Processes user data
- Loads crop requirements
- Calculates all SQIs
- Returns final soil rating (SR)

#### Scoring Logic

- Uses "most limiting factor" approach - combines minimum score with mean of remaining scores
- Depth-weighted aggregation across soil horizons
- Final rating scale:
  - **S0**: No constraint (100%)
  - **S1**: Slight constraint (90%)
  - **S2**: Moderate constraint (70%)
  - **S3**: Severe constraint (50%)
  - **S4**: Very severe constraint (30%)
  - **N**: Not suitable (<10%)

---

### 2. `GAEZ_crop_req.py` - Crop Requirement Data Access

Retrieves crop-specific soil requirement thresholds.

#### Functions

- **`getGAEZ_requirements()`**: Database version (PostgreSQL)
- **`getGAEZ_requirements_csv()`**: CSV file version
- **`getGAEZ_requirements_source()`**: Unified interface supporting both sources

#### Requirement Types

| Type | Description |
|------|-------------|
| `profile` | Constraint curves for soil properties (pH, OC, EC, ESP, etc.) |
| `texture` | Texture class scores |
| `terrain` | Slope class ratings |
| `phase` | Phase-based constraints (stony, saline, etc.) |
| `drainage` | Drainage class scores by particle size class |

#### Input Levels

| Level | Description |
|-------|-------------|
| **L (Low)** | Subsistence farming, minimal inputs |
| **I (Intermediate)** | Moderate inputs |
| **H (High)** | Commercial farming, high inputs |

---

### 3. `GAEZ_SSURGO_data.py` - SSURGO Data Retrieval & Processing

Interfaces with USDA SSURGO database.

#### Key Functions

- **`mukey_wcs()`**: Fetches SSURGO raster data via Web Coverage Service (WCS) for an area of interest
- **`prepare_AEA_AOI()`**: Transforms AOI to Albers Equal Area projection (EPSG:5070)
- **`ssurgo_gaez_data()`**: Queries Soil Data Access (SDA) API and extracts horizon-level properties
- **`sda_return()`**: Executes SQL queries against USDA Soil Data Mart

#### Data Processing

- Joins multiple SSURGO tables (COMPONENT, CHORIZON, CHFRAGS, CORESTRICTIONS, etc.)
- Derives properties:
  - Texture class from sand/silt/clay percentages
  - Bulk density using Saxton & Rawls (2006) pedotransfer equations
  - ESP from SAR using Richards (1954) formula
  - Base saturation from CEC and TEB
  - CEC/clay ratio
- Applies lookup tables for:
  - Drainage classes (1-7 scale)
  - Particle size classes (coarse/medium/fine)
  - Texture IDs (1-12)

#### Helper Functions

| Function | Purpose |
|----------|---------|
| `gettt()` | Determines USDA texture class from sand/silt/clay percentages |
| `classify_pscl()` | Classifies particle size class (coarse/medium/fine) |
| `getTXT_id()` | Maps texture name to numeric ID |
| `getTextGroup()` | Maps texture to coarse/medium/fine group |

---

### 4. `GAEZ_US_phase_calc.py` - Soil Phase Classification

Classifies SSURGO data into FAO GAEZ soil phases.

#### Main Function

**`classify_gaez_v4_phases()`**: Identifies all applicable phases for each soil component

#### 22 Phase Types Identified

##### Physical Phases
- **Stony**: Coarse fragments ≥ 35%
- **Lithic**: Bedrock within 50 cm
- **Petric**: Coarse fragments ≥ 40% within 100 cm
- **Skeletic**: Coarse fragments ≥ 40% within 50 cm
- **Rudic**: Coarse fragments ≥ 35% or boulders/cobbles/stones
- **Gravelly**: Coarse fragments ≥ 40% within 100 cm
- **Concretionary**: Coarse fragments ≥ 40% with concretions

##### Cemented Layers
- **Petrocalcic**: Cemented carbonate layer ≤ 100 cm
- **Petrogypsic**: Cemented gypsum layer ≤ 100 cm
- **Petroferric**: Indurated ironstone/ferric horizon ≤ 100 cm
- **Fragipan**: Dense, root-restricting fragipan layer
- **Duripan**: Silica-cemented duripan ≤ 100 cm
- **Placic**: Thin iron-cemented pan

##### Hydrologic Phases
- **Phreatic**: Water table ≤ 50 cm, poorly drained
- **Anthraquic**: Prolonged ponding/flooding with waterlogged conditions
- **Inundic**: Frequently or permanently inundated
- **Excessively Drained**: Drains too quickly

##### Chemical Phases
- **Saline**: EC ≥ 4 dS/m
- **Salic**: EC ≥ 15 dS/m
- **Sodic**: ESP ≥ 6% or SAR ≥ 13

##### Climate Phases
- **Vertic**: Smectitic mineralogy OR (clay ≥40%, PI ≥20, LEP ≥15%)
- **Gelic**: Pergelic/subgelic temperature class OR permafrost OR high frost action

#### Classified Indices

| Index | Description | Range |
|-------|-------------|-------|
| `phase_ids_list` | List of HWSD phase IDs | List (0 = no phase) |
| `il` | Impermeable layer depth class | 0-4 |
| `swr` | Soil water regime class | 0-4 |
| `roots` | Rooting limitation class | 0-6 |
| `vertic` | Vertic properties flag | 0/1 |
| `gelic` | Gelic properties flag | 0/1 |

---

### 5. `GAEZ_soil_data_processing.py` - User Data Integration

Allows users to override map-based data with field observations.

#### Functions

| Function | Purpose |
|----------|---------|
| `process_plot_data()` | Integrates field-observed soil horizons, texture, coarse fragments |
| `process_site_data()` | Updates site coordinates, bedrock depth, slope from field data |
| `process_lab_data()` | Incorporates laboratory measurements (pH, OC, CEC, EC, ESP, etc.) |

#### Processing Steps

1. Cleans and validates user data
2. Interpolates properties to 1-cm depth increments (0-200 cm)
3. Aggregates to standard depth intervals
4. Merges with map data, prioritizing user observations
5. Recalculates derived properties (texture class, drainage)

---

### 6. `gaez_config.py` - Configuration File

Central configuration for file paths and parameters.

#### Contents

```python
# CSV file paths for crop requirement lookup tables
profile_req_url = "path/to/GAEZ_profile_req_rf.csv"
phase_req_url = "path/to/GAEZ_phase_req_rf.csv"
drainage_req_url = "path/to/GAEZ_drainage_req_rf.csv"
texture_req_url = "path/to/GAEZ_text_req_rf.csv"
terrain_req_url = "path/to/GAEZ_terrain_req_rf.csv"

# Horizon depth column names
class hz_names:
    top_col_name = 'hzdept_r'
    bottom_col_name = 'hzdepb_r'
```

---

### 7. `surgo_data.py` - Data Exploration Script

Exploratory data analysis script for understanding SSURGO structure.

#### Analyses

- Loads gSSURGO geodatabase layers
- Maps SSURGO attributes to GAEZ requirements
- Investigates data completeness and missingness
- Documents derived property calculations:
  - CEC/clay from soil CEC and clay fraction
  - Base saturation from CEC and TEB
  - ESP from SAR using Richards (1954) equation
- Filters datasets for complete profiles with continuous depth coverage

**Purpose**: Documentation and validation - not used in production workflow

---

### 8. `SSURGO_GAEZ_Calc.ipynb` - Jupyter Notebook Demo

End-to-end workflow demonstration.

#### Workflow

1. Define area of interest (AOI) as WKT polygon
2. Fetch SSURGO mukey raster via WCS
3. Extract unique map unit keys
4. Query SSURGO data from SDA API
5. Classify soil phases
6. Load crop requirements
7. Calculate all SQI scores (SQ1-SQ7)
8. Compute final soil rating (SR)

#### Example Output

```python
CROP_ID='4' (Maize), Input Level='L' (Low)
SQ1: 20.04 (nutrient availability - severe constraint)
SQ2: 94.55 (nutrient retention - slight constraint)
SQ3: 97.82 (rooting conditions - no constraint)
SQ4: 100.0 (oxygen availability - no constraint)
SQ5: 100.0 (salinity - no constraint)
SQ6: 100.0 (gypsum/lime - no constraint)
SQ7: 98.45 (workability - no constraint)
SR: 19.17 (final soil rating - N: Not suitable for low-input maize)
```

**Note**: SQ3 and SQ7 previously returned `NaN` due to missing `rd` (restrictive depth) and `fragvol` (coarse fragments) data. The fix implemented in `GAEZ_SQI_functions.py:774-780` now imputes defaults (rd=200cm, fragvol=0%) for missing values, treating absence of restrictions as optimal conditions.

**Interpretation**:
- The low SR (19.17) is driven by **SQ1 (20.04)** - severe nutrient deficiency
- Physical conditions are excellent (SQ3, SQ4, SQ7 near 100)
- This sandy loam soil would benefit from fertilizer inputs (switch to Intermediate/High input level)

---

## System Architecture

```
User Input (AOI, Crop, Input Level)
    ↓
GAEZ_SSURGO_data → Fetch SSURGO data
    ↓
GAEZ_US_phase_calc → Classify phases
    ↓
GAEZ_soil_data_processing → Merge user data (optional)
    ↓
GAEZ_crop_req → Load crop requirements
    ↓
GAEZ_SQI_functions → Calculate SQ1-SQ7 → Final SR
```

## Key Dependencies

```python
# Core data manipulation
pandas
numpy

# Geospatial operations
geopandas
shapely
rasterio
pyproj

# Scientific computing
scipy  # Interpolation (PCHIP)

# Web services
requests  # API calls to USDA SDA
```

## Data Sources

| Source | Description | URL |
|--------|-------------|-----|
| **SSURGO** | USDA Soil Survey Geographic Database | - |
| **GAEZ v4** | FAO crop requirement tables | - |
| **WCS Service** | SSURGO raster data web service | http://casoilresource.lawr.ucdavis.edu/ |
| **SDA API** | Soil Data Access tabular service | https://sdmdataaccess.sc.egov.usda.gov/ |

## Usage Example

```python
import GAEZ_SQI_functions
import GAEZ_crop_req
import GAEZ_SSURGO_data
import GAEZ_US_phase_calc

# 1. Fetch SSURGO data for AOI
aoi = gpd.GeoDataFrame({'geometry': [aoi_polygon]}, crs="EPSG:4326")
raster = GAEZ_SSURGO_data.mukey_wcs(aoi, db='gssurgo', res=30)
mukey_list = np.unique(raster.read(1))

# 2. Get SSURGO data
ssurgo_df = GAEZ_SSURGO_data.ssurgo_gaez_data(mukey_list)

# 3. Classify phases
phase_df = GAEZ_US_phase_calc.classify_gaez_v4_phases(ssurgo_df)

# 4. Calculate soil ratings
map_data = phase_df[phase_df['cokey'] == target_cokey]
gaez_scores = GAEZ_SQI_functions.gaez_sqi_ratings(
    map_data,
    CROP_ID='4',  # Maize
    inputLevel='L',  # Low input
    depthWt_type=3  # Deep rooting
)

print(gaez_scores)
```

## References

1. **FAO GAEZ v4 Documentation**: https://openknowledge.fao.org/items/039f7ec9-98af-49e1-8d24-850122c69bef
2. **SSURGO Metadata Tables and Columns**: https://www.nrcs.usda.gov/sites/default/files/2022-08/SSURGO-Metadata-Tables-and-Columns-Report.pdf
3. **Saxton & Rawls (2006)**: Soil water characteristic estimates by texture and organic matter
4. **Richards (1954)**: Diagnosis and Improvement of Saline and Alkali Soils

---

## Troubleshooting

### SQ3 and SQ7 Return NaN

**Problem**: In earlier versions, SQ3 (Rooting Conditions) and SQ7 (Workability) would return `NaN` for soils with missing data.

**Cause**: SSURGO leaves `rd` (restrictive depth) and `fragvol` (coarse fragments) as `NaN` when no restrictions or fragments exist.

**Solution**: ✅ Fixed in `GAEZ_SQI_functions.py:774-780`

The system now automatically imputes default values:
- `rd = 200 cm` when missing (assumes deep, unrestricted soil)
- `fragvol = 0%` when missing (assumes no coarse fragments)

For detailed explanation, see `NaN_Issues_Explanation.md`.

### Missing Crop Requirement Data

Ensure CSV file paths in `gaez_config.py` point to valid GAEZ requirement tables:
- `GAEZ_profile_req_rf.csv`
- `GAEZ_phase_req_rf.csv`
- `GAEZ_drainage_req_rf.csv`
- `GAEZ_text_req_rf.csv`
- `GAEZ_terrain_req_rf.csv`

---

## Notes

This system provides a comprehensive framework for evaluating agricultural land suitability using standardized GAEZ methodology with high-resolution US soil data.

### Key Features
- Automated SSURGO data retrieval via WCS/SDA API
- Comprehensive soil phase classification (22 phase types)
- Seven soil quality indices (SQI1-SQI7) for holistic assessment
- Handles missing data gracefully with scientifically-sound defaults
- Supports user field/lab data integration to override map-based estimates
