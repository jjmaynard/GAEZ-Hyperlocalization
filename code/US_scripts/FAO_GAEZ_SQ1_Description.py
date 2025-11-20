"""
FAO GAEZ SQ1: NUTRIENT AVAILABILITY - DETAILED DESCRIPTION
===========================================================

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
SQ1: NUTRIENT AVAILABILITY

SQ1 represents the inherent capacity of soil to supply essential plant nutrients 
under low to intermediate input agricultural management systems. This soil quality 
indicator is particularly decisive for successful low-level input farming and remains 
important for intermediate input systems where fertilizer applications may be limited.

POSITION IN GAEZ FRAMEWORK:
SQ1 is one of seven key soil quality indicators used in the FAO GAEZ methodology:
- SQ1: Nutrient availability (focus of this document)
- SQ2: Nutrient retention capacity
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

Nutrient availability in soil is a complex property that reflects the soil's ability 
to supply essential nutrients to plants throughout their growing season. This involves:

1. The total quantity of nutrients present in the soil
2. The forms in which nutrients exist (available vs. unavailable)
3. The rate at which nutrients are released from soil minerals and organic matter
4. The chemical conditions (pH, redox) that control nutrient availability
5. The biological processes that transform nutrients
6. The physical accessibility of nutrients to plant roots

AGRICULTURAL RELEVANCE:

For low-input farming systems:
- Natural soil fertility is the primary nutrient source
- Limited or no fertilizer application
- Crop productivity directly dependent on inherent soil nutrient availability
- Long-term sustainability requires maintaining natural soil nutrient capital

For intermediate-input systems:
- Supplements natural fertility with modest fertilizer inputs
- Soil nutrient availability affects fertilizer efficiency
- Better native fertility reduces external input requirements
"""

# ============================================================================
# SOIL CHARACTERISTICS EVALUATED
# ============================================================================

"""
SQ1 DIAGNOSTIC CHARACTERISTICS:

The assessment of nutrient availability considers multiple interrelated soil 
characteristics that collectively determine the soil's capacity to supply nutrients. 
These characteristics are evaluated separately for topsoil and subsoil layers.

-------------------
TOPSOIL (0-30 cm)
-------------------

1. SOIL TEXTURE/STRUCTURE
   
   Definition: The relative proportions of sand, silt, and clay particles, and 
   their arrangement into aggregates.
   
   Role in nutrient availability:
   - Clay minerals provide cation exchange sites for nutrient retention
   - Silt contributes moderate nutrient-holding capacity
   - Sand provides minimal nutrient retention but good aeration
   - Structure affects water infiltration, root penetration, and microbial activity
   
   Texture classes evaluated:
   - Coarse (sandy): Low nutrient retention, rapid leaching
   - Medium (loamy): Moderate to good nutrient retention, balanced properties
   - Fine (clayey): High nutrient retention, potential for compaction
   - Very fine (heavy clay): Very high retention but can limit availability
   
   Optimal range: Medium textures (loams, silt loams) typically provide best 
   balance of nutrient retention and availability.


2. ORGANIC CARBON (OC)
   
   Definition: The carbon content of soil organic matter, typically expressed 
   as a percentage of soil mass.
   
   Role in nutrient availability:
   - Primary reservoir of nitrogen (95-98% of soil N is organic)
   - Source of phosphorus through mineralization
   - Provides sulfur and micronutrients
   - Enhances cation exchange capacity (CEC)
   - Improves soil structure and water retention
   - Supports beneficial microbial communities
   - Chelates micronutrients, increasing availability
   
   Typical ranges:
   - Very low: <0.5% OC
   - Low: 0.5-1.0% OC
   - Moderate: 1.0-2.0% OC
   - High: 2.0-4.0% OC
   - Very high: >4.0% OC
   
   Critical thresholds: Below 1% OC, soils typically show significant nutrient 
   deficiencies and poor biological activity.


3. SOIL pH
   
   Definition: The measure of soil acidity or alkalinity on a logarithmic scale 
   (typically measured in water or 0.01M CaCl2).
   
   Role in nutrient availability:
   - Controls solubility and availability of most nutrients
   - Affects microbial activity and nutrient transformations
   - Influences aluminum and manganese toxicity
   - Determines phosphorus fixation patterns
   
   pH ranges and nutrient effects:
   
   Extremely acid (pH < 4.5):
   - Aluminum, iron, manganese toxicity
   - Very low availability of N, P, K, Ca, Mg, Mo
   - Restricted microbial activity
   
   Very strongly acid (pH 4.5-5.0):
   - High aluminum toxicity risk
   - Low availability of P, Ca, Mg, Mo
   - Reduced microbial activity
   
   Strongly acid (pH 5.1-5.5):
   - Moderate aluminum toxicity
   - Reduced availability of P, Ca, Mg
   - Increased availability of Mn, Fe, Zn, Cu, B
   
   Moderately acid (pH 5.6-6.0):
   - Minimal toxicity issues
   - Good availability of most micronutrients
   - Moderate P availability
   
   Slightly acid (pH 6.1-6.5):
   - Optimal for most nutrients
   - Maximum P availability
   - Good microbial activity
   
   Neutral (pH 6.6-7.3):
   - Excellent for most crops
   - Good availability of all macronutrients
   - Optimal microbial activity
   
   Slightly alkaline (pH 7.4-7.8):
   - Beginning of micronutrient deficiency risk (Fe, Mn, Zn, Cu)
   - Reduced P availability
   
   Moderately alkaline (pH 7.9-8.4):
   - Deficiencies of Fe, Mn, Zn, Cu likely
   - Phosphorus fixation by calcium
   
   Strongly alkaline (pH 8.5-9.0):
   - Severe micronutrient deficiencies
   - Sodium toxicity risk
   - Very low P availability
   
   Very strongly alkaline (pH > 9.0):
   - Multiple severe nutrient deficiencies
   - Sodium toxicity
   - Poor crop performance


4. TOTAL EXCHANGEABLE BASES (TEB)
   
   Definition: The sum of exchangeable calcium (Ca), magnesium (Mg), potassium (K), 
   and sodium (Na) cations, typically expressed in cmol(+)/kg or meq/100g.
   
   Role in nutrient availability:
   - Direct measure of basic cation nutrient reserves
   - Indicates soil buffering capacity
   - Reflects weathering stage and soil age
   - Related to base saturation and soil fertility
   
   Components:
   - Calcium (Ca2+): Essential macronutrient, 65-85% of bases
   - Magnesium (Mg2+): Essential macronutrient, 10-20% of bases
   - Potassium (K+): Essential macronutrient, 2-5% of bases
   - Sodium (Na+): Not essential; high levels indicate salinity
   
   Typical ranges (cmol(+)/kg):
   - Very low: <5
   - Low: 5-10
   - Moderate: 10-20
   - High: 20-40
   - Very high: >40
   
   Interpretation: Higher TEB indicates greater reservoir of essential cations 
   and generally better nutrient availability, particularly for Ca, Mg, and K.


----------------------
SUBSOIL (30-100 cm)
----------------------

The subsoil evaluation focuses on characteristics most relevant to deep rooting 
crops and long-term nutrient supply:

1. SOIL TEXTURE/STRUCTURE
   - Affects deep root penetration and nutrient access
   - Influences water movement and nutrient leaching
   - Fine-textured subsoils can retain nutrients but may restrict roots

2. SOIL pH
   - Controls nutrient availability in the root zone
   - Subsoil acidity can limit deep rooting
   - Affects aluminum toxicity at depth

3. TOTAL EXCHANGEABLE BASES (TEB)
   - Indicates nutrient reserves accessible to deep roots
   - Important for perennial crops and deep-rooted annuals
   - Reflects long-term nutrient supply capacity
"""

# ============================================================================
# RATING METHODOLOGY
# ============================================================================

"""
SQ1 CALCULATION APPROACH:

The FAO GAEZ methodology uses a sophisticated approach to combine multiple soil 
characteristics into a single nutrient availability rating. This approach recognizes 
that:

1. Soil characteristics are interrelated and partially redundant
2. The most limiting factor often controls overall performance
3. Multiple moderate limitations can compound effects
4. Both topsoil and subsoil contribute to nutrient availability

CALCULATION PROCEDURE:

Step 1: Individual Characteristic Rating
--------
Each soil characteristic is assigned a rating (0-100 scale) based on:
- Crop-specific nutrient requirements
- Established threshold values
- Non-linear response curves
- Research-based relationships

Step 2: Identification of Most Limiting Factor
--------
Among all characteristics evaluated, the one with the lowest rating is identified 
as the "most limiting" characteristic.

Step 3: Calculate Average of Remaining Characteristics
--------
The remaining (less limiting) characteristics are averaged to represent the 
supporting conditions.

Step 4: Combine Most Limiting with Average
--------
The final SQ1 rating combines:
- The most limiting characteristic (higher weight)
- The average of remaining characteristics (moderate weight)

Mathematical representation (simplified):
SQ1 = f(MOST_LIMITING, AVERAGE_OF_OTHERS)

Where the combination function (f) gives greater weight to the most limiting factor.

This approach ensures that:
- A single severe limitation significantly reduces the rating
- Multiple moderate limitations have cumulative effects
- Exceptionally good conditions in some characteristics can partially compensate 
  for limitations in others
- The rating reflects both critical constraints and overall fertility

Step 5: Layer Integration
--------
Topsoil (0-30 cm) and subsoil (30-100 cm) ratings are integrated with emphasis 
on the topsoil, which is most critical for nutrient availability:

SQ1_final = weighted_combination(SQ1_topsoil, SQ1_subsoil)

Typical weighting: 70-80% topsoil, 20-30% subsoil
"""

# ============================================================================
# RATING CLASSES
# ============================================================================

"""
SQ1 RATING CLASSIFICATION:

The continuous SQ1 scores (0-100) are typically classified into discrete classes 
for mapping and interpretation:

CLASS 1: VERY HIGH (No or slight limitations)
Score: 85-100
Description: Excellent natural nutrient availability
Characteristics:
- High organic matter content (>2%)
- Optimal or near-optimal pH (6.0-7.5)
- High exchangeable bases (>20 cmol(+)/kg)
- Favorable texture (medium loam to silt loam)
- Minimal nutrient deficiencies or imbalances

Agricultural implications:
- Suitable for intensive crop production with minimal inputs
- Low fertilizer requirements
- Sustainable productivity with good management
- Wide range of crop options
- Economic returns from low-input systems


CLASS 2: HIGH (Slight to moderate limitations)
Score: 60-84
Description: Good natural nutrient availability with minor constraints
Characteristics:
- Moderate to good organic matter (1.0-2.0%)
- Acceptable pH range (5.5-6.0 or 7.5-8.0)
- Moderate to high exchangeable bases (10-20 cmol(+)/kg)
- Generally favorable texture with minor limitations
- Some nutrient deficiencies possible

Agricultural implications:
- Suitable for most crops with modest fertilizer inputs
- Good response to organic matter additions
- Minor amendments may improve productivity
- Reliable yields with proper management
- Economic viability at low to intermediate input levels


CLASS 3: MEDIUM (Moderate limitations)
Score: 40-59
Description: Adequate nutrient availability with notable constraints
Characteristics:
- Low to moderate organic matter (0.5-1.0%)
- Suboptimal pH (5.0-5.5 or 8.0-8.5)
- Low to moderate exchangeable bases (5-10 cmol(+)/kg)
- Less favorable texture (sandy or heavy clay)
- Multiple moderate nutrient limitations

Agricultural implications:
- Requires fertilizer inputs for satisfactory yields
- Soil amendments beneficial (lime, organic matter)
- Crop selection important
- Careful nutrient management essential
- Economic viability at intermediate input levels


CLASS 4: LOW (Severe limitations)
Score: 20-39
Description: Poor natural nutrient availability
Characteristics:
- Very low organic matter (<0.5%)
- Strongly acid or alkaline pH (<5.0 or >8.5)
- Low exchangeable bases (<5 cmol(+)/kg)
- Unfavorable texture (very sandy or very heavy clay)
- Severe nutrient deficiencies or toxicities

Agricultural implications:
- Requires intensive fertilizer programs
- Major amendments needed (lime, organic matter, micronutrients)
- Limited crop options
- High input costs relative to yields
- Economic viability questionable for annual crops
- May be suitable only for adapted species or forestry


CLASS 5: VERY LOW (Very severe limitations)
Score: 0-19
Description: Extremely poor nutrient availability
Characteristics:
- Essentially no organic matter
- Extremely acid or alkaline pH
- Very low or no exchangeable bases
- Extremely unfavorable texture
- Multiple severe nutrient constraints and toxicities

Agricultural implications:
- Not suitable for conventional agriculture
- Requires major land reclamation efforts
- Very high input costs
- Poor economic returns
- Consider non-agricultural uses
- May support only highly adapted native vegetation
"""

# ============================================================================
# CROP-SPECIFIC CONSIDERATIONS
# ============================================================================

"""
CROP RESPONSE TO SQ1:

While SQ1 provides a general assessment of nutrient availability, crop responses 
vary based on:

1. Nutrient requirements:
   - Heavy feeders (corn, cotton, vegetables) are more sensitive to low SQ1
   - Legumes less dependent on soil N but need other nutrients
   - Low-input crops (millets, sorghum) more tolerant of poor SQ1

2. Root characteristics:
   - Deep-rooted crops access subsoil nutrients (considers both layers)
   - Shallow-rooted crops depend primarily on topsoil SQ1
   - Extensive root systems exploit nutrients more efficiently

3. Growth duration:
   - Long-season crops require sustained nutrient availability
   - Short-season crops less affected by moderate limitations
   - Perennials depend on long-term nutrient supply

4. Nutrient use efficiency:
   - Some crops are efficient at extracting nutrients from poor soils
   - Mycorrhizal associations enhance P availability
   - Genetic variation in nutrient uptake efficiency

5. Economic factors:
   - High-value crops justify inputs to overcome low SQ1
   - Low-value crops require naturally high SQ1 for profitability
   - Input availability affects feasibility of low-SQ1 cultivation
"""

# ============================================================================
# MANAGEMENT IMPLICATIONS
# ============================================================================

"""
MANAGEMENT STRATEGIES BY SQ1 CLASS:

VERY HIGH SQ1 (85-100):
- Focus on maintaining soil quality
- Practice nutrient budgeting to avoid depletion
- Use cover crops and organic amendments
- Minimize erosion and organic matter loss
- Consider crop rotation to optimize nutrient use

HIGH SQ1 (60-84):
- Maintain organic matter levels
- Apply modest fertilizer inputs based on crop needs
- Address specific minor deficiencies (e.g., K, micronutrients)
- Use soil testing to fine-tune fertilization
- Implement conservation practices

MEDIUM SQ1 (40-59):
- Regular soil testing essential
- Balanced fertilizer programs required
- Increase organic matter through residue management
- Address pH issues (lime or sulfur)
- Consider green manures and cover crops
- Select crops appropriate for fertility level

LOW SQ1 (20-39):
- Intensive soil improvement needed
- Major organic matter additions
- Correct pH problems (lime for acidity, sulfur for alkalinity)
- Comprehensive fertilizer programs
- Build soil quality over time
- Start with adapted, low-requirement crops
- Consider integrated soil fertility management

VERY LOW SQ1 (0-19):
- Evaluate economic feasibility of agriculture
- Major reclamation efforts required
- Consider alternative land uses
- If cultivating, focus on:
  * Highly adapted species
  * Extensive soil improvement (multi-year effort)
  * High-value crops to justify costs
  * Reduced tillage to build organic matter
  * Possible use of biochar or other amendments
"""

# ============================================================================
# RELATIONSHIP TO OTHER SOIL QUALITIES
# ============================================================================

"""
SQ1 INTERACTIONS WITH OTHER GAEZ SOIL QUALITIES:

SQ1 ↔ SQ2 (Nutrient Retention Capacity):
- SQ1 measures existing nutrient availability
- SQ2 measures capacity to retain added nutrients
- Low SQ1 + Low SQ2 = High fertilizer losses, poor efficiency
- Low SQ1 + High SQ2 = Good response to fertilization
- High SQ1 + High SQ2 = Optimal conditions

SQ1 ↔ SQ3 (Rooting Conditions):
- Good rooting (SQ3) allows plants to access available nutrients (SQ1)
- Poor rooting restricts nutrient uptake even when SQ1 is high
- Deep roots access subsoil nutrients (important for SQ1 evaluation)

SQ1 ↔ SQ4 (Oxygen Availability):
- Waterlogging (low SQ4) alters nutrient transformations
- Anaerobic conditions cause N loss through denitrification
- Poor drainage can induce Fe, Mn deficiencies or toxicities
- Affects organic matter decomposition and nutrient release

SQ1 ↔ SQ5 (Excess Salts):
- High salinity interferes with nutrient uptake
- Sodium can displace Ca, Mg, K from exchange sites
- Salt stress increases nutrient requirements
- Combined SQ1-SQ5 limitations severely restrict crop options

SQ1 ↔ SQ6 (Toxicity):
- Aluminum toxicity (low pH) already considered in SQ1 via pH
- Calcium carbonate excess affects micronutrient availability
- pH extremes in SQ1 often correlate with toxicity in SQ6

SQ1 ↔ SQ7 (Workability):
- Poor workability limits management options
- Difficult tillage may prevent incorporation of amendments
- Physical constraints affect organic matter management
- Both influenced by texture and structure
"""

# ============================================================================
# LIMITATIONS AND CONSIDERATIONS
# ============================================================================

"""
IMPORTANT LIMITATIONS OF SQ1:

1. Static assessment:
   - SQ1 represents soil properties at time of survey
   - Doesn't account for dynamic changes during growing season
   - Nutrient depletion through cropping not modeled in real-time

2. Reference crop basis:
   - Original GAEZ maps often use maize as reference
   - Other crops may have different responses
   - Site-specific crop evaluations provide more accurate ratings

3. Scale considerations:
   - Global/regional assessments use representative soil units
   - Local variability not captured at coarse scales
   - Field-level assessment may differ from mapped values

4. Input level assumptions:
   - Most relevant for low-input systems
   - High-input systems less constrained by native SQ1
   - Intermediate systems show variable responses

5. Temporal factors not included:
   - Seasonal nutrient availability variations
   - Weather effects on mineralization
   - Nutrient release timing vs. crop demand

6. Biological factors simplified:
   - Microbial community effects generalized
   - Mycorrhizal associations not explicitly modeled
   - Root exudate effects on nutrient availability not included

7. Management history unknown:
   - Previous fertilization affects current availability
   - Residual nutrients from past cropping not captured
   - Soil degradation or improvement trends not tracked

8. Interaction effects:
   - Complex nutrient interactions simplified
   - Antagonistic effects between nutrients not fully captured
   - Synergistic effects may be underestimated

RECOMMENDED USES:

Best for:
- Large-scale land use planning
- Comparative assessment between regions
- Identifying areas with inherent fertility constraints
- Prioritizing areas for soil improvement
- Preliminary feasibility studies

Should be supplemented with:
- Local soil testing for specific sites
- Crop-specific nutrient requirements
- Economic analysis of input costs
- Farmer knowledge and experience
- Adaptive management approaches
"""

# ============================================================================
# TECHNICAL SPECIFICATIONS
# ============================================================================

"""
DATA SOURCES AND QUALITY:

Primary data source: Harmonized World Soil Database (HWSD) v1.2
- Spatial resolution: 30 arc-seconds (~1 km at equator)
- Based on regional and national soil maps
- Integrates multiple classification systems (FAO '74, '90, WRB)

Soil property data quality:
- Varies by region (better in developed countries)
- Some areas rely on expert estimates
- Limited field sampling in remote regions
- Uncertainty in spatial distribution

CALCULATION DETAILS:

Rating functions:
- Non-linear relationships between soil properties and ratings
- Thresholds based on crop response research
- Adjustments for texture-nutrient interactions
- pH curves specific to nutrient availability effects

Weighting schemes:
- Most limiting factor: ~60-70% weight
- Average of others: ~30-40% weight
- Topsoil: ~70-80% of final rating
- Subsoil: ~20-30% of final rating

(Note: Exact weighting formulas are proprietary to GAEZ methodology)

OUTPUT FORMATS:

- Raster grids at various resolutions
- Vector polygons with attribute tables
- Tabular data by soil unit
- Statistical summaries by administrative region
- Integration with crop suitability models

VALIDATION:

- Cross-referenced with crop performance data
- Compared to soil survey interpretations
- Calibrated against fertilizer response trials
- Validated through expert knowledge
- Continually updated with new research
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

RELATED FAO RESOURCES:

- FAO Soils Portal: https://www.fao.org/soils-portal
- GAEZ Data Portal: http://www.gaez.iiasa.ac.at/
- Harmonized World Soil Database: https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v12
- Land evaluation guidelines: https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/

ADDITIONAL READING:

Sanchez, P.A., et al. 2009. Digital Soil Map of the World. Science, 325(5941): 680-681.

Sys, C., E. Van Ranst, J. Debaveye. 1991. Land Evaluation. Part I: Principles in Land 
Evaluation and Crop Production Calculations. Agricultural Publications No. 7, 
General Administration for Development Cooperation, Brussels, Belgium.

Van Diepen, C.A., et al. 1991. Crop growth simulation model WOFOST. Documentation 
version 4.1. Centre for World Food Studies, Wageningen, The Netherlands.
"""

# ============================================================================
# SUMMARY
# ============================================================================

"""
KEY TAKEAWAYS:

1. SQ1 assesses the inherent capacity of soil to supply plant nutrients
2. Particularly important for low-input agricultural systems
3. Evaluates multiple soil properties in topsoil and subsoil
4. Uses a "most limiting factor" approach combined with average conditions
5. Rated on a 0-100 scale, classified into 5 categories
6. Crop responses vary based on species, rooting depth, and requirements
7. Management strategies should be tailored to SQ1 class
8. Should be considered alongside other soil qualities (SQ2-SQ7)
9. Best used for regional planning; supplement with local soil testing
10. Part of comprehensive FAO GAEZ land evaluation framework

SQ1 provides a scientifically-based, globally-consistent framework for assessing 
soil nutrient availability, enabling informed decisions about agricultural land use, 
crop selection, and input requirements.
"""

if __name__ == "__main__":
    print("FAO GAEZ SQ1: NUTRIENT AVAILABILITY")
    print("=" * 60)
    print("\nThis module contains detailed documentation on SQ1.")
    print("\nKey soil characteristics evaluated:")
    print("  Topsoil (0-30 cm):")
    print("    - Soil texture/structure")
    print("    - Organic carbon content")
    print("    - Soil pH")
    print("    - Total exchangeable bases")
    print("\n  Subsoil (30-100 cm):")
    print("    - Soil texture/structure")
    print("    - Soil pH")
    print("    - Total exchangeable bases")
    print("\nRating classes: Very High, High, Medium, Low, Very Low")
    print("\nFor complete documentation, see the detailed text above.")
