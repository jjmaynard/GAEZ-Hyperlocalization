"""
FAO GAEZ SQ4: OXYGEN AVAILABILITY TO ROOTS - DETAILED DESCRIPTION
==================================================================

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
SQ4: OXYGEN AVAILABILITY TO ROOTS

SQ4 represents the soil's capacity to supply adequate oxygen to plant roots for 
respiration and normal metabolic function. This soil quality indicator assesses 
drainage conditions, aeration status, and the presence of oxygen-limiting conditions 
such as waterlogging, poor internal drainage, or impeded gas exchange.

POSITION IN GAEZ FRAMEWORK:
SQ4 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability
- SQ2: Nutrient retention capacity
- SQ3: Rooting conditions
- SQ4: Oxygen availability to roots (focus of this document)
- SQ5: Excess salts
- SQ6: Toxicity
- SQ7: Workability/field management constraints
"""

# ============================================================================
# CONCEPTUAL BASIS
# ============================================================================

"""
FUNDAMENTAL CONCEPT:

Oxygen availability in soil is critical because plant roots require oxygen for 
aerobic respiration to generate energy (ATP) for nutrient uptake, growth, and 
metabolic processes. Adequate soil aeration ensures:

1. Root respiration and energy production
2. Active nutrient uptake (especially N, P, K)
3. Root growth and elongation
4. Beneficial aerobic soil organisms
5. Nutrient transformations (nitrification)
6. Prevention of toxic compound accumulation
7. Maintenance of favorable soil chemistry

When oxygen is limited (anaerobic conditions):
- Root respiration is inhibited
- Energy production decreases drastically
- Nutrient uptake becomes passive and inefficient
- Root growth ceases or slows dramatically
- Toxic compounds accumulate (ethylene, organic acids, H2S, Fe2+, Mn2+)
- Denitrification causes nitrogen losses
- Methane production may occur
- Root diseases proliferate
- Plant stress increases, yields decline

AGRICULTURAL RELEVANCE:

For most crops (except rice and aquatic plants):
- Adequate oxygen is absolutely essential
- Even brief waterlogging can damage crops
- Chronic poor drainage severely limits productivity
- Seasonal flooding restricts crop selection
- Anaerobic conditions are highly detrimental

Critical periods:
- Germination (seeds need oxygen)
- Early growth stages
- Rapid growth periods (high oxygen demand)
- Flowering and grain fill
- Root development phases

Management implications:
- Drainage systems may be needed
- Crop selection must match drainage class
- Planting dates must avoid wet periods
- Field operations limited by wetness
- Irrigation management critical
- Raised beds may be beneficial

Environmental context:
- Natural wetlands have permanently poor drainage
- Floodplains have seasonal inundation
- High water tables limit root zones
- Perched water on restrictive layers
- Climate affects severity (humid vs. arid regions)
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ4 DIAGNOSTIC CHARACTERISTICS:

The assessment of oxygen availability focuses on soil properties that control 
water movement, drainage, aeration, and the duration/frequency of saturation.

----------------------
DRAINAGE ASSESSMENT
----------------------

Soil drainage is the most critical factor for oxygen availability. It integrates 
the effects of multiple soil properties and landscape position.


1. SOIL DRAINAGE CLASS
   
   Definition: The frequency and duration of periods when the soil is free of 
   saturation, based on natural conditions (before artificial drainage).
   
   Drainage classes (USDA/FAO system):
   
   EXCESSIVELY DRAINED:
   - Water removed very rapidly
   - Very porous soils (sands, gravels)
   - Steep slopes
   - No water table within profile
   - May be too dry rather than too wet
   - Excellent oxygen availability but drought-prone
   
   SOMEWHAT EXCESSIVELY DRAINED:
   - Water removed rapidly
   - Porous soils on slopes
   - Deep water table
   - No saturation problems
   - Excellent oxygen availability
   
   WELL DRAINED:
   - Water removed readily but not rapidly
   - Most root zone not saturated for significant periods
   - Water table generally deep (>100 cm)
   - May have brief saturation in lower subsoil
   - Optimal drainage for most crops
   - Excellent oxygen availability
   
   MODERATELY WELL DRAINED:
   - Water removed somewhat slowly
   - Briefly saturated in upper subsoil
   - May have water table at 50-100 cm for brief periods
   - Upper profile generally well aerated
   - Good oxygen availability except deep in profile
   - Suitable for most crops with minor limitations
   
   SOMEWHAT POORLY DRAINED:
   - Water removed slowly
   - Saturated at shallow depth for significant periods
   - Water table at 30-90 cm seasonally
   - Upper profile may be briefly saturated
   - Moderate oxygen limitations
   - Many crops have reduced yields
   - Drainage improvement often beneficial
   
   POORLY DRAINED:
   - Water removed very slowly
   - Saturated at or near surface for extended periods
   - Water table at 0-50 cm much of the year
   - Frequent surface saturation
   - Severe oxygen limitations
   - Major crop restrictions
   - Drainage essential for most crops
   
   VERY POORLY DRAINED:
   - Water removed so slowly that soil is saturated at or near surface 
     most of the year
   - Water table at or above surface much of time
   - Permanent or nearly permanent saturation
   - Very severe oxygen limitations
   - Natural wetland conditions
   - Only hydrophytic plants without drainage
   - May not be drainable

   Duration and timing matter:
   - Brief saturation: minimal damage
   - Prolonged saturation: severe damage
   - Saturation during critical growth stages: worst
   - Winter saturation: less damaging than growing season
   - Frequency: repeated brief saturations cumulative


2. DEPTH TO WATER TABLE
   
   Definition: The depth from soil surface to the saturated zone, varying 
   seasonally and with rainfall.
   
   Water table dynamics:
   
   Permanent (static) water table:
   - Present year-round
   - Depth varies seasonally but always present
   - Typical in low landscape positions
   - Limits rooting depth absolutely
   - Causes permanent reduced zone
   
   Perched water table:
   - Forms above restricting layer
   - Temporary, after rainfall or irrigation
   - May occur even with deep permanent table
   - Common with clay or hardpan layers
   - Can saturate upper profile while deep soil dry
   
   Seasonal water table:
   - Present only during wet season
   - Depth varies from at surface to deep
   - Typical in areas with seasonal rainfall
   - May allow crop growth in dry season
   - Restricts wet-season cropping
   
   Fluctuating water table:
   - Responds quickly to rainfall
   - May rise and fall repeatedly
   - Creates cycles of saturation/aeration
   - Difficult for plant adaptation
   - Causes repeated stress
   
   Water table depth implications:
   
   >150 cm (deep):
   - No effect on rooting or aeration
   - Excellent conditions
   
   100-150 cm:
   - Minor effect on deep-rooted crops
   - Generally satisfactory
   
   60-100 cm:
   - Limits rooting depth
   - Affects deep-rooted crops
   - May stress shallow-rooted crops if rises further
   
   30-60 cm:
   - Severe limitation for most crops
   - Restricts effective rooting zone
   - Oxygen stress likely
   - Only shallow-rooted or tolerant crops
   
   0-30 cm:
   - Extreme limitation
   - Very few crop options
   - May require drainage or special management
   - Suitable mainly for rice or wetland crops
   
   At or above surface:
   - Wetland conditions
   - Conventional crops impossible without drainage
   - Only aquatic/wetland plants


3. REDOXIMORPHIC FEATURES (Mottling and Gleying)
   
   Definition: Soil features resulting from repeated cycles of reduction and 
   oxidation due to saturation, indicating oxygen deprivation.
   
   Types of redoximorphic features:
   
   REDOX CONCENTRATIONS (Mottles):
   - Masses or nodules of accumulated iron/manganese oxides
   - Colors: red, reddish brown, yellowish brown, brown, black
   - Form in aerated microsites or during oxidized periods
   - Indicate fluctuating water table
   - Bright distinct colors indicate active redox processes
   
   REDOX DEPLETIONS:
   - Zones where iron/manganese removed
   - Colors: gray, light gray, white, olive
   - Form where reduced and mobilized during saturation
   - Indicate prolonged saturation
   - Extent and contrast indicate severity
   
   GLEY COLORS:
   - Reduced matrix colors: gray, bluish gray, greenish gray
   - Indicate permanent or prolonged saturation
   - Low chroma colors (0-2)
   - Result from ferrous iron (reduced)
   - Indicate very poor drainage
   
   Interpretation by depth and abundance:
   
   No redoximorphic features to 100+ cm:
   - Excellent drainage and aeration
   - No oxygen limitations
   
   Few faint mottles below 75 cm:
   - Very minor, brief saturation deep in profile
   - No practical limitation
   
   Common distinct mottles 50-75 cm:
   - Seasonal water table in this zone
   - Moderate limitation for deep-rooted crops
   
   Many prominent mottles 30-50 cm:
   - Frequent saturation at this depth
   - Significant oxygen limitation
   - Restricts many crops
   
   Dominant depletions/gley starting at 30 cm:
   - Prolonged saturation
   - Severe oxygen limitation
   - Major crop restrictions
   
   Gley matrix starting at surface or shallow depth:
   - Very poor drainage
   - Extreme oxygen limitation
   - Very limited crop suitability


4. SOIL PERMEABILITY AND HYDRAULIC CONDUCTIVITY
   
   Definition: The rate at which water moves through soil, determining how 
   quickly excess water drains away.
   
   Permeability classes:
   
   Very rapid (>15 cm/hr):
   - Very coarse sands, gravels
   - Water drains almost immediately
   - Excellent aeration
   - May be droughty
   
   Rapid (5-15 cm/hr):
   - Coarse sands
   - Quick drainage
   - Excellent aeration
   
   Moderately rapid (1.5-5 cm/hr):
   - Sandy loams, some loams
   - Good drainage
   - Good aeration
   
   Moderate (0.5-1.5 cm/hr):
   - Loams, silt loams
   - Adequate drainage
   - Good aeration if no restrictive layers
   
   Moderately slow (0.15-0.5 cm/hr):
   - Clay loams, some silty clay loams
   - Somewhat slow drainage
   - May have temporary saturation
   - Adequate aeration if internal drainage good
   
   Slow (0.05-0.15 cm/hr):
   - Clays, silty clays
   - Slow drainage
   - Prolonged saturation likely
   - Poor aeration potential
   
   Very slow (<0.05 cm/hr):
   - Heavy clays, compacted layers
   - Very slow drainage
   - Extended saturation
   - Poor aeration
   
   Restricting layers:
   - Drastically reduce permeability
   - Cause perched water tables
   - Create saturation above layer
   - Include: fragipans, claypans, hardpans, bedrock


5. SOIL TEXTURE AND STRUCTURE EFFECTS
   
   Texture influences drainage:
   
   Coarse textures (sands):
   - Large pores drain rapidly by gravity
   - Excellent drainage unless water table high
   - High permeability
   - Good aeration
   
   Medium textures (loams):
   - Balance of pore sizes
   - Moderate permeability
   - Good drainage if well-structured
   - Adequate aeration
   
   Fine textures (clays):
   - Small pores, slow drainage
   - Low permeability
   - Can have poor drainage
   - Aeration depends on structure
   
   Structure critical in fine-textured soils:
   
   Well-structured clays:
   - Aggregates create macropores
   - Water drains between peds
   - Can have good drainage despite clay
   - Good aeration along ped faces
   
   Massive clays:
   - No macropores
   - Very slow drainage
   - Poor aeration
   - Prone to saturation


6. LANDSCAPE POSITION AND TOPOGRAPHY
   
   Definition: Position in the landscape affects water accumulation and 
   drainage patterns.
   
   Landscape positions:
   
   Summits and ridges:
   - Shedding positions
   - Excellent drainage
   - No water accumulation
   - May be too dry
   
   Shoulders and backslopes:
   - Well drained
   - Water moves through and away
   - No accumulation
   - Good aeration
   
   Footslopes:
   - Receive seepage from upslope
   - May have springs or seeps
   - Can be poorly drained
   - Variable aeration
   
   Toeslopes:
   - Accumulate water
   - Often poorly drained
   - High water tables
   - Poor aeration common
   
   Depressions and basins:
   - Water accumulates
   - Poorly to very poorly drained
   - Ponding common
   - Poor aeration
   - Wetlands often form here
   
   Floodplains and terraces:
   - Variable drainage
   - Subject to flooding
   - Water tables often shallow
   - Seasonal saturation
   
   Slope gradient effects:
   
   >15%: Excessive to well drained
   8-15%: Well drained
   3-8%: Well to moderately well drained
   1-3%: Variable, depends on soil properties
   0-1%: Often poorly drained
   Depressional: Very poorly drained


7. FLOODING AND PONDING
   
   Definition: Temporary inundation by surface water from overflow of streams 
   or local accumulation.
   
   Flooding frequency classes:
   
   None: No flooding expected
   Rare: <1% chance annually
   Occasional: 1-5% chance annually
   Frequent: 5-50% chance annually
   Very frequent: >50% chance annually
   
   Flooding duration:
   
   Extremely brief: <2 hours
   Very brief: 2-7 hours
   Brief: 1-7 days
   Long: 7-30 days
   Very long: >30 days
   
   Ponding (local water accumulation):
   - No overflow from streams
   - Water collects in depressions
   - Must evaporate or infiltrate to drain
   - Can be prolonged in heavy soils
   
   Effects on oxygen availability:
   
   Brief occasional flooding:
   - Minor impact if during dormant season
   - Significant if during growing season
   
   Frequent or prolonged flooding:
   - Severe oxygen stress
   - Major crop limitations
   - Restricts planting dates
   - Limits crop choices
   
   Growing season vs. dormant season:
   - Growing season flooding most damaging
   - Dormant season flooding less critical
   - Timing relative to crop cycle crucial


8. ARTIFICIAL DRAINAGE SYSTEMS
   
   While SQ4 typically evaluates natural conditions, the presence or potential 
   for artificial drainage is relevant:
   
   Surface drainage:
   - Land smoothing
   - Bedding and furrows
   - Grassed waterways
   - Removes ponded water
   - Improves surface conditions
   
   Subsurface drainage:
   - Tile drains
   - Mole drains
   - Ditches and canals
   - Lowers water table
   - Improves internal drainage
   
   Drainage effectiveness:
   - Can convert poorly drained to moderately well drained
   - Expensive installation and maintenance
   - Not all soils drainable
   - May create environmental concerns
   - Requires outlet for water
"""

# ============================================================================
# RATING SYSTEM
# ============================================================================

"""
SQ4 RATING SCALE:

Soils are rated on a 0-100 scale based on oxygen availability to roots:

0-100 SCALE INTERPRETATION:
- 80-100: Very High - Excellent oxygen availability, no limitations
- 60-79:  High - Good oxygen availability, minor limitations
- 40-59:  Medium - Moderate oxygen availability, significant limitations
- 20-39:  Low - Poor oxygen availability, severe limitations
- 0-19:   Very Low - Very poor oxygen availability, extreme limitations


VERY HIGH (80-100): EXCELLENT OXYGEN AVAILABILITY

Soil characteristics:
- Well drained or moderately well drained
- Deep water table (>100 cm year-round)
- Moderate to rapid permeability
- No redoximorphic features above 75 cm
- No flooding or ponding
- Good soil structure
- Favorable landscape position (slopes, uplands)

Oxygen availability:
- Roots have continuous oxygen supply
- No saturation in active root zone
- Excellent gas exchange
- Aerobic conditions throughout profile
- No reduction reactions
- Optimal for aerobic organisms

Crop performance:
- All upland crops thrive
- No oxygen-related stress
- Maximum root development
- Efficient nutrient uptake
- No disease pressure from poor drainage
- Optimal yields achievable

Management implications:
- No drainage needed
- Normal field operations possible
- No restrictions on planting dates
- Flexible crop selection
- Standard management practices work
- May need irrigation in dry periods


HIGH (60-79): GOOD OXYGEN AVAILABILITY

Soil characteristics:
- Moderately well drained
- Seasonal water table 50-100 cm
- Moderate permeability
- Few to common redox features 50-100 cm
- No flooding, or rare brief flooding
- No ponding
- Generally favorable position

Oxygen availability:
- Adequate oxygen for most crops
- Brief or deep saturation only
- Minor oxygen stress possible deep in profile
- Good aeration in main root zone
- Generally aerobic conditions

Crop performance:
- Most upland crops do well
- Some deep-rooted crops may have minor limitations
- Very sensitive crops may show slight stress
- Generally high yields
- Occasional stress during wet periods

Management implications:
- Drainage usually not needed
- Field operations occasionally delayed
- Minor planting date restrictions
- Most crops suitable
- Consider surface drainage if ponding occurs
- Slightly increased disease risk in wet years


MEDIUM (40-59): MODERATE OXYGEN AVAILABILITY

Soil characteristics:
- Somewhat poorly drained
- Water table 30-90 cm seasonally
- Slow to moderately slow permeability
- Common to many redox features 30-60 cm
- Occasional flooding, or
- Brief ponding, or
- Perched water table common

Oxygen availability:
- Oxygen stress during wet periods
- Prolonged saturation in subsoil
- Brief saturation in topsoil possible
- Reduced zone present seasonally
- Alternating aerobic/anaerobic conditions
- Oxygen adequate only when well-drained periods

Crop performance:
- Moderate crop limitations
- Sensitive crops severely affected
- Tolerant crops grow satisfactorily
- Yield reductions common (10-30%)
- Planting dates critical
- Root diseases more common
- Crop selection important

Management implications:
- Drainage improvement beneficial
- Surface drainage often needed
- Field operations often delayed
- Restricted planting window
- Careful crop selection necessary
- Consider raised beds
- Increased management needed
- May need alternate wet/dry season crops


LOW (20-39): POOR OXYGEN AVAILABILITY

Soil characteristics:
- Poorly drained
- Water table 0-50 cm much of year
- Very slow permeability
- Many prominent redox features starting shallow (15-30 cm)
- Gley colors present
- Frequent flooding or prolonged ponding, or
- Water table at or near surface seasonally

Oxygen availability:
- Severe oxygen deficiency
- Prolonged saturation near surface
- Extended anaerobic conditions
- Brief aerated periods only
- Reduced zone dominant
- Toxic compounds accumulate

Crop performance:
- Severe crop limitations
- Only tolerant species suitable
- Major yield reductions (30-60%)
- Upland crops fail or severely stunted
- Root development restricted
- High disease incidence
- Crop options very limited

Management implications:
- Drainage essential for most crops
- Extensive drainage systems needed
- Field operations severely restricted
- Very limited planting windows
- Crop selection highly restricted
- Rice and wetland crops suitable
- Consider only wet-season crops
- May not be economically drainable
- Alternative uses may be more appropriate


VERY LOW (0-19): VERY POOR OXYGEN AVAILABILITY

Soil characteristics:
- Very poorly drained
- Water table at or above surface most of year
- Impermeable or nearly so
- Dominant gley matrix from surface
- Reduced colors throughout
- Very frequent flooding or permanent ponding, or
- Permanent saturation
- Natural wetland conditions

Oxygen availability:
- Essentially no oxygen in root zone
- Permanent or nearly permanent saturation
- Continuous anaerobic conditions
- Reduced environment dominant
- Toxic compound accumulation severe
- Only adapted hydrophytes survive

Crop suitability:
- Unsuitable for conventional crops
- Only true aquatic/wetland plants
- Rice possible if water controlled
- Upland crops impossible
- Natural wetland vegetation

Management reality:
- Drainage may not be feasible or permitted
- Environmental protection may prevent drainage
- Wetland designation likely
- Conventional agriculture not viable
- Consider wetland crops or conservation uses

Alternative uses:
- Natural wetland preservation
- Wildlife habitat
- Water quality functions
- Wetland rice in some regions
- Aquaculture potential
- Carbon sequestration
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
APPROACH TO RATING SQ4:

The rating methodology integrates multiple indicators of drainage and oxygen 
availability:

1. PRIMARY RATING FACTOR:

   Drainage Class:
   - Single most important indicator
   - Integrates multiple factors
   - Weighted 50-60% of total rating
   - Strong relationship to oxygen availability
   
   Drainage class rating scale:
   - Excessively drained: 95-100
   - Somewhat excessively drained: 90-95
   - Well drained: 85-95
   - Moderately well drained: 65-80
   - Somewhat poorly drained: 40-60
   - Poorly drained: 20-40
   - Very poorly drained: 0-20


2. MODIFIER FACTORS:

   Depth to Water Table:
   - Direct indicator of root zone saturation
   - Seasonal high water table used
   - Deeper table = higher rating
   - Perched tables reduce rating
   
   Redoximorphic Features:
   - Depth to first features
   - Abundance and contrast
   - Earlier and more prominent = lower rating
   
   Flooding Frequency and Duration:
   - Frequent flooding reduces rating
   - Long duration reduces rating more
   - Growing season timing most critical
   
   Ponding:
   - Reduces rating significantly
   - Duration matters
   - Frequency matters
   
   Permeability:
   - Affects drainage effectiveness
   - Very slow permeability reduces rating
   - Interacts with drainage class


3. PROFILE CONSIDERATIONS:

   Upper profile most critical (0-50 cm):
   - Where most root activity occurs
   - Brief saturation here severely damaging
   - Weighted heavily in rating
   
   Lower profile (50-100 cm):
   - Important for deep-rooted crops
   - Saturation here less immediately damaging
   - Still significant for rating


4. TEMPORAL FACTORS:

   Duration of saturation:
   - Brief (<7 days): minor impact
   - Moderate (1-4 weeks): significant impact
   - Prolonged (>1 month): severe impact
   - Permanent: extreme impact
   
   Frequency:
   - Rare: minimal impact
   - Occasional: moderate impact
   - Frequent: severe impact
   - Continuous: extreme impact
   
   Seasonal timing:
   - Dormant season saturation: less severe
   - Growing season saturation: most severe
   - Critical crop stages: worst timing


5. INTERACTION EFFECTS:

   Multiple limitations:
   - Poor drainage + shallow water table: severe
   - Poor drainage + frequent flooding: extreme
   - Slow permeability + low position: poor drainage
   - Restrictive layer + high rainfall: very poor drainage
   
   Compensating factors:
   - Artificial drainage improves rating (if present)
   - Favorable season timing reduces impact
   - Coarse texture improves drainage despite position


6. CLIMATE CONTEXT:

   Humid regions:
   - Drainage more critical
   - Saturation more frequent and prolonged
   - Weight SQ4 more heavily
   
   Arid regions:
   - Drainage less commonly limiting
   - May never saturate
   - Well-drained rating even in low positions
   - SQ4 less critical than water supply
   
   Monsoon climates:
   - Seasonal variation extreme
   - Wet season critical for drainage
   - Dry season may be well-drained
   - Dual season ratings useful


7. SPECIAL CASES:

   Rice paddies:
   - Poor drainage is beneficial
   - Rating system reversed
   - Very poorly drained best for flooded rice
   - But must drain for other crops
   
   Irrigated agriculture:
   - May create drainage problems
   - Can saturate naturally well-drained soils
   - Management-induced poor drainage
   - Drainage becomes critical
   
   Tidal areas:
   - Regular saturation cycles
   - Salt water intrusion complicates
   - Extreme management challenges
   - Often very low rating
"""

# ============================================================================
# CROP-SPECIFIC RESPONSES
# ============================================================================

"""
CROP RESPONSE TO SQ4 CLASSES:

Crops vary enormously in tolerance to poor drainage and oxygen deficiency.

VERY HIGH OXYGEN AVAILABILITY (80-100):

Excellent for all upland crops:
- All cereals (wheat, maize, barley, oats, sorghum)
- All grain legumes (soybeans, peas, beans, peanuts, chickpeas)
- Cotton
- All vegetables
- All fruit trees and vines
- Alfalfa and clovers
- Root crops (potatoes, carrots, beets)
- All ornamentals
- Tobacco
- Sunflower

No crops restricted by drainage.


HIGH OXYGEN AVAILABILITY (60-79):

Excellent for most crops:
- Cereals generally good
- Most vegetables
- Shallow-rooted crops
- Short-season crops

Good for:
- Deep-rooted legumes (minor limitations)
- Some tree fruits (minor limitations)
- Cotton (minor limitations)

Very sensitive crops may show slight stress:
- Some root vegetables
- Some ornamentals requiring perfect drainage


MEDIUM OXYGEN AVAILABILITY (40-59):

Suitable with tolerant varieties:
- Maize (tolerant varieties)
- Wheat (adapted varieties)
- Soybeans (tolerant varieties)
- Some vegetables (lettuce, cabbage, carrots with care)
- Grasses (reed canarygrass, tall fescue)
- Cranberries (require wetness)

Marginal or unsuitable:
- Cotton (very sensitive)
- Alfalfa (very sensitive)
- Most fruit trees (very sensitive)
- Peanuts (sensitive)
- Root crops (sensitive to rot)
- Tomatoes (sensitive)

Management critical:
- Planting dates crucial
- Variety selection important
- May need beds or ridges


LOW OXYGEN AVAILABILITY (20-39):

Limited options:
- Rice (excellent - requires flooding)
- Cranberries
- Some grasses (tolerant species)
- Willows and wetland trees
- Water-tolerant vegetables (watercress, taro)

Generally unsuitable:
- Most upland cereals
- Most vegetables
- Tree fruits
- Cotton
- Alfalfa and most legumes
- Root crops

Marginal with intensive management:
- Some adapted grass varieties
- Some short-season crops if well-timed


VERY LOW OXYGEN AVAILABILITY (0-19):

Suitable:
- Rice (flooded culture)
- Taro (poi)
- Water chestnuts
- Lotus
- Aquatic vegetables
- Cattails and wetland plants
- Swamp forest species

Unsuitable:
- All conventional upland crops
- All common vegetables
- All common field crops
- All fruit trees


DRAINAGE SENSITIVITY BY CROP:

Very sensitive (require excellent drainage):
- Cotton
- Alfalfa
- Fruit trees (most)
- Onions
- Carrots
- Tomatoes
- Peanuts
- Tobacco
- Avocado

Moderately sensitive:
- Maize (corn)
- Soybeans
- Wheat
- Potatoes
- Many vegetables

Moderately tolerant:
- Barley
- Oats
- Some grass species
- Some vegetable varieties

Tolerant:
- Rice (upland varieties)
- Some sorghum varieties
- Reed canarygrass
- Switchgrass
- Willows

Very tolerant:
- Rice (lowland/flooded)
- Cranberries
- Taro
- Aquatic plants


CRITICAL GROWTH STAGES:

Most sensitive stages for upland crops:
1. Germination (seeds need oxygen)
2. Seedling establishment
3. Rapid vegetative growth
4. Flowering
5. Grain/fruit fill

Brief saturation impacts:
- During sensitive stages: severe damage
- During less sensitive stages: moderate damage
- Dormant season: minimal damage (perennials)
"""

# ============================================================================
# MANAGEMENT STRATEGIES BY SQ4 CLASS
# ============================================================================

"""
MANAGEMENT APPROACHES FOR DIFFERENT SQ4 RATINGS:

VERY HIGH OXYGEN AVAILABILITY (80-100):

Management approach:
- Maintain good drainage
- No special measures needed
- Standard practices work
- Focus on other limiting factors

Practices:
- Avoid compaction (maintains infiltration)
- Maintain organic matter (improves structure)
- Contour farming to control erosion
- May need irrigation in dry climates

Advantages:
- No drainage costs
- Flexible operations
- Wide crop selection
- Predictable field conditions


HIGH OXYGEN AVAILABILITY (60-79):

Management approach:
- Maintain adequate drainage
- Monitor wet spots
- Minor preventive measures
- Generally standard practices

Possible improvements:
- Surface drainage in depressions
- Land smoothing to prevent ponding
- Avoid compaction
- Consider raised beds in wet spots

Crop management:
- Select adapted varieties
- Avoid planting immediately after heavy rain
- Most crops perform well


MEDIUM OXYGEN AVAILABILITY (40-59):

Management approach:
- Improve drainage where feasible
- Adapt practices to limitations
- Careful crop and variety selection
- Timing critical

Surface drainage improvements:

Land forming:
- Smooth surface to eliminate depressions
- Create gentle slopes for runoff
- Fill low spots
- Cost-effective first step

Bedding:
- Create raised planting beds
- Furrows between beds drain water
- Effective for row crops
- Annual or semi-permanent
- 10-30 cm beds typical

Surface ditches:
- Collect and convey water off field
- Network of field ditches to main drains
- Regular maintenance needed
- Reduces ponding time

Subsurface drainage:
- Tile drains lower water table
- Expensive but effective
- Spacing and depth calculated
- Requires outlet
- May be cost-effective for high-value crops

Crop management:
- Plant on beds or ridges
- Delay planting until adequately dry
- Select tolerant varieties
- Avoid susceptible crops
- Shorter season varieties (plant late, mature before fall rains)
- Consider cover crops to improve structure

Field operations:
- Wait for adequate drying
- Avoid working wet soil (causes compaction)
- Use low ground pressure equipment
- Limit traffic


LOW OXYGEN AVAILABILITY (20-39):

Management approach:
- Intensive drainage essential for most crops
- Alternative crop/system selection
- Accept severe limitations
- May not be economically viable for field crops

Drainage systems required:

Subsurface drainage:
- Tile drains essential
- Close spacing needed (10-20 m)
- Depth 80-120 cm
- High installation cost
- Maintenance critical
- May need pumping if no gravity outlet

Surface drainage:
- Also needed
- Bed and furrow systems
- Extensive ditch networks
- Regular maintenance

Raised bed systems:
- Significant elevation (30-50 cm)
- Imported soil may be needed
- High initial cost
- Suitable for vegetables

Alternative approaches:

Rice cultivation:
- Use poor drainage as advantage
- Level land for flooding
- Bunds to hold water
- Controlled drainage
- High yields possible

Wetland crops:
- Cranberries (commercial wetland crop)
- Taro
- Other adapted species

Pasture:
- Wetland grass species
- Extensive rather than intensive
- Lower productivity
- May be most practical use

Conservation uses:
- Wetland preservation
- Wildlife habitat
- Water quality improvement
- May have environmental incentives

Economic reality:
- Drainage costs may exceed benefits
- Consider alternative land uses
- Environmental restrictions may apply
- Subsidy programs may help


VERY LOW OXYGEN AVAILABILITY (0-19):

Management reality:
- Conventional agriculture not viable
- Drainage may be impossible or prohibited
- Accept wetland character
- Focus on adapted systems

Wetland rice:
- Ideal conditions
- Control water depth
- Prepare land (leveling, bunds)
- Can be highly productive
- Requires appropriate climate

Aquaculture:
- Fish farming
- Shellfish in tidal areas
- Waterfowl production
- Can be productive

Wetland crops:
- Cranberries (commercial)
- Aquatic vegetables
- Wetland ornamentals
- Limited markets

Conservation:
- Wetland preservation
- Wildlife habitat
- Wetland mitigation banking
- Carbon sequestration
- May provide income through programs

Forestry:
- Swamp forests
- Cypress, tupelo, mangroves
- Long-term investment
- Limited species options

Regulated uses:
- Wetland designation may prohibit drainage
- Permits required for modifications
- Environmental protection priority
- May receive conservation payments


GENERAL DRAINAGE IMPROVEMENT STRATEGIES:

1. Assessment first:
   - Determine cause of poor drainage
   - Is it correctable?
   - Cost-benefit analysis
   - Environmental considerations

2. Progressive approach:
   - Start with surface drainage (cheapest)
   - Add subsurface if needed
   - Evaluate results
   - Additional measures if justified

3. Maintenance essential:
   - Ditches fill with sediment
   - Tile drains can clog
   - Outlets can block
   - Regular inspection and cleaning

4. System design:
   - Professional design for subsurface
   - Proper sizing and layout
   - Adequate outlet essential
   - May need pump if gravity insufficient

5. Consider impacts:
   - Drainage affects downstream areas
   - Wetland loss may be regulated
   - Water quality concerns
   - May need permits

6. Long-term management:
   - Maintain improved conditions
   - Avoid recompaction
   - Keep structures functional
   - Adapt practices to new conditions
"""

# ============================================================================
# INTERACTIONS WITH OTHER SOIL QUALITIES
# ============================================================================

"""
SQ4 INTERACTIONS WITH OTHER GAEZ INDICATORS:

SQ4 ↔ SQ1 (Nutrient Availability):
- Waterlogging causes denitrification (N loss)
- Anaerobic conditions alter nutrient forms
- Iron and manganese reduction changes availability
- Phosphorus availability changes with redox
- Sulfate reduction produces toxic H2S
- Poor drainage can both increase and decrease availability
- Together determine actual nutrient access

SQ4 ↔ SQ2 (Nutrient Retention Capacity):
- Alternating wet/dry cycles mobilize nutrients
- Reduction dissolves retained Fe, Mn
- Saturation leaches nutrients despite high CEC
- Denitrification causes N loss regardless of retention
- Poor drainage reduces fertilizer efficiency
- Together determine nutrient losses

SQ4 ↔ SQ3 (Rooting Conditions):
- Waterlogging restricts rooting as effectively as compaction
- Shallow water table limits rooting depth
- Anaerobic conditions prevent root penetration
- Roots avoid saturated zones
- Both factors restrict explorable soil volume
- Combined limitations are multiplicative
- Must have both good drainage and good physical conditions

SQ4 ↔ SQ5 (Excess Salts):
- Poor drainage concentrates salts at surface
- Inadequate leaching allows salt accumulation
- High water tables deliver salts to root zone
- Drainage essential for salt leaching
- Both factors often coincide in problem soils
- Irrigation-induced poor drainage causes salinization
- Proper drainage necessary for salt management

SQ4 ↔ SQ6 (Toxicity):
- Reduction produces toxic Fe2+, Mn2+, H2S
- Anaerobic organic acids accumulate
- Aluminum more toxic in waterlogged acid soils
- Ethylene accumulation in saturated soils
- Poor drainage exacerbates toxicity problems
- Both factors cause severe plant stress
- May be difficult to separate effects

SQ4 ↔ SQ7 (Workability):
- Wet soils impossible to work
- Poor drainage delays field operations
- Wet soil compacts easily
- Limited workable days
- Both factors restrict management
- Poor drainage creates workability problems
- Drainage improvement improves both
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ4:

1. Temporal variability:
   - Drainage varies seasonally
   - Water tables fluctuate
   - Wet years vs. dry years differ drastically
   - Static rating doesn't capture dynamics
   - Long-term average used

2. Weather dependence:
   - Same soil drains well in drought, poorly in deluge
   - Climate change affecting patterns
   - Extreme events not fully captured
   - Rating based on typical conditions

3. Artificial drainage not fully captured:
   - Rating typically natural condition
   - Installed drainage systems change SQ4
   - Maintenance affects performance
   - Degradation over time not tracked
   - May rate poorly but function well if drained

4. Scale issues:
   - Map units may contain drainage variability
   - Toeslope seeps not mapped
   - Local perched tables not identified
   - Field-scale variability significant

5. Indicator limitations:
   - Redox features indicate past conditions
   - May not reflect current water table
   - Drainage class subjective
   - Permeability estimates uncertain

6. Crop-specific responses:
   - Generic rating doesn't fit all crops
   - Rice benefits from what limits others
   - Tolerance varies enormously
   - Critical timing not captured

7. Management effects:
   - Irrigation can create poor drainage
   - Compaction reduces drainage
   - Recent changes not reflected
   - Historical modifications unknown

8. Interaction complexity:
   - Effects of poor drainage complex
   - Direct (oxygen) and indirect (disease) impacts
   - Difficult to isolate SQ4 from other factors
   - Interactions with other SQs strong

RECOMMENDED USES:

Best for:
- Identifying naturally poorly drained soils
- Screening for drainage problems
- Regional planning
- Crop suitability at broad scale
- Prioritizing drainage improvements

Should be supplemented with:
- Site-specific drainage assessment
- Water table monitoring
- Seasonal observation
- Crop performance history
- Local knowledge
- Soil pit examination for redox features
- Understanding of installed drainage
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on soil surveys of variable detail and age
- Drainage class from national soil surveys

Soil property data quality:
- Drainage class: qualitative, interpreted
- Water table depth: often estimated, variable data
- Redox features: from soil profile descriptions, variable detail
- Permeability: calculated or estimated, limited measurements
- Better data in intensively surveyed regions
- Older surveys may not reflect current drainage improvements

CALCULATION DETAILS:

Rating functions:
- Drainage class primary factor
- Non-linear penalties for poor drainage
- Water table depth modifies rating
- Flooding/ponding reduces rating
- Permeability considered

Drainage class weights:
- Excessively to well drained: 85-100
- Moderately well drained: 65-80
- Somewhat poorly drained: 40-60
- Poorly drained: 20-40
- Very poorly drained: 0-20

Modifiers:
- Flooding frequency: -5 to -30 points
- Ponding: -10 to -40 points
- Very slow permeability: -5 to -15 points
- High water table: -10 to -40 points

Climate context:
- Ratings adjusted for regional climate
- Humid regions: weight drainage more heavily
- Arid regions: poor drainage less limiting
- Monsoon regions: seasonal considerations

(Note: Exact formulas proprietary to GAEZ methodology)

OUTPUT FORMATS:
- Raster grids at multiple resolutions
- Vector polygons with drainage attributes
- Tabular summaries by soil unit
- Integration with other SQ indicators
- Crop-specific suitability classes

VALIDATION:
- Cross-referenced with crop performance
- Compared with field drainage assessments
- Calibrated against drainage district needs
- Expert review by soil scientists
- Updated with newer survey data
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

Vepraskas, M.J. and L.P. Wilding (eds.). 2018.
Aquic Conditions and Hydric Soils: The Problem Soils.
SSSA Special Publication 50. Soil Science Society of America, Madison, WI.

Skaggs, R.W., M.A. Breve, J.W. Gilliam. 1994.
Hydrologic and water quality impacts of agricultural drainage.
Critical Reviews in Environmental Science and Technology, 24(1): 1-32.

Drew, M.C. 1997.
Oxygen deficiency and root metabolism: injury and acclimation under hypoxia and anoxia.
Annual Review of Plant Physiology and Plant Molecular Biology, 48: 223-250.

Kozlowski, T.T. 1984.
Responses of woody plants to flooding.
In: Flooding and Plant Growth. Academic Press, Orlando, FL. pp. 129-163.

Pezeshki, S.R. 2001.
Wetland plant responses to soil flooding.
Environmental and Experimental Botany, 46(3): 299-312.

DRAINAGE ENGINEERING REFERENCES:

Skaggs, R.W. and J. van Schilfgaarde (eds.). 1999.
Agricultural Drainage.
Agronomy Monograph No. 38. American Society of Agronomy, Madison, WI.

Ritzema, H.P. (ed.). 1994.
Drainage Principles and Applications.
ILRI Publication 16. International Institute for Land Reclamation and Improvement,
Wageningen, The Netherlands.

USDA-NRCS. 2001.
National Engineering Handbook, Part 650: Engineering Field Handbook, Chapter 14: Water Table Control.
United States Department of Agriculture, Natural Resources Conservation Service.

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- Land evaluation guidelines: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/

WETLAND AND HYDRIC SOIL RESOURCES:

USDA-NRCS. 2017.
Field Indicators of Hydric Soils in the United States, Version 8.1.
L.M. Vasilas, G.W. Hurt, and C.V. Noble (eds.).
USDA-NRCS in cooperation with the National Technical Committee for Hydric Soils.

Mitsch, W.J. and J.G. Gosselink. 2015.
Wetlands, 5th Edition.
John Wiley & Sons, Hoboken, NJ.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ4 assesses oxygen availability to plant roots
2. Drainage is the primary determinant of oxygen availability
3. Most crops require well-drained to moderately well-drained conditions
4. Poor drainage is one of the most severe soil limitations
5. Rated on 0-100 scale, classified into 5 categories
6. Water table depth, saturation duration, and timing are critical
7. Crop tolerance to poor drainage varies enormously
8. Drainage improvement possible but expensive
9. Some soils cannot be economically drained
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ4 is critical because:
- Oxygen deficiency causes immediate plant stress
- Even brief waterlogging damages most crops
- Poor drainage affects multiple plant processes
- Cannot be compensated by fertilization
- Limits crop selection severely
- Determines field operation timing
- Affects long-term soil health

Management realities:
- Prevention better than cure (avoid compaction)
- Natural drainage cannot be created easily
- Drainage systems are expensive
- Not all soils drainable
- Some poorly drained soils best in alternative uses
- Rice and wetland crops benefit from poor drainage
- Environmental regulations increasingly restrict drainage

Understanding SQ4 is essential for:
- Realistic crop selection
- Assessing drainage improvement needs
- Economic feasibility of land use
- Timing of field operations
- Variety selection
- System design (beds, drainage)
- Environmental compliance
- Sustainable land management

Poor drainage is often the most limiting factor - good fertility and adequate 
depth are useless if roots cannot function due to oxygen deficiency.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ4: OXYGEN AVAILABILITY TO ROOTS")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ4.")
    print("\nKey soil characteristics evaluated:")
    print("  Drainage assessment:")
    print("    - Soil drainage class")
    print("    - Depth to water table")
    print("    - Redoximorphic features (mottling and gleying)")
    print("    - Soil permeability and hydraulic conductivity")
    print("    - Soil texture and structure effects")
    print("    - Landscape position and topography")
    print("    - Flooding and ponding")
    print("    - Artificial drainage systems")
    print("\nRating classes: Very High, High, Medium, Low, Very Low")
    print("\nFor complete documentation, see the detailed text above.")
