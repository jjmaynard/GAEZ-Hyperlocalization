# Why SQ3 and SQ7 Return NaN - Explanation

## Problem Summary

In the Jupyter notebook example (`SSURGO_GAEZ_Calc.ipynb`), **SQ3** (Rooting Conditions) and **SQ7** (Workability) return `NaN` instead of numeric scores. This occurs due to **missing data** in critical SSURGO fields.

---

## Root Cause Analysis

### Missing Data Fields

Both SQ3 and SQ7 require the following soil properties:

| Field | Description | Location in Code |
|-------|-------------|------------------|
| **`rd`** | Restrictive depth (cm) | `GAEZ_SQI_functions.py:353, 644` |
| **`fragvol`** | Coarse fragment volume (%) | `GAEZ_SQI_functions.py:404, 683` |

When these values are **NaN** (not available) in the SSURGO data, the calculations fail.

---

## How NaN Propagates

### Step-by-Step Breakdown

#### In `calculate_SQ3()`:

```python
# Line 353: Get restrictive depth from data
rd = data['rd'].iloc[0]  # If rd is NaN...

# Line 355: Calculate rd score using constraint curve
sq3_rd_score = constraint_curve(rd, sq3_rd_req[['score', 'property_value']])
# → constraint_curve(NaN, ...) returns NaN

# Line 404: Get coarse fragment volume for each layer
cf = layer['fragvol']  # If fragvol is NaN...

# Line 406: Calculate cf score
sq3_cf_score = constraint_curve(cf, sq3_cf_req[['score', 'property_value']])
# → constraint_curve(NaN, ...) returns NaN

# Line 426: Final score calculation
SQ3_scores.append(sq3_rd_score * (np.mean([low_val, high_mean]) / 100))
# → If sq3_rd_score is NaN, entire expression becomes NaN

# Line 432: Sum weighted scores
return np.sum([score * weight for score, weight in zip(SQ3_scores, wts)])
# → If any score is NaN, final result is NaN
```

#### In `calculate_SQ7()`:

```python
# Line 644: Get restrictive depth
rd = data['rd'].iloc[0]  # If rd is NaN...

# Line 646: Calculate rd score
rd_score = constraint_curve(rd, rd_req[['score', 'property_value']])
# → Returns NaN

# Line 683: Get coarse fragments
cf = layer['fragvol']  # If fragvol is NaN...

# Line 685: Calculate cf score
cf_score = constraint_curve(cf, cf_req[['score', 'property_value']])
# → Returns NaN

# Line 688-691: Include rd_score and cf_score in score dictionary
score_dict = {
    'rd': rd_score,  # NaN!
    'cf': cf_score,  # NaN!
    # ... other scores
}

# Line 695-696: Calculate mean of scores
low_val = score_df.iloc[min_idx, 0]  # Could be NaN
high_mean = score_df.drop(score_df.index[min_idx]).mean().values[0]  # NaN propagates

# Result: Final SQ7 score becomes NaN
```

---

## Why `constraint_curve()` Returns NaN

The `constraint_curve()` function doesn't explicitly handle NaN inputs:

```python
def constraint_curve(x, data, sort_data=True):
    # ...
    x_arr = np.atleast_1d(x).astype(float)  # NaN → NaN

    result = np.empty_like(x_arr)

    # NaN comparisons always return False
    result[x_arr < lower_prop] = lower_score      # NaN < value → False
    result[x_arr > upper_prop] = upper_score      # NaN > value → False
    in_range = (x_arr >= lower_prop) & (x_arr <= upper_prop)  # False

    # NaN doesn't match any condition, result[NaN_position] remains uninitialized or NaN
    return result.item() if np.isscalar(x) else result
```

---

## Example Data from Notebook

For component `cokey='25328476'`:

```
       rd  fragvol  vertic  gelic
401   NaN      NaN       0      0
402   NaN      NaN       0      0
403   NaN      NaN       0      0
404   NaN      NaN       0      0
```

**Problem**: Both `rd` and `fragvol` are `NaN` for all horizons!

---

## Why These Fields Are Missing

### Restrictive Depth (`rd`)

From SSURGO table `CORESTRICTIONS`:
- Only populated when a **restrictive layer exists** (bedrock, hardpan, etc.)
- If soil has **no restriction** within 200 cm, `rd` = `NaN`
- This is common for deep, well-developed soils

### Coarse Fragment Volume (`fragvol`)

From SSURGO table `CHFRAGS`:
- Only populated when **coarse fragments are present**
- If horizons have **negligible rock fragments** (< 1%), `fragvol` = `NaN`
- This is normal for fine-textured alluvial or loess soils

---

## Solutions

### Option 1: Impute Default Values (Recommended)

Treat missing values as "no limitation":

```python
# Before calling calculate_SQ3/SQ7:
data['rd'] = data['rd'].fillna(200)      # No restriction = 200 cm depth
data['fragvol'] = data['fragvol'].fillna(0)  # No fragments = 0%
```

### Option 2: Modify `constraint_curve()` to Handle NaN

Add NaN handling logic:

```python
def constraint_curve(x, data, sort_data=True):
    # ... existing code ...

    x_arr = np.atleast_1d(x).astype(float)

    # Handle NaN: assume no constraint (return max score)
    nan_mask = np.isnan(x_arr)

    result = np.empty_like(x_arr)
    result[nan_mask] = upper_score  # Assign best score for NaN

    # ... rest of logic for non-NaN values
```

### Option 3: Modify SQ3/SQ7 Functions

Add default handling at the source:

```python
# In calculate_SQ3() at line 353:
rd = data['rd'].iloc[0]
if pd.isna(rd):
    rd = 200  # Default: no restriction

# At line 404:
cf = layer['fragvol']
if pd.isna(cf):
    cf = 0  # Default: no fragments
```

---

## Impact on Other SQIs

| SQI | Uses `rd`? | Uses `fragvol`? | Affected by NaN? |
|-----|-----------|----------------|------------------|
| SQ1 | No | No | ✅ Works |
| SQ2 | No | No | ✅ Works |
| **SQ3** | **Yes** | **Yes** | ❌ **Returns NaN** |
| SQ4 | No | No | ✅ Works |
| SQ5 | No | No | ✅ Works |
| SQ6 | No | No | ✅ Works |
| **SQ7** | **Yes** | **Yes** | ❌ **Returns NaN** |

---

## Recommended Fix

**Add this preprocessing step before calculating SQIs:**

```python
# In GAEZ_SQI_functions.py, at the start of gaez_sqi_ratings():

def gaez_sqi_ratings(map_data, CROP_ID, inputLevel, depthWt_type=1,
                     plot_data=None, site_data=None, lab_data=None):
    """..."""

    # Integrate user data
    map_data = GAEZ_soil_data_processing.process_plot_data(plot_data, map_data)
    map_data = GAEZ_soil_data_processing.process_site_data(site_data, map_data)
    map_data = GAEZ_soil_data_processing.process_lab_data(lab_data, map_data)

    # FIX: Handle missing values with sensible defaults
    map_data['rd'] = map_data['rd'].fillna(200)      # No restriction
    map_data['fragvol'] = map_data['fragvol'].fillna(0)  # No fragments

    # ... rest of function
```

This ensures:
- Missing `rd` → treated as **no rooting restriction** (200 cm)
- Missing `fragvol` → treated as **no coarse fragments** (0%)
- SQ3 and SQ7 calculate properly
- No loss of soil suitability information

---

## Verification

After applying the fix, expected output:

```python
# Before:
SQ3: NaN
SQ7: NaN

# After:
SQ3: ~95-100 (no physical restrictions)
SQ7: ~95-100 (good workability)
```

This makes sense because the soil in the example (well-drained loamy sand) has:
- No restrictive layers
- No coarse fragments
- Deep rooting potential
- Good workability

---

## Summary

**Why NaN occurs:**
1. SSURGO leaves `rd` and `fragvol` as NaN when no restrictions/fragments exist
2. `constraint_curve()` doesn't handle NaN inputs
3. NaN propagates through arithmetic operations in SQ3/SQ7

**Best solution:**
- Impute defaults: `rd=200cm` (no restriction), `fragvol=0%` (no fragments)
- Apply at the start of `gaez_sqi_ratings()` function
- Maintains consistency with GAEZ methodology (absence of constraint = high score)
