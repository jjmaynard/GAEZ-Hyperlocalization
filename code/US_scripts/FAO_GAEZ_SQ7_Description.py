"""
FAO GAEZ SQ7: WORKABILITY/FIELD MANAGEMENT CONSTRAINTS - DETAILED DESCRIPTION
==============================================================================

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
SQ7: WORKABILITY/FIELD MANAGEMENT CONSTRAINTS

SQ7 represents the physical and practical constraints that affect the ease with 
which soil can be managed, worked, and cultivated. This soil quality indicator 
assesses characteristics that determine how readily soil can be tilled, planted, 
harvested, and managed for agricultural production, including aspects such as 
soil consistence, stoniness, slope, and climatic factors affecting field operations.

POSITION IN GAEZ FRAMEWORK:
SQ7 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability
- SQ2: Nutrient retention capacity
- SQ3: Rooting conditions
- SQ4: Oxygen availability to roots
- SQ5: Excess salts
- SQ6: Toxicity
- SQ7: Workability/field management constraints (focus of this document)
"""

# ============================================================================
# CONCEPTUAL BASIS
# ============================================================================

"""
FUNDAMENTAL CONCEPT:

Workability encompasses the soil and site characteristics that determine how 
easily agricultural operations can be performed. Good workability means:

1. Soil can be tilled without excessive power or equipment wear
2. Appropriate moisture range for field operations is adequate
3. Seedbeds can be prepared satisfactorily
4. Planting, fertilizing, and spraying can be done when needed
5. Harvest operations can be completed efficiently
6. Equipment can traverse fields without excessive difficulty
7. Timeliness of operations can be maintained

Poor workability creates:
- Limited windows for field operations
- High equipment costs and wear
- Difficulty achieving good seedbeds
- Delayed planting or harvest
- Soil degradation from working at wrong moisture
- Increased labor and time requirements
- Higher production costs
- Lower yields from untimely operations

AGRICULTURAL RELEVANCE:

Workability affects:
- Operating costs and efficiency
- Timeliness of crop establishment
- Crop performance and yields
- Equipment selection and investment
- Labor requirements
- Management intensity needed
- Crop selection possibilities
- Economic viability

Critical for:
- Mechanized agriculture (high sensitivity)
- Labor-limited operations
- High-value crops requiring precise timing
- Short planting/harvest windows
- Operations at specific moisture conditions

Less critical for:
- Hand-labor operations (more flexible)
- Perennial crops (less frequent cultivation)
- No-till systems (reduced tillage needs)
- Rangeland and forestry (minimal working)

Management implications:
- Equipment type and size selection
- Operation timing and scheduling
- Labor planning
- Drainage needs
- Traffic management
- Erosion control measures
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ7 DIAGNOSTIC CHARACTERISTICS:

The assessment of workability evaluates multiple soil, terrain, and climatic 
factors that affect field operations.

----------------------
SOIL TEXTURE AND CONSISTENCE
----------------------

1. TEXTURE EFFECTS ON WORKABILITY
   
   Definition: The relative proportions of sand, silt, and clay particles 
   determine many workability characteristics.
   
   Sandy soils (Coarse texture):
   
   Advantages:
   - Easy to work at wide moisture range
   - Low draft requirements (easy pulling)
   - Quick to dry after rain
   - Long working windows
   - Minimal stickiness or plasticity
   - Good trafficability
   - Low equipment wear
   
   Disadvantages:
   - Poor structure formation
   - Wind erosion susceptible
   - May be too loose (wheel slip)
   - Single-grain, non-cohesive
   - Difficult to form beds or ridges
   
   Optimal for:
   - Early season operations
   - Frequent cultivation
   - Low-power equipment
   - Root crops requiring loose soil
   
   
   Loamy soils (Medium texture):
   
   Advantages:
   - Moderate draft requirements
   - Good tilth achievable
   - Reasonable working range
   - Forms good seedbeds
   - Adequate structure
   - Generally good workability
   
   Disadvantages:
   - Moderate drying time needed
   - Some moisture sensitivity
   - Can compact if overworked
   
   Optimal for:
   - Most agricultural operations
   - Wide range of crops
   - Standard equipment
   - Balance of properties
   
   
   Clay soils (Fine texture):
   
   Advantages (when properly managed):
   - Excellent structure potential
   - High productivity
   - Strong clod formation
   - Good water retention
   
   Disadvantages:
   - High draft requirements (difficult pulling)
   - Very narrow working moisture range
   - Sticky when wet (clogs equipment)
   - Very hard when dry (extreme difficulty)
   - Slow to dry after rain
   - Plastic and unworkable when too wet
   - High equipment wear
   - Compacts easily when wet
   - Smears if worked wet
   - Short working windows
   - Shrinks and swells
   
   Critical moisture dependencies:
   - Too wet: completely unworkable, causes severe damage
   - Optimal: brief window, excellent results
   - Too dry: requires excessive power, forms large clods
   
   Management challenges:
   - Timing critical
   - Weather-dependent operations
   - Higher equipment costs
   - More labor intensive
   - Requires experience and skill
   
   Best practices:
   - Work only at proper moisture
   - Minimize passes
   - Controlled traffic
   - Avoid wet soil traffic
   - Consider permanent beds


2. SOIL CONSISTENCE
   
   Definition: The resistance of soil to deformation or rupture under applied 
   stress, strongly moisture-dependent.
   
   Consistence when wet:
   
   Non-sticky, non-plastic:
   - Excellent workability
   - Wide moisture range
   - Typical of sandy soils
   
   Slightly sticky, slightly plastic:
   - Good workability
   - Adequate moisture range
   - Typical of loamy soils
   
   Sticky, plastic:
   - Poor workability when wet
   - Clogs equipment
   - Smears if worked
   - Must dry to work
   - Typical of clay soils
   
   Very sticky, very plastic:
   - Very poor workability
   - Essentially unworkable when wet
   - Severe equipment problems
   - Heavy clays and sodic soils
   
   Consistence when moist (optimal for working):
   
   Friable:
   - Ideal workability
   - Crumbles easily
   - Forms good seedbed
   - Optimal moisture content
   
   Firm:
   - Moderate workability
   - Requires more power
   - Still acceptable
   
   Very firm:
   - Difficult to work
   - High power needed
   - Marginal conditions
   
   Consistence when dry:
   
   Soft, loose:
   - Easy to work but may be dusty
   - Typical of sandy soils
   
   Slightly hard:
   - Moderate difficulty
   - Typical of loams
   
   Hard:
   - Difficult to work
   - High power requirements
   - Poor clod breakdown
   - Typical of clays
   
   Very hard:
   - Extremely difficult
   - May require wetting first
   - Excessive equipment wear
   - Dense clays, crusted soils
   
   Extremely hard:
   - Essentially unworkable when dry
   - Massive clays, cemented soils
   - Must wet to soften


3. SOIL STRUCTURE AND AGGREGATION
   
   Well-aggregated soils:
   - Better workability
   - Stable structure
   - Less compaction susceptibility
   - Wider working moisture range
   - Better tilth
   - Easier seedbed preparation
   
   Poorly aggregated soils:
   - Poor workability
   - Unstable structure
   - High compaction risk
   - Narrow working range
   - Poor tilth
   - Difficult seedbed preparation
   - Crusting problems
   
   Massive structure:
   - Very poor workability
   - Essentially structureless
   - Cloddy when worked
   - High draft
   - Common in degraded or sodic soils


----------------------
SURFACE STONINESS AND ROCK OUTCROPS
----------------------

1. SURFACE STONINESS
   
   Definition: The proportion of soil surface covered by stones, cobbles, 
   or boulders >25 cm diameter.
   
   Stoniness classes and workability effects:
   
   Stone-free or few stones (<0.01% coverage):
   - No interference with operations
   - Excellent workability
   - No equipment damage
   - All operations possible
   
   Slightly stony (0.01-0.1% coverage):
   - Minimal interference
   - Occasional stone encounters
   - Very minor equipment impacts
   - Essentially no limitation
   
   Moderately stony (0.1-3% coverage):
   - Some interference
   - Regular stone encounters
   - Minor equipment damage possible
   - May affect some operations (root crops)
   - Tillage implements may be lifted occasionally
   
   Stony (3-15% coverage):
   - Significant interference
   - Frequent stone encounters
   - Moderate equipment damage
   - Root crops difficult
   - Harvest complications
   - Some implements not suitable
   
   Very stony (15-50% coverage):
   - Major interference
   - Continuous stone problems
   - High equipment damage and wear
   - Many operations very difficult
   - Root crops generally impossible
   - Limited crop options
   - Specialized equipment needed
   
   Extremely stony (50-90% coverage):
   - Severe interference
   - Operations extremely difficult
   - Very high equipment damage
   - Most operations impractical
   - Very limited crop options
   - May only suit pasture or forestry
   
   Stony land (>90% coverage):
   - Operations essentially impossible
   - Unsuitable for cultivation
   - Pasture or natural vegetation only


2. ROCK OUTCROPS
   
   Definition: Exposed bedrock at or protruding above the soil surface.
   
   Classes by percentage of area:
   
   None (0%):
   - No limitations
   
   Few rock outcrops (2-10%):
   - Minor navigation obstacles
   - Reduces effective tillable area
   - Some equipment limitations
   
   Rock outcrops common (10-25%):
   - Significant obstacles
   - Greatly reduces tillable area
   - Major equipment limitations
   - Field shape irregular
   
   Rock outcrops abundant (25-50%):
   - Severe obstacles
   - Little tillable area
   - Most operations very difficult
   - Limited to small equipment or hand work
   
   Rock outcrop dominant (>50%):
   - Operations essentially impossible
   - Not suitable for cultivation


3. COARSE FRAGMENTS THROUGH PROFILE
   
   Even if not at surface, stones/gravel in profile affect:
   - Tillage depth (stones brought to surface)
   - Equipment wear (subsurface contact)
   - Root crop quality (deformed by stones)
   - Implement penetration
   - Water management


----------------------
TOPOGRAPHY AND SLOPE
----------------------

1. SLOPE GRADIENT
   
   Definition: The degree of inclination of the land surface from horizontal.
   
   Effects on workability:
   
   Nearly level (0-2% slope):
   - Excellent workability
   - All directions of operation
   - All equipment suitable
   - No erosion concern from tillage
   - Possible drainage issues
   
   Gently sloping (2-5% slope):
   - Excellent to good workability
   - Most directions of operation
   - All standard equipment
   - Minor erosion concern
   - Generally no limitations
   
   Sloping (5-8% slope):
   - Good workability
   - Directional considerations needed
   - All standard equipment still suitable
   - Moderate erosion concern
   - Contour farming beneficial
   
   Moderately steep (8-15% slope):
   - Moderate workability
   - Operations across slope required
   - Some equipment limitations (size)
   - Significant erosion concern
   - Contour farming essential
   - Terracing may be needed
   - Tractor stability concerns begin
   
   Steep (15-30% slope):
   - Limited workability
   - Severe equipment limitations
   - Small equipment only
   - High erosion risk
   - Terracing often required
   - Tractor overturn risk
   - May limit to hand work or specialized equipment
   - Harvest difficult
   
   Very steep (30-45% slope):
   - Very limited workability
   - Most operations very difficult or impossible
   - Hand labor or specialized equipment only
   - Extreme erosion risk
   - Generally unsuitable for annual crops
   - Perennial crops with special management possible
   - Pasture or forestry more suitable
   
   Extremely steep (>45% slope):
   - Operations essentially impossible
   - Not suitable for cultivation
   - Forestry or natural vegetation only
   - Extreme erosion hazard


2. SLOPE LENGTH AND SHAPE
   
   Slope length:
   - Long slopes: erosion risk, longer field operations
   - Short slopes: less erosion, but more turning
   
   Slope shape:
   - Convex: accelerating flow, high erosion
   - Concave: decelerating flow, deposition
   - Uniform: even flow, manageable
   
   Slope aspect (direction):
   - Affects solar exposure and moisture
   - Influences working conditions
   - North vs. south slopes dry differently


3. TERRAIN COMPLEXITY
   
   Simple, uniform slopes:
   - Easier to manage
   - Consistent operations
   - Standard equipment
   
   Complex, irregular terrain:
   - Difficult management
   - Variable operations
   - Equipment challenges
   - Irregular field shapes
   - Numerous obstacles


----------------------
SOIL MOISTURE REGIME AND CLIMATE
----------------------

1. CLIMATIC WORKING DAYS
   
   Definition: The number of days per year when soil moisture conditions 
   permit field operations without damage to soil or crops.
   
   Factors determining working days:
   
   Rainfall distribution:
   - Frequent rain: few working days
   - Concentrated rain: better working windows
   - Dry seasons: ample working days
   
   Soil drainage:
   - Well-drained: dries quickly, many working days
   - Poorly drained: stays wet, few working days
   
   Soil texture:
   - Sandy: dries fast, many working days
   - Clay: dries slowly, few working days
   
   Climate:
   - Humid regions: fewer working days
   - Arid regions: many working days (but may need irrigation)
   - Monsoon: distinct dry season with many working days
   
   Seasonal considerations:
   - Spring wetness delays planting
   - Fall rains complicate harvest
   - Winter freeze periods (no working)
   - Summer may be only working season in some regions
   
   Working days classification:
   
   Abundant (>250 days/year):
   - Excellent workability
   - Very flexible scheduling
   - Minimal weather constraints
   - Typical of arid regions
   
   Adequate (150-250 days/year):
   - Good workability
   - Reasonable flexibility
   - Some weather constraints
   - Typical of temperate regions
   
   Limited (75-150 days/year):
   - Moderate workability constraints
   - Restricted scheduling
   - Significant weather dependence
   - Typical of humid regions or cold climates
   
   Very limited (30-75 days/year):
   - Severe workability constraints
   - Very restricted operations
   - High weather dependence
   - Poorly drained soils in humid regions
   
   Extremely limited (<30 days/year):
   - Extreme workability constraints
   - Operations very difficult to schedule
   - May be unsuitable for annual crops
   - Very poorly drained or extreme climates


2. EQUIPMENT TRAFFICABILITY
   
   Definition: Ability of soil to support equipment without excessive 
   sinking, rutting, or compaction.
   
   Good trafficability:
   - Soil supports equipment
   - Minimal rutting
   - Low compaction risk
   - Wide working moisture range
   - Sandy to loamy soils
   
   Poor trafficability:
   - Equipment sinks
   - Severe rutting
   - High compaction risk
   - Narrow working range
   - Clay soils when wet
   - Very soft organic soils
   
   Bearing capacity:
   - Ability to support loads
   - Lower when wet
   - Very low in organic soils
   - Affects equipment size that can be used


----------------------
SOIL DEPTH AND ROOTING RESTRICTIONS
----------------------

(Overlaps with SQ3 but affects working)

Shallow soils (<50 cm):
- Limit tillage depth
- Equipment strikes bedrock/hardpan
- Implements can't penetrate
- Damage to equipment
- Difficult to establish deep-rooted crops

Very shallow soils (<25 cm):
- Severe tillage limitations
- Only shallow cultivation possible
- Hand tools may be necessary
- Essentially unsuitable for deep tillage


----------------------
SPECIAL CONDITIONS
----------------------

1. FLOODING HAZARD
   
   Frequent flooding:
   - Unpredictable working windows
   - May lose crops
   - Equipment access problems
   - Timing very uncertain
   
   Affects planting and harvest timing critically


2. WIND EROSION SUSCEPTIBILITY
   
   In arid regions with sandy soils:
   - Limits cultivation (exposes soil)
   - Requires special practices
   - No-till preferred
   - Working increases erosion risk


3. CRUSTING AND SEALING
   
   Soils prone to surface crusting:
   - Difficult seedbed maintenance
   - Emergence problems
   - Requires additional operations
   - More working needed
   - Fine-textured or sodic soils most susceptible


4. SOIL TEMPERATURE
   
   Cold soils:
   - Delayed spring operations
   - Equipment works frozen soil (damage)
   - Limits working season
   - Affects planting dates
   - Heavy soils warm slowly


5. PERMANENT SOIL WETNESS
   
   Very poorly drained soils:
   - Never fully dry
   - Very few working days
   - Equipment always causes damage
   - Essentially unworkable
"""

# ============================================================================
# RATING SYSTEM
# ============================================================================

"""
SQ7 RATING SCALE:

Soils are rated on a 0-100 scale based on ease of working and management:

0-100 SCALE INTERPRETATION:
- 80-100: Very High - Excellent workability, minimal constraints
- 60-79:  High - Good workability, minor constraints
- 40-59:  Medium - Moderate workability, significant constraints
- 20-39:  Low - Poor workability, severe constraints
- 0-19:   Very Low - Very poor workability, extreme constraints


VERY HIGH (80-100): EXCELLENT WORKABILITY

Soil and site characteristics:
- Loamy to sandy loam texture
- Well-drained
- Level to gently sloping (<5%)
- Stone-free or few stones
- No rock outcrops
- Friable consistence
- Good structure
- Deep soil (>100 cm)
- Adequate climatic working days (>200/year)

Workability properties:
- Wide working moisture range
- Easy tillage (low draft)
- Excellent seedbed formation
- All equipment suitable
- Good trafficability
- Minimal weather dependence
- Long working windows
- Low equipment wear
- Operations can be done when needed

Management advantages:
- Flexible operation scheduling
- Timeliness achievable
- Low operating costs
- Standard equipment adequate
- All crops suitable
- High efficiency
- Minimal labor needs
- Low management intensity

Examples:
- Deep loamy soils on level land
- Well-drained sandy loams
- Intensively managed agricultural land


HIGH (60-79): GOOD WORKABILITY

Soil and site characteristics:
- Sandy loam to clay loam texture
- Well to moderately well-drained
- Level to sloping (5-8%)
- Few to some stones
- Occasional rock outcrops
- Generally friable
- Moderate structure
- Moderately deep soil (50-100 cm)
- Good climatic working days (150-200/year)

Workability properties:
- Adequate working moisture range
- Moderate tillage requirements
- Good seedbed achievable
- Most equipment suitable
- Good trafficability
- Some weather dependence
- Reasonable working windows
- Moderate equipment wear

Management implications:
- Generally flexible scheduling
- Timeliness usually achievable
- Moderate operating costs
- Some directional considerations (slope)
- Most crops suitable
- Good efficiency
- Standard practices work well

Limitations:
- Some timing sensitivity
- Minor equipment constraints
- Possible erosion on slopes
- Occasional weather delays


MEDIUM (40-59): MODERATE WORKABILITY

Soil and site characteristics:
- Clay loam to clay texture, or
- Moderately steep slopes (8-15%), or
- Moderately stony (3-15% surface cover), or
- Somewhat poorly drained, or
- Some rock outcrops (2-10%), or
- Limited working days (75-150/year), or
- Shallow soil (25-50 cm)

Workability properties:
- Narrow working moisture range (clay soils)
- Difficult tillage (high draft)
- Seedbed requires extra effort
- Equipment limitations present
- Moderate trafficability issues
- Significant weather dependence
- Restricted working windows
- High equipment wear possible

Management requirements:
- Careful operation timing essential
- Timeliness challenging
- Higher operating costs
- Specialized equipment may be needed
- Crop selection considerations
- Erosion control essential on slopes
- Drainage improvement beneficial
- More intensive management needed
- Higher labor requirements

Specific challenges by cause:

Heavy clay soils:
- Work only at correct moisture
- High power requirements
- Sticky when wet, hard when dry
- Short working window
- Compaction risk
- Requires experience

Moderate slopes:
- Contour operations required
- Equipment size limitations
- Erosion control essential
- Terracing may be beneficial
- Directional constraints

Stony soils:
- Equipment damage risk
- Slower operations
- Some implements unsuitable
- Root crop limitations
- Harvest complications

Limited working days:
- Weather-dependent operations
- Delayed operations common
- Flexible scheduling difficult
- May miss optimal timing


LOW (20-39): POOR WORKABILITY

Soil and site characteristics:
- Heavy clay texture, or
- Steep slopes (15-30%), or
- Very stony (15-50% surface cover), or
- Poorly drained, or
- Common rock outcrops (10-25%), or
- Very limited working days (30-75/year), or
- Very shallow soil (<25 cm), or
- Multiple moderate limitations

Workability properties:
- Very narrow working range
- Very difficult tillage
- Poor seedbeds difficult to avoid
- Severe equipment limitations
- Poor trafficability
- High weather dependence
- Very restricted operations
- Excessive equipment wear
- Operations often impossible to complete properly

Management challenges:
- Operation timing critical but difficult
- Timeliness rarely achieved
- High operating costs
- Specialized equipment essential
- Very limited crop options
- Intensive erosion control needed
- Major drainage needs
- Very intensive management required
- High labor requirements
- Low efficiency

Specific challenges:

Heavy clays:
- Extremely limited working range
- Massive equipment requirements or hand work
- Severe stickiness or hardness
- Very short windows
- High compaction and smearing risk
- May be sodic (worst case)

Steep slopes:
- Small equipment only
- Hand labor often needed
- Extreme erosion risk
- Terracing essential
- Overturn hazard
- Limited to perennial crops or special management

Very stony:
- Continuous equipment damage
- Very slow operations
- Many implements unsuitable
- Root crops impossible
- Specialized equipment essential

Poorly drained:
- Very few working days
- Always at risk of damage
- Drainage essential
- May never be truly workable

Economic viability:
- High costs relative to productivity
- May not be economically viable
- Consider less intensive land uses
- May need major capital improvements


VERY LOW (0-19): VERY POOR WORKABILITY

Soil and site characteristics:
- Very heavy clay (sodic), or
- Very steep slopes (>30%), or
- Extremely stony (>50% surface), or
- Very poorly drained, or
- Rock outcrop dominant (>25%), or
- Extremely limited working days (<30/year), or
- Multiple severe limitations

Workability properties:
- Operations essentially impossible with standard methods
- Tillage requires extreme measures
- Seedbeds very poor or impossible
- Equipment cannot be used or severely restricted
- No trafficability
- Complete weather dependence
- Operations almost never possible appropriately
- Prohibitive equipment wear/damage

Management reality:
- Conventional mechanized agriculture not viable
- Hand labor only option for cultivation
- Extreme costs if operations attempted
- Very limited crop options (perennials, pasture)
- Not economically viable for annual crops
- May require complete redesign of production system

Specific conditions:

Heavy sodic clays:
- Essentially unworkable
- Plastic when wet, rock-hard when dry
- Almost no working window
- Causes severe equipment problems
- Requires major reclamation

Very steep slopes:
- Impossible to use equipment
- Hand labor only
- Extreme erosion
- Generally unsuitable for cultivation
- Forestry or natural vegetation appropriate

Rock outcrop/extremely stony:
- No tillable area
- Equipment impossible to use
- Not cultivatable
- Pasture or natural vegetation only

Very poorly drained:
- Never dries adequately
- Always causes damage
- Wet season operations impossible
- Suitable only for wetland crops (rice) or retirement

Alternative uses:
- Forestry
- Natural vegetation
- Wildlife habitat
- Extensive grazing (poor quality)
- Conservation/retirement
- Wetlands (if applicable)
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
APPROACH TO RATING SQ7:

The rating methodology integrates multiple factors affecting workability:

1. PRIMARY RATING FACTORS:

   Soil texture and consistence:
   - Weighted 30-40% of rating
   - Sandy soils rate highest (easy to work)
   - Clay soils rate lowest (difficult to work)
   - Modified by structure and drainage
   
   Slope gradient:
   - Weighted 20-30% of rating
   - Level best, steep severely limits
   - Exponential decrease with slope
   - Interacts with erosion concern
   
   Surface stoniness:
   - Weighted 15-25% of rating
   - Percentage cover determines impact
   - Rock outcrops treated similarly
   - Severe stone content very limiting
   
   Drainage/climatic working days:
   - Weighted 15-25% of rating
   - Working days available per year
   - Interaction of soil drainage and climate
   - Very important in humid regions


2. TEXTURE-CONSISTENCE RATING:

   Rating by texture class:
   - Sand, loamy sand: 90-100
   - Sandy loam: 85-95
   - Loam: 80-90
   - Silt loam: 75-85
   - Sandy clay loam: 70-80
   - Clay loam: 60-75
   - Silty clay loam: 55-70
   - Sandy clay: 50-65
   - Silty clay: 40-55
   - Clay: 30-50
   - Heavy clay: 20-40
   - Heavy clay (sodic): 0-20
   
   Modified by:
   - Structure: good structure improves rating
   - Consistence: friable better than hard/sticky
   - Organic matter: improves workability of clays


3. SLOPE RATING:

   Rating by slope class:
   - 0-2%: 95-100
   - 2-5%: 85-95
   - 5-8%: 70-85
   - 8-15%: 45-70
   - 15-30%: 20-45
   - 30-45%: 5-20
   - >45%: 0-5
   
   Adjustments:
   - Slope length: longer slopes slightly worse
   - Erosion susceptibility: increases limitation
   - Terrain complexity: reduces rating further


4. STONINESS RATING:

   Rating by stone coverage:
   - 0-0.01%: 95-100
   - 0.01-0.1%: 90-95
   - 0.1-3%: 70-90
   - 3-15%: 40-70
   - 15-50%: 15-40
   - 50-90%: 5-15
   - >90%: 0-5
   
   Rock outcrops rated similarly
   
   Type of coarse fragments:
   - Rounded: less problematic
   - Angular: more problematic
   - Size: larger worse than smaller


5. WORKING DAYS RATING:

   Rating by working days available:
   - >250 days: 95-100
   - 150-250 days: 75-95
   - 75-150 days: 45-75
   - 30-75 days: 20-45
   - <30 days: 0-20
   
   Determined by:
   - Rainfall distribution
   - Soil drainage class
   - Soil texture (drying rate)
   - Temperature (freezing periods)
   - Regional climate patterns


6. INTEGRATION METHOD:

   Most limiting factor approach with averaging:
   
   Step 1: Calculate individual factor ratings
   Step 2: Identify most limiting factor
   Step 3: Weight factors:
      - Most limiting: 50-60% weight
      - Other factors: 40-50% combined
   
   Result: Final rating between 0-100
   
   Example:
   - Texture: 70 (clay loam)
   - Slope: 85 (5%)
   - Stoniness: 90 (few stones)
   - Working days: 60 (limited)
   
   Most limiting: Working days (60)
   Final rating = 0.55×60 + 0.45×[(70+85+90)/3]
                = 33 + 0.45×82
                = 33 + 37 = 70 (High class)


7. MULTIPLE LIMITATION EFFECTS:

   Single severe limitation:
   - Caps overall rating
   - Cannot average to acceptable level
   - Heavy clay OR steep slope = low rating
   
   Multiple moderate limitations:
   - Cumulative effect
   - Each additional limitation reduces rating
   - Combined worse than single issue


8. MANAGEMENT LEVEL CONSIDERATIONS:

   High-input/mechanized systems:
   - More sensitive to workability
   - Precise timing needed
   - Equipment limitations critical
   - SQ7 weighted heavily
   
   Low-input/hand labor systems:
   - Less sensitive to workability
   - More flexible with conditions
   - Can work steeper slopes
   - SQ7 less critical
   
   No-till systems:
   - Reduced sensitivity to some factors
   - Texture/consistence less important
   - Drainage still critical
   - Slope still matters


9. CROP-SPECIFIC ADJUSTMENTS:

   Perennial crops:
   - Less frequent tillage
   - Higher tolerance of poor workability
   - Slope and stoniness still matter for harvest
   
   Annual crops:
   - Frequent operations needed
   - Low tolerance of poor workability
   - All factors critical
   
   Root crops:
   - Very sensitive to stoniness
   - Need deep, stone-free soils
   - Texture critical for harvest
   
   No-till crops:
   - Reduced texture sensitivity
   - Drainage and slope still critical


10. CLIMATE-REGION ADJUSTMENTS:

    Humid temperate:
    - Working days most limiting
    - Drainage critical
    - Weight these factors heavily
    
    Arid/semi-arid:
    - Working days abundant
    - Texture, slope more important
    - Weight these factors heavily
    
    Tropical humid:
    - Working days seasonally limited
    - Heavy rainfall affects operations
    - Drainage very important
    
    Cold regions:
    - Short season limits working days
    - Frost considerations
    - Soil temperature important
"""

# ============================================================================
# CROP-SPECIFIC RESPONSES
# ============================================================================

"""
CROP SENSITIVITY TO WORKABILITY CONSTRAINTS:

HIGHLY SENSITIVE CROPS (require excellent workability):

Root and tuber crops:
- Potatoes, carrots, beets, radishes
- Need stone-free, loose soil
- Require multiple operations
- Harvest very sensitive to conditions
- Cannot tolerate stones (deformed products)
- Need deep tillage

Sugar beet:
- Deep taproot requires loose soil
- Stone-free essential
- Harvest equipment sensitive
- Precise timing needed

Vegetables (most):
- Multiple operations
- Precise timing for quality
- Seedbed critical
- Transplanting requires good conditions
- Harvest timing critical for quality

Peanuts:
- Underground pods
- Need friable soil
- Harvest sensitive to moisture
- Require good trafficability


MODERATELY SENSITIVE CROPS:

Cereals (wheat, barley, oats):
- Need good seedbed
- Harvest sensitive to timing
- Multiple operations beneficial
- Some tolerance of poor conditions
- Can work on some slopes

Maize:
- Large equipment typical
- Benefits from good trafficability
- Can tolerate some stones
- Sensitive to compaction

Soybeans:
- Moderate sensitivity
- Harvest timing important
- Benefits from good seedbed
- Some tolerance of conditions

Cotton:
- Multiple operations needed
- Harvest weather-sensitive
- Benefits from good workability
- Some tolerance of constraints


TOLERANT CROPS (lower sensitivity):

Small grains on slopes:
- Can be grown on steeper land
- Harvest less equipment-intensive
- Some hand harvest possible

Forages:
- Infrequent operations
- Can tolerate poor workability
- Slopes acceptable
- Some stoniness tolerated
- Harvest less sensitive

Pasture:
- Minimal operations
- Low sensitivity to workability
- Suitable for poor workability sites
- Can utilize steep slopes


VERY TOLERANT (minimal workability needs):

Perennial forages (established):
- No tillage after establishment
- Only harvest operations
- Low equipment requirements
- Steep slopes acceptable

Orchards/vineyards:
- Established with difficulty then permanent
- Minimal subsequent cultivation
- Can be on slopes
- Some stoniness acceptable
- Harvest considerations vary

Forestry:
- Minimal operations
- Can utilize very poor workability
- Steep slopes, stony soils acceptable
- Harvest has some limitations

Rangeland:
- No cultivation
- No workability requirement
- Suitable for all poor workability conditions
"""

# ============================================================================
# MANAGEMENT STRATEGIES BY SQ7 CLASS
# ============================================================================

"""
MANAGEMENT APPROACHES FOR DIFFERENT SQ7 RATINGS:

VERY HIGH (80-100): EXCELLENT WORKABILITY

Management approach:
- Standard mechanized agriculture
- Flexible operation scheduling
- Timeliness achievable
- All crops suitable

Practices:
- Use appropriate equipment for conditions
- Maintain good soil conditions
- Avoid unnecessary compaction
- Preserve structure
- Standard tillage or no-till both work

Advantages:
- Low operating costs
- High efficiency
- Wide crop selection
- Minimal constraints


HIGH (60-79): GOOD WORKABILITY

Management approach:
- Standard agriculture with some care
- Generally flexible scheduling
- Most crops suitable

Practices:
- Monitor moisture for operations (if clay loam)
- Follow contours if sloping
- Erosion control if needed
- Avoid working too wet
- Select appropriate equipment

Minor adjustments:
- Timing slightly more critical
- Some directional constraints
- Equipment size consideration
- Erosion prevention


MEDIUM (40-59): MODERATE WORKABILITY

Management approach:
- Careful management essential
- Restricted scheduling
- Crop selection important
- Higher costs expected

Specific management by limitation type:

For CLAY SOILS:

Timing critical:
- Work only at correct moisture
- Test before entering field
- Avoid working wet (causes smearing)
- Avoid working too dry (excessive clods)
- Weather forecasting essential

Equipment considerations:
- Higher horsepower needed
- Low ground pressure preferred
- Tracks better than wheels
- Specialized implements
- More frequent maintenance

Soil improvement:
- Add organic matter
- Improve structure
- Lime if acidic
- Gypsum if sodic
- Reduce tillage intensity
- Consider permanent bed systems

Traffic management:
- Controlled traffic farming
- Permanent wheel tracks
- Minimize passes
- Combine operations where possible

Alternative systems:
- No-till or reduced tillage
- Permanent beds
- Strip till
- Avoid deep tillage


For MODERATE SLOPES (8-15%):

Erosion control essential:
- Contour farming mandatory
- Strip cropping
- Terracing beneficial
- Cover crops
- Residue management
- Grass waterways

Equipment adaptation:
- Smaller equipment
- Appropriate for slope
- Hillside equipment if needed
- Safety considerations

Operation direction:
- Across slope only
- Plan field layout
- Irregular field shapes
- More turning required

Crop selection:
- Perennials preferred
- High residue crops
- Avoid row crops if possible
- Forages excellent


For STONY SOILS (3-15% cover):

Equipment protection:
- Stone guards on implements
- Reinforced equipment
- Slower operations
- More maintenance
- Higher wear costs

Crop selection:
- Avoid root crops
- Small grains suitable
- Forages good
- Tree fruits possible

Operations adaptation:
- Shallower tillage
- Avoid deep plowing
- No-till preferred
- Specialized harvest equipment

Stone management:
- Stone picking if economical
- Periodic removal
- May worsen over time (tillage brings up)


For LIMITED WORKING DAYS (75-150):

Scheduling critical:
- Seize opportunities
- Flexible operation plans
- Alternative dates ready
- Weather monitoring constant

Equipment readiness:
- Maintenance current
- Ready to go quickly
- May need extra capacity
- Backup equipment valuable

Drainage improvement:
- Surface drainage
- Subsurface if feasible
- Improves working days significantly
- Good return on investment

Crop selection:
- Flexible planting dates
- Short season varieties
- Less timing-sensitive crops
- Perennials reduce need


LOW (20-39): POOR WORKABILITY

Management approach:
- Intensive specialized management
- Very restricted operations
- Limited crop options
- High costs
- Questionable economic viability

For HEAVY CLAY SOILS:

Extreme timing sensitivity:
- Very brief working window
- Must work at exact moisture
- Equipment ready and waiting
- Operations may be delayed weeks
- May miss optimal timing

Major equipment requirements:
- Very high horsepower
- Specialized implements
- Frequent breakdowns
- Very high maintenance
- Low ground pressure essential

Soil modification approaches:
- Massive organic matter additions
- Deep ripping when dry
- Gypsum if sodic (large amounts)
- Lime if acidic
- Sand addition (very expensive)
- Raised beds with imported soil

Alternative systems:
- No-till essential
- Permanent beds
- Avoid all unnecessary tillage
- May need complete system redesign

Crop limitations:
- Only most tolerant crops
- Avoid sensitive crops
- Perennials preferred
- May need to change farming system


For STEEP SLOPES (15-30%):

Severe erosion risk:
- Terracing essential for annual crops
- Huge investment required
- Maintenance intensive

Equipment severe limitations:
- Small equipment only
- Hand labor often needed
- Very slow operations
- Safety hazards significant
- Overturn risk high

Crop restrictions:
- Perennials strongly preferred
- Annual crops risky
- Tree crops
- Forages
- Avoid row crops

Economic reality:
- High costs
- Lower productivity
- May not be viable for annual crops
- Consider permanent vegetation


For VERY STONY SOILS (15-50%):

Severe equipment problems:
- Constant damage
- Very high wear
- Slow operations
- Many implements unusable

Crop severe restrictions:
- No root crops
- Limited to crops tolerant of stones
- Tree fruits possible
- Forages suitable

Stone management:
- Removal may not be economical
- Would need to be ongoing
- Deteriorates with tillage

Consider alternative:
- Pasture
- Forestry
- Less intensive use


For VERY LIMITED WORKING DAYS (<75):

Operations very difficult:
- Rarely good conditions
- Miss optimal timing regularly
- Delayed plantings common
- Harvest complications

Major drainage needed:
- Subsurface drainage essential
- Surface drainage too
- May be expensive or impossible
- Check feasibility and cost

Crop severe restrictions:
- Very flexible crops only
- Wide planting windows needed
- Perennials preferred
- Annual crops risky

Economic viability:
- High risk of losses
- Unpredictable timing
- Low reliability
- May not be viable


VERY LOW (0-19): VERY POOR WORKABILITY

Management reality:
- Conventional mechanized agriculture not viable
- Extreme costs if attempted
- Very limited options
- Alternative land uses appropriate

For HEAVY SODIC CLAYS:

Essentially unworkable:
- No working window
- Plastic when wet
- Rock-hard when dry
- Equipment cannot function

Reclamation required:
- Gypsum (massive amounts)
- Drainage essential
- Years to improve
- Very expensive
- Success uncertain

Alternative: Change land use or retire


For VERY STEEP SLOPES (>30%):

Operations impossible:
- No equipment usable
- Hand labor only option
- Extreme erosion
- Safety hazards

Appropriate uses:
- Forestry
- Natural vegetation
- Permanent vegetation only
- Conservation


For EXTREMELY STONY/ROCK OUTCROP:

No tillable area:
- Cannot use equipment
- No cultivation possible

Appropriate uses:
- Extensive grazing (poor)
- Natural vegetation
- Wildlife habitat
- Forestry (limited)


For VERY POORLY DRAINED:

Never workable:
- Always too wet
- Operations always cause damage
- Cannot establish crops

Options:
- Wetland rice if climate suitable
- Wetland preservation
- Aquaculture
- Land retirement

Drainage:
- May not be feasible
- May not be permitted
- Very expensive if possible


GENERAL PRINCIPLES:

Prevention of degradation:
- Maintain good conditions
- Avoid compaction
- Work at proper moisture
- Preserve structure
- Minimize unnecessary operations

Adaptation strategies:
- Match crops to workability
- Adjust systems to constraints
- Use appropriate equipment
- Improve conditions where feasible
- Accept limitations where unchangeable

Economic decisions:
- Calculate costs vs. returns
- Poor workability increases costs
- May require system change
- Alternative uses may be better
- Some land not viable for cultivation
"""

# ============================================================================
# INTERACTIONS WITH OTHER SOIL QUALITIES
# ============================================================================

"""
SQ7 INTERACTIONS WITH OTHER GAEZ INDICATORS:

SQ7 ↔ SQ1 (Nutrient Availability):
- Good workability allows timely fertilization
- Poor workability delays operations, affects nutrient management
- Stony soils difficult to incorporate amendments
- Steep slopes complicate fertilizer application
- Working at wrong moisture can reduce nutrient availability
- Generally independent but management linkage

SQ7 ↔ SQ2 (Nutrient Retention Capacity):
- Poor workability may lead to surface application only
- Good workability allows incorporation
- Compaction from poor timing reduces retention
- Structure degradation affects both
- Generally independent factors

SQ7 ↔ SQ3 (Rooting Conditions):
- Shallow soils limit both working depth and rooting
- Stony soils affect both tillage and roots
- Compaction from poor workability creates hardpans
- Working wet soil reduces rooting potential
- Both affected by soil depth
- Strong interaction through compaction

SQ7 ↔ SQ4 (Oxygen Availability):
- Poor drainage reduces working days AND oxygen
- Compaction from working wet reduces aeration
- Heavy clay soils have both poor workability and drainage risk
- Very strong interaction
- Combined effects multiplicative
- Poor drainage = poor workability in humid climates

SQ7 ↔ SQ5 (Excess Salts):
- Sodic soils have worst possible workability (sticky, dispersed)
- Saline soils may crust severely
- Workability affects ability to reclaim
- Salt management requires good workability
- Strong interaction through sodicity

SQ7 ↔ SQ6 (Toxicity):
- Acid clay soils combine poor workability with Al toxicity
- Lime incorporation difficult in poor workability soils
- Amendment application easier with good workability
- Steep slopes complicate amelioration efforts
- Workability affects management of toxicity
- Moderate interaction through management difficulty
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ7:

1. Subjective assessment:
   - "Workability" somewhat subjective
   - Experience-dependent
   - Cultural and regional differences in what's acceptable
   - Equipment technology evolving
   - Management skill varies

2. Weather variability:
   - Working days vary year to year
   - Based on long-term averages
   - Extreme years differ greatly
   - Climate change affecting patterns

3. Management level not considered:
   - High-skill managers cope better
   - Equipment quality matters
   - Capital availability affects options
   - Rating assumes moderate management

4. Crop-specific differences:
   - Generic rating doesn't fit all crops
   - Root crops very sensitive
   - Perennials less sensitive
   - No-till systems less affected

5. Technological change:
   - New equipment changes feasibility
   - GPS guidance helps on slopes
   - Low-pressure tires improve trafficability
   - No-till reduces workability importance
   - Rating may not reflect latest technology

6. Economic context missing:
   - Costs vs. returns not considered
   - What's economically viable varies
   - High-value crops justify more effort
   - Low-value crops need easy working

7. Scale dependencies:
   - Large operations need better workability
   - Small operations more flexible
   - Hand labor changes everything
   - Equipment size affects capability

8. Temporal dynamics:
   - Conditions change over time
   - Compaction develops
   - Drainage improves or worsens
   - Management affects workability
   - Static rating doesn't capture changes

RECOMMENDED USES:

Best for:
- Preliminary land evaluation
- Regional planning
- Identifying challenging areas
- Equipment selection guidance
- Crop suitability screening
- Comparative assessment

Should be supplemented with:
- Local experience and knowledge
- Actual field testing
- Crop-specific evaluation
- Economic analysis
- Equipment availability assessment
- Management skill consideration
- Weather risk analysis
- Long-term observation
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on national soil surveys
- Variable quality by region

Soil property data quality:
- Texture: widely measured, reliable
- Drainage class: interpreted, variable quality
- Stoniness: often estimated, variable
- Slope: from DEM, generally good
- Structure: descriptive, subjective
- Working days: calculated from climate data

Terrain data:
- Slope from digital elevation models
- Generally good quality
- Resolution affects accuracy

Climate data:
- Rainfall distribution
- Temperature patterns
- Used to estimate working days
- Variable quality by region

CALCULATION DETAILS:

Rating functions:

For texture:
- Categorical rating by texture class
- Modified by structure and consistence
- Clay soils rated lowest
- Sandy soils rated highest

For slope:
- Exponential decrease with gradient
- Threshold at 15% (steep)
- Near zero above 45%

For stoniness:
- Percentage coverage
- Exponential decrease
- Threshold at 15% coverage

For working days:
- Calculated from:
  * Rainfall distribution
  * Soil drainage class
  * Soil texture (drying rate)
  * Temperature (freezing days)
- Regional models vary

Integration:
- Most limiting factor approach
- Weighted average of factors
- Most limiting 50-60% weight
- Others 40-50% combined

Profile considerations:
- Surface conditions most important
- Subsurface affects trafficability
- Restrictions at depth affect tillage

(Note: Exact formulas proprietary to GAEZ methodology)

OUTPUT FORMATS:
- Raster grids at multiple resolutions
- Vector polygons with attributes
- Tabular summaries by soil unit
- Integration with other SQ indicators
- Crop-specific suitability classes

VALIDATION:
- Compared with agricultural land use
- Calibrated against farmer experience
- Expert review by soil scientists
- Updated with new data
- Regional adjustments
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

SOIL WORKABILITY REFERENCES:

Larson, W.E. and W.R. Gill. 1973.
Soil physical parameters for designing new tillage systems.
In: Conservation Tillage: Proceedings of a National Conference, Soil Conservation 
Society of America, pp. 13-22.

Soane, B.D., P.S. Blackwell, J.W. Dickson, D.J. Painter. 1981.
Compaction by agricultural vehicles: A review II. Compaction under tyres and other 
running gear.
Soil and Tillage Research, 1(4): 373-400.

Campbell, D.J. and J.K. Henshall. 1991.
Bulk density. In: K.A. Smith and C.E. Mullins (eds.), Soil Analysis: Physical Methods.
Marcel Dekker, New York, pp. 329-366.

SLOPE AND EROSION REFERENCES:

Wischmeier, W.H. and D.D. Smith. 1978.
Predicting Rainfall Erosion Losses: A Guide to Conservation Planning.
USDA Agriculture Handbook No. 537. U.S. Department of Agriculture, Washington, DC.

Renard, K.G., G.R. Foster, G.A. Weesies, D.K. McCool, D.C. Yoder. 1997.
Predicting Soil Erosion by Water: A Guide to Conservation Planning with the Revised 
Universal Soil Loss Equation (RUSLE).
USDA Agriculture Handbook No. 703. U.S. Department of Agriculture, Washington, DC.

TILLAGE AND SOIL MANAGEMENT:

Unger, P.W. and T.C. Kaspar. 1994.
Soil compaction and root growth: A review.
Agronomy Journal, 86(5): 759-766.

Hamza, M.A. and W.K. Anderson. 2005.
Soil compaction in cropping systems: A review of the nature, causes and possible solutions.
Soil and Tillage Research, 82(2): 121-145.

Håkansson, I. and R.C. Reeder. 1994.
Subsoil compaction by vehicles with high axle load – extent, persistence and crop response.
Soil and Tillage Research, 29(2-3): 277-304.

EQUIPMENT AND TRAFFICABILITY:

McKyes, E. 1985.
Soil Cutting and Tillage.
Elsevier, Amsterdam.

Gill, W.R. and G.E. Vanden Berg. 1968.
Soil Dynamics in Tillage and Traction.
USDA Agriculture Handbook No. 316. U.S. Department of Agriculture, Washington, DC.

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- Land evaluation guidelines: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/

CONSERVATION TILLAGE:

Derpsch, R., T. Friedrich, A. Kassam, L. Hongwen. 2010.
Current status of adoption of no-till farming in the world and some of its main benefits.
International Journal of Agricultural and Biological Engineering, 3(1): 1-25.

FAO. 2001.
Conservation Agriculture: Case Studies in Latin America and Africa.
FAO Soils Bulletin 78. FAO, Rome.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ7 assesses ease of soil working and field management
2. Major factors: texture/consistence, slope, stoniness, working days
3. Determines feasibility and cost of mechanized operations
4. Critical for timeliness of operations
5. Rated on 0-100 scale, classified into 5 categories
6. Heavy clay soils and steep slopes most limiting
7. Poor workability increases costs and reduces efficiency
8. Crop selection must match workability constraints
9. Some limitations correctable, others permanent
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ7 is important because:
- Affects economic viability directly through costs
- Determines feasibility of mechanized agriculture
- Influences timeliness and crop performance
- Limits crop selection options
- Cannot be easily changed (inherent properties)
- Becoming more critical with larger equipment
- Critical for modern commercial agriculture

Management implications:
- Good workability = flexible, efficient, profitable
- Poor workability = constrained, expensive, difficult
- Severe limitations may preclude annual cropping
- Equipment must match conditions
- Timing critical in poor workability soils
- Alternative systems may be needed (no-till, perennials)

Economic reality:
- Workability directly affects costs
- Poor workability reduces land value
- May determine viability of farming enterprise
- High-value crops can justify poor workability
- Low-value crops require good workability
- Some land not economically cultivatable

Understanding SQ7 is essential for:
- Realistic economic assessment
- Equipment selection and sizing
- Operation planning and scheduling
- Crop selection
- System design (tillage vs. no-till)
- Labor and time budgeting
- Risk assessment (timeliness)
- Long-term viability evaluation

Good workability is increasingly important in modern agriculture with:
- Larger equipment (requires better trafficability)
- Tighter scheduling (requires more working days)
- Higher costs (requires efficiency)
- Mechanization emphasis (requires suitable conditions)

Poor workability is a hidden cost multiplier - it increases expenses for every 
operation while often reducing yields through untimely operations.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ7: WORKABILITY/FIELD MANAGEMENT CONSTRAINTS")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ7.")
    print("\nKey soil and site characteristics evaluated:")
    print("  Soil factors:")
    print("    - Soil texture and consistence")
    print("    - Soil structure and aggregation")
    print("    - Soil moisture regime")
    print("\n  Site factors:")
    print("    - Surface stoniness and rock outcrops")
    print("    - Slope gradient and terrain")
    print("    - Soil depth and rooting restrictions")
    print("\n  Climate factors:")
    print("    - Climatic working days per year")
    print("    - Equipment trafficability")
    print("\nRating classes: Very High, High, Medium, Low, Very Low")
    print("\nFor complete documentation, see the detailed text above.")
