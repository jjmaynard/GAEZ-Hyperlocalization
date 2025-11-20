"""
FAO GAEZ SQ5: EXCESS SALTS - DETAILED DESCRIPTION
==================================================

Based on the FAO Global Agro-Ecological Zones (GAEZ) methodology and the 
Harmonized World Soil Database (HWSD) framework.

Data Citation:
Fischer, G., F. Nachtergaele, S. Prieler, H.T. van Velthuizen, L. Verelst, D. Wiberg, 2008. 
Global Agro-ecological Zones Assessment for Agriculture (GAEZ 2008). 
IIASA, Laxenburg, Austria and FAO, Rome, Italy.
"""

# ============================================================================
# OVERVIEW
# ============================================================================

"""
SQ5: EXCESS SALTS

SQ5 represents the presence and concentration of soluble salts and exchangeable 
sodium in soil that can adversely affect plant growth, soil structure, and 
agricultural productivity. This soil quality indicator assesses salinity (total 
soluble salts) and sodicity (excess exchangeable sodium), both of which create 
severe limitations for crop production.

POSITION IN GAEZ FRAMEWORK:
SQ5 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability
- SQ2: Nutrient retention capacity
- SQ3: Rooting conditions
- SQ4: Oxygen availability to roots
- SQ5: Excess salts (focus of this document)
- SQ6: Toxicity
- SQ7: Workability/field management constraints
"""

# ============================================================================
# CONCEPTUAL BASIS
# ============================================================================

"""
FUNDAMENTAL CONCEPT:

Excess salts in soil create multiple problems for plant growth through:

SALINITY (Total Soluble Salts):
1. Osmotic stress - reduces water availability to plants
2. Ion toxicity - specific ions harm plants at high concentrations
3. Nutritional imbalances - interferes with nutrient uptake
4. Reduced soil microbial activity
5. Germination and seedling establishment problems

SODICITY (Excess Exchangeable Sodium):
1. Soil structure degradation - dispersion of clay particles
2. Reduced permeability and infiltration
3. Surface crusting and sealing
4. Poor aeration when wet
5. Extreme hardness when dry
6. Difficult seedbed preparation
7. Sodium toxicity to plants

Sources of soil salts:
- Natural: weathering of rocks, seawater intrusion, fossil salts
- Irrigation: salts in irrigation water accumulate over time
- Fertilizers: residual salts from fertilizer use
- Poor drainage: prevents leaching of salts
- Capillary rise: brings salts from saline water tables
- Marine influences: coastal areas, tidal flooding

AGRICULTURAL RELEVANCE:

Global extent:
- ~1 billion hectares affected by salinity/sodicity worldwide
- ~20-30% of irrigated lands affected
- Major agricultural constraint in arid/semi-arid regions
- Increasing problem with irrigation expansion

Crop impacts:
- Reduced germination and stand establishment
- Stunted growth and reduced vigor
- Lower yields (10-100% reduction)
- Reduced crop quality
- Complete crop failure in severe cases
- Limited crop selection

Economic impacts:
- Yield losses worth billions annually
- Land abandonment in severe cases
- High reclamation costs
- Reduced land values
- Increased input costs for tolerant crops

Management challenges:
- Difficult and expensive to remediate
- Requires good quality water for leaching
- Drainage essential
- Long-term process
- Can worsen with poor management
- Prevention far easier than cure

Environmental concerns:
- Salt mobilization contaminates water
- Drainage water disposal problems
- Wetland salinization
- Loss of agricultural productivity
- Desertification in extreme cases
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ5 DIAGNOSTIC CHARACTERISTICS:

The assessment of excess salts focuses on measurements and indicators of both 
salinity and sodicity throughout the soil profile.

----------------------
SALINITY ASSESSMENT
----------------------

1. ELECTRICAL CONDUCTIVITY (EC)
   
   Definition: Measure of the ability of soil solution to conduct electrical 
   current, directly related to concentration of dissolved salts. Units: 
   dS/m (deciSiemens per meter) or mmhos/cm (equivalent).
   
   Measurement methods:
   
   ECe (EC of saturation extract):
   - Standard reference method
   - Soil saturated with distilled water
   - Extract obtained by suction
   - Most commonly used and reported
   
   EC1:5 or EC1:2 (soil:water ratio):
   - Soil mixed with water at ratio
   - Simpler and faster than saturation
   - Must convert to ECe for interpretation
   - Used in many surveys
   
   ECa (apparent EC):
   - Field measurement with sensors
   - Electromagnetic induction or resistivity
   - Rapid spatial mapping
   - Affected by moisture and texture
   
   Salinity classification by ECe:
   
   Non-saline (0-2 dS/m):
   - Negligible salt content
   - No effects on most crops
   - Optimal conditions
   
   Very slightly saline (2-4 dS/m):
   - Minimal effects
   - Sensitive crops may be affected
   - Most crops unaffected
   
   Slightly saline (4-8 dS/m):
   - Moderate salt stress
   - Many crops show yield reduction
   - Sensitive crops severely affected
   - Management needed
   
   Moderately saline (8-16 dS/m):
   - Significant salt stress
   - Only moderately tolerant crops productive
   - Sensitive and many moderately sensitive crops fail
   - Special management essential
   
   Strongly saline (16-32 dS/m):
   - Severe salt stress
   - Only tolerant crops survive
   - Major yield reductions even for tolerant crops
   - Reclamation often needed
   
   Very strongly saline (>32 dS/m):
   - Extreme salt stress
   - Very few crops possible
   - Even salt-tolerant crops severely affected
   - Generally unsuitable for agriculture
   - Reclamation very difficult and expensive
   
   Salt composition matters:
   - Chloride salts most common and damaging
   - Sulfate salts less harmful
   - Carbonate/bicarbonate salts affect pH
   - Sodium salts cause both salinity and sodicity
   
   Profile distribution:
   - Surface accumulation common (evaporation)
   - Subsurface accumulation at water table depth
   - Can vary greatly with depth
   - Leaching patterns affect distribution


2. TOTAL DISSOLVED SOLIDS (TDS)
   
   Definition: Total concentration of dissolved salts in soil solution, 
   expressed in mg/L or ppm.
   
   Relationship to EC:
   - TDS (mg/L) ≈ EC (dS/m) × 640 (approximate)
   - Varies with salt composition
   - EC preferred for practical use
   
   Typical relationships:
   - Fresh water: <500 mg/L TDS
   - Slightly saline: 500-1,500 mg/L
   - Moderately saline: 1,500-5,000 mg/L
   - Highly saline: 5,000-15,000 mg/L
   - Very highly saline: >15,000 mg/L
   - Seawater: ~35,000 mg/L


3. SPECIFIC IONS
   
   Major cations (positively charged):
   - Sodium (Na+): Most problematic for sodicity
   - Calcium (Ca2+): Beneficial, ameliorates sodium
   - Magnesium (Mg2+): Less harmful than sodium
   - Potassium (K+): Generally not excessive
   
   Major anions (negatively charged):
   - Chloride (Cl-): Very toxic to many crops
   - Sulfate (SO4²-): Less toxic than chloride
   - Bicarbonate (HCO3-): Affects pH and calcium
   - Carbonate (CO3²-): Precipitates calcium
   
   Toxic ions at high concentrations:
   
   Chloride toxicity:
   - Extremely toxic to many fruit trees
   - Accumulates in leaves
   - Causes leaf burn and defoliation
   - Threshold varies by crop (0.5-10 meq/L)
   
   Sodium toxicity:
   - Direct toxicity to plants
   - Indirect through sodicity effects
   - Affects many crops at >5-10 meq/L
   
   Boron:
   - Essential micronutrient but toxic at excess
   - Very narrow safe range
   - Toxic at >1-2 mg/L for sensitive crops
   - Can be natural or from irrigation water


----------------------
SODICITY ASSESSMENT
----------------------

1. EXCHANGEABLE SODIUM PERCENTAGE (ESP)
   
   Definition: The percentage of cation exchange capacity (CEC) occupied by 
   sodium ions.
   
   Formula: ESP = (Exchangeable Na / CEC) × 100
   
   Sodicity classification by ESP:
   
   Non-sodic (ESP <6%):
   - Negligible sodium effects
   - No structural problems
   - Normal soil properties
   
   Slightly sodic (ESP 6-10%):
   - Minor sodium effects
   - Slight structural degradation
   - Beginning of dispersion
   - May have minor problems
   
   Moderately sodic (ESP 10-15%):
   - Moderate sodium effects
   - Noticeable structural problems
   - Clay dispersion occurring
   - Reduced permeability
   - Management needed
   
   Strongly sodic (ESP 15-25%):
   - Severe sodium effects
   - Major structural degradation
   - Extensive clay dispersion
   - Very poor permeability
   - Surface crusting
   - Special management essential
   
   Very strongly sodic (ESP >25%):
   - Extreme sodium effects
   - Severe structural collapse
   - Nearly impermeable when wet
   - Extremely hard when dry
   - Very difficult to manage
   - Reclamation very challenging
   
   Mechanisms of sodium damage:
   - Sodium disperses clay particles
   - Clays clog pores
   - Infiltration rate drops
   - Surface sealing occurs
   - Erosion increases
   - Compaction worsens


2. SODIUM ADSORPTION RATIO (SAR)
   
   Definition: Ratio of sodium to calcium plus magnesium in soil solution, 
   predicting sodicity development.
   
   Formula: SAR = [Na+] / √([Ca2+] + [Mg2+])/2
   (Concentrations in meq/L)
   
   SAR interpretation:
   
   Low (SAR <10):
   - Low sodicity hazard
   - Minimal structural problems
   - Safe for most soils
   
   Medium (SAR 10-18):
   - Moderate sodicity hazard
   - Structural problems possible
   - Management needed on sensitive soils
   
   High (SAR 18-26):
   - High sodicity hazard
   - Structural problems likely
   - Special management needed
   
   Very high (SAR >26):
   - Very high sodicity hazard
   - Severe structural problems expected
   - Intensive management essential
   
   Relationship ESP-SAR (approximate):
   - ESP ≈ 100 × (-0.0126 + 0.01475 × SAR)
   - Allows prediction of ESP from solution analysis
   - SAR easier to measure in irrigation water


3. pH EFFECTS IN SODIC SOILS
   
   Sodic soils often have high pH:
   
   Mechanisms:
   - Sodium carbonate and bicarbonate accumulation
   - Hydrolysis of sodium on exchange sites
   - Generates hydroxyl ions (OH-)
   - pH can exceed 10
   
   Effects of high pH in sodic soils:
   - Amplifies sodium damage
   - Increases clay dispersion
   - Precipitates calcium (unavailable)
   - Causes micronutrient deficiencies
   - Organic matter dissolved and dispersed
   - Creates black, dispersed surface ("black alkali")
   - Extremely hostile to most plants


----------------------
PROFILE DISTRIBUTION
----------------------

Salts and sodium distribution patterns:

1. SURFACE ACCUMULATION
   - Evaporation concentrates salts at surface
   - White crusts visible
   - Worst for germination
   - Common in arid climates
   - Intensified by irrigation

2. SUBSURFACE ACCUMULATION
   - Salts leach below root zone
   - Accumulate at wetting front or water table
   - Less immediately visible
   - Can affect deep-rooted crops
   - Rises with capillary action

3. UNIFORM DISTRIBUTION
   - Throughout profile
   - Indicates saline parent material or groundwater
   - Severe limitation

4. LAYERED PATTERNS
   - Salt/sodium concentrated in specific horizons
   - Often at textural discontinuities
   - Variable effects depending on depth

Depth considerations:
- Surface salinity: 0-30 cm critical for annual crops
- Subsoil salinity: 30-100 cm affects deep-rooted crops
- Deep salinity: >100 cm affects trees, may rise with irrigation


----------------------
FIELD INDICATORS
----------------------

Visual indicators of salinity/sodicity:

1. WHITE SALT CRUSTS
   - Crystalline deposits on surface
   - After evaporation
   - Indicates high salinity
   - Can be sampled and tested

2. POOR OR SPOTTY CROP GROWTH
   - Bare patches in fields
   - Stunted growth in saline spots
   - Patchy patterns
   - Worse in low areas

3. DARK, GREASY APPEARANCE WHEN WET (sodic)
   - Dispersed clay and organic matter
   - "Black alkali" appearance
   - Indicates high sodium and pH

4. HARD, CLODDY STRUCTURE WHEN DRY (sodic)
   - Difficult to break clods
   - Poor tilth
   - Indicates dispersion

5. SURFACE CRUSTING (sodic)
   - Hard seal forms after rain
   - Prevents emergence
   - Indicates sodium dispersion

6. PUDDLING AND POOR DRAINAGE (sodic)
   - Water stands on surface
   - Very slow infiltration
   - Slippery when wet

7. VEGETATION INDICATORS
   - Salt-tolerant weeds (saltgrass, pickleweed)
   - Absence of sensitive plants
   - Chlorosis and tip burn
   - Reduced vigor
"""

# ============================================================================
# RATING SYSTEM
# ============================================================================

"""
SQ5 RATING SCALE:

Soils are rated on a 0-100 scale based on absence of salt problems:

0-100 SCALE INTERPRETATION:
- 80-100: Very High - No salt problems
- 60-79:  High - Minor salt problems
- 40-59:  Medium - Moderate salt problems
- 20-39:  Low - Severe salt problems
- 0-19:   Very Low - Extreme salt problems

Note: Rating decreases as salinity/sodicity increases (opposite of first 4 SQs)


VERY HIGH (80-100): NO SALT PROBLEMS

Soil characteristics:
- Non-saline (ECe <2 dS/m)
- Non-sodic (ESP <6%, SAR <10)
- No visible salt accumulation
- Normal pH (not affected by sodium)
- Good soil structure
- Normal permeability

Crop suitability:
- All crops suitable regarding salinity
- No salt-related limitations
- Optimal growing conditions
- No special management needed

Management:
- Standard practices sufficient
- Monitor irrigation water quality
- Maintain adequate drainage
- Prevent salt accumulation


HIGH (60-79): MINOR SALT PROBLEMS

Soil characteristics:
- Very slightly saline (ECe 2-4 dS/m), or
- Very slightly sodic (ESP 6-10%, SAR 10-13), or
- Minor localized salt accumulation
- pH slightly elevated (7.5-8.5)
- Structure beginning to show effects
- Permeability slightly reduced

Crop impacts:
- Most crops perform well
- Very sensitive crops may show slight stress
- Minor yield reductions (<10%)
- Germination slightly affected
- Some crops show salt accumulation in leaves

Suitable crops:
- Most field crops
- Most vegetables (with care)
- Most tree fruits
- Wide crop selection

Management needs:
- Monitor salt levels
- Use moderate leaching fraction
- Select adapted varieties
- Good water management
- Maintain drainage
- Apply gypsum if sodic


MEDIUM (40-59): MODERATE SALT PROBLEMS

Soil characteristics:
- Moderately saline (ECe 4-8 dS/m), or
- Moderately sodic (ESP 10-15%, SAR 13-18), or
- Both slight salinity and sodicity, or
- Visible salt accumulation in places
- pH elevated (8.0-9.0)
- Structure degraded
- Permeability reduced
- Crusting may occur

Crop impacts:
- Sensitive crops fail or severely reduced
- Moderately sensitive crops show stress
- Yield reductions 10-50%
- Germination problems
- Plant toxicity symptoms
- Reduced stand establishment

Suitable crops:
- Moderately tolerant crops only
- Barley, cotton, sugar beet, date palm
- Some forages (tall wheatgrass, bermudagrass)
- Very limited vegetable options
- Special varieties needed

Management requirements:
- Salt-tolerant crops essential
- Leaching requirement significant (15-30%)
- Drainage critical
- Gypsum application if sodic
- Specialized practices needed
- Pre-plant irrigation to leach salts
- Avoid salt-sensitive crops
- May need beds or furrows for drainage


LOW (20-39): SEVERE SALT PROBLEMS

Soil characteristics:
- Highly saline (ECe 8-16 dS/m), or
- Highly sodic (ESP 15-25%, SAR 18-26), or
- Combined salinity and sodicity, or
- Extensive salt crusting
- High pH (8.5-10.0)
- Severe structural degradation
- Very poor permeability
- Extreme crusting and hardness

Crop impacts:
- Most crops fail
- Only tolerant crops viable
- Yield reductions 50-90%
- Very poor germination
- Severe toxicity symptoms
- Limited crop survival

Suitable crops (very limited):
- Barley (most tolerant grain)
- Date palm
- Very tolerant forages (saltgrass, Bermuda grass)
- Some halophytic species
- May need special salt-tolerant varieties

Management challenges:
- Intensive reclamation often needed
- High leaching requirements (30-50%)
- Expensive drainage systems required
- Large gypsum applications if sodic
- May need deep plowing/mixing
- Long-term reclamation process
- May not be economically viable
- Alternative uses may be better


VERY LOW (0-19): EXTREME SALT PROBLEMS

Soil characteristics:
- Very highly saline (ECe >16 dS/m), or
- Very highly sodic (ESP >25%, SAR >26), or
- Severe combined salinity and sodicity
- Thick salt crusts
- Very high pH (>9.5)
- Complete structural collapse
- Nearly impermeable
- Extreme hardness when dry
- May have black alkali conditions

Crop suitability:
- Essentially unsuitable for conventional agriculture
- Only most extreme halophytes
- Even tolerant crops severely affected
- No economic crop production without reclamation

Alternative uses:
- Salt-tolerant vegetation
- Wildlife habitat (salt marsh)
- Aquaculture (brine shrimp)
- Solar evaporation ponds
- May be irreclaimable
- Land retirement may be necessary

Reclamation challenges:
- Very expensive and time-consuming
- May take 5-10+ years
- Requires excellent drainage and water supply
- Large quantities of amendments needed
- Success uncertain
- Often not economically feasible
- Environmental disposal issues
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
APPROACH TO RATING SQ5:

The rating methodology integrates measurements of both salinity and sodicity:

1. PRIMARY RATING FACTORS:

   Salinity (ECe):
   - Single most important factor in saline soils
   - Weighted 50-70% where salinity dominant
   - Direct correlation with crop tolerance
   - Rapid impact on plants
   
   Sodicity (ESP or SAR):
   - Most important in sodic soils
   - Weighted 50-70% where sodicity dominant
   - Affects soil properties and plants
   - Long-term structural impacts
   
   When both present:
   - Multiplicative effect (worse than either alone)
   - Both factors weighted
   - Combined effects lower rating more


2. RATING FUNCTIONS:

   For salinity (based on ECe):
   
   Rating by EC level:
   - 0-2 dS/m: 90-100 (no limitation)
   - 2-4 dS/m: 70-90 (slight limitation)
   - 4-8 dS/m: 45-70 (moderate limitation)
   - 8-16 dS/m: 20-45 (severe limitation)
   - >16 dS/m: 0-20 (extreme limitation)
   
   Non-linear decrease:
   - Steeper decline at higher salinity
   - Reflects crop response curves
   - Few crops tolerate >16 dS/m
   
   For sodicity (based on ESP):
   
   Rating by ESP:
   - 0-6%: 90-100 (no limitation)
   - 6-10%: 70-90 (slight limitation)
   - 10-15%: 45-70 (moderate limitation)
   - 15-25%: 20-45 (severe limitation)
   - >25%: 0-20 (extreme limitation)
   
   Structural effects emphasized:
   - Impacts on permeability
   - Crusting and hardness
   - Management difficulty


3. PROFILE INTEGRATION:

   Depth weighting:
   - Surface (0-30 cm): 60-70% of rating
   - Subsurface (30-100 cm): 30-40% of rating
   
   Rationale:
   - Surface critical for germination
   - Most roots in upper profile
   - Deep salinity affects deep-rooted crops
   - Can rise to surface with time
   
   Profile pattern effects:
   - Uniform high salinity: worst
   - Surface accumulation: very bad for establishment
   - Subsurface accumulation: limits deep-rooted crops
   - Layered: variable effects


4. MOST LIMITING FACTOR:

   Single severe limitation dominant:
   - Very high surface salinity: caps rating at ~20
   - Extreme sodicity: caps rating at ~15
   - Both severe: rating approaches 0
   
   Multiple moderate limitations:
   - Cumulative effects
   - Combined impact worse than additive


5. MODIFIER FACTORS:

   pH in sodic soils:
   - High pH (>9) amplifies sodium effects
   - Further reduces rating
   - Indicates severe sodicity
   
   Specific ion toxicity:
   - High chloride: additional penalty
   - High boron: crop-specific penalty
   - Considered if data available
   
   Permeability effects:
   - Very low permeability worsens prognosis
   - Makes reclamation difficult
   - Reduces rating


6. CLIMATE CONSIDERATIONS:

   Arid regions:
   - Salinity more common and severe
   - Less natural leaching
   - Problem more intractable
   - Weight SQ5 more heavily
   
   Humid regions:
   - Salinity less common
   - Natural leaching helps
   - Easier to manage if occurs
   - Sodicity can still be severe
   
   Irrigation:
   - Irrigated lands at higher risk
   - Rate based on developed salinity
   - Consider irrigation water quality


7. RECLAMATION POTENTIAL:

   Affects rating in context:
   - Easy to reclaim: higher effective rating
   - Difficult to reclaim: lower effective rating
   - Irreclaimable: minimum rating
   
   Factors affecting reclamation:
   - Drainage feasibility
   - Water availability for leaching
   - Amendment needs and costs
   - Time required
   - Economic viability
"""

# ============================================================================
# CROP-SPECIFIC RESPONSES
# ============================================================================

"""
CROP TOLERANCE TO SALINITY:

Crops vary enormously in salt tolerance, typically rated by EC threshold 
(ECe at which yield reduction begins) and slope (% yield loss per unit EC).

SENSITIVE CROPS (Threshold <1.5 dS/m):

Field crops:
- Beans (1.0 dS/m)
- Carrots (1.0 dS/m)

Fruit crops:
- Strawberry (1.0 dS/m)
- Avocado (1.3 dS/m)
- Lemon (1.5 dS/m)
- Apple, pear (1.5 dS/m)

Forage crops:
- White clover (1.5 dS/m)

Vegetables:
- Radish (1.2 dS/m)
- Celery (1.8 dS/m)


MODERATELY SENSITIVE (Threshold 1.5-3.5 dS/m):

Field crops:
- Maize (1.7 dS/m)
- Rice (3.0 dS/m)
- Soybeans (5.0 dS/m but foliage sensitive)
- Broadbean (1.6 dS/m)
- Flax (1.7 dS/m)

Fruit crops:
- Orange (1.7 dS/m)
- Grapefruit (1.8 dS/m)
- Peach (1.7 dS/m)
- Apricot (1.6 dS/m)
- Grape (1.5 dS/m)
- Almond (1.5 dS/m)

Vegetables:
- Tomato (2.5 dS/m)
- Cucumber (2.5 dS/m)
- Cantaloupe (2.2 dS/m)
- Spinach (2.0 dS/m)
- Cabbage (1.8 dS/m)
- Potato (1.7 dS/m)
- Bell pepper (1.5 dS/m)
- Lettuce (1.3 dS/m)
- Onion (1.2 dS/m)


MODERATELY TOLERANT (Threshold 3.5-6.0 dS/m):

Field crops:
- Wheat (6.0 dS/m)
- Sorghum (6.8 dS/m)
- Oats (4.8 dS/m)
- Safflower (5.3 dS/m)
- Sunflower (4.8 dS/m)
- Rapeseed/canola (3.9 dS/m)
- Groundnut (3.2 dS/m)
- Sugarcane (1.7 dS/m - sensitive)

Forage crops:
- Alfalfa (2.0 dS/m)
- Clover (red, alsike) (1.5 dS/m)
- Orchard grass (1.5 dS/m)
- Fescue (tall) (3.9 dS/m)

Vegetables:
- Beet (4.0 dS/m)
- Squash (4.9 dS/m)
- Broccoli (2.8 dS/m)


TOLERANT (Threshold 6.0-10.0 dS/m):

Field crops:
- Barley (8.0 dS/m) - most tolerant grain
- Sugar beet (7.0 dS/m)
- Cotton (7.7 dS/m)

Forage crops:
- Bermudagrass (6.9 dS/m)
- Tall wheatgrass (7.5 dS/m)
- Crested wheatgrass (7.5 dS/m)

Tree crops:
- Date palm (4.0 dS/m, highly tolerant)


HIGHLY TOLERANT (Threshold >10 dS/m):

Forage crops:
- Saltgrass (Distichlis) (>10 dS/m)
- Nuttall alkali grass (>10 dS/m)
- Barley hay (18 dS/m for feed)

Halophytes (salt-loving plants):
- Salicornia (pickleweed) (>40 dS/m)
- Atriplex (saltbush) (>20 dS/m)
- Some mangrove species (>20 dS/m)


YIELD REDUCTION PATTERNS:

General response curve:
- Below threshold: minimal effect (0-10% loss)
- Above threshold: linear decline typically
- Slope varies: 5-50% per dS/m
- Sensitive crops: steep slope
- Tolerant crops: gentle slope

Example (Wheat, threshold 6.0 dS/m, slope 7.1%/dS/m):
- 6 dS/m: 100% yield
- 8 dS/m: ~86% yield
- 10 dS/m: ~71% yield
- 12 dS/m: ~57% yield
- 14 dS/m: ~43% yield

Complete failure typically at 2-3× threshold


FACTORS AFFECTING TOLERANCE:

Growth stage sensitivity:
- Germination and seedling: most sensitive
- Vegetative growth: moderately sensitive
- Reproductive: variable by crop
- Maturity: usually less sensitive

Environmental interactions:
- High temperature: increases sensitivity
- Low humidity: increases sensitivity
- High light: may increase tolerance
- Water stress: greatly increases sensitivity

Management factors:
- Leaching fraction: critical
- Water quality: determines salt load
- Fertilization: affects osmotic potential
- Variety selection: genetic differences


SODICITY TOLERANCE:

Generally less information than salinity, but principles:

Most crops sensitive to sodicity:
- Structural degradation affects all
- Poor germination universal
- Reduced stands common
- Combined salinity-sodicity worst

Relative sodicity tolerance (general):
- Rhodes grass: very tolerant
- Tall wheatgrass: tolerant
- Barley: moderately tolerant
- Most crops: sensitive

Note: Sodicity tolerance largely reflects tolerance to poor physical conditions 
rather than sodium ion toxicity per se.
"""

# ============================================================================
# MANAGEMENT STRATEGIES BY SQ5 CLASS
# ============================================================================

"""
MANAGEMENT APPROACHES FOR DIFFERENT SQ5 RATINGS:

VERY HIGH (80-100): NO SALT PROBLEMS

Management approach:
- Prevent salt accumulation
- Monitor irrigation water
- Maintain good drainage
- Standard practices

Preventive measures:
- Use good quality irrigation water (EC <0.7 dS/m)
- Ensure adequate drainage
- Apply appropriate leaching fraction
- Monitor salt buildup over time
- Avoid over-application of saline fertilizers

Advantages:
- No salt-related costs
- Full crop choice
- Normal management
- No special equipment


HIGH (60-79): MINOR SALT PROBLEMS

Management approach:
- Careful monitoring
- Minor adjustments to practices
- Maintain leaching
- Select adapted varieties

Water management:
- Apply leaching fraction: 10-15%
- Use best available water
- Avoid deficit irrigation
- Maintain uniform infiltration

Crop selection:
- Avoid most sensitive crops
- Use moderately sensitive to tolerant crops
- Select salt-tolerant varieties within crops
- Most crops still viable

Salt monitoring:
- Test soil every 2-3 years
- Watch for accumulation trends
- Monitor crop symptoms
- Adjust practices as needed

Amendments:
- Gypsum if ESP >6%
- Improve surface structure
- Enhance infiltration


MEDIUM (40-59): MODERATE SALT PROBLEMS

Management approach:
- Active salt management essential
- Significant adjustments needed
- Restricted crop selection
- May need reclamation

Water management critical:

Leaching requirements:
- 15-30% leaching fraction needed
- Extra water for salt removal
- Pre-plant leaching beneficial
- Post-harvest leaching if possible

Irrigation methods:
- Sprinkler or surface may worsen (evaporation)
- Drip reduces evaporation losses
- Subsurface drip ideal
- Avoid over-irrigation (drainage limit)

Water quality:
- Use best quality water available
- Blend waters if possible
- May need water treatment

Crop selection restricted:
- Only moderately tolerant crops viable
- Varieties within crops critical
- Barley instead of wheat
- Cotton instead of alfalfa
- Sugar beet option

Cultural practices:

Seedbed preparation:
- Pre-plant irrigation to leach surface
- Plant on beds with furrow irrigation
- Seeds on shoulder of bed (less salt)
- Higher seeding rates (compensate mortality)

Planting:
- Avoid planting into saline seedbed
- Time planting after leaching rain or irrigation
- Use transplants instead of seeds where possible

Fertility management:
- Avoid saline fertilizers (especially Cl-based)
- Use low-salt fertilizer sources
- Split applications to reduce osmotic effect
- May need higher rates (less efficient uptake)

Amendments for sodicity:

Gypsum (calcium sulfate):
- Displaces sodium with calcium
- Improves structure
- Dose: 2-10 tons/acre depending on ESP
- Work into soil
- Requires leaching to remove displaced sodium

Sulfur:
- Oxidizes to sulfuric acid
- Reacts with soil carbonates to form gypsum
- Slower acting than gypsum
- Dose: 1-5 tons/acre
- Best in calcareous sodic soils

Other amendments:
- Organic matter improves structure
- Iron sulfate (in high pH)
- Sulfuric acid (direct acidification)


LOW (20-39): SEVERE SALT PROBLEMS

Management approach:
- Intensive reclamation often required
- Very restricted crop choices
- High costs
- Long-term commitment

Reclamation process:

1. Assessment:
   - Detailed soil testing (multiple depths)
   - Determine salt type and amount
   - Evaluate drainage conditions
   - Test water supply
   - Calculate leaching and amendment requirements
   - Cost-benefit analysis

2. Install drainage (essential):
   - Subsurface tile drains
   - Spacing 10-30 m depending on soil
   - Depth 1-2 m
   - Outlet to disposal area
   - May need pumps
   - Expensive but necessary

3. Amend if sodic:
   - Gypsum application: 5-20 tons/acre
   - Incorporate with deep tillage
   - Sulfur if calcareous: 2-10 tons/acre
   - Organic matter if available

4. Leaching process:
   - Apply large volumes of water
   - May need 1-3 ft (30-90 cm) of water
   - Multiple leaching events
   - Monitor drainage water
   - May take 1-3 years

5. Cropping during reclamation:
   - Start with most tolerant crops
   - Barley, sugar beet
   - Forages for soil improvement
   - May have low yields initially
   - Gradual improvement

Challenges:
- Large water requirement for leaching
- Need good quality leaching water
- Drainage water disposal (environmental)
- Time consuming (years)
- Expensive
- Success not guaranteed
- May worsen before improves


VERY LOW (0-19): EXTREME SALT PROBLEMS

Management reality:
- Reclamation very difficult and expensive
- May not be technically feasible
- May not be economically viable
- Alternative uses often more appropriate

Reclamation attempts:
- Follow process for severe problems but:
- Even larger amendment needs (>20 tons/acre)
- Very large leaching requirements (>3 ft water)
- May need 5-10 years
- Very expensive
- High failure risk
- Drainage disposal major problem

Special techniques:

Deep plowing:
- Mix surface salt with deeper soil
- Dilution effect
- 3-6 ft deep plowing
- Expensive specialized equipment
- May help but not cure

Subsurface irrigation:
- Eliminates surface evaporation
- Reduces salt accumulation
- Expensive to install
- Requires good management

Crop alternatives:
- Salt-tolerant forage (saltgrass)
- No crop yield expectation
- More like rangeland
- Very low value

Alternative land uses:

Retirement:
- Remove from agricultural production
- May receive conservation payments
- Restoration to natural vegetation
- Prevent degradation spread

Salt-tolerant systems:
- Halophyte cultivation (research stage)
- Aquaculture (brine shrimp)
- Salt production (solar evaporation)
- Renewable energy (salt-tolerant biofuel crops)

Conservation:
- Salt marsh habitat
- Wildlife values
- Wetland credits
- Carbon sequestration

Economic reality:
- Reclamation costs may exceed land value
- Ongoing management costs high
- Success uncertain
- Alternative uses more viable
- May be best to accept limitation


GENERAL PRINCIPLES ACROSS ALL CLASSES:

Prevention:
- Much easier and cheaper than cure
- Good water quality critical
- Adequate drainage essential
- Appropriate irrigation management
- Monitor for early detection

Water management:
- Key to both prevention and control
- Leaching fraction based on water and soil EC
- Drainage absolutely essential
- Cannot manage salinity without drainage

Crop selection:
- Match crop tolerance to soil salinity
- Use salt-tolerant varieties
- Consider alternative crops
- Diversification reduces risk

Amendments:
- Address sodicity (gypsum)
- Improve structure
- Enhance infiltration
- Long-term investment

Monitoring:
- Regular soil testing
- EC and ESP measurements
- Track trends over time
- Adjust management based on results
"""

# ============================================================================
# INTERACTIONS WITH OTHER SOIL QUALITIES
# ============================================================================

"""
SQ5 INTERACTIONS WITH OTHER GAEZ INDICATORS:

SQ5 ↔ SQ1 (Nutrient Availability):
- High salinity interferes with nutrient uptake
- Osmotic stress reduces water and nutrient absorption
- Sodium displaces calcium, magnesium, potassium
- Nutritional imbalances common in saline soils
- High pH in sodic soils precipitates micronutrients
- Salinity can increase or decrease availability depending on element
- Combined effects reduce plant nutrition severely

SQ5 ↔ SQ2 (Nutrient Retention Capacity):
- High ionic strength affects retention
- Sodium saturates exchange sites
- Displaces other nutrient cations
- Very high salinity increases retention (more competition)
- But makes nutrients less available to plants
- Leaching salts also leaches nutrients (trade-off)

SQ5 ↔ SQ3 (Rooting Conditions):
- Sodicity destroys structure (physical barrier)
- Dense sodic layers impede root penetration
- High salinity reduces root growth
- Roots avoid saline zones
- Combined physical and chemical barriers
- Effective rooting depth reduced
- Both factors restrict root exploration

SQ5 ↔ SQ4 (Oxygen Availability):
- Sodic soils have poor drainage (structure collapse)
- Low permeability causes waterlogging
- Anaerobic conditions common in sodic soils
- Salinity and poor drainage often coincide
- Both cause plant stress
- Combined effects often lethal
- Poor drainage prevents salt leaching (vicious cycle)

SQ5 ↔ SQ6 (Toxicity):
- Specific ion toxicity part of salt problem
- Chloride, sodium, boron toxic at high levels
- High pH in sodic soils affects metal availability
- Some toxic elements mobilized by salinity
- Difficult to separate salt effects from toxicity
- Both contribute to plant stress
- May be impossible to distinguish in field

SQ5 ↔ SQ7 (Workability):
- Sodic soils extremely difficult to work
- Plastic and sticky when wet
- Extremely hard when dry
- Poor tilth and structure
- Crusting prevents operations
- Salts may clog equipment
- Both factors restrict management options
- Makes amelioration difficult
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ5:

1. Temporal and spatial variability:
   - Salinity changes seasonally
   - Rainfall and irrigation alter concentrations
   - Evaporation concentrates salts
   - Water table fluctuations affect distribution
   - Static rating doesn't capture dynamics
   - High spatial variability even within fields

2. Measurement challenges:
   - EC easy to measure but varies with moisture
   - ESP requires CEC and Na analysis (expensive)
   - Sampling depth and timing critical
   - Profile distribution varies
   - Field survey data often limited
   - Estimates may be inaccurate

3. Water quality interaction:
   - Soil salinity depends on irrigation water
   - May develop or worsen with poor water
   - May improve with good water and drainage
   - Rating should consider irrigation context
   - Water quality data often unavailable

4. Reclamation not considered:
   - Rating typically natural or current condition
   - Doesn't account for potential improvement
   - Reclaimed soils may perform much better
   - Or may re-salinize if management poor
   - Future condition uncertain

5. Crop-specific issues:
   - Generic rating doesn't fit all crops
   - Tolerance varies enormously
   - Rice actually prefers some salinity
   - Critical growth stages not considered
   - Variety differences significant

6. Multiple salt effects:
   - Osmotic, toxic, and nutritional effects combined
   - Difficult to separate
   - Salinity and sodicity interact
   - pH effects complicate
   - Total impact hard to predict

7. Management level not included:
   - Highly managed systems can cope better
   - Low-input systems more vulnerable
   - Technology available matters
   - Economic resources critical
   - Rating doesn't reflect management capacity

8. Environmental context:
   - Climate affects severity
   - Drainage disposal becoming restricted
   - Reclamation may not be permitted
   - Wetland designation may prevent improvement
   - Regulations increasingly important

RECOMMENDED USES:

Best for:
- Identifying salt-affected soils
- Regional assessment of salinity problems
- Preliminary crop suitability evaluation
- Screening for reclamation needs
- Comparative evaluation of land areas

Should be supplemented with:
- Detailed soil sampling and testing
- EC and ESP measurements at multiple depths
- Irrigation water quality analysis
- Crop-specific tolerance data
- Economic analysis of management options
- Local experience and field trials
- Monitoring over time
- Professional reclamation planning if needed
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on national soil surveys of variable quality
- Salinity data incomplete in many regions

Soil property data quality:
- EC and ESP: limited field measurements
- Often estimated from landscape position and climate
- Salt-affected soil mapping variable
- Better data in irrigated regions
- Poor data in remote areas
- Temporal variability not captured

CALCULATION DETAILS:

Rating functions:

For salinity (ECe):
- Exponential decline with increasing EC
- Threshold at 2 dS/m for sensitive crops
- Steep decline from 4-16 dS/m
- Near zero above 20 dS/m

For sodicity (ESP):
- Similar exponential decline
- Threshold at 6% ESP
- Structural effects emphasized
- Very low ratings above 25% ESP

Combined effects:
- Multiplicative when both present
- Both salinity and sodicity reduce rating
- Total effect worse than either alone

Profile weighting:
- Surface (0-30 cm): 60-70% weight
- Subsurface (30-100 cm): 30-40% weight

Climate adjustments:
- Arid regions: salinity weighted more heavily
- Humid regions: natural leaching considered
- Irrigation: developed salinity emphasized

(Note: Exact formulas proprietary to GAEZ methodology)

OUTPUT FORMATS:
- Raster grids at multiple resolutions
- Vector polygons with salinity/sodicity attributes
- Tabular summaries by soil unit
- Integration with other SQ indicators
- Crop-specific suitability with salt considerations

VALIDATION:
- Compared with salt-affected soil surveys
- Calibrated against crop performance
- Expert review by soil scientists
- Updated with reclamation district data
- Continues to improve with better data
"""

# ============================================================================
# REFERENCES AND FURTHER READING
# ============================================================================

"""
KEY REFERENCES:

Fischer, G., F. Nachtergaele, S. Prieler, H.T. van Velthuizen, L. Verelst, D. Wiberg, 2008. 
Global Agro-ecological Zones Assessment for Agriculture (GAEZ 2008). 
IIASA, Laxenburg, Austria and FAO, Rome, Italy.

FAO. 1976. A framework for land evaluation. 
FAO Soils Bulletin 32. Rome.

FAO. 2007. Land evaluation: towards a revised framework. 
Land and Water Discussion Paper 6. Rome.

FAO/IIASA/ISRIC/ISS-CAS/JRC. 2009. Harmonized World Soil Database (version 1.1). 
FAO, Rome, Italy and IIASA, Laxenburg, Austria.

SALINITY AND SODICITY REFERENCES:

Maas, E.V. and G.J. Hoffman. 1977.
Crop salt tolerance – current assessment.
Journal of Irrigation and Drainage Division, ASCE 103(IR2): 115-134.

Ayers, R.S. and D.W. Westcot. 1985.
Water quality for agriculture.
FAO Irrigation and Drainage Paper 29 (Rev. 1). FAO, Rome.

Rhoades, J.D., A. Kandiah, A.M. Mashali. 1992.
The use of saline waters for crop production.
FAO Irrigation and Drainage Paper 48. FAO, Rome.

Tanji, K.K. (ed.). 1990.
Agricultural Salinity Assessment and Management.
ASCE Manuals and Reports on Engineering Practice No. 71. American Society of Civil Engineers, New York.

Sposito, G. 2008.
The Chemistry of Soils, 2nd Edition.
Oxford University Press, Oxford, UK.

RECLAMATION REFERENCES:

Abrol, I.P., J.S.P. Yadav, F.I. Massoud. 1988.
Salt-affected soils and their management.
FAO Soils Bulletin 39. FAO, Rome.

Qadir, M., A. Tubeileh, J. Akhtar, A. Larbi, P.S. Minhas, M.A. Khan. 2008.
Productivity enhancement of salt-affected environments through crop diversification.
Land Degradation & Development, 19(4): 429-453.

USDA-NRCS. 1998.
National Engineering Handbook, Part 623: Irrigation, Chapter 2: Irrigation Water Requirements.
United States Department of Agriculture, Natural Resources Conservation Service.

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- FAO Land and Water: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/
- Global Map of Salt-affected Soils: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/global-map-of-salt-affected-soils/

CROP TOLERANCE DATA:

Maas, E.V. 1990.
Crop salt tolerance.
In: K.K. Tanji (ed.), Agricultural Salinity Assessment and Management.
ASCE Manuals and Reports on Engineering Practice No. 71. pp. 262-304.

Shannon, M.C. and C.M. Grieve. 1999.
Tolerance of vegetable crops to salinity.
Scientia Horticulturae, 78(1-4): 5-38.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ5 assesses problems from excess soluble salts and exchangeable sodium
2. Salinity creates osmotic stress and ion toxicity
3. Sodicity destroys soil structure and causes sodium toxicity
4. Affects ~1 billion hectares globally, especially in irrigated lands
5. Rated on 0-100 scale (high rating = low salt problem)
6. Crops vary enormously in salt tolerance (100-fold range)
7. Prevention much easier than cure
8. Reclamation expensive, time-consuming, and uncertain
9. Drainage absolutely essential for management
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ5 is critical because:
- Salt problems are widespread and increasing
- Severely limits crop selection and yields
- Cannot be ignored or compensated easily
- Worsens with poor irrigation management
- Can lead to land abandonment
- Reclamation difficult and expensive
- Prevention requires ongoing vigilance

Management essentials:
- Good quality irrigation water
- Adequate drainage system
- Appropriate leaching fraction
- Salt-tolerant crops if affected
- Gypsum for sodicity
- Regular monitoring
- Long-term commitment

Economic reality:
- Salt problems reduce land value dramatically
- Reclamation costs often exceed benefits
- Severely affected soils may be retired
- Prevention far more economical than cure
- Affects viability of irrigated agriculture

Environmental issues:
- Drainage water disposal problematic
- Wetland salinization concern
- Regulations increasingly restrict drainage
- May need to accept limitation

Understanding SQ5 is essential for:
- Irrigation system design and management
- Crop selection in affected areas
- Assessing reclamation feasibility
- Long-term sustainability of irrigated agriculture
- Land valuation and purchase decisions
- Regional agricultural planning

Excess salts represent one of the most severe and intractable soil limitations, 
requiring vigilant prevention and sophisticated management to avoid or remediate.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ5: EXCESS SALTS")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ5.")
    print("\nKey soil characteristics evaluated:")
    print("  Salinity assessment:")
    print("    - Electrical conductivity (EC)")
    print("    - Total dissolved solids (TDS)")
    print("    - Specific ion concentrations")
    print("\n  Sodicity assessment:")
    print("    - Exchangeable sodium percentage (ESP)")
    print("    - Sodium adsorption ratio (SAR)")
    print("    - pH effects in sodic soils")
    print("\n  Profile distribution and field indicators")
    print("\nRating classes: Very High (no salts), High, Medium, Low, Very Low")
    print("\nNote: High rating = good (no salt problems)")
    print("\nFor complete documentation, see the detailed text above.")
