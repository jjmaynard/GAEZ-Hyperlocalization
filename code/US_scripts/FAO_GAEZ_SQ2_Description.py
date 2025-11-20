"""
FAO GAEZ SQ2: NUTRIENT RETENTION CAPACITY - DETAILED DESCRIPTION
=================================================================

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
SQ2: NUTRIENT RETENTION CAPACITY

SQ2 represents the soil's ability to retain and store nutrients against losses 
through leaching and other processes. This soil quality indicator reflects the 
soil's capacity to hold nutrients in forms accessible to plant roots and prevent 
their displacement beyond the root zone by percolating water.

POSITION IN GAEZ FRAMEWORK:
SQ2 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability
- SQ2: Nutrient retention capacity (focus of this document)
- SQ3: Rooting conditions
- SQ4: Oxygen availability to roots
- SQ5: Excess salts
- SQ6: Toxicity
- SQ7: Workability/field management constraints
"""

# ============================================================================
# CONCEPTUAL BASIS
# ============================================================================

"""
FUNDAMENTAL CONCEPT:

Nutrient retention capacity is the soil's ability to hold nutrients against 
leaching and loss processes. This property is crucial because:

1. Prevents nutrient losses to groundwater (environmental concern)
2. Maintains nutrients in the root zone for plant uptake
3. Improves fertilizer use efficiency
4. Reduces frequency of fertilizer applications
5. Buffers against nutrient deficiencies between applications
6. Protects water quality from nutrient pollution

The retention mechanism operates primarily through:
- Cation exchange capacity (CEC) for positively charged nutrients
- Anion exchange capacity (AEC) for negatively charged nutrients
- Physical adsorption on soil particle surfaces
- Chemical precipitation and complexation
- Organic matter binding and chelation

AGRICULTURAL RELEVANCE:

For all farming systems:
- Determines fertilizer management strategies
- Affects timing and frequency of nutrient applications
- Influences susceptibility to nutrient losses
- Critical for environmental stewardship
- Impacts economic efficiency of fertilizer use

Particularly important when:
- High rainfall or irrigation causes deep percolation
- Sandy soils with inherently low retention
- Intensive cropping with high nutrient removal
- Applying soluble fertilizers
- Managing mobile nutrients (N, S)
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ2 DIAGNOSTIC CHARACTERISTICS:

The assessment of nutrient retention capacity focuses on soil properties that 
determine the soil's ability to hold nutrients against leaching and loss. 
These characteristics are evaluated separately for topsoil and subsoil layers.

-------------------
TOPSOIL (0-30 cm)
-------------------

1. CATION EXCHANGE CAPACITY (CEC)
   
   Definition: The total quantity of exchangeable cations that a soil can 
   adsorb and hold, expressed in cmol(+)/kg or meq/100g.
   
   Role in nutrient retention:
   - Primary mechanism for retaining cationic nutrients (Ca2+, Mg2+, K+, NH4+)
   - Prevents leaching of essential cations below root zone
   - Provides buffering capacity against pH changes
   - Reflects both clay mineralogy and organic matter content
   - Determines fertilizer holding capacity
   
   CEC sources:
   - Clay minerals:
     * Montmorillonite (smectite): 80-150 cmol(+)/kg
     * Vermiculite: 100-150 cmol(+)/kg
     * Illite: 10-40 cmol(+)/kg
     * Kaolinite: 3-15 cmol(+)/kg
     * Chlorite: 10-40 cmol(+)/kg
   
   - Organic matter: 200-400 cmol(+)/kg
   
   - Amorphous materials (allophane): 25-70 cmol(+)/kg
   
   Typical ranges (cmol(+)/kg):
   - Very low: <6
   - Low: 6-12
   - Moderate: 12-25
   - High: 25-40
   - Very high: >40
   
   Interpretation: Higher CEC provides greater nutrient storage capacity and 
   better retention against leaching. However, very high CEC may indicate 
   difficult-to-manage heavy clay soils.


2. SOIL TEXTURE AND CLAY CONTENT
   
   Definition: The relative proportions of sand, silt, and clay particles, 
   with special emphasis on clay content and type.
   
   Role in nutrient retention:
   - Clay particles provide the primary CEC sites
   - Clay content correlates strongly with retention capacity
   - Clay type determines CEC magnitude
   - Structure affects water movement and leaching potential
   
   Texture classes and retention:
   
   Coarse (sandy) textures:
   - Low clay content (<15%)
   - Low CEC (typically <10 cmol(+)/kg)
   - High leaching potential
   - Rapid water percolation
   - Limited nutrient storage
   - Requires frequent, small fertilizer applications
   
   Medium (loamy) textures:
   - Moderate clay content (15-35%)
   - Moderate CEC (10-25 cmol(+)/kg)
   - Balanced retention and drainage
   - Good nutrient storage
   - Moderate leaching risk
   - Efficient fertilizer use
   
   Fine (clayey) textures:
   - High clay content (35-60%)
   - High CEC (>25 cmol(+)/kg)
   - Excellent retention capacity
   - Slow water percolation
   - High nutrient storage
   - Less frequent fertilizer needs
   
   Very fine (heavy clay) textures:
   - Very high clay content (>60%)
   - Very high CEC (>40 cmol(+)/kg)
   - Extremely high retention
   - Very slow drainage
   - Can have nutrient availability issues despite retention
   - Management challenges
   
   Critical consideration: Not all clays are equal - clay mineralogy matters 
   as much as clay quantity for determining actual CEC and retention capacity.


3. ORGANIC CARBON (OC)
   
   Definition: The carbon content of soil organic matter, expressed as 
   percentage of soil mass.
   
   Role in nutrient retention:
   - Major contributor to CEC (200-400 cmol(+)/kg)
   - Chelates metal cations (Fe3+, Cu2+, Zn2+, Mn2+)
   - Forms organo-mineral complexes that retain nutrients
   - Binds phosphorus in organic forms
   - Creates stable aggregates that reduce leaching
   - pH-dependent charge increases retention at higher pH
   
   Organic matter effects on retention:
   
   At low pH (4.0-5.5):
   - Reduced negative charge on organic matter
   - Lower CEC contribution
   - Still provides chelation sites
   - Buffering capacity important
   
   At neutral pH (6.5-7.5):
   - Maximum negative charge expression
   - Highest CEC contribution
   - Optimal chelation and complexation
   - Strong nutrient binding
   
   At high pH (>8.0):
   - Continued high charge
   - Competition with carbonate minerals
   - Still important for micronutrient retention
   
   Typical ranges and retention effects:
   - Very low (<0.5% OC): Minimal organic CEC contribution
   - Low (0.5-1.0% OC): Limited organic retention enhancement
   - Moderate (1.0-2.0% OC): Significant retention improvement
   - High (2.0-4.0% OC): Major retention capacity
   - Very high (>4.0% OC): Dominant retention mechanism
   
   Critical insight: In sandy soils, organic matter may be the primary 
   source of CEC and retention capacity. Loss of organic matter in such 
   soils severely compromises nutrient retention.


4. BASE SATURATION
   
   Definition: The percentage of CEC occupied by basic cations (Ca2+, Mg2+, 
   K+, Na+) rather than acidic cations (H+, Al3+).
   
   Role in nutrient retention:
   - Indicates current saturation of exchange sites
   - Affects availability of retained nutrients
   - Influences leaching vulnerability
   - Relates to buffering capacity
   - Determines liming requirements
   
   Base saturation ranges:
   
   Very low (<20%):
   - Exchange complex dominated by H+ and Al3+
   - Very acid conditions
   - Aluminum toxicity likely
   - Basic cations easily leached
   - Low retention of applied cations initially
   - High liming requirement
   
   Low (20-35%):
   - Acid soil conditions
   - Exchange sites largely occupied by H+ and Al3+
   - Risk of Al toxicity
   - Moderate cation retention once sites filled
   - Liming beneficial
   
   Moderate (35-50%):
   - Slightly acid to neutral pH
   - Good balance of exchange site occupancy
   - Adequate cation retention
   - Reasonable buffering capacity
   - May benefit from lime or not
   
   High (50-80%):
   - Neutral to slightly alkaline pH
   - Exchange sites well-occupied by basic cations
   - Excellent cation retention
   - Good buffering capacity
   - Liming usually not needed
   
   Very high (>80%):
   - Alkaline pH conditions
   - May indicate calcareous soils
   - Very high base cation retention
   - Potential micronutrient deficiency issues
   - No liming needed; may need acidification
   
   Management interpretation: Base saturation affects how quickly applied 
   nutrients are retained vs. leached. Low base saturation soils initially 
   retain nutrients poorly until exchange sites are saturated.


----------------------
SUBSOIL (30-100 cm)
----------------------

The subsoil characteristics are critical because:
- Deep-rooted crops access subsoil nutrients
- Leached nutrients from topsoil accumulate here
- Subsoil acts as safety net against nutrient losses
- Root zone storage capacity includes subsoil
- Many nutrients are retained more strongly in subsoil

1. CATION EXCHANGE CAPACITY (CEC)
   
   Typically lower than topsoil due to:
   - Lower organic carbon content
   - Often higher clay content but fewer active surfaces
   - Less biological activity
   - Reduced weathering in some profiles
   
   Subsoil CEC importance:
   - Captures nutrients leaching from topsoil
   - Provides additional nutrient reservoir
   - Deep roots can access retained nutrients
   - Extends effective rooting zone
   - Reduces groundwater contamination
   
   Evaluation considerations:
   - Compare topsoil to subsoil CEC gradient
   - Steep decline indicates poor subsurface retention
   - Similar or increasing CEC suggests good deep retention
   - Clay accumulation (argillic) horizons may have high subsoil CEC


2. SOIL TEXTURE AND CLAY CONTENT
   
   Subsoil texture often differs from topsoil:
   - May have clay accumulation (Bt horizons)
   - Can be sandier if topsoil deposited over sand
   - May show weathering differences
   - Structure often more massive than topsoil
   
   Importance for retention:
   - Clay-enriched subsoils provide excellent nutrient storage
   - Sandy subsoils create leaching pathway
   - Texture transitions affect water and nutrient movement
   - Restricting layers can cause perched retention zones
   
   Profile patterns:
   
   Uniform profile:
   - Similar retention throughout root zone
   - Predictable nutrient behavior
   - Relatively simple management
   
   Texture-contrast profile:
   - Abrupt changes affect retention
   - Finer subsoil improves retention
   - Coarser subsoil increases leaching risk
   - May cause perched water tables
   
   Gradual transition:
   - Progressive change with depth
   - Clay increase common in older soils
   - Generally favorable for retention
   - Extended effective root zone


3. BASE SATURATION
   
   Subsoil base saturation often differs from topsoil:
   - May be lower if acids leach downward
   - May be higher if bases accumulate
   - Important for deep rooting crops
   - Indicates effectiveness as nutrient reservoir
   
   Interpretation:
   - High subsoil base saturation = good nutrient storage
   - Low subsoil base saturation = continued leaching risk
   - Increasing with depth = effective retention zone
   - Decreasing with depth = poor retention profile


4. CALCIUM CARBONATE (CaCO3)
   
   Definition: The presence and quantity of calcium carbonate, indicating 
   calcareous soil conditions.
   
   Role in nutrient retention:
   - Provides buffering capacity
   - Maintains high pH
   - Contributes to calcium supply
   - Can fix phosphorus
   - Affects micronutrient retention (may reduce availability)
   
   Calcareous soil retention characteristics:
   - High retention of cations
   - Phosphorus fixation by calcium
   - Reduced availability of Fe, Mn, Zn
   - Anion retention generally low
   - pH buffered above 7.5
"""

# ============================================================================
# RATING SYSTEM
# ============================================================================

"""
SQ2 RATING SCALE:

Soils are rated on a 0-100 scale based on their nutrient retention capacity:

0-100 SCALE INTERPRETATION:
- 80-100: Very High retention capacity
- 60-79:  High retention capacity
- 40-59:  Medium retention capacity
- 20-39:  Low retention capacity
- 0-19:   Very Low retention capacity


VERY HIGH RETENTION (80-100):

Soil characteristics:
- High to very high CEC (>25 cmol(+)/kg)
- High clay content (>35%) with high-activity clays
- High organic matter (>3%)
- Base saturation >50%
- Fine to very fine texture throughout profile

Nutrient retention properties:
- Minimal leaching losses
- Excellent fertilizer use efficiency
- Nutrients retained through heavy rainfall
- Extended residual effects of applications
- Low risk of groundwater contamination

Management implications:
- Can apply larger, less frequent fertilizer doses
- High rates safely retained
- Slow-release fertilizers less critical
- Timing of application more flexible
- Excellent for organic amendments retention
- May need to monitor for nutrient accumulation

Suitable for:
- Intensive cropping systems
- High-value crops with large nutrient needs
- Areas with high rainfall or irrigation
- Situations requiring environmental protection
- Organic farming with amendment-based nutrition

Potential limitations:
- Very high retention may limit availability
- Heavy clays may have workability issues
- High pH/carbonates may affect micronutrients


HIGH RETENTION (60-79):

Soil characteristics:
- Moderate to high CEC (15-25 cmol(+)/kg)
- Moderate clay content (25-35%) or adequate organic matter
- Medium to fine texture
- Base saturation 40-60%
- Relatively uniform retention in root zone

Nutrient retention properties:
- Good protection against leaching
- Efficient fertilizer use
- Moderate residual effects
- Reasonable protection during heavy rain
- Low to moderate groundwater risk

Management implications:
- Standard fertilizer management practices work well
- Moderate application rates appropriate
- Some flexibility in timing
- Split applications beneficial but not critical
- Good response to organic amendments
- Generally efficient nutrient use

Suitable for:
- Most agricultural crops
- Diverse cropping systems
- Areas with moderate to high rainfall
- Sustainable agriculture practices
- Balanced input systems

Common soil types:
- Loam to clay loam topsoils
- Soils with moderate organic matter
- Many agricultural mollisols and alfisols


MEDIUM RETENTION (40-59):

Soil characteristics:
- Moderate CEC (10-15 cmol(+)/kg)
- Moderate clay content (15-25%) with low-activity clays
- Low to moderate organic matter (1-2%)
- Base saturation 30-50%
- Sandy loam to loam textures
- May have sandy or lighter subsoil

Nutrient retention properties:
- Moderate leaching risk
- Some nutrient losses in high rainfall
- Limited residual effects
- Fertilizer efficiency variable
- Moderate groundwater contamination risk

Management implications:
- Requires careful fertilizer management
- Split applications recommended
- Timing critical to match crop uptake
- Slow-release fertilizers beneficial
- Organic matter management important
- Monitor for leaching losses
- Irrigation management affects retention

Suitable for:
- Crops with moderate nutrient requirements
- Areas with well-distributed rainfall
- Systems with careful nutrient management
- Situations where monitoring is possible

Management priorities:
- Build organic matter to improve retention
- Use split applications
- Match timing to crop demand
- Consider slow-release or coated fertilizers
- Prevent over-application


LOW RETENTION (20-39):

Soil characteristics:
- Low CEC (5-10 cmol(+)/kg)
- Low clay content (<15%)
- Low organic matter (<1%)
- Sandy to sandy loam texture
- Base saturation variable
- Often sandy throughout profile

Nutrient retention properties:
- High leaching risk
- Rapid nutrient losses with rainfall
- Short residual effects
- Poor fertilizer efficiency
- High groundwater contamination risk
- Mobile nutrients especially vulnerable

Management implications:
- Requires intensive management
- Multiple small applications necessary
- Precise timing essential
- Slow-release fertilizers highly beneficial
- Organic matter critical but difficult to maintain
- Fertigation ideal if available
- Environmental risk management important

Suitable for:
- Drought-tolerant crops with low requirements
- Controlled irrigation systems
- Specialty crops with intensive management
- Situations with frequent fertilizer access

Management strategies:
- Light, frequent applications
- Foliar nutrition supplementation
- Fertigation through irrigation
- Polymer-coated fertilizers
- Cover crops to prevent leaching
- Green manures for nutrient cycling


VERY LOW RETENTION (0-19):

Soil characteristics:
- Very low CEC (<5 cmol(+)/kg)
- Very low clay content (<10%)
- Very low organic matter (<0.5%)
- Sand to loamy sand texture
- Often sandy throughout deep profile
- May be highly weathered oxisols/ultisols

Nutrient retention properties:
- Extreme leaching risk
- Very rapid nutrient losses
- Minimal residual effects
- Very poor fertilizer efficiency
- Severe groundwater contamination risk
- Nearly all nutrients mobile

Management implications:
- Extremely intensive management required
- Very frequent, small applications needed
- Conventional fertilizers largely ineffective
- Slow-release or controlled-release essential
- Fertigation strongly recommended
- High economic and environmental cost
- May not be economically viable for many crops

Suitable for:
- Very limited crop options
- Only with sophisticated irrigation/fertigation
- Highly specialized production systems
- May be better suited to forestry or conservation

Limitations:
- High fertilizer costs
- High labor/management requirements
- Environmental risk if not managed expertly
- Limited crop suitability
- May require soil modification

Improvement options:
- Clay addition (expensive)
- Massive organic matter additions
- Permanent cover/mulch systems
- Shift to less intensive land use
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
APPROACH TO RATING SQ2:

The rating methodology integrates multiple soil properties using both 
"most limiting factor" and "weighted average" approaches:

1. PRIMARY RATING FACTORS:
   
   Cation Exchange Capacity (CEC):
   - Single most important parameter
   - Weighted 50-60% of total rating
   - Evaluated separately for topsoil and subsoil
   - Non-linear rating curves based on CEC ranges
   
   Soil Texture/Clay Content:
   - Weighted 25-35% of total rating
   - Correlated with but independent of CEC
   - Considers particle size distribution
   - Evaluates profile texture uniformity
   
   Organic Carbon:
   - Weighted 10-20% of total rating
   - More important in sandy soils
   - Considered for CEC contribution
   - Quality and stability matter


2. MODIFIER FACTORS:
   
   Base Saturation:
   - Modifies retention effectiveness
   - Very low BS (<20%) reduces rating
   - Affects buffer capacity consideration
   
   Profile Characteristics:
   - Texture-contrast effects
   - Presence of restrictive layers
   - Clay accumulation zones
   - Carbonate accumulation


3. PROFILE INTEGRATION:
   
   Topsoil vs. Subsoil weighting:
   - Topsoil (0-30 cm): 60-70% of rating
   - Subsoil (30-100 cm): 30-40% of rating
   
   Rationale:
   - Most root activity in topsoil
   - Most nutrient cycling in topsoil
   - Subsoil provides safety net
   - Deep roots access subsoil


4. MOST LIMITING FACTOR CONSIDERATION:
   
   Applied when:
   - One characteristic is severely limiting
   - Sandy texture throughout profile
   - Very low CEC despite other factors
   - Extreme base saturation (very low or very high)
   
   Effect:
   - Single severe limitation caps overall rating
   - Prevents averaging from masking critical constraint
   - More important in SQ2 than in SQ1


5. RATING ADJUSTMENTS:
   
   Climate considerations:
   - Higher rainfall areas weight retention more heavily
   - Arid areas reduce importance of retention
   - Irrigation intensity affects rating interpretation
   
   Crop considerations:
   - Deep-rooted crops value subsoil retention more
   - Crops with low requirements less affected by retention
   - High-value crops justify management of low retention
   
   Management level:
   - High-input systems can partially overcome low retention
   - Low-input systems critically dependent on retention
   - Fertigation systems reduce retention importance


6. SPECIAL CASES:
   
   Organic soils (Histosols):
   - Very high CEC from organic matter
   - Rated separately from mineral soils
   - Different management implications
   
   Volcanic soils (Andisols):
   - Variable charge clays (allophane)
   - High CEC but unique behavior
   - Phosphorus fixation issues
   
   Highly weathered soils (Oxisols/Ultisols):
   - Low CEC despite high clay content
   - Low-activity clays (kaolinite, iron oxides)
   - Require special rating considerations
"""

# ============================================================================
# CROP-SPECIFIC RESPONSES
# ============================================================================

"""
CROP RESPONSE TO SQ2 CLASSES:

Different crops respond variably to nutrient retention capacity based on their 
rooting depth, nutrient requirements, and growth duration.

VERY HIGH RETENTION (80-100):

Most suitable for:
- Rice (intensive flooded systems)
- Sugarcane (high nutrient removal)
- Banana/plantain (continuous uptake)
- Intensive vegetables (high turnover)
- Forage grasses (frequent harvest)

Good for:
- Maize (high nutrient use)
- Cotton (extended season)
- Potato (moderate requirements)
- Most field crops

May need adjustments:
- Crops sensitive to heavy clay (root crops may have poor shape)
- Micronutrient-demanding crops if pH very high


HIGH RETENTION (60-79):

Excellent for:
- Wheat and small grains
- Maize and sorghum
- Soybeans and pulses
- Cotton
- Most vegetables
- Temperate fruit trees

Generally suitable for:
- Nearly all field crops
- Most tree crops
- Intensive systems
- Organic production


MEDIUM RETENTION (40-59):

Suitable with good management:
- Wheat and small grains
- Grain legumes
- Maize (with split applications)
- Vegetables (with frequent fertilization)
- Annual crops generally

Requires careful management:
- Deep-rooted perennials
- High nutrient-demanding crops
- Crops with long growing seasons

May be marginal for:
- Crops under high leaching conditions
- Very high nutrient-demanding crops without intensive management


LOW RETENTION (20-39):

Limited suitability:
- Short-season crops with low requirements
- Crops with efficient nutrient uptake
- Drought-tolerant species
- Crops suited to sandy soils

Requires intensive management:
- Most cereals (with fertigation)
- Vegetables (with frequent light applications)
- Fruits with drip irrigation/fertigation

Generally unsuitable:
- High nutrient-demanding crops without fertigation
- Perennial crops with simple management
- Crops in high rainfall without sophisticated management


VERY LOW RETENTION (0-19):

Very limited options:
- Only with fertigation systems
- Specialized production (e.g., greenhouse-style field culture)
- Very low nutrient demand crops

Generally unsuitable:
- Most commercial field crops
- Conventional production systems
- Low to moderate input agriculture

May be suitable for:
- Pine plantations
- Some native vegetation restoration
- Very low-input extensive grazing
"""

# ============================================================================
# MANAGEMENT STRATEGIES BY SQ2 CLASS
# ============================================================================

"""
MANAGEMENT APPROACHES FOR DIFFERENT SQ2 RATINGS:

VERY HIGH RETENTION (80-100):

Fertilizer management:
- Can use larger, less frequent applications
- Standard or high analysis fertilizers effective
- Split applications beneficial but not critical
- Broadcast or banded application both work
- Pre-plant applications have good residual effect

Advantages:
- Flexibility in application timing
- Reduced application frequency
- Good fertilizer efficiency
- Lower labor/equipment costs
- Environmental safety buffer

Considerations:
- Monitor for nutrient accumulation over time
- Heavy clay may have other management issues
- Very high pH may affect micronutrient availability


HIGH RETENTION (60-79):

Fertilizer management:
- Standard agricultural fertilizer practices
- 2-3 split applications for most crops
- Conventional fertilizer formulations
- Pre-plant + top-dress programs work well
- Residual fertility can be managed

Best practices:
- Match application to crop demand patterns
- Use soil and plant tissue testing
- Maintain organic matter
- Standard precision agriculture techniques


MEDIUM RETENTION (40-59):

Fertilizer management:
- Multiple split applications (3-4 or more)
- Timing critical - match crop uptake
- Consider slow-release fertilizers
- Avoid large single applications
- Top-dress applications important

Strategies to improve efficiency:
- Build organic matter content
- Use cover crops between cash crops
- Apply mulches to reduce leaching
- Time applications before crop demand peaks
- Use nitrification inhibitors for nitrogen
- Consider fertigation if irrigation available

Environmental protection:
- Buffer strips near water bodies
- Avoid application before heavy rain
- Monitor groundwater if vulnerable area
- Use appropriate buffer zones


LOW RETENTION (20-39):

Fertilizer management:
- Frequent small applications (weekly to biweekly)
- Slow-release or coated fertilizers highly beneficial
- Foliar fertilization to supplement
- Fertigation ideal if possible
- Avoid single large applications

Essential practices:
- Intensive organic matter management
- Cover crops when field not in production
- Deep-rooted cover crops to capture leached nutrients
- Perennial ground covers in tree crops
- Mulching to reduce leaching
- Precision timing of applications

Technology aids:
- Soil moisture monitoring for leaching prediction
- Split application equipment
- Drip irrigation with injection capability
- Leaf tissue testing for deficiency detection

Economic considerations:
- Higher fertilizer costs per unit crop production
- Increased labor and equipment costs
- May not be viable for low-value crops
- Calculate fertilizer efficiency carefully


VERY LOW RETENTION (0-19):

Fertilizer management:
- Very frequent applications (2-3 times per week)
- Controlled-release fertilizers essential
- Fertigation strongly recommended or required
- Foliar applications important
- Conventional fertilizers largely ineffective

Critical practices:
- Continuous organic matter addition
- Permanent mulch or cover systems
- May require physical soil modification
- Consider raised beds with imported soil
- Intensive monitoring systems

Technology requirements:
- Automated irrigation/fertigation systems
- Real-time soil moisture monitoring
- Frequent tissue testing
- Weather monitoring for rainfall

Viability assessment:
- Calculate break-even fertilizer costs
- May only be viable for very high-value crops
- Consider alternative land uses
- Evaluate long-term soil improvement potential


GENERAL STRATEGIES ACROSS ALL CLASSES:

1. Organic matter management:
   - Critical for improving retention at any level
   - More important in low-retention soils
   - Compost, manures, crop residues
   - Cover crops and green manures

2. Precision agriculture:
   - Variable rate application based on SQ2 zones
   - Targeted management by soil class
   - Optimize inputs to soil capacity

3. Conservation practices:
   - Reduced tillage preserves structure and OM
   - Cover crops prevent leaching losses
   - Contour farming reduces runoff
   - Buffer strips protect water quality

4. Monitoring and adjustment:
   - Regular soil testing
   - Plant tissue analysis
   - Adapt management to results
   - Track fertilizer efficiency
"""

# ============================================================================
# INTERACTIONS WITH OTHER SOIL QUALITIES
# ============================================================================

"""
SQ2 INTERACTIONS WITH OTHER GAEZ INDICATORS:

SQ2 ↔ SQ1 (Nutrient Availability):
- High SQ2 helps maintain high SQ1 over time
- Low SQ2 requires higher SQ1 to start (reserves leach rapidly)
- SQ2 determines how long applied nutrients remain available
- Together determine fertilizer requirements
- SQ1 addresses "how much"; SQ2 addresses "how long"

SQ2 ↔ SQ3 (Rooting Conditions):
- Deep rooting allows access to nutrients retained in subsoil
- Poor rooting negates benefits of subsoil retention
- Deep roots can retrieve leached nutrients
- Texture-contrast issues affect both SQ2 and SQ3
- Compacted layers affect both rooting and retention

SQ2 ↔ SQ4 (Oxygen Availability):
- Waterlogging in high-retention soils can cause:
  * Denitrification (N losses despite retention)
  * Reduction and mobilization of retained Fe, Mn
  * Nutrient form changes
- Poor drainage affects both oxygen and retention
- Heavy clays may have both high SQ2 and low SQ4

SQ2 ↔ SQ5 (Excess Salts):
- High salinity increases nutrient retention through:
  * High ionic strength
  * Competition for exchange sites
- But reduces nutrient availability to plants
- Leaching salts also leaches nutrients (trade-off)
- Good retention helps prevent salinization

SQ2 ↔ SQ6 (Toxicity):
- High retention can hold toxic elements (Al, heavy metals)
- Carbonate accumulation affects both SQ2 and SQ6
- pH effects common to both indicators
- Retention of toxins may be beneficial (prevents movement)

SQ2 ↔ SQ7 (Workability):
- High clay content increases both retention and workability problems
- Sandy soils have both low retention and good workability
- Management of high-retention soils may be constrained
- Application timing affected by workability
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ2:

1. Static assessment:
   - SQ2 represents inherent retention capacity
   - Doesn't model dynamic nutrient movement
   - Actual leaching depends on rainfall, irrigation, ET
   - Seasonal variations not captured

2. Anion retention not fully addressed:
   - Focus primarily on cation retention (CEC)
   - Anion exchange capacity (AEC) rarely measured
   - Phosphate fixation mechanisms simplified
   - Nitrate and sulfate leaching not explicitly modeled

3. Clay mineralogy details:
   - Specific clay minerals not always identified
   - CEC assumed from texture in many datasets
   - High clay doesn't always mean high CEC (kaolinitic soils)
   - Volcanic soils have unique retention properties

4. Organic matter quality:
   - Total OC measured, not stability or quality
   - Labile vs. stable OM not differentiated
   - Charcoal/biochar not separately considered
   - Decomposition rates not factored

5. Management effects not included:
   - Previous fertilization affects current retention behavior
   - Compaction impacts retention and movement
   - Tillage effects on structure and retention
   - Long-term trends from management not captured

6. Scale limitations:
   - Spatial variability within mapping units
   - Point measurements represent larger areas
   - Field-scale variation not captured
   - Local retention can differ from map values

7. Mobile nutrient focus:
   - Retention evaluation emphasizes leachable nutrients
   - Less relevant for immobile nutrients (P in many soils)
   - Nitrogen leaching most critical concern
   - Other nutrients may behave differently

8. Climate context needed:
   - Retention importance varies with rainfall
   - Irrigation affects interpretation
   - Temperature affects mineralization and demand
   - Must interpret SQ2 with climate data

RECOMMENDED USES:

Best for:
- Screening areas for leaching risk
- Planning fertilizer management strategies
- Environmental risk assessment
- Identifying soils needing special management
- Regional agricultural planning

Should be supplemented with:
- Local rainfall and climate data
- Irrigation water quality and quantity
- Specific crop nutrient requirements
- Economic analysis of management options
- Environmental regulations and guidelines
- Site-specific soil testing
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on regional and national soil surveys
- Integrates multiple classification systems

Soil property data quality:
- CEC measurements variable in quality
- Often estimated from texture and OM
- Clay mineralogy data limited in many regions
- Base saturation data incomplete in some areas

CALCULATION DETAILS:

Rating functions:
- Non-linear relationships for CEC and retention
- Texture-based adjustments to CEC ratings
- Organic matter contributions weighted by stability
- Profile integration considers depth and root access

Weighting schemes:
- CEC: 50-60% of rating
- Texture/Clay: 25-35% of rating
- Organic Carbon: 10-20% of rating
- Topsoil: 60-70% of final rating
- Subsoil: 30-40% of final rating

(Note: Exact formulas are proprietary to GAEZ methodology)

OUTPUT FORMATS:
- Raster grids at multiple resolutions
- Vector polygons with soil attributes
- Tabular summaries by administrative unit
- Integration with other GAEZ indicators
- Crop-specific suitability maps

VALIDATION:
- Compared with fertilizer loss studies
- Calibrated against leaching experiments
- Cross-referenced with water quality data
- Expert review by soil scientists
- Updated with new research findings
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

RELATED TECHNICAL REFERENCES:

Brady, N.C. and R.R. Weil. 2016. The Nature and Properties of Soils, 15th Edition. 
Pearson Education, Upper Saddle River, NJ.

Sposito, G. 2008. The Chemistry of Soils, 2nd Edition. 
Oxford University Press, Oxford, UK.

Tan, K.H. 2010. Principles of Soil Chemistry, 4th Edition. 
CRC Press, Boca Raton, FL.

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- Land evaluation guidelines: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/

NUTRIENT MANAGEMENT RESOURCES:

Snyder, C.S., T.W. Bruulsema, T.L. Jensen, and P.E. Fixen. 2009. 
Review of greenhouse gas emissions from crop production systems and fertilizer management effects. 
Agriculture, Ecosystems & Environment, 133(3-4): 247-266.

Roberts, T.L. 2007. Right product, right rate, right time and right place... 
the foundation of best management practices for fertilizer. 
IFA International Workshop on Fertilizer Best Management Practices, Brussels, Belgium.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ2 assesses the soil's capacity to retain nutrients against leaching
2. Critical for fertilizer efficiency and environmental protection
3. Based primarily on CEC, clay content, and organic matter
4. Evaluated separately for topsoil and subsoil
5. Rated on 0-100 scale, classified into 5 categories
6. Determines fertilizer management strategy requirements
7. More important in high rainfall/irrigation areas
8. Low retention requires intensive, specialized management
9. Interacts with other soil qualities, especially SQ1
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ2 provides essential information for:
- Designing fertilizer management programs
- Assessing environmental risks from nutrient leaching
- Determining economic viability of different cropping systems
- Planning soil improvement strategies
- Protecting groundwater quality

Understanding SQ2 is crucial for sustainable agriculture that balances 
productivity, economic efficiency, and environmental stewardship.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ2: NUTRIENT RETENTION CAPACITY")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ2.")
    print("\nKey soil characteristics evaluated:")
    print("  Topsoil (0-30 cm):")
    print("    - Cation exchange capacity (CEC)")
    print("    - Soil texture and clay content")
    print("    - Organic carbon content")
    print("    - Base saturation")
    print("\n  Subsoil (30-100 cm):")
    print("    - Cation exchange capacity (CEC)")
    print("    - Soil texture and clay content")
    print("    - Base saturation")
    print("    - Calcium carbonate (CaCO3)")
    print("\nRating classes: Very High, High, Medium, Low, Very Low")
    print("\nFor complete documentation, see the detailed text above.")
