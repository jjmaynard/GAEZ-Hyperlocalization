"""
FAO GAEZ SQ6: TOXICITY - DETAILED DESCRIPTION
==============================================

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
SQ6: TOXICITY

SQ6 represents the presence of soil chemical conditions or substances that are 
toxic or harmful to plant growth. This soil quality indicator assesses various 
forms of toxicity including aluminum toxicity in acid soils, calcium carbonate 
excess in alkaline soils, heavy metal contamination, and other toxic substances 
that restrict plant growth and crop productivity.

POSITION IN GAEZ FRAMEWORK:
SQ6 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability
- SQ2: Nutrient retention capacity
- SQ3: Rooting conditions
- SQ4: Oxygen availability to roots
- SQ5: Excess salts
- SQ6: Toxicity (focus of this document)
- SQ7: Workability/field management constraints
"""

# ============================================================================
# CONCEPTUAL BASIS
# ============================================================================

"""
FUNDAMENTAL CONCEPT:

Soil toxicity arises from the presence of chemical elements or conditions at 
concentrations or states that harm plant growth. Unlike nutrient deficiencies 
(addressed in SQ1) or excess salts (SQ5), toxicity involves direct harm to 
plant tissues and metabolic processes.

MAJOR TOXICITY TYPES:

1. Aluminum Toxicity (Acid Soils):
   - Most widespread form globally
   - Affects ~4 billion hectares worldwide
   - Restricts root growth severely
   - Interferes with nutrient uptake
   - Major limitation in tropical/subtropical regions

2. Manganese Toxicity (Acid/Waterlogged Soils):
   - Common in acid, poorly drained soils
   - Mn2+ reduced form highly available
   - Causes bronzing and necrosis
   - Often accompanies aluminum toxicity

3. Iron Toxicity:
   - Primarily in flooded rice soils
   - Reduced Fe2+ form toxic
   - Bronzing symptoms
   - "Bronzing disease" of rice

4. Calcium Carbonate Excess (Calcareous Soils):
   - Induces micronutrient deficiencies (Fe, Mn, Zn)
   - Iron chlorosis common
   - Phosphorus fixation
   - High pH effects

5. Heavy Metal Toxicity:
   - Natural: serpentine soils (Ni, Cr), mineralized areas
   - Anthropogenic: mining, smelting, industrial contamination
   - Elements: Cd, Pb, Cu, Zn, Ni, Cr, As, Hg
   - Food chain concerns

6. Boron Toxicity:
   - Natural in arid regions
   - Irrigation water source
   - Very narrow safe range
   - Leaf necrosis

7. Other Toxicities:
   - Sulfide toxicity (acid sulfate soils)
   - Organic acid accumulation
   - Allelopathic compounds
   - Industrial contaminants

AGRICULTURAL RELEVANCE:

Impact on crops:
- Restricted root development
- Reduced nutrient and water uptake
- Visible symptoms on foliage
- Yield reductions or complete failure
- Food safety concerns (heavy metals)
- Limited crop selection

Geographic distribution:
- Aluminum toxicity: widespread tropics/subtropics
- Calcareous soils: arid and semi-arid regions
- Heavy metals: localized but severe
- Manganese: humid regions with poor drainage
- Varies greatly by region and parent material

Management challenges:
- Many toxicities difficult to remediate
- Soil amendments expensive
- Genetic tolerance variable
- Long-term sustainability issues
- Some toxicities permanent
- Food safety regulations increasingly strict

Economic impacts:
- Major yield losses
- High amendment costs
- Land value reduction
- Crop selection limitations
- Food contamination issues
- Health costs in severe cases
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ6 DIAGNOSTIC CHARACTERISTICS:

The assessment of toxicity evaluates multiple chemical conditions and elements 
that can cause harm to plants.

---------------------------
ALUMINUM TOXICITY (Acid Soils)
---------------------------

1. SOIL pH AND ALUMINUM ACTIVITY
   
   Definition: In acid soils (pH <5.5), aluminum dissolves from minerals and 
   becomes available in toxic Al3+ form.
   
   pH thresholds for aluminum toxicity:
   
   pH >5.5:
   - Minimal aluminum in solution
   - Al precipitated as hydroxides
   - Not toxic
   
   pH 5.0-5.5:
   - Al begins to dissolve
   - Increasing toxicity
   - Sensitive crops affected
   
   pH 4.5-5.0:
   - Significant Al toxicity
   - Many crops affected
   - Moderate to severe limitation
   
   pH 4.0-4.5:
   - High Al toxicity
   - Most crops severely affected
   - Major limitation
   
   pH <4.0:
   - Extreme Al toxicity
   - Very few crops tolerate
   - Extreme limitation
   
   Aluminum saturation percentage:
   - Percentage of effective CEC occupied by Al3+
   - Al saturation = (Exchangeable Al / ECEC) × 100
   
   Critical thresholds:
   - <20% Al saturation: Low toxicity
   - 20-40% Al saturation: Moderate toxicity
   - 40-60% Al saturation: High toxicity
   - >60% Al saturation: Severe toxicity
   
   Mechanisms of aluminum toxicity:
   - Inhibits root cell division and elongation
   - Damages root tips
   - Interferes with DNA replication
   - Binds to phosphorus (reduces availability)
   - Disrupts calcium uptake
   - Interferes with magnesium function
   - Reduces water uptake
   
   Symptoms in plants:
   - Stunted, stubby roots
   - Coralloid (branched) root system
   - Brown, damaged root tips
   - Reduced top growth
   - Phosphorus deficiency symptoms (often)
   - Calcium deficiency symptoms
   - Poor drought tolerance


2. EXCHANGEABLE ALUMINUM
   
   Definition: The amount of aluminum ions held on exchange sites and readily 
   available for plant uptake. Measured in cmol(+)/kg or meq/100g.
   
   Concentration levels:
   - <0.5 cmol(+)/kg: Low, minimal toxicity
   - 0.5-1.5 cmol(+)/kg: Moderate toxicity
   - 1.5-3.0 cmol(+)/kg: High toxicity
   - >3.0 cmol(+)/kg: Severe toxicity
   
   Note: Absolute amount less important than Al saturation percentage and pH.


3. BASE SATURATION (Related to Al Toxicity)
   
   Low base saturation indicates acid conditions:
   - <20% base saturation: High risk of Al toxicity
   - 20-35%: Moderate risk
   - >35%: Lower risk (if pH not extremely low)


4. CROP-SPECIFIC TOLERANCE TO ALUMINUM
   
   Sensitive crops (damaged at Al sat >15-20%):
   - Alfalfa
   - Cotton
   - Lettuce
   - Onion
   - Most fruit trees
   
   Moderately sensitive (damaged at Al sat >25-40%):
   - Maize
   - Soybeans
   - Wheat (many varieties)
   - Tobacco
   - Potatoes
   
   Moderately tolerant (tolerate Al sat 40-60%):
   - Oats
   - Rye
   - Some wheat varieties
   - Some rice varieties
   
   Tolerant (tolerate Al sat >60%):
   - Cassava
   - Tea
   - Pineapple
   - Some tropical forages
   - Adapted native species


---------------------------
MANGANESE TOXICITY
---------------------------

1. MANGANESE AVAILABILITY AND TOXICITY
   
   Definition: In acid and/or waterlogged soils, manganese is reduced to Mn2+ 
   which is highly available and can be toxic at high concentrations.
   
   Conditions promoting Mn toxicity:
   - Low pH (<5.5)
   - Poor drainage (anaerobic conditions)
   - High organic matter (provides reducing conditions)
   - High native Mn content
   
   Exchangeable Mn levels:
   - <50 ppm: Adequate, non-toxic
   - 50-100 ppm: Borderline, some crops affected
   - 100-200 ppm: Toxic to many crops
   - >200 ppm: Severely toxic to most crops
   
   Note: Critical levels vary by crop and soil pH
   
   Symptoms of Mn toxicity:
   - Brown speckling on older leaves
   - Necrotic spots
   - Chlorosis between veins (interveinal)
   - "Crinkle leaf" in some species
   - Stunted growth
   - Purpling of stems
   
   Crop sensitivity to Mn toxicity:
   
   Sensitive:
   - Soybeans
   - Beans
   - Clover
   - Lettuce
   - Cucumber
   
   Moderately sensitive:
   - Wheat
   - Barley
   - Maize
   - Potato
   
   Tolerant:
   - Rice (adapted to flooded conditions)
   - Oats
   - Rye grass
   
   Interactions:
   - Often occurs with Al toxicity in acid soils
   - Combined effects worse than either alone
   - Silicon can ameliorate Mn toxicity


---------------------------
IRON TOXICITY
---------------------------

1. IRON TOXICITY IN FLOODED SOILS
   
   Definition: In anaerobic (flooded) conditions, iron is reduced to Fe2+ which 
   is highly soluble and can reach toxic concentrations.
   
   Primarily affects flooded rice:
   - "Bronzing disease" of rice
   - Leaf bronzing and brown spots
   - Reduced tillering
   - Yield losses 10-100%
   
   Conditions promoting Fe toxicity:
   - Continuous flooding
   - High organic matter
   - Acid sulfate soils
   - High native Fe content
   - Low phosphorus availability
   
   Critical Fe2+ levels:
   - <100 ppm in soil solution: Safe
   - 100-300 ppm: Borderline
   - >300 ppm: Toxic to rice
   - >500 ppm: Severely toxic
   
   Management:
   - Intermittent drainage (oxidizes Fe2+)
   - Phosphorus fertilization (precipitates Fe)
   - Liming (raises pH, reduces Fe solubility)
   - Tolerant rice varieties
   - Silicate fertilizers
   
   Less common in upland crops:
   - Usually occurs only in extremely acid, wet soils
   - Or in poorly drained, high-Fe soils


---------------------------
CALCIUM CARBONATE EXCESS (Calcareous Soils)
---------------------------

1. CALCIUM CARBONATE CONTENT
   
   Definition: Presence of calcium carbonate (lime) in soil, common in arid 
   and semi-arid regions. Measured as % CaCO3.
   
   Classification by CaCO3 content:
   
   Non-calcareous (<1% CaCO3):
   - No lime-induced problems
   - Normal Fe, Mn, Zn availability
   
   Slightly calcareous (1-5% CaCO3):
   - Minor lime effects
   - Slight risk of Fe chlorosis
   - Most crops unaffected
   
   Moderately calcareous (5-15% CaCO3):
   - Moderate lime effects
   - Fe chlorosis on sensitive crops
   - Zn deficiency possible
   - P fixation by Ca
   
   Strongly calcareous (15-25% CaCO3):
   - Strong lime effects
   - Fe chlorosis common
   - Multiple micronutrient deficiencies likely
   - Crop selection limited
   
   Extremely calcareous (>25% CaCO3):
   - Severe lime-induced problems
   - Fe chlorosis on most crops
   - Very limited crop selection
   - Special management essential
   
   Depth of lime:
   - Surface CaCO3: immediate effects
   - Subsoil CaCO3: affects deep-rooted crops
   - Cemented horizons (petrocalcic): physical barrier
   
   pH in calcareous soils:
   - Buffered at 7.5-8.5
   - Cannot be easily acidified
   - High pH perpetuates problems


2. LIME-INDUCED CHLOROSIS
   
   Definition: Iron deficiency induced by high soil pH and CaCO3 content, 
   causing interveinal chlorosis (yellowing between leaf veins).
   
   Mechanism:
   - High pH precipitates Fe as Fe(OH)3 (unavailable)
   - Bicarbonate interferes with Fe uptake and translocation
   - Calcium competes with Fe uptake
   
   Severity factors:
   - Active CaCO3 content (finely divided)
   - Soil pH
   - Bicarbonate concentration
   - Poor drainage (exacerbates)
   - Genetic sensitivity of crop
   
   Crop sensitivity to lime-induced chlorosis:
   
   Very sensitive:
   - Azalea, blueberry (calcifuges)
   - Pin oak
   - Sorghum
   - Soybean (many varieties)
   - Peach, pear
   
   Sensitive:
   - Maize
   - Grain sorghum
   - Dry beans
   - Citrus
   - Grape
   
   Moderately sensitive:
   - Wheat (many varieties)
   - Barley (some varieties)
   - Sugar beet
   - Cotton
   
   Tolerant:
   - Alfalfa
   - Barley (tolerant varieties)
   - Safflower
   - Date palm
   - Pistachio


3. MICRONUTRIENT DEFICIENCIES IN CALCAREOUS SOILS
   
   Calcium carbonate excess causes deficiencies of:
   
   Iron (Fe):
   - Most common problem
   - Interveinal chlorosis
   - Reduced photosynthesis and yields
   
   Zinc (Zn):
   - Also very common
   - Stunted growth, small leaves
   - Reduced yields
   - Critical in maize, rice, citrus
   
   Manganese (Mn):
   - Less common than Fe or Zn
   - Similar chlorotic symptoms
   
   Copper (Cu):
   - Occasional in very high lime soils
   - Dieback of shoots
   
   Phosphorus fixation:
   - High Ca precipitates P as Ca-phosphates
   - Reduces P availability
   - Requires higher P fertilizer rates


---------------------------
HEAVY METAL TOXICITY
---------------------------

1. NATURALLY OCCURRING HEAVY METALS
   
   Serpentine soils:
   - High in Ni, Cr, Co
   - Mg:Ca ratio imbalanced
   - Low in essential nutrients
   - Specialized vegetation only
   - Very limited agricultural use
   
   Seleniferous soils:
   - High selenium content
   - Toxic to livestock (selenium poisoning)
   - Indicator plants (Astragalus)
   - Agricultural limitations
   
   Mineralized areas:
   - Near ore deposits
   - Variable metals depending on geology
   - Localized but severe
   
   Volcanic soils:
   - May have elevated As, F, heavy metals
   - Usually not severe enough to limit crops


2. ANTHROPOGENIC HEAVY METAL CONTAMINATION
   
   Sources:
   - Mining and smelting operations
   - Industrial emissions
   - Sewage sludge application
   - Contaminated irrigation water
   - Pesticide residues (As, Pb in old orchards)
   - Atmospheric deposition
   
   Common contaminant metals:
   
   Cadmium (Cd):
   - Highly toxic
   - Accumulates in food crops (food safety issue)
   - Mobile in soil, easily taken up by plants
   - Severe health concerns
   - Kidney and bone damage in humans
   
   Lead (Pb):
   - Common near roads (old leaded gasoline)
   - Lead paint contamination
   - Mining/smelting areas
   - Neurotoxin, especially to children
   - Less mobile in soil, but surface contamination serious
   
   Copper (Cu):
   - Old orchards (Bordeaux mixture)
   - Pig manure (Cu supplements)
   - Mine tailings
   - Toxic to plants at high levels
   - Accumulates in surface soil
   
   Zinc (Zn):
   - Mining and smelting
   - Galvanized materials
   - Micronutrient at low levels, toxic at high
   - Can interfere with other nutrients
   
   Nickel (Ni):
   - Natural in serpentine
   - Smelting operations
   - Some sewage sludge
   
   Chromium (Cr):
   - Industrial contamination
   - Leather tanning
   - Some forms very toxic
   
   Arsenic (As):
   - Old pesticides (lead arsenate)
   - Mining areas
   - Some groundwater
   - Highly toxic, carcinogenic
   
   Mercury (Hg):
   - Industrial contamination
   - Some fungicides historically
   - Mining operations
   - Extremely toxic
   
   Critical soil concentrations (approximate):
   
   Element | Total soil concentration causing toxicity
   --------|------------------------------------------
   Cd      | 3-8 mg/kg (crop dependent)
   Pb      | 100-500 mg/kg (plants), lower for health
   Cu      | 100-200 mg/kg
   Zn      | 200-500 mg/kg
   Ni      | 100-1000 mg/kg (variable by crop)
   Cr      | 75-100 mg/kg (Cr VI), higher for Cr III
   As      | 20-50 mg/kg
   Hg      | 0.5-5 mg/kg
   
   Note: Background levels much lower (<2 mg/kg for most)
   
   Food safety concerns:
   - Heavy metals accumulate in edible plant parts
   - Health risk to consumers
   - Regulations increasingly strict
   - May preclude food crop production
   - Leafy vegetables accumulate more than grains
   - Cadmium and lead most concerning


3. ASSESSMENT OF HEAVY METAL PROBLEMS
   
   Indicators of contamination:
   - Proximity to mines, smelters, industry
   - History of sewage sludge use
   - Old orchards
   - Near roads (Pb)
   - Unusual plant symptoms or death
   - Specialized heavy metal indicator plants
   
   Soil testing:
   - Total metal content (digestion)
   - Available metal (extractable)
   - Bioavailable forms most relevant
   - Multiple depths if accumulation at surface
   
   Regulatory limits:
   - Vary by country and land use
   - Food production has strictest limits
   - Residential areas (child exposure concern)
   - Industrial areas less strict
   - Cleanup levels specified by regulation


---------------------------
BORON TOXICITY
---------------------------

1. BORON TOXICITY
   
   Definition: Boron is essential micronutrient but toxic in excess, with very 
   narrow safe range.
   
   Sources:
   - Natural in arid region soils
   - Irrigation water (major source)
   - Industrial wastes
   - Some fertilizers
   
   Critical soil levels:
   - <0.5 ppm (hot water extractable): Deficient
   - 0.5-2.0 ppm: Adequate range
   - 2-5 ppm: Marginal toxicity, sensitive crops affected
   - >5 ppm: Toxic to most crops
   
   Symptoms of B toxicity:
   - Leaf tip and margin necrosis
   - Yellowing progressing from tips
   - Premature leaf drop
   - Reduced yields
   
   Crop sensitivity to boron:
   
   Very sensitive (<1 ppm toxic):
   - Citrus
   - Stone fruits
   - Many ornamentals
   
   Sensitive (1-2 ppm):
   - Wheat
   - Barley
   - Beans
   
   Moderately tolerant (2-4 ppm):
   - Maize
   - Oats
   - Potato
   - Alfalfa
   
   Tolerant (>4 ppm):
   - Cotton
   - Sugar beet
   - Asparagus
   
   Management:
   - Monitor irrigation water for B
   - Leaching if salinity not a problem
   - Crop selection based on tolerance
   - Difficult to remediate


---------------------------
OTHER TOXICITIES
---------------------------

1. ACID SULFATE SOILS
   
   Definition: Soils containing iron sulfides (pyrite) that, when drained and 
   oxidized, produce sulfuric acid.
   
   Formation:
   - Coastal/estuarine sediments
   - Tidal marshes
   - Mangrove areas
   - Contain reduced sulfur (FeS2)
   
   Upon drainage and oxidation:
   - Pyrite oxidizes to sulfuric acid
   - pH can drop to <3.5
   - Extreme acidity
   - Very high Al, Fe, Mn
   - Multiple severe toxicities
   
   Characteristics:
   - Yellow jarosite mottles
   - Very low pH (<4.0 common)
   - "Dead zones" with no vegetation
   - Water extremely acidic
   - Fish kills in drainage water
   
   Management:
   - Liming (massive amounts needed)
   - Keep flooded (prevent oxidation)
   - Drainage triggers problem
   - Very difficult to reclaim
   - Prevention better than cure


2. ORGANIC ACID ACCUMULATION
   
   In waterlogged soils:
   - Anaerobic decomposition produces organic acids
   - Acetic, butyric, propionic acids
   - Phenolic compounds
   - Toxic to roots
   - Compounds can also cause oxygen stress
   
   Management:
   - Drainage
   - Aeration
   - Organic matter management


3. ALLELOPATHY
   
   Definition: Toxic compounds released by plants that inhibit other plants.
   
   Examples:
   - Black walnut (juglone)
   - Sorghum residues
   - Some weed species
   
   Agricultural relevance:
   - Crop rotation considerations
   - Cover crop selection
   - Residue management
   - Usually manageable with knowledge
"""

# ============================================================================
# RATING SYSTEM
# ============================================================================

"""
SQ6 RATING SCALE:

Soils are rated on a 0-100 scale based on absence of toxicity:

0-100 SCALE INTERPRETATION:
- 80-100: Very High - No toxicity problems
- 60-79:  High - Minor toxicity problems
- 40-59:  Medium - Moderate toxicity problems
- 20-39:  Low - Severe toxicity problems
- 0-19:   Very Low - Extreme toxicity problems

Note: Rating decreases as toxicity increases


VERY HIGH (80-100): NO TOXICITY PROBLEMS

Soil characteristics:
- pH 5.5-8.0 (optimal range)
- No aluminum toxicity
- Low or no CaCO3 content
- Background heavy metal levels only
- No manganese toxicity
- Well-aerated when not intentionally flooded
- No contamination

Crop suitability:
- All crops suitable regarding toxicity
- No toxic limitations
- Wide crop selection
- Optimal growing conditions

Management:
- Standard practices
- No special amendments needed
- Normal fertility management


HIGH (60-79): MINOR TOXICITY PROBLEMS

Soil characteristics:
- pH 5.0-5.5 or 8.0-8.5 (marginally acid or alkaline)
- Low aluminum saturation (<20%)
- Slight to moderate CaCO3 content (1-5%)
- Minor micronutrient deficiency risk
- No heavy metal issues
- Occasional Mn elevation

Crop impacts:
- Very sensitive crops may be affected
- Most crops perform well
- Minor yield reductions possible (<10%)
- May need micronutrient fertilization

Suitable crops:
- Most field crops
- Select varieties for pH tolerance
- Avoid most sensitive crops

Management needs:
- Liming if pH <5.5 (for sensitive crops)
- Micronutrient fertilization if calcareous
- Monitor for developing problems
- Crop selection based on tolerance


MEDIUM (40-59): MODERATE TOXICITY PROBLEMS

Soil characteristics:
- pH 4.5-5.0 or >8.5 (strongly acid or alkaline)
- Moderate aluminum saturation (20-40%), or
- Moderate CaCO3 content (5-15%), or
- Elevated Mn levels (50-100 ppm), or
- Minor heavy metal contamination, or
- Moderately calcareous with chlorosis risk

Crop impacts:
- Sensitive crops severely affected or fail
- Tolerant crops show moderate stress
- Yield reductions 10-40%
- Visual toxicity symptoms common
- Nutrient deficiencies induced

Suitable crops:
- Tolerant crops only
- Specific varieties needed
- Limited crop selection
- May need special management

Management requirements:
- Liming essential for acid soils (2-5 tons/acre)
- Fe chelates or acidification for calcareous soils
- Micronutrient fertilization
- Tolerant varieties critical
- Regular soil testing
- May need raised beds or container growing for some crops
- Crop rotation to manage Al-sensitive crops


LOW (20-39): SEVERE TOXICITY PROBLEMS

Soil characteristics:
- pH <4.5 or >9.5 (very strongly acid or alkaline)
- High aluminum saturation (40-60%), or
- High CaCO3 content (15-25%), or
- High Mn levels (100-200 ppm), or
- Moderate heavy metal contamination, or
- Combined toxicities

Crop impacts:
- Most crops fail or severely stunted
- Only very tolerant species/varieties viable
- Yield reductions 40-80%
- Severe toxicity symptoms
- Multiple deficiencies induced
- Poor economic returns

Suitable crops (very limited):
- Cassava, tea, pineapple (Al-tolerant)
- Very tolerant barley varieties (calcareous)
- Adapted native species
- May need genetic selection/breeding

Management challenges:
- Heavy liming needed (5-10+ tons/acre)
- Repeated applications necessary
- Very expensive micronutrient programs
- Long-term reclamation needed
- May not be economically viable
- Food safety testing if heavy metals present


VERY LOW (0-19): EXTREME TOXICITY PROBLEMS

Soil characteristics:
- pH <4.0 or >10 (extremely acid or alkaline)
- Very high aluminum saturation (>60%), or
- Extremely calcareous (>25% CaCO3), or
- Severe heavy metal contamination, or
- Acid sulfate soils, or
- Multiple severe toxicities

Crop suitability:
- Essentially unsuitable for conventional agriculture
- Only most adapted species survive
- No economic crop production
- Specialized vegetation only

Examples:
- Acid sulfate soils (pH <3.5)
- Serpentine barrens
- Mine spoils
- Heavily contaminated industrial sites
- Extreme calcareous conditions

Alternative uses:
- Phytoremediation (plant-based cleanup)
- Natural vegetation preservation
- Waste disposal sites
- May require complete soil removal/replacement
- Land retirement
- Some specialty tolerant crops (research)

Reclamation:
- May be impossible or impractical
- Extremely expensive if attempted
- Long-term process (10-20+ years)
- Success uncertain
- Regulatory issues with contamination
- Removal and disposal may be only option
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
APPROACH TO RATING SQ6:

The rating methodology evaluates multiple types of toxicity:

1. PRIMARY RATING FACTORS:

   For acid soils (pH <5.5):
   
   Aluminum toxicity dominant:
   - pH most important indicator
   - Aluminum saturation percentage
   - Weighted 60-80% of toxicity rating
   
   Rating by pH and Al saturation:
   - pH >5.5, Al sat <20%: 85-100
   - pH 5.0-5.5, Al sat 20-30%: 65-85
   - pH 4.5-5.0, Al sat 30-50%: 40-65
   - pH 4.0-4.5, Al sat 50-70%: 20-40
   - pH <4.0, Al sat >70%: 0-20
   
   Manganese toxicity:
   - Often accompanies Al toxicity
   - Reduces rating further if severe
   - Combined effects worse than Al alone
   
   For alkaline/calcareous soils (pH >7.5):
   
   Calcium carbonate content primary:
   - CaCO3 percentage
   - Active lime content
   - Weighted 60-80% of toxicity rating
   
   Rating by CaCO3 content:
   - <1% CaCO3: 90-100
   - 1-5% CaCO3: 75-90
   - 5-15% CaCO3: 45-75
   - 15-25% CaCO3: 20-45
   - >25% CaCO3: 0-20
   
   pH amplifies effects:
   - pH 7.5-8.0: minor amplification
   - pH 8.0-8.5: moderate amplification
   - pH >8.5: severe amplification
   
   For heavy metal contamination:
   
   Single metal exceedance:
   - Any metal exceeding critical level
   - Rating depends on degree of exceedance
   - Food safety concerns may preclude use
   
   Rating by contamination level:
   - Background levels: 90-100
   - Slight elevation (2-3× background): 70-90
   - Moderate (3-10× background): 40-70
   - High (10-50× background): 20-40
   - Extreme (>50× background): 0-20


2. MOST LIMITING FACTOR APPROACH:

   Single severe toxicity:
   - Caps overall rating
   - Cannot be averaged away
   - Extreme Al toxicity: rating <20
   - Severe contamination: rating <15
   - Acid sulfate: rating approaches 0


3. MULTIPLE TOXICITY INTERACTIONS:

   Additive effects:
   - Al + Mn toxicity: combined worse
   - CaCO3 + high pH: amplified effects
   - Multiple heavy metals: cumulative toxicity
   
   Each additional toxicity:
   - Further reduces rating
   - Multiplicative effect common
   - Management complexity increases


4. PROFILE CONSIDERATIONS:

   Depth distribution:
   - Surface toxicity (0-30 cm): 60-70% weight
   - Subsoil toxicity (30-100 cm): 30-40% weight
   
   Rationale:
   - Most root activity in topsoil
   - Surface critical for establishment
   - Deep toxicity affects deep-rooted crops
   - Can limit all rooting if severe throughout


5. AMELIORATION POTENTIAL:

   Affects practical rating:
   
   Easily corrected (liming of moderate acidity):
   - Higher effective rating
   - Responsive to management
   
   Difficult to correct (heavy metals):
   - Lower effective rating
   - Permanent or very long-term problem
   
   Impossible to correct (some contamination):
   - Minimum rating
   - Alternative uses only


6. CROP-SPECIFIC CONSIDERATIONS:

   Generic rating vs. specific crops:
   - Rating for moderately sensitive crop
   - Tolerant crops rate soil higher
   - Sensitive crops rate soil lower
   
   Adjustments by crop:
   - Cassava on acid soil: higher rating
   - Alfalfa on calcareous: higher rating
   - Citrus on calcareous: lower rating


7. SPECIAL CONSIDERATIONS:

   Food safety with heavy metals:
   - Contamination level may prohibit food crops
   - But allow fiber crops or phytoremediation
   - Regulatory limits affect land use
   
   Acid sulfate soils:
   - Catastrophic if drained
   - May be acceptable if kept flooded (rice)
   - Potential toxicity vs. actual
   
   Localized vs. widespread:
   - Small contaminated areas manageable
   - Widespread toxicity more severe limitation
"""

# ============================================================================
# CROP-SPECIFIC RESPONSES
# ============================================================================

"""
CROP TOLERANCE TO VARIOUS TOXICITIES:

ALUMINUM TOLERANCE (Acid Soils):

Very sensitive (pH <5.5 causes problems):
- Alfalfa
- Sugar beet
- Cotton
- Most legumes (except lupins)
- Most fruit trees
- Onion, lettuce

Moderately sensitive:
- Maize
- Soybeans (varies by variety)
- Wheat (varies by variety)
- Tobacco
- Potatoes

Moderately tolerant:
- Oats
- Rye
- Some wheat varieties
- Rice

Tolerant:
- Cassava
- Tea
- Pineapple
- Blueberry (prefers acid)
- Some tropical forages
- Lupins
- Cowpea


LIME/HIGH pH TOLERANCE:

Very sensitive (chlorosis at pH >7.5):
- Azalea, rhododendron
- Blueberry
- Pin oak
- Sorghum
- Soybeans (many varieties)
- Peach, pear

Sensitive:
- Maize
- Dry beans
- Citrus
- Grape
- Potato

Moderately tolerant:
- Wheat (varies by variety)
- Cotton
- Sugar beet
- Tomato

Tolerant:
- Alfalfa (prefers alkaline)
- Barley
- Safflower
- Date palm
- Pistachio
- Asparagus


MANGANESE TOXICITY TOLERANCE:

Sensitive:
- Soybeans
- Dry beans
- Clover
- Cucumber
- Lettuce

Moderately sensitive:
- Wheat
- Barley
- Maize
- Potato

Tolerant:
- Rice (adapted to flooded soils)
- Oats
- Rye grass
- Tea


HEAVY METAL TOLERANCE:

Generally all crops sensitive but variations exist:

Zinc:
- Sensitive: Most crops at >200 ppm
- Some tolerance: Grasses, some cereals

Copper:
- Sensitive: Most crops at >100 ppm
- Some tolerance: Grasses, barley

Nickel (serpentine):
- Very few tolerant: Specialized native species
- Crop production very limited

Cadmium:
- All crops accumulate in edible parts
- Food safety concern regardless of plant tolerance
- Leafy vegetables accumulate more
- Lettuce, spinach particularly problematic

Lead:
- Plants relatively tolerant to high soil Pb
- Surface contamination/soil adhesion main food concern
- Root crops problematic in contaminated soils
"""

# ============================================================================
# MANAGEMENT STRATEGIES BY SQ6 CLASS
# ============================================================================

"""
MANAGEMENT APPROACHES FOR DIFFERENT SQ6 RATINGS:

VERY HIGH (80-100): NO TOXICITY PROBLEMS

Management approach:
- Standard practices
- No special measures needed
- Maintain favorable conditions
- Monitor to prevent problems

Preventive practices:
- Maintain pH in optimal range
- Avoid contamination
- Proper waste disposal
- Monitor fertilizer sources


HIGH (60-79): MINOR TOXICITY PROBLEMS

Management approach:
- Minor amendments if needed
- Careful crop selection
- Monitor for progression

For slight acidity (pH 5.0-5.5):
- Lime if growing sensitive crops: 1-2 tons/acre
- Select moderately tolerant crops
- May not need amendment for tolerant crops

For slight alkalinity/lime:
- Minor Fe deficiency possible
- Foliar Fe sprays if chlorosis appears
- Select moderately tolerant varieties
- Acidifying fertilizers (sulfur-coated urea, ammonium sulfate)

Practices:
- Soil testing every 2-3 years
- Monitor crop symptoms
- Adjust as needed


MEDIUM (40-59): MODERATE TOXICITY PROBLEMS

Management approach:
- Active management essential
- Amendments usually needed
- Restricted crop selection
- Ongoing monitoring

For moderate acidity (pH 4.5-5.0):

Liming program:
- Apply agricultural limestone: 2-5 tons/acre
- Dolomitic lime if Mg also low
- Incorporate into soil
- May need repeated applications
- Test annually to monitor progress
- Target pH 5.8-6.2 for most crops

Alternative: Select Al-tolerant crops:
- Rye, oats instead of wheat
- Adapted varieties of maize, soybeans
- Forages tolerant to acidity
- Blueberries (prefer acid)

Additional practices:
- Add organic matter (buffers Al)
- Ensure adequate P (precipitates Al)
- Adequate Ca reduces Al uptake
- Deep incorporation if subsoil also acid

For moderate lime excess (5-15% CaCO3):

Iron management:
- Soil application of Fe-chelates (EDDHA best in alkaline)
- Foliar Fe sprays (ferrous sulfate)
- Acidifying fertilizers
- May need annual applications
- Expensive

Zinc management:
- Soil or foliar Zn applications
- Zinc chelates or zinc sulfate
- Critical for maize, rice, citrus

Crop selection:
- Avoid most sensitive crops
- Select lime-tolerant varieties
- Barley instead of wheat if severe
- Sugar beet, alfalfa good choices

Soil modification attempts:
- Sulfur application to acidify: 500-2000 lbs/acre
- Very slow acting in calcareous soils (years)
- Only affects surface inches
- Repeated applications needed
- Often not practical except for high-value crops

For moderate heavy metal contamination:

Assessment first:
- Detailed sampling and testing
- Multiple elements
- Available vs. total concentrations
- Food safety evaluation

Management options:

Immobilization:
- Liming to raise pH (reduces availability of Cd, Pb, Zn)
- Phosphorus addition (immobilizes Pb)
- Organic matter (binds metals)
- Reduces uptake but doesn't remove metals

Crop selection:
- Avoid leafy vegetables if Cd present
- Avoid root crops if surface contamination
- Fiber crops instead of food crops
- Non-edible crops (flowers, Christmas trees)

Phytoremediation (in some cases):
- Hyperaccumulator plants extract metals
- Requires harvest and disposal
- Long-term process (years to decades)
- Feasible for moderate contamination only


LOW (20-39): SEVERE TOXICITY PROBLEMS

Management approach:
- Intensive reclamation often needed
- Very restricted crop options
- High costs
- Long-term commitment

For severe acidity (pH <4.5):

Major liming program:
- Large limestone applications: 5-10+ tons/acre
- Incorporate deeply
- May need 20-50 tons total over time
- Takes 3-5 years to reach target pH
- Annual testing and reapplication
- Very expensive

Consider only most tolerant crops:
- Cassava
- Tea
- Pineapple
- Adapted forages
- May still have low yields initially

Additional amendments:
- Phosphorus to precipitate Al
- Calcium to ameliorate Al toxicity
- Organic matter for buffering
- Gypsum in some cases (supplies Ca without raising pH much)

For severe lime excess (>15% CaCO3):

Severe chlorosis inevitable:
- Massive Fe-chelate applications needed
- Very expensive
- May need 10-50 lbs Fe-EDDHA per acre annually
- Cost may exceed crop value

Acidification attempts:
- Sulfur: may need 1-5 tons/acre
- Elemental sulfur very slow
- Sulfuric acid faster but dangerous
- Only affects surface layer
- Re-alkalinizes from depth
- Often not successful

Crop restrictions:
- Only most lime-tolerant crops
- Alfalfa, barley, safflower
- Date palm, pistachio for trees
- May need specialized rootstocks for fruit

Alternative: Raised beds with imported soil:
- For high-value crops
- Very expensive
- Imported acid soil
- Acidifying mulches
- Intensive management

For severe heavy metal contamination:

May preclude food crop production:
- Regulatory limits may prohibit
- Liability concerns
- Health risks

Options:

Removal and replacement:
- Excavate contaminated soil
- Dispose in licensed facility
- Replace with clean soil
- Very expensive ($50,000-500,000+ per acre)
- Only for high-value use (residential, commercial)

Containment:
- Cap with clean soil
- Prevent exposure and leaching
- Regular monitoring
- Still requires management

Phytoremediation:
- Grow hyperaccumulator plants
- Harvest and dispose properly
- Very long-term (20-50 years)
- Uncertain success
- Research stage for most metals

Alternative uses:
- Non-food crops (fiber, biofuel)
- Phytoremediation as land use
- Industrial use
- Open space with restricted access


VERY LOW (0-19): EXTREME TOXICITY PROBLEMS

Management reality:
- Conventional agriculture not viable
- Reclamation extremely difficult and expensive
- May be impossible to remediate
- Alternative uses or retirement

For extreme acidity (pH <4.0):

Acid sulfate soils:
- Catastrophic problem when drained
- Prevention critical: keep flooded if possible
- If drained: massive liming (20-100+ tons/acre)
- May need 10-20 years to remediate
- Surface water extremely acidic (environmental disaster)
- Often impossible to reclaim economically

Management if must use:
- Keep water table high (prevent pyrite oxidation)
- Flooded rice if climate suitable
- Very heavy liming if must drain
- Long-term commitment

For extreme lime excess (>25% CaCO3):

Essentially permanent condition:
- Cannot be meaningfully acidified
- Soil will re-buffer to alkaline
- Permanent Fe and Zn chlorosis
- Very limited crop options

Adapted uses:
- Natural vegetation
- Date palms in appropriate climate
- Some specialty alkaline-adapted crops
- Land retirement may be best option

For extreme heavy metal contamination:

Human health concern:
- May require evacuation/relocation
- Residential areas: removal mandatory
- Agricultural areas: may be designated contaminated site

Options:

Complete removal:
- Required if health risk
- Extremely expensive
- Contaminated soil disposal difficult
- May be only option

Permanent containment:
- Cap and contain
- No agricultural use
- Monitor perpetually
- Prevent human and environmental exposure

Restricted access:
- Fence and post
- No agricultural use
- Industrial use only if any
- May become brownfield site

Specialized phytoremediation research:
- Experimental approaches
- Willow, poplar plantations
- Harvest for safe disposal or energy
- Very long-term
- Success uncertain


GENERAL PRINCIPLES ACROSS ALL CLASSES:

Prevention:
- Easier than cure for all toxicities
- Maintain appropriate pH
- Avoid contamination
- Test before problems develop

Diagnosis:
- Soil testing essential
- Multiple depths if profile variable
- Tissue testing to confirm plant uptake
- Visual symptoms for field diagnosis

Crop selection:
- Match crop tolerance to soil condition
- Use tolerant varieties
- Consider alternative crops
- Genetic improvement ongoing

Soil amendments:
- Lime for acidity
- Fe-chelates for chlorosis
- Must be economically viable
- Long-term management needed

Economic reality:
- Severe toxicity expensive to manage
- May not be economically viable
- Alternative uses may be better
- Land value severely reduced

Monitoring:
- Regular testing
- Track changes over time
- Adjust management
- Early detection of problems
"""

# ============================================================================
# INTERACTIONS WITH OTHER SOIL QUALITIES
# ============================================================================

"""
SQ6 INTERACTIONS WITH OTHER GAEZ INDICATORS:

SQ6 ↔ SQ1 (Nutrient Availability):
- Aluminum toxicity interferes with P uptake and availability
- Calcareous soils precipitate P, reduce availability
- High pH affects micronutrient availability (Fe, Mn, Zn)
- Low pH increases availability of some nutrients (Fe, Mn) to toxic levels
- Toxicity causes nutrient imbalances
- Combined effects reduce effective fertility

SQ6 ↔ SQ2 (Nutrient Retention Capacity):
- Aluminum saturates exchange sites (displaces nutrients)
- Calcareous soils have high retention but poor availability
- pH extremes affect CEC magnitude
- Toxicity and retention interact at molecular level
- Heavy metals may occupy exchange sites

SQ6 ↔ SQ3 (Rooting Conditions):
- Aluminum toxicity severely restricts root growth
- Short, stubby roots cannot explore soil volume
- Calcareous hardpans create physical barrier
- Heavy metal toxicity reduces root development
- Toxic subsoils prevent deep rooting
- Combined physical and chemical barriers

SQ6 ↔ SQ4 (Oxygen Availability):
- Waterlogging increases Mn and Fe toxicity (reduction)
- Poor drainage exacerbates toxicities in acid soils
- Anaerobic conditions mobilize toxic metals
- Both factors create severe stress
- Acid sulfate soils worst if fluctuating water table
- Drainage management affects toxicity severity

SQ6 ↔ SQ5 (Excess Salts):
- High pH in sodic soils often accompanies lime excess
- Salinity and heavy metal toxicity additive stress
- Some saline soils also contaminated
- pH affects both salinity and specific toxicities
- Management for one may affect other
- Combined salinity + Al toxicity (some coastal acid sulfate)

SQ6 ↔ SQ7 (Workability):
- Acid soils often have poor structure
- Heavy lime applications improve workability
- Contaminated soils may have poor structure
- Toxicity doesn't directly affect workability
- But amendments may improve it
- Management difficulty increased by toxicity
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ6:

1. Complexity of toxicity:
   - Multiple forms possible
   - Interactions difficult to predict
   - Laboratory tests may not reflect field behavior
   - Bioavailability varies with conditions
   - Static measurements don't capture dynamics

2. Crop-specific responses:
   - Generic rating doesn't fit all crops
   - Tolerance varies enormously
   - Some crops benefit from conditions toxic to others
   - Critical growth stages not considered
   - Variety differences significant

3. Amelioration potential variable:
   - Some toxicities easily corrected (liming)
   - Others impossible (heavy metal removal)
   - Economic viability varies
   - Time frames very different
   - Success uncertain in severe cases

4. Spatial variability:
   - Contamination often highly variable
   - pH can vary within fields
   - Map units may not capture local problems
   - Sampling critical but expensive

5. Food safety separate from plant tolerance:
   - Plants may grow but accumulate toxic metals
   - Heavy metals in food chain major concern
   - Regulatory limits increasingly strict
   - May preclude food crops even if plants grow

6. Temporal changes:
   - pH changes with management
   - Contamination may worsen or improve
   - Static rating doesn't capture trends
   - Historical data may not reflect current status

7. Measurement challenges:
   - Total vs. available concentration
   - Extractant methods vary
   - Field vs. lab pH differences
   - Heavy metal speciation important but complex

8. Management level not considered:
   - Intensive management can overcome some problems
   - Low-input systems more vulnerable
   - Technology and economic resources matter
   - Rating doesn't reflect management capacity

RECOMMENDED USES:

Best for:
- Screening for toxicity problems
- Regional assessment
- Identifying problem areas
- Preliminary crop suitability
- Prioritizing detailed investigation

Should be supplemented with:
- Detailed soil testing (multiple depths, elements)
- Tissue testing to confirm uptake
- Crop-specific tolerance information
- Economic analysis of management options
- Food safety testing if contamination suspected
- Professional consultation for severe problems
- Site history investigation
- Long-term monitoring
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on national soil surveys
- Variable quality and detail by region

Soil property data quality:
- pH: widely measured, generally reliable
- CaCO3: less commonly measured, often estimated
- Exchangeable Al: limited measurements
- Heavy metals: rarely in standard surveys
- Better data in problem areas
- Contamination data very limited

CALCULATION DETAILS:

Rating functions:

For aluminum toxicity (acid soils):
- pH primary indicator
- Al saturation percentage if available
- Exponential decline below pH 5.5
- Very low ratings below pH 4.5

For lime excess (calcareous soils):
- CaCO3 content primary indicator
- pH modifier
- Exponential decline above 5% CaCO3
- Very low ratings above 25% CaCO3

For heavy metals:
- Any exceedance of critical level
- Degree of exceedance determines severity
- Food safety considerations
- May preclude any agricultural use

Combined toxicities:
- Most limiting factor dominates
- Multiple toxicities multiplicative
- Worst case determines rating

Profile weighting:
- Surface (0-30 cm): 60-70%
- Subsurface (30-100 cm): 30-40%

Crop-specific adjustments:
- Tolerant crops rate soils higher
- Sensitive crops rate soils lower
- Can vary by 20-40 points for same soil

(Note: Exact formulas proprietary to GAEZ methodology)

OUTPUT FORMATS:
- Raster grids at multiple resolutions
- Vector polygons with attributes
- Tabular summaries by soil unit
- Integration with other SQ indicators
- Crop-specific suitability classes

VALIDATION:
- Compared with crop performance data
- Calibrated against field observations
- Expert review by soil scientists
- Updated with new research
- Limited by data availability
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

ALUMINUM TOXICITY REFERENCES:

Foy, C.D., R.L. Chaney, M.C. White. 1978.
The physiology of metal toxicity in plants.
Annual Review of Plant Physiology, 29: 511-566.

Kochian, L.V., O.A. Hoekenga, M.A. Piñeros. 2004.
How do crop plants tolerate acid soils? Mechanisms of aluminum tolerance and phosphorus efficiency.
Annual Review of Plant Biology, 55: 459-493.

Von Uexküll, H.R. and E. Mutert. 1995.
Global extent, development and economic impact of acid soils.
Plant and Soil, 171(1): 1-15.

CALCAREOUS SOIL REFERENCES:

Lindsay, W.L. 1979.
Chemical Equilibria in Soils.
John Wiley & Sons, New York.

Loeppert, R.H. and W.P. Inskeep. 1996.
Iron. In: Methods of Soil Analysis, Part 3: Chemical Methods.
SSSA Book Series No. 5. Soil Science Society of America, Madison, WI. pp. 639-664.

Marschner, H. 1995.
Mineral Nutrition of Higher Plants, 2nd Edition.
Academic Press, London.

HEAVY METAL REFERENCES:

Adriano, D.C. 2001.
Trace Elements in Terrestrial Environments: Biogeochemistry, Bioavailability, and Risks of Metals, 2nd Edition.
Springer-Verlag, New York.

Alloway, B.J. (ed.). 2013.
Heavy Metals in Soils: Trace Metals and Metalloids in Soils and their Bioavailability, 3rd Edition.
Springer, Dordrecht.

Kabata-Pendias, A. and H. Pendias. 2001.
Trace Elements in Soils and Plants, 3rd Edition.
CRC Press, Boca Raton, FL.

McLaughlin, M.J., D.R. Parker, J.M. Clarke. 1999.
Metals and micronutrients – food safety issues.
Field Crops Research, 60(1-2): 143-163.

ACID SULFATE SOIL REFERENCES:

Dent, D. 1986.
Acid Sulphate Soils: A Baseline for Research and Development.
ILRI Publication 39. International Institute for Land Reclamation and Improvement, Wageningen.

Pons, L.J. 1973.
Outline of the genesis, characteristics, classification and improvement of acid sulphate soils.
In: Proceedings of the International Symposium on Acid Sulphate Soils. 
ILRI Publication 18, Vol. 1. pp. 3-27.

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- Land evaluation guidelines: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/

MANAGEMENT REFERENCES:

Adams, F. (ed.). 1984.
Soil Acidity and Liming, 2nd Edition.
Agronomy Monograph No. 12. American Society of Agronomy, Madison, WI.

Fageria, N.K. and V.C. Baligar. 2008.
Ameliorating soil acidity of tropical Oxisols by liming for sustainable crop production.
Advances in Agronomy, 99: 345-399.

U.S. EPA. 2007.
Treatment Technologies for Site Cleanup: Annual Status Report (Twelfth Edition).
EPA-542-R-07-012. U.S. Environmental Protection Agency, Washington, DC.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ6 assesses presence of toxic soil conditions and substances
2. Major types: Al toxicity, lime excess, heavy metals, Mn/Fe toxicity
3. Aluminum toxicity affects ~4 billion hectares globally (acid soils)
4. Lime excess common in arid/semi-arid regions
5. Heavy metal contamination localized but severe
6. Rated on 0-100 scale (high rating = no toxicity)
7. Crops vary enormously in tolerance to different toxicities
8. Some toxicities easily corrected (liming), others impossible
9. Food safety concerns with heavy metals separate from plant growth
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ6 is critical because:
- Toxicity directly harms plant tissues
- Cannot be compensated by other good conditions
- Some forms widespread (Al, lime)
- Others severe where present (contamination)
- Restricts crop selection dramatically
- Some forms impossible to remediate
- Food safety concerns increasingly important

Management realities:
- Aluminum toxicity: liming effective but expensive
- Lime excess: acidification difficult, crop selection better
- Heavy metals: may be impossible to remediate
- Prevention far easier than cure
- Severe toxicity may preclude agriculture
- Economic viability often questionable

Types by correctability:
- Readily corrected: Moderate Al toxicity (liming)
- Difficult to correct: Lime excess, severe acidity
- Impossible to correct: Heavy metal contamination, extreme conditions
- Permanent limitations: Serpentine soils, extreme contamination

Understanding SQ6 is essential for:
- Realistic land evaluation
- Crop selection
- Amendment programs
- Food safety assessment
- Land use planning
- Contaminated site management
- Long-term sustainability

Toxicity often represents an absolute limitation - even excellent fertility 
and water supply cannot overcome severe toxicity to produce viable crops or 
safe food.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ6: TOXICITY")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ6.")
    print("\nKey soil characteristics evaluated:")
    print("  Aluminum toxicity (acid soils):")
    print("    - Soil pH and aluminum activity")
    print("    - Exchangeable aluminum")
    print("    - Aluminum saturation percentage")
    print("\n  Calcium carbonate excess (calcareous soils):")
    print("    - CaCO3 content")
    print("    - Lime-induced chlorosis")
    print("    - Micronutrient deficiencies")
    print("\n  Heavy metal toxicity:")
    print("    - Natural and anthropogenic contamination")
    print("    - Multiple elements (Cd, Pb, Cu, Zn, Ni, Cr, As, Hg)")
    print("\n  Other toxicities:")
    print("    - Manganese and iron toxicity")
    print("    - Boron toxicity")
    print("    - Acid sulfate soils")
    print("\nRating classes: Very High (no toxicity), High, Medium, Low, Very Low")
    print("\nNote: High rating = good (no toxic problems)")
    print("\nFor complete documentation, see the detailed text above.")
