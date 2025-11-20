"""
SQ2 (Nutrient Retention Capacity) Crop Interpretations - FIELD CROPS
Based on FAO GAEZ Methodology

SQ2 evaluates the soil's ability to retain and store nutrients against losses 
through leaching and other processes. This is critical for:
- Preventing nutrient losses to groundwater
- Maintaining nutrients in the root zone for plant uptake
- Improving fertilizer use efficiency
- Reducing frequency of fertilizer applications
- Environmental protection from nutrient pollution

Based on FAO GAEZ methodology which evaluates:
- Topsoil (0-30cm): CEC, Texture/Clay Content, Organic Carbon, Base Saturation
- Subsoil (30-100cm): CEC, Texture/Clay Content, Base Saturation, CaCO3

KEY SOIL PROPERTIES:
- Cation Exchange Capacity (CEC): Primary retention mechanism for Ca, Mg, K, NH4
- Clay Content: Provides CEC sites, correlates with retention capacity  
- Organic Matter: High CEC contributor (200-400 cmol/kg), chelates micronutrients
- Base Saturation: Affects retention effectiveness and nutrient availability
- Profile Characteristics: Texture-contrast effects, clay accumulation zones

RATING SCALE:
- Very High: 80-100 (Excellent retention - minimal leaching losses)
- High: 60-79 (Good retention - efficient fertilizer use)
- Medium: 40-59 (Moderate retention - careful management needed)
- Low: 20-39 (High leaching risk - intensive management required)
- Very Low: 0-19 (Extreme leaching risk - very limited crop options)

MANAGEMENT IMPLICATIONS:
High retention soils allow larger, less frequent fertilizer applications with high 
efficiency. Low retention soils require frequent small applications, slow-release 
products, or fertigation to prevent nutrient losses and maintain plant nutrition.
"""

SQ2_INTERPRETATIONS = {
    # ========================================================================
    # FIELD CROPS
    # ========================================================================
    
    "Corn": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC (>25 cmol/kg), high clay 
content (>35%), and/or high organic matter (>3%) provide superior nutrient storage capacity. 
Minimal leaching losses even under heavy rainfall or irrigation. Can apply full seasonal N 
requirement (150-200 lb N/ac) in 2 applications (pre-plant + V6) with excellent retention 
through 120+ day season. Fertilizer use efficiency >80% achievable. K applications retained 
for multi-year benefit. Starter P highly effective as retention prevents movement away from 
seed furrow. Environmental benefits: very low risk of NO3 leaching to groundwater. 

MANAGEMENT STRATEGY: Standard or slightly concentrated application timing works well. Pre-plant 
applications of N, P, K retained effectively. Fall N applications viable in these soils (though 
spring still preferred in high-rainfall areas). Can use anhydrous ammonia, urea, or other 
soluble forms without excessive concern about leaching. Broadcast or banded applications both 
effective. Good residual fertility builds over years with positive nutrient balance.

CONSIDERATIONS: If clay content very high (>50%), may have workability issues affecting 
application timing. Very high CEC soils may initially show slower fertilizer response as 
exchange sites are filled, but long-term efficiency is excellent.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC (15-25 cmol/kg), 
moderate clay content (25-35%), or adequate organic matter (2-3%) provide good nutrient storage. 
Reasonable protection against leaching under normal rainfall. Plan 2-3 split N applications 
(pre-plant, V6, V10-12) for 150+ lb N/ac to optimize efficiency and match crop uptake. Fertilizer 
use efficiency 60-75%. K and P well retained; applications have good 2-3 year residual effect. 
Nitrate leaching risk low except under very heavy rainfall events (>3 inches).

MANAGEMENT STRATEGY: Standard corn belt fertilizer practices work well. Split N applications 
beneficial but not critical - can adjust based on weather. Pre-plant + side-dress programs 
reliable. Broadcast fertilization acceptable, though banding provides small efficiency gain. 
Most fertilizer forms (anhydrous, UAN, urea) perform well. Good conditions for precision 
agriculture with variable rate applications matched to yield potential.

CONSIDERATIONS: Time major fertilizer applications to avoid extended heavy rain forecasts. 
In irrigated fields, manage irrigation to minimize deep percolation and leaching.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC (10-15 cmol/kg), 
moderate clay (15-25%) with low-activity clays, or low-moderate organic matter (1-2%) provide 
limited nutrient storage. Leaching risk increases under heavy rainfall or over-irrigation. 
Essential to split N applications into 3-4 events (pre-plant or starter, V4-V6, V10, possibly 
V14-V16 for high yields) to minimize losses while maintaining plant nutrition. Expect 40-60% 
fertilizer use efficiency without careful management. Nitrate leaching risk moderate to high.

MANAGEMENT STRATEGY: Multiple split N applications critical - match timing to crop uptake 
patterns. Reduce individual application rates (40-60 lb N/ac per application). Consider 
nitrogen stabilizers (nitrification inhibitors like nitrapyrin, NBPT with urea) to extend 
retention time. Slow-release fertilizers (ESN, polymer-coated urea) provide significant 
benefit. Starter fertilization important but use modest rates (10-15 lb N/ac) to prevent 
early losses. Monitor soil moisture and avoid fertilizing before heavy rainfall. Build organic 
matter through residue management and cover crops - each 1% OM increase provides equivalent 
of ~5 cmol/kg CEC increase.

ENVIRONMENTAL CONCERNS: Moderate risk of NO3 leaching to tile drains and groundwater. Use 
fall cover crops (cereal rye, radish) to capture residual N. Maintain buffer strips near 
waterways. Consider precision tools (NDVI, chlorophyll meters) to optimize N timing and rates.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC (5-10 cmol/kg), low clay 
(<15%), or very low organic matter (<1%) provide poor nutrient storage. Sandy to sandy loam 
textures throughout profile. High leaching risk - nutrients move rapidly below root zone with 
rainfall or irrigation. Essential to split N into 5-7 applications (15-30 lb N/ac each) timed 
to active uptake periods. Without intensive management, expect <40% fertilizer use efficiency. 
Corn may be marginal crop choice at this retention level unless irrigation with fertigation 
available.

MANAGEMENT STRATEGY: Very frequent, small N applications essential. Ideal: fertigation through 
center pivot or drip irrigation with 2-3 applications per week during rapid growth (V10-R1), 
total season 150-180 lb N/ac. Without fertigation: weekly applications V4-V16 (6-8 events). 
Nitrogen stabilizers and slow-release products (ESN, polymer-coated) mandatory for any efficiency. 
Consider foliar N supplementation during grain fill. Split apply all nutrients - even P and K 
have some mobility in these soils. Avoid pre-plant applications - nutrients will leach before 
crop establishes. Starter fertilizer in seed furrow or 2×2 band critical.

SOIL IMPROVEMENT: Build organic matter aggressively: return all residues, use cover crops 
year-round when field not in production, consider manure applications. Each 1% increase in 
OM provides major retention boost. Deep-rooted cover crops (radish, turnip, rye) capture 
leached nutrients and bring back to surface.

ENVIRONMENTAL CONCERNS: High risk of NO3 leaching to groundwater. May not meet water quality 
protection standards in sensitive watersheds without sophisticated management. Required: 
tissue testing to guide applications, fall cover crops mandatory, maintain 50+ ft buffer 
strips near water. Consider alternative crops with lower nutrient requirements.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Very low CEC (<5 cmol/kg), very low 
clay (<10%), and very low organic matter (<0.5%) provide minimal nutrient storage. Sand to 
loamy sand throughout deep profile. Extreme leaching risk - conventional corn production not 
viable. Nutrients leach within hours to days of rainfall. Fertilizer use efficiency <20% with 
conventional methods. 

MANAGEMENT OPTIONS: Only feasible with sophisticated fertigation: center pivot or drip irrigation 
with injection system, applying 5-10 lb N/ac every 2-3 days during active growth (V6-R3), total 
180-200 lb N/ac. All nutrients must be spoon-fed continuously. Controlled-release fertilizers 
(polymer-coated, 120-180 day release) essential for any broadcast applications, but still 
inefficient. Foliar nutrition required to supplement.

VIABILITY ASSESSMENT: Calculate economics carefully. High fertilizer costs ($80-120/ac just 
for N with special products and multiple applications), plus irrigation/fertigation equipment 
and management costs, may exceed returns except for very high-yield environments or high grain 
prices. Consider yield potential realistically: likely 100-120 bu/ac maximum even with excellent 
management due to stress periods between fertigations.

ALTERNATIVE CROPS: Grain sorghum (more drought tolerant, lower N requirement, deeper roots to 
scavenge leached nutrients). Perennial warm-season grasses for forage/biomass (permanent root 
system, multi-year nutrient capture). Specialized high-value vegetables under plasticulture 
with drip fertigation.

ENVIRONMENTAL: Extremely high risk of groundwater contamination. May be prohibited for row crop 
production in wellhead protection areas or sensitive watersheds. If cropped, mandatory: 
year-round living cover when field not planted, wide buffer strips, may need groundwater 
monitoring wells. Long-term soil improvement through massive organic matter additions required - 
consider transitioning to permanent vegetation."""
    },
    
    "Soybeans": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC and clay content 
provide superior storage for P, K, Ca, Mg, S, and micronutrients critical for both plant growth 
and N-fixation symbiosis. Although soybeans fix 50-70% of N needs from atmosphere (not requiring 
soil N retention), excellent retention of other nutrients is crucial for optimal yields. Can 
apply full seasonal P-K requirements (60-80 lb P₂O₅, 80-120 lb K₂O for 60 bu/ac) in single 
pre-plant application with minimal losses. Starter fertilizer retained in seed furrow area. 
Micronutrients (Mo, Fe, Mn, Zn, B) well retained and available.

MANAGEMENT STRATEGY: Pre-plant broadcast or deep-banded P-K applications highly effective. 
Excellent conditions for building soil test levels with multi-year applications. Lime applications 
(if needed) have long-lasting effect due to retention. Starter fertilizer (10-34-0) in 2×2 inch 
placement provides reliable early growth boost. Foliar applications of micronutrients (if needed) 
show good response as soil reserves are maintained. Sulfur retention good - single application 
of 20-30 lb S/ac (gypsum, AMS, elemental S) provides season-long availability.

N-FIXATION BENEFITS: High Ca and Mo retention particularly important for N-fixation. Adequate Ca 
ensures nodule formation and function. Mo is component of nitrogenase enzyme - Mo deficiency 
severely limits fixation even with good nodulation. High CEC retains these critical elements. 
Base saturation typically >60% in these soils provides optimal pH buffering for rhizobia bacteria.

CONSIDERATIONS: Very high CEC soils may show slower initial P response as fixation sites are 
saturated, but long-term P availability excellent. If pH >7.5 and high carbonate, may need 
chelated Fe for varieties susceptible to chlorosis.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good 
storage for P, K, and essential elements. Standard soybean production practices work well. 
Apply P-K requirements (40-60 lb P₂O₅, 60-90 lb K₂O for 50 bu/ac) in 1-2 applications - 
either all pre-plant or split pre-plant + early reproductive stage. Good retention allows 
building soil test levels over time. Fertilizer use efficiency 60-70% typical.

MANAGEMENT STRATEGY: Pre-plant P-K broadcast followed by incorporation or deep banding both 
effective. Starter fertilizer (low N, 10-15 lb N/ac maximum to avoid inhibiting nodulation) 
with P provides reliable early growth response. Good conditions for achieving 150-200 lb N/ac 
from biological fixation - soil conditions support robust nodulation. Sulfur application 
(15-20 lb S/ac) retained adequately through season. Lime applications have good 3-4 year 
effectiveness.

ENVIRONMENTAL: Low risk of nutrient runoff or leaching. Good P retention particularly important 
for water quality - dissolved P movement minimal. Eroded sediment carries some P but well-bound 
to soil particles. These soils support sustainable long-term soybean production with minimal 
environmental impact when managed properly.

CONSIDERATIONS: If K soil test is low-medium, may benefit from split application (pre-plant + R3) 
rather than single application, as soybean K uptake is high during seed fill and some loss can 
occur even in these soils under very heavy rainfall.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
storage for P, K, and other nutrients. Critical to manage fertilizer timing and rates carefully 
to prevent losses while maintaining nutrition through reproductive stages. Plan split applications: 
pre-plant P-K (partial amount) + R1-R3 top-dress (remainder) to ensure adequate nutrition during 
heavy seed-fill nutrient demand.

MANAGEMENT STRATEGY: Split P-K applications recommended: 50-60% pre-plant broadcast or banded 
+ 40-50% top-dress at R1-R3 (potash particularly important during seed fill). For 50 bu/ac: 
30 lb P₂O₅ + 50 lb K₂O pre-plant, then 30 lb P₂O₅ + 50 lb K₂O at R1-R3. Reduces loss risk while 
ensuring late-season availability. Starter fertilizer important: low-N starter (0-20-20 or 10-34-0 
at 10-15 lb N/ac) in 2×2 placement, as these soils may not hold adequate early P near seed. Foliar 
P-K-micronutrient applications at R1-R3 provide additional safety margin.

SULFUR MANAGEMENT: Split S applications beneficial: 10 lb S/ac pre-plant + 10 lb S/ac at R1, 
as sulfate leaching risk moderate in these soils. Build organic matter - each 1% OM increase 
provides 20-40 lb additional organic S reserve.

N-FIXATION SUPPORT: These soils can support good fixation but may need supplemental Mo and B 
(both mobile in low-retention soils). Consider pre-plant application of 0.1 lb Mo/ac (sodium 
molybdate) + 1 lb B/ac to ensure adequate reserves. If pH <6.0, lime to improve nodulation and 
Mo availability.

ENVIRONMENTAL CONCERNS: Moderate P loss risk in high-rainfall events or over-irrigation. Apply 
P based on soil test - avoid excess. Consider buffer strips and vegetative filter areas. Fall 
cover crops capture and hold nutrients over winter.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture, and low 
organic matter provide poor nutrient storage. P, K, S, and micronutrients subject to leaching 
losses. Essential to use frequent split applications and slow-release products. Soybeans more 
viable than corn at this retention level because N-fixation eliminates reliance on soil N 
retention, but other nutrients still challenging.

MANAGEMENT STRATEGY: Multiple split applications essential for all nutrients. P-K split into 3 
applications: starter at plant (10-15 lb P₂O₅, 15-20 lb K₂O in 2×2), broadcast at V4-V6 (20-30 lb 
P₂O₅, 30-40 lb K₂O), and foliar/broadcast at R1-R3 (10-20 lb P₂O₅, 30-50 lb K₂O). Sulfur split: 
10 lb S/ac at plant, 10 lb S/ac at R1. Weekly drip fertigation ideal if available, applying small 
amounts continuously.

SOIL IMPROVEMENT: Aggressively build organic matter. Return all residues. Plant cover crops 
immediately after harvest (radish, rye, vetch blend) to capture mobile nutrients and add biomass. 
Apply manure or compost if available - provides both nutrients and OM. Each 1% OM increase 
dramatically improves retention.

N-FIXATION CHALLENGES: Low retention of Ca, Mo, Co, Fe affects nodulation and fixation efficiency. 
Pre-plant application of 1 lb Mo/ac + 2 lb B/ac + 100 lb gypsum/ac (Ca and S) improves fixation 
environment. Inoculation absolutely essential - these soils often lack established rhizobia. 
Consider liquid inoculant for in-furrow application plus granular for broader coverage.

ENVIRONMENTAL: High risk of P and K loss to groundwater (uncommon in most soils but occurs in 
very sandy soils). Apply nutrients only as needed based on soil test. Use tissue testing R1-R2 
to guide additional applications - don't over-apply. Consider whether soybeans economically viable 
given high input costs and management requirements.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy texture 
throughout profile, negligible organic matter provide almost no nutrient storage. Soybeans 
somewhat more viable than corn (because fixed N not dependent on soil retention) but still 
extremely challenging. P, K, S, Ca, Mg, and micronutrients leach rapidly with any rainfall. 
Conventional production not economically feasible in most cases.

MANAGEMENT OPTIONS: Only viable with intensive fertigation system. Drip irrigation with daily 
injection of complete nutrient solution (P-K-S-Ca-Mg-micronutrients) during V4-R6 stages. 
Weekly tissue testing to adjust rates. Foliar applications 2-3 times weekly during reproductive 
stages supplement soil-applied nutrients. Controlled-release P and K products (polymer-coated) 
provide partial buffer but still inefficient. Starter fertilizer critical but will leach within 
10-14 days of heavy rain.

N-FIXATION CHALLENGES: Very difficult to maintain adequate Ca, Mo, Co, and Fe for nodulation 
and N-fixation in these soils. Mo and B leach particularly rapidly. Weekly foliar applications 
of complete micronutrient package required. Even with intensive management, expect only 100-150 lb 
N/ac from fixation vs. 150-200 in better soils - may need supplemental N.

VIABILITY ASSESSMENT: Calculate economics carefully. High input costs ($100-150/ac for non-N 
fertilizers plus application costs) may not be recovered even at 40-50 bu/ac. Alternative approaches: 
1) Plasticulture with drip fertigation for high-value edamame production. 2) Organic production 
with massive compost additions (10+ tons/ac annually) to build OM and retention - but takes 5-10 
years to improve meaningfully. 3) Consider perennial legumes (alfalfa, clover) with permanent root 
systems and multi-year nutrient capture efficiency.

ENVIRONMENTAL: Extreme risk of nutrient losses to groundwater. May not be permissible in wellhead 
protection areas. If cropped: mandatory year-round cover crops, wide buffer strips, frequent 
monitoring. Long-term recommendation: transition to permanent perennial vegetation or conservation 
program enrollment."""
    },
    
    "Winter Wheat": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC and clay content 
provide exceptional nutrient storage through 9-month winter wheat cycle (Sept-June). Critical for 
winter survival as good Ca and K retention supports cold hardiness. N applied in fall retained 
through winter dormancy and available for spring growth. Can apply most or all seasonal requirements 
(100-120 lb N, 40-60 lb P₂O₅, 60-80 lb K₂O for 70+ bu/ac) in fall with minimal winter loss.

MANAGEMENT STRATEGY: Fall nutrient program highly effective. Apply P-K-S pre-plant or at seeding. 
N split: 30-50 lb N/ac at seeding (supports fall tillering, enhances winter hardiness) + 50-70 lb 
N/ac at green-up (Feb-Mar) + optional 20-30 lb N/ac at Feekes 5-6 for high yields. These soils 
retain fall N applications through winter - volatilization and denitrification minimal, leaching 
negligible even with winter/spring rains. Strong fall growth (25-35 tillers/plant) builds carbohydrate 
reserves for winter survival and spring regrowth.

COLD HARDINESS: High CEC soils with >60% base saturation provide excellent Ca and K retention 
crucial for cold tolerance. These elements strengthen cell walls and regulate ice formation in 
plant tissues. Good retention ensures adequate availability during fall hardening period and 
minimizes winter kill.

PHOSPHORUS MANAGEMENT: Fall P critical for root development before winter. High retention means 
P stays in root zone - not lost to fixation or leaching. Banded P at seeding provides starter 
effect plus spring availability. These soils allow building high soil test P (>30 ppm) that 
supports multiple years of production.

CONSIDERATIONS: If soil test P already high, can reduce or eliminate P applications and rely 
on soil reserves. Very high CEC soils (>40 cmol/kg) with heavy clay may have spring workability 
issues affecting top-dress N application timing - may need liquid N and drop nozzles vs. dry 
broadcast.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good 
nutrient storage through winter wheat season. Standard wheat belt practices work well. Fall-applied 
nutrients largely retained through winter with modest losses. Good Ca retention supports winter 
hardiness.

MANAGEMENT STRATEGY: Split N applications recommended: 30-40 lb N/ac at seeding + 60-70 lb N/ac 
at green-up + optional 20 lb N/ac at jointing for high protein. Fall N supports adequate fall 
growth (20-30 tillers/plant) without excessive loss risk. P-K can be applied all at seeding or 
split with P at seeding and K top-dressed at green-up. Retention adequate for most fertilizers - 
anhydrous, UAN, urea all perform well.

WINTER SURVIVAL: Good retention of Ca, K, and other elements supports winter hardiness in 
these soils. Adequate fall fertility encourages strong crown development and carbohydrate 
accumulation critical for cold tolerance. Base saturation >50% typical, providing good buffering.

ENVIRONMENTAL: Low risk of fall/winter N leaching in these soils. Spring applications coincide 
with active uptake, further minimizing loss. Good P retention protects water quality.

CONSIDERATIONS: In very high rainfall areas (>40 inches annual), consider reducing fall N to 
20-30 lb/ac and increasing green-up application to minimize any winter loss risk. Time spring N 
application with weather - avoid just before heavy rain if possible.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
nutrient storage through 9-month wheat season. Risk of fall-applied N loss over winter through 
leaching and denitrification. Careful timing and product selection essential.

MANAGEMENT STRATEGY: Conservative fall N (15-20 lb N/ac maximum) - just enough for stand 
establishment and modest fall growth (15-20 tillers/plant). Reserve majority of N for split 
spring applications: 50-60 lb N/ac at green-up + 30-40 lb N/ac at jointing + optional 10-20 lb 
N/ac at boot for protein. This timing strategy minimizes winter loss risk while matching uptake 
patterns. Consider N stabilizers (nitrapyrin, DCD) with fall N in higher rainfall areas. 
Slow-release products (ESN, polymer-coated) beneficial for fall application.

PHOSPHORUS-POTASSIUM: Apply full P requirement at seeding (critical for fall root development) - 
P leaching minimal even in moderate-retention soils. Split K: 50% at seeding + 50% at green-up, 
as K more mobile than P. Foliar K at boot stage provides additional assurance if soil test 
moderate.

SULFUR: Split S applications: 10 lb S/ac at seeding + 10 lb S/ac at green-up. Sulfate mobile in 
these soils - splitting reduces loss risk while ensuring availability during high-demand periods 
(tillering and boot-to-heading).

SOIL IMPROVEMENT: Build organic matter through residue management and cover crops after wheat 
harvest (summer cover critical for continuous living cover). Each 1% OM increase improves N and 
S retention meaningfully.

CONSIDERATIONS: If pH <5.8, lime application critical for winter survival and spring vigor - 
but lime has shorter duration effectiveness in moderate-retention soils. May need re-application 
every 3-4 years vs. 5-7 years in high-retention soils.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture provide 
poor nutrient storage through long wheat season. High risk of fall/winter N loss through leaching 
and denitrification. Sandy soils also prone to winter heaving damage. Careful management essential 
for successful winter wheat production.

MANAGEMENT STRATEGY: Minimal fall N (10-15 lb N/ac) - only enough for germination and basic 
establishment. Risk of N loss over winter too high for larger fall applications. Heavy reliance 
on spring N: split into 3-4 applications (40-50 lb at green-up, 30-40 lb at Feekes 5, 20-30 lb 
at Feekes 7-8, optional 10 lb at boot). Smaller, more frequent applications prevent leaching 
losses during spring rains. Use N stabilizers mandatory with any fall N. ESN (polymer-coated 
urea) for fall provides slow release through winter.

PHOSPHORUS: Critical to apply adequate P at seeding despite leaching risk - wheat absolutely 
requires strong fall root development for winter survival. Use 30-40 lb P₂O₅ in seed furrow or 
2×2 band. High rate compensates for retention limitations and ensures availability during short 
fall growing period.

POTASSIUM-SULFUR: Split all mobile nutrients. K: 1/3 at seeding, 1/3 at green-up, 1/3 at jointing. 
S: three 10 lb/ac applications at seeding, green-up, and jointing. Foliar applications of K-S at 
boot stage supplement soil applications.

WINTER HARDINESS CONCERNS: Low retention of Ca (critical for cold tolerance) increases winter kill 
risk in sandy soils. Apply gypsum (100-200 lb/ac, provides Ca and S) in fall. Some Ca retained 
through winter even in these soils as less mobile than N or K. If pH <6.0, lime essential but 
effectiveness short-lived.

VIABILITY: Winter wheat challenging in low-retention soils. Consider spring wheat (shorter season, 
less N loss risk) or grain sorghum (deeper roots can scavenge leached nutrients) as alternatives.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy profile 
provide almost no nutrient storage through 9-month winter wheat cycle. Extreme leaching risk 
makes conventional winter wheat production uneconomical. Fall-applied nutrients largely lost 
during winter. Even spring-applied N subject to rapid leaching.

MANAGEMENT OPTIONS: Winter wheat generally not recommended in these soils. If attempted: 
Absolutely no fall N - leaching losses >80% over winter. All N spring-applied in weekly 
applications (10-15 lb N/ac per week from green-up through boot, 8-10 total applications). 
Fertigation ideal if irrigation available. Controlled-release N products (180-day release) 
only option for reducing application frequency, but still inefficient.

PHOSPHORUS-POTASSIUM: Despite low retention, must apply adequate P at seeding for fall root 
development - use high rate (40-50 lb P₂O₅) to compensate for losses. Split K into multiple 
applications starting at green-up. Weekly foliar micronutrient applications required as leaching 
eliminates soil reserves.

WINTER HARDINESS: Very poor Ca retention severely compromises cold tolerance. High winter kill 
risk. Heavy fall gypsum application (300-500 lb/ac) attempts to provide Ca buffer but most 
leaches anyway. Low organic matter and poor aggregation in these soils also increase frost 
heaving risk.

ALTERNATIVE CROPS: Strong recommendation for spring wheat instead of winter wheat in very low 
retention soils. Benefits: 1) Shorter season (120 vs. 270 days) drastically reduces leaching 
risk. 2) All nutrients applied during active growth period. 3) Eliminates winter loss risk. 
4) Spring planting allows pre-plant tillage to incorporate retained nutrients. Or consider 
barley (more stress tolerant) or grain sorghum (deeper roots, more efficient nutrient use).

SOIL IMPROVEMENT: Long-term organic matter building essential. Winter cover crops mandatory 
(cereal rye after harvest, grows through winter, terminated spring). May need 10-15 years of 
intensive OM management to bring retention to even medium level. Consider whether cropping 
economically viable vs. converting to perennial grass, conservation program enrollment, or 
other use."""
    },

    "Spring Wheat": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior 
nutrient storage through spring wheat's shorter 100-120 day season. Can apply full seasonal 
requirements (90-110 lb N, 30-50 lb P₂O₅, 40-60 lb K₂O for 60+ bu/ac) in 1-2 applications with 
minimal losses. Spring mineralization in these soils (good OM, active microbial activity) provides 
additional N credit (30-60 lb N/ac) during growing season.

MANAGEMENT STRATEGY: Broadcast or banded pre-plant P-K-S application retained through season. 
N split: 60-70% at seeding or early tillering + 30-40% at flag leaf emergence optimizes grain 
protein. High retention allows some flexibility - if wet spring delays second N application, 
earlier N still available. Starter fertilizer (10-34-0 type) highly effective as retention 
keeps P concentrated near seed. Foliar applications generally not needed as soil reserves 
adequate.

PROTEIN OPTIMIZATION: High retention soils allow precise protein management. If target is feed 
wheat (<13% protein), use single N application at seeding. If target is high-protein hard red 
spring (>14% protein), split N with 40-50 lb N/ac at flag leaf stage retained and available 
during grain fill protein synthesis.

SOIL HEALTH: These soils support excellent spring wheat yields with high efficiency. Build on 
strength by maintaining OM through residue return and diverse crop rotations. Spring wheat fits 
well in rotation, maturing early enough for cover crop after harvest.

CONSIDERATIONS: In very wet springs with saturated soil, some denitrification N loss possible 
even in high-retention soils. If extended wet period expected, consider split N vs. all preplant.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good 
storage through spring wheat season. Standard practices work well. Modest spring mineralization 
provides supplemental N (20-40 lb N/ac). Fertilizer use efficiency 60-70%.

MANAGEMENT STRATEGY: Split N beneficial: 60-70 lb N/ac broadcast pre-plant or at seeding + 
30-40 lb N/ac at flag leaf. Or single application of 90-100 lb N/ac at early tillering if labor 
saving preferred - retention adequate to support this with good efficiency. P-K applied all 
pre-plant or at seeding - retention good through 4-month season. Starter fertilizer at seeding 
accelerates early growth in often-cool spring soils.

PROTEIN MANAGEMENT: Split N allows protein optimization. Base application supports yield, 
late application boosts protein if needed for hard red spring market premiums. These soils 
allow reliable protein response to late N.

ENVIRONMENTAL: Low leaching risk during typical spring wheat season. Spring planting coincides 
with crop uptake, minimizing loss window. Good P retention protects water quality.

CONSIDERATIONS: Spring wheat planted into cool soils (40-45°F) benefits from starter P 
despite adequate soil levels - cold soil reduces P availability and mobility. Even with good 
retention, banded starter provides early boost.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
storage through season. Spring leaching risk from snowmelt and spring rains. Careful timing 
essential to match applications with crop uptake and minimize losses.

MANAGEMENT STRATEGY: Multiple split N applications recommended: 40-50 lb N/ac at seeding + 
30-40 lb N/ac at tillering (Feekes 3-4) + 20-30 lb N/ac at flag leaf. Smaller, more frequent 
doses reduce loss risk while maintaining plant nutrition. Consider N stabilizers (NBPT with 
urea) to extend retention time between applications. Slow-release products (ESN) beneficial 
for base application.

PHOSPHORUS-POTASSIUM: Apply full P requirement at seeding (critical for early root development 
in cool spring soils) - P relatively immobile even in moderate-retention soils. Split K: 60% 
at seeding + 40% at early boot, as K more mobile and late demand high.

SULFUR MANAGEMENT: Split S applications essential in these soils as sulfate mobile. Apply 
10 lb S/ac at seeding + 10 lb S/ac at early boot. Organic S mineralization limited in cool 
spring soils, even with moderate OM.

TIMING CONSIDERATIONS: Spring wheat's short season advantage in moderate-retention soils. 
Unlike winter wheat, all applications during active growth period reduces total loss potential. 
Plant early as conditions allow - maximizes growing season length and nutrient use period before 
summer heat and drought stress.

SOIL IMPROVEMENT: Increase OM through diverse rotations. Spring wheat followed by cover crop 
(early maturity allows long cover crop season) builds OM and captures residual nutrients. 
Pea-wheat rotations add N, improve soil structure.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture provide 
poor storage. Spring leaching risk high from snowmelt and spring rains. Short spring wheat 
season (100-120 days) somewhat mitigates retention limitations compared to winter wheat, but 
still requires intensive management.

MANAGEMENT STRATEGY: Frequent split N essential: 30-40 lb N/ac at seeding + 20-30 lb N/ac at 
Feekes 3 + 20-30 lb N/ac at Feekes 5 + 20 lb N/ac at flag leaf. Weekly applications ideal if 
feasible. Timing critical - applications just before heavy rain will leach. Use weather 
forecasts to guide timing. N stabilizers and slow-release products mandatory. ESN or polymer-coated 
urea for base application extends availability.

PHOSPHORUS: High rate at seeding compensates for retention limitations. Use 40-50 lb P₂O₅ 
banded with seed or 2×2. Critical for rapid root development in spring wheat's race against 
summer heat and drought.

POTASSIUM-SULFUR: Split all mobile nutrients. K: three applications at seeding, tillering, and 
boot. S: three 10 lb/ac applications at seeding, tillering, and boot. Foliar K-S at boot provides 
additional insurance.

MICRONUTRIENTS: Sandy, low-OM soils often deficient in Zn, Mn, Cu. Soil-applied micronutrients 
leach readily. Use seed treatment or foliar applications. Tissue test at boot to guide foliar 
supplementation.

SOIL IMPROVEMENT: Build OM aggressively. Spring wheat - cover crop rotation adds substantial 
biomass. Pea before wheat adds N and OM. Return all straw. Consider occasional manure application 
if available. Target 1% OM increase over 3-5 years - each 1% gain dramatically improves retention.

VIABILITY: Spring wheat more viable in low-retention soils than winter wheat due to shorter 
season and active-growth-only nutrient requirements. Still challenging and high-cost, but 
feasible with intensive management.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy profile 
provide almost no storage. Even spring wheat's short season cannot overcome extreme retention 
limitations. Conventional production generally not economical.

MANAGEMENT OPTIONS: If attempted, requires extreme management intensity. Weekly N applications 
(10-15 lb N/ac per week, 8-10 total applications from planting through heading). Fertigation 
through sprinkler irrigation only viable approach for commercial production. Controlled-release 
N (180-day type) only option for reducing application frequency, but efficiency still <50%.

PHOSPHORUS: Despite leaching risk, adequate P at seeding non-negotiable. Apply 50-60 lb P₂O₅ 
banded with seed - high rate compensates for rapid loss and ensures some availability through 
critical seedling period. Foliar P applications at tillering and boot supplement.

POTASSIUM-SULFUR-MICRONUTRIENTS: All mobile nutrients require weekly applications or 
controlled-release products. Complete foliar nutrition program essential - biweekly applications 
of K-S-micronutrient packages from tillering through grain fill.

SPRING WHEAT VS ALTERNATIVES: Spring wheat slightly more viable than winter wheat in these 
soils due to shorter season, but still marginal. Better alternatives: 1) Barley - more stress 
tolerant, lower N requirement, shorter season (90-100 days). 2) Oats - very low N requirement, 
good performance in poor soils. 3) Field peas - N-fixing legume, single season, some retention 
benefit from fixing atmospheric N. 4) Spring triticale - more stress tolerant than wheat.

SOIL IMPROVEMENT: Intensive long-term OM building required for these soils to support viable 
grain production. Annual cover cropping, frequent manure/compost applications, possibly green 
manure crops dedicated to OM building. Realistic timeline: 10-15 years to achieve meaningful 
improvement. Consider whether grain production viable vs. perennial forage crops, conservation 
enrollment, or alternative land use.

ENVIRONMENTAL: Extreme nutrient loss risk threatens water quality. Weekly applications, even 
if economically justified, may not meet environmental protection standards in sensitive areas. 
May require buffer zones, monitoring, possibly restricted from cropping in watershed protection 
areas."""
    },

    "Cotton": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC critical for cotton's 
intensive nutrient requirements and long season (150-180 days). Cotton is K-intensive crop 
(requires 60+ lb K₂O per bale, more than N) - high retention essential for maintaining adequate 
K through boll fill. Can apply full seasonal requirements (150-180 lb N, 50-70 lb P₂O₅, 120-180 lb 
K₂O for 2+ bales/ac) in 2-3 applications with minimal losses.

MANAGEMENT STRATEGY: Pre-plant or at-plant application of P-K provides season-long availability. 
Cotton's peak K uptake during flowering-boll fill (July-Aug in US Cotton Belt) - high retention 
ensures K remains available during this critical 60-day period despite potential for leaching 
from irrigation or summer thunderstorms. N split: 30-40% pre-plant or at-plant + 40-50% at early 
bloom + 10-20% at peak bloom. These soils hold split-applied N effectively through extended season.

POTASSIUM CRITICAL: Cotton removes ~50 lb K₂O per bale in harvested seed cotton. High-retention 
soils essential for avoiding mid-season K deficiency that limits boll set and fill. Leaf symptoms 
of K deficiency (marginal chlorosis, "firing") rare in these soils with adequate application. 
Soil test K builds over years with positive balance.

MICRONUTRIENTS: Cotton requires adequate B for pollen viability and boll retention, Zn for 
growth regulation and boll development. High-retention soils maintain good micronutrient reserves. 
Foliar B applications at first square and first bloom still recommended even with good soil B, 
as insurance for high yields.

ENVIRONMENTAL: Good retention protects water quality - important as cotton production often 
in areas with irrigation return flow concerns. High CEC buffers against pesticide leaching as 
well as nutrients.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good 
storage through cotton's long season. Standard Cotton Belt practices effective. Good retention 
particularly important for K management in this K-intensive crop.

MANAGEMENT STRATEGY: Split N applications: 30-40% pre-plant + 40-50% at early bloom + 10-20% 
at peak bloom. This timing matches cotton's N uptake pattern (slow early, rapid at flowering). 
P-K split recommended: 60-70% pre-plant broadcast or banded + 30-40% side-dress at early bloom. 
For 2 bales/ac: apply 100-120 lb K₂O split, as cotton's peak K demand during boll fill must be 
met to prevent premature cutout.

POTASSIUM MANAGEMENT: Monitor petiole K during flowering. In good-retention soils, adequate 
pre-plant K usually maintains sufficiency, but split application provides additional insurance. 
Late-season K deficiency (August) can occur even in these soils if initial application inadequate 
or yield potential exceeds estimate. Foliar K applications at first bloom supplement soil K 
in high-yield situations.

SULFUR: Cotton requires 15-25 lb S/ac. Split S applications beneficial: 10-15 lb S/ac pre-plant + 
10 lb S/ac at early bloom. These soils retain sulfate moderately well but splitting reduces risk 
of late-season deficiency.

BORON: Tissue test-based foliar B applications at pinhead square, first bloom, and peak bloom. 
Soil-applied B subject to some leaching even in these soils. Foliar applications ensure adequate 
B during critical pollination and boll retention period.

CONSIDERATIONS: Irrigated cotton in these soils can achieve high yields (2.5+ bales/ac) with 
good fertility management. Monitor fertigation water for nutrient content - may provide significant 
portion of Ca, Mg, S requirements.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
storage through cotton's long season. K leaching risk during summer rains or heavy irrigation 
particularly concerning for this K-intensive crop. Careful split applications and monitoring 
essential.

MANAGEMENT STRATEGY: Multiple split N applications: 25-30% pre-plant + 30-40% early bloom + 
20-30% peak bloom + optional 10-20% at boll fill if tissue test shows deficiency. Smaller, 
more frequent applications reduce leaching losses during summer storms. K absolutely must be 
split: 30-40% pre-plant + 30-40% early bloom + 20-30% first bloom + optional foliar at peak 
bloom if petiole test low. For 1.5 bales/ac: total 90-110 lb K₂O split over 3-4 applications. 
P split: 50-60% pre-plant + 40-50% early bloom.

PETIOLE TESTING: Essential in moderate-retention soils to monitor nutrient status, especially 
K. Sample petioles at first bloom, peak bloom, and boll fill. K critical level: >35,000 ppm 
at first bloom, >25,000 at peak bloom. Below critical requires immediate foliar K + side-dress 
K application.

SULFUR: Split S essential as sulfate mobile in these soils. Apply 10 lb S/ac pre-plant + 10 lb 
S/ac early bloom + optional 5-10 lb S/ac at peak bloom if deficiency symptoms or tissue test low.

FERTIGATION: If irrigation available, fertigation provides ideal nutrient delivery method for 
moderate-retention soils. Allows small, frequent applications matching uptake. Can inject N-K 
solutions weekly during rapid growth (flowering-boll fill). Reduces leaching losses compared 
to periodic broadcast applications.

SOIL IMPROVEMENT: Build OM through winter cover crops (rye, vetch, radish blends) after cotton. 
Return cotton gin trash if available. Each 1% OM increase dramatically improves retention of 
all nutrients, particularly K.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture, low OM 
provide poor storage through cotton's 150-180 day season. High leaching risk for all nutrients, 
especially critical for K (cotton's highest nutrient removal). Intensive split applications 
essential. Cotton economically marginal in these soils without irrigation and fertigation capability.

MANAGEMENT STRATEGY: Very frequent split applications required. N split into 5-7 applications: 
small amount at plant (15-20 lb N/ac) + weekly or biweekly applications 15-20 lb N/ac during 
early bloom through peak bloom + optional late application based on tissue test. K absolutely 
critical to split: 4-6 applications starting pre-plant (20-30 lb K₂O), then at pinhead square, 
first bloom, peak bloom, and boll fill (15-25 lb K₂O each), total 90-120 lb K₂O. Foliar K 
applications every 10-14 days during flowering supplement soil K.

POTASSIUM CRISIS RISK: Low-retention soils notoriously difficult for cotton K management. 
Summer rains leach soil K rapidly. Symptoms appear suddenly as "firing" of leaves during peak 
boll fill - by this point yield loss already occurring. Prevention requires aggressive split 
applications + continuous petiole monitoring (biweekly during flowering) + rapid response with 
foliar + side-dress K if petiole levels decline.

FERTIGATION: Strongly recommended for cotton on low-retention soils. Weekly injection of N-K 
solutions through irrigation (drip ideal, pivot acceptable) maintains continuous plant nutrition 
and reduces leaching compared to less frequent broadcast applications. Can apply total seasonal 
N-K in 15-20 small doses matching uptake.

PHOSPHORUS-SULFUR-MICRONUTRIENTS: Even less-mobile P requires split applications in these 
soils. Apply 40-50% P pre-plant banded + 30-40% at early bloom + foliar P at peak bloom. S 
split into 4-5 applications. All micronutrients via foliar (soil-applied will leach) - weekly 
complete foliar nutrition program during flowering.

SOIL IMPROVEMENT: Cotton production on low-retention soils requires long-term commitment to OM 
building. Intensive cover crop program (winter rye, spring tillage, summer sunn hemp or cowpeas 
before late cotton planting). May need 5-10 years to meaningfully improve retention. Consider 
economics carefully - high input costs may not be recovered.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy profile, 
negligible OM provide almost no nutrient storage. Cotton's long season (150-180 days) and 
intensive nutrient requirements (especially K) make conventional production uneconomical in 
these soils. Extreme leaching risk for all nutrients.

MANAGEMENT OPTIONS: Cotton viable only with sophisticated irrigation-fertigation system. 
Requirements: drip or low-pressure precision irrigation with injection capability, daily nutrient 
applications during rapid growth phases (bloom-boll fill), continuous monitoring (petioles weekly, 
soil EC/pH biweekly), weather tracking to adjust for rainfall leaching events. Nutrient program: 
N-K solutions injected daily or every-other-day (5-10 lb N/ac, 8-12 lb K₂O/ac per injection) 
from pinhead square through boll maturity, total 15-25 applications. P via weekly fertigation. 
Foliar complete nutrition twice weekly during flowering.

POTASSIUM NIGHTMARE: Cotton's 60+ lb K₂O per bale requirement nearly impossible to meet in 
very-low-retention soils without continuous fertigation. Single day heavy rain (>2 inches) can 
leach so much soil K that deficiency symptoms appear within 3-5 days. Emergency foliar K + 
side-dress K required after major rainfall events. Even with intensive management, maintaining 
adequate K throughout season extremely challenging.

VIABILITY ASSESSMENT: Economics generally unfavorable. High input costs: $150-250/ac for 
nutrients alone (multiple applications, special products) + irrigation/fertigation costs + 
intensive monitoring and labor. May not be recovered even at 1.5-2.0 bales/ac with good cotton 
prices. Risk high - any management failure (missed fertigation, irrigation breakdown, untimely 
rainfall) causes immediate nutrient stress and yield loss.

ALTERNATIVE CROPS: Strong recommendation against cotton in very-low-retention soils. Better 
alternatives: 1) Peanuts - legume with N-fixation, shorter season, lower K requirement. 
2) Grain sorghum - short season, efficient nutrient use, deep roots. 3) Bermudagrass for hay - 
perennial, continuous root system, multi-cut allows multiple small fertilizer applications. 
4) Pecan orchard - permanent trees with deep roots eventually scavenge nutrients from deep 
profile.

SOIL IMPROVEMENT: These soils need massive OM additions to support row crop production. Annual 
applications of 15-20 tons/ac compost or manure. Continuous cover cropping. Possibly green 
manure crops for 2-3 years before attempting cotton. Realistic timeline for meaningful improvement: 
15-20 years. Economics may favor non-agricultural use."""
    },
    
    "Grain Sorghum": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior 
storage for grain sorghum's moderate nutrient requirements. Sorghum needs ~70-80% of corn's N 
(110-140 lb N/ac vs 150-180 for corn) but benefits from excellent retention which maximizes 
efficiency. Can apply full seasonal requirements in 1-2 applications with minimal loss. Sorghum's 
deeper, more extensive root system (up to 8 ft vs corn's 5-6 ft) effectively exploits retained 
nutrients throughout soil profile.

MANAGEMENT STRATEGY: Pre-plant broadcast or banded P-K highly effective. N split: 60-70% at 
planting + 30-40% at 4-5 leaf stage. High retention allows flexibility in timing - if delayed 
by weather, early N still available. Sorghum's advantage in high-retention soils: lower total 
N requirement saves input costs while maintaining high yields (140+ bu/ac potential). Excellent 
conditions for using less expensive conventional N sources (urea, UAN) without stabilizers.

DROUGHT TOLERANCE SYNERGY: High nutrient retention complements sorghum's drought tolerance. 
Deep retained nutrients accessible even when surface soil dry. Strong root development supported 
by retained Ca, Mg, K enhances drought survival. Good conditions for achieving both high yields 
in favorable years and reliable moderate yields in drought years.

CONSIDERATIONS: In extremely high-retention soils (CEC >40), sorghum may show slightly slower 
early growth than corn as nutrients initially held tightly, but mid-late season performance 
excellent.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good 
storage for sorghum's moderate nutrient needs. Standard dryland sorghum practices work well. 
Split N applications: 50-60% pre-plant + 40-50% at 4-6 leaf stage for 120-140 bu/ac. Good 
retention allows efficient use of moderate fertilizer rates.

MANAGEMENT STRATEGY: Broadcast or banded pre-plant P-K retained adequately through season. 
Sorghum's deeper roots access retained subsoil nutrients effectively - this is advantage over 
corn. N management simpler than corn - lower total requirement (100-130 lb N/ac) and good 
retention means 2 split applications sufficient. Can use standard N sources without expensive 
stabilizers or slow-release products in these soils.

COMPARATIVE ADVANTAGE: At this retention level, sorghum's efficiency advantages become apparent. 
Lower N requirement + good retention = higher fertilizer use efficiency than corn. Deep roots 
capture any nutrients that leach below corn's root zone. Better return on fertilizer investment. 
Consider sorghum over corn in fields with good but not excellent retention.

ENVIRONMENTAL: Low N leaching risk with sorghum's moderate N rates in these soils. Good P 
retention protects water quality. Sorghum's efficient nutrient use reduces environmental impact.

CONSIDERATIONS: Time major N application to avoid extended heavy rain. Sorghum more flexible 
than corn on N timing due to lower rates and better drought tolerance.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
storage but sorghum well-suited to this environment. This is "sweet spot" for sorghum over corn - 
retention limitations favor crop with lower N requirement and deeper roots. Split N essential: 
40-50% at planting + 30-40% at 4-6 leaf + optional 10-20% at boot if tissue test shows deficiency. 
Total N: 90-120 lb/ac for 100-120 bu/ac.

MANAGEMENT STRATEGY: Multiple smaller N applications reduce leaching risk. Consider N stabilizers 
(nitrapyrin, NBPT) to extend retention between applications. Slow-release products (ESN) provide 
modest benefit for base application. P-K split: 60% at planting + 40% at 6-leaf stage. Sorghum's 
extensive root system (more branched than corn, deeper penetration) scavenges retained nutrients 
effectively even from moderate-retention soils.

SORGHUM ADVANTAGES IN MEDIUM-RETENTION SOILS: 1) Lower N requirement (90-120 vs 130-160 lb N/ac 
for corn) reduces loss risk and cost. 2) Deeper roots (up to 8 ft) capture nutrients that leach 
below corn's shallower root zone. 3) Better drought tolerance allows delayed N applications if 
early applications lost to leaching - can still recover. 4) More efficient nutrient use means 
better ROI on fertilizer in leaching-prone soils.

SOIL IMPROVEMENT: Build OM through residue return and cover crops. Sorghum's fibrous root system 
and high biomass production contribute significant OM. Each 1% OM increase provides equivalent 
of ~5 cmol/kg CEC increase, benefiting subsequent crops.

CONSIDERATIONS: In moderate-retention soils with irrigation, manage irrigation carefully to 
minimize leaching. Sorghum more forgiving than corn if over-irrigation causes leaching.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture provide 
poor storage but sorghum STRONGLY PREFERRED over corn at this retention level. Sorghum's advantages 
critical in low-retention soils: 1) Lower N requirement (70-100 lb N/ac vs 100-140 for corn). 
2) Deeper roots (7-8 ft potential) retrieve leached nutrients. 3) Better drought tolerance allows 
survival between fertilizer applications. 4) More efficient nutrient use under stress.

MANAGEMENT STRATEGY: Frequent split N essential: 30-40 lb N/ac at planting + 20-30 lb N/ac at 
4-leaf + 20-30 lb N/ac at flag leaf + optional 10-20 lb N/ac at boot based on tissue test. 
Total: 70-100 lb N/ac for 70-100 bu/ac (still higher yields per lb N than corn in these soils). 
N stabilizers and slow-release products mandatory. Split all nutrients - P-K-S applied in 3 
applications to maintain availability.

ROOT ADVANTAGE: Sorghum's root system is game-changer in low-retention soils. Roots penetrate 
deeper and branch more extensively than corn. Can retrieve nutrients that leach to 4-6 ft depth 
(beyond corn's reach). Makes sorghum much more reliable than corn even at lower fertility. 
Fibrous root mass also improves soil structure and OM, benefiting long-term retention.

DROUGHT SYNERGY: Low-retention soils often sandy and drought-prone. Sorghum's superior drought 
tolerance allows production where corn would fail. Can delay applications if leaching occurred, 
as sorghum recovers better from temporary stress. Allows "insurance" applications if early N 
lost.

SOIL IMPROVEMENT: Sorghum ideal for building OM in low-retention soils. High biomass production 
+ extensive root system adds significant organic matter annually. Consider 2-3 years of sorghum 
with full residue return to improve soil before attempting more demanding crops.

VIABILITY: Sorghum economically viable in low-retention soils where corn marginal. Lower input 
costs, reliable yields, good stress tolerance. Clear choice for low-retention, drought-prone 
environments.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy profile, but 
sorghum MOST VIABLE GRAIN CROP option at this retention level. Sorghum's unique characteristics 
make it best choice: extremely deep rooting (up to 10 ft documented), superior drought tolerance, 
efficient nutrient use, ability to go dormant and resume growth. Still challenging, but feasible 
with good management where corn impossible.

MANAGEMENT OPTIONS: Frequent small N applications essential: 15-20 lb N/ac at planting + 15-20 lb 
N/ac every 2-3 weeks from 4-leaf through boot (6-8 total applications, 70-100 lb N/ac total). 
Fertigation through irrigation strongly recommended - weekly injection of 10-15 lb N/ac during 
active growth. Controlled-release N (180-day) for base application, though still only 40-50% 
efficient. All nutrients require split applications.

ROOT SYSTEM ADVANTAGE: Sorghum's root system is extreme scavenger. In deep sandy profiles, roots 
documented to 10+ ft depth - can retrieve nutrients far below any other grain crop's reach. 
Extensive lateral branching captures nutrients across wide area. This makes sorghum uniquely 
adapted to very-low-retention soils. Acts as "nutrient miner" bringing leached nutrients back 
to surface in residue.

DROUGHT TOLERANCE: Critical in very sandy soils with low water-holding capacity. Sorghum can 
go dormant during drought, survive on very little water, and resume growth when moisture returns. 
Allows production without irrigation in many areas where corn requires irrigation. With irrigation, 
can tolerate lower-frequency applications reducing leaching from excess water.

VIABILITY ASSESSMENT: Sorghum viable for 60-80 bu/ac in very-low-retention soils with intensive 
management - far better than corn (30-40 bu/ac if successful at all). Input costs still significant 
($60-90/ac for N with special products and multiple applications) but returns possible with good 
prices. Better economics than corn due to lower inputs, higher reliability.

ALTERNATIVE COMPARISON: If grain crop desired in very-low-retention soil, sorghum is the choice. 
Alternatives: pearl millet (even more drought tolerant, similar deep roots), forage sorghum or 
sorghum-sudangrass hybrid (harvest as forage, multiple cuts allow multiple small fertilizer 
applications), perennial warm-season grasses (permanent root system).

SOIL IMPROVEMENT: Use sorghum as soil-building crop. Massive root system and high biomass add 
significant OM annually. With full residue return and cover crop in winter, can improve very-poor 
soils meaningfully over 5-7 years. May transition to higher-value crops once retention improved."""
    },

    "Barley": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior 
storage through barley's relatively short season (90-110 days). Can apply most seasonal requirements 
(80-110 lb N, 40-60 lb P₂O₅, 50-70 lb K₂O for 80+ bu/ac) in 1-2 applications with minimal loss. 
High retention particularly important for MALTING barley where precise N management critical for 
protein control (target <13% protein).

MANAGEMENT STRATEGY: For feed barley: Pre-plant or at-seeding application of full N-P-K effective. 
Single application (90-100 lb N/ac) retained adequately through 100-day season. For malting barley: 
Split N to control protein: 50-60 lb N/ac at seeding + optional 20-30 lb N/ac at tillering only 
if tissue test shows deficiency. High retention means minimal N loss but nutrients remain available 
- allows precise protein management. Goal: adequate yield (70-80 bu/ac) with <13% protein for 
malting market premiums.

PROTEIN MANAGEMENT: High-retention soils ideal for malting barley production. Applied N stays 
available throughout season, so can use conservative N rates without yield penalty. Too much N 
in malting barley produces high protein (>14%) which reduces malting quality and market value. 
These soils allow fine-tuning N application for optimal yield-protein balance.

TEST WEIGHT: High retention supports strong straw and good grain fill, leading to excellent test 
weights (>48 lb/bu typical). Good K retention particularly important for test weight - K deficiency 
causes poor kernel plumpness. P retention supports vigorous early growth and rapid maturity.

CONSIDERATIONS: If soil test N high from previous crop, reduce or eliminate N application for 
malting barley. High-retention soils maintain residual N that can push protein too high.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage 
through barley's short season. Standard practices work well. Split N recommended: 60-70 lb N/ac 
at seeding + 20-30 lb N/ac at tillering for feed barley (80-100 bu/ac). For malting barley: 
50-60 lb N/ac at seeding with minimal or no topdressing to control protein <13%.

MANAGEMENT STRATEGY: Pre-plant P-K application retained adequately through season. Barley's 
relatively low nutrient requirements compared to wheat or corn are advantage in good-retention 
soils - nutrients stay available throughout shorter season. Starter fertilizer at seeding provides 
early boost. Good conditions for achieving both yield and quality goals.

MALTING vs FEED: These soils suitable for both markets. For malting: use conservative N rates 
(50-70 lb N/ac total), monitor soil test and previous crop residual N. For feed: can use higher 
N rates (80-100 lb N/ac) without protein concerns. Split applications allow adjustment based 
on early-season growth.

TEST WEIGHT: Good retention supports 45-48 lb/bu test weights typical. Adequate K particularly 
important for kernel plumpness and test weight. Good P availability supports rapid spring growth 
and timely maturity.

ENVIRONMENTAL: Low leaching risk with barley's moderate N rates and short season in these soils. 
Spring planting and maturity before summer heat/rain minimize loss window.

CONSIDERATIONS: Barley more tolerant of moderate pH (5.5-6.0) than wheat. These good-retention 
soils often have good base saturation (>50%) providing adequate pH buffering.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC provides limited 
storage but barley well-adapted due to short season and moderate nutrient requirements. Split N 
essential: 50-60 lb N/ac at seeding + 20-30 lb N/ac at tillering + optional 10-20 lb N/ac at 
early boot for feed barley. For malting barley: single application 50-70 lb N/ac at seeding, 
avoid topdressing to control protein.

MANAGEMENT STRATEGY: Multiple smaller N applications reduce leaching risk. Consider N stabilizers 
with spring applications if heavy rain forecast. Slow-release products (ESN) provide modest 
benefit. P-K split: 60% at seeding + 40% at tillering. Barley's relatively short season (90-110 
days) is advantage in moderate-retention soils - less time for nutrient losses compared to wheat 
or corn.

MALTING BARLEY ADVANTAGE: Moderate-retention soils can actually benefit malting barley production. 
Some N leaching helps prevent excessive protein accumulation. Can use slightly higher N rates 
(60-70 lb N/ac) at seeding with confidence some will leach, resulting in final protein 12-13% 
(ideal for malting). Reduces risk of protein being too low (<11.5%, poor enzyme levels).

TEST WEIGHT: Moderate retention may reduce test weights to 42-45 lb/bu without careful management. 
Split K applications important for kernel plumpness. Foliar K at boot stage provides supplemental 
insurance if soil test moderate.

SOIL IMPROVEMENT: Build OM through residue return (barley straw high-C/N, excellent for OM 
building) and cover crops after barley. Early maturity (July in most areas) allows long cover 
crop season, benefiting soil health. Each 1% OM increase improves retention.

CONSIDERATIONS: Barley somewhat more tolerant of moderate retention than wheat due to shorter 
season. Spring barley particularly well-adapted as all nutrients applied during active growth.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture provide 
poor storage but barley more viable than wheat at this retention level. Barley advantages: 
1) Lower N requirement (70-90 lb N/ac vs 90-110 for wheat). 2) Shorter season (90-100 days) 
reduces leaching time window. 3) Better tolerance of slightly acid pH (5.5-6.0) common in sandy 
soils. 4) More efficient nutrient use under stress.

MANAGEMENT STRATEGY: Frequent split N: 30-40 lb N/ac at seeding + 20-30 lb N/ac at tillering + 
20-30 lb N/ac at early boot (feed barley only). Malting barley: 40-50 lb N/ac at seeding + 
20-30 lb N/ac at tillering only if tissue test shows deficiency - protein still concerns even 
in low-retention soils due to concentration effect from lower yields. N stabilizers mandatory. 
Slow-release products for base application extend availability.

PHOSPHORUS-POTASSIUM: High P rate at seeding compensates for retention limitations. Use 50-60 lb 
P₂O₅ banded for early root development. K split into three applications. Foliar K at boot 
supplements soil applications and directly supports test weight.

FEED vs MALTING: Feed barley more suitable than malting in low-retention soils. Stress conditions 
(nutrient deficiency between applications, potential drought in sandy soils) make achieving 
consistent malting grade difficult. Feed barley market more forgiving of variable test weights 
and protein levels.

SOIL IMPROVEMENT: Barley good choice for building OM in low-retention soils. Early maturity 
allows cover crop establishment. Barley straw (if not harvested) adds significant OM. Consider 
barley in rotation with soil-building goals.

VIABILITY: Barley more viable than wheat in low-retention soils, less viable than grain sorghum 
or oats. Expect 50-70 bu/ac feed barley with intensive management. Still economically marginal 
for malting production.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC, very sandy profile 
provide almost no storage but barley still more viable than wheat at this extreme. Barley's 
short season (90-100 days) is major advantage - reduces leaching exposure time by 30-40% compared 
to winter wheat.

MANAGEMENT OPTIONS: Very frequent N applications: 20-30 lb N/ac at seeding + 15-20 lb N/ac at 
tillering + 15-20 lb N/ac at early boot + 10-15 lb N/ac at boot (feed only), total 60-80 lb N/ac. 
Fertigation through sprinkler irrigation ideal if available - weekly 10-15 lb N/ac injections 
from seeding through boot. Controlled-release N (120-day type) for base application only option 
for reducing frequency, though efficiency still <50%. All nutrients require weekly applications 
or slow-release products.

PHOSPHORUS-POTASSIUM-MICRONUTRIENTS: Despite leaching risk, adequate P at seeding essential. 
Apply 50-60 lb P₂O₅ banded. K split into 4-5 applications. Complete foliar nutrition program 
(biweekly K-S-micronutrients) required as soil reserves leach immediately.

FEED BARLEY ONLY: Malting barley production not feasible in very-low-retention soils. Cannot 
achieve consistent test weight (>48 lb/bu) or protein control (<13%) needed for malting market. 
Feed barley more realistic target, though still challenging.

ALTERNATIVE GRAINS: Consider alternatives better adapted to very-low-retention soils: 1) Oats - 
even shorter season (80-90 days), lower N requirement, excellent acid tolerance for sandy soils. 
2) Spring triticale - more stress tolerant than barley or wheat. 3) Grain sorghum - much deeper 
roots retrieve leached nutrients. 4) Annual ryegrass for forage - allows multiple cuts with 
small fertilizer applications each time.

SOIL IMPROVEMENT: If cropping these soils, use barley as transition/building crop. Early maturity 
allows long cover crop season. Plant cover crop immediately after harvest (July-August), grows 
through fall and spring, terminated following May. This plus barley straw return adds significant 
OM annually. Realistic timeline: 8-12 years to improve retention meaningfully.

VIABILITY: Barley marginally viable for 40-50 bu/ac feed production with intensive management 
and high input costs. Economics marginal except with high prices. Consider whether grain production 
appropriate land use vs. perennial forage, conservation, or other use."""
    },

    "Oats": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through oats' short season (80-100 days). Oats have relatively LOW nutrient requirements (70-90 lb N, 
40-60 lb P₂O₅, 50-70 lb K₂O for 100+ bu/ac) - lowest among major cereals. Can apply entire seasonal 
requirement in single pre-plant or at-seeding application with minimal loss due to short season and 
moderate rates. High retention advantageous but less critical than for higher-demanding crops.

MANAGEMENT STRATEGY: Single application at seeding typically adequate. Broadcast or banded N-P-K 
(80-90 lb N/ac) retained through short season. Oats' advantage: low nutrient demand means high-retention 
soils provide substantial natural fertility contribution through mineralization. May reduce fertilizer 
rates 10-20% compared to wheat or barley in these soils. Good choice for organic production where N 
sources limited - excellent soil exploits natural fertility effectively.

SOIL BUILDING: Oats excellent for improving soil in high-retention soils. Dense fibrous root system 
adds significant OM. Early maturity (July in most areas) allows long cover crop season after harvest. 
Oat straw (high C:N ratio) excellent for building soil structure and OM when incorporated. Consider 
oats in rotation to maintain/improve soil quality.

CONSIDERATIONS: In very high retention soils with high residual N (following legumes or heavy manure), 
may need to reduce N rates to prevent lodging (weak straw from excessive vegetative growth). Oats more 
prone to lodging than wheat or barley.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage 
through oats' short season. Oats' low nutrient requirements are advantage - single application at 
seeding usually sufficient. Apply 70-90 lb N/ac, 40-60 lb P₂O₅, 50-70 lb K₂O at or before seeding. 
Good retention ensures availability through 90-day season.

MANAGEMENT STRATEGY: Pre-plant or at-seeding application of full seasonal requirement. Split application 
optional - can apply 60-70% at seeding + 30-40% at tillering if heavy rain forecast at planting, but 
usually not necessary in good-retention soils. Oats' relatively low N requirement (about 80% of wheat's) 
means leaching risk minimal even in moderate-retention soils.

COMPARATIVE ADVANTAGE: Oats preferred over wheat or barley in good-retention soils when: 1) Following 
high-residual-N crop (risk of wheat/barley lodging; oats more tolerant). 2) Nurse crop for forage seeding 
(low N competition with establishing legumes). 3) Early feed need (oats mature 10-20 days before wheat). 
4) Acid soil conditions (oats most pH-tolerant cereal, pH 5.0-5.5 acceptable).

ENVIRONMENTAL: Very low leaching risk with oats' short season and moderate N rates in these soils. 
Excellent choice for environmental protection areas, buffer strips, or cover crop preceding sensitive 
crops.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for oats' short 
season and low nutrient requirements. This is oats' "sweet spot" - low N demand means leaching losses 
minimal even in moderate-retention soils. Single application at seeding usually adequate: 70-90 lb N/ac, 
40-50 lb P₂O₅, 50-60 lb K₂O.

MANAGEMENT STRATEGY: At-seeding application of full seasonal requirement. Split application optional 
benefit: 60% at seeding + 40% at tillering reduces any leaching risk in high-rainfall situations. 
Consider N stabilizers if planting into very wet conditions or heavy rain forecast. Oats particularly 
well-adapted to moderate-retention soils - excellent choice over wheat or barley at this retention level.

OATS ADVANTAGES IN MEDIUM-RETENTION SOILS: 1) Lower N requirement reduces leaching losses and costs. 
2) Short season (80-100 days) limits exposure time for nutrient losses. 3) Dense root system scavenges 
nutrients efficiently. 4) More forgiving than other cereals if early N application partially lost to 
leaching. 5) Excellent acid tolerance (pH 5.0-5.5) common in sandy moderate-retention soils.

SOIL IMPROVEMENT: Oats excellent transition crop for building moderate-retention soils. Fibrous roots 
improve structure. Early harvest allows cover crop establishment. Relatively weed-suppressive, helping 
clean fields for subsequent crops. Good choice in rotation for soil health goals.

CONSIDERATIONS: At moderate retention, oats more reliable than wheat or barley. Can achieve 70-90 bu/ac 
feed oats with basic fertilization program.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but oats BEST CEREAL CHOICE at 
this retention level. Oats' unique advantages critical in low-retention soils: 1) Lowest N requirement 
among cereals (60-80 lb N/ac vs 90-110 for wheat/barley). 2) Shortest season (80-90 days) - 30-40% 
shorter than winter wheat, reducing leaching exposure. 3) Best acid tolerance (pH 5.0-5.5 acceptable) - 
low-retention soils often sandy and acidic. 4) Most efficient nutrient use under stress.

MANAGEMENT STRATEGY: Split N application: 40-50 lb N/ac at seeding + 30-40 lb N/ac at tillering. Smaller 
applications reduce individual losses. N stabilizers beneficial for base application. P banded at seeding 
(40-50 lb P₂O₅) for early root development. K split: 40 lb K₂O at seeding + 30 lb K₂O at tillering. 
Even with splits, oats more forgiving than wheat/barley if some N lost.

ROOT SYSTEM ADVANTAGE: Oats' extremely fibrous root system (more dense branching than wheat/barley) 
excellent for scavenging nutrients from low-retention soils. Roots explore larger soil volume, intercepting 
nutrients before leaching beyond reach. This makes oats significantly more reliable than other cereals.

SOIL IMPROVEMENT: Oats ideal for building low-retention soils. Massive fibrous root system adds substantial 
OM (more root biomass per unit weight than wheat). Early maturity critical advantage - plant cover crop 
immediately after harvest (late July typically), grows through fall and following spring, terminated next 
May. This oat-cover crop system adds significant annual OM, building retention over 3-5 years.

VIABILITY: Oats economically viable for 50-70 bu/ac feed production in low-retention soils with basic 
management. More reliable and lower cost than wheat/barley. If growing small grain in low-retention soil, 
oats is the choice.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but oats STILL MOST VIABLE CEREAL 
GRAIN option. Oats' combination of low N requirement, short season, excellent acid tolerance, and superior 
root system makes it only cereal with reasonable chance in very-low-retention soils. Still challenging but 
feasible where wheat/barley impossible.

MANAGEMENT OPTIONS: Frequent split N: 30-40 lb N/ac at seeding + 20-30 lb N/ac at tillering + 20-30 lb 
N/ac at early boot, total 70-90 lb N/ac. Weekly applications ideal if feasible (10-15 lb N/ac per week 
from seeding to boot, 6-7 applications). Fertigation through sprinkler if available - biweekly injections 
10-15 lb N/ac. Controlled-release N (90-120 day type) for base application only option for reducing frequency, 
though efficiency still <50%.

ROOT ADVANTAGE: Oats' root system superior scavenger in sandy very-low-retention soils. Extremely dense 
fibrous root mass intercepts nutrients across wide area and multiple depths before leaching. Can retrieve 
some nutrients from 3-4 ft depth (unusual for small grain). This unique capability makes oats viable where 
other cereals fail completely.

SEASON ADVANTAGE: Oats' 80-90 day season is 50-60% shorter than winter wheat (270 days), 25-30% shorter 
than spring wheat (110-120 days). Dramatically reduces time window for nutrient losses. All applications 
during active growing season further reduces losses vs winter wheat with fall/winter loss exposure.

ACID TOLERANCE: Critical advantage in very sandy soils often extremely acidic (pH 4.5-5.5). Oats tolerates 
pH 5.0 adequately, pH 5.5 well - better than any other cereal. Wheat/barley fail below pH 5.5. This alone 
may make oats only viable cereal option regardless of retention considerations.

VIABILITY: Oats marginally viable for 40-50 bu/ac feed production with intensive management. Economics 
marginal but better than any other cereal. If cropping very-low-retention soil with grain, oats only 
reasonable choice. Alternatives: pearl millet (even shorter season, better drought tolerance), annual 
ryegrass for forage (allows multiple cuts with small fertilizer applications each time).

SOIL IMPROVEMENT: Use oats as building crop. Massive root system turnover adds significant OM annually. 
With continuous cover cropping after early harvest, can improve very-poor soils meaningfully over 8-12 
years. Long-term strategy: build retention with oats-cover crop rotation for decade, then transition to 
higher-value crops."""
    },

    "Rice": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
but rice unique - flooded conditions dramatically alter nutrient dynamics. Flooding creates ANAEROBIC 
(oxygen-free) conditions fundamentally changing nutrient retention and availability. High CEC benefits: 
1) Excellent cation retention (K, Ca, Mg, NH4) even under flood. 2) Reduced P fixation as Fe/Al oxides 
reduced under flooding, releasing previously fixed P. 3) Good micronutrient buffering capacity. 

MANAGEMENT STRATEGY: Pre-flood N application (40-50% of total, 60-80 lb N/ac) incorporated before flooding 
provides base. High CEC retains NH4 (ammonium form under flooded anaerobic conditions) against losses. 
Mid-season N topdressing (30-40%, 50-60 lb N/ac) at panicle initiation. Late N application (10-20%, 
20-30 lb N/ac) at heading for grain fill. Total: 130-170 lb N/ac for 7,000-9,000 lb/ac. High retention 
reduces mid-season and late-season N requirements - some systems use only pre-flood + mid-season in 
high-CEC soils.

FLOODED CONDITIONS EFFECTS: Organic matter decomposition slows under anaerobic conditions but continues, 
providing slow steady N release throughout season. High-retention soils with good OM (>2%) provide 50-80 lb 
N/ac through mineralization over season. P becomes MORE available under flooding as Fe-bound P released 
(Fe3+ reduced to Fe2+, releasing P). K, Ca, Mg well retained but some K loss through flood water drainage.

ENVIRONMENTAL: High retention combined with flood water retention minimizes N losses to environment. 
Denitrification occurs (anaerobic conditions convert NO3 to N2 gas) but less problematic than in aerobic 
cropping because N managed as NH4. Some N loss in flood water drainage but high CEC minimizes this.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage under 
flooded rice conditions. Standard rice belt fertilization practices work well. Pre-flood N (50-60% of 
total, 70-90 lb N/ac) + mid-season topdress (30-40%, 40-60 lb N/ac) + optional heading application 
(10-20%, 15-30 lb N/ac). Total: 125-180 lb N/ac for 6,000-8,000 lb/ac.

MANAGEMENT STRATEGY: Incorporate pre-flood N (urea, ammonium sulfate) 1-2 weeks before permanent flood 
establishment. Good retention holds NH4 against leaching losses. Flood water acts as barrier reducing 
volatilization losses compared to aerobic conditions. Mid-season topdress as urea broadcast into flood 
water or injected near soil surface. Some volatilization loss from flood water surface but moderate 
retention recaptures significant portion.

PHOSPHORUS-POTASSIUM: Pre-flood broadcast P (40-60 lb P₂O₅/ac) and K (60-80 lb K₂O/ac). Flooding makes P 
more available - even moderate-retention soils release Fe-bound P under reduction. K well retained but 
some loss in flood water drainage - consider split application (60% pre-flood + 40% mid-season topdress) 
in flood-and-drain systems.

SULFUR: Important for rice quality (protein content, milling quality). Apply 20-30 lb S/ac pre-flood. 
Sulfate reduced to sulfide under flooding - some loss as H2S gas but high-retention soils buffer against 
excessive losses. Ammonium sulfate as N source provides dual N-S benefit.

CONSIDERATIONS: Flood water management affects retention. Continuous flood systems retain nutrients better 
than flood-and-drain systems. In good-retention soils, can manage with less frequent drainage cycles.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful N management 
under flooded conditions. Rice unique challenge: moderate retention limits pre-flood NH4 holding capacity, 
increasing mid-season N needs. Multiple split N applications essential: pre-flood (40-50%, 60-70 lb N/ac) + 
mid-season (30-40%, 50-60 lb N/ac) + heading (20-30%, 30-40 lb N/ac). Total: 140-170 lb N/ac.

MANAGEMENT STRATEGY: Smaller pre-flood application reduces risk of NH4 leaching or denitrification losses 
before flood established. Larger mid-season applications compensate. Consider nitrification inhibitors 
with pre-flood N to prevent conversion of NH4 to NO3 (which denitrifies readily under flooding). Deep 
placement of N (2-3 inches below soil surface) at pre-flood or mid-season reduces volatilization and 
enhances retention in moderate-CEC soils.

PHOSPHORUS MANAGEMENT: Moderate-retention soils still benefit from P release under flooding but less 
dramatic than high-retention soils. Apply higher P rates (50-70 lb P₂O₅/ac) pre-flood to compensate. 
Banded P at drill seeding more efficient than broadcast in moderate-retention soils.

FLOOD WATER MANAGEMENT: Critical in moderate-retention soils. Minimize drainage events - each drain-dry 
cycle causes N losses through nitrification-denitrification. Continuous flood where practical. If must 
drain (weed control, mid-season aeration), time drainage to avoid period right after topdress N application. 
Re-establish flood quickly to minimize aerobic phase.

SOIL IMPROVEMENT: Build OM through residue return, winter cover crops (vetch, clover), organic amendments. 
Rice production with flooded conditions naturally builds OM over time (slow decomposition), improving 
retention for subsequent crops.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC creates challenges even under 
flooded conditions. Limited NH4 retention capacity means high N losses despite flooding. Very frequent 
split N applications required: pre-flood minimal (20-30%, 30-40 lb N/ac) + multiple mid-season applications 
(every 2-3 weeks, 20-30 lb N/ac each, 3-4 applications). Total: 140-180 lb N/ac for 4,000-6,000 lb/ac.

MANAGEMENT STRATEGY: Deep N placement (2-4 inches below surface) critical for retention in low-CEC soils. 
Broadcast N into flood water has extreme volatilization losses (>50%) in these soils. Use injection equipment 
or hand-placed super granules of urea placed deep near plants. Split applications every 2-3 weeks from 
tillering through heading maintain plant nutrition despite poor soil retention.

SPECIAL CONSIDERATION - LIGHT TEXTURE: Low-retention rice soils usually sandy texture. Problems: 1) Flood 
water seepage/percolation losses carry NH4 with them. 2) Difficulty maintaining consistent flood depth - 
fluctuating water table causes nutrient concentration changes. 3) Fe/Mn deficiency common in sandy flooded 
soils despite anaerobic conditions. 4) Poor soil structure makes establishing smooth levees difficult.

PHOSPHORUS-POTASSIUM: High rates needed (60-80 lb P₂O₅/ac, 80-100 lb K₂O/ac) to overcome poor retention. 
All pre-flood, incorporated. K split: 60% pre-flood + 40% mid-season topdress to compensate for losses in 
seepage water. Foliar K applications late season supplement soil K.

VIABILITY: Rice production challenging in low-retention soils. High inputs, intensive management, yet 
moderate yields. Common in regions with sandy rice soils (Gulf Coast, some California areas) but requires 
sophisticated management. Consider whether rice economically viable vs alternative crops.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes rice production extremely 
challenging even with flooding benefits. Very sandy texture causes multiple problems: severe flood water 
seepage (impossible to maintain consistent flood), extreme NH4 leaching with seepage water, poor levee 
formation, Fe/Mn deficiency despite anaerobic conditions.

MANAGEMENT OPTIONS: Rice generally not viable in very-low-retention soils. If attempted: intensive deep 
placement program. All N applied as super granules (large urea granules) hand-placed or mechanically 
injected 3-4 inches deep next to plants. Multiple applications (4-6 times through season, 20-30 lb N/ac 
each, total 120-180 lb N/ac). Deep placement only method achieving any efficiency in these soils - broadcast 
into flood water >70% loss.

WATER MANAGEMENT CRISIS: Very sandy soils cannot maintain flood. Seepage rates >2 inches/day exceed 
practical pumping capacity. Fluctuating water levels stress plants and concentrate/dilute nutrients 
unpredictably. Heavy clay additions (100+ tons/ac) sometimes attempted to seal fields but extremely 
expensive and not always successful. Plastic/bentonite liners prohibitively expensive for field-scale 
production.

ALTERNATIVE CONSIDERATION: Furrow-irrigated dry-seeded "rice" production avoiding flood. Actually aerobic 
production with frequent irrigation. Requires completely different management (like irrigated wheat) and 
different varieties. Yields typically 40-60% of flooded rice but may be only viable approach in very-low-
retention soils. Or reconsider whether rice appropriate crop vs alternatives better adapted to soil.

VIABILITY: Conventional flooded rice production not viable. Multiple insurmountable challenges in very-low-
retention soils. Recommend alternative crops or non-rice use of land. If must grow rice: furrow-irrigated 
dry-seeded system only possibility, but recognize this is fundamentally different production system with 
lower yields and different economics."""
    },

    "Sunflower": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through sunflower's 100-120 day season. Sunflowers have MODERATE nutrient requirements compared to most 
row crops (80-120 lb N, 40-60 lb P₂O₅, 60-80 lb K₂O for 2,000-3,000 lb/ac seed). Major advantage: deep 
tap root (5-6 ft common, up to 10 ft) with extensive lateral root system makes sunflowers excellent 
nutrient scavengers. High retention combined with extensive roots = efficient nutrient use.

MANAGEMENT STRATEGY: Single pre-plant application of full seasonal N-P-K requirement usually adequate. 
Broadcast or banded, incorporated. Sunflowers' deep roots recover any nutrients that move downward, so 
leaching risk minimal even if heavy early-season rain. Optional side-dress N at early flowering if 
vegetative growth appears weak, but rarely needed in high-retention soils with adequate pre-plant 
application. 

SUNFLOWER ADVANTAGES IN HIGH-RETENTION SOILS: 1) Low fertilizer requirement compared to corn/soybeans 
reduces costs. 2) Deep roots access subsoil nutrients other crops cannot reach. 3) Excellent scavenging 
of residual nutrients from previous crops - good rotation crop following heavily fertilized vegetables 
or potatoes. 4) Drought tolerance - deep roots access deep moisture along with nutrients. 5) Short-season 
option for late planting following winter wheat or early vegetable harvest.

SULFUR: Important nutrient for sunflowers (10-20 lb S/ac). High oil content requires adequate S. Ammonium 
sulfate as N source provides both nutrients. Or gypsum if using urea N source. High-retention soils hold 
sulfate better than sandy soils.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage through 
sunflower season. Standard sunflower fertilization practices work well. Pre-plant application of 80-120 lb 
N/ac, 40-60 lb P₂O₅, 60-80 lb K₂O retained through season. Sunflowers' deep root system particularly 
valuable - recovers nutrients from deep in profile if any downward movement occurs.

MANAGEMENT STRATEGY: Pre-plant broadcast or banded application of full seasonal requirement. Split N 
optional - can apply 70-80% pre-plant + 20-30% side-dress at early bud stage if concerned about loss 
from heavy rainfall, but usually not necessary. P banded at planting more efficient than broadcast in 
moderate-high retention soils. K broadcast and incorporated.

ROTATION CONSIDERATIONS: Sunflowers excellent rotation crop in good-retention soils. Benefits following 
crops: 1) Deep roots break compaction, improve soil structure. 2) Deep roots recover deep nutrients, 
reducing leaching to groundwater. 3) Residue decomposition releases nutrients for following crop. 4) 
Disease break for cereals and soybeans. 5) Late maturity (Sept-Oct) allows fall cover crop establishment 
for further soil improvement.

COMPARATIVE ADVANTAGE: In good-retention soils, sunflowers economically competitive with soybeans (similar 
revenue potential) while improving soil. Higher drought tolerance than soybeans makes sunflowers more 
reliable in semi-arid regions with moderate retention.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC but sunflowers well-adapted 
to these soils. Sunflowers' unique characteristics make them BETTER suited to moderate-retention soils 
than most other row crops: 1) Deep tap root system (5-8 ft typical) recovers mobile nutrients before 
they leach beyond reach. 2) Moderate N requirement reduces total amount potentially lost. 3) Excellent 
drought tolerance common in moderate-retention (often sandy) soils. 4) Wide adaptability to pH 6.0-8.5 
handles varied soil conditions.

MANAGEMENT STRATEGY: Pre-plant application adequate: 80-110 lb N/ac, 40-50 lb P₂O₅, 60-80 lb K₂O. Consider 
N split if planting into very wet soil: 70-80% pre-plant + 20-30% side-dress at early bud. P banded at 
planting maximizes efficiency. In moderate-retention soils, sunflowers' deep roots critical advantage - 
intercept nutrients at 2-4 ft depth that annual crops cannot reach.

SUNFLOWERS IDEAL FOR MODERATE-RETENTION SOILS: Common situations where sunflowers excel: 1) Sandy loam 
soils too droughty for corn in dry years. 2) Rotation crop for building moderate-retention soils - adds 
deep OM through root turnover. 3) Saline or alkaline moderate-retention soils (pH 7.5-8.5) where other 
crops struggle - sunflowers tolerate high pH better than corn or soybeans. 4) Following heavily fertilized 
potatoes or vegetables - sunflower roots recover deep residual N.

ECONOMICS: Lower input costs than corn (less fertilizer, seed, often no insecticide) with comparable 
net returns in moderate-retention soils where corn yields limited by water/nutrient stress.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but sunflowers EXCELLENT CHOICE 
for low-retention soils. Sunflowers' combination of deep roots, moderate nutrient needs, and excellent 
drought/stress tolerance makes them one of the best row crops for low-retention conditions. Often out-
perform corn and soybeans economically in these challenging soils.

MANAGEMENT STRATEGY: Split N application: 60-70% pre-plant (60-80 lb N/ac) + 30-40% side-dress at early 
bud stage (30-40 lb N/ac). P banded at planting (40-60 lb P₂O₅) critical for early root development. 
K split: 50 lb K₂O pre-plant + 30 lb K₂O side-dress. Even with low retention, sunflowers' deep roots 
recover significant nutrients from 3-5 ft depth that moved downward with rainfall/irrigation.

CRITICAL ADVANTAGE - DEEP ROOTS: In low-retention sandy soils, sunflowers' ability to root 6-8 ft deep 
is game-changer. Corn/soybeans primarily feed from 0-3 ft. Nutrients that leach below this zone are 
lost to them but still available to sunflowers. This means sunflowers effectively have higher "retention" 
than retention rating suggests - the plant-soil system retains nutrients even if soil alone does not.

DROUGHT TOLERANCE: Critical in low-retention soils typically sandy and droughty. Sunflowers maintain 
production with 40-60% less water than corn. Deep roots access moisture other crops cannot reach. This 
makes sunflowers viable where corn fails in dry years. Insurance advantage in marginal situations.

SOIL IMPROVEMENT: Deep root system turnover adds OM deep in profile, improving retention over time. 
Thick stalks, large leaves add substantial surface residue. Good choice for building low-retention soils 
over 5-10 years while maintaining economically viable production.

VIABILITY: Sunflowers fully viable and often preferred choice for 2,000-2,500 lb/ac production in low-
retention soils with split fertilization program. Economics often better than corn or soybeans in these 
conditions.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but sunflowers STILL VIABLE where 
most row crops fail. Sunflowers' unique adaptations allow production in very-low-retention soils: 1) Deep 
roots (6-10 ft) recover nutrients from extreme depth. 2) Exceptional drought tolerance allows production 
in very sandy soils without irrigation. 3) Lower nutrient requirement than corn reduces total loss. 4) 
Wide pH tolerance (6.0-8.5) handles variable very-sandy-soil conditions.

MANAGEMENT OPTIONS: Frequent split N: 40-50 lb N/ac pre-plant + 30-40 lb N/ac at 6-leaf stage + 20-30 lb 
N/ac at early bud, total 90-120 lb N/ac. Smaller applications reduce individual losses. Controlled-release 
N for base application improves efficiency. P-K at planting in bands close to seed: 40-50 lb P₂O₅, 50-60 lb 
K₂O retained better when banded.

ROOT SYSTEM ADVANTAGE: Sunflowers' massive root system in very sandy soils extends 8-10 ft deep, 4-6 ft 
laterally. Extremely large root biomass intercepts nutrients across wide area and deep profile. Can recover 
nutrients from 6-8 ft depth that moved beyond reach of other crops. This unique ability makes sunflowers 
viable where other row crops impossible.

IRRIGATION CONSIDERATION: Sunflowers unique among row crops - can produce without irrigation in very sandy 
soils if rainfall >18 inches growing season. Deep roots access deep soil moisture. Corn/soybeans require 
irrigation in these soils, adding cost. Sunflowers' dryland capability significant economic advantage.

ALTERNATIVE SYSTEMS: Subsurface drip fertigation for high-value confectionery sunflower production. Small 
frequent N injections (5-10 lb N/ac weekly from 6-leaf through flowering). Achieves higher yields and 
quality than split dry fertilizer applications. Economics require confectionery sunflower prices ($0.40-0.60/lb) 
vs oilseed ($0.20-0.30/lb).

VIABILITY: Sunflowers viable for 1,500-2,000 lb/ac oilseed production with split fertilization. More viable 
than corn or soybeans in very-low-retention soils. If growing row crop in these conditions, sunflowers 
first choice. Economics competitive with dryland wheat, better than most alternatives."""
    },

    "Canola": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through canola's overwintering season (fall planted) or spring season (spring canola). Canola has HIGH 
nutrient requirements (120-180 lb N, 60-80 lb P₂O₅, 80-100 lb K₂O for 2,500-4,000 lb/ac seed) - comparable 
to corn. High oilseed production requires substantial nutrients, particularly N for protein and oil content.

WINTER CANOLA MANAGEMENT: Split N critical despite high retention. Fall application minimal (30-40 lb N/ac) 
for establishment and fall growth. Winter period with slow growth allows mineralization accumulation. Spring 
topdress (80-140 lb N/ac) in split applications: 50-60% at greenup/rosette + 40-50% at bolting/early bloom. 
High retention holds spring N through flowering and seed fill periods (May-July). P-K applied at fall planting.

SPRING CANOLA MANAGEMENT: Split N: 40-50% at planting + 30-40% at rosette (4-6 leaf) + 20-30% at bolting. 
Shorter growing season (90-100 days) but intensive N demand during rapid spring growth. High retention 
allows these relatively large applications without significant loss.

SULFUR: Critical nutrient for canola - oilseed production requires high S (20-40 lb S/ac). Canola has 
highest S requirement of common crops. Apply in fall (winter canola) or at spring planting. Ammonium 
sulfate provides N-S combination. High-retention soils hold sulfate better through long season.

ENVIRONMENTAL: High retention important given canola's heavy N requirement and spring application timing 
(period of high precipitation in many regions). Good retention minimizes environmental impact from intensive 
fertilization program required for oilseed production.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage through 
canola season. Standard commercial practices work well. Winter canola: 30-40 lb N/ac fall + 80-120 lb N/ac 
spring (split at greenup and bolting). Spring canola: split 40-50% at planting + 30-40% at rosette + 
20-30% at bolting, total 120-160 lb N/ac.

MANAGEMENT STRATEGY: Winter canola benefits from fall P-K application (60-80 lb P₂O₅, 80-100 lb K₂O) 
retained through winter and available for spring growth surge. Spring canola: all P-K at planting, banded 
preferred for P efficiency. S application at planting or with first N application (20-30 lb S/ac) - adequate 
retention through season.

TIMING CONSIDERATIONS: Spring N application timing critical for winter canola. Too early (before greenup) 
in moderate-high retention soils can lead to excessive vegetative growth and lodging. Properly timed 
applications (late March-April in most regions) align N availability with rapid stem elongation phase.

YIELD POTENTIAL: In good-retention soils, canola competitive with wheat and corn for net returns. Premium 
prices for food-grade canola oil justify intensive management. High retention supports yields of 2,500-3,500 
lb/ac winter canola, 2,000-3,000 lb/ac spring canola.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful N management 
through canola's demanding season. Canola's high N requirement (120-160 lb N/ac) combined with moderate 
retention necessitates frequent split applications to minimize losses while maintaining plant nutrition.

WINTER CANOLA MANAGEMENT: Fall application minimal (20-30 lb N/ac) - only for establishment, reduce loss 
risk over winter. Spring N in multiple splits: 40-50 lb N/ac at greenup + 40-50 lb N/ac at rosette + 30-40 lb 
N/ac at bolting, total 110-140 lb N/ac. More splits reduce individual application size, reducing leaching 
risk in moderate-retention soils.

SPRING CANOLA MANAGEMENT: Three-way split: 40-50% at planting + 30-40% at rosette + 20-30% at bolting. 
Consider N stabilizers with base application to reduce nitrification and subsequent leaching losses. ESN 
(polymer-coated controlled-release urea) for portion of base application provides steady release through 
season.

SULFUR MANAGEMENT: Particularly important in moderate-retention soils often sandy and S-deficient. Apply 
20-30 lb S/ac at planting. Ammonium sulfate as N source provides dual N-S benefit. Monitor tissue S levels 
mid-season - if deficient, foliar S application rescues crop.

SOIL TEXTURE CONSIDERATION: Moderate-retention canola soils often sandy loam to loam texture. Adequate 
for canola if pH suitable (6.0-7.5). Canola tap root relatively deep (3-4 ft) helps scavenge nutrients in 
these soils. Not as effective as sunflower but better than soybeans for nutrient recovery.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes canola production challenging. 
Canola's high N requirement (120-160 lb N/ac) combined with low retention creates significant loss risk 
and economic challenges. Frequent split applications required but labor/cost intensive.

MANAGEMENT STRATEGY: Winter canola minimal fall N (20-30 lb N/ac). Spring N in 4 split applications: 
30-40 lb N/ac at greenup + 30-40 lb N/ac at rosette + 30-40 lb N/ac at bolting + 20-30 lb N/ac at early 
flowering, total 110-150 lb N/ac. Spring canola: four applications from planting through flowering, 
30-40 lb N/ac each. N stabilizers and controlled-release N essential for efficiency.

SPECIAL CONSIDERATION - SANDY SOILS: Low-retention canola soils typically sandy texture. Problems: 1) 
Poor moisture retention compounds nutrient stress. 2) Often acidic (pH<6.0) - canola sensitive to acidity, 
clubroot disease severe in acidic conditions. 3) Low OM common in sandy soils - reduces natural N supply 
through mineralization. 4) Boron deficiency common in sandy low-retention soils - canola B requirement 
relatively high (1-2 lb B/ac).

ECONOMIC VIABILITY: Canola marginally viable in low-retention soils. High N requirement + high loss rate = 
expensive fertilization program (often $80-120/ac N costs vs $40-60/ac in high-retention soils). Yields 
reduced (1,500-2,500 lb/ac vs 2,500-3,500 lb/ac in better soils) while costs higher. Economics work only 
with premium prices or crop insurance support.

ALTERNATIVES: Consider wheat or sunflower in low-retention soils - both have lower N requirements and 
better adapted to challenging soil conditions. If canola desired (rotation benefits, market opportunities), 
recognize intensive management required and marginal economics.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes canola production economically 
non-viable in most situations. Canola's combination of high N requirement, sensitive root system, disease 
susceptibility, and moderate drought tolerance all problematic in very-low-retention soils.

MANAGEMENT OPTIONS: If attempting canola: Winter canola abandoned - overwinter survival poor in very sandy 
soils (frost heaving, poor moisture retention). Spring canola only option. Intensive fertigation program: 
weekly injections through drip or center pivot, 15-25 lb N/ac per week from 4-leaf through flowering (8-10 
applications, total 120-180 lb N/ac). Controlled-release N for base application + frequent supplemental 
applications. Economics prohibitive unless premium price available.

LIMITING FACTORS BEYOND RETENTION: Very-low-retention soils typically very sandy. Multiple problems for 
canola: 1) Clubroot disease severe in acidic sandy soils - canola extremely susceptible. 2) Poor moisture 
retention - canola has moderate drought tolerance but insufficient for very sandy soils without irrigation. 
3) Boron deficiency universal in very sandy soils - canola high B requirement. 4) Poor seedbed - canola 
tiny seed requires firm, fine seedbed difficult to achieve in very sandy soil. 5) Frost heaving winter 
canola in loose sandy soil.

DISEASE CONSIDERATIONS: Very sandy soils often acidic (pH 5.0-6.0). Clubroot (Plasmodiophora brassicae) 
thrives in acidic conditions and devastates canola. Once introduced, persists decades. Blackleg (Leptosphaeria 
maculans) also problematic. Disease management alone may make canola non-viable regardless of fertilizer 
issues.

VIABILITY: Canola production not recommended in very-low-retention soils. Multiple insurmountable challenges 
beyond just nutrient retention. If oilseed production desired, consider sunflower (much better adapted to 
very sandy conditions). If brassica crop desired for rotation, consider forage turnips or radishes (much 
more forgiving than canola)."""
    },

    "Dry Beans": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
but dry beans have UNIQUE characteristics - as legumes, they fix atmospheric N, reducing or eliminating 
N fertilizer requirement. Beans primary needs: P (40-80 lb P₂O₅/ac) and K (60-100 lb K₂O/ac), both well 
retained in high-CEC soils. High retention major advantage for P - beans sensitive to P deficiency during 
early vegetative growth and flowering.

MANAGEMENT STRATEGY: Pre-plant P-K broadcast or banded, no additional applications needed through season. 
N management unique: starter N (10-20 lb N/ac) at planting assists establishment before nodulation begins. 
Then bean's rhizobia bacteria fix N (60-150 lb N/ac depending on variety and conditions). Excessive N 
fertilizer (>30 lb N/ac total) inhibits nodulation, reduces N fixation, lowers economics. High retention 
soils with good OM (>2.5%) may not need any N fertilizer - mineralization provides adequate starter N.

NODULATION MANAGEMENT: High-retention soils often support excellent nodulation. Good soil structure, adequate 
Ca and Mo (micronutrient) present in high-CEC soils. Inoculate seed with appropriate Rhizobium phaseoli 
strain if beans not grown recently (>3 years). Successful nodulation: beans fix 60-150 lb N/ac, 50-80% of 
plant N requirement, significant cost savings.

SULFUR-MICRONUTRIENTS: Beans require adequate S (10-15 lb S/ac), Zn (1-2 lb Zn/ac), B (0.5-1 lb B/ac). 
High-retention soils often adequate in micronutrients but test to verify. Sulfate well retained in high-CEC 
soils - single application adequate.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
bean P-K requirements. Standard dry bean practices: minimal N (0-20 lb N/ac starter), moderate P (40-60 lb 
P₂O₅/ac), moderate K (60-80 lb K₂O/ac). P-K pre-plant broadcast or banded.

MANAGEMENT STRATEGY: Limit N fertilizer to minimize interference with N fixation. Starter N (10-20 lb N/ac) 
acceptable if soil cold at planting or OM low (<2%). Most bean N from fixation. Inoculate seed with Rhizobium 
if beans not in rotation recently. Good nodulation provides 80-120 lb N/ac fixed, sufficient for 1,500-2,500 
lb/ac yield.

PHOSPHORUS IMPORTANCE: Beans very sensitive to P deficiency, especially during flowering/pod set. P banded 
at planting (40-60 lb P₂O₅/ac) ensures early availability. In moderate-high retention soils, banding efficiency 
excellent - P held near roots, minimal tie-up. Adequate P improves nodulation, N fixation, and pod set.

VARIETY CONSIDERATIONS: Black beans, pinto beans, navy beans, kidney beans, great northern - all manageable 
with standard fertilization program in good-retention soils. Variety selection based on market demands rather 
than soil limitations at this retention level.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for bean production 
with careful P management. Beans well-adapted to moderate-retention soils - short season (80-100 days), 
moderate nutrient requirements, N fixation reduces fertilizer needs. More forgiving than many row crops.

MANAGEMENT STRATEGY: Minimal N (0-20 lb N/ac starter only). P banded at planting (40-60 lb P₂O₅/ac) 
critical - banding essential in moderate-retention soils to prevent P loss through fixation by Fe/Al oxides. 
K broadcast (60-80 lb K₂O/ac) or banded. Single application adequate through short season.

PHOSPHORUS MANAGEMENT: P availability critical for beans. Moderate-retention soils often sandy with Fe/Al 
oxides that fix P, making it unavailable. Banded P (2-3 inches to side, 2-3 inches below seed) places P 
where roots can access before fixation occurs. Consider higher rates (60-80 lb P₂O₅/ac) in moderate-retention 
soils to compensate for partial fixation.

NODULATION CHALLENGES: Moderate-retention soils sometimes problematic for nodulation: 1) Sandy soils often 
low pH (<6.0) - lime to pH 6.2-6.5 for optimal nodulation. 2) Low Mo availability in acidic moderate-retention 
soils - Mo essential for nitrogenase enzyme. Apply 0.1-0.2 lb Mo/ac if pH <6.2. 3) Inoculation essential - 
native rhizobia populations lower in moderate-retention soils.

ECONOMIC ADVANTAGE: Beans' N-fixing ability major economic advantage in moderate-retention soils. Corn or 
wheat in these soils require 100-150 lb N/ac ($60-90/ac cost, significant losses). Beans require minimal 
N fertilizer, fix their own. This reduces input costs and environmental impact.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but beans still reasonable option. 
Beans' N-fixing ability major advantage - eliminates primary nutrient loss concern (N leaching). Primary 
challenges: P retention and nodulation reliability in low-retention (typically sandy) soils.

MANAGEMENT STRATEGY: No N fertilizer (0-10 lb N/ac maximum) - even minimal N suppresses nodulation in 
low-retention soils. P banded essential: 60-80 lb P₂O₅/ac placed 2 inches to side and below seed. Banding 
critical in low-retention soils where P fixation and leaching both occur. K split possible if concerned 
about leaching: 50 lb K₂O/ac at planting + 30 lb K₂O/ac at early flowering.

NODULATION MANAGEMENT: Critical in low-retention soils. Challenges: 1) Sandy low-retention soils typically 
acidic (pH 5.0-6.0) - lime to pH 6.5 essential for nodulation. 2) Low Mo availability - apply 0.2-0.3 lb 
Mo/ac as foliar spray at 4-6 trifoliate leaf stage. 3) Ca deficiency common in sandy soils - apply gypsum 
200-300 lb/ac at planting for Ca. 4) Always inoculate seed - native rhizobia populations inadequate. 
5) Avoid soil compaction - roots and nodules require good aeration.

VARIETY SELECTION: Choose varieties specifically bred for sandy soil adaptation. Characteristics: strong 
root systems, moderate maturity (90-100 days allows early harvest before fall rains in sandy soils), 
resistance to common diseases in sandy conditions (white mold, rust).

ECONOMIC VIABILITY: Beans viable in low-retention soils due to N-fixing ability. Input costs moderate 
compared to N-dependent crops. Yields 1,000-1,800 lb/ac achievable with good management. Economics competitive 
with small grains, better than corn in these challenging soils.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but beans worth considering despite 
challenges. Beans' N-fixing ability means primary leaching concern (N) not applicable. Challenges focus 
on P retention, nodulation reliability, and general plant stress in very sandy conditions.

MANAGEMENT OPTIONS: Absolutely no N fertilizer - any N application suppresses nodulation. P management 
critical: banded placement mandatory, 60-80 lb P₂O₅/ac placed close to seed (2x2 band - 2 inches to side, 
2 inches below). Even with banding, P efficiency <40% in very-low-retention soils. Consider higher rates 
(80-100 lb P₂O₅/ac) to compensate. K fertigation if drip irrigation available - small frequent applications. 
Dry fertilization: split 40 lb K₂O/ac at planting + 30 lb K₂O/ac at flowering + 20 lb K₂O/ac at pod fill.

NODULATION CHALLENGES: Severe in very-low-retention soils. Multiple problems: 1) Extreme acidity common 
(pH 4.5-5.5) - lime heavily to pH 6.5-7.0. 2) Very low Mo - foliar application essential (0.3-0.5 lb Mo/ac). 
3) Ca deficiency severe - gypsum 400-600 lb/ac at planting. 4) Poor soil structure, low aeration stress 
nodules. 5) Moisture stress in sandy soil disrupts nodulation. Despite inoculation, nodulation success rate 
<60% in very-low-retention soils.

IRRIGATION REQUIREMENT: Beans generally drought-sensitive, very-low-retention soils drought-prone. Irrigation 
virtually mandatory for reliable production. Drip or sprinkler. Advantage: can fertigate P-K through 
irrigation system, improving efficiency. Weekly fertigation: 5-10 lb K₂O/ac from flowering through pod fill.

VARIETY SELECTION: Choose short-season varieties (80-90 days) to minimize stress duration. Bush types better 
than climbing types (less moisture demand). Disease-resistant varieties essential - white mold severe in 
sandy irrigated conditions.

VIABILITY: Beans marginally viable in very-low-retention soils with irrigation and intensive management. 
Economics marginal due to irrigation costs, high P rates, inoculant costs, Ca/Mo applications, yet moderate 
yields (800-1,500 lb/ac). Consider whether beans appropriate vs alternatives better adapted to very sandy 
conditions (sunflowers, peanuts in southern areas)."""
    },

    "Peanuts": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
but peanuts have UNIQUE characteristics combining two advantages: 1) Legume N fixation capability (80-150 lb 
N/ac fixed), and 2) Deep tap root (3-5 ft) with extensive lateral root system. High retention particularly 
critical for Ca - peanuts have HIGHEST Ca requirement of common crops (30-50 lb Ca/ac). Ca must be available 
in fruiting zone (top 3-4 inches soil) for proper pod fill and prevention of "pops" (unfilled pods).

MANAGEMENT STRATEGY: Minimal N (0-20 lb N/ac starter maximum). High-retention soils with good OM (>2%) may 
need no N - mineralization provides adequate starter before nodulation. P-K broadcast: 40-80 lb P₂O₅/ac, 
80-120 lb K₂O/ac (peanuts moderately K-intensive). CALCIUM management critical: apply gypsum (300-600 lb/ac) 
at early bloom and again 3-4 weeks later. Gypsum provides Ca AND sulfate (S), both needed. High retention 
keeps Ca available in fruiting zone through 3-4 month pod fill period.

NODULATION: Peanuts excellent N-fixers, requiring specific Rhizobium strain (Bradyrhizobium sp.). Always 
inoculate seed if peanuts not grown recently. High-retention soils with good structure support excellent 
nodulation. Successful nodulation: 80-150 lb N/ac fixed, 70-90% of plant N requirement.

SULFUR-CALCIUM INTERACTION: Peanuts require high S (20-40 lb S/ac) for oil quality and N fixation. Gypsum 
(CaSO4) ideal source - provides both Ca and S. Two applications (at early bloom and 3-4 weeks later) ensure 
availability during critical pod development period. High retention holds sulfate through season.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
peanut requirements. Standard southeastern US peanut practices: 0-20 lb N/ac starter, 40-60 lb P₂O₅/ac, 
80-100 lb K₂O/ac pre-plant. Gypsum applications (400-800 lb/ac total) split at early bloom and 3 weeks 
later. Good retention ensures Ca availability through pod fill.

MANAGEMENT STRATEGY: Avoid excess N - inhibits nodulation and promotes excessive vine growth at expense 
of pod fill. Inoculate seed with peanut-specific Rhizobium. Good nodulation provides 100-140 lb N/ac fixed. 
P banded at planting or broadcast. K broadcast pre-plant. Monitor tissue K mid-season - adequate K (>1.5% 
in recent mature leaves) essential for pod fill and disease resistance.

CALCIUM TIMING: Critical for peanuts. Ca uptake occurs directly through peg and pod, NOT translocated from 
leaves. Must be present in soil fruiting zone. First gypsum application at early bloom (50-60 days after 
planting when first flowers appear). Second application 3-4 weeks later ensures Ca availability through 
extended pod development period (pods develop over 6-8 week period, not all at once). Good retention 
maintains Ca availability but timing still critical.

YIELD POTENTIAL: In good-retention soils, peanuts produce 4,000-5,500 lb/ac with proper management. Excellent 
conditions for high-quality peanuts (large pods, high shelling percentage, minimal pops).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for peanut production 
with careful Ca management. Peanuts adapted to moderate-retention soils (traditional peanut belt has many 
sandy loam soils). Challenge: ensuring adequate Ca availability in fruiting zone throughout pod development.

MANAGEMENT STRATEGY: Minimal N (0-10 lb N/ac). P-K pre-plant: 40-60 lb P₂O₅/ac banded, 80-100 lb K₂O/ac 
broadcast. GYPSUM program critical: 3 applications (early bloom, peak bloom, late bloom) 300-400 lb/ac each, 
total 900-1,200 lb/ac. More frequent applications compensate for moderate retention - ensures continuous 
Ca availability in fruiting zone. Some growers apply gypsum with irrigation water (calcium chloride solution) 
for steady supply.

TEXTURE CONSIDERATION: Moderate-retention peanut soils typically sandy loam to loam texture. Actually ideal 
for peanuts despite moderate CEC - good for several reasons: 1) Adequate drainage prevents pod rots. 2) 
Easy digging at harvest (pods easily separated from soil). 3) Moderate retention adequate for Ca if managed 
properly. 4) Good soil temperature for southern crop.

NODULATION: Usually good in peanut-belt moderate-retention soils. Inoculation essential if new field. Lime 
to pH 6.0-6.5 optimizes nodulation. Adequate Ca from gypsum improves nodulation success. Monitor mid-season - 
should see numerous pink nodules on upper lateral roots.

IRRIGATION CONSIDERATION: Moderate-retention soils often require irrigation for consistent peanut yields. 
Advantage: can apply Ca through irrigation (fertigation). Calcium chloride or calcium nitrate solutions 
injected weekly from bloom through pod fill maintain Ca availability.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC challenges Ca management, critical 
for peanuts. However, peanuts actually well-adapted to sandy low-retention soils IF Ca management addressed. 
Traditional peanut areas include many deep sandy soils (Coastal Plain). Keys to success: intensive Ca program, 
good nodulation, adequate irrigation.

MANAGEMENT STRATEGY: Absolutely no N fertilizer - any N suppresses nodulation. P banded: 60-80 lb P₂O₅/ac. 
K split: 60 lb K₂O/ac pre-plant + 40 lb K₂O/ac at pegging stage (when pegs enter soil). GYPSUM program 
intensive: 4-5 applications starting at early bloom, every 2-3 weeks, 250-400 lb/ac per application, total 
1,000-1,600 lb/ac. Frequent applications maintain Ca concentration in sandy low-retention fruiting zone.

CALCIUM ALTERNATIVES: In low-retention soils, consider calcium-rich irrigation water if available. Or 
fertigation with calcium nitrate/calcium chloride - weekly injections 10-15 lb Ca/ac from bloom through 
pod maturity. Foliar Ca sprays NOT effective for peanuts - Ca must be in soil because uptake through pegs/pods 
directly, not translocated from foliage.

NODULATION CHALLENGES: Sandy low-retention soils often acidic (pH 5.0-6.0) and low in Ca - both inhibit 
nodulation. Lime to pH 6.0-6.5 before planting. Even though applying gypsum for pod Ca, also apply lime 
for pH/nodulation. Gypsum does NOT change pH (neutral salt), so lime needed separately. Inoculation mandatory.

IRRIGATION REQUIREMENT: Low-retention soils require irrigation for reliable peanut production. Deep sandy 
soils drought-prone. Irrigation also vehicle for Ca fertigation in intensive systems. Sprinkler or drip both 
work - can inject Ca through either system.

VIABILITY: Peanuts viable in low-retention soils with intensive Ca management and irrigation. Yields 3,000-4,000 
lb/ac achievable. Traditional peanut production on sandy Coastal Plain soils demonstrates viability. Higher 
management requirements and Ca costs but still economically viable with proper practices.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC creates severe Ca management challenges 
for peanuts. However, peanuts STILL POSSIBLE in very sandy soils - much of southeastern US peanut production 
occurs on deep sands with very low CEC. Success requires understanding unique peanut Ca dynamics and intensive 
Ca management program.

MANAGEMENT OPTIONS: Intensive Ca fertigation program mandatory. Weekly calcium injections through irrigation: 
calcium nitrate or calcium chloride, 10-20 lb Ca/ac per week from bloom through pod maturity (12-14 weeks, 
total 120-280 lb Ca/ac). Or very frequent gypsum applications: broadcast 200-300 lb/ac every 10-14 days from 
bloom through pod fill (6-8 applications). Water immediately after gypsum to move Ca into fruiting zone.

NITROGEN-FIXATION: Critical that peanuts fix own N - fertilizer N not viable in very-low-retention soils 
(massive leaching losses). Nodulation success essential. Challenge: very sandy soils often extremely acidic 
(pH 4.5-5.5) and very low Ca - both severely inhibit nodulation. Solution: heavy lime application (2-4 tons/ac 
to achieve pH 6.0-6.5) and pre-plant Ca (gypsum 500-800 lb/ac incorporated before planting). Inoculate seed 
with fresh high-quality peanut inoculant.

P-K MANAGEMENT: Banded P mandatory (60-80 lb P₂O₅/ac in 2x2 band). Banding only way achieving any P efficiency 
in very-low-retention soil. K fertigation if possible - weekly injections 5-10 lb K₂O/ac. Dry K fertilization: 
multiple split applications (4-5 times from planting through pod fill), 30-40 lb K₂O/ac each.

IRRIGATION: Absolutely mandatory - very sandy soils cannot support dryland peanuts. Drip or sprinkler with 
fertigation capability. Ca fertigation through drip most efficient system for very-low-retention soils. 
Maintains steady Ca concentration in fruiting zone despite poor retention.

SOIL BUILDING: Consider peanuts part of long-term soil building program. Peanut nodules add substantial N 
annually. Deep tap root residue adds OM deep in profile. Continuous peanut production with cover crops 
(rye, oats after peanuts) builds OM and retention over 8-12 years. Improved retention makes Ca management 
progressively easier.

VIABILITY: Peanuts viable in very-low-retention soils with irrigation and intensive Ca-fertigation program. 
Yields 2,500-3,500 lb/ac achievable. Economics depend on Ca program costs ($60-100/ac for fertigation 
program) and irrigation costs but still viable. Many successful peanut operations on very sandy soils 
throughout Southeast demonstrate viability with proper Ca management."""
    },

    "Sugar Beets": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through sugar beet's long season (150-180 days) and HEAVY nutrient requirements. Sugar beets among most 
nutrient-demanding crops: 180-240 lb N, 80-120 lb P₂O₅, 200-280 lb K₂O per acre for 25-35 ton/ac yield. 
High retention critical for preventing losses of massive nutrient applications.

MANAGEMENT STRATEGY: Split N applications despite high retention - beet season very long, uptake pattern 
extends over 5+ months. Pre-plant or at-planting: 40-50% of total N (80-120 lb N/ac). Early side-dress at 
4-6 leaf stage: 30-40% (60-80 lb N/ac). Late side-dress at canopy closure: 20-30% (40-60 lb N/ac). All P-K 
pre-plant broadcast or banded. High retention allows these large applications without severe leaching.

SUGAR-QUALITY CONSIDERATIONS: High retention benefits sugar quality. Excessive late-season N reduces sugar 
content and increases impurities (amino-N) that interfere with sugar extraction. High-retention soils allow 
precise N management - late applications retained but not over-supplied. Target: 17-18% sugar content at 
harvest requires N cutoff 8-10 weeks before harvest.

POTASSIUM IMPORTANCE: Sugar beets K-intensive (200+ lb K₂O/ac). K critical for sugar translocation from 
leaves to root, sugar content, and disease resistance. High CEC ensures K availability through long storage 
period. Tissue testing mid-season: >3.5% K in youngest mature leaf blade indicates adequacy.

SODIUM: Sugar beets unusual - benefit from Na fertilization (only common crop with Na response). Apply 50-100 lb 
Na₂O/ac (as table salt, NaCl) where soil Na low. High-retention soils hold Na better than sandy soils.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
beet requirements. Standard sugar beet belt practices: split N (40-50% pre-plant, 30-40% early season, 
20-30% mid-season), total 180-220 lb N/ac. P-K pre-plant: 80-100 lb P₂O₅, 200-240 lb K₂O per acre.

MANAGEMENT STRATEGY: Three-split N program standard. Early splits ensure N available during rapid vegetative 
growth phase (first 90 days). Final split supports continued root bulking but timed to deplete before final 
maturity - excess late-season N reduces sugar percentage and increases molasses-forming impurities. Good 
retention supports consistent yields of 25-30 ton/ac with 16-18% sugar.

BORON: Critical micronutrient for sugar beets - B deficiency causes "heart rot" (black, hollowed root core). 
Apply 2-3 lb B/ac pre-plant or broadcast mid-season. In moderate-high retention soils, single application 
usually adequate. Higher rate (3 lb B/ac) if pH >7.5 (B availability reduced in alkaline conditions).

IRRIGATION TIMING: Most sugar beets irrigated. High retention soils use water efficiently but timing affects 
nutrient availability. Avoid heavy irrigation late season - promotes late N uptake reducing sugar quality. 
In high-retention soils, late irrigation less likely to cause quality problems than in sandy soils (where 
heavy late water can leach deep residual N back into root zone).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful management 
of heavy beet nutrient requirements. More frequent split N applications needed to prevent losses: pre-plant 
(30-40%, 60-80 lb N/ac), early side-dress (30-40%, 60-80 lb N/ac), mid-season (20-30%, 40-60 lb N/ac), 
late June (10-20%, 20-40 lb N/ac). Total: 180-260 lb N/ac.

MANAGEMENT STRATEGY: Smaller individual N applications reduce leaching risk. Use N stabilizers (nitrification 
inhibitors) with pre-plant and first side-dress applications to reduce losses. P banded at planting more 
efficient than broadcast in moderate-retention soils. K split: 60-70% pre-plant + 30-40% mid-season side-dress 
compensates for some K loss.

CHALLENGE: Sugar beets' long season (150-180 days) combined with moderate retention creates extended exposure 
for nutrient losses. This is NOT ideal sugar beet soil - high-retention soils preferred. Can produce 20-28 
ton/ac with intensive management but input costs high due to frequent applications. Sugar content may be 
lower (15-17%) if late-season N management imperfect.

SOIL IMPROVEMENT: Build OM through rotation. Sugar beets followed by small grain with cover crop, then back 
to beets. Beet residue (tops, crowns) high in nutrients - incorporate for soil building. Over 8-12 years, 
can improve moderate-retention soil meaningfully.

ECONOMICS: Marginal in moderate-retention soils. High input costs (frequent fertilizer applications, often 
more total fertilizer needed due to losses) while yields potentially lower. Viable only with good sugar beet 
prices and contracts. Consider whether beets best crop choice vs alternatives.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC inadequate for economic sugar beet 
production in most situations. Sugar beets' massive nutrient requirements combined with low retention create 
severe loss potential. Very frequent split N required: 5-6 applications through season, 30-50 lb N/ac each, 
total 180-300 lb N/ac (higher total needed due to losses).

MANAGEMENT CHALLENGES: Multiple problems in low-retention soils: 1) Frequent split N applications expensive 
(labor, equipment). 2) Even with splits, significant N losses to leaching. 3) K management difficult - beets' 
high K demand + low retention = very high K application rates needed (250-300+ lb K₂O/ac), expensive. 4) 
Long season extends loss exposure period. 5) Sugar quality issues - difficulty managing late-season N means 
often excess late N, reducing sugar content.

IRRIGATION COMPLICATIONS: Low-retention beet soils require frequent irrigation. Each irrigation event can 
leach nutrients. Fertigation possible solution - inject N-K with each irrigation. Requires specialized 
equipment and expertise. Even with fertigation, efficiency <60% in low-retention soils.

ALTERNATIVE CROPS: In low-retention soils, consider alternatives to sugar beets: 1) Potatoes - shorter 
season, somewhat lower nutrient demand. 2) Corn - better adapted to sandy soils. 3) Dry beans - N-fixing 
reduces fertilizer losses. 4) Sunflowers - deep roots, moderate demand. Sugar beets economically marginal 
at best.

VIABILITY: Sugar beets generally not viable in low-retention soils. Input costs (excessive fertilizer rates, 
frequent applications, fertigation equipment) too high while yields reduced (15-22 ton/ac typical) and quality 
problems (low sugar content 14-16%, high impurities). Not recommended except in unusual circumstances (very 
high beet prices, established fertigation infrastructure, contracts guaranteeing returns).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes sugar beet production economically 
non-viable. Sugar beets' combination of massive nutrient requirements, very long season, and high soil quality 
needs all incompatible with very-low-retention soils.

TECHNICAL BARRIERS: Even with intensive fertigation, cannot economically supply beets' nutrient requirements 
in very-low-retention soils. Weekly N-K injections required (15-25 lb N/ac, 20-30 lb K₂O/ac per week for 
20-22 weeks, totals: 300-550 lb N/ac, 400-660 lb K₂O/ac). Costs $120-180/ac for fertilizer alone, not 
including irrigation and injection costs. Nutrient use efficiency <40% even with best practices.

BEYOND RETENTION ISSUES: Multiple additional problems in very sandy soils: 1) Poor stand establishment - 
beet seed tiny, requires firm smooth seedbed difficult in loose sand. 2) Soil compaction from heavy harvest 
equipment (loaded beet trucks, harvesters) creates severe compaction in wet sandy soils. 3) Wind erosion 
during long season - exposed sandy soil between rows erodes badly. 4) Root quality - sandy soils grow "hairy" 
roots (excessive lateral roots) reducing processing quality. 5) Disease pressure - many beet diseases favored 
by sandy conditions.

HARVEST COMPLICATIONS: Beet harvest late (Sept-Nov). Very sandy soils often too loose or too wet for efficient 
harvest. Roots difficult to lift cleanly - excessive soil adheres to roots or roots break during lifting. 
Processing plants penalize for excess soil and broken roots.

RECOMMENDATION: Do not attempt sugar beet production in very-low-retention soils. Multiple technical and 
economic barriers make success essentially impossible. Consider any alternative crop better suited to very 
sandy conditions. Even with unlimited budget for inputs, physical limitations (poor stand, harvest issues, 
root quality) prevent viable production."""
    },

    "Alfalfa": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through alfalfa's long production period (3-5 years) and VERY HEAVY nutrient requirements. Alfalfa among 
most nutrient-extracting crops: removes 250-280 lb N, 60-70 lb P₂O₅, 220-260 lb K₂O per ton of dry hay. 
At 7-8 ton/ac yield (high-CEC soils), annual removal: 1,750-2,240 lb N, 420-560 lb P₂O₅, 1,540-2,080 lb 
K₂O per acre.

MANAGEMENT STRATEGY: Alfalfa unique - FIXES OWN NITROGEN through Rhizobium symbiosis (excellent fixation 
can provide 100% of N needs). Therefore, N fertilization MINIMAL or ZERO despite massive removal. Focus: 
P-K management. Pre-planting: heavy broadcast 80-120 lb P₂O₅/ac, 200-300 lb K₂O/ac incorporated deeply. 
Annual topdress: 40-60 lb P₂O₅/ac, 200-300 lb K₂O/ac broadcast after first cutting. High retention holds 
these large K applications against loss.

POTASSIUM CRITICAL: Alfalfa extremely K-intensive. K requirements exceed any other common crop. K affects: 
stand persistence, winter hardiness, disease resistance, regrowth vigor, yield, forage quality (protein 
content). High-retention soils essential for maintaining K availability through multiple cuttings each season 
for multiple years. Tissue testing after first cutting: >2.5% K in upper stems indicates adequacy.

PHOSPHORUS MANAGEMENT: High P requirement but less dynamic than K (not removed as rapidly with harvest). 
Adequate P critical for seedling establishment, nodulation, nitrogen fixation. High-retention soils hold P 
well. Build soil test P to >50 ppm (Bray P1) before planting for optimal stand establishment.

CALCIUM-pH: Alfalfa requires high Ca (>1,500 lb Ca/ac annually), pH 6.5-7.5 optimal. High-retention soils 
often adequate Ca. If needed, lime maintains both pH and Ca supply. High CEC buffers pH, stabilizes Ca 
availability through stand life.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
alfalfa's heavy requirements. Standard alfalfa practices: pre-plant 80-100 lb P₂O₅, 200-280 lb K₂O per 
acre. Annual topdress after first cutting: 40-50 lb P₂O₅, 180-240 lb K₂O per acre for 6-7 ton/ac yield.

MANAGEMENT STRATEGY: No N fertilizer - alfalfa fixes 100-300 lb N/ac annually depending on stand vigor 
and fixation success. Inoculate seed with alfalfa-specific Rhizobium (Sinorhizobium meliloti) at planting. 
Good nodulation: large pink/tan nodules on tap root and upper laterals within 4-6 weeks. Failed nodulation 
rare in good-retention soils with proper pH (6.5-7.5).

POTASSIUM SPLIT APPLICATION: Consider split K in high-retention soils with very high yields. Apply 50-60% 
of annual K requirement after first cutting + 40-50% after second cutting. Ensures K availability during 
all critical regrowth periods. Inadequate K: reduced regrowth vigor, winter injury, increased disease 
(especially in northern regions where winter hardiness critical).

STAND LONGEVITY: In good-retention soils with adequate P-K management, alfalfa stands productive 4-6 years. 
Persistence depends on variety, pest pressure, harvest management, and fertility - especially K. Monitor 
tissue K annually. If K falls below 2.0-2.5%, topdress heavily or stand will decline rapidly.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC manageable for alfalfa but 
requires intensive K management. Alfalfa's extreme K demand combined with moderate retention necessitates 
frequent K applications to maintain stand vigor and persistence.

MANAGEMENT STRATEGY: Pre-plant: 80-100 lb P₂O₅ (banded if possible for establishment), 250-300 lb K₂O 
(broadcast incorporated). Annual K program: split 3-4 times. After each cutting: 80-100 lb K₂O/ac (total 
240-300+ lb K₂O/ac annual for 5-6 ton/ac yield). More frequent smaller applications compensate for moderate 
retention. Skip K after final fall cutting to avoid promoting late growth that reduces winter hardiness.

CHALLENGE - POTASSIUM DEPLETION: In moderate-retention soils, inadequate K management rapidly depletes 
stands. Symptoms: reduced regrowth vigor after each cutting, stand thinning after 2-3 years, yellowing 
leaf margins, increased winter injury. Once K-depleted, very difficult and expensive to restore stand. 
Prevention through consistent K program essential.

PHOSPHORUS: Banded at establishment critical in moderate-retention soils. Broadcast P susceptible to fixation 
by Fe/Al oxides common in sandy moderate-retention soils. Maintain soil test P >40-50 ppm through annual 
topdressing.

STAND LIFE: Typically 3-4 years in moderate-retention soils with good management. Shorter than high-retention 
soils due to difficulty maintaining adequate K throughout all plants in field. Replanting costs factor into 
economics. Still viable but more management-intensive.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes long-term alfalfa production 
very challenging. Alfalfa's massive K requirements incompatible with low retention - cannot economically 
maintain adequate K availability for vigorous productive stands over multiple years.

MANAGEMENT CHALLENGES: Pre-plant: 100-120 lb P₂O₅ (banded), 300-400 lb K₂O (broadcast). Annual K: split 
after every cutting, 80-120 lb K₂O/ac per application (after first, second, third cuttings = 240-360 lb 
K₂O/ac annually). Despite intensive K program, severe challenges: 1) K leaching losses significant even 
with splits. 2) Uneven K distribution across field leads to variable stand vigor. 3) Lower yields (3-5 
ton/ac) yet higher K application rates needed. 4) Economics marginal - high K costs, frequent applications.

NODULATION ISSUES: Low-retention soils often acidic (pH 5.0-6.0) and low Ca - both severely inhibit alfalfa 
nodulation and nitrogen fixation. Heavy lime required (2-4 tons/ac to achieve pH 6.5-7.0). Without successful 
nodulation, must apply N fertilizer (defeats alfalfa's main economic advantage). Even with lime and inoculation, 
nodulation success variable in low-CEC soils.

STAND PERSISTENCE: Typically 2-3 years maximum in low-retention soils. K depletion, variable nodulation, 
environmental stress cause rapid stand decline. By year 3, often <40% stand remaining. Frequent re-establishment 
(every 2-3 years) expensive, negates alfalfa's advantage over annual crops.

ALTERNATIVES: Consider alternatives to alfalfa in low-retention soils: 1) Grass hay (orchardgrass, timothy) 
- lower K demand, longer stand life. 2) Red clover - shorter stand life but less K-demanding than alfalfa. 
3) Annual forage sorghum or sudangrass - no stand maintenance, more adapted to sandy soils. 4) Grass-legume 
mixtures - mixed stands more stable than pure alfalfa in challenging soils.

VIABILITY: Alfalfa marginally viable in low-retention soils. High input costs (K fertilizer, frequent applications, 
frequent stand replacement) often exceed returns. Viable only with very high hay prices or specific market 
demands for alfalfa vs alternative forages.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes alfalfa production essentially 
non-viable. Alfalfa's combination of extreme K demands, long stand life requirement, high Ca needs, and pH 
sensitivity all incompatible with very-low-retention soils.

TECHNICAL BARRIERS: Cannot economically supply alfalfa K requirements in very-low-retention soils. Would 
require: fertigating K after every cutting (difficult with hay crops), 100-150 lb K₂O/ac per application, 
4-5 applications annually = 400-750 lb K₂O/ac annually for marginal 2-4 ton/ac yields. K costs alone $120-180/ac 
annually. Efficiency <30% due to severe leaching. Economics impossible.

NODULATION FAILURE: Very-low-retention soils almost always extremely acidic (pH 4.5-5.5) and Ca-deficient. 
Alfalfa cannot nodulate effectively below pH 6.2. Required lime applications (4-6 tons/ac) prohibitively 
expensive for hay crop returns. Without nodulation, must apply 200-300 lb N/ac annually - defeats alfalfa's 
purpose and makes economics absurd.

PHYSICAL LIMITATIONS: Beyond chemical issues: 1) Poor seedbed in very sandy soil - tiny alfalfa seed requires 
firm fine seedbed. 2) Harvest equipment compaction severe in sandy soils. 3) Erosion during establishment 
(bare sandy soil exposed). 4) Poor moisture retention - alfalfa drought-sensitive during establishment. 5) 
Root diseases (Phytophthora, Fusarium) severe in sandy soils.

STAND FAILURE: Even if established, stands fail first year. K deficiency, failed nodulation, environmental 
stress cause complete failure. 50-80% stand loss first year typical. Second year remnant stand non-productive.

RECOMMENDATION: Absolutely do not attempt alfalfa in very-low-retention soils. Technical and economic barriers 
insurmountable. Consider alternatives: 1) Warm-season grass hay (bermudagrass in South, switchgrass) - adapted 
to sandy soils, responsive to N fertilizer. 2) Annual rye or wheat for forage - can apply N through season. 
3) Pearl millet or sudangrass - excellent forage production in sandy soils. 4) Non-agricultural use (forestry, 
wildlife habitat, conservation). Anything preferable to failed alfalfa."""
    },

    "Red Clover": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
for red clover's moderate nutrient requirements. Red clover simpler than alfalfa - shorter stand life (2-3 
years typical), moderate yield (3-4 ton/ac dry matter), moderate K requirement (140-200 lb K₂O/ac annually). 
As legume, fixes atmospheric N (60-150 lb N/ac annually) through Rhizobium symbiosis.

MANAGEMENT STRATEGY: No N fertilizer (relies on fixation). Pre-planting: 50-80 lb P₂O₅/ac, 120-160 lb K₂O/ac. 
Annual topdress: 40-50 lb P₂O₅/ac, 120-160 lb K₂O/ac for continued productivity. Much simpler than alfalfa's 
intensive K program. High retention holds these moderate applications adequately.

COMPARATIVE ADVANTAGES OVER ALFALFA: Red clover easier to grow in several ways: 1) Less K-demanding (about 
50-60% of alfalfa's K requirement). 2) More acid-tolerant (pH 6.0-6.5 acceptable vs alfalfa requiring 6.5-7.5). 
3) More shade-tolerant - excellent as grass mixture component. 4) Cheaper to establish (seed $2-3/lb vs alfalfa 
$6-8/lb). 5) More flexible harvest timing. Disadvantages: shorter stand life (2-3 years vs 4-6), slightly 
lower forage quality.

GRASS-CLOVER MIXTURES: Red clover excellent in mix with orchardgrass, timothy, or tall fescue. Clover fixes 
N, benefiting companion grass (60-80 lb N/ac transferred to grass). Mixture yields often equal pure stands 
while being more stable, requiring less intensive K management.

NODULATION: Inoculate seed with red clover Rhizobium (Rhizobium leguminosarum bv. trifolii) if clover not 
grown recently. Good nodulation typical in high-retention soils with pH >6.0.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
clover requirements. Standard practices: pre-plant 50-80 lb P₂O₅, 120-160 lb K₂O per acre. Annual topdress: 
40-50 lb P₂O₅, 120-140 lb K₂O per acre for 3-4 ton/ac dry matter yield.

MANAGEMENT STRATEGY: Red clover particularly well-suited to moderate-high retention soils. Less demanding 
than alfalfa but more productive than white clover. Excellent choice for: 1) Rotation hay crop (2-year red 
clover between row crops). 2) Nurse crop seeding with small grain (underseed red clover in wheat/barley, 
harvest clover after grain harvest). 3) Green manure/cover crop (plow under before flowering for maximum 
N contribution to next crop).

POTASSIUM MANAGEMENT: Single annual topdress adequate in good-retention soils. Apply after first cutting 
(late May-early June typically). Clover less sensitive to K depletion than alfalfa - stands remain productive 
with moderate K program.

VERSATILITY: Red clover serves multiple purposes: forage hay, pasture, green manure, cover crop for soil 
improvement and N contribution. Good-retention soils support all uses well. As green manure: can provide 
80-140 lb N/ac to following crop (plow under at flowering for maximum N yield).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for red clover - 
clover particularly well-adapted to moderate-retention soils. This is red clover's advantage over alfalfa: 
productive and economical at moderate fertility/retention levels.

MANAGEMENT STRATEGY: Pre-plant: 60-80 lb P₂O₅ (banded if possible), 140-180 lb K₂O (broadcast). Annual 
topdress: split K application beneficial - 70-90 lb K₂O after first cutting + 60-80 lb K₂O after second 
cutting, total 130-170 lb K₂O annually. Split application compensates for moderate retention.

RED CLOVER IDEAL FOR MODERATE-RETENTION SOILS: Multiple advantages: 1) More acid-tolerant than alfalfa 
(pH 5.8-6.5 acceptable). Moderate-retention soils often slightly acidic. 2) Lower K requirement easier to 
satisfy. 3) Shorter stand life means less long-term K depletion pressure. 4) Excellent for building 
moderate-retention soils - N fixation, root turnover, and residue decomposition add OM. 5) In grass-clover 
mixture, mixed stand more forgiving than pure alfalfa in moderate-retention soils.

ROTATION USE: Particularly valuable in row crop rotations on moderate-retention soils. Sequence: corn/soybeans 
→ small grain (wheat/oats) → red clover (2 years) → back to row crops. Clover period builds soil fertility 
and OM, improving retention for subsequent crops.

NODULATION: Usually good in moderate-retention soils if pH >5.8. Inoculate seed if clover new to field. 
Adequate Ca and Mo availability at pH 5.8-6.5 supports nodulation.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but red clover still viable option 
- much better adapted than alfalfa to low-retention soils. Clover's moderate K demand, acid tolerance, and 
short stand life make it feasible where alfalfa fails.

MANAGEMENT STRATEGY: Pre-plant: 60-80 lb P₂O₅ (banded), 150-200 lb K₂O (broadcast). Annual K: split after 
each cutting, 70-90 lb K₂O/ac per application (total 140-180 lb K₂O annually for 2-3 ton/ac yield). Despite 
low retention, clover's moderate demands manageable with split K applications.

NODULATION CHALLENGES: Low-retention soils often acidic (pH 5.0-6.0). Red clover tolerates pH 5.8-6.5 but 
suboptimal nodulation below pH 6.0. Lime to pH 6.0-6.5 if possible. Mo deficiency common in acidic low-retention 
soils - apply 0.1-0.2 lb Mo/ac for improved nodulation. Inoculation mandatory.

GRASS-CLOVER MIXTURE PREFERRED: In low-retention soils, grass-clover mixture more stable than pure clover. 
Grass roots stabilize soil, complement clover. Mixture less sensitive to K variations across field. Recommended 
mix: 50-60% grass (orchardgrass or tall fescue) + 40-50% red clover.

SOIL IMPROVEMENT: Red clover excellent for building low-retention soils. Two-year clover stand: fixes 120-250 lb 
N/ac total, adds substantial root biomass and OM. Use in rotation: row crop → small grain → clover (2 years) 
→ row crop. After 8-12 years, retention measurably improved.

VIABILITY: Red clover viable in low-retention soils with split K applications. Economics better than alfalfa 
(lower inputs, adequate productivity). Good choice for hay or forage where alfalfa not feasible.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but red clover still POSSIBLE where 
alfalfa impossible. Clover's advantages: moderate K demand, short stand life, acid tolerance, lower establishment 
cost allow consideration in very-low-retention soils.

MANAGEMENT OPTIONS: Pre-plant: 60-80 lb P₂O₅ (banded), 180-220 lb K₂O. Annual K fertigation if possible - 
monthly injections through sprinkler, 40-50 lb K₂O/ac per application (total 120-150 lb K₂O annually). Dry 
K fertilization: split after each cutting, 60-80 lb K₂O/ac. Despite low retention, clover's lower total 
requirement vs alfalfa makes economics marginally viable.

NODULATION: Severe challenges in very sandy soils (typically pH 4.5-5.5). Lime heavily to pH 6.0-6.5 (2-4 
tons/ac). Apply Mo (0.2-0.3 lb/ac) and adequate Ca (gypsum if pH acceptable after lime). Inoculate with high-
quality fresh inoculant. Even with best practices, nodulation success <70% in very-low-retention soils.

STAND LIFE: Typically 1-2 years in very-low-retention soils vs 2-3 years in better soils. K depletion, 
environmental stress cause decline. Still economical if using as short-term forage or green manure - doesn't 
require long persistence for these uses.

ALTERNATIVE USE - GREEN MANURE: Perhaps best use for red clover in very-low-retention soils. Plant clover 
in spring, grow through summer, plow under fall or following spring. Fixed N (60-100 lb N/ac) benefits next 
crop. Root biomass adds OM. Minimal K applications needed for single-season growth (100-120 lb K₂O/ac total). 
Much more feasible than trying to maintain multi-year forage stand.

GRASS-CLOVER MIXTURE: Definitely preferred over pure clover in very-low-retention soils. Grass component 
(orchardgrass, tall fescue) more adapted to very sandy conditions. Mixture: 60-70% grass + 30-40% clover. 
Apply N to grass component (80-120 lb N/ac annually split) since clover N fixation unreliable.

VIABILITY: Red clover marginally viable as short-term crop (1-2 years) or green manure in very-low-retention 
soils. Multi-year productive forage stand difficult. Economics depend on purpose (green manure may be cost-
effective even if short-term; forage production marginal). Better adapted than alfalfa but still challenging."""
    },

    "Sugarcane": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC essential for sugarcane's 
EXTREMELY heavy nutrient demands over multi-year ratoon cycle (4-7 years). Sugarcane removes massive 
quantities: 200-250 lb N, 100-150 lb P₂O₅, 400-500 lb K₂O per 100 tons cane annually. High retention 
critical for maintaining fertility through successive ratoon crops without excessive fertilizer losses.

MANAGEMENT STRATEGY: Plant cane: heavy pre-plant (100-120 lb N, 80-100 lb P₂O₅, 200-250 lb K₂O) followed 
by side-dress (80-100 lb N, 150-200 lb K₂O at 60-90 days). First ratoon: 180-220 lb N, 80-100 lb P₂O₅, 
350-400 lb K₂O applied in 2-3 splits (at ratoon emergence, tillering, and grand growth). Subsequent ratoons: 
similar to first ratoon. High retention allows larger individual applications reducing labor over long season 
(12-16 months per crop).

RATOON LONGEVITY: High retention supports 5-7 productive ratoon crops. Each successive ratoon mines soil 
reserves - good retention slows depletion. Ratoon decline (reduced vigor, thinner stalks, more disease) 
accelerates in low-retention soils requiring replanting every 2-3 crops. High retention extends ratoon 
productivity reducing costly replanting frequency.

POTASSIUM CRITICAL: Sugarcane among highest K-demanding crops - 400-500 lb K₂O per 100 tons. K affects 
stalk strength, disease resistance, sugar content, ratoon vigor. High retention maintains K through long 
season and across ratoons. Split K applications: 50-60% at planting/ratooning, 40-50% at tillering/grand 
growth.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC adequate for 4-5 ratoon cycles 
with intensive fertilization. Sugarcane's extreme demands manageable but require careful program. Split 
applications essential: plant cane (3 splits), ratoons (2-3 splits per crop). Total annual requirements: 
200-250 lb N, 100-150 lb P₂O₅, 400-500 lb K₂O per 100 tons cane.

MANAGEMENT STRATEGY: More frequent splits than high-retention soils. Plant cane: pre-plant (80 lb N, 80 
lb P₂O₅, 150 lb K₂O) + 60 days (70 lb N, 150 lb K₂O) + 120 days (50 lb N, 100 lb K₂O). Ratoons: emergence 
(60 lb N, 80 lb P₂O₅, 150 lb K₂O) + tillering (70 lb N, 150 lb K₂O) + grand growth (70 lb N, 150 lb K₂O). 
More splits compensate for moderate retention during 12-16 month crops.

RATOON MANAGEMENT: Expect 4-5 productive ratoons vs 5-7 in high-retention. Ratoon decline accelerates after 
4th crop. Monitor soil tests annually - K depletion common in moderate retention under sugarcane's heavy 
removal. May need increased K rates (450-550 lb K₂O/ac) in later ratoons. Consider replanting after 4-5 
ratoons to maintain productivity.

TRASH MANAGEMENT: Maintain green harvest (leave trash blanket) in moderate-retention soils. Trash mulch 
conserves moisture, adds OM (improving retention over time), returns some nutrients, reduces erosion. Burns 
common historically but sacrifice OM benefits important for retention.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for sugarcane's 
extreme demands. Limits ratoon longevity to 2-3 productive crops. Intensive split applications mandatory: 
4-5 splits per crop. Fertigation highly recommended if irrigation available.

MANAGEMENT STRATEGY: Four to five-split program. Plant cane: pre-plant (60 lb N, 80 lb P₂O₅, 120 lb K₂O) 
+ 45 days (50 lb N, 100 lb K₂O) + 90 days (50 lb N, 100 lb K₂O) + 135 days (40 lb N, 80 lb K₂O), total 
200 lb N, 80 lb P₂O₅, 400 lb K₂O. Ratoons similar split pattern. Fertigation through drip or center pivot: 
biweekly injections 15-20 lb N/ac, 25-30 lb K₂O/ac for 20-24 weeks.

RATOON DECLINE: Severe issue in moderate retention. First ratoon acceptable (80-90% of plant cane yield). 
Second ratoon declining (70-80%). Third ratoon poor (60-70%). Beyond third ratoon usually uneconomical. 
Replant every 3-4 crops necessary vs 5-7 in high retention. Frequent replanting increases costs significantly.

QUALITY IMPACTS: Moderate retention affects not just yield but quality. Sugar content may be reduced (11-13% 
vs 14-16% optimal) in later ratoons as plants stress from inadequate nutrition. Cane quality (CCS - commercial 
cane sugar) declines faster in moderate retention. Harvest timing critical - avoid delays that reduce quality 
further.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes traditional ratoon sugarcane 
production extremely difficult. Sugarcane's massive demands (200-250 lb N, 400-500 lb K₂O annually) over 
multi-year cycle not sustainable in low retention. Ratoon longevity 1-2 crops maximum. Economics marginal.

MANAGEMENT OPTIONS: Two approaches, both challenging. 1) Annual replanting: treat as annual crop, replant 
every year, intensive fertilization (5-6 splits per crop or fertigation). Eliminates ratoon but replanting 
costs ($800-1,200/ac) prohibitive. 2) Short ratoon cycle: 1-2 ratoons only then replant. Still requires 
intensive fertigation or 5-6 splits per crop.

FERTIGATION MANDATORY: Only viable approach in low-retention sugarcane. Weekly or biweekly injections 15-25 
lb N/ac, 30-40 lb K₂O/ac for 24-30 weeks per crop. Drip ideal but center pivot acceptable. Without fertigation, 
losses through leaching make economic production impossible - fertilizer costs exceed returns.

QUALITY CRISIS: Low retention produces multiple quality problems: thin stalks (reduced tonnage per stalk), 
low sugar content (10-12% vs 14-16%), high fiber (reduces milling efficiency), disease susceptibility (stressed 
plants), poor ratooning (weak stools, thin stands). Even plant cane quality poor compared to better soils.

VIABILITY: Sugarcane production marginal to non-viable in low-retention soils. Economics rarely favorable - 
extreme input costs (frequent replanting, intensive fertigation, high fertilizer rates) versus reduced yields 
and quality. Consider alternative crops. If attempting sugarcane: fertigation mandatory, 2-3 year maximum 
ratoon cycle, expect yields 40-60% of optimal.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes sugarcane production non-viable. 
Sugarcane's extreme multi-year nutrient demands fundamentally incompatible with very-low-retention soils. 
Cannot maintain adequate fertility through 12-16 month crops and multi-year ratoons despite intensive 
management.

MANAGEMENT IMPOSSIBILITY: No practical management system provides adequate nutrition in very-low-retention 
sugarcane. Intensive fertigation twice-weekly still produces severe deficiencies during rapid growth phases 
(grand growth period: 4-8 months with 2-3 inches/day growth rates, massive nutrient demand). Very sandy soils 
cannot buffer nutrition for these demand peaks.

RATOON FAILURE: Ratoon crops impossible in very-low-retention soils. Even if plant cane marginally successful 
(yields <50% normal), ratoon emergence poor, stands thin (20-40% of plant cane stand density), growth weak, 
disease severe. First ratoon typically <30% of plant cane yield - economically disastrous. No viable ratoon 
system exists.

REPLANTING ECONOMICS: Annual replanting theoretically possible but economically catastrophic. Replanting 
costs $800-1,200/ac plus intensive fertigation/fertilization ($400-600/ac). Total costs $1,200-1,800/ac 
versus revenues from low yields (40-60 tons/ac, low sugar) of $1,500-2,500/ac. Marginal or negative returns 
every year.

ALTERNATIVES: DO NOT GROW sugarcane in very-low-retention soils. Sugarcane requires fertile soils for 
economic production - among most demanding field crops. Better alternatives: 1) Energy cane (lower sugar 
expectations, biomass focus, shorter season). 2) Sweet sorghum (annual crop, lower demands, easier management). 
3) Improved pasture or hay crops. 4) Row crops better adapted to sandy soils (peanuts, sweet potatoes, 
watermelons). Among all field crops, sugarcane one of WORST choices for very-low-retention soils."""
    },

    "Tobacco": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC but CAUTION - tobacco unique 
crop where excessive retention/fertility can REDUCE quality. High N produces thick dark leaves with harsh 
taste, poor burn characteristics, reduced value. Optimal pH 5.5-6.5 (slightly acid) and MODERATE organic 
matter (1-2%) actually preferable to very high OM (>3%). Controlled N availability critical for leaf quality.

MANAGEMENT STRATEGY: Conservative N program despite high retention: 50-80 lb N/ac total (much lower than 
most crops). Split carefully: 40-50% at transplant (25-40 lb N) + 50-60% at 3-4 weeks (25-40 lb N). NO LATE 
N - cutoff 4-6 weeks before harvest. Late N delays maturity, reduces quality (poor burn, high nicotine, harsh 
flavor). P-K applied fully pre-plant: 80-100 lb P₂O₅, 100-150 lb K₂O. High retention holds these adequately.

QUALITY-RETENTION RELATIONSHIP: High retention risks excessive N availability from mineralization (60-80 lb 
N/ac from high OM) plus fertilizer N. Can produce >120 lb N/ac available - excessive for quality tobacco. 
Monitor tissue tests closely. Reduce fertilizer N if OM high. May need only 30-50 lb N/ac fertilizer in very 
high retention/OM soils.

POTASSIUM-QUALITY: K critical for tobacco quality - affects burn rate, ash color, leaf handling. Adequate K 
(100-150 lb K₂O/ac) produces white ash, good burn, proper curing. Deficient K: dark ash, poor burn, difficult 
curing. High retention maintains K through season. Use K sulfate if possible (better leaf quality than KCl, 
Cl can reduce quality).""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC OPTIMAL for quality tobacco 
production. Provides adequate nutrition without excess that reduces quality. This retention level often 
produces BEST balance of yield and quality - sufficient nutrients for good leaf development without excessive 
growth that harms characteristics.

MANAGEMENT STRATEGY: Standard tobacco program: 60-80 lb N/ac split 50% transplant + 50% at 3-4 weeks. P-K 
pre-plant: 80-100 lb P₂O₅, 100-150 lb K₂O. Good retention maintains these through season. Avoid excess N - 
quality tobacco depends on balanced moderate nutrition, not maximum nutrition. Cutoff N 4-6 weeks before 
harvest critical.

QUALITY ADVANTAGES: This retention level produces excellent quality tobacco: medium-thick leaves (not thin/
weak, not thick/harsh), good color (golden to red-brown depending on type), excellent burn characteristics, 
balanced nicotine (not too low/too high), good curing quality. Many premium tobacco regions have soils in 
this retention range.

SULFUR IMPORTANT: Tobacco has moderate S requirement (20-30 lb S/ac). S affects protein content, curing 
quality, flavor. Good retention usually provides adequate S but monitor if using low-S fertilizers (urea, 
DAP). Consider ammonium sulfate or K sulfate to supply S with N or K.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC acceptable for tobacco production - 
actually can be ADVANTAGEOUS for quality. Lower retention reduces risk of excessive N from mineralization. 
Ensures controlled N availability producing high-quality leaf. Careful fertilization maintains adequacy without 
excess.

MANAGEMENT STRATEGY: Split N essential in moderate retention: 30-40 lb N at transplant + 30-40 lb at 3-4 
weeks, total 60-80 lb N/ac. Two splits maintain availability during critical growth periods (establishment, 
rapid vegetative growth) without excess. P banded at transplant: 80-100 lb P₂O₅. K split possible: 80 lb 
pre-plant + 40 lb at 3-4 weeks, total 120 lb K₂O.

QUALITY CONSIDERATIONS: Moderate retention with controlled fertilization produces excellent quality tobacco. 
Lower OM (0.5-1.5%) means less mineralized N - easier to control total N availability. Avoid excess fertilizer 
- better slightly deficient than excessive for tobacco quality. Thin leaves preferable to thick harsh leaves.

VARIETY SELECTION: Choose varieties suited to moderate fertility. Some tobacco types bred for high fertility, 
others for moderate. Burley tobacco often grown on moderate-fertility soils. Flue-cured can tolerate moderate 
fertility well. Cigar-wrapper requires careful nutrition control - moderate retention ideal.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC limits tobacco production to lower 
yields but can still produce ACCEPTABLE quality with proper management. Tobacco has moderate nutrient demands 
(60-80 lb N/ac) - lower than corn, cotton, vegetables. This makes tobacco viable in low retention where many 
crops fail.

MANAGEMENT STRATEGY: Three-split N compensates for low retention: 25-30 lb at transplant + 25-30 lb week 3 
+ 20-25 lb week 6, total 70-85 lb N/ac. More frequent splits maintain availability during 90-120 day season. 
P banded: 80-100 lb P₂O₅. K split: 60 lb pre-plant + 40 lb week 3 + 30 lb week 6, total 130 lb K₂O.

QUALITY IMPACTS: Low retention produces lighter, thinner leaves. This is NOT necessarily negative - light 
thin leaves can be high quality if properly grown and cured. Avoid deficiencies (especially K) that cause 
poor curing. Quality acceptable for most tobacco classes though yields lower (1,800-2,400 lb/ac vs 2,500-
3,000 optimal).

LIME-pH MANAGEMENT: Low-retention soils typically acidic (pH 5.0-6.0). Tobacco tolerates slight acidity 
(pH 5.5-6.5 optimal) better than many crops. Light lime (1-2 tons/ac to pH 5.8-6.2) adequate. Avoid overliming 
- pH >7.0 reduces tobacco quality and increases disease (especially bacterial wilt).

VIABILITY: Tobacco viable for 1,800-2,400 lb/ac in low-retention soils. Historically, tobacco often grown 
on sandy moderate-to-low fertility soils in southeastern US. Better adapted than most row crops to challenging 
conditions. Economics moderate - lower yields but tobacco's high value ($1.50-2.50/lb) makes even modest 
yields profitable.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes tobacco production challenging 
but STILL MORE VIABLE than most field crops. Tobacco's moderate demands (60-80 lb N/ac), tolerance to slight 
acidity, and high value provide advantages over corn, cotton, soybeans in very-low-retention conditions.

MANAGEMENT OPTIONS: Intensive four-split program or fertigation. Four splits: 20 lb N at transplant + 20 lb 
week 3 + 20 lb week 6 + 15 lb week 9, total 75 lb N/ac. K splits: 50 + 35 + 30 + 20 = 135 lb K₂O. P banded: 
80-100 lb P₂O₅. Fertigation through drip: weekly injections 8-12 lb N/ac, 12-18 lb K₂O/ac for 8-12 weeks.

QUALITY-VIABILITY: Very-low-retention tobacco produces light thin leaves, lower yields (1,400-2,000 lb/ac), 
but can still achieve acceptable quality grades. Critical: maintain adequate K through frequent splits or 
fertigation - K deficiency destroys quality regardless of retention level. Thin leaves not inherently low 
quality if nutrition balanced.

RAISED BEDS: Consider raised beds (6-8 inches) with compost (20-30% by volume) for very-low-retention tobacco. 
Temporary retention improvement plus better root environment support quality production. Beds reduce leaching, 
improve moisture retention (tobacco sensitive to drought), warm soil (tobacco heat-loving).

VARIETY-TYPE SELECTION: Light air-cured types (Burley) or fire-cured types most forgiving in very-low-
retention. Flue-cured possible but challenging. Avoid cigar-wrapper types (extremely demanding of uniform 
nutrition and quality). Consider lower-grade tobacco classes where quality expectations moderate.

VIABILITY: Tobacco marginally viable for 1,400-2,000 lb/ac in very-low-retention soils with intensive 
management. Among better field crop options for very sandy conditions - moderate demands, high value, tolerance 
to challenges. Economics marginal but possible - intensive inputs ($600-900/ac) versus returns from modest 
yields ($2,100-4,000/ac at $1.50-2.00/lb). Better choice than corn, cotton, soybeans, most vegetables in 
very-low-retention conditions."""
    },

    "Clover": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage for 
clover's moderate-heavy nutrient requirements over 2-4 year stand life. Despite N-fixing ability (100-200 lb 
N/ac annually), clovers are HEAVY K feeders removing 200-300 lb K₂O/ac/year in harvested forage. Adequate 
P (60-80 lb P₂O₅/ac) critical for establishment and nodulation. High retention maintains P-K through multi-
year stands.

MANAGEMENT STRATEGY: Establishment year: 60-80 lb P₂O₅, 100-120 lb K₂O broadcast and incorporated before 
seeding. Minimal N (20-30 lb/ac) assists establishment until nodulation begins. Production years: 80-100 lb 
P₂O₅, 200-250 lb K₂O annually split after cuttings (40-50 lb K₂O after each of 3-4 cuttings). High retention 
allows somewhat larger K applications reducing application frequency.

CLOVER TYPES: Multiple species with different characteristics. 1) Red clover (most common, 2-3 year stand, 
moderate demands, 4-5 tons DM/ac). 2) White clover (low-growing, persistent, excellent grazing tolerance, 
lower yields 3-4 tons but long-lived 4-6 years). 3) Alsike clover (tolerates wet acidic soils better than 
red/white, 3-4 tons). 4) Crimson clover (annual, excellent N-fixer for cover crops, 2-3 tons single cut). 
High retention supports all types excellently.

NODULATION: High CEC with adequate Ca-Mg (pH 6.0-7.0) supports excellent nodulation. Rhizobium leguminosarum 
forms numerous pink nodules on upper roots. Good nodulation fixes 100-200 lb N/ac annually - essentially 
entire N need. Inoculate seed if clover not grown recently (3+ years). Check nodulation 4-6 weeks after 
emergence.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC adequate for productive clover 
stands (3-4 years red, 4-5 years white). Standard management: establishment (60-80 lb P₂O₅, 100-120 lb K₂O), 
production years (60-80 lb P₂O₅, 180-220 lb K₂O annually). Split K after each cutting maintains availability 
despite good retention - clover's rapid removal requires replenishment.

MANAGEMENT STRATEGY: Two-split K during production years: 60-70% early season (100-120 lb K₂O spring), 30-40% 
mid-season (60-80 lb K₂O after second cutting). P annually or every 2 years depending on soil test. Minimal 
N unless poor nodulation - soil test plus nodule check determine need. Good retention supports 3-4 cuts red 
clover (4-5 tons DM/ac annually) or continuous grazing white clover (3-4 tons).

GRASS-CLOVER MIXTURES: Excellent option in good-retention soils. Mixtures (50-60% grass + 40-50% clover by 
forage) combine grass structure with clover protein and N-fixation. Common mixtures: orchardgrass-red clover, 
tall fescue-white clover, timothy-alsike. Grass component receives modest N (60-80 lb N/ac annually) since 
clover provides 40-60 lb N/ac through transfer and residues.

POTASSIUM CRITICAL: K most limiting nutrient for clover persistence. Adequate K (180-220 lb K₂O/ac annually) 
ensures: strong stands, winter-hardiness, disease resistance, protein content, long stand life. Deficient K: 
thin stands, winter-kill, increased disease, shortened stand life. Good retention maintains K between 
applications.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for clover with intensive 
K management. Clover somewhat adapted to moderate fertility - more so than alfalfa, less than grasses. Stand 
life reduced: red clover 2-3 years, white clover 3-4 years. Three-split K compensates for moderate retention 
during growing season.

MANAGEMENT STRATEGY: Establishment: P banded (60-80 lb P₂O₅), K broadcast (100-120 lb K₂O). Production years: 
three-split K - early spring (80 lb K₂O), after first cut (70 lb K₂O), after second cut (60 lb K₂O), total 
210 lb K₂O annually. P annually (60-80 lb P₂O₅) - moderate retention requires more frequent P than high 
retention. Modest N (30-50 lb/ac) if nodulation poor due to pH <6.0.

NODULATION CHALLENGES: Moderate-retention soils often slightly acidic (pH 5.5-6.5). If pH <6.0, nodulation 
reduced. Lime to pH 6.0-6.5 improves nodulation dramatically. Mo deficiency possible below pH 6.0 - apply 
0.2-0.3 lb Mo/ac if liming not feasible immediately. Inoculation mandatory in moderate-retention conditions.

VARIETY-SPECIES SELECTION: White clover most tolerant of moderate fertility - consider for permanent pasture. 
Red clover acceptable but stand life 2-3 years vs 3-4 in better soils. Alsike clover excellent if soil also 
wet or acidic - tolerates pH 5.5-6.5 better than red/white. Grass-clover mixture strongly recommended over 
pure clover - grass component more adapted to moderate retention.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes clover challenging but VIABLE - 
more adaptable than alfalfa to poor conditions. White clover most successful (tolerates low fertility better 
than red clover). Stand life reduced: red clover 1-2 years, white clover 2-3 years. Intensive K management 
essential: four splits or fertigation.

MANAGEMENT STRATEGY: Establishment: P banded (60-80 lb P₂O₅), K broadcast (100-120 lb K₂O), lime to pH 6.0-
6.5 if needed. Production years: four-split K (50 + 50 + 50 + 40 = 190 lb K₂O/ac) or fertigation biweekly 
(15-20 lb K₂O/ac per injection, 10-12 injections annually). P annually: 60-80 lb P₂O₅. Supplemental N likely 
needed: 40-60 lb N/ac annually split with K due to poor nodulation.

NODULATION FAILURE: Low-retention soils typically acidic (pH 5.0-6.0), low Ca - severely inhibits clover 
nodulation. Even with lime and inoculation, expect <60% nodulation success. Must supplement with fertilizer 
N (40-60 lb N/ac annually). This reduces clover's economic advantage (N-fixing) but clover still viable due 
to moderate total demand and forage quality.

GRASS-CLOVER ESSENTIAL: Pure clover stands not recommended in low retention. Grass-clover mixture (60-70% 
grass + 30-40% clover) much better adapted. Grass component (tall fescue, orchardgrass) more tolerant of low 
retention. Apply N primarily for grass (80-120 lb N/ac annually) - don't rely on clover N-fixation. Clover 
component adds protein and some N but not primary N source.

VIABILITY: White clover viable for 2-3 tons/ac in low-retention soils primarily in mixtures. Red clover 
marginal - 1-2 year stands, lower yields (2-3 tons/ac). Economics depend on purpose: dairy/beef grazing 
(protein valuable) vs hay (quality variable). Better adapted than alfalfa but still challenging. Consider 
grass hay (less demanding) or grass-clover mixture (most practical approach).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes clover production extremely 
difficult. Even white clover's moderate demands and adaptability challenged by very-low-retention conditions. 
Stand life 1-2 years maximum. Pure clover stands not viable - grass-clover mixture only approach with any 
success potential.

MANAGEMENT OPTIONS: Grass-clover mixture (70-80% grass + 20-30% clover) with intensive fertilization. 
Establishment: P banded (60-80 lb P₂O₅), K broadcast (100-120 lb K₂O), lime heavily (2-4 tons/ac to pH 6.0-
6.5). Production: fertigation biweekly (12-18 lb N/ac, 18-25 lb K₂O/ac) or five splits (apply N-K together 
every 3-4 weeks during season).

NODULATION FAILURE: Very-low-retention soils almost always extremely acidic (pH 4.5-5.5) and Ca-deficient. 
Clover nodulation essentially zero even with lime, inoculation, and Mo. Must apply full N for grass component 
(100-140 lb N/ac annually) - cannot rely on clover N-fixation. Clover becomes minor component adding some 
protein but not fixing significant N.

SPECIES-VARIETY: White clover only species with any viability - most stress-tolerant. New Zealand white 
clover cultivars bred for grazing and persistence may survive 2-3 years with intensive management. Red clover 
fails completely (too demanding, short-lived even in good soils). Alsike clover possible if also wet (tolerates 
wet acidic conditions) but still marginal.

ALTERNATIVE USE: Short-term cover crop or green manure perhaps best use for clover in very-low-retention 
soils. Crimson clover (annual) planted fall, grows slowly through winter, rapid growth spring, terminated 
late spring. Even with poor nodulation, fixes 30-60 lb N/ac plus adds OM. Single-season use avoids perennial 
stand persistence challenges.

VIABILITY: Perennial clover stands not recommended in very-low-retention soils. Success rate very low, costs 
high, persistence poor. If attempting: grass-clover mixture only, white clover only, intensive fertigation, 
expect 1-2 year stand life, yields 1-2 tons/ac clover component. Better alternatives: grass hay (more adapted), 
annual clover cover crops (avoids persistence issues), or soil improvement before attempting forage legumes."""
    },

    "Grass Hay": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports highly productive grass 
hay (8-12+ tons/ac annually, 4-5 cuttings) with good nutrient use efficiency. Grasses are heavy N feeders 
(150-300 lb N/ac depending on yield level) - high retention reduces leaching losses and maintains availability 
through multiple cuttings. Good K retention critical - hay removal can reach 300-400 lb K₂O/ac annually at 
high production levels.

MANAGEMENT STRATEGY: Split N after each cutting: 50-60 lb N/ac after each of 4-5 cuttings, total 200-300 lb 
N/ac annually. K split similarly: 60-80 lb K₂O/ac after each cutting (K removed in hay proportional to yield 
- 40-50 lb K₂O/ton hay). High retention allows somewhat larger individual applications. P broadcast annually 
or every 2 years: 40-60 lb P₂O₅/ac. High retention minimizes P losses.

GRASS SPECIES: Cool-season grasses dominate hay production. 1) Orchardgrass (high-yielding 6-8 tons/ac, 
palatable, versatile). 2) Timothy (moderate yield 4-6 tons but excellent horse hay quality). 3) Tall fescue 
(persistent, tolerates stress, 5-7 tons). 4) Smooth bromegrass (cold-hardy northern species, 5-7 tons). 5) 
Warm-season: bermudagrass (southern regions, extremely high yield 8-10+ tons, requires intensive N). High 
retention supports all species excellently.

PROTEIN CONTENT: Grass hay protein content (CP%) depends primarily on N availability and cutting timing. 
Adequate N (200-300 lb N/ac split) plus early cutting (boot to early heading stage) produces 12-18% CP. High 
retention maintains N between applications ensuring consistent protein. Later cutting reduces CP (8-12%) and 
digestibility but increases tonnage.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC adequate for productive grass 
hay (6-8 tons/ac, 3-4 cuttings) with proper N-K management. Standard program: 150-250 lb N/ac and 200-300 lb 
K₂O/ac annually split after each cutting. P 40-60 lb P₂O₅/ac annually or every 2 years.

MANAGEMENT STRATEGY: Split applications essential despite good retention - grass hay makes rapid removal 
requiring frequent replenishment. After each cutting: 50-60 lb N/ac + 60-80 lb K₂O/ac. If 4 cuttings: total 
200-240 lb N + 240-320 lb K₂O. Adjust N rate to yield goal and quality needs (higher N for more protein). K 
rate based on removal (40-50 lb K₂O/ton hay - at 8 tons, need 320-400 lb K₂O/ac).

YIELD-QUALITY OPTIMIZATION: Good retention allows choice: high yield (late cutting, more tonnage, lower 
quality) or high quality (early cutting, less tonnage, higher protein/digestibility). Most operations: early 
first cutting (quality for lactating dairy or horses), later subsequent cuttings (tonnage for dry cows, 
stocker cattle). Split N program supports either strategy.

STAND LONGEVITY: Good retention promotes long stand life (5-10+ years) with proper management. Adequate K 
critical for persistence - K deficiency accelerates stand thinning, winter-kill, weed invasion. Annual soil 
tests plus tissue tests at first cutting monitor fertility status. Renovate stands when productivity declines 
<4 tons/ac or weeds >30%.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for grass hay (4-6 tons/
ac, 2-3 cuttings) with intensive split N-K applications. Smaller individual cuttings and longer intervals 
between cuttings than high-retention soils. Four-split program compensates for moderate retention.

MANAGEMENT STRATEGY: Four-split N-K: early spring green-up (50 lb N, 60 lb K₂O) + after first cutting (50 lb 
N, 60 lb K₂O) + after second cutting (40 lb N, 50 lb K₂O) + late season (30 lb N, 40 lb K₂O), total 170 lb 
N and 210 lb K₂O. P banded or broadcast: 40-60 lb P₂O₅ annually (moderate retention requires annual vs 
biennial P).

SPECIES SELECTION: Species selection critical in moderate retention. Tall fescue most adapted - deep roots 
(3-4 ft), stress-tolerant, persistent even under moderate fertility. Orchardgrass acceptable but less persistent 
than in high retention. Timothy marginal - prefers good fertility. Bermudagrass (warm-season) excellent if 
region suitable - tolerates moderate fertility better than cool-season grasses.

GRASS-LEGUME MIXTURE: Strongly recommended for moderate-retention hay. Mixture (60-70% grass + 30-40% legume, 
typically red clover or alfalfa) reduces N requirement (legume provides 60-100 lb N/ac) and improves protein. 
Apply N only to grass component (80-120 lb N/ac vs 170 lb N pure grass). Heavy K still required: 200-250 lb 
K₂O/ac for mixture.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes productive grass hay challenging. 
Yields limited to 3-5 tons/ac with intensive management. Five-split N-K or fertigation recommended. Grass-
legume mixture more practical than pure grass - reduces N requirement and improves economics.

MANAGEMENT STRATEGY: Pure grass: five splits N-K (35 + 35 + 30 + 30 + 25 = 155 lb N, 45 + 45 + 40 + 35 = 165 
lb K₂O) or fertigation biweekly (15-20 lb N/ac, 18-25 lb K₂O/ac, 8-12 injections annually). Grass-legume 
mixture (RECOMMENDED): three-split N-K (40 + 35 + 30 = 105 lb N, 50 + 45 + 40 = 135 lb K₂O) - legume provides 
50-80 lb N/ac reducing fertilizer N need.

SPECIES SELECTION: Tall fescue or bermudagrass most successful in low-retention hay. Both have: deep roots 
(access moisture/nutrients below surface), stress tolerance, persistence under challenging conditions. 
Orchardgrass marginal - moderate persistence. Timothy, smooth bromegrass not recommended - require better 
fertility. Bermudagrass excellent if southern region (very adapted to sandy low-retention soils common in 
Southeast).

GRAZING vs HAY: Consider managed grazing rather than hay in low-retention conditions. Advantages: 1) No 
nutrient removal (nutrients recycled through manure). 2) Lower input costs (no harvesting equipment). 3) Less 
nutrient demand (grazing removes less than hay). 4) Profitable even at lower forage yields. Rotational 
grazing (intensive management) produces equivalent returns to haying with lower inputs.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes productive grass hay extremely 
difficult. Yields 2-4 tons/ac maximum despite intensive inputs. Grass-legume mixture essential - pure grass 
not economical (N costs prohibitive). Fertigation or six-split program necessary. Economics marginal for hay 
- grazing more viable.

MANAGEMENT OPTIONS: Grass-legume mixture (70-80% grass + 20-30% legume): fertigation biweekly (18-25 lb N/ac, 
20-30 lb K₂O/ac, 10-14 injections) or six splits (20-25 lb N + 25-35 lb K₂O every 3-4 weeks during season). 
Pure grass: not recommended - N requirement (150+ lb/ac) combined with very sandy soil losses make economics 
impossible.

SPECIES-VARIETY: Bermudagrass only species with good success in very-low-retention hay. Deep roots (4-6 ft), 
extreme stress tolerance, persistence in sandy soils. Requires intensive N but much better adapted than cool-
season grasses. Cool-season options: tall fescue marginally viable, all others fail. Legume: white clover 
only (most tolerant) - red clover and alfalfa fail in very low retention.

GRAZING ALTERNATIVE: Managed grazing MUCH better option than hay in very-low-retention soils. Reasons: 1) 
Nutrient recycling through manure eliminates hay removal losses (saves 200-300 lb K₂O/ac). 2) Lower yield 
expectations acceptable (3-4 tons consumed vs 6-8 tons harvested as hay). 3) Rotational grazing matches 
frequent fertilization needs (apply N-K each rotation). 4) Economics better - no harvesting costs, lower 
inputs, acceptable returns even at modest yields.

VIABILITY: Grass hay production marginal in very-low-retention soils. Yields low (2-4 tons/ac), quality 
variable, input costs extremely high ($300-500/ac fertilization alone). Economics rarely favorable for hay. 
Better alternatives: 1) Rotational grazing (much better economics, avoids removal losses). 2) Bahiagrass or 
bermudagrass improved pasture (low-input persistent sods). 3) Soil improvement over 3-5 years before attempting 
productive hay. If attempting hay: bermudagrass only, fertigation mandatory, grass-legume mixture essential, 
expect marginal economics."""
    },

    "Silage Corn": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports extremely high biomass 
production (30-35+ tons/ac fresh weight, 8-10+ tons DM/ac) with good nutrient efficiency. Silage corn has 
HIGHER nutrient demands than grain corn - whole-plant harvest removes stover that would be returned in grain 
production. Requirements: 180-220 lb N, 80-120 lb P₂O₅, 180-240 lb K₂O per 30 tons fresh weight.

MANAGEMENT STRATEGY: Split N through growth stages: 40% pre-plant (70-90 lb N), 35% at V6-V8 stage (65-80 lb 
N), 25% at V10-V12/tasseling (45-55 lb N). Total N 10-15% higher than grain corn due to stover removal. All 
P plus most K pre-plant: 80-120 lb P₂O₅, 120-160 lb K₂O. Remaining K (40-60 lb K₂O) at V6-V8. High retention 
maintains nutrients through rapid growth phase (weeks 4-10) when corn accumulates 70% of biomass.

HARVEST TIMING: Optimal silage harvest: 32-38% dry matter (milk to early dent stage, 90-110 days depending 
on maturity). Earlier harvest (<30% DM): seepage losses, reduced nutrients, lower feed value. Later harvest 
(>40% DM): difficult packing, reduced digestibility. High retention supports adequate nutrition through black 
layer (physiological maturity) allowing harvest at optimal DM.

FORAGE QUALITY: High-quality silage corn: >70% TDN, >8% crude protein, >50% grain in DM, low fiber. Adequate 
nutrition (especially N and K) throughout season produces high digestibility and energy density. High retention 
prevents late-season deficiencies that reduce grain fill and forage quality.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC adequate for excellent silage 
corn (25-30 tons/ac fresh, 7-9 tons DM/ac) with proper split fertilization. Standard program: 180-220 lb N 
(three splits), 80-100 lb P₂O₅ (pre-plant), 180-220 lb K₂O (70% pre-plant + 30% V6-V8).

MANAGEMENT STRATEGY: Three-split N essential: 40% pre-plant (70-85 lb) + 35% V6-V8 (65-75 lb) + 25% V10-V12 
(45-60 lb). Higher N rate than grain corn due to stover removal (roughly 10-15% increase). K management 
critical - silage removes 5-7 lb K₂O/ton vs grain corn leaving most K in stover. Split K: 130-150 lb pre-
plant + 50-70 lb V6-V8 for total 180-220 lb K₂O.

VARIETY SELECTION: Silage corn varieties bred specifically for forage: higher digestibility, more grain (50-
55% grain in DM vs 40-45% conventional), improved stalk quality, optimized plant architecture. Choose maturity 
appropriate for region - silage harvested 5-10 days later than grain to reach 32-38% DM. Brown midrib (BMR) 
types: extremely high digestibility (75-80% TDN) but lower yields, more lodging - trade-off depends on feeding 
program.

YIELD-QUALITY BALANCE: Good retention supports choice: high yield (late-maturing varieties, later harvest) 
or high quality (earlier varieties, harvest at 32-35% DM). Most dairy operations prioritize quality for 
lactating cow rations. Beef operations may prioritize tonnage for backgrounding/finishing cattle. Split N 
supports either strategy.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for silage corn's 
heavy demands. Limits yields to 20-25 tons fresh (6-7 tons DM/ac). Four-split N compensates for moderate 
retention during rapid growth period. Intensive K management essential due to heavy removal in silage.

MANAGEMENT STRATEGY: Four-split N: 30% pre-plant (55-65 lb) + 30% V4-V6 (55-65 lb) + 25% V10-V12 (45-55 lb) 
+ 15% tasseling (30-35 lb), total 185-220 lb N. Earlier first side-dress (V4-V6 vs V6-V8) ensures availability 
before rapid uptake begins. K split: 60% pre-plant (110-130 lb) + 40% V6-V8 (75-90 lb), total 185-220 lb K₂O. 
P banded: 80-100 lb P₂O₅.

FORAGE QUALITY IMPACTS: Moderate retention produces acceptable forage quality with intensive management but 
challenges: lower grain percentage (45-50% vs 50-55% optimal), reduced TDN (65-70% vs 70-75%), variable 
digestibility. Still produces acceptable dairy or beef feed though not optimal. Harvest timing critical - 
must harvest at proper DM (32-38%) to maximize quality.

COMPARISON TO GRAIN CORN: At moderate retention, silage corn removes more nutrients than grain corn returns 
(silage: whole plant removed; grain: only grain removed, stover returned with 70% of K, 30% of N). This 
makes fertility management more critical for silage. Consider grain corn if retention marginal - lower removal, 
easier management, comparable or better economics depending on market.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes silage corn production 
challenging. Silage corn's heavy demands (180-220 lb N, 180-220 lb K₂O/ac) difficult to meet economically in 
low retention. Yields limited to 15-20 tons fresh (5-6 tons DM/ac). Fertigation or five-split program necessary. 
Economics marginal.

MANAGEMENT STRATEGY: Fertigation (RECOMMENDED): weekly injections 18-25 lb N/ac, 20-25 lb K₂O/ac for 10-14 
weeks (V4 through dent stage). Total 180-250 lb N, 200-250 lb K₂O through injections. P banded: 80-100 lb 
P₂O₅. Five-split alternative: apply N-K together weeks 0, 3, 6, 9, 12 (35-40 lb N + 40-45 lb K₂O each 
application).

FORAGE QUALITY CHALLENGES: Low retention produces quality problems: low grain percentage (40-45%), reduced 
TDN (60-65%), high fiber (reduced digestibility), variable quality. Suitable for dry cows, heifers, backgrounding 
cattle but marginal for lactating dairy. Even with intensive management, cannot achieve premium silage quality 
typical of better soils.

ALTERNATIVE FORAGES: Consider alternative silage crops better adapted to low retention: 1) Forage sorghum or 
sorghum-sudangrass (more stress-tolerant, lower N requirement, 12-18 tons fresh, acceptable quality). 2) 
Small grain silage (winter wheat, triticale - lower removal, earlier harvest, 8-12 tons fresh). 3) Grass-
legume haylage (lower yields but better quality, less demanding). All produce better economics than corn 
silage in low retention.

VIABILITY: Silage corn marginally viable for 15-20 tons fresh in low-retention soils. Economics marginal - 
high input costs (fertigation, intensive fertilization) versus modest yields and quality. Better alternatives 
exist (forage sorghum, grass-legume) for low-retention forage production. If growing silage corn: fertigation 
mandatory, expect quality issues, consider for backgrounding/finishing cattle (less demanding) not lactating 
dairy (requires high quality).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes silage corn production non-viable. 
Silage corn's extreme demands (180-220 lb N, 180-220 lb K₂O/ac) combined with whole-plant removal cannot be 
sustained in very-low-retention conditions. Even with intensive fertigation, quality and yield insufficient 
for economic production.

MANAGEMENT IMPOSSIBILITY: No practical management system produces acceptable silage corn in very-low-retention. 
Intensive fertigation twice-weekly still produces: severe deficiencies during rapid growth, poor ear development 
(grain <35% DM), high fiber/low digestibility (<60% TDN), variable maturity. Biomass may reach 12-18 tons 
fresh but quality so poor (mostly stalk, little grain) that feed value marginal.

QUALITY CRISIS: Very-low-retention silage corn produces unacceptable forage: very low grain (<35% of DM vs 
50-55% target), extremely high fiber (poor digestibility), very low energy (<58% TDN vs 70-75% target), very 
low protein (<6% CP vs 8-10%). Not suitable for any high-production livestock (lactating dairy, finishing 
cattle). Barely acceptable for maintenance rations (dry cows, replacement heifers) but even then, poor value 
per ton.

ALTERNATIVE FORAGES: DO NOT GROW silage corn in very-low-retention soils. Much better forage options: 1) 
Forage sorghum or sorghum-sudangrass (50% of silage corn's N requirement, similar or better yields in poor 
conditions, acceptable quality). 2) Pearl millet (extremely stress-tolerant, 15-20 tons fresh, moderate 
quality). 3) Sudangrass (lowest demands, 12-16 tons fresh, suitable for backgrounding). 4) Improved bermudagrass 
or bahiagrass pasture (low-input, persistent, grazing-based). All produce better economics than attempting 
silage corn.

VIABILITY: Silage corn production not recommended in very-low-retention soils. Technical barriers (inadequate 
nutrition despite intensive management, poor quality, inconsistent yields) and economic barriers (extreme 
costs, poor feed value, negative returns) make success virtually impossible. Among forage crops, silage corn 
one of WORST choices for very-low-retention conditions. Choose adapted forages (sorghum family, warm-season 
grasses) instead."""
    },
    
    # ========================================================================
    # VEGETABLE CROPS
    # ========================================================================

    "Tomatoes": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through tomato's long season (90-120 days from transplant to final harvest). Tomatoes are HEAVY 
feeders with extended harvest requiring sustained nutrient availability. Can apply substantial portion 
of seasonal requirements (200-250 lb N, 100-150 lb P₂O₅, 300-400 lb K₂O/ac) in pre-plant and early 
applications with good retention through harvest. High K retention particularly critical - tomatoes 
K-intensive for fruit quality, disease resistance, and continuous production.

MANAGEMENT STRATEGY: Pre-plant P-K broadcast or banded retained effectively. N split: 40-50% at 
transplant/establishment + 30-40% at first fruit set + 20-30% during peak harvest. High retention 
allows somewhat larger individual applications, reducing labor. Ca retention critical for preventing 
blossom-end rot - this physiological disorder occurs even in high-Ca soils if water stress prevents 
Ca uptake. Good CEC provides Ca buffer against temporary stress. Drip fertigation ideal for high-value 
crop but not mandatory in high-retention soils.

BLOSSOM-END ROT MANAGEMENT: High-retention soils help prevent BER by maintaining steady Ca availability. 
Even in these soils, side-dress Ca (gypsum) at flowering beneficial as insurance. Foliar Ca (calcium 
chloride or calcium nitrate sprays) supplements soil Ca during rapid fruit sizing.

ENVIRONMENTAL: Low leaching risk even with heavy fertilization. Important for water quality as tomatoes 
grown near water bodies in some regions. Good retention justifies precision fertilization for this 
high-value crop.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage 
through tomato season. Standard commercial tomato fertilization practices work well. Split N applications: 
30-40% at transplant + 30-40% at first fruit set + 20-30% mid-harvest + optional 10-20% late season 
for extended harvest. K split 2-3 times to maintain availability during heavy fruit load periods.

MANAGEMENT STRATEGY: Pre-plant P-K adequate for season with split application option for K. Side-dress 
applications every 2-3 weeks during harvest maintain plant nutrition and fruit quality. Ca management 
important - gypsum application before transplanting + periodic side-dress or foliar applications 
prevent blossom-end rot. Good conditions for both fresh market and processing tomatoes. Drip fertigation 
provides excellent control if available but not essential.

POTASSIUM CRITICAL: Tomatoes remove ~4 lb K₂O per ton fruit. For 40 ton/ac crop, 160 lb K₂O removed 
in fruit alone plus plant uptake. Split K applications (3-4 times through season) maintain availability 
in good-retention soils without excessive rates per application. Tissue testing at first fruit, peak 
bloom, and peak harvest guides K management.

CONSIDERATIONS: High-value crop justifies intensive management. Tissue test-guided fertigation or 
side-dress applications optimize nutrition and quality. These soils support multiple harvest flushes 
over extended period.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful management 
through long tomato season. Frequent split applications essential to prevent losses while maintaining 
plant nutrition. N split into 4-6 applications: small amount at transplant (20-30 lb N/ac) + weekly 
or biweekly applications 20-40 lb N/ac from first flower through mid-harvest. K requires 4-5 splits 
to prevent leaching and maintain fruit quality.

MANAGEMENT STRATEGY: Drip fertigation strongly recommended for moderate-retention soils. Allows weekly 
injections of N-K solutions maintaining steady plant nutrition without large applications that would 
leach. Without fertigation: side-dress every 10-14 days with soluble fertilizers. Use slow-release 
products (polymer-coated, sulfur-coated) for base application to extend availability between side-dress 
applications.

CALCIUM MANAGEMENT: Critical challenge in moderate-retention soils. Ca leaches more readily than in 
high-retention soils, increasing blossom-end rot risk. Strategy: gypsum at transplanting (200-300 lb/ac) 
+ side-dress gypsum every 2-3 weeks during fruit sizing + weekly foliar Ca sprays during rapid fruit 
growth. Maintain consistent moisture - fluctuations exacerbate BER even with adequate Ca.

SOIL IMPROVEMENT: Build OM through cover crops (winter rye after tomatoes). Each 1% OM increase 
improves retention and Ca buffering. Tomatoes' high value justifies soil improvement investments.

CONSIDERATIONS: Moderate retention increases management intensity and input costs. Calculate economics - 
may favor processing tomatoes (lower grade requirements) over fresh market (stringent quality standards) 
at this retention level.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC, sandy texture make tomato 
production challenging. Tomatoes' long season, heavy nutrient requirements, and sensitivity to deficiencies 
difficult to manage in low-retention soils. Drip fertigation essentially mandatory for commercial production. 
Weekly N-K injections (15-25 lb N/ac, 20-35 lb K₂O/ac per injection) maintain plant nutrition.

MANAGEMENT STRATEGY: Fertigation-based nutrition program: starter solution at transplanting + daily to 
weekly injections throughout season (adjust frequency based on rainfall and soil). Total season: 200-250 lb 
N/ac and 300-400 lb K₂O/ac delivered in 15-25 small applications. Use water-soluble fertilizers designed 
for injection systems. Side-dress applications alone inadequate - nutrients leach between applications.

BLOSSOM-END ROT EPIDEMIC RISK: Low Ca retention makes BER severe problem in these soils. Multi-pronged 
approach required: 1) Pre-plant gypsum (500-1000 lb/ac) provides Ca buffer. 2) Gypsum with every other 
fertigation injection or biweekly side-dress. 3) Calcium nitrate or calcium chloride in fertigation solution. 
4) Weekly foliar Ca sprays. 5) Maintain absolutely consistent moisture - any water stress triggers BER.

VIABILITY ASSESSMENT: High production costs ($200-350/ac for nutrients and application vs $100-150 in 
high-retention soils). Feasible only for fresh market tomatoes with premium prices ($20+/25-lb carton). 
Processing tomatoes ($80-100/ton) may not be profitable. Calculate break-even carefully. Determinate 
varieties (concentrated harvest) easier to manage than indeterminate types requiring extended nutrition.

ALTERNATIVE: Plasticulture system with raised beds, plastic mulch, and drip irrigation provides best 
environment for managing low-retention soils. Initial cost high but improves water and nutrient control.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes conventional field tomato 
production economically non-viable. Tomatoes' combination of high nutrient demands, long season, and 
sensitivity to deficiencies cannot be managed cost-effectively in very-low-retention soils with conventional 
methods.

MANAGEMENT OPTIONS: Only viable approach: intensive plasticulture system with daily drip fertigation. 
Requirements: raised beds (6-8 inches) with incorporated compost, plastic mulch, drip tape, injection 
system, daily fertigation schedule. Inject complete nutrient solution daily (5-10 lb N/ac, 3-5 lb P₂O₅/ac, 
8-12 lb K₂O/ac per injection) from transplant through harvest. Include Ca in every injection. Weekly foliar 
micronutrient applications supplement soil applications.

BLOSSOM-END ROT: Severe challenge even with intensive management. Sandy soils dry rapidly despite irrigation - 
any moisture fluctuation triggers BER. Strategy: pre-plant incorporation of 2-3 tons/ac gypsum + compost 
providing Ca buffer, daily fertigation with Ca-containing fertilizers, twice-weekly foliar Ca applications, 
multiple daily short irrigation cycles maintaining constant moderate moisture.

VIABILITY ASSESSMENT: Extreme input costs ($400-600/ac for nutrients, materials, and intensive management). 
Only justifiable for: 1) Specialty/heirloom tomatoes commanding super-premium prices ($3-4/lb vs $1-1.50 
for standard). 2) Early-season tomatoes (May-June production where earliness brings premium). 3) Small-scale 
high-value production direct to restaurants/farmers markets. Large-scale processing or standard fresh market 
production not economically viable.

ALTERNATIVE RECOMMENDATION: These soils not appropriate for field tomato production. Better alternatives: 
1) Greenhouse/high tunnel production with soilless media - eliminate soil limitations entirely. 2) Large 
container production (5-10 gallon pots with quality potting mix). 3) Extreme raised beds (12-18 inches) 
filled with imported loam/compost blend - essentially container production at field scale. 4) Reconsider 
crop choice - select vegetables better adapted to low-retention soils."""
    },
    
    "Peppers": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through pepper's extended season (90-120 days harvest period after transplant). Peppers extremely K-intensive 
(250-300 lb K₂O/ac for 20+ ton crop) - high retention essential for maintaining K availability during 
continuous fruit production. Can apply substantial seasonal requirements in 2-3 split applications with 
minimal losses.

MANAGEMENT STRATEGY: Pre-plant P-K broadcast or banded provides season-long availability. N split: 40-50% 
at transplant/early growth + 30-40% at first fruit set + 20-30% during peak production. K split 2-3 times 
through season supporting continuous flowering and fruit development. High retention means peppers access 
retained subsoil nutrients with their moderately deep roots (18-24 inches).

CALCIUM FOR BLOSSOM-END ROT: High retention provides good Ca buffer. BER less common in peppers than 
tomatoes but occurs in bell types, especially large-fruited cultivars. Pre-plant gypsum (200-300 lb/ac) 
+ periodic side-dress or foliar Ca during peak fruit load provides insurance. Hot peppers (jalapeño, 
serrano, etc.) rarely show BER.

FRUIT QUALITY: High K retention supports excellent fruit quality - thick walls, good color development, 
firmness, and disease resistance. Extended harvest period (multiple flushes over 3-4 months) exploits 
retention capacity of these soils.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage 
through pepper season. Standard commercial practices work well. Split N applications: 30-40% at transplant + 
30-40% at first fruit + 20-30% mid-season + optional application for extended harvest. K split 3 times 
minimum to maintain availability during heavy fruit loads.

MANAGEMENT STRATEGY: Pre-plant P-K provides base. Side-dress or fertigation every 2-3 weeks during harvest 
maintains nutrition. K particularly important - tissue testing at first harvest, peak harvest guides K 
management. Adequate K (tissue >3.5% K) essential for thick walls, good color, disease resistance. Ca 
management for large bell types: gypsum before transplanting + foliar Ca at first fruit set and during 
rapid fruit sizing.

EXTENDED PRODUCTION: Good retention supports continuous production over extended period. Multiple harvest 
flushes typical - initial flush, mid-season flush, late-season flush. Adequate nutrition maintains 
plant vigor and fruit quality through all flushes. Hot pepper types (smaller fruit, lower K demand per 
fruit) particularly well-suited to good-retention soils - less intensive management than bells.

CONSIDERATIONS: These soils support both fresh market bells and processing peppers (jalapeños, etc.) with 
standard management. Drip fertigation provides optimization but not essential.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful K management 
through extended pepper season. K leaching risk during summer rains significant - peppers' very high K 
demand (250-300 lb K₂O/ac) difficult to maintain in moderate-retention soils. Frequent split applications 
essential.

MANAGEMENT STRATEGY: Drip fertigation strongly recommended. Weekly K injections (20-30 lb K₂O/ac) maintain 
plant nutrition during continuous fruit production. N injections (15-20 lb N/ac weekly) prevent leaching 
losses. Without fertigation: side-dress every 10-14 days with high-K fertilizers (e.g., 15-5-30 or similar 
K-heavy blends). Foliar K applications supplement soil applications.

TISSUE TESTING: Essential in moderate-retention soils. Sample leaves biweekly during harvest. Target tissue 
K >3.5%, N 3.5-4.5%. Below targets indicates leaching losses - increase application frequency or rates. 
Adjust fertigation injection rates based on tissue results and plant appearance.

CALCIUM MANAGEMENT: Split Ca applications essential. Gypsum at transplant (300-400 lb/ac) + biweekly side-dress 
or fertigation injections + weekly foliar Ca during fruit sizing (bell types). Hot peppers less sensitive but 
benefit from Ca fertilization.

SOIL IMPROVEMENT: Build OM aggressively. Cover crops after peppers (winter rye, vetch). Each 1% OM increase 
improves K retention significantly. Peppers' high value justifies soil improvement investments.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes pepper K management extremely 
challenging. Peppers' very high K requirement combined with low soil retention creates continuous deficiency 
risk. Drip fertigation mandatory for commercial production. Weekly or twice-weekly N-K injections maintain 
plant nutrition.

MANAGEMENT STRATEGY: Fertigation program: 10-15 lb N/ac and 20-30 lb K₂O/ac injected weekly or twice 
weekly from transplant through final harvest. Total season: 180-220 lb N/ac and 250-350 lb K₂O/ac in 
15-25 applications. Use complete water-soluble fertilizers with high K ratios (1:0.5:2 or 1:0.5:3 
N:P:K ratios). Foliar K applications (potassium sulfate or potassium nitrate sprays) twice weekly supplement 
soil applications.

DEFICIENCY SYMPTOMS: Watch for K deficiency signs appearing rapidly in low-retention soils: marginal 
chlorosis and necrosis on older leaves, thin-walled fruit, poor color, blossom-end rot (Ca deficiency but 
exacerbated by K deficiency interfering with Ca uptake). Symptoms appear suddenly when soil K depleted by 
heavy fruit load or leaching rain. Emergency applications (foliar + side-dress) needed immediately.

VARIETY SELECTION: Hot peppers (jalapeño, serrano, cayenne) more viable than bells in low-retention soils. 
Smaller fruit size means lower total K requirement. Still challenging but more manageable. If growing bells, 
favor medium-sized varieties over large-fruited types.

VIABILITY: High input costs ($250-400/ac for fertigation, materials, labor). Only viable for fresh market 
with good prices. Processing peppers (lower value) marginal. Small-scale production for farmers markets 
more feasible than large-scale wholesale.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes pepper production extremely 
challenging to non-viable. Peppers' extremely high K requirement (highest among common vegetables) cannot 
be maintained in very-low-retention soils without extraordinary efforts.

MANAGEMENT OPTIONS: Only approach with any viability: intensive plasticulture with daily drip fertigation. 
Raised beds (6-8 inches) with incorporated compost, plastic mulch, drip tape, daily fertigation injections 
of N-K-Ca solutions. Inject complete nutrients daily during fruiting: 5-8 lb N/ac, 10-15 lb K₂O/ac, 
3-5 lb CaO/ac. Multiple daily short irrigation cycles maintain constant moisture and nutrient availability. 
Foliar applications (N-K-Ca-micronutrients) twice weekly supplement soil nutrition.

POTASSIUM CRISIS: K leaches within 24-48 hours of heavy rain even with daily fertigation. After rainfall 
>1 inch, immediately increase K injection rates for 3-5 days to replenish soil solution. Emergency foliar 
K applications after major rain events. Tissue test weekly to monitor K status.

VIABILITY ASSESSMENT: Extreme costs ($500-800/ac for materials, intensive fertigation, labor). Only possibly 
viable for: 1) Specialty hot peppers (habanero, ghost pepper, etc.) commanding premium prices ($4-8/lb). 
2) Small-scale direct-to-consumer sales where extreme quality commands high prices. 3) Very early season 
production where earliness brings large premiums. Standard fresh market bells or processing peppers absolutely 
not economically viable.

RECOMMENDATION: Very-low-retention soils inappropriate for field pepper production. Alternatives: 1) Greenhouse/ 
high tunnel with soilless media. 2) Container production (5-gallon minimum) with quality potting mix - hot 
peppers work well in containers. 3) Extreme raised beds (12-18 inches) with imported loam/compost blend. 
4) Choose different vegetables better adapted to low-retention environment."""
    },

    "Potatoes": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through potato's 100-120 day season and HEAVY nutrient requirements. Potatoes among most nutrient-demanding 
crops: 200-250 lb N, 100-150 lb P₂O₅, 250-350 lb K₂O per acre for 400-500 cwt/ac yield. High retention 
critical given massive nutrient applications and shallow root system (12-18 inches).

MANAGEMENT STRATEGY: Split N applications despite high retention - long season and shallow roots necessitate 
availability throughout. Pre-plant: 30-40% of total N (60-100 lb N/ac) incorporated. At emergence: 30-40% 
(60-100 lb N/ac) side-dressed. At tuber initiation: 20-30% (40-60 lb N/ac) side-dressed or fertigated. 
Avoid late N which delays maturity, reduces storage quality, increases hollow heart. All P-K pre-plant 
broadcast or banded - high rates needed.

POTASSIUM CRITICAL: Potatoes extremely K-intensive (highest of major row crops). K affects: tuber size, 
specific gravity (processing quality), disease resistance, storage quality, bruise resistance. High CEC 
essential for maintaining K availability through tuber bulking phase. Tissue testing at early bloom: >5% 
K in petioles indicates adequacy.

CALCIUM-QUALITY: Adequate Ca reduces internal defects (hollow heart, internal brown spot). High-retention 
soils usually adequate Ca. However, Ca competes with K uptake - at very high K applications, Ca deficiency 
possible even in high-Ca soils. Monitor and supplement if needed (gypsum side-dress at tuber initiation).

SULFUR-MICRONUTRIENTS: Potatoes require adequate S (20-30 lb S/ac), B (1-2 lb B/ac), Mn, Zn. High-retention 
soils often adequate but test to verify. S particularly important for scab resistance and processing quality.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
potato requirements. Standard commercial practices: split N (30-40% pre-plant, 30-40% emergence, 20-30% 
tuber initiation), total 200-240 lb N/ac. P-K pre-plant: 100-130 lb P₂O₅, 250-300 lb K₂O per acre for 
350-450 cwt/ac.

MANAGEMENT STRATEGY: Three-split N program standard. Timing critical - cutoff N applications 6-8 weeks 
before harvest to allow proper skin set and maturity. Late N delays maturity, reduces storage quality, 
lowers specific gravity (critical for processing). Good retention supports consistent quality yields.

POTASSIUM SPLIT: Consider split K application in high-yielding situations: 60-70% pre-plant + 30-40% at 
tuber initiation. Ensures K availability during critical tuber bulking period (weeks 6-12 after planting). 
Inadequate K: small tubers, poor specific gravity, increased disease susceptibility (early blight, late blight).

VARIETY CONSIDERATIONS: Russet types (Idaho russets, processing russets) require highest fertility and 
respond best to high retention. Round whites and reds slightly less demanding. Fingerlings and specialty 
types moderately demanding - good-retention soils support all types well.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC manageable for potatoes with 
intensive management but challenging. Potatoes' massive K requirement combined with moderate retention 
necessitates careful frequent applications. Shallow root system (12-18 inches) cannot compensate for 
moderate retention through deep scavenging.

MANAGEMENT STRATEGY: Four-split N program: pre-plant (25-30%, 50-70 lb N/ac), emergence (25-30%, 50-70 lb 
N/ac), early tuber initiation (25-30%, 50-70 lb N/ac), mid-tuber bulking (15-20%, 30-50 lb N/ac), total 
180-260 lb N/ac. More splits reduce individual application losses. K split: 50% pre-plant + 30% emergence + 
20% tuber initiation, total 250-300+ lb K₂O/ac.

FERTIGATION ADVANTAGE: Drip fertigation particularly beneficial in moderate-retention soils. Weekly injections 
maintain steady nutrient availability despite moderate soil storage capacity. Can inject N-K throughout season 
with precise timing. Reduces total fertilizer requirement 10-20% compared to dry applications while improving 
yield and quality.

SOIL TEXTURE: Moderate-retention potato soils typically sandy loam to loam - actually preferred potato 
textures (good tuber shape, skin finish, easy harvest). Moderate CEC adequate IF managed intensively. More 
challenging than high-retention but still commercially viable.

SCAB MANAGEMENT: Common scab (Streptomyces scabies) favored by alkaline conditions and K deficiency. In 
moderate-retention soils, maintain adequate K (reduces scab) and avoid over-liming (pH 5.2-5.8 optimal 
for scab suppression, though varieties vary). S applications (elemental S or ammonium sulfate) help acidify 
and suppress scab.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes potato production very 
challenging. Potatoes' combination of massive K requirement, shallow roots, and long season all problematic 
in low-retention soils. Frequent split N-K applications required but labor/cost intensive.

MANAGEMENT STRATEGY: Five or more N splits: pre-plant (20-25%), emergence (20-25%), early tuber initiation 
(20-25%), mid-tuber bulking (15-20%), late tuber bulking (10-15%), total 180-280 lb N/ac. Despite splits, 
significant N losses expected. K splits: 40-50% pre-plant + 30-40% emergence + 20-30% tuber initiation, 
total 280-350 lb K₂O/ac (higher total due to losses).

FERTIGATION ESSENTIAL: In low-retention soils, drip fertigation approaching mandatory for viable potato 
production. Weekly or twice-weekly N-K injections from emergence through tuber bulking. Typical injection: 
15-25 lb N/ac, 25-35 lb K₂O/ac per week for 10-14 weeks. Maintains constant supply despite poor retention. 
Dry fertilization alone has <50% efficiency in low-retention potato soils.

YIELD-QUALITY IMPACTS: Expect yields 250-350 cwt/ac (vs 350-500 cwt/ac in high-retention). Quality issues: 
variable tuber size, lower specific gravity (especially problematic for processing varieties), increased 
hollow heart and internal defects, poor storage quality. Economics marginal except with premium fresh market 
prices or contracts.

VARIETY SELECTION: Choose varieties specifically adapted to sandy soil conditions. Characteristics: moderate 
maturity (100-110 days, not full-season 130+ day types), good disease resistance (especially early blight 
common under stress), tolerance to variable moisture/nutrients. Norland, Red Pontiac better adapted than 
Russet Burbank or processing russets.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes commercial potato production 
economically non-viable in most situations. Potatoes' combination of extreme K demands, shallow root system, 
long season, and quality requirements incompatible with very-low-retention soils.

MANAGEMENT OPTIONS: Only possibly viable with extreme intensive drip fertigation: twice-weekly injections, 
20-30 lb N/ac + 35-45 lb K₂O/ac per injection, 20-24 injections per season. Total: 400-720 lb N/ac, 
700-1,080 lb K₂O/ac applied (actual crop use only 40-50% due to severe leaching). Costs $150-250/ac for 
fertilizer alone, plus drip system installation and operation.

CALCIUM-MAGNESIUM MANAGEMENT: Weekly Ca-Mg fertigation essential (3-5 lb Ca/ac, 1-2 lb Mg/ac). Without 
constant Ca supply, severe internal defects (hollow heart, internal brown spot, brown center). Very-low-
retention soils cannot buffer Ca availability - daily requirement must be supplied constantly.

QUALITY CRISIS: Even with intensive management, quality problems severe: low specific gravity (55-60 vs 
65-70 target for processing), excessive internal defects, poor storability, variable size. Processing 
potatoes essentially non-viable (cannot meet quality specifications). Fresh market potatoes marginal - 
small size, defects, poor appearance.

IRRIGATION CHALLENGE: Very sandy soils require frequent irrigation (daily or every other day). Each irrigation 
leaches nutrients despite fertigation. Must inject nutrients with every irrigation to maintain availability. 
Center pivot or solid-set sprinkler more practical than drip for very-low-retention potatoes (can cover 
larger area), but fertigation efficiency lower.

VIABILITY: Commercial potato production not recommended in very-low-retention soils. Multiple technical 
and economic barriers. If attempting: limit to small acreage (<10 acres), use extreme drip fertigation, 
target niche fresh market (farmers markets, CSA), choose early-maturing adapted varieties. Yields 150-250 
cwt/ac at best, costs $800-1,200/ac (vs $600-800/ac in good soils). Economics work only with direct-to-
consumer premiums."""
    },

    "Sweet Potatoes": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
but sweet potatoes have UNIQUE characteristics - moderate nutrient requirements compared to Irish potatoes. 
Sweet potatoes: 80-120 lb N, 40-80 lb P₂O₅, 120-180 lb K₂O for 400-600 bu/ac (20-30 tons/ac). Long season 
(100-120 days) but modest daily nutrient uptake rate. High retention advantageous but less critical than 
for many vegetables.

MANAGEMENT STRATEGY: Single pre-plant application often adequate in high-retention soils. Broadcast or 
incorporated: 80-100 lb N/ac, 40-60 lb P₂O₅, 120-150 lb K₂O. Sweet potatoes' unique growth pattern: slow 
initial growth (first 6-8 weeks), then rapid vine growth, then tuber bulking (final 6-8 weeks). High 
retention holds nutrients through all phases.

NITROGEN CAUTION: Sweet potatoes unusual - excessive N REDUCES quality. Over-fertilization (>120 lb N/ac) 
causes excessive vine growth at expense of tuber development. High-retention soils with high OM (>3%) may 
need REDUCED N application (60-80 lb N/ac) vs standard rates. Monitor vine growth - if extremely vigorous, 
reduce N next season.

POTASSIUM QUALITY: K critical for tuber quality - smooth skin, uniform shape, good color, high dry matter 
content (sweetness). High CEC ensures K availability during tuber bulking phase (final 8 weeks). Adequate 
K also improves storage quality and reduces post-harvest losses.

ADVANTAGES IN HIGH-RETENTION SOILS: 1) Can use lower N rates, reducing costs and vine management issues. 
2) Good K retention supports optimal quality. 3) pH buffering capacity (sweet potatoes prefer pH 5.0-6.5, 
tolerant to acidity). 4) Micronutrient availability good.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
sweet potato requirements. Standard practices: pre-plant 80-100 lb N/ac, 40-60 lb P₂O₅, 120-150 lb K₂O. 
Single application usually adequate through season, though split N optional (60% pre-plant + 40% at vine 
growth, 4-6 weeks after planting).

MANAGEMENT STRATEGY: Sweet potatoes well-adapted to good-retention soils. Avoid excessive N - promotes 
vine growth over tuber development. In good-retention soils with OM 2-3%, consider conservative N rates 
(70-90 lb N/ac total). K broadcast pre-plant or split 60% pre-plant + 40% at vine growth.

VARIETY CONSIDERATIONS: Storage types (Beauregard, Orleans, Covington) and fresh market types all respond 
well in good-retention soils. These soils support both table stock production (uniform #1 grades) and 
processing production (french fries, puree). Excellent conditions for organic sweet potato production 
(good fertility reduces N fertilizer needs).

COMPARATIVE ADVANTAGE: Sweet potatoes much better adapted to moderate-high retention soils than Irish 
potatoes. Lower nutrient requirements, less intensive management, fewer quality issues. In the sweet potato 
belt (Southeast US), most production occurs on good-retention loamy soils.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for sweet potatoes - 
sweet potatoes particularly well-suited to moderate-retention soils. This is sweet potato's advantage: 
productive at moderate retention levels. Many commercial sweet potato areas have moderate-retention soils.

MANAGEMENT STRATEGY: Split N application recommended: 60-70 lb N/ac pre-plant + 30-40 lb N/ac at vine growth 
(4-6 weeks after planting), total 90-110 lb N/ac. K split: 100-120 lb K₂O/ac pre-plant + 50-60 lb K₂O/ac 
at vine growth. P all pre-plant (40-60 lb P₂O₅/ac).

SWEET POTATO ADAPTATION TO MODERATE-RETENTION: Multiple advantages: 1) Modest nutrient requirements vs 
other vegetables. 2) Acid-tolerant (pH 5.0-6.5 optimal) common in moderate-retention soils. 3) Drought-
tolerant once established - moderate-retention soils often sandy and droughty; sweet potatoes handle this. 
4) Few fertility-related quality problems compared to Irish potatoes. 5) Long storage roots (2-4 ft) 
scavenge nutrients deeper than shallow-rooted crops.

SOIL TEXTURE PREFERENCE: Moderate-retention sweet potato soils typically sandy loam texture - actually 
PREFERRED for sweet potatoes. Produces smooth, uniform, well-shaped tubers (vs heavy clay which produces 
rough, misshapen tubers). Easy digging at harvest. This is sweet potato's ideal soil type.

ECONOMIC ADVANTAGE: Sweet potatoes economically competitive in moderate-retention soils. Lower input costs 
than most vegetables, good yields (300-500 bu/ac achievable), good storage life (6-12 months under proper 
conditions). Excellent choice for moderate-retention vegetable production.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but sweet potatoes STILL VIABLE - 
much better adapted than most vegetables to low-retention soils. Sweet potatoes' combination of moderate 
nutrient needs, deep roots, drought tolerance, and acid tolerance makes them excellent choice for challenging 
soils.

MANAGEMENT STRATEGY: Split N: 50-60 lb N/ac pre-plant + 30-40 lb N/ac at vine growth + 20-30 lb N/ac at 
early tuber bulking, total 100-130 lb N/ac. K split: 80-100 lb K₂O/ac pre-plant + 50-60 lb K₂O/ac at vine 
growth + 40-50 lb K₂O/ac at tuber bulking. Multiple splits compensate for low retention. P banded at 
planting (40-60 lb P₂O₅/ac).

ROOT SYSTEM ADVANTAGE: Sweet potato storage roots extend 2-4 ft deep with extensive lateral spreading. 
Much deeper than Irish potato (12-18 inches). This deep rooting allows sweet potatoes to recover nutrients 
from depth that other vegetables cannot reach. Effectively increases "retention" from plant perspective 
even though soil retention poor.

ACID TOLERANCE: Critical advantage in low-retention soils typically acidic (pH 5.0-6.0). Sweet potatoes 
thrive at pH 5.0-6.0 - optimal range. Irish potatoes, tomatoes, peppers require pH 6.0-7.0. Sweet potatoes 
adapted to conditions that challenge other vegetables.

DROUGHT TOLERANCE: Low-retention sandy soils drought-prone. Sweet potatoes excel - among most drought-
tolerant vegetables. Can produce acceptable yields with 25-30% less water than Irish potatoes or tomatoes. 
If irrigation limited, sweet potatoes viable where other vegetables fail.

VIABILITY: Sweet potatoes viable and often PREFERRED vegetable for low-retention soils. Yields 250-400 bu/ac 
achievable with split fertilization. Economics better than most vegetables at this retention level. Traditional 
sweet potato production occurs extensively on sandy low-retention Coastal Plain soils.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but sweet potatoes STILL AMONG BEST 
vegetable options. Sweet potatoes' unique combination of characteristics makes them one of few vegetables 
viable in very-low-retention soils: deep roots, drought tolerance, acid tolerance, moderate nutrient needs, 
forgiving nature.

MANAGEMENT OPTIONS: Multiple split applications: pre-plant (40 lb N/ac), vine growth at 4 weeks (30 lb N/ac), 
early tuber bulking at 8 weeks (30 lb N/ac), mid-tuber bulking at 12 weeks (20 lb N/ac), total 120-140 lb 
N/ac. K splits: similar pattern, 60-80-60-40 lb K₂O/ac, total 240-280 lb K₂O. Fertigation through sprinkler 
irrigation beneficial if available: biweekly injections 15-20 lb N/ac, 25-30 lb K₂O/ac.

DEEP ROOT ADVANTAGE: In very sandy soils, sweet potato roots penetrate 3-5 ft, spreading 4-6 ft laterally. 
This massive root system intercepts nutrients across large volume and recovers nutrients that leached beyond 
reach of other crops. Makes sweet potatoes dramatically more viable than shallow-rooted vegetables (lettuce, 
spinach, Irish potatoes, peppers) in very sandy conditions.

STRESS TOLERANCE: Sweet potatoes tolerate multiple stresses common in very-low-retention soils: 1) Extreme 
acidity (pH 4.5-5.5 acceptable, though 5.0-6.0 preferred). 2) Low Ca (most vegetables fail, sweet potatoes 
continue). 3) Drought cycles from poor water retention. 4) Heat stress (high soil temps in exposed sandy 
soil). 5) Al toxicity at low pH (sweet potatoes moderately tolerant).

VARIETY SELECTION: Choose varieties bred for sandy soil adaptation. Beauregard, Orleans, Covington all 
adapted to deep sandy soils. These varieties developed in regions with extensive very sandy soils (North 
Carolina, Louisiana, Mississippi Coastal Plain).

VIABILITY: Sweet potatoes viable for 200-350 bu/ac production in very-low-retention soils with split 
fertilization or fertigation. Economics still viable - input costs higher but yields acceptable, storage 
life good. Sweet potatoes among TOP CHOICES for vegetable production in very-low-retention soils. If growing 
vegetable in very sandy conditions, consider sweet potatoes first."""
    },

    "Cucumbers": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through cucumber's 50-70 day harvest period and HEAVY continuous nutrient requirements. Cucumbers: 150-200 lb 
N, 80-120 lb P₂O₅, 150-200 lb K₂O for 700+ bushels/ac. Rapid growth, continuous fruit production, and 
shallow root system (12-18 inches) make retention critical.

MANAGEMENT STRATEGY: Multiple split N applications essential despite high retention - shallow roots and 
continuous fruiting necessitate constant availability. Pre-plant: 30-40% (50-80 lb N/ac). At flowering: 
30-40% (50-70 lb N/ac). Mid-harvest: 20-30% (30-50 lb N/ac). Late harvest: optional 10-20% (15-30 lb N/ac) 
for extended season. P-K pre-plant broadcast or banded.

POTASSIUM FOR QUALITY: K critical for cucumber fruit quality - straight fruit, uniform color, crispness, 
shelf life, disease resistance. High retention maintains K availability during continuous fruit production 
phase. Tissue testing mid-season: >3.5% K in recent mature leaves indicates adequacy.

CALCIUM-QUALITY: Adequate Ca reduces blossom-end rot-like defects (shrunken discolored fruit ends). High-
retention soils usually adequate but Ca competes with high K uptake. Monitor and supplement (gypsum or 
calcium nitrate) if fruit quality issues appear.

FERTIGATION ADVANTAGE: Drip fertigation excellent for cucumbers in high-retention soils. Weekly injections 
15-25 lb N/ac, 15-25 lb K₂O/ac during flowering and harvest maintain optimal nutrition with minimal loss.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
cucumber requirements. Standard practices: split N (30-40% pre-plant, 30-40% flowering, 20-30% mid-harvest), 
total 150-180 lb N/ac. P-K pre-plant: 80-100 lb P₂O₅, 150-180 lb K₂O per acre for 500-700 bushels/ac.

MANAGEMENT STRATEGY: Three-split N program adequate in good-retention soils. Timing aligned with growth 
stages: establishment (first 3 weeks), flowering and early harvest (weeks 4-6), peak harvest (weeks 7-10). 
Cucumbers' shallow roots require readily available nutrients in upper 12-18 inches throughout season.

VARIETY CONSIDERATIONS: Slicing cucumbers, picklingcucumbers (cucumbers for processing), specialty types 
(English, Persian, Kirby) all respond well in good-retention soils. These soils support both fresh market 
and processing production. Excellent for greenhouse/high tunnel production where retention combined with 
controlled environment optimizes yields.

DISEASE-FERTILITY INTERACTION: Good fertility improves disease resistance - especially important for cucumbers 
susceptible to many diseases (powdery mildew, downy mildew, bacterial wilt, anthracnose). Adequate K and Ca 
strengthen cell walls. Avoid excessive N which promotes lush growth favoring disease.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful management 
for cucumbers' demanding season. Shallow roots cannot compensate for moderate retention. Four-split N program: 
pre-plant (25-30%), flowering (25-30%), early harvest (25-30%), mid-harvest (20-25%), total 150-180 lb N/ac.

MANAGEMENT STRATEGY: More frequent smaller applications compensate for moderate retention and shallow roots. 
K split: 60% pre-plant + 40% at flowering maintains availability through harvest. Fertigation highly beneficial 
in moderate-retention soils - weekly injections 15-20 lb N/ac, 15-20 lb K₂O/ac from flowering through harvest.

MULCHING BENEFIT: Black plastic mulch particularly beneficial in moderate-retention soils. Benefits: 1) 
Reduces nutrient leaching from rainfall (mulch sheds rain). 2) Maintains steady soil moisture (reduces 
nutrient concentration fluctuations). 3) Warms soil (cucumbers warm-season crop). 4) Reduces disease pressure. 
5) Concentrates feeder roots under mulch where fertilizer bands placed.

SOIL TEXTURE: Moderate-retention cucumber soils typically sandy loam - acceptable for cucumbers though loam 
preferred. Requires irrigation for consistent production. Plastic mulch + drip irrigation + fertigation 
combination optimal for moderate-retention cucumber production.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes cucumber production challenging. 
Cucumbers' combination of shallow roots, high nutrient demands, and continuous harvest all problematic in 
low-retention soils. Intensive fertigation approaching mandatory.

MANAGEMENT STRATEGY: Drip fertigation with weekly injections: 15-25 lb N/ac, 15-25 lb K₂O/ac per week from 
flowering through harvest (typically 6-10 weeks, total 90-250 lb N/ac, 90-250 lb K₂O). Dry fertilization 
alone insufficient - shallow roots in low-retention soil cannot maintain nutrition. Plastic mulch + drip 
tape + daily irrigation + weekly fertigation standard commercial system for low-retention soils.

SPECIAL CHALLENGES: 1) Rapid nutrient fluctuations - low retention means heavy rain leaches nutrients quickly, 
causing quality swings. 2) Increased disease pressure under stress. 3) Misshapen fruit common (uneven 
nutrition). 4) Short productive period (4-6 weeks vs 6-8 weeks in better soils). 5) Lower total yield (350-500 
bushels/ac vs 600-800 bushels/ac).

VARIETY SELECTION: Choose varieties specifically bred for stress tolerance. Characteristics: parthenocarpic 
(sets fruit without pollination - important when stress reduces pollinator activity), disease-resistant, 
adapted to frequent harvest, uniform fruit size under variable conditions.

VIABILITY: Cucumbers marginally viable in low-retention soils. High input costs (drip system, plastic mulch, 
intensive fertigation, frequent harvest) while yields reduced. Viable only with: 1) High fresh market prices 
(direct-to-consumer, farmers markets). 2) Processing contracts (pickles). 3) Greenhouse/high tunnel production 
(controls environment). Field production in low-retention soils economically marginal for wholesale markets.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes field cucumber production 
extremely challenging to non-viable. Cucumbers' shallow roots (12-18 inches, shallower than most vegetables) 
combined with heavy continuous nutrient demands incompatible with very-low-retention soils.

MANAGEMENT OPTIONS: Only potentially viable approach: intensive raised-bed plasticulture with daily fertigation. 
Raised beds (6-8 inches) with incorporated compost (2-3 inches), plastic mulch, drip tape, daily complete 
nutrient injections. Inject 5-10 lb N/ac, 5-10 lb K₂O/ac, 2-3 lb CaO/ac daily during harvest period. Tissue 
test twice weekly to monitor nutrient status and adjust injection rates.

SHALLOW ROOT CRISIS: Cucumbers have shallowest root system among common vegetables. In very-low-retention 
soils, effective rooting depth only 8-12 inches (vs 12-18 inches in better soils). Nutrients leach below 
this rapidly. Daily fertigation mandatory - cannot maintain nutrition with even twice-weekly injections.

QUALITY PROBLEMS: Even with intensive management, quality issues severe: crooked fruit (uneven Ca/K nutrition), 
pale color, bitterness (stress response), soft texture, poor shelf life. Fruit sizing highly variable. 
Disease pressure extreme (stressed plants susceptible).

ALTERNATIVE SYSTEMS: 1) Greenhouse production with soilless media (perlite, coconut coir, rockwool) - 
completely avoids soil retention issues, achieves excellent quality and yields. 2) Large container production 
(5-gallon minimum) with quality potting mix. 3) Extreme raised beds (12-18 inches) with imported loam + 
compost blend. 4) Abandon field production in very-low-retention soil.

VIABILITY: Field cucumber production not economically viable in very-low-retention soils for commercial 
purposes. Costs ($600-900/ac for materials and intensive management) vs yields (250-400 bushels/ac) vs 
quality problems make economics impossible for wholesale. Small-scale production for farmers markets possibly 
marginal with premium prices. Strongly recommend alternative vegetables better adapted to very sandy conditions 
(sweet potatoes, watermelons, peanuts) or alternative production systems (greenhouse, containers)."""
    },

    "Squash": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through squash's 60-100+ day season (summer vs winter types) and HEAVY nutrient requirements. Summer squash: 
150-180 lb N, 80-100 lb P₂O₅, 150-200 lb K₂O for 800+ bushels/ac continuous harvest. Winter squash: 180-220 lb 
N, 100-130 lb P₂O₅, 200-250 lb K₂O for 30+ tons/ac. High retention supports vigorous vine growth and heavy 
fruit production.

MANAGEMENT STRATEGY: Summer squash (zucchini, yellow squash): Split N (40% pre-plant, 30% early flowering, 
30% mid-harvest) supports continuous 6-8 week harvest period. Weekly side-dress applications maintain production. 
Winter squash (butternut, acorn, hubbard): Split N (40% pre-plant, 40% vine growth, 20% early fruit set) 
through long 100-120 day season. All P-K pre-plant: high rates support massive vine system and fruit load.

POTASSIUM IMPORTANCE: K critical for fruit quality in both types. Summer squash: straight fruit, tender skin, 
good flavor, disease resistance during continuous harvest. Winter squash: rind hardness, storage quality 
(4-6 months), sweetness, dry matter content. High retention ensures K availability through extended fruiting 
periods.

CALCIUM MANAGEMENT: Adequate Ca for cell structure and storage quality (especially winter types). High-
retention soils usually adequate but monitor if very high K applications used (K competes with Ca uptake). 
Gypsum side-dress at fruit set supplements if needed.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
squash requirements. Standard practices: Summer squash - split N (40% pre-plant, 30% flowering, 30% mid-
harvest), total 150-170 lb N/ac. Winter squash - split N (40% pre-plant, 40% vine growth, 20% fruit set), 
total 180-200 lb N/ac. P-K pre-plant: 80-110 lb P₂O₅, 150-200 lb K₂O per acre.

MANAGEMENT STRATEGY: Three-split N program adequate for both types in good-retention soils. Summer squash 
benefits from weekly side-dress (10-15 lb N/ac) during harvest to maintain plant vigor and continuous 
production. Winter squash: heavier application at vine growth stage supports massive vine development 
(15-20 ft spread), then moderate application at fruit set supports fruit bulking without promoting late 
excessive vine growth.

TYPE COMPARISONS: Zucchini most productive summer type (800+ bushels/ac). Yellow summer squash similar. 
Patty pan slightly lower yielding. Winter types: Butternut (25-35 tons/ac), Acorn (20-30 tons/ac), Hubbard 
and Kabocha (25-35 tons/ac). All types respond well to good-retention soils with proper split fertilization.

DISEASE-FERTILITY: Good nutrition improves disease resistance - critical for squash susceptible to powdery 
mildew, vine borers, bacterial wilt. Adequate K and Ca strengthen plant tissues. Avoid excessive N promoting 
lush growth favoring powdery mildew.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful management for 
squash's heavy and continuous needs. Four-split N program for summer squash: pre-plant (30%), flowering 
(25%), early harvest (25%), mid-harvest (20%), total 150-180 lb N/ac. Winter squash: pre-plant (30%), 
early vine growth (30%), mid-vine growth (25%), fruit set (15%), total 180-210 lb N/ac.

MANAGEMENT STRATEGY: More frequent applications compensate for moderate retention. Summer squash: biweekly 
side-dress (12-18 lb N/ac) during 6-8 week harvest maintains vigor despite moderate soil storage. Winter 
squash: three applications during vine growth phase (weeks 4-10) ensure nutrients available during massive 
vine development. K split: 60% pre-plant + 40% at flowering/vine growth.

FERTIGATION BENEFIT: Drip fertigation particularly beneficial for squash in moderate-retention soils. Weekly 
injections 15-20 lb N/ac, 15-25 lb K₂O/ac maintain steady nutrition. Plastic mulch + drip combination improves 
efficiency and reduces disease pressure (foliage stays dry, soil splash reduced).

VARIETY SELECTION: Summer squash: choose early, compact varieties (Black Beauty zucchini, Early Prolific 
yellow) better adapted to moderate fertility than large spreading types. Winter squash: favor small-fruited 
types (Butterbaby, Table Ace acorn) over very large types (Blue Hubbard, Giant Pumpkins) in moderate-retention 
soils.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes squash production challenging, 
especially winter types. Summer squash more viable than winter types - shorter season, smaller plant size, 
lower total nutrient demand. Five or more N splits required: pre-plant (25%), flowering (20%), early harvest 
(20%), mid-harvest (20%), late harvest (15%), total 140-180 lb N/ac.

MANAGEMENT STRATEGY: Drip fertigation highly recommended in low-retention soils. Weekly injections 15-20 lb 
N/ac, 20-25 lb K₂O/ac from flowering through harvest. Plastic mulch + drip system standard for low-retention 
squash production. Dry fertilization alone has <50% efficiency - shallow summer squash roots (12-18 inches) 
and somewhat deeper winter squash roots (24-30 inches) cannot maintain nutrition without constant supply.

YIELD IMPACTS: Summer squash: 400-600 bushels/ac (vs 700-900 bushels/ac in high-retention). Winter squash: 
15-25 tons/ac (vs 25-35 tons/ac). Quality issues: smaller fruit size, variable size distribution, shorter 
harvest period (summer types), reduced storage quality (winter types). Disease pressure increases under stress.

TYPE RECOMMENDATIONS: Summer squash more viable than winter types in low-retention soils: 1) Shorter season 
(60-75 days vs 100-120 days) reduces loss exposure. 2) Smaller plant size = lower total nutrient demand. 
3) Continuous harvest allows nutrition monitoring and adjustment. Zucchini most reliable summer type. If 
growing winter squash, choose early varieties (Buttercup, Delicata) over late full-season types.

VIABILITY: Summer squash viable with drip fertigation for 400-600 bushels/ac. Winter squash marginally 
viable - high inputs, moderate yields, quality variables. Economics depend on market - fresh market premiums 
vs wholesale pricing critical.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes squash production extremely 
challenging. Summer squash marginally possible with intensive management; winter squash generally not viable.

SUMMER SQUASH MANAGEMENT: Only possibility: intensive raised-bed plasticulture. Raised beds (6-8 inches) 
with incorporated compost, plastic mulch, drip tape, daily or twice-weekly fertigation. Inject 10-15 lb 
N/ac, 15-20 lb K₂O/ac per injection during flowering and harvest (typically 8-12 injections over 6-8 week 
season). Compact varieties only (1-2 ft spread vs 3-4 ft standard). Yields 300-500 bushels/ac at best.

WINTER SQUASH CHALLENGES: Generally not recommended. Problems: 1) Long season (100-120 days) = extended 
nutrient loss exposure. 2) Massive vine system (15-20 ft spread) = extremely high total nutrient demand. 
3) Large fruit development = concentrated late-season K demand difficult to supply. 4) Storage quality poor 
(low dry matter, thin rinds, poor keeping). Even with intensive fertigation, winter squash quality inadequate 
for commercial marketing.

ALTERNATIVE APPROACHES: 1) Container production - summer squash works in large containers (15-20 gallon) 
with quality potting mix. 2) Extreme raised beds (12-18 inches) with imported loam + compost. 3) Small-scale 
intensive beds for farmers market/CSA. 4) Greenhouse/high tunnel with soilless media (summer squash only, 
trellised).

VIABILITY ASSESSMENT: Summer squash marginally viable for small-scale production with premium prices. Winter 
squash not recommended - technical and economic barriers too great. Costs $500-700/ac for raised bed system, 
yields 300-500 bushels/ac summer squash, quality variable. Winter squash yields <15 tons/ac with poor storage 
quality - not commercially viable.

RECOMMENDATION: In very-low-retention soils, avoid winter squash. Summer squash only for small-scale 
intensive production. Consider alternative vegetables better adapted: sweet potatoes (deep roots, drought 
tolerant), watermelons (moderate retention requirements), snap beans (short season, N-fixing)."""
    },

    "Pumpkins": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through pumpkin's long season (100-120 days) and HEAVY nutrient requirements for massive vine systems 
and large fruit. Pumpkins: 150-200 lb N, 100-150 lb P₂O₅, 200-250 lb K₂O for 25+ tons/ac. High retention 
critical given extensive vine spread (15-20 ft) and concentrated fruit bulking period.

MANAGEMENT STRATEGY: Split N to match growth phases: 40% pre-plant (60-80 lb N/ac), 40% early vine growth 
weeks 4-6 (60-80 lb N/ac), 20% fruit set week 8 (30-40 lb N/ac). Avoid late N which delays maturity, 
reduces color, poor storage. All P-K pre-plant broadcast - massive rates support both vine and fruit 
development. High retention holds nutrients through long season despite large plant demands.

POTASSIUM-COLOR: K critical for orange color development in jack-o-lantern types. Adequate K (220-250 lb 
K₂O/ac) ensures deep orange color, hard rind, good storage (4-6 months). High CEC maintains K availability 
during concentrated fruit maturation period (final 4-6 weeks).

SIZE MANAGEMENT: High-retention soils support large-fruited types (50-100+ lb giant pumpkins). For consistent 
commercial sizes (10-20 lb jack-o-lanterns), moderate vine vigor through controlled N timing prevents 
excessive vegetative growth that produces variable fruit sizes.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
pumpkin requirements. Standard practices: split N (40% pre-plant, 40% vine growth, 20% fruit set), total 
150-200 lb N/ac. P-K pre-plant: 100-130 lb P₂O₅, 200-230 lb K₂O for 18-25 tons/ac.

MANAGEMENT STRATEGY: Three-split N program adequate. Timing critical: cutoff N at fruit set (week 8-10) 
allows 10-12 weeks for fruit maturation and color development. Late N delays maturity, reduces color, 
increases vine growth at expense of fruit quality. K availability through fruit maturation (September-October 
harvest) ensures color and rind hardness.

VARIETY CONSIDERATIONS: Medium-sized jack-o-lanterns (12-20 lb) ideal for good-retention soils. Large 
carving types (20-30 lb), mini pumpkins (1-3 lb), and pie pumpkins (5-8 lb) all well-adapted. Good 
retention supports multiple fruits per vine - 3-5 fruits typical on jack-o-lantern types.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful management 
of pumpkin's heavy and concentrated demands. Four-split N: pre-plant (30%), early vine growth (30%), 
mid-vine growth (25%), fruit set (15%), total 150-200 lb N/ac. K split: 60% pre-plant + 40% at vine 
growth.

MANAGEMENT STRATEGY: More frequent applications compensate for moderate retention and long season. Drip 
fertigation beneficial: biweekly injections 15-20 lb N/ac, 20-25 lb K₂O/ac during vine growth and fruit 
development phases. Plastic mulch + drip combination improves efficiency.

SIZE-TYPE SELECTION: Moderate-retention soils favor small to medium types. Pie pumpkins (4-8 lb) and 
medium jack-o-lanterns (10-15 lb) more reliable than large types (20+ lb). Miniature pumpkins (1-3 lb) 
excellent choice - lower total nutrient demand, earlier maturity (90-100 days vs 110-120 days), 2-3 week 
shorter loss exposure.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes pumpkin production challenging, 
especially large types. Five or more N splits required or drip fertigation mandatory. Weekly injections 
15-20 lb N/ac, 20-25 lb K₂O/ac from vine growth through fruit set (typically 10-12 weeks). Plastic mulch 
+ drip system standard for low-retention pumpkin production.

MANAGEMENT CHALLENGES: 1) Long season (100-120 days) = extended loss exposure. 2) Massive vine system = 
high total demand. 3) Concentrated late-season K demand difficult to supply as soil retention depletes 
through season. 4) Color and rind quality issues common (inadequate late-season K). 5) Storage quality 
reduced (soft rinds, decay).

TYPE RECOMMENDATIONS: Small pie pumpkins (4-6 lb) most viable - shortest season (95-105 days), lowest 
total nutrient demand, acceptable quality despite challenging conditions. Mini pumpkins (1-3 lb) also 
good choice. Large jack-o-lanterns (20+ lb) generally not viable - quality problems, economics marginal.

VIABILITY: Pie and mini pumpkins viable for 12-18 tons/ac with drip fertigation. Jack-o-lanterns marginally 
viable, quality variable. Economics depend on direct marketing vs wholesale - premium prices needed for 
low-retention production costs.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes pumpkin production extremely 
challenging to non-viable. Pumpkins' combination of long season, massive vine systems, and heavy late-
season K demands incompatible with very-low-retention soils.

MANAGEMENT OPTIONS: Only potentially viable for small pie pumpkins with intensive raised-bed system. 
Raised beds (6-8 inches) with incorporated compost, plastic mulch, drip tape, twice-weekly complete 
nutrient injections. Inject 10-15 lb N/ac, 15-20 lb K₂O/ac per injection from vine growth through fruit 
maturation (12-14 injections). Compact, short-vined varieties only.

QUALITY CRISIS: Even with intensive management, quality problems severe: pale color (inadequate late K), 
thin soft rinds (poor storage, decay), small fruit (inadequate nutrition during bulking), variable sizing 
(inconsistent nutrition). Processing quality (for puree) also poor - low dry matter, poor color.

VIABILITY ASSESSMENT: Field pumpkin production not economically viable. Costs $600-800/ac for intensive 
raised bed system vs yields 8-12 tons/ac pie pumpkins (poor quality) or <8 tons/ac jack-o-lanterns (very 
poor quality). Direct-to-consumer marketing with premium prices possibly marginally viable for small pie 
pumpkins only.

RECOMMENDATION: Avoid pumpkin production in very-low-retention soils. If attempting: limit to small pie 
pumpkins (<5 lb), small acreage (<2 acres), intensive raised beds, direct marketing only. Jack-o-lanterns 
and large types not viable. Consider alternative crops better adapted to very sandy conditions."""
    },

    "Watermelon": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through watermelon's long season (85-100 days) and HEAVY nutrient requirements. Watermelons: 150-200 lb N, 
80-120 lb P₂O₅, 200-300 lb K₂O for 40+ tons/ac. Very high K requirement critical for sugar accumulation 
(12-13° Brix target), flesh firmness, and rind strength.

MANAGEMENT STRATEGY: Split N through growth phases: 30-40% pre-plant (50-80 lb N/ac), 30-40% vine growth 
weeks 3-5 (50-70 lb N/ac), 20-30% fruit set week 6-7 (40-60 lb N/ac). Cutoff N 6-8 weeks before harvest 
to allow sugar accumulation (late N reduces sweetness). All P-K pre-plant, though K split option: 70% 
pre-plant + 30% at fruit set maintains availability during critical sugar accumulation phase.

POTASSIUM-SUGAR: K absolutely critical for watermelon quality. Inadequate K: low Brix (<10°), pale flesh, 
hollow heart, poor firmness. High CEC ensures K availability during 4-6 week fruit maturation/sugar 
accumulation period (final growth phase). Tissue testing at early fruit set: >3.5% K in recent mature 
leaves indicates adequacy.

CALCIUM-QUALITY: Adequate Ca reduces hollow heart disorder (internal cavity). High-retention soils usually 
adequate Ca but monitor if extreme K applications (Ca competes with K uptake). Gypsum side-dress at fruit 
set supplements if needed.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
watermelon's K-intensive requirements. Standard practices: split N (30-40% pre-plant, 30-40% vine growth, 
20-30% fruit set), total 150-180 lb N/ac. P-K pre-plant: 80-110 lb P₂O₅, 200-260 lb K₂O for 30-40 tons/ac.

MANAGEMENT STRATEGY: Three-split N program with careful timing. Cutoff N applications 6 weeks before 
anticipated harvest allows sugar accumulation without late vegetative growth. K split application beneficial 
in high-yielding situations: 70% pre-plant + 30% at fruit set ensures availability during critical sugar 
accumulation phase.

IRRIGATION-NUTRITION: Most watermelons irrigated. In good-retention soils, manage irrigation timing with 
nutrition in mind. Avoid heavy irrigation late season - can leach residual nutrients back into root zone, 
promoting late vegetative growth, reducing sugar content. Moderate irrigation during fruit maturation 
maintains plant health while allowing proper sugar concentration.

VARIETY CONSIDERATIONS: Large seeded types (25-35 lb), seedless types (15-25 lb), icebox types (10-15 lb), 
mini types (5-8 lb) all well-adapted to good-retention soils. Seedless varieties particularly K-sensitive 
- require consistent high K availability for proper sizing and sugar development.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC manageable for watermelons 
with careful K management. Four-split N program: pre-plant (25-30%), early vine growth (25-30%), mid-vine 
growth (25-30%), fruit set (15-20%), total 150-180 lb N/ac. K split essential: 60% pre-plant + 40% at 
fruit set compensates for moderate retention during critical sugar accumulation.

MANAGEMENT STRATEGY: More frequent applications or fertigation beneficial. Weekly drip injections during 
fruit development and maturation: 10-15 lb N/ac, 15-25 lb K₂O/ac. Plastic mulch + drip combination standard 
for moderate-retention watermelon production - improves water/nutrient efficiency, warms soil, reduces 
disease pressure.

QUALITY IMPACTS: Expect slightly lower sugar content (10-11° Brix vs 12-13° in high-retention), smaller 
average fruit size (15-25 lb vs 20-30 lb), increased hollow heart incidence. Still commercially acceptable 
with intensive K management. Icebox varieties (10-15 lb) particularly well-adapted to moderate-retention 
soils - lower total K demand, earlier maturity.

SOIL TEXTURE: Moderate-retention watermelon soils typically sandy loam - actually preferred watermelon 
texture (good drainage, warm quickly, easy handling at harvest). Moderate CEC adequate IF K management 
intensive.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes watermelon production 
challenging. Watermelons' high K requirement for quality (200-280 lb K₂O/ac) combined with low retention 
creates significant loss risk. Drip fertigation highly recommended - weekly injections 15-20 lb N/ac, 
25-35 lb K₂O/ac from vine growth through fruit maturation (typically 10-12 weeks).

MANAGEMENT STRATEGY: Plastic mulch + drip + fertigation standard commercial system for low-retention 
watermelon production. Daily irrigation with twice-weekly nutrient injections maintains constant availability 
despite poor soil storage. Tissue testing every 2 weeks during fruit development monitors K status - 
adjust injection rates to maintain >3.5% K in tissue.

QUALITY CHALLENGES: 1) Lower sugar content (9-11° Brix) despite intensive K management. 2) Smaller fruit 
(12-20 lb average vs 20-30 lb). 3) Hollow heart common (Ca/K imbalance). 4) Thicker rind (stress response), 
less flesh. 5) Pale flesh color. 6) Shorter shelf life. Still marketable but quality reduced vs high-
retention production.

VARIETY SELECTION: Icebox types (10-15 lb) better adapted than large types (25+ lb) - lower total nutrient 
demand, shorter season (80-90 days vs 95-105 days), more reliable quality under stress. Seeded types more 
reliable than seedless (seedless very K-sensitive).

VIABILITY: Watermelons viable for 20-30 tons/ac with drip fertigation system. Economics marginal for 
wholesale markets (high input costs, moderate quality) but acceptable for direct-to-consumer sales with 
premium prices.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes quality watermelon production 
extremely difficult. However, watermelons SOMEWHAT VIABLE where many vegetables fail - deep tap roots (3-4 ft) 
and moderate drought tolerance provide advantages in very sandy soils.

MANAGEMENT OPTIONS: Intensive drip fertigation mandatory. Twice-weekly to three-times-weekly injections: 
10-15 lb N/ac, 20-30 lb K₂O/ac per injection from vine growth through fruit maturation (20-25 injections 
total). Daily irrigation with nutrient injections synchronizes water/nutrient availability. Plastic mulch 
+ drip system essential.

ROOT ADVANTAGE: Watermelon tap roots penetrate 3-4 ft with extensive lateral spread (6-8 ft). Deeper than 
most vegetables (tomatoes 18-24 inches, peppers 12-18 inches). This depth allows watermelons to intercept 
nutrients that leached beyond shallow-rooted crop reach. Effectively increases retention from plant 
perspective.

QUALITY LIMITATIONS: Even with best management, quality problems: low Brix (8-10° vs 12-13° target), small 
fruit (8-15 lb), very thick rind (stress response), pale flesh, hollow heart frequent, poor shelf life. 
Marketable but lower grade - roadside stand quality vs premium grocery quality.

VARIETY SELECTION: Small icebox types (8-12 lb) only viable option. Short-season seeded varieties. Yellow-
flesh types sometimes perform better than red-flesh in very sandy soils (yellow types slightly more stress-
tolerant, though market more limited).

VIABILITY: Watermelons marginally viable for 12-20 tons/ac with intensive fertigation. Economics depend 
heavily on marketing channel - direct sales at farm stand/farmers market with premium prices possibly 
viable. Wholesale marketing generally not economically viable due to quality issues and high production 
costs. Among vegetables, watermelons one of better choices for very-low-retention soils due to deep roots 
and moderate drought tolerance."""
    },

    "Cantaloupe": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through cantaloupe's 80-90 day season and HEAVY nutrient requirements. Cantaloupes: 100-150 lb N, 80-100 lb 
P₂O₅, 150-200 lb K₂O for 900+ cartons/ac (25+ tons/ac). High K requirement critical for sugar content 
(12-14° Brix target), aromatic compounds, firm flesh, and netting development.

MANAGEMENT STRATEGY: Split N through growth phases: 35-40% pre-plant (40-60 lb N/ac), 35-40% vine growth 
weeks 3-4 (40-55 lb N/ac), 20-25% fruit set/early sizing week 5-6 (25-40 lb N/ac). Cutoff N 4-5 weeks 
before harvest to allow sugar concentration (late N reduces Brix, delays maturity, promotes soft fruit). 
All P-K pre-plant or K split: 70% pre-plant + 30% at fruit set.

POTASSIUM-QUALITY: K absolutely critical for cantaloupe quality. Adequate K: high Brix (12-14°), aromatic 
esters (melon flavor/aroma), firm flesh (shipping quality), proper netting (visual quality). Inadequate K: 
low Brix (<10°), poor aroma, soft flesh, smooth skin (poor netting). High retention ensures K through 
3-4 week fruit maturation period.

CALCIUM-FIRMNESS: Adequate Ca critical for flesh firmness and shelf life. High Ca improves cell wall 
structure, reduces post-harvest softening, extends shelf life 3-5 days (critical for shipping melons). 
High-retention soils usually adequate Ca.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
cantaloupe's K-intensive requirements. Standard practices: split N (35-40% pre-plant, 35-40% vine growth, 
20-25% fruit set), total 100-140 lb N/ac. P-K pre-plant: 80-100 lb P₂O₅, 150-180 lb K₂O for 650-900 
cartons/ac.

MANAGEMENT STRATEGY: Three-split N program with precise timing. Cutoff N applications 4-5 weeks before 
harvest critical - late N reduces sugar accumulation, delays slip (vine separation at maturity), produces 
soft fruit with poor shelf life. K split beneficial: 70% pre-plant + 30% at fruit set maintains availability 
during sugar accumulation phase.

NETTING-QUALITY: Proper netting (mesh pattern on rind) indicates maturity and quality. Good nutrition 
(especially adequate K, Ca, B) produces uniform well-developed netting. Inadequate nutrition: smooth skin 
or irregular netting, visual quality defects. B (0.5-1.0 lb B/ac) specifically important for netting 
development.

HARVEST-QUALITY: Cantaloupes harvest at "full slip" (vine separates cleanly from fruit when mature). Good 
nutrition produces uniform maturity allowing efficient harvest, high pack-out percentage. Poor nutrition: 
variable maturity requiring multiple harvests, lower pack-out (over/under-mature fruit).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC requires careful K management 
for quality melons. Four-split N: pre-plant (30%), early vine growth (25-30%), mid-vine growth (25-30%), 
fruit set (15-20%), total 100-140 lb N/ac. K split essential: 60% pre-plant + 40% at fruit set.

MANAGEMENT STRATEGY: Fertigation highly beneficial - weekly injections 10-15 lb N/ac, 15-20 lb K₂O/ac 
during vine growth and fruit development. Plastic mulch + drip system standard for moderate-retention 
cantaloupe production. Improves water/nutrient efficiency, warms soil (cantaloupes heat-loving), reduces 
Fusarium wilt pressure.

QUALITY IMPACTS: Expect slightly lower Brix (10-12° vs 12-14°), smaller fruit (2-3 lb vs 3-5 lb), less 
aromatic, softer flesh, variable netting quality. Still commercially acceptable with intensive K management. 
Eastern types (smaller, 2-3 lb) better adapted to moderate retention than large Western shipping types 
(4-5 lb).

DISEASE PRESSURE: Fusarium wilt (Fusarium oxysporum f.sp. melonis) severe in moderate-retention sandy 
soils, especially when stressed. Use resistant varieties (many modern hybrids resistant to races 0, 1, 2). 
Good nutrition improves disease resistance - adequate K particularly important.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes quality cantaloupe production 
challenging. Cantaloupes' high K requirement for quality combined with low retention creates significant 
challenges. Drip fertigation mandatory - weekly injections 12-18 lb N/ac, 18-25 lb K₂O/ac from vine growth 
through fruit maturation (8-10 weeks).

MANAGEMENT STRATEGY: Plastic mulch + drip + fertigation standard. Daily irrigation with weekly or twice-
weekly nutrient injections. Tissue testing every 2 weeks monitors K status - maintain >3.5% K. Foliar K 
applications (potassium nitrate sprays) supplement soil K during fruit sizing.

QUALITY CHALLENGES: 1) Lower Brix (9-11° vs 12-14° target) - reduced sweetness. 2) Poor aroma (aromatic 
ester production requires adequate K). 3) Soft flesh (poor Ca/K nutrition). 4) Irregular or poor netting. 
5) Variable maturity (inconsistent nutrition across field). 6) Short shelf life (2-3 days vs 7-10 days). 
Still marketable for local/regional markets but not shipping quality.

DISEASE PRESSURE: Fusarium wilt extremely severe in sandy low-retention soils, especially under stress. 
Resistant varieties absolutely mandatory. Root-knot nematodes also problematic in sandy soils, further 
stressing plants. Consider grafted plants (cantaloupe scion on resistant rootstock) for low-retention 
situations - improves disease resistance and vigor.

VIABILITY: Cantaloupes marginally viable for 450-650 cartons/ac with intensive drip fertigation. Economics 
marginal for wholesale due to quality issues and high input costs. More viable for farmers markets/roadside 
stands where quality expectations moderate and prices premium.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes quality cantaloupe production 
extremely difficult to non-viable. Cantaloupes' combination of high K demands, moderate season length 
(80-90 days), and quality requirements challenging in very-low-retention soils.

MANAGEMENT OPTIONS: Only approach with any viability: intensive raised-bed plasticulture with twice-weekly 
fertigation. Raised beds (6-8 inches) with compost, plastic mulch, drip tape, injections 10-15 lb N/ac + 
18-25 lb K₂O/ac twice weekly (16-20 injections total). Foliar K-Ca applications weekly during fruit 
development. Grafted plants on vigorous disease-resistant rootstocks.

QUALITY CRISIS: Even with intensive management, quality severe problems: very low Brix (7-10° barely 
acceptable), minimal aroma, very soft flesh (ships poorly or not at all), poor or absent netting, extremely 
variable maturity, very short shelf life (1-2 days). Not suitable for any wholesale market. Marginal even 
for direct-to-consumer sales - consumer expectations for cantaloupe quality (sweetness, aroma) difficult 
to meet.

DISEASE DEVASTATION: Fusarium wilt, root-knot nematodes, and other soilborne diseases catastrophic in 
very-low-retention soils. Even resistant varieties struggle under severe stress. Grafting essential but 
expensive ($0.50-1.00/plant vs $0.10-0.20/plant for seed). Crop rotation ineffective in very sandy soils 
(pathogens persist).

VIABILITY: Cantaloupe production not recommended in very-low-retention soils. Technical barriers (quality, 
disease) and economic barriers (high costs, low quality, limited markets) make success unlikely. If 
attempting: small scale only (<1 acre), grafted plants, intensive raised beds, direct marketing only, 
manage customer expectations (melons will be "good" not "excellent").

ALTERNATIVES: Watermelons significantly better adapted to very-low-retention soils than cantaloupes. 
Watermelon deeper roots, more stress-tolerant, less disease-prone, lower quality threshold. If growing 
melon in very sandy soil, choose watermelon over cantaloupe."""
    },

    "Snap Beans": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through snap bean's short season (50-65 days) and MODERATE nutrient requirements. Snap beans unusual: 
legume with N-fixing capability BUT limited fixation compared to soybeans/dry beans. Requirements: 50-80 lb 
N (including fixation), 60-80 lb P₂O₅, 80-100 lb K₂O for 7+ tons/ac. High retention supports good nodulation 
and pod production.

MANAGEMENT STRATEGY: Minimal starter N (20-30 lb N/ac) at planting assists establishment before nodulation 
begins (10-14 days). Then rely on N fixation (snap beans fix 30-60 lb N/ac, about 50% of need - less than 
soybeans 70-90%). All P-K pre-plant: adequate P critical for nodulation and early pod set. High retention 
holds P-K through short season despite rapid growth.

NODULATION CONSIDERATIONS: Snap beans have MODERATE N-fixing ability (better than common garden beans, 
less than soybeans/dry beans). High-retention soils with good structure, adequate Ca, pH 6.0-7.0 support 
good nodulation. Inoculate if beans not grown recently (3+ years). Successful nodulation: small pink 
nodules on upper lateral roots visible by flowering.

POTASSIUM-QUALITY: K critical for pod quality - tender, straight, good color, crisp texture. Adequate K 
(80-100 lb K₂O/ac) reduces fiber content (tough pods), improves green color, enhances crispness. High 
retention maintains K during critical 3-4 week harvest period.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
snap bean requirements. Standard practices: starter N 20-30 lb N/ac at planting, rely on fixation for 
remainder. P-K pre-plant: 60-80 lb P₂O₅, 80-100 lb K₂O for 5-7 tons/ac.

MANAGEMENT STRATEGY: Light starter N at planting (beans sensitive to excess N which suppresses nodulation). 
Inoculate seed with Rhizobium phaseoli if beans new to field. P banded at planting improves early nodulation 
and pod set. K broadcast pre-plant adequate through short season in good-retention soils.

HARVEST CONSIDERATIONS: Snap beans typically 2-4 harvests for hand-pick, single harvest for mechanical. 
Good nutrition produces uniform maturity (concentrates harvest, improves efficiency), consistent pod size, 
good quality through harvest window. Inadequate K: progressive quality decline with later harvests (first 
harvest good, later harvests tough and fibrous).

VARIETY TYPES: Bush types (45-55 days, determinate growth) and pole types (55-65 days, indeterminate 
growth) both respond well to good retention. Bush types for processing (single mechanical harvest). Pole 
types for fresh market (extended harvest, multiple picks). Good-retention soils support both types well.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for snap beans with 
proper management. Snap beans relatively WELL-ADAPTED to moderate-retention soils - short season (50-65 
days), moderate total demand, N-fixing ability all favorable. Starter N 20-30 lb N/ac, P banded 60-80 lb 
P₂O₅, K broadcast or split 80-100 lb K₂O.

MANAGEMENT STRATEGY: P banding essential in moderate-retention soils - ensures early availability for 
nodulation and root development. K split optional: 60-70 lb K₂O/ac pre-plant + 20-30 lb K₂O/ac at early 
flowering if concerned about losses. Snap beans' short season advantage: limited time window for nutrient 
losses even in moderate-retention soils.

NODULATION CHALLENGES: Moderate-retention soils often slightly acidic (pH 5.5-6.0) - can limit nodulation. 
Lime to pH 6.0-6.5 improves nodulation success. If pH cannot be raised, apply moderate supplemental N 
(total 50-70 lb N/ac split: 30 lb at planting + 25-40 lb at flowering) to compensate for poor fixation. 
Inoculation mandatory.

POD QUALITY: Expect good quality with proper K management. Moderate-retention soils can produce tender, 
good-color pods. Key: adequate K through harvest window. Tissue testing at early flowering: >2.0% K 
indicates adequacy. If <2.0%, side-dress K (25-35 lb K₂O/ac) immediately.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but snap beans STILL VIABLE - 
better adapted than most vegetables to low-retention soils. Advantages: short season (50-65 days reduces 
loss exposure), N-fixing reduces fertilizer needs, moderate total demand. Starter N 30-40 lb N/ac, P 
banded 60-80 lb P₂O₅, K split 60 lb K₂O pre-plant + 30 lb K₂O flowering.

MANAGEMENT STRATEGY: Split K application compensates for low retention. P banding absolutely critical - 
low-retention soils typically sandy with high P-fixation capacity, broadcast P largely unavailable. Side-
dress N at flowering (30-40 lb N/ac) compensates for likely poor nodulation in low-retention acidic soils.

NODULATION LIMITATIONS: Low-retention soils typically acidic (pH 5.0-6.0), low Ca - both inhibit snap 
bean nodulation severely. Even with inoculation, expect <40% nodulation success. Therefore, must supplement 
with fertilizer N (total 70-80 lb N/ac: 30-40 lb planting + 30-40 lb flowering). This reduces snap beans' 
economic advantage (N-fixing) but still viable.

POD QUALITY MANAGEMENT: Low-retention soils produce acceptable quality IF K adequate. Challenge: maintaining 
K through harvest in low-retention conditions. Split K application plus foliar K sprays (potassium sulfate, 
5 lb K₂O/100 gal, 2-3 applications during flowering/harvest) maintain pod quality.

VIABILITY: Snap beans viable for 3-5 tons/ac in low-retention soils - among best vegetable choices for 
challenging conditions. Short season, moderate inputs, acceptable quality. Economics better than most 
vegetables at low retention. Consider bush beans (single harvest) over pole beans (extended harvest more 
challenging in low-retention soils).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but snap beans STILL AMONG BEST 
vegetable options for very-low-retention soils. Snap beans' short season (50-60 days), moderate demands, 
and tolerance to stress make them viable where most vegetables fail.

MANAGEMENT OPTIONS: Bush beans only (pole beans too demanding for extended harvest). Intensive split 
applications: starter N 30 lb/ac + flowering N 30 lb/ac + early pod N 20 lb/ac, total 80 lb N/ac (assume 
minimal fixation). P banded 60-80 lb P₂O₅. K split: 50 lb pre-plant + 30 lb flowering + 20 lb early pod, 
total 100 lb K₂O. Fertigation through sprinkler beneficial if available: biweekly injections 15-20 lb N/ac, 
15-20 lb K₂O/ac.

NODULATION FAILURE: Very-low-retention soils almost always extremely acidic (pH 4.5-5.5) and Ca-deficient. 
Snap bean nodulation essentially zero even with inoculation. Must rely entirely on fertilizer N. Apply 
lime if possible (2-3 tons/ac to reach pH 6.0) for future crops, but current crop needs fertilizer N.

SHORT-SEASON ADVANTAGE: Snap beans' 50-60 day season critical advantage in very-low-retention soils. 
Exposure window for nutrient losses 50-60% shorter than tomatoes (120 days), peppers (140 days), or winter 
squash (100 days). This makes snap beans economically viable where longer-season vegetables impossible.

POD QUALITY: Acceptable quality achievable with intensive K management. Pods may be slightly tough/fibrous 
compared to high-retention production but still marketable. Processing beans (canning/freezing) more 
forgiving of quality variations than fresh market.

VIABILITY: Snap beans viable for 2-4 tons/ac in very-low-retention soils with intensive split fertilization. 
Among TOP vegetable choices for very sandy conditions. Economics reasonable - moderate input costs (short 
season), acceptable yields, multiple market channels (fresh, processing, pick-your-own). If growing 
vegetable in very-low-retention soil, snap beans should be on short list of candidates."""
    },

    "Peas": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through pea's short cool season (60-70 days) and MODERATE nutrient requirements. Peas: 40-60 lb N (including 
fixation), 60-80 lb P₂O₅, 60-80 lb K₂O for 2-3 tons shelling peas or 5-6 tons snap peas. High retention 
supports good nodulation despite cool soil conditions.

MANAGEMENT STRATEGY: Minimal starter N (15-25 lb N/ac) at planting - peas excellent N-fixers (better than 
snap beans) fixing 60-80 lb N/ac or 70-90% of needs. All P-K pre-plant: adequate P essential for cool-soil 
nodulation (peas establish in 40-50°F soil). High retention maintains nutrients through rapid spring growth 
period.

COOL-SEASON ADVANTAGE: Peas unique among vegetables - thrive in cool conditions (optimal growth 55-65°F, 
tolerate frost). Plant early spring (or fall in mild climates). Cool conditions slow nutrient mineralization 
BUT high retention compensates - stored nutrients released slowly but steadily. Advantage over warm-season 
crops requiring rapid mineralization.

NODULATION-PHOSPHORUS: P absolutely critical for pea nodulation in cool soils. Adequate P (60-80 lb P₂O₅/ac 
banded) ensures nodulation success at 45-55°F soil temps. Peas form LARGE nodules (pea-sized, hence name) 
on upper tap root. Check nodulation at flowering - healthy nodules pink/red inside. High-retention soils 
with good Ca (pH 6.0-7.0) promote excellent nodulation.

HARVEST-QUALITY: Peas harvested young (shelling peas 60-65 days, snap/snow peas 55-60 days) for tender 
texture and sweet flavor. Good nutrition produces uniform maturity, tender pods, sweet peas. Inadequate K: 
tough pods, starchy peas (low sugar), poor flavor.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
pea requirements. Standard practices: minimal starter N 15-25 lb N/ac, rely on fixation for remainder. 
P-K pre-plant: 60-80 lb P₂O₅ (CRITICAL), 60-80 lb K₂O for 1.5-2.5 tons shelling or 4-5 tons snap peas.

MANAGEMENT STRATEGY: P banded at planting most critical input - ensures cool-soil availability for early 
nodulation. Peas planted when soil 40-50°F (March-April in most regions) - cold temperatures reduce P 
availability. Banding overcomes temperature limitations. Inoculate seed with Rhizobium leguminosarum if 
peas not grown recently (3+ years).

VARIETY CONSIDERATIONS: Multiple types with different retention sensitivity. 1) Shelling peas (English 
peas): moderate retention adequate, harvest dry peas from pods. 2) Snap peas (edible pods, full peas): 
prefer good retention for tender pods plus sweet peas. 3) Snow peas (flat pods, tiny peas): most tolerant 
to moderate retention, pods dominant component. All types viable in good-retention soils.

DISEASE MANAGEMENT: Pea root rots (Aphanomyces, Fusarium) severe in poorly-drained or compacted soils. 
High-retention soils with good structure resist root rots. Good nutrition (adequate P for roots, balanced 
K-Ca) improves disease resistance. Crop rotation essential (3+ year break from peas/lentils).

HARVEST TIMING: Peas extremely time-sensitive - harvest window 3-7 days for peak quality. Early: pods 
flat, peas tiny. Peak: pods full, peas sweet and tender. Late: peas starchy, tough, pod strings develop. 
Good nutrition produces uniform maturity concentrating harvest at peak quality.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC generally ADEQUATE for peas - 
surprisingly well-adapted to moderate retention. Factors: short season (60-70 days), cool conditions (slow 
mineralization AND slow leaching), excellent N-fixing (60-80 lb N/ac), moderate total demands. Starter N 
15-25 lb N/ac, P banded 60-80 lb P₂O₅ (ESSENTIAL), K broadcast 60-80 lb K₂O.

MANAGEMENT STRATEGY: P banding absolutely critical in moderate-retention soils - direct contact with roots 
ensures availability in cool soil. K broadcast adequate for short season - limited loss exposure. If soil 
acidic (pH <6.0), lime before planting or apply supplemental N (total 40-60 lb N/ac: 20-25 at planting + 
20-35 at flowering) to compensate for poor nodulation.

COOL-SOIL ADVANTAGE: Peas' cool-season growth pattern ADVANTAGE in moderate-retention soils. Planted March-
April when soil 40-50°F. Cool temperatures mean: 1) Slow nutrient mineralization (less competition from 
flush). 2) Slow leaching rates (limited water movement). 3) Slow crop growth initially (gradual nutrient 
demand). Together these factors allow moderate-retention soils to support peas better than many vegetables.

NODULATION SUCCESS: Moderate-retention soils often slightly acidic (pH 5.5-6.5). If pH >6.0, inoculation 
alone adequate for good nodulation. If pH 5.5-6.0, marginal - inoculation + supplemental N (20-35 lb at 
flowering). If pH <5.5, poor nodulation - apply full supplemental N (40-60 lb N/ac split).

VARIETY SELECTION: Snow peas most forgiving of moderate retention (pods main component, pea development 
less critical). Snap peas intermediate. Shelling peas most demanding (pea quality critical). For moderate 
retention, favor snow or snap over shelling types.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but peas VIABLE - better adapted 
than most vegetables to low-retention conditions. Cool-season advantage: peas grow in cold soil (March-
April) when leaching rates low, mineralization slow, disease pressure minimal. Starter N 20-30 lb N/ac, P 
banded 60-80 lb P₂O₅, K split 50 lb pre-plant + 20-30 lb flowering.

MANAGEMENT STRATEGY: Split K compensates for low retention during critical pod-fill/pea-development period. 
P banding mandatory - low-retention soils typically sandy with high P-fixation. Side-dress N at flowering 
(30-40 lb N/ac) compensates for likely poor nodulation in low-retention acidic soils (pH 5.0-6.0 typical).

NODULATION CHALLENGES: Low-retention soils typically acidic, low-Ca - both severely inhibit pea nodulation. 
Even with inoculation, expect <50% nodulation success. Must supplement with fertilizer N (total 60-80 lb 
N/ac: 20-30 planting + 30-40 flowering + 10-20 at pod set if needed). This reduces economic advantage but 
peas still viable due to short season and moderate total demand.

DISEASE PRESSURE: Pea root rots less severe in low-retention (sandy, well-drained) soils than high-retention 
(clayey, poorly-drained) soils. This is ADVANTAGE for peas in sandy conditions - while nutrition challenging, 
disease management easier. Well-drained sandy soils inhibit Aphanomyces and Fusarium root rots.

POD-PEA QUALITY: Low retention can produce good quality with proper K management. Key: adequate K during 
3-4 week harvest period. Tissue testing at early flowering: >2.5% K adequate. If lower, side-dress K 
immediately (20-30 lb K₂O/ac). Snow peas most successful (pods main component). Snap peas intermediate. 
Shelling peas most challenging (pea quality critical).

VIABILITY: Peas viable for 1-2 tons shelling or 3-4 tons snap/snow in low-retention soils. Among better 
vegetable options for low-retention conditions. Short season (60-70 days), cool growth period (low leaching), 
moderate inputs all favorable. Consider peas strong candidate for low-retention vegetable production.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but peas STILL VIABLE option - 
surprising resilience in very-low-retention soils. Peas' cool-season ecology provides unique advantages: 
grow in 40-50°F soil when chemical/biological activity minimal, short season (60-70 days), moderate demands, 
N-fixing reduces fertilizer needs.

MANAGEMENT OPTIONS: Intensive split applications: starter N 25 lb/ac + flowering N 30 lb/ac + pod-set N 
20 lb/ac, total 75 lb N/ac (assume minimal fixation). P banded 60-80 lb P₂O₅ essential. K split: 40 lb 
pre-plant + 25 lb flowering + 15 lb pod-set, total 80 lb K₂O. Three splits compensate for very low retention 
during rapid late-season growth (flowering through harvest: weeks 5-8).

NODULATION FAILURE: Very-low-retention soils almost always extremely acidic (pH 4.5-5.5) and Ca-deficient. 
Pea nodulation essentially zero even with inoculation. Must rely on fertilizer N. Lime application (2-3 
tons/ac to pH 6.0) beneficial for future crops but current crop needs supplemental N.

COOL-SEASON WINDOW: Peas' growth period (March-May in most regions) coincides with lowest leaching rates 
(cool temperatures, moderate rainfall, low ET). This is MAJOR advantage over summer vegetables. Spring 
conditions in very sandy soils favorable: adequate moisture, minimal leaching, low disease pressure. Peas 
exploit this window effectively.

DRAINAGE ADVANTAGE: Very-low-retention soils almost always extremely well-drained (sandy). This is 
ADVANTAGE for peas - root rots (Aphanomyces, Fusarium) minimal in well-drained conditions. While nutrition 
challenging, disease management easy. Root rots devastate peas in poorly-drained high-retention clays but 
absent from well-drained sands.

VARIETY-QUALITY: Snow peas most successful in very-low-retention (pods main component, less demanding than 
shelling types). Acceptable pod quality achievable with intensive K splits. Snap peas intermediate - possible 
but quality variable. Shelling peas least successful (pea development/quality challenging, better options 
available).

VIABILITY: Peas viable for 1-1.5 tons shelling or 2-3 tons snow/snap in very-low-retention soils with 
intensive management. Among TOP vegetable choices for very sandy conditions - cool season ecology provides 
major advantages. Economics reasonable for direct marketing (farmers markets, roadside stands, pick-your-
own). Processing peas (canning, freezing) less viable due to quality variability. If growing vegetables in 
very-low-retention soil, peas should be considered alongside snap beans as best options."""
    },

    "Sweet Corn": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through sweet corn's moderate season (75-90 days) and HEAVY nutrient requirements. Sweet corn: 140-180 lb 
N, 80-100 lb P₂O₅, 120-160 lb K₂O for 10-12+ tons/ac (1,000+ dozen ears). High retention critical for 
sweet corn's rapid growth phase and intensive nutrient demand period.

MANAGEMENT STRATEGY: Split N through growth stages: 35-40% pre-plant (50-70 lb N/ac), 35-40% at 12-18 
inches (V6-V8 stage, 50-70 lb N/ac), 20-25% at tasseling/silking (30-45 lb N/ac). Three splits match corn's 
demand pattern and minimize losses. All P-K pre-plant or K split: 70% pre-plant + 30% at V6-V8.

RAPID-GROWTH DEMANDS: Sweet corn extremely rapid growth weeks 4-8 (V6-V8 through tasseling): 1.5-2.5 
inches/day, 8-12 leaves every 7-10 days, massive biomass accumulation. This period accounts for 60-70% of 
total N-P-K uptake despite being only 30% of growing season. High retention ensures availability during 
this critical window.

POLLINATION-KERNEL FILL: Adequate N through tasseling essential for ear size (14-18 rows, 500-700 kernels/
ear). Adequate K during kernel fill (2-3 weeks post-pollination) critical for sugar content and tender 
texture. High retention maintains K through fill period preventing tough/starchy kernels.

QUALITY FACTORS: Sweet corn quality determined by: 1) Ear size (8-9 inch minimum, diameter >1.5 inches). 
2) Kernel fill (complete to tip - 85-95% fill). 3) Sweetness (12-16% sugar, variety-dependent). 4) 
Tenderness (adequate water + K). High retention supports all quality factors.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
sweet corn's heavy demands. Standard practices: split N (35-40% pre-plant, 35-40% V6-V8, 20-25% tassel), 
total 140-180 lb N/ac. P-K: 80-100 lb P₂O₅, 120-160 lb K₂O for 8-10 tons/ac.

MANAGEMENT STRATEGY: Three-split N program essential - sweet corn's rapid growth means large uptake over 
short period (4-5 weeks). Late N application (at tassel/silk) particularly important for kernel fill and 
quality. K split beneficial: 70% pre-plant + 30% at V6-V8 maintains availability during ear development.

VARIETY CONSIDERATIONS: Three types with different retention sensitivity. 1) Standard sugary (su): moderate 
sugar (12-14%), moderate retention adequate, traditional sweet corn flavor. 2) Sugar-enhanced (se): higher 
sugar (16-18%), better retention preferred for quality, tender longer. 3) Supersweet (sh2): highest sugar 
(20-24%), most demanding - requires good retention for quality and yield. All types viable in good-retention 
soils.

IRRIGATION-NUTRITION: Sweet corn sensitive to water stress particularly during pollination (tassel-to-silk) 
and kernel fill (2-3 weeks post). Water stress during pollination: poor kernel set, gaps, unfilled tips. 
Water stress during fill: tough starchy kernels, low sugar. Irrigation + good nutrition synergistic for 
quality.

HARVEST TIMING: Sweet corn quality extremely time-sensitive. Peak harvest: 18-22 days post-silking (milk 
stage, kernels release milky fluid when pressed). Quality declines rapidly: sugar converts to starch 6-8 
hours after harvest (standard su types), slower in se/sh2 types. Uniform good nutrition concentrates 
maturity, maximizes peak-quality harvest window.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for sweet corn's 
heavy demands but manageable with intensive splits. Four-split N: pre-plant (30%), V4-V6 (25-30%), V10-V12 
(25-30%), tassel/silk (15-20%), total 140-180 lb N/ac. K split: 60% pre-plant + 40% at V6-V8.

MANAGEMENT STRATEGY: Four-split N compensates for moderate retention during rapid-growth period. Early 
side-dress (V4-V6 vs V6-V8) ensures availability before demand peak. Second side-dress (V10-V12, just 
before tasseling) critical for ear size and kernel number. Final application (tassel/silk) supports kernel 
fill and quality.

FERTIGATION OPTION: Overhead sprinkler fertigation highly beneficial for moderate-retention sweet corn. 
Weekly injections 15-20 lb N/ac, 15-20 lb K₂O/ac during rapid growth (weeks 4-9) maintains constant supply. 
Prevents deficiency during peak demand while avoiding excess early (which can leach).

QUALITY IMPACTS: Moderate retention produces acceptable quality with intensive management. Expect: slightly 
smaller ears (7-8 inches vs 8-9 inches), fewer kernel rows (12-16 vs 14-18), possible tip-fill issues 
(kernel set 75-85% vs 85-95%), slightly lower sweetness. Still commercially acceptable, especially for 
fresh-market direct sales.

VARIETY SELECTION: Standard sugary (su) types most forgiving of moderate retention - moderate sugar goals, 
traditional vigor. Sugar-enhanced (se) possible but quality variable. Supersweet (sh2) not recommended for 
moderate retention - extremely demanding, quality unreliable, gaps/tip-fill issues common.

VIABILITY: Sweet corn viable for 6-8 tons/ac with four-split N and intensive K management. Economics 
moderate - high input costs (fertilizer, splits/fertigation) but acceptable yields and quality for fresh 
market. Processing corn (canning, freezing) marginal - quality variability and modest yields challenge 
profitability.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes sweet corn production 
challenging. Sweet corn's combination of heavy demands (140-180 lb N/ac), rapid uptake period (weeks 4-9), 
and high quality requirements difficult in low-retention conditions. Fertigation mandatory - weekly 
injections 15-25 lb N/ac, 18-25 lb K₂O/ac for 8-10 weeks.

MANAGEMENT STRATEGY: Overhead sprinkler or drip fertigation standard for low-retention sweet corn. Weekly 
or twice-weekly nutrient injections match supply to demand, minimize losses. Starter fertilizer at planting 
(30-40 lb N, 80-100 lb P₂O₅ banded) ensures early vigor. Then begin fertigation at V4-V6, continue through 
kernel fill (weeks 3-10).

QUALITY CHALLENGES: Low retention produces quality problems even with intensive management: 1) Small ears 
(6-7 inches common vs 8-9 target). 2) Poor tip fill (kernels 60-75% to tip vs 85-95%). 3) Low kernel 
count (10-14 rows vs 14-18). 4) Reduced sweetness (8-12% sugar vs 12-16%). 5) Tough/starchy texture 
(inadequate K). 6) Variable maturity (inconsistent nutrition). Quality suitable for pick-your-own or farm 
stands but not wholesale.

POLLINATION-FILL: Low retention particularly impacts pollination and kernel fill - most nutrient-sensitive 
growth stages. Poor N availability during tasseling: small ears, few kernel rows. Poor K during fill: 
starchy tough kernels. Tissue testing at V10-V12 (pre-tassel): >3.0% N and >2.0% K minimum. If deficient, 
emergency foliar applications (urea, potassium nitrate) partially compensate.

VARIETY LIMITATIONS: Only standard sugary (su) types viable in low retention - moderate quality targets, 
traditional vigor, moderate demands. Sugar-enhanced (se) marginal - quality inconsistent. Supersweet (sh2) 
not viable - extreme demands, quality failures common.

VIABILITY: Sweet corn marginally viable for 4-6 tons/ac with intensive fertigation. Economics marginal - 
high input costs (fertigation equipment, weekly injections, irrigation) versus modest yields and quality 
issues. More viable for direct marketing (pick-your-own, roadside stands) where quality expectations 
moderate and customer experience valued. Not suitable for wholesale or processing due to quality 
inconsistency.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes sweet corn production extremely 
difficult to non-viable. Sweet corn's heavy demands (140-180 lb N/ac), rapid uptake rates, quality 
sensitivity, and market quality expectations combine to challenge success in very-low-retention soils.

MANAGEMENT OPTIONS: Only approach with any viability: intensive overhead fertigation with twice-weekly 
injections. Starter at planting: 40 lb N, 80-100 lb P₂O₅ banded. Then fertigation: 15-20 lb N/ac + 20-25 
lb K₂O/ac twice weekly from V4 through kernel fill (12-14 injections total). Foliar micronutrients weekly 
(especially Zn for kernel development).

QUALITY CRISIS: Even with intensive management, quality severe problems: very small ears (5-6 inches vs 
8-9 standard), extreme tip-fill issues (40-60% fill vs 85-95%), very low kernel count (8-12 rows vs 14-18), 
low sweetness (6-10% sugar vs 12-16%), extremely tough/starchy texture, highly variable maturity. Quality 
not acceptable for any wholesale market. Marginal even for direct sales - consumer expectations for sweet 
corn (tender, sweet, full ears) difficult or impossible to meet.

POLLINATION FAILURES: Very-low-retention soils + sweet corn's heavy N demands during tasseling = frequent 
pollination failures. Symptoms: poor silk development, incomplete kernel set, barren ears, gaps, nubbin 
ears (mini-ears 2-4 inches). Even with fertigation, timing challenges (nutrient application vs plant demand) 
cause intermittent deficiencies during critical pollination window.

KERNEL-FILL DISASTER: Inadequate K during fill period (2-3 weeks post-pollination) produces extremely 
tough, starchy, nearly inedible kernels. Very-low-retention soils cannot maintain K through fill despite 
intensive fertigation. Result: corn looks acceptable (ears present) but quality terrible (texture, flavor, 
tenderness unacceptable).

VIABILITY: Sweet corn production not recommended in very-low-retention soils. Multiple technical barriers 
(pollination failures, quality crisis, consistency problems) and economic barriers (extreme input costs, 
very low yields, unmarketable quality) make success unlikely. Even for direct marketing, customer 
disappointment (quality far below supermarket standards) damages reputation.

ALTERNATIVES: If considering sweet corn in very sandy soil, STRONGLY reconsider. Nearly all other vegetables 
better adapted to very-low-retention conditions. Better options: snap beans, peas, potatoes, sweet potatoes, 
watermelons. All produce acceptable quality in low retention where sweet corn fails. Sweet corn one of WORST 
vegetable choices for very-low-retention soils."""
    },

    "Spinach": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through spinach's short cool season (40-50 days) and MODERATE nutrient requirements. Spinach: 80-120 lb N, 
60-80 lb P₂O₅, 80-100 lb K₂O for 10-12+ tons/ac fresh weight. High retention supports rapid leaf growth and 
excellent quality.

MANAGEMENT STRATEGY: Split N for extended harvest: 50% pre-plant (40-60 lb N/ac), 50% after first harvest 
(40-60 lb N/ac, supports regrowth). Single-harvest: all N pre-plant. All P-K pre-plant: adequate availability 
for rapid root establishment and leaf development. High retention maintains nutrients through cool-season 
growth.

COOL-SEASON SPECIALTY: Spinach extremely cold-hardy (survives 15-20°F, optimal growth 50-60°F). Plant early 
spring or fall. Cool conditions ideal for spinach: 1) Slow bolting (flowering delayed at <65°F, spinach 
remains vegetative). 2) Tender leaves (cool weather produces soft succulent texture). 3) High quality (deep 
green color, mild sweet flavor). High-retention soils support extended harvest in cool conditions.

NITRATE ACCUMULATION: Spinach naturally accumulates nitrates (NO₃) in leaves - normal and safe at typical 
levels but can be excessive with over-fertilization. High-retention soils with proper N rates produce 
excellent quality without excessive nitrates. Target: <4,000 ppm NO₃ in leaves (typical range 500-3,000 
ppm with proper management).

QUALITY FACTORS: High-quality spinach: dark green color (indicates adequate N + Fe), tender texture (cool 
growth + adequate water), mild sweet flavor (adequate K + cool conditions), thick leaves (adequate Ca-Mg). 
High retention with balanced fertility produces premium spinach.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
spinach requirements. Standard practices: split N for multiple harvest (50% pre-plant + 50% after first 
harvest) or single application for single cut, total 80-120 lb N/ac. P-K pre-plant: 60-80 lb P₂O₅, 80-100 
lb K₂O for 8-10 tons/ac.

MANAGEMENT STRATEGY: P-K broadcast or banded pre-plant adequate in good-retention soils - spinach short 
season and moderate demand. N split beneficial for extended harvest (2-3 cuts over 6-8 weeks) - maintains 
leaf quality and regrowth vigor. Single-harvest spinach (one cut at maturity): all N pre-plant sufficient.

HARVEST SYSTEMS: Two approaches with different retention needs. 1) Baby spinach (1-2 inch leaves, 20-30 
days): single harvest, lower N (60-80 lb/ac), intensive planting (seed broadcast or close rows). 2) Mature 
spinach (4-6 inch leaves, 40-50 days): multiple harvests possible (cut-and-come-again), higher N (100-120 
lb/ac split), wider spacing. Good-retention soils support both systems.

DISEASE MANAGEMENT: Spinach diseases (downy mildew, white rust, anthracnose) favored by wet conditions. 
Good-retention soils with adequate structure and drainage resist disease. Avoid excess N (produces succulent 
disease-prone tissue). Proper N rates + good retention = balanced growth with disease resistance.

BOLTING MANAGEMENT: Spinach bolts (flowers) when days lengthen (>14 hours) and warm (>70°F). Bolting ends 
harvest - leaves bitter, stems tough, plant inedible. Cool-season planting (early spring, fall) and proper 
variety selection (slow-bolt types) delay bolting. Good retention supports rapid growth completing harvest 
before bolting begins.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC generally ADEQUATE for spinach - 
well-adapted to moderate retention. Factors: short season (40-50 days), cool growth (slow leaching), 
moderate demands, rapid maturity. Split N beneficial: 60 lb pre-plant + 40-50 lb after first harvest (if 
multiple cuts) or 80-100 lb pre-plant (single harvest).

MANAGEMENT STRATEGY: Baby spinach particularly well-suited to moderate retention - single harvest, short 
season (20-30 days), lower N (60-80 lb/ac), minimal loss exposure. Mature spinach possible with split N - 
first application at planting, second after first cut to support regrowth.

COOL-SEASON ADVANTAGE: Spinach's cool-season ecology ADVANTAGE in moderate-retention soils (similar to 
peas). Spring planting (March-April) or fall planting (August-September) coincides with cool temperatures: 
slow mineralization, slow leaching, adequate moisture, minimal disease. Moderate retention adequate in cool 
conditions where inadequate in summer heat.

IRRIGATION-QUALITY: Moderate-retention soils (typically sandy loams) require irrigation for quality spinach. 
Spinach 95% water - adequate moisture essential for tender succulent leaves. Water stress: tough fibrous 
leaves, bitter flavor, premature bolting. Drip or overhead irrigation maintains quality in moderate-retention 
soils.

NITRATE MANAGEMENT: Moderate-retention soils with split N less prone to excessive nitrate accumulation than 
high-retention soils with excessive N. Natural leaching in moderate retention maintains nitrates at safe 
levels (<4,000 ppm) with proper N rates.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but spinach VIABLE - well-adapted 
to low-retention conditions. Advantages: short season (40-50 days baby, 50-60 mature), cool growth (minimal 
leaching), moderate demands, rapid maturity. Baby spinach particularly successful: 20-30 days, 60-80 lb 
N/ac, single harvest.

MANAGEMENT STRATEGY: Baby spinach (20-30 days): single N application 60-80 lb/ac pre-plant, short season 
prevents significant losses even in low retention. Mature spinach (40-60 days): split N essential - 50-60 
lb pre-plant + 40-50 lb at 3-4 weeks (before first harvest), total 90-110 lb N/ac. P banded 60-80 lb P₂O₅. 
K split: 60 lb pre-plant + 30 lb at 3-4 weeks.

COOL-SEASON WINDOW: Spinach's spring/fall growth windows MAJOR advantage in low-retention soils. Cool 
temperatures (April-May, September-October) mean low leaching rates, adequate moisture, slow mineralization. 
Low retention adequate in these conditions. Summer spinach not viable in low-retention soils (heat + poor 
retention = quality crisis).

QUALITY CONSIDERATIONS: Low retention produces acceptable quality with proper management. Baby spinach 
slightly thinner leaves but tender and flavorful. Mature spinach good quality if K adequate - tissue testing 
at 3-4 weeks: >3.5% K indicates adequacy. If low, side-dress K immediately.

SALINITY TOLERANCE: Spinach moderately salt-tolerant (threshold EC 2.0 dS/m, 50% yield reduction at 5.3 
dS/m). This is ADVANTAGE in low-retention sandy soils where salt accumulation minimal due to natural 
leaching. Spinach tolerates sandy soil conditions better than most leafy greens.

VIABILITY: Spinach viable for 8-10 tons/ac mature or 6-8 tons baby in low-retention soils. Among best 
leafy greens for low-retention conditions. Economics good for baby spinach (high value, short season, 
single harvest). Mature spinach moderate economics (multiple harvests increase labor but also yield).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but spinach STILL VIABLE - 
particularly baby spinach. Baby spinach 20-30 day season provides major advantage in very-low-retention 
soils - extremely short loss exposure window. Mature spinach more challenging but possible with intensive 
management.

MANAGEMENT OPTIONS: Baby spinach (RECOMMENDED): single N application 70-80 lb/ac pre-plant, P banded 60-80 
lb P₂O₅, K 70-80 lb/ac pre-plant. 20-30 day season minimizes losses even in very low retention. Harvest at 
1-2 inch leaves, single cut.

MATURE SPINACH: Split N essential - 50 lb pre-plant + 40 lb week 3 + 30 lb week 5, total 120 lb N/ac. K 
split: 50 lb pre-plant + 30 lb week 3 + 20 lb week 5. Three splits maintain availability through 50-60 day 
season. Multiple harvests possible (2-3 cuts) but quality declines with later cuts.

COOL-SEASON ECOLOGY: Spinach's spring/fall growth CRITICAL for very-low-retention viability. Cool soil 
temps (45-55°F) slow chemical/biological processes minimizing losses. Spring window (March-May) ideal: 
adequate moisture, cool temps, low disease pressure, rapid growth. Fall window (September-November) similar. 
Summer spinach not viable - bolts immediately in heat.

RAISED-BED OPTION: Raised beds with compost improves very-low-retention spinach. Beds 4-6 inches tall, 
compost 20-30% by volume. Temporary retention improvement sufficient for baby spinach season (20-30 days). 
Drip irrigation + plastic mulch optional but beneficial - conserves moisture, warms soil, improves growth.

QUALITY-VIABILITY: Baby spinach produces acceptable quality in very-low-retention with intensive management: 
tender leaves, good color, mild flavor. Leaves slightly smaller/thinner than optimal but commercially 
acceptable especially for fresh-market direct sales (farmers markets, CSA, restaurants). Mature spinach 
quality more variable - first harvest acceptable, later harvests tougher and more fibrous.

NITRATE SAFETY: Very-low-retention soils with rapid leaching naturally prevent nitrate accumulation. Spinach 
from very sandy soils typically low nitrates (<2,000 ppm vs 4,000 ppm limit) even with intensive N 
fertilization. Natural leaching provides automatic nitrate management.

VIABILITY: Baby spinach highly viable for 5-7 tons/ac in very-low-retention soils - among TOP leafy green 
choices for very sandy conditions. Short season, acceptable quality, high value. Economics excellent for 
direct marketing. Mature spinach marginally viable - quality issues and intensive management challenge 
profitability."""
    },

    "Kale": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through kale's moderate season (55-75 days) and MODERATE-HEAVY nutrient requirements. Kale: 100-150 lb N, 
80-100 lb P₂O₅, 100-140 lb K₂O for 12-15+ tons/ac fresh weight. High retention supports extended production 
and excellent quality.

MANAGEMENT STRATEGY: Split N for extended harvest: 50% pre-plant (50-75 lb N/ac), 50% at 4-6 weeks after 
harvest begins (50-75 lb N/ac, supports regrowth). All P-K pre-plant adequate in high-retention soils. Kale 
long harvest window (4-8 weeks after first cut) - split N maintains leaf quality throughout.

EXTENDED-SEASON PRODUCTION: Kale extremely cold-hardy (survives 10-15°F, quality improves with light frost). 
Plant early spring for summer harvest or late summer for fall/winter harvest. Fall kale superior quality - 
cold temperatures convert starches to sugars producing sweeter, less bitter leaves. High retention supports 
winter production (slow growth but continuous harvest November-March in mild climates).

NUTRIENT-DENSITY: Kale extremely nutrient-dense vegetable (vitamins A, C, K, minerals Ca, Fe). This density 
reflects kale's high nutrient requirements - "you are what you eat" applies to plants too. High-retention 
soils with balanced fertility produce nutritionally-superior kale. Adequate Ca-Mg particularly important 
for kale's high mineral content.

QUALITY FACTORS: Premium kale: dark green-blue color (indicates adequate N), tender leaves (young growth + 
cool temps), mild sweet flavor (adequate K + cool conditions + light frost), thick substantial leaves 
(adequate Ca-Mg). High retention with proper fertility produces highest-quality kale.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
kale requirements. Standard practices: split N (50% pre-plant + 50% at 4-6 weeks), total 100-150 lb N/ac. 
P-K pre-plant: 80-100 lb P₂O₅, 100-140 lb K₂O for 10-12 tons/ac.

MANAGEMENT STRATEGY: Split N essential for extended harvest. Kale typically harvested over 6-10 weeks 
(multiple pickings of lower leaves or periodic whole-plant cuts). Second N application at 4-6 weeks (as 
harvest begins) maintains leaf quality and vigor through harvest period.

HARVEST SYSTEMS: Multiple approaches. 1) Baby kale (2-3 inch leaves, 25-35 days): single harvest, lower N 
(70-90 lb/ac), very tender. 2) Salad kale (4-6 inch leaves, 40-50 days): 1-2 harvests, moderate N (90-120 
lb/ac), tender enough for fresh salads. 3) Cooking kale (8-12 inch leaves, 55-75 days): multiple harvests 
(continuous picking), higher N (120-150 lb/ac), tougher leaves for cooking. Good-retention soils support 
all types.

VARIETY CONSIDERATIONS: Many kale types with different growth habits. 1) Curly kale (common, cold-hardy, 
uniform harvest). 2) Lacinato/Dinosaur kale (Italian type, dark blue-green, extremely cold-hardy, premium 
quality). 3) Red Russian kale (colorful, very tender, cold-hardy). 4) Siberian kale (extremely hardy, mild 
flavor). All thrive in good-retention soils.

COLD-HARDINESS: Kale survives 10-15°F, continues growth at 40-50°F. This cold-hardiness allows fall-planted 
kale to grow slowly through winter (in mild climates) or resume growth in early spring (cold climates). 
Good retention supports slow winter growth providing fresh harvest November-March.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for kale with proper 
management. Kale moderately well-adapted to moderate retention - moderate demands, moderate season, extended 
harvest compatible with split applications. Split N: 60-70 lb pre-plant + 50-60 lb at 4-6 weeks, total 
110-130 lb N/ac.

MANAGEMENT STRATEGY: Split N and K compensate for moderate retention. K split particularly beneficial for 
extended harvest: 70-80 lb K₂O pre-plant + 40-50 lb at 4-6 weeks. P banded 80-100 lb P₂O₅ ensures early 
availability. Baby kale well-suited to moderate retention - shorter season (25-35 days), lower demands, 
limited loss exposure.

COOL-SEASON ADVANTAGE: Kale's cool-season preference advantage in moderate-retention soils. Spring (March-
May) and fall (August-November) plantings coincide with cool temperatures, moderate rainfall, low ET - 
conditions minimize leaching in moderate-retention soils. Summer kale possible but heat-stress and higher 
leaching rates challenge success.

QUALITY IMPACTS: Moderate retention produces good quality with split applications. Leaves may be slightly 
smaller, lighter green color, mildly less sweet than high-retention production. Still commercially excellent 
especially after light frost (sweetens flavor, tenderizes texture). Baby and salad kale particularly 
successful - tender and flavorful even from moderate-retention soils.

VIABILITY: Kale viable for 8-12 tons/ac in moderate-retention soils with split N-K. Economics good - kale 
high value (especially baby/salad types $3-6/lb), extended harvest (spreads labor), multiple market channels 
(fresh, frozen, chips). Among better leafy greens for moderate-retention conditions.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC challenging for kale but VIABLE 
with intensive management. Kale's extended harvest period (6-10 weeks) increases loss exposure in low-
retention soils. Baby kale most successful - short season (25-35 days), single harvest, limited losses. 
Mature kale requires intensive splits.

MANAGEMENT STRATEGY: Baby kale (RECOMMENDED for low retention): 70-90 lb N/ac pre-plant, P banded 80-100 
lb P₂O₅, K 80-100 lb/ac pre-plant. Single harvest at 2-3 inches minimizes loss exposure.

MATURE KALE: Three-split N - 50 lb pre-plant + 40 lb week 4 + 35 lb week 8, total 125 lb N/ac. Three-split 
K - 60 lb pre-plant + 40 lb week 4 + 30 lb week 8, total 130 lb K₂O. Multiple splits maintain availability 
through extended harvest period. Fertigation alternative: biweekly injections 12-18 lb N/ac, 15-20 lb 
K₂O/ac.

QUALITY CHALLENGES: Low retention produces acceptable quality with intensive management but some issues: 
lighter green color (marginal N), thinner leaves (marginal Ca-Mg), slightly bitter flavor (inconsistent K), 
smaller leaves. Baby kale less affected - harvested young before deficiencies severe. Mature kale more 
challenging - later harvests show increasing quality decline.

COLD-SEASON ADVANTAGE: Kale's extreme cold-hardiness advantage in low-retention soils. Fall-planted kale 
(August-September) grows vigorously in warm soil, then slows with cool weather. Slow winter growth (November-
March) reduces nutrient demand matching low-retention supply capacity. Quality excellent - cold sweetens 
flavor.

VIABILITY: Baby kale viable for 6-9 tons/ac in low-retention soils - good option for sandy conditions. 
Economics reasonable - high value, short season, single harvest. Mature kale marginally viable - extended 
season and quality issues challenge profitability. If growing kale in low-retention, favor baby over mature 
types.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes mature kale challenging but 
baby kale VIABLE. Baby kale's 25-35 day season provides advantage in very-low-retention soils similar to 
baby spinach. Mature kale possible with intensive raised-bed production.

MANAGEMENT OPTIONS: Baby kale (RECOMMENDED): 80-90 lb N/ac pre-plant, P banded 80-100 lb P₂O₅, K 90-100 
lb/ac pre-plant. 25-35 day season minimizes losses. Harvest at 2-3 inches, single cut.

MATURE KALE: Raised beds mandatory - beds 6-8 inches with compost (30-40% by volume). Four-split nutrients: 
N (40 + 35 + 30 + 25 = 130 lb/ac), K (50 + 40 + 30 + 20 = 140 lb K₂O/ac). Drip irrigation + fertigation 
alternative: biweekly injections 15-20 lb N/ac + 18-25 lb K₂O/ac.

COLD-HARDINESS ADVANTAGE: Kale's extreme cold-tolerance MAJOR advantage in very-low-retention soils. Fall 
planting (August-September) establishes plants in warm soil. Winter growth (November-March) extremely slow - 
minimal nutrient demand matches very-low-retention capacity. Harvest continues through winter (mild climates) 
with excellent quality - cold produces sweet tender leaves.

QUALITY-VIABILITY: Baby kale produces acceptable to good quality in very-low-retention: tender texture, 
good color, mild flavor. Slightly smaller leaves but commercially acceptable especially after light frost. 
Mature kale quality variable - first harvests acceptable, later harvests show progressive decline (tougher, 
more bitter, lighter color).

MICROGREENS OPTION: Kale microgreens (7-14 days from seed to harvest) extremely well-suited to very-low-
retention soils. Ultra-short season prevents nutrient losses. Microgreens ultra-high value ($20-40/lb), 
indoor production possible (controlled environment eliminates soil limitations), minimal inputs. If very-
low-retention soil limits field production, consider kale microgreens.

VIABILITY: Baby kale viable for 5-8 tons/ac in very-low-retention soils with intensive management. Among 
better leafy green options for very sandy conditions. Economics reasonable for direct marketing (farmers 
markets, restaurants, CSA). Mature kale marginally viable - quality inconsistent, costs high. Microgreens 
excellent alternative - eliminates retention issues entirely."""
    },

    "Lettuce": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through lettuce's short season (45-75 days depending on type) and MODERATE nutrient requirements. Lettuce: 
80-120 lb N, 60-80 lb P₂O₅, 80-100 lb K₂O for 800-1,000 cartons/ac (18-25 tons/ac depending on type). High 
retention supports rapid growth and premium quality.

MANAGEMENT STRATEGY: Split N for head types: 50% pre-plant (40-60 lb N/ac), 50% at 3-4 weeks (40-60 lb 
N/ac, during head formation). Leaf lettuce: single application pre-plant adequate (short season, multiple 
harvests). All P-K pre-plant - high retention maintains availability through season.

LETTUCE TYPES: Multiple types with different characteristics. 1) Crisphead/Iceberg (75-85 days, large dense 
heads, highest N demand, best retention required). 2) Butterhead/Boston (55-65 days, loose tender heads, 
moderate N). 3) Romaine/Cos (60-70 days, upright heads, moderate N). 4) Leaf lettuce (45-55 days, no heads, 
lowest N, multiple harvests). High-retention soils support all types excellently.

QUALITY-TEMPERATURE: Lettuce cool-season crop (optimal 60-70°F, bolts >75°F). Heat stress produces bitter 
flavor (lactucin compounds), premature bolting, tip burn (Ca deficiency), poor head formation. Cool conditions 
+ good retention + balanced fertility produce mild sweet tender lettuce.

CALCIUM-TIP BURN: Tip burn (leaf margin necrosis) caused by Ca deficiency under rapid growth and/or heat 
stress. High-retention soils with adequate Ca (pH 6.2-6.8, sufficient CEC for Ca storage) plus consistent 
moisture prevent tip burn. Most common in crisphead lettuce under heat stress.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
lettuce requirements. Standard practices: split N for head types (50% pre-plant + 50% at 3-4 weeks), total 
80-120 lb N/ac. Leaf lettuce: single application 70-90 lb N/ac. P-K pre-plant: 60-80 lb P₂O₅, 80-100 lb 
K₂O for 700-900 cartons/ac.

MANAGEMENT STRATEGY: Head lettuce split N supports head formation period (weeks 4-7 from transplant). 
Adequate N during heading produces large dense heads (1.5-2.5 lb), crisp texture, good color. Deficient N: 
small heads, yellow-green color, poor quality. K critical for crispness - "crisp" lettuce literally depends 
on adequate K for cell turgor.

VARIETY-SEASON: Variety selection affects retention needs. Spring varieties (planted March-April) more 
heat-tolerant, moderate demands. Summer varieties (May-June) very heat-tolerant but quality challenging. 
Fall varieties (July-August transplants for September-November harvest) highest quality, most demanding. 
Good-retention soils support all seasons but fall lettuce particularly excellent.

TRANSPLANT-DIRECT SEED: Head lettuce typically transplanted (4-6 week plugs) for uniformity and earlier 
harvest. Leaf lettuce often direct-seeded (lower cost, continuous seeding for successive harvests). Good-
retention soils support both methods. Transplants require adequate P for establishment - banded application 
beneficial.

HARVEST-QUALITY: Premium lettuce: appropriate size (head lettuce 1-2 lb heads, leaf lettuce 6-10 oz bunches), 
crisp texture (adequate K + Ca + water), mild sweet flavor (cool growth, adequate K), attractive color 
(medium to dark green, adequate N), no defects (no tip burn, insect damage, or disease).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC adequate for most lettuce types 
with proper management. Leaf lettuce particularly well-adapted - short season (45-55 days), moderate demands, 
multiple successive plantings possible. Head lettuce viable but requires splits. Split N: 50 lb pre-plant + 
40-50 lb week 3-4, total 90-100 lb N/ac.

MANAGEMENT STRATEGY: Leaf lettuce (RECOMMENDED for moderate retention): 70-90 lb N/ac pre-plant, harvest 
at 45-55 days. Short season limits loss exposure even in moderate retention. Successive plantings every 2-3 
weeks (April-June, August-September) provide continuous harvest.

HEAD LETTUCE: Split N-K compensates for moderate retention during heading period. N: 50 lb pre-plant + 
40-50 lb week 3-4. K: 60 lb pre-plant + 30 lb week 3-4. Crisphead most challenging (highest demands, longest 
season). Butterhead and Romaine more forgiving. Consider intermediate types (mini-romaine, butter-crunch) 
for moderate retention.

QUALITY IMPACTS: Moderate retention produces good to excellent quality with proper management. Leaf lettuce 
quality typically excellent - short season, moderate demands. Head lettuce acceptable quality but possible 
issues: slightly smaller heads (1-1.5 lb vs 1.5-2.5 lb), less crisp texture (marginal K), occasional tip 
burn (marginal Ca), lighter color (marginal N).

IRRIGATION-QUALITY: Moderate-retention sandy loams require irrigation for quality lettuce. Lettuce 95% 
water, shallow roots (8-12 inches) - consistent moisture essential. Drip irrigation ideal: conserves water, 
prevents foliar disease (vs overhead), allows fertigation. Overhead also viable but disease risk higher.

VIABILITY: Leaf lettuce highly viable for 15-20 tons/ac in moderate-retention soils. Head lettuce viable 
for 600-800 cartons/ac with splits. Economics excellent for leaf lettuce (high value $1-3/bunch, continuous 
harvest, fresh market). Head lettuce moderate economics - higher inputs but also higher value.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but lettuce VIABLE - particularly 
leaf types. Leaf lettuce well-adapted: short season (45-55 days), moderate demands, shallow roots (matches 
fertigation capability), high value. Head lettuce challenging but possible with intensive management.

MANAGEMENT STRATEGY: Leaf lettuce (RECOMMENDED): 80-100 lb N/ac pre-plant or split 50 + 40 lb/ac, P banded 
60-80 lb P₂O₅, K 80-100 lb/ac split 60 + 30. Short season minimizes losses.

HEAD LETTUCE: Three-split nutrients compensate for low retention. N: 40 + 35 + 30 = 105 lb/ac (pre-plant + 
week 2 + week 4). K: 50 + 30 + 25 = 105 lb K₂O (same timing). P banded: 60-80 lb P₂O₅. Fertigation 
alternative: weekly injections 12-15 lb N/ac + 12-15 lb K₂O/ac for 6-8 weeks.

QUALITY CHALLENGES: Low retention produces acceptable quality with intensive management but challenges: 1) 
Smaller heads (1-1.5 lb vs 2 lb). 2) Less crisp (marginal K). 3) Tip burn risk (marginal Ca, especially 
under heat stress). 4) Lighter color (marginal N). 5) Variable maturity (inconsistent nutrition). Leaf 
lettuce less affected - tender and flavorful with proper management.

TIP BURN MANAGEMENT: Low-retention sandy soils often low Ca - increases tip burn risk especially under 
heat stress or rapid growth. Solutions: 1) Maintain soil pH 6.2-6.8 (improves Ca availability). 2) Apply 
gypsum 300-500 lb/ac (adds Ca without raising pH). 3) Foliar Ca sprays (calcium chloride, 5 lb/100 gal, 
2-3 applications during head formation). 4) Consistent irrigation (prevents water stress-related Ca 
deficiency).

VARIETY SELECTION: Favor leaf over head lettuce in low retention. If growing head types, choose butterhead 
or mini-romaine (more forgiving than crisphead). Heat-tolerant varieties if summer production (though spring/
fall preferred). Many modern varieties bred for tip burn resistance.

VIABILITY: Leaf lettuce viable for 12-18 tons/ac in low-retention soils. Among best leafy greens for sandy 
conditions - short season, acceptable quality, high value. Head lettuce marginally viable - quality variable, 
intensive inputs. Economics favor leaf lettuce for direct marketing.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes head lettuce extremely 
challenging but leaf lettuce STILL VIABLE. Leaf lettuce's 45-55 day season, shallow roots (compatible with 
raised beds), and multiple harvest system provide advantages in very-low-retention soils.

MANAGEMENT OPTIONS: Leaf lettuce (RECOMMENDED): Raised beds 4-6 inches with compost (30% by volume), drip 
irrigation, plastic mulch optional. N split: 50 lb pre-plant + 40 lb week 3, total 90 lb/ac. P banded: 
60-80 lb P₂O₅. K split: 60 lb pre-plant + 35 lb week 3, total 95 lb K₂O. Two splits adequate for short 
season.

HEAD LETTUCE: Raised beds mandatory, fertigation essential. Beds 6-8 inches, compost 40-50% by volume, 
drip tape + plastic mulch. Fertigation: biweekly injections 12-18 lb N/ac + 15-20 lb K₂O/ac for 8-10 weeks. 
Foliar Ca sprays weekly (calcium chloride) prevent tip burn.

QUALITY-VIABILITY: Leaf lettuce produces acceptable quality in very-low-retention with raised beds: tender 
leaves, mild flavor, good color. Slightly smaller plants but commercially viable especially for direct sales 
(farmers markets, restaurants, CSA). Multiple successive plantings (every 2 weeks) provide continuous supply.

HEAD LETTUCE CRISIS: Head lettuce quality severe problems in very-low-retention even with intensive 
management: very small heads (0.5-1 lb vs 1.5-2.5 lb), poor texture (soft, not crisp), severe tip burn 
(Ca deficiency under rapid growth), pale color, variable maturity. Not economically viable - costs extreme, 
quality poor, yields low.

HYDROPONIC ALTERNATIVE: Very-low-retention soils that challenge soil-based lettuce production may be 
suitable for hydroponic systems. Hydroponics eliminate soil retention issues entirely. Lettuce one of best 
hydroponic crops - short season (35-45 days hydroponics vs 60-75 soil), high value, year-round production 
possible. Consider hydroponic lettuce if soil limitations severe.

VIABILITY: Leaf lettuce viable for 8-12 tons/ac in very-low-retention soils with raised beds and intensive 
management. Among best leafy greens for very sandy conditions - short season, acceptable quality, high 
value. Economics reasonable for direct marketing. Head lettuce not viable - quality and cost barriers 
insurmountable. If considering lettuce in very-low-retention, choose leaf types only."""
    },

    "Cabbage": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through cabbage's moderate-long season (70-120 days depending on type) and HEAVY nutrient requirements. 
Cabbage: 150-200 lb N, 80-120 lb P₂O₅, 120-180 lb K₂O for 30-50 tons/ac (20-25 ton minimum commercial). 
High retention critical for cabbage's extended head formation period.

MANAGEMENT STRATEGY: Split N through growth stages: 40% pre-plant or at transplant (60-80 lb N/ac), 35% 
at 3-4 weeks/early heading (55-70 lb N/ac), 25% at mid-heading (40-50 lb N/ac). Three splits match demand 
pattern and support 4-8 week heading period. All P, most K pre-plant: 80-120 lb P₂O₅, 80-120 lb K₂O. 
Remaining K (30-60 lb K₂O) at early heading.

CABBAGE TYPES: Multiple types with different retention needs. 1) Early cabbage (70-85 days, 2-4 lb heads, 
pointed or round, moderate N). 2) Mid-season (85-100 days, 4-6 lb heads, round, moderate-heavy N). 3) Late/
storage cabbage (100-120 days, 5-10 lb heads, very dense, heaviest N demand). High-retention soils support 
all types, particularly critical for storage cabbage extended season.

HEAD FORMATION: Cabbage forms EXTREMELY dense heads (compacted leaves, high dry matter 8-10% vs lettuce 
4-5%). This density reflects massive nutrient accumulation over 4-8 weeks. Adequate N + K + Ca essential 
for head formation: tight dense heads, heavy weight (3-8 lb), crisp texture, long storage life (storage 
types 4-6 months).

QUALITY-SPLITTING: Head splitting (cracking) major quality defect reducing value 50-80%. Caused by excess 
water/N after heads form - rapid expansion splits tight heads. High retention with proper N timing prevents 
splitting: adequate but not excessive N, cutoff late N (3-4 weeks before harvest), consistent moisture 
(prevents growth surges after dry periods).""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
cabbage's heavy demands. Standard practices: three-split N (40% pre-plant + 35% early heading + 25% mid-
heading), total 150-200 lb N/ac. P-K: 80-120 lb P₂O₅ pre-plant, K split 80-100 lb pre-plant + 40-60 lb 
early heading, total 120-160 lb K₂O for 25-45 tons/ac.

MANAGEMENT STRATEGY: Split N critical for extended season (70-120 days) and heavy head-formation demands. 
Second N application (early heading, weeks 3-4) most critical - supports initial head formation and determines 
head size potential. Third application (mid-heading, weeks 6-8) completes head development and improves 
density/storage quality.

VARIETY-SEASON: Season affects retention requirements. Spring cabbage (transplant March-April, harvest 
June-July): rapid growth, moderate demands, 2-4 lb heads. Summer cabbage (transplant May-June, harvest 
August-September): heat-stressed, challenging quality, 3-5 lb heads. Fall cabbage (transplant July-August, 
harvest October-November): highest quality, largest heads (5-8 lb), best for storage. Good-retention soils 
support all seasons but fall cabbage particularly excellent - cool conditions produce sweet mild flavor.

CALCIUM-QUALITY: Ca critical for head quality and storage life. Adequate Ca produces firm tight heads, 
crisp texture, extended storage (storage types 4-6 months at 32°F). Deficient Ca causes internal breakdown 
(tip burn inside heads, brown spots on inner leaves) particularly during storage. Good-retention soils with 
pH 6.2-7.0 provide adequate Ca.

HARVEST-STORAGE: Head maturity indicated by firmness (squeeze test - solid head ready for harvest). Proper 
nutrition + cool conditions produce dense heads storing 4-6 months (late types) or 1-2 months (early types). 
Poor nutrition: loose heads, short storage, internal breakdown.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for cabbage's heavy 
demands and extended season. Early cabbage most adaptable - shorter season (70-85 days), moderate demands 
(120-150 lb N/ac), smaller heads (2-4 lb). Storage cabbage difficult - long season (100-120 days), heavy 
demands (180-200 lb N/ac), large heads (5-10 lb). Four-split N compensates for moderate retention.

MANAGEMENT STRATEGY: Four-split N essential: 30% pre-plant (45-60 lb) + 30% week 3 (45-60 lb) + 25% week 
6 (40-50 lb) + 15% week 9 (25-40 lb), total 155-210 lb N/ac. Four splits maintain availability through 
extended heading period. K split: 70 lb pre-plant + 40 lb week 3 + 30 lb week 6, total 140 lb K₂O. P 
banded: 80-120 lb P₂O₅.

FERTIGATION OPTION: Overhead or drip fertigation beneficial for moderate-retention cabbage. Biweekly 
injections 15-20 lb N/ac + 15-20 lb K₂O/ac during heading period (weeks 4-12) maintain consistent supply. 
Prevents feast-famine cycles (excess after application, deficiency before next) that cause quality problems.

QUALITY IMPACTS: Moderate retention produces acceptable quality with intensive management but challenges: 
smaller heads (2-5 lb vs 4-8 lb), less dense (lower dry matter), shorter storage life (1-3 months vs 4-6), 
possible internal defects (tip burn from marginal Ca), lighter green color (marginal N late-season). Still 
commercially viable for fresh market though not optimal for long-term storage.

VARIETY SELECTION: Early and mid-season varieties most successful in moderate retention. Storage cabbage 
(100-120 days) marginal - quality variable, large head development challenging. Consider Asian cabbages 
(Napa, Bok Choy) as alternatives - shorter seasons (50-70 days), moderate demands, excellent quality in 
moderate retention.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes traditional cabbage challenging 
but EARLY types viable with intensive management. Early cabbage 70-85 days, 2-4 lb heads, moderate demands 
(120-150 lb N/ac) - more adaptable to low retention than late storage types (100-120 days, 6-10 lb heads, 
extreme demands 180-200 lb N/ac).

MANAGEMENT STRATEGY: Early cabbage (RECOMMENDED): Four to five-split nutrients. N: 35 + 30 + 30 + 25 + 15 
= 135 lb/ac (pre-plant + weeks 2, 4, 6, 8). K: 40 + 35 + 30 + 25 = 130 lb K₂O/ac (weeks 0, 2, 4, 6). P 
banded: 80-100 lb P₂O₅. Multiple splits compensate for losses through 10-12 week season.

FERTIGATION MANDATORY: Low-retention cabbage requires drip or overhead fertigation. Weekly or biweekly 
injections 15-20 lb N/ac + 15-20 lb K₂O/ac maintain consistent availability. Tissue testing every 2-3 weeks 
monitors status - target >3.5% N and >2.5% K in wrapper leaves.

QUALITY CHALLENGES: Low retention produces small heads (2-3 lb vs 4-6 lb target), loose structure (poor 
density), short storage life (days to 1-2 weeks vs months), internal quality issues (tip burn, browning), 
pale color. Suitable for immediate fresh market but not storage. Quality acceptable for local/regional 
sales, roadside stands, farmers markets where expectations moderate.

CALCIUM CRISIS: Low-retention sandy soils typically low Ca (pH 5.0-6.0) - severe problems for cabbage. 
Internal tip burn (brown spotting on inner leaves) extremely common, reduces quality and storage life. 
Solutions: lime to pH 6.5-7.0 (may take months), gypsum 500-800 lb/ac (immediate Ca without pH change), 
foliar Ca sprays (calcium chloride 5-10 lb/100 gal, weekly during heading), consistent irrigation (water 
stress exacerbates Ca deficiency).

VIABILITY: Early cabbage marginally viable for 15-25 tons/ac with intensive fertigation. Economics marginal 
- high input costs (fertigation, multiple splits, Ca management) versus modest yields and quality issues. 
More viable for direct marketing where quality expectations moderate. Storage cabbage not viable in low 
retention - season too long, demands too heavy, quality too poor.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes cabbage production extremely 
difficult to non-viable. Cabbage's combination of heavy demands (150-200 lb N/ac), extended season (70-120 
days), dense head formation, and quality requirements challenge success in very-low-retention soils.

MANAGEMENT OPTIONS: Only early cabbage with any viability, only with intensive raised beds. Beds 6-8 inches, 
compost 40-50% by volume, drip tape + fertigation, plastic mulch. Biweekly injections 18-25 lb N/ac + 20-30 
lb K₂O/ac for 10-12 weeks. Foliar Ca sprays weekly. P banded 80-100 lb P₂O₅.

QUALITY CRISIS: Even with intensive management, quality severe problems: very small heads (1-2 lb vs 4-6 
lb commercial standard), very loose structure (barely forms heads, more like leafy rosettes), extremely 
short storage (harvest day to 2-3 days maximum), internal breakdown (severe tip burn throughout heads), 
very pale color (chronic N deficiency), variable maturity (inconsistent nutrition prevents uniform heading). 
Quality not acceptable for any wholesale market, marginal even for direct sales - consumer expectations 
for cabbage (tight dense heads 2+ lb) difficult or impossible to meet.

HEAD-FORMATION FAILURE: Cabbage requires SUSTAINED adequate nutrition over 4-8 week heading period to form 
tight dense commercial heads. Very-low-retention soils cannot maintain nutrient availability even with 
intensive fertigation - timing mismatches (injection vs demand), leaching between applications, root zone 
limitations all prevent sustained supply. Result: loose rosettes that never form true heads or extremely 
loose poor-quality heads.

CALCIUM CATASTROPHE: Cabbage has HIGHEST Ca requirements among vegetables for head quality. Very-low-
retention sandy soils typically severely Ca-deficient (pH 4.5-5.5, low CEC cannot hold Ca). Internal tip 
burn affects 60-90% of heads even with lime, gypsum, and foliar Ca - brown spots throughout inner leaves 
make heads unmarketable. Ca requirement + retention limitations insurmountable barrier.

VIABILITY: Cabbage production not recommended in very-low-retention soils. Multiple insurmountable barriers: 
extended season allows severe losses, heavy demands exceed supply capacity, head formation requires sustained 
nutrition (impossible in very low retention), Ca requirements cannot be met, quality expectations cannot be 
achieved. Success rate extremely low even with intensive management and high costs.

ALTERNATIVES: If considering cabbage in very sandy soil, STRONGLY reconsider. Better brassica alternatives: 
1) Bok Choy (50-60 days, moderate demands, acceptable quality possible). 2) Kale (55-75 days, moderate 
demands, no head-formation requirement). 3) Collards (60-80 days, similar to kale). All produce acceptable 
quality in very-low-retention where cabbage fails. Among vegetables, cabbage one of WORST choices for very-
low-retention soils."""
    },

    "Broccoli": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through broccoli's moderate season (70-100 days) and HEAVY nutrient requirements. Broccoli: 150-200 lb N, 
80-100 lb P₂O₅, 120-160 lb K₂O for 300-400 cartons/ac (7-10 tons heads/ac). High retention critical for 
broccoli's extended head-formation period and quality.

MANAGEMENT STRATEGY: Split N through growth stages: 40% pre-plant or at transplant (60-80 lb N/ac), 35% 
at 3-4 weeks/button stage (55-70 lb N/ac), 25% at early head formation (40-50 lb N/ac). Three splits match 
demand pattern. All P, most K pre-plant: 80-100 lb P₂O₅, 80-120 lb K₂O. Remaining K (40 lb K₂O) at button 
stage supports head expansion.

HEAD FORMATION: Broccoli forms central head (main harvest, 6-10 oz typical, 1-2 lb premium) plus side shoots 
(secondary harvest after main head cut, extends harvest 2-4 weeks). Adequate N essential for head size and 
bead quality (individual florets should be tight, uniform, dark green - not yellow or loose). Late N (third 
split) particularly important for side-shoot production.

QUALITY-TEMPERATURE: Broccoli cool-season crop (optimal 60-70°F). Heat stress produces buttoning (premature 
tiny heads <2 oz, unmarketable), hollow stems, loose beads, bitter flavor. Cold stress (<35°F sustained) 
causes purple coloration (acceptable but indicates stress). Cool conditions + high retention + balanced 
fertility produce large uniform dark-green heads.

HARVEST TIMING: Broccoli extremely time-sensitive - must harvest when beads tight and green, before yellowing 
(flower opening). Window 3-5 days for peak quality. Good nutrition produces uniform maturity concentrating 
harvest, large heads maximizing value, good side-shoot production extending season.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
broccoli's heavy demands. Standard practices: three-split N (40% pre-plant + 35% button + 25% early head), 
total 150-200 lb N/ac. P-K: 80-100 lb P₂O₅ pre-plant, K split 80-100 lb pre-plant + 40-50 lb button, total 
120-150 lb K₂O for 250-350 cartons/ac.

MANAGEMENT STRATEGY: Split N critical for head size and quality. Second application (button stage, tiny 
head first visible) determines head size potential - this is when head begins expanding. Third application 
(early head formation) completes main head and supports side shoots after main head harvest.

VARIETY-SEASON: Season affects quality and yields. Spring broccoli (transplant March-April, harvest June-
July): rapid growth, good quality, 250-350 cartons/ac. Summer broccoli (May-July harvest): heat-stressed, 
buttoning common, 150-250 cartons/ac. Fall broccoli (transplant July-August, harvest September-November): 
highest quality and yields (300-400 cartons/ac), largest heads, best flavor (cool temperatures sweeten 
broccoli). Good-retention soils support all seasons but fall broccoli particularly outstanding.

SIDE-SHOOT PRODUCTION: After main head harvest, side shoots develop from leaf axils. 3-4 weeks additional 
harvest adds 30-50% to total yield. Adequate late N (third split) essential for vigorous side-shoot 
production. Good-retention soils maintain N availability through extended side-shoot period.

HOLLOW STEM: Hollow stem (internal cavity in main stem) quality defect reducing value. Caused by rapid 
growth from excess N and/or high temperatures. Good retention with proper N timing (three splits, not 
excessive) prevents hollow stem - balanced steady growth rather than excessive surge.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for broccoli's heavy 
demands but manageable with intensive splits. Broccoli moderately adaptable - shorter than cabbage (70-100 
vs 70-120 days), more forgiving of variable nutrition than cauliflower. Four-split N compensates: 30% pre-
plant + 30% week 3 + 25% week 6 + 15% week 9, total 160-180 lb N/ac.

MANAGEMENT STRATEGY: Four-split N maintains availability through extended season. Early splits (pre-plant, 
week 3) support vegetative growth. Middle splits (week 6, 9) support head formation and side shoots. K 
split: 70 lb pre-plant + 40 lb week 3 + 30 lb week 6, total 140 lb K₂O. P banded: 80-100 lb P₂O₅.

FERTIGATION OPTION: Drip or overhead fertigation beneficial for moderate-retention broccoli. Biweekly 
injections 15-20 lb N/ac + 15-20 lb K₂O/ac during rapid growth and heading (weeks 4-12) prevent deficiency 
periods. More consistent nutrition improves head uniformity and reduces buttoning (premature heading from 
stress).

QUALITY IMPACTS: Moderate retention produces acceptable quality with intensive management but challenges: 
smaller main heads (4-8 oz vs 8-12 oz), reduced side-shoot production (20-30% yield increase vs 30-50%), 
variable bead quality (some looseness), lighter green color, occasional hollow stem (if N timing off). 
Still commercially viable but not premium quality.

VARIETY SELECTION: Standard varieties acceptable for moderate retention. Avoid extremely early varieties 
(<60 days) - these are bred for speed and tend to button under any stress. Prefer mid-season varieties 
(75-85 days) with stress tolerance. Hybrid varieties generally better than OP (open-pollinated) - more 
uniform, better stress tolerance, larger heads.

VIABILITY: Broccoli viable for 200-300 cartons/ac with four-split N and proper management. Economics 
moderate - high input costs (splits/fertigation, transplants) but broccoli high value ($2-4/lb fresh). More 
viable for fall production (better quality, higher yields) than spring/summer.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes broccoli production challenging. 
Broccoli's heavy demands (150-200 lb N/ac), extended season (70-100 days), quality sensitivity, and market 
expectations difficult in low-retention conditions. Fertigation highly recommended - weekly injections 15-25 
lb N/ac, 18-25 lb K₂O/ac for 10-14 weeks.

MANAGEMENT STRATEGY: Five-split nutrients or fertigation mandatory. Five splits: N (35 + 35 + 30 + 30 + 25 
= 155 lb/ac at weeks 0, 2, 4, 6, 8), K (40 + 35 + 30 + 25 = 130 lb K₂O/ac at weeks 0, 2, 4, 6). P banded: 
80-100 lb P₂O₅. Frequent applications compensate for losses.

QUALITY CHALLENGES: Low retention produces quality problems: small main heads (3-6 oz vs 6-12 oz commercial), 
minimal side shoots (10-20% increase vs 30-50%), loose beads (individual florets separate easily), light 
green to yellow-green color, severe buttoning risk (stress-induced premature tiny heads), hollow stems. 
Quality suitable for processing (florets) or budget fresh market but not premium.

BUTTONING EPIDEMIC: Buttoning (premature formation of tiny 1-2 oz heads) extremely common in low-retention 
broccoli. Any stress (water, N deficiency, heat) triggers buttoning. Low retention's inherent variability 
(periods of adequacy followed by deficiency) creates perfect buttoning conditions. Solutions limited: 
fertigation provides most consistent supply, transplant larger plugs (6-8 weeks vs standard 4-6), avoid 
heat stress (only fall/spring crops), stress-tolerant varieties.

BORON CRITICAL: Low-retention sandy soils typically B-deficient. Broccoli sensitive to B deficiency - 
causes hollow stem, brown spots in head, bitter flavor. Apply 1-2 lb B/ac pre-plant or include in fertigation 
(0.1-0.2 lb B/ac per injection). Tissue testing mid-season: target >25 ppm B.

VIABILITY: Broccoli marginally viable for 150-250 cartons/ac with intensive fertigation. Economics marginal 
- high input costs versus modest yields and quality issues. More viable for processing market (florets, 
frozen) where appearance less critical than fresh premium. Fall production only - spring/summer buttoning 
too severe.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes broccoli production extremely 
difficult to non-viable. Broccoli's heavy demands, extended season, quality requirements, and stress 
sensitivity combine to challenge success in very-low-retention soils.

MANAGEMENT OPTIONS: Only approach with any viability: intensive raised beds with fertigation. Beds 6-8 
inches, compost 40-50% by volume, drip tape + plastic mulch. Fertigation: biweekly injections 20-25 lb 
N/ac + 20-25 lb K₂O/ac for 12-14 weeks. P banded: 80-100 lb P₂O₅. Foliar B sprays: 0.2-0.3 lb B/100 gal, 
2-3 applications.

QUALITY CRISIS: Even with intensive management, quality severe problems: very small main heads (2-4 oz vs 
6-10 oz standard, many <2 oz = buttoning), essentially no side shoots (plant dies after main head or produces 
tiny shoots), extremely loose beads (heads fall apart, individual florets separate), yellow-green to yellow 
color (chronic N deficiency), severe hollow stem, extremely variable maturity. Quality not acceptable for 
fresh market wholesale, marginal even for processing.

BUTTONING DISASTER: Buttoning (tiny premature heads 1-2 oz) affects 40-70% of crop in very-low-retention 
even with fertigation. Very-low-retention's inability to buffer nutrition creates constant stress triggering 
buttoning. Transplant stress, brief dry period, heat wave, nutrient-timing mismatch all cause buttoning. 
Result: most plants produce unmarketable tiny heads worth 10-25% of normal value.

BORON-HOLLOW STEM: Very-low-retention sandy soils severely B-deficient (often <0.3 ppm vs 1.0+ ppm adequate). 
Broccoli's high B requirement + severe deficiency = hollow stem in 60-90% of heads even with B applications. 
Hollow stem reduces value 30-50% (fresh market) or makes heads unmarketable. B availability in very low 
retention insufficient even with adequate applications - pH, leaching, root limitations prevent uptake.

VIABILITY: Broccoli production not recommended in very-low-retention soils. Multiple barriers: extended 
season allows severe losses, heavy demands exceed supply capacity, buttoning epidemic destroys yields, 
hollow stem affects most heads, quality unacceptable for fresh market. Success rate very low, costs 
extremely high, returns negative or minimal.

ALTERNATIVES: If considering broccoli in very sandy soil, STRONGLY reconsider. Better brassica options: 1) 
Kale (shorter season, lower demands, no head requirement). 2) Collards (similar to kale, even more stress-
tolerant). 3) Chinese cabbage - Bok Choy (50-60 days vs broccoli 70-100, much better adapted). Among 
vegetables, broccoli one of WORST choices for very-low-retention soils."""
    },

    "Cauliflower": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through cauliflower's moderate-long season (70-120 days depending on type) and VERY HEAVY nutrient 
requirements. Cauliflower: 180-220 lb N, 100-120 lb P₂O₅, 150-180 lb K₂O for 400-600 cartons/ac (10-15 
tons heads/ac). Cauliflower MOST DEMANDING of all brassicas - high retention essential.

MANAGEMENT STRATEGY: Split N through growth stages: 35-40% pre-plant or at transplant (65-90 lb N/ac), 
35-40% at 3-4 weeks/button stage (65-90 lb N/ac), 25-30% at early curd formation (50-60 lb N/ac). Three 
splits crucial - cauliflower cannot tolerate N deficiency at any stage without serious quality loss. All P, 
most K pre-plant: 100-120 lb P₂O₅, 100-130 lb K₂O. Remaining K (50 lb K₂O) at button stage.

CURD FORMATION: Cauliflower forms dense white curd (modified flower structure, pre-flower stage). EXTREME 
sensitivity to stress during curd formation - any stress (water, N deficiency, heat, cold, irregular nutrition) 
causes defects: 1) Buttoning (tiny premature curds <4 oz). 2) Ricing (loose grainy texture, florets separate). 
3) Hollow stem. 4) Discoloration (yellow, purple, brown). High retention with consistent management critical.

QUALITY-BLANCHING: White curds require blanching (light exclusion) - leaves tied over curd or self-blanching 
types (leaves naturally cover curd). Blanching prevents chlorophyll development (green color), anthocyanin 
(purple from cold), yellowing from sunlight. Modern self-blanching varieties easier management. Colored 
types (purple, orange, green) don't require blanching.

TEMPERATURE SENSITIVITY: Cauliflower MOST temperature-sensitive vegetable. Optimal 60-65°F (extremely 
narrow!). Above 75°F: buttoning, poor curd development, ricing, bitterness. Below 50°F sustained: premature 
buttoning, purple color. High retention buffers temperature stress through consistent nutrition.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
cauliflower's very heavy demands. Standard practices: three-split N (35-40% pre-plant + 35-40% button + 
25-30% early curd), total 180-220 lb N/ac. P-K: 100-120 lb P₂O₅ pre-plant, K split 100-120 lb pre-plant + 
50-60 lb button, total 150-180 lb K₂O for 350-550 cartons/ac.

MANAGEMENT STRATEGY: Split N absolutely critical - cauliflower will not tolerate N deficiency at any growth 
stage. Second application (button stage) particularly critical - this is when curd begins forming, determines 
curd size potential. Too-early or too-late application causes quality defects (buttoning if deficient, 
ricing if late-excessive).

VARIETY-SEASON MATCHING: Season selection critical for cauliflower success - more critical than any other 
vegetable. Spring cauliflower (transplant March-April, harvest June-July): risky, heat stress common, 
buttoning frequent, 300-400 cartons/ac. Summer cauliflower: NOT RECOMMENDED - extreme heat-stress, severe 
buttoning, poor quality. Fall cauliflower (transplant July-August, harvest September-November): BEST SEASON 
- consistent cool temps, highest quality and yields (450-600 cartons/ac), least stress. Cauliflower should 
be primarily fall crop.

TRANSPLANT QUALITY: Cauliflower extremely sensitive to transplant stress (more than broccoli/cabbage). 
Stressed transplants never fully recover - produce small buttons instead of full curds. Use large vigorous 
plugs (6-8 weeks, well-fertilized), transplant carefully (minimal root disturbance), irrigate immediately. 
Good-retention soils support rapid establishment reducing stress.

HARVEST WINDOW: Cauliflower very time-sensitive - harvest when curd 6-8 inches diameter, compact, white 
(or appropriate color), before ricing begins. Window 3-7 days for peak quality (longer than broccoli 3-5 
days but shorter than cabbage 2-3 weeks). Good nutrition produces uniform maturity allowing efficient 
harvest.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC extremely challenging for 
cauliflower's very heavy demands and extreme stress sensitivity. Cauliflower LEAST adaptable of brassicas 
to moderate retention - highest demands (180-220 lb N/ac), narrowest temperature range (60-65°F optimal), 
most sensitive to nutrition variability. Only fall production recommended - spring/summer too risky. Four 
to five-split N mandatory.

MANAGEMENT STRATEGY: Five-split N compensates for moderate retention: 25% pre-plant + 25% week 2 + 25% 
week 4 + 15% week 6 + 10% week 8, total 190-220 lb N/ac. Frequent splits prevent deficiency periods (even 
brief deficiency causes quality defects). K split: 80 lb pre-plant + 50 lb week 2 + 40 lb week 4, total 170 
lb K₂O. P banded: 100-120 lb P₂O₅.

FERTIGATION ESSENTIAL: Drip or overhead fertigation strongly recommended for moderate-retention cauliflower. 
Weekly injections 18-25 lb N/ac + 18-25 lb K₂O/ac for 10-14 weeks provide most consistent nutrition possible. 
Cauliflower's extreme stress sensitivity requires maximum nutrition consistency - fertigation provides this 
better than split applications.

QUALITY CHALLENGES: Moderate retention produces quality problems even with intensive management: smaller 
curds (4-6 oz vs 1.5-2 lb commercial), frequent buttoning (20-40% of crop produces <4 oz curds), ricing 
(loose grainy texture), discoloration (yellow/brown spotting), hollow stem, variable maturity. Yields 250-400 
cartons/ac vs 450-600 optimal. Quality marginal for premium fresh market though acceptable for processing 
(florets).

BORON-MOLYBDENUM CRITICAL: Cauliflower high micronutrient demands, especially B and Mo. Moderate-retention 
soils often deficient. B deficiency: hollow stem, brown curd, bitter flavor. Mo deficiency: whiptail (narrow 
distorted leaves), poor curd development. Apply: 1-2 lb B/ac + 0.1-0.2 lb Mo/ac pre-plant. Tissue testing 
mid-season: target >30 ppm B, >0.3 ppm Mo.

VIABILITY: Cauliflower marginally viable for 250-400 cartons/ac in moderate-retention soils with intensive 
fertigation, ONLY fall production. Economics marginal - extremely high input costs (fertigation, frequent 
applications, large transplants, micronutrients) versus modest yields and quality issues. High risk - 
investment loss if buttoning severe. Consider carefully whether cauliflower worth risk in moderate retention.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes cauliflower production 
extremely difficult. Cauliflower's combination of very heavy demands (180-220 lb N/ac), extreme stress 
sensitivity, narrow temperature requirements (60-65°F optimal), and quality expectations nearly impossible 
in low-retention conditions. Only fall production with intensive fertigation has any viability.

MANAGEMENT STRATEGY: Intensive fertigation mandatory - weekly injections 20-25 lb N/ac + 20-25 lb K₂O/ac 
for 12-15 weeks. P banded: 100-120 lb P₂O₅. Micronutrients: B 1-2 lb/ac + Mo 0.2 lb/ac pre-plant, then 
foliar sprays (0.2 lb B + 0.05 lb Mo per 100 gal) every 2 weeks during curd formation.

QUALITY DISASTER: Low retention produces severe quality problems: very small curds (2-4 oz vs 1-2 lb, most 
<4 oz = buttons), extremely high buttoning rate (40-70% of plants), severe ricing (curds fall apart into 
individual florets), widespread discoloration (yellow, brown, purple spotting), hollow stem in most plants, 
bitter flavor, extremely variable maturity. Quality not acceptable for fresh market wholesale. Marginally 
viable for processing florets (if sufficient non-button plants).

BUTTONING EPIDEMIC: Buttoning affects 40-70% of crop in low-retention even with fertigation. Cauliflower's 
extreme stress sensitivity + low retention's inability to provide consistent nutrition = buttoning disaster. 
Any stress (transplant shock, brief water stress, nutrient-timing mismatch, unexpected temperature extreme) 
triggers irreversible buttoning. Button plants worthless - too small for market, uneconomical to harvest.

ECONOMIC CATASTROPHE: Cauliflower one of highest input-cost vegetables: expensive transplants ($0.15-0.30/
plant vs lettuce $0.05-0.10), intensive fertigation, multiple micronutrient applications, precise harvest 
timing (labor-intensive), high cull rate. Low-retention production amplifies all costs while reducing yields 
and quality. Economics nearly always negative - costs far exceed returns. Investment loss almost certain.

VIABILITY: Cauliflower production NOT RECOMMENDED in low-retention soils. Technical barriers (extreme 
buttoning, quality crisis, nutrition-buffer impossibility) and economic barriers (extreme costs, high failure 
rate, unmarketable product) make success extremely unlikely. Even fall production with intensive management 
fails more often than succeeds. Risk-to-reward ratio extremely unfavorable.

ALTERNATIVES: If considering cauliflower in low-retention soil, STRONGLY reconsider and choose alternatives. 
Any other brassica better adapted: broccoli more stress-tolerant, cabbage less demanding, kale/collards 
much easier. Any other vegetable family likely better choice. Cauliflower absolutely WORST vegetable for 
low-retention conditions - difficulty level extreme, success probability very low.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes cauliflower production 
essentially impossible. Cauliflower's very heavy demands, extreme stress sensitivity, and quality requirements 
cannot be met in very-low-retention soils even with unlimited resources and intensive management.

MANAGEMENT IMPOSSIBILITY: No practical management approach provides consistent adequate nutrition for 
cauliflower in very-low-retention soils. Intensive raised beds with compost + fertigation twice-weekly + 
foliar feeding + micronutrients still produces >60% buttoning, severe quality defects, mostly unmarketable 
crop. Very-low-retention's inability to buffer nutrition creates constant extreme stress - exactly what 
cauliflower cannot tolerate.

CATASTROPHIC FAILURE: Very-low-retention cauliflower production fails completely 70-90% of attempts. 
Remaining 10-30% "successes" produce: 80-90% buttons (<4 oz unmarketable tiny curds), 5-15% small curds 
(4-8 oz, marginal quality, low value), 0-5% commercial curds (>12 oz, acceptable quality). Yields typically 
<100 cartons/ac vs 400-600 target. Most crop not worth harvesting - labor cost exceeds value.

ECONOMIC DEVASTATION: Cauliflower requires highest inputs of any vegetable: $0.20-0.30/plant transplants, 
intensive fertigation system, twice-weekly injections, multiple foliar applications, micronutrient programs, 
raised beds + compost, precise harvest (very labor-intensive). Very-low-retention production amplifies costs 
while virtually guaranteeing crop failure. Investment loss $3,000-5,000/ac typical - costs far exceed any 
possible returns. Financial disaster.

STRESS-SENSITIVITY CATASTROPHE: Cauliflower's extreme stress sensitivity makes it fundamentally incompatible 
with very-low-retention soils. Very-low-retention inherently creates variable stressful growing conditions - 
exactly opposite of cauliflower's requirements for extremely consistent stress-free environment. No management 
technique can overcome this fundamental incompatibility.

VIABILITY: Cauliflower production absolutely NOT VIABLE in very-low-retention soils. DO NOT ATTEMPT. Success 
probability near zero, investment loss virtually certain, labor/resources wasted on unmarketable crop. Among 
all crops (vegetables, field crops, fruits), cauliflower single WORST choice for very-low-retention soils - 
difficulty level extreme, requirements impossible to meet, failure almost guaranteed.

ALTERNATIVES: If someone insists on growing cauliflower in very-low-retention soil despite strong warnings: 
1) Use hydroponic or container production instead (eliminates soil limitations entirely). 2) Or choose ANY 
other vegetable - literally any vegetable easier than cauliflower in very sandy soil. 3) Or grow colored 
cauliflower (purple, orange) which slightly more stress-tolerant than white (though still extremely difficult). 
Best advice: DON'T GROW CAULIFLOWER in very-low-retention soils - choose adapted crops instead."""
    },

    "Onions": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through onion's long season (110-175 days depending on type) and MODERATE-HEAVY nutrient requirements. 
Onions: 100-150 lb N, 80-100 lb P₂O₅, 100-140 lb K₂O for 600-800 cwt/ac (30-40 tons/ac). High retention 
essential for onion's extended season and shallow root system.

MANAGEMENT STRATEGY: Split N through growth stages: 30-35% at planting or after emergence (30-50 lb N/ac), 
35-40% at 6-8 weeks/early bulbing (35-60 lb N/ac), 25-30% at 10-12 weeks/mid-bulbing (25-45 lb N/ac). Three 
splits match demand pattern. CRITICAL: cutoff N 4-6 weeks before harvest - late N delays maturity, reduces 
storage quality (promotes neck rot), produces thick necks. All P, most K at planting: 80-100 lb P₂O₅, 80-100 
lb K₂O. Remaining K (30-40 lb K₂O) at early bulbing.

BULBING PHYSIOLOGY: Onion bulbing triggered by day-length (photoperiod). Short-day types (10-12 hours, 
southern): bulb early (90-110 days), store poorly, mild flavor. Intermediate-day (12-14 hours, most regions): 
bulb mid-season (110-140 days), moderate storage, moderate pungency. Long-day (14-16 hours, northern): bulb 
late (140-175 days), excellent storage (6-10 months), pungent flavor. High retention supports all types 
through complete bulbing period.

STORAGE QUALITY: Storage onions require: 1) Hard neck (firm tight neck, not thick/soft). 2) Proper maturity 
(tops fall over naturally, outer scales dry and papery). 3) Complete field curing (1-2 weeks after topple, 
on soil surface). 4) Low N at bulbing (promotes hard dry scales). High retention with proper N timing 
(cutoff 4-6 weeks before harvest) produces excellent storage quality - onions store 6-10 months (long-day 
types) at 32-35°F, 65-70% RH.

SHALLOW ROOTS: Onions have extremely shallow roots (6-12 inches, most roots top 6 inches) - among most 
shallow of all vegetables. This makes onions: 1) Drought-sensitive (require irrigation in most regions). 2) 
Dependent on soil retention (cannot access nutrients below 12 inches). 3) Sensitive to soil surface conditions 
(crust, compaction). High retention in root zone critical.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
onion requirements. Standard practices: three-split N (30-35% planting + 35-40% early bulbing + 25-30% mid-
bulbing), total 100-150 lb N/ac. P-K: 80-100 lb P₂O₅ at planting, K split 80-100 lb planting + 30-40 lb 
early bulbing, total 110-140 lb K₂O for 500-700 cwt/ac.

MANAGEMENT STRATEGY: Split N essential for long season (110-175 days) and shallow roots. Second application 
(early bulbing, as day-length triggers bulbing response) particularly important - supports rapid bulb 
expansion (2-4 weeks of very rapid growth). Third application (mid-bulbing) completes bulb sizing. CUTOFF 
N 4-6 weeks before anticipated harvest - late N sacrifices storage quality for minimal size increase (poor 
trade-off).

ONION TYPES: Multiple types with different uses. 1) Storage onions (long-day, 140-175 days, pungent, hard 
scales, 6-10 month storage). 2) Fresh/sweet onions (short/intermediate-day, 90-140 days, mild, soft scales, 
1-3 month storage). 3) Pearl/cocktail onions (70-90 days, small bulbs <1.5 inch). 4) Bunching/scallions 
(60-75 days, no bulbs, harvest for green tops). Good-retention soils support all types excellently, storage 
types particularly benefit from retention through extended season.

TRANSPLANT-SEED-SETS: Three planting methods. 1) Transplants (4-6 week plugs): earliest harvest, most 
expensive, best uniformity. 2) Direct seed: lowest cost, later harvest, good uniformity with precision 
seeding. 3) Sets (small bulbs): earliest harvest, variable uniformity, higher cost. Good-retention soils 
support all methods. Storage onions typically transplants or direct seed. Fresh onions often sets (speed to 
market).

BOTRYTIS-STORAGE: Botrytis neck rot (Botrytis allii) major storage disease. Caused by: excess N late-season 
(soft necks), incomplete field curing (necks not dry), harvest damage. Good retention with proper N cutoff 
produces hard dry necks resisting neck rot. Field cure 1-2 weeks after topple dries necks completely.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for onions - long 
season (110-175 days) and shallow roots (6-12 inches) limit retention value. Four-split N essential: 25% 
planting + 30% week 6 + 30% week 10 + 15% week 14, total 110-140 lb N/ac. Fresh onions (shorter season 
90-140 days) more adaptable than storage onions (longer season 140-175 days).

MANAGEMENT STRATEGY: Four-split N compensates for moderate retention and shallow roots. Splits every 4 
weeks maintains availability in shallow root zone despite moderate retention below root zone. K split: 70 lb 
planting + 35 lb week 6 + 25 lb week 10, total 130 lb K₂O. P banded: 80-100 lb P₂O₅ (shallow placement 
critical for shallow roots).

FERTIGATION OPTION: Drip fertigation excellent for moderate-retention onions. Weekly or biweekly injections 
10-15 lb N/ac + 10-15 lb K₂O/ac for 14-20 weeks (depending on type). Delivers nutrients directly to shallow 
root zone, compensates for moderate retention below roots. Drip also provides consistent moisture critical 
for shallow-rooted onions.

QUALITY IMPACTS: Moderate retention produces good quality with proper management. Storage quality potentially 
excellent IF N cutoff managed properly (4-6 weeks before harvest) - excess N more common problem than 
deficiency in storage-quality issues. Bulb size acceptable (2.5-3.5 inch vs 3-4 inch optimal). Uniformity 
good with consistent management.

SOIL CRUSTING: Moderate-retention soils (sandy loams) prone to surface crusting after rain/irrigation. 
Crust prevents emergence (direct-seeded onions) and restricts shallow root growth. Solutions: 1) Shallow 
cultivation (1-2 inches) breaks crust. 2) Sprinkler irrigation (light frequent) prevents crust formation. 
3) Transplants (vs direct seed) avoid emergence issues. 4) Organic mulch (straw, grass clippings) prevents 
crusting.

VIABILITY: Fresh/sweet onions highly viable for 400-600 cwt/ac in moderate-retention soils. Storage onions 
viable but more challenging - longer season increases loss exposure. Economics good for fresh onions (premium 
price, moderate inputs). Storage onions moderate economics - lower price but excellent storability extends 
marketing period.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC problematic for onions - long 
season (110-175 days) and shallow roots (6-12 inches, most in top 6) create challenges. Nutrients below 12 
inches unavailable (roots don't reach), nutrients in top 6 inches vulnerable to losses (low retention, high 
exposure). Fertigation highly recommended - biweekly injections 10-15 lb N/ac + 12-18 lb K₂O/ac for 14-24 
weeks.

MANAGEMENT STRATEGY: Frequent splits or fertigation mandatory for low-retention onions. Five-split approach: 
N (25 + 25 + 25 + 20 + 15 = 110 lb/ac at weeks 0, 4, 8, 12, 16), K (40 + 30 + 25 + 20 = 115 lb K₂O/ac at 
weeks 0, 4, 8, 12). P banded shallow: 80-100 lb P₂O₅ at 2-3 inches depth (matches root zone). Frequent 
applications maintain availability in shallow zone.

QUALITY CHALLENGES: Low retention produces acceptable onions IF management intensive but challenges: smaller 
bulbs (2-3 inch vs 3-4 inch), lighter color (inadequate S - sandy soils often S-deficient), variable 
maturity (inconsistent nutrition), possible storage issues (if late N not controlled). Fresh onions less 
affected than storage types.

SULFUR CRITICAL: Onions require high S (20-40 lb S/ac) for bulb quality - pungency, firmness, scale color, 
storage quality. Low-retention soils typically S-deficient (S leaches like N). Include S in program: 
ammonium sulfate (24% S), potassium sulfate (17% S), or elemental S (90% S, slow-release). S particularly 
important for storage onions - pungency and firm scales enhance storability.

IRRIGATION CRITICAL: Onions' shallow roots (6-12 inches) make irrigation mandatory in most low-retention 
soils. Drip ideal: efficient, allows fertigation, maintains consistent shallow-zone moisture. Overhead also 
viable (though less efficient). Water stress during bulbing reduces size dramatically - consistent moisture 
essential weeks 8-16.

VARIETY SELECTION: Fresh/sweet onions (short/intermediate-day) better adapted to low retention than storage 
onions (long-day). Shorter season (90-140 vs 140-175 days) limits loss exposure. If growing storage onions, 
choose earlier long-day types (140-155 days vs 155-175). Sets faster to harvest than transplants or seed - 
consider for low retention.

VIABILITY: Fresh onions viable for 350-550 cwt/ac in low-retention soils with fertigation. Storage onions 
marginally viable - quality variable, season too long for reliable results. Economics moderate for fresh 
(premium prices offset costs). Storage onions marginal economics.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes onion production very 
challenging - long season (110-175 days) and shallow roots (6-12 inches) create severe nutrient-supply 
problems. Only fresh/sweet onions (short season) with intensive fertigation have viability. Storage onions 
extremely difficult.

MANAGEMENT OPTIONS: Fresh onions only (short/intermediate-day, 90-120 days). Raised beds mandatory: 4-6 
inches tall, compost 30-40% by volume. Drip fertigation: biweekly injections 12-18 lb N/ac + 15-20 lb K₂O/ac 
for 12-16 weeks (6-8 injections). P banded shallow: 80-100 lb P₂O₅ at 2-3 inches. S included: ammonium 
sulfate or potassium sulfate provides S with N-K. Sets (small bulbs) faster to harvest than transplants or 
seed - preferred for very low retention.

STORAGE ONIONS: Not recommended - 140-175 day season too long for very-low-retention viability. If 
attempting: raised beds + compost, intensive twice-weekly fertigation, earliest long-day varieties (140-150 
days only), expect modest results. Quality and yield insufficient for commercial storage-onion economics.

QUALITY-VIABILITY: Fresh onions produce acceptable quality in very-low-retention with raised beds: medium 
bulbs (2-3 inch), mild flavor, good appearance. Slightly lighter color (S-deficiency common despite 
applications) but commercially viable. Primarily for fresh market direct sales (farmers markets, roadside 
stands, restaurants) where quality expectations moderate and premium prices obtainable.

SHALLOW-ROOT ADVANTAGE: Onions' shallow roots (6-12 inches) allow raised-bed production to encompass entire 
root zone. Beds 4-6 inches + 6 inches soil below = 10-12 inches total, captures 90-95% of root system. This 
makes onions more suitable for raised-bed production than deep-rooted crops (tomatoes, watermelons). Raised 
beds' temporary retention improvement sufficient for onion's shallow needs.

BUNCHING ONIONS: Bunching onions/scallions (60-75 days to harvest for green tops, no bulbs) well-suited to 
very-low-retention soils. Short season, moderate demands, high value. Harvest before bulbing begins - avoids 
bulbing-stage nutrition challenges. Successive plantings every 3-4 weeks (April-August) provide continuous 
harvest. Economics excellent - high value ($3-5/bunch), rapid turnover, multiple crops per season.

VIABILITY: Fresh bulbing onions marginally viable for 300-450 cwt/ac with intensive raised beds and 
fertigation. Storage onions not viable - season too long, quality too variable, economics negative. Bunching 
onions highly viable - excellent option for very-low-retention vegetable production. If growing onions in 
very-low-retention, favor bunching types over bulbing types."""
    },

    "Carrots": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC provides superior storage 
through carrot's moderate season (70-110 days depending on type) and MODERATE nutrient requirements. Carrots: 
80-120 lb N, 80-100 lb P₂O₅, 100-140 lb K₂O for 25-35+ tons/ac. High retention supports excellent root 
development and quality.

MANAGEMENT STRATEGY: Split N for long-season types: 50% pre-plant (40-60 lb N/ac), 50% at 4-6 weeks after 
emergence (40-60 lb N/ac). Short-season bunching carrots: single application 70-90 lb N/ac pre-plant adequate. 
All P-K pre-plant: 80-100 lb P₂O₅, 100-140 lb K₂O. High retention maintains availability through root-
development period.

ROOT DEVELOPMENT: Carrot quality depends on root morphology: straight, smooth, uniform taper, appropriate 
length, good color (orange, or appropriate for colored types). Factors affecting root quality: 1) Soil 
structure (loose, friable, deep, no compaction or hardpan). 2) Adequate balanced nutrition (excess N produces 
hairy/forked roots, deficient N produces short stunted roots). 3) Consistent moisture (prevents cracking). 
High-retention soils with good structure produce excellent root morphology.

CARROT TYPES: Multiple types for different uses. 1) Nantes (6-7 inches, cylindrical, excellent quality, 
fresh market). 2) Imperator (8-10 inches, slender taper, processing/fresh). 3) Chantenay (5-6 inches, broad 
shoulders, thick, heavy soils). 4) Danvers (6-7 inches, intermediate shape, adaptable). 5) Baby/mini (3-4 
inches, specialty fresh). High-retention soils support all types excellently, particularly important for 
long types (Imperator) requiring deep root development.

SOIL TEXTURE CRITICAL: Carrots require loose friable soil for straight root development. Heavy clay soils: 
roots forked, twisted, short (high retention but poor structure). Sandy soils: roots straight, long, smooth 
(good structure but low retention). Sandy loam or loamy sand ideal: good structure + adequate retention. 
High-retention sandy loam represents optimal combination.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC provides good storage for 
carrot requirements. Standard practices: split N for long-season types (50% pre-plant + 50% at 4-6 weeks), 
total 80-120 lb N/ac. Bunching carrots: single application 70-90 lb N/ac. P-K pre-plant: 80-100 lb P₂O₅, 
100-140 lb K₂O for 20-30 tons/ac.

MANAGEMENT STRATEGY: Split N supports root development without excess. First application at planting 
supports germination and early growth (4-6 weeks). Second application (4-6 weeks after emergence) supports 
rapid root enlargement phase (weeks 6-12). Avoid excess N - causes excessive tops, forked/hairy roots, poor 
root color.

VARIETY-SEASON: Season affects variety selection and yields. Spring carrots (seeded March-May, harvest 
July-August): rapid growth, Nantes or Danvers types, moderate yields (18-25 tons/ac). Summer carrots (seeded 
May-June, harvest August-October): heat-stressed, lower quality, 15-22 tons/ac. Fall carrots (seeded July-
August, harvest October-December): highest quality and yields (25-35 tons/ac), sweetest flavor (cold converts 
starch to sugar), best for storage. Good-retention soils support all seasons but fall carrots particularly 
excellent.

GERMINATION CHALLENGES: Carrot seed tiny, slow-germinating (10-20 days), sensitive to crusting. Solutions: 
1) Shallow seeding (1/4-1/2 inch, no deeper). 2) Light frequent irrigation (prevents crust, maintains 
moisture). 3) Mix with radish seed (radishes emerge fast, break crust for carrots, then harvested early). 
4) Cover with sand or vermiculite (prevents crusting). Good-retention soils with good structure support 
germination.

COLOR-NUTRITION: Orange color from beta-carotene (vitamin A precursor). Adequate nutrition (especially N + 
K) produces deep orange color. Deficient nutrition: pale orange or yellow-orange. Modern colored types 
(purple, red, yellow, white) have similar nutrition requirements. Quality carrots require balanced nutrition 
for optimal color regardless of type.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC generally ADEQUATE for carrots - 
surprisingly well-adapted. Factors favoring carrots in moderate retention: moderate demands, moderate season 
(70-110 days), relatively deep roots (8-12 inches, better than onions/lettuce), tolerant of varied conditions. 
Split N: 50 lb pre-plant + 40-50 lb week 4-6, total 90-100 lb N/ac.

MANAGEMENT STRATEGY: Two-split N adequate for moderate retention - carrots relatively forgiving compared to 
demanding vegetables (cauliflower, peppers). K split optional: 80 lb pre-plant + 40 lb week 4-6, total 120 
lb K₂O. P broadcast or banded: 80-100 lb P₂O₅.

SOIL-TEXTURE ADVANTAGE: Moderate-retention soils typically sandy loams - IDEAL texture for carrots. Balance 
of: loose structure (straight roots, easy harvest), adequate retention (sufficient nutrients), good drainage 
(prevents rot). While retention moderate, texture advantages compensate - straight smooth roots, excellent 
quality. Many premium carrot-production regions have moderate-retention sandy loams combining good structure 
+ adequate retention.

ROOT-QUALITY MANAGEMENT: Moderate retention with proper N management produces excellent root quality. Key: 
avoid excess N (causes forking, hairy roots, poor color). Better slightly deficient than excessive - 
deficient roots shorter/paler but straight and smooth, excess roots forked/hairy/poor (unmarketable). Two-
split N prevents excess while maintaining adequacy.

VARIETY SELECTION: Nantes and Danvers types excellent for moderate-retention soils. Imperator possible 
(requires deeper root zone, longer season). Baby carrots highly successful - short season (60-75 days), 
moderate demands, harvest before retention becomes limiting, premium price. Consider baby carrots strong 
candidate for moderate-retention production.

VIABILITY: Carrots highly viable for 18-28 tons/ac in moderate-retention soils. Among best vegetable choices 
for moderate retention - moderate demands, well-adapted, excellent quality achievable. Economics excellent - 
moderate inputs, good yields, strong market (fresh, processing, juicing, baby). Carrots should be considered 
high-priority crop for moderate-retention vegetable production.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC but carrots WELL-ADAPTED - among 
best vegetables for low-retention conditions. Advantages: moderate demands (80-120 lb N/ac), moderate season 
(70-110 days), sandy texture ideal for root development (straight smooth roots), reasonable prices (makes 
moderate inputs economically viable). Split N: 50 lb pre-plant + 40 lb week 4 + 30 lb week 8, total 120 lb 
N/ac.

MANAGEMENT STRATEGY: Three-split N compensates for low retention through 14-16 week season. P banded: 80-
100 lb P₂O₅ enhances early root development. K split: 70 lb pre-plant + 40 lb week 4, total 110 lb K₂O. 
Three splits maintain adequacy without excess (excess N worse than modest deficiency for carrot root quality).

SANDY-SOIL ADVANTAGE: Low-retention soils typically sandy - EXCELLENT for carrot production. Sandy texture 
provides: 1) Straight smooth roots (no forking, twisting, hairy roots). 2) Easy harvest (roots pull cleanly). 
3) Minimal washing needed (sand rinses easily vs clay). 4) Excellent drainage (prevents rot). While retention 
low, texture advantages make sandy soils preferred for carrots commercially. Many major carrot-production 
regions have low-retention sandy soils.

ROOT-QUALITY EXCELLENCE: Low-retention sandy soils produce SUPERIOR root morphology - straight, smooth, 
uniform, excellent color. Quality often better than high-retention clay soils (which produce forked, twisted, 
difficult-to-harvest roots despite better retention). For carrots, soil structure more important than 
retention level - sandy soils' structure advantages outweigh retention limitations.

VARIETY SUCCESS: All carrot types successful in low-retention sandy soils. Imperator (long slender) 
particularly excellent - requires deep loose soil, which sandy soils provide. Baby carrots excellent - short 
season (60-75 days), premium price, rapid turnover. Nantes, Danvers all produce premium quality in sandy 
low-retention conditions.

VIABILITY: Carrots highly viable for 15-25 tons/ac in low-retention soils - among TOP vegetable choices for 
low-retention conditions. Sandy texture advantages (root quality, easy harvest) offset retention limitations 
(modest yields). Economics excellent - acceptable yields, premium quality (straight smooth roots command 
premium), moderate inputs, strong markets. Carrots should be high-priority crop for low-retention sandy-soil 
vegetable production.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but carrots STILL HIGHLY VIABLE - 
among absolute best vegetables for very-low-retention conditions. Carrots unique: very sandy soils' texture 
advantages (root morphology, harvest ease) outweigh retention disadvantages. Many commercial carrot operations 
use very-low-retention sandy soils specifically for superior root quality.

MANAGEMENT OPTIONS: Three to four-split N: 40 lb pre-plant + 35 lb week 4 + 30 lb week 8 + 20 lb week 12 = 
125 lb N/ac. P banded: 80-100 lb P₂O₅. K split: 60 lb pre-plant + 40 lb week 4 + 30 lb week 8 = 130 lb 
K₂O. Splits maintain availability through season. Short-season baby carrots (60-75 days): 80 lb N/ac split 
50 + 30, P banded 80 lb P₂O₅, K 80 lb/ac split 50 + 30.

TEXTURE ADVANTAGE: Very-low-retention soils almost always very sandy (sands, loamy sands) - IDEAL for 
carrots. Provides: 1) Exceptionally straight smooth uniform roots (premium quality). 2) Extremely easy 
harvest (roots pull effortlessly from sand). 3) Minimal washing (sand rinses completely vs clay staining). 
4) Zero forking/twisting (structural defects absent in sand). 5) Deep rooting possible (no hardpan in deep 
sands). Texture advantages make very sandy soils commercially preferred for high-quality carrot production.

ROOT QUALITY PREMIUM: Very-low-retention sandy soils produce HIGHEST quality carrot roots - appearance, 
morphology, and marketability superior to high-retention clays. While yields modest (12-22 tons/ac vs 25-35 
optimal), quality premium compensates. Premium straight 8-10 inch Imperators from sandy soils command 20-40% 
price premium over forked/twisted carrots from clay soils.

BABY-CARROT EXCELLENCE: Baby carrots (60-75 days, 3-4 inch roots, specialty fresh market) exceptionally 
well-suited to very-low-retention sands. Short season minimizes retention limitations, sandy texture produces 
perfect straight uniform mini-roots, premium prices ($3-5/bunch) make lower yields economically viable. 
Successive plantings every 3-4 weeks (April-August) provide continuous supply.

IRRIGATION CRITICAL: Very-low-retention sandy soils require irrigation for carrots. Drip ideal: efficient, 
precise, allows fertigation if desired. Overhead also viable (though less efficient). Consistent moisture 
essential for: 1) Germination (2-3 weeks critical period). 2) Root development (prevents cracking from dry-
wet cycles). Sandy soils drain rapidly - frequent irrigation necessary.

VIABILITY: Carrots highly viable for 12-22 tons/ac in very-low-retention soils - among TOP TWO vegetable 
choices for very sandy conditions (with snap beans). Texture advantages offset retention limitations. Economics 
excellent - acceptable yields, premium quality commands higher prices, moderate inputs, strong markets. Baby 
carrots particularly profitable - short season, premium price, continuous production. If growing vegetables 
in very-low-retention sandy soil, carrots should be FIRST consideration - best adapted, highest quality, 
most reliable success."""
    },
    
    # ========================================================================
    # FRUIT & NUT CROPS
    # ========================================================================

    "Apples": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports long-lived productive 
apple orchards (30-50+ year lifespan) with consistent nutrient availability through growing season and across 
years. Perennial tree crops benefit tremendously from high retention - mature trees have extensive root 
systems accessing large soil volume. Moderate annual requirements (80-120 lb N, 40-60 lb P₂O₅, 100-150 lb 
K₂O/ac) maintained efficiently in high-retention soils.

MANAGEMENT STRATEGY: Split N applications optimize tree response: 50-60% early spring (bud break to bloom), 
40-50% post-bloom (petal fall to June). Total 80-120 lb N/ac depending on tree size, vigor, crop load. K 
annually: 100-150 lb K₂O/ac, broadcast or split. P every 2-3 years: 40-60 lb P₂O₅/ac based on soil test. 
High retention allows biennial P applications reducing costs and labor.

CALCIUM CRITICAL: Ca essential for apple quality - firmness, storage life, prevents physiological disorders 
(bitter pit, cork spot, internal breakdown). High retention maintains Ca availability but foliar Ca sprays 
(calcium chloride 0.5-0.8%, 4-6 applications from petal fall through August) directly improve fruit Ca. 
Adequate soil Ca (pH 6.0-7.0, good CEC) supports tree health; foliar Ca improves fruit quality.

VIGOR-BEARING BALANCE: High retention supports excellent tree vigor but CAUTION - excessive vegetative 
growth reduces fruiting. Manage N to balance: vigorous young non-bearing trees need 100-120 lb N/ac; mature 
bearing trees need 60-80 lb N/ac. Terminal shoot growth 8-12 inches optimal - less indicates deficiency, 
more indicates excess promoting vegetative growth over fruit.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC excellent for productive apple 
orchards. This retention level supports 20-30 year orchard life with standard annual fertility program. 
Many premier apple regions have soils in this retention range - provides adequate nutrition without excessive 
vigor that delays bearing or promotes disease (fire blight).

MANAGEMENT STRATEGY: Standard split N program: 60% early spring (bud break to bloom) + 40% post-bloom (petal 
fall to June), total 80-120 lb N/ac adjusted to tree vigor and crop load. K annually: 100-150 lb K₂O/ac. 
P annually or alternate years: 40-60 lb P₂O₅/ac. Annual soil testing plus leaf tissue analysis (July sample 
from mid-shoots) guide fertility adjustments.

CROP-LOAD NUTRITION: Adjust N to crop load: heavy crop years need upper range (100-120 lb N/ac), light 
crop years lower range (60-80 lb N/ac). Good retention allows some flexibility - reduces annual adjustments 
needed since retention buffers year-to-year variation. This helps maintain consistent tree performance despite 
biennial bearing tendency.

MICRONUTRIENTS: B for fruit set and seed development, Zn for shoot growth and leaf size, Fe if pH >7.0. 
Good retention maintains most micronutrients adequately. Annual B spray (1-2 lb/ac) at pink/bloom improves 
fruit set. Foliar Zn if tissue analysis indicates deficiency (<15 ppm). Foliar Ca (4-6 applications) improves 
fruit quality and storage.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC workable for apple orchards with 
more intensive annual management. Perennial nature allows trees to access nutrients from extensive root 
system (8-12 ft deep, spreading 1.5-2× canopy diameter). Orchard life 15-25 years with proper care. Annual 
soil testing and tissue analysis essential.

MANAGEMENT STRATEGY: Three-split N compensates for moderate retention: 40% early spring (bud break) + 35% 
bloom + 25% post-bloom (petal fall), total 100-140 lb N/ac (higher than high-retention to compensate for 
losses). K split: 70% spring + 30% mid-summer, total 120-180 lb K₂O/ac. P annually: 40-60 lb P₂O₅/ac 
(cannot skip years in moderate retention).

YOUNG-TREE ESTABLISHMENT: More challenging in moderate retention - slower establishment, delayed bearing 
(4-6 years vs 2-4 years optimal). Heavy initial P application (80-100 lb P₂O₅/ac) at planting plus annual 
N-K support faster development. Consider fertigation first 3-5 years if drip irrigation installed - biweekly 
injections promote better establishment.

FRUIT-QUALITY IMPACTS: Moderate retention affects fruit quality: smaller size (80-100 count vs 72-88 optimal), 
reduced storage life (4-5 months vs 6-8 months), increased physiological disorders (bitter pit, cork spot 
from Ca deficiency). Intensive foliar Ca program (6-8 applications vs 4-6) partially compensates. Focus on 
varieties producing excellent quality at moderate vigor.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes conventional apple orchard 
production challenging. Long-term nature (20-30 year investment) demands adequate sustained fertility - 
difficult in low retention. Young tree establishment slow and uncertain. Mature tree productivity reduced. 
Orchard life shortened to 12-18 years. Economics marginal unless intensive management implemented.

MANAGEMENT OPTIONS: Two approaches: 1) Intensive fertigation if drip/micro-sprinkler installed - biweekly 
injections 10-15 lb N/ac, 12-18 lb K₂O/ac during growing season (April-August). 2) Four-split conventional 
program: 30 lb N at bud break + 30 lb at bloom + 25 lb at petal fall + 25 lb in June, total 110 lb N/ac. 
P banded annually: 60-80 lb P₂O₅. K split quarterly: 40 lb each quarter (spring, early summer, late summer, 
fall) = 160 lb K₂O annually.

TREE-SIZE MANAGEMENT: Consider dwarf rootstocks (M.9, M.26) over standard in low-retention soils. Advantages: 
1) Smaller root system better supplied by limited retention. 2) Earlier bearing (2-3 years vs 5-7). 3) 
Shorter orchard life acceptable (12-15 years dwarf vs 30+ standard). 4) Higher density planting increases 
per-acre productivity. Dwarfs require intensive management but better adapted to low retention than vigorous 
standards.

QUALITY-YIELD CHALLENGES: Low retention produces: smaller fruit (100-125 count), reduced sugar (11-13 Brix 
vs 14-16), poor storage (2-4 months), severe physiological disorders (bitter pit universal without intensive 
foliar Ca). Fresh market quality marginal - consider processing varieties (applesauce, juice) with lower 
quality expectations. Intensive foliar nutrition helps but cannot fully compensate.

VIABILITY: Apple orchard establishment marginal in low-retention soils. Better alternatives: choose fruit 
crops better adapted to low fertility (peaches, plums - shorter-lived, less demanding) or implement multi-
year soil improvement before planting orchard. If establishing apples: dwarf rootstocks mandatory, fertigation 
strongly recommended, processing varieties more reliable than fresh market, expect 12-18 year orchard life, 
intensive annual inputs required.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes conventional apple orchard 
production non-viable. Long-term perennial nature (requiring 20-40 year sustained fertility) fundamentally 
incompatible with very-low-retention conditions. Young trees fail to establish properly - weak growth, high 
mortality, delayed bearing (8-12 years if ever). Mature trees severely deficient, short-lived (8-12 years), 
poor productivity.

MANAGEMENT IMPOSSIBILITY: No practical fertility system sustains apple orchards in very-low-retention soils. 
Intensive fertigation twice-weekly still produces deficiencies during critical periods (bloom, fruit set, 
early fruit development). Very sandy soils cannot buffer nutrition for trees' extended root zones and long 
seasonal demands. Orchard investment ($8,000-15,000/ac establishment) cannot be recovered with poor uncertain 
production.

ESTABLISHMENT FAILURE: Young apple trees require 3-5 years intensive care to reach bearing. In very-low-
retention soils, even with extreme inputs, trees: remain stunted (<4 ft growth vs 8-12 ft normal), develop 
multiple deficiency symptoms (N, K, Mg, Ca, B, Zn), show poor survival (30-50% loss vs <5% normal), never 
reach full bearing potential. Economic disaster - multi-year investment with no return.

ROOTSTOCK IRRELEVANT: Even ultra-dwarf rootstocks (M.27, extremely dwarfing) fail in very-low-retention. 
While dwarfs better than standards (less soil volume needed), they cannot overcome extreme deficiency. Dwarfs 
still require 8-12 years bearing life to recoup establishment costs - impossible to achieve in very-low-
retention.

ALTERNATIVES: DO NOT establish apple orchards in very-low-retention soils under any circumstances. Among 
worst possible fruit crop choices for extreme sandy conditions. Better alternatives: 1) Brambles (blackberries, 
raspberries - short-lived, lower demands, rapid returns). 2) Strawberries (perennial but short cycle, intensive 
but manageable). 3) Blueberries if pH acid (moderate demands, deep roots when established). 4) Annual vegetable 
crops (avoid long-term perennial investment). Among perennial fruit crops, apples one of WORST choices for 
very-low-retention soils."""
    },

    "Peaches": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports vigorous productive 
peach orchards (12-18 year economic life) with excellent tree health and fruit quality. Peaches have moderate 
to high annual needs (80-120 lb N, 40-80 lb P₂O₅, 100-150 lb K₂O/ac) but shorter orchard life than apples 
makes high retention less critical than for long-lived crops. Still, high retention optimizes production.

MANAGEMENT STRATEGY: Single early-season N application optimal: 80-120 lb N/ac applied 2-3 weeks before 
bloom (late winter/early spring). Early N timing supports: fruit set, shoot growth, leaf development. Late 
N (after May) promotes excessive vegetative growth, reduces fruit quality, delays maturity - avoid. K annually: 
100-150 lb K₂O/ac broadcast winter/early spring. P every 2-3 years: 40-80 lb P₂O₅/ac.

pH PREFERENCES: Peaches prefer slightly acid soil (pH 6.0-6.5). In high-retention soils with pH >6.8, 
monitor Fe, Mn, Zn - availability decreases at neutral/alkaline pH. Most high-retention soils have adequate 
pH but if naturally alkaline, sulfur acidification beneficial. Peaches more sensitive to high pH than apples 
- Fe chlorosis common above pH 7.5.

VIGOR MANAGEMENT: High retention supports vigorous growth but CAUTION - excessive vigor problematic for 
peaches. Overly vigorous trees: delayed bearing, dense canopy (poor light penetration, reduced fruit color/
sugar), increased disease (brown rot in dense canopy). Moderate N (80-100 lb/ac for bearing trees) maintains 
adequate vigor without excess. Terminal shoot growth 18-24 inches optimal.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC excellent for peach production. 
This retention level often OPTIMAL - provides adequate nutrition without excessive vigor that reduces fruit 
quality. Many premium peach regions have soils in this retention range balancing tree vigor and fruit quality.

MANAGEMENT STRATEGY: Standard single N application: 80-120 lb N/ac applied 2-3 weeks before bloom (February-
March depending on region). Early timing critical - supports fruit set and early growth without promoting 
late vegetative growth that reduces quality. K annually: 100-150 lb K₂O/ac for fruit size and quality. P 
annually or alternate years: 40-60 lb P₂O₅/ac.

FRUIT QUALITY: Good retention with proper N management produces excellent peach quality: good fruit size 
(2.5-3 inches diameter), excellent color (70-90% red blush), high sugar (12-15 Brix), firm flesh, good 
flavor. Adequate K critical for size and firmness. Ca for firmness and storage (though peaches not long-
stored like apples). B for fruit set. This retention level ideal for premium fresh market peaches.

YOUNG-TREE ESTABLISHMENT: Peaches establish faster than apples (bearing 2-4 years vs 3-6) and are somewhat 
less demanding during establishment. Good retention supports reliable establishment with standard fertility. 
First year: 0.5 lb N per tree monthly May-July. Second year: 0.75 lb N per tree monthly March-July. Third 
year: transition to per-acre rates as trees reach bearing.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC acceptable for peach production - 
actually can be ADVANTAGEOUS. Peaches moderately adapted to variable fertility: shorter-lived than apples 
(12-15 years vs 30+ years), natural annual renewal through heavy pruning, moderate demands manageable through 
intensive but short-term inputs. Many successful peach regions have moderate-retention soils.

MANAGEMENT STRATEGY: Split N program compensates for moderate retention: 60% late winter (2-3 weeks pre-
bloom) + 40% early summer (immediately post-harvest for early varieties, late June for mid/late varieties), 
total 100-140 lb N/ac. Two-split maintains availability through fruit development without excessive late 
vegetative growth. K split: 80 lb K₂O spring + 50 lb post-harvest, total 130 lb. P annually: 60-80 lb P₂O₅.

TREE LONGEVITY: Moderate retention reduces orchard life to 10-14 years vs 15-20 years optimal. However, 
peaches naturally short-lived compared to apples/pears - 12-15 years typical even in good soils. Moderate 
retention's modest life reduction less problematic for peaches than longer-lived fruit. Economic analysis 
shows acceptable returns over 10-12 year cycle.

VARIETY SELECTION: All peach types viable in moderate retention. Clingstone (processing) actually preferable 
for moderate fertility - less demanding of premium quality than fresh freestone. Consider: early varieties 
(shorter nutrient demand period), small-moderate tree size varieties (less total demand), disease-resistant 
varieties (stress from moderate fertility increases disease susceptibility).""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes peach production challenging 
but MORE VIABLE than apples at same retention level. Peaches' shorter life (12-15 years vs 30+ apples) and 
moderate demands make low retention more manageable - not long-term commitment. Still requires intensive 
management but economically feasible unlike apples.

MANAGEMENT STRATEGY: Three-split N: 50 lb late winter (pre-bloom) + 40 lb early summer (post-harvest early 
varieties or June drop for late) + 30 lb mid-summer (July), total 120 lb N/ac. More splits than good retention 
compensate for losses. K three-split: 60 + 45 + 45 = 150 lb K₂O/ac. P annually: 60-80 lb P₂O₅/ac banded if 
possible.

FERTIGATION OPTION: Drip or micro-sprinkler fertigation excellent for low-retention peaches. Biweekly 
injections 12-18 lb N/ac, 15-20 lb K₂O/ac during March-August growing season. Fertigation particularly 
beneficial for young tree establishment - more consistent nutrition speeds bearing, improves survival. 
Fertigation investment recovered through better production.

FRUIT-QUALITY IMPACTS: Low retention produces quality challenges: smaller fruit (2-2.5 inches), reduced 
color (<70% blush), lower sugar (10-12 Brix), softer flesh, variable maturity. Still commercially viable 
for processing (canning, frozen) where quality standards less stringent than fresh market. Consider clingstone 
processing varieties over fresh freestone - better economics at reduced quality.

VIABILITY: Peaches marginally viable for 250-400 bu/ac in low-retention soils. Among better fruit crop 
choices for low retention - moderate demands, relatively short commitment, manageable inputs. Economics 
marginal for fresh market (quality limitations) but viable for processing. Better than apples, pears, cherries 
at low retention. If growing tree fruit in low retention, peaches reasonable choice over longer-lived more-
demanding crops.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes peach production extremely 
difficult but STILL more viable than apples. Peaches' moderate demands and short life provide advantages 
over demanding long-lived fruits. However, even peaches' tolerance has limits - commercial production 
marginal to non-viable without extreme management.

MANAGEMENT OPTIONS: Intensive fertigation only viable approach: weekly injections 15-20 lb N/ac, 18-25 lb 
K₂O/ac for 20-25 weeks (March-August). P pre-plant: 80-100 lb P₂O₅/ac incorporated deeply. Or four-split 
program: N (35 + 30 + 30 + 25 = 120 lb/ac) and K (40 + 40 + 35 + 35 = 150 lb K₂O/ac) every 4-6 weeks during 
season.

ESTABLISHMENT CHALLENGES: Young peach trees struggle in very-low-retention soils: slow growth (3-5 ft vs 
6-10 ft normal first year), poor survival (20-40% loss), delayed bearing (4-6 years vs 2-3), weak root 
systems. Intensive first-year care: monthly fertigation or splits, consistent irrigation, pest/disease 
management. Economics questionable - high establishment costs with uncertain returns.

ORCHARD LIFE: Very short economic life in very-low-retention: 8-12 years vs 15-18 optimal. Trees decline 
rapidly after 8-10 years - reduced vigor, smaller fruit, increased disease, poor survival. Short life 
makes economic returns difficult - establishment costs amortized over fewer years. Requires higher annual 
returns to justify investment.

PROCESSING FOCUS: Fresh market peaches not viable - quality too poor (small fruit <2 inches, poor color, 
low sugar <10 Brix). Processing peaches (canning) marginally viable if: processor nearby (transportation 
costs critical), contract ensures acceptable prices, understanding of reduced yields/quality. Processing 
standards lower than fresh but still have minimum size/sugar requirements that may be difficult to meet.

VIABILITY: Peach production marginal in very-low-retention soils. Among less-bad choices for tree fruit 
in extreme conditions but still not recommended. Better alternatives: 1) Short-lived soft fruits (strawberries, 
brambles - 3-5 year cycle vs 12-15). 2) Annual crops avoiding perennial investment. 3) Soil improvement 
over 3-5 years before attempting fruit. If attempting peaches: fertigation mandatory, processing varieties 
only, expect 8-12 year life, intensive management required, economic viability questionable."""
    },

    "Strawberries": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports intensive strawberry 
production (20,000+ lb/ac) with excellent berry quality over 2-4 year productive life. Strawberries are 
HEAVY feeders for shallow-rooted perennial: 100-120 lb N, 60-80 lb P₂O₅, 120-150 lb K₂O/ac annually. Very 
high K demand critical for fruit quality - size, firmness, flavor, color. High retention maintains nutrients 
in root zone (top 6-12 inches).

MANAGEMENT STRATEGY: Split nutrients through season matching plant development stages. Establishment year 
(June-planted for following-year production): 40 lb N + 60 lb P₂O₅ + 60 lb K₂O/ac at planting, then 20 lb 
N + 30 lb K₂O/ac monthly July-September. Production years: 30 lb N + 40 lb K₂O/ac early spring (bud break), 
25 lb N + 40 lb K₂O/ac at bloom, 20 lb N + 40 lb K₂O/ac during harvest, 30 lb N + 30 lb K₂O/ac renovation 
(post-harvest), total 105 lb N and 150 lb K₂O/ac annually.

POTASSIUM CRITICAL: K most important nutrient for strawberry quality - affects size, firmness, flavor, 
color, shelf life. Adequate K (140-160 lb K₂O/ac) produces large firm berries with excellent flavor and 
3-5 day shelf life. Deficient K: small soft berries, poor flavor, <1 day shelf life, unmarketable. High 
retention maintains K availability through heavy fruiting period (4-6 weeks continuous harvest).

PRODUCTION SYSTEMS: Two main systems, both benefit from high retention. 1) Matted row: June-planted mother 
plants produce runners forming dense rows, heavy production year 2-3, then replant. 2) Annual plasticulture: 
September-planted bare-root or plugs, single-year production (April-June), intensive (raised beds, plastic 
mulch, drip irrigation), highest yields (25,000-30,000 lb/ac), premium quality. High retention supports 
either system excellently.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC supports productive strawberries 
(15,000-20,000 lb/ac) with good quality over 2-3 year cycle. Standard split nutrient program: establishment 
year (50 lb N + 60 lb P₂O₅ + 70 lb K₂O/ac at planting, then 20 lb N + 30 lb K₂O/ac monthly summer), production 
years (100-120 lb N + 140-160 lb K₂O/ac in 4 splits through season).

MANAGEMENT STRATEGY: Four-split program during production year: early spring (30 lb N + 40 lb K₂O), bloom 
(25 lb N + 40 lb K₂O), harvest (25 lb N + 40 lb K₂O), renovation (25 lb N + 35 lb K₂O). P pre-plant or 
annual spring application: 60-80 lb P₂O₅/ac. Good retention maintains availability through extended harvest 
(4-6 weeks) without excessive splits.

FERTIGATION: Drip irrigation common in modern strawberry production (plasticulture system). Fertigation 
through drip excellent approach for good-retention soils: weekly injections 10-15 lb N/ac, 12-18 lb K₂O/ac 
during active growth and fruiting. Precise nutrition control optimizes quality - especially important for 
high-value fresh market berries ($3-6/lb).

BORON ESSENTIAL: B critical for strawberry fruit set and development. Adequate B (1-2 lb/ac annually, split 
or foliar) ensures good pollination and seed set - critical since strawberry fruit development depends on 
seed number (more seeds = larger berries). B deficiency: small misshapen berries with reduced seed set. 
Apply B with spring pre-bloom fertilization.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for strawberries' 
heavy demands and shallow roots but MANAGEABLE with intensive plasticulture system. Matted row system less 
successful - 2-3 year cycle difficult to maintain adequate fertility. Annual plasticulture (raised beds, 
plastic mulch, drip) more reliable - intensive one-year production with heavy inputs.

MANAGEMENT STRATEGY: Plasticulture system: pre-plant (60 lb N + 80 lb P₂O₅ + 70 lb K₂O/ac incorporated 
into beds) + weekly fertigation (12-18 lb N/ac, 15-20 lb K₂O/ac, 20-25 weeks from planting through harvest). 
Total 300-400 lb N and 370-470 lb K₂O/ac in annual system - much higher than perennial but economic over 
single intensive season. Matted row (if attempted): five-split N-K annually plus heavy pre-plant P.

RAISED BEDS: Highly recommended for moderate-retention strawberries. Beds (6-8 inches high, 24-30 inches 
wide) provide: improved drainage (strawberries sensitive to wet conditions), warmer soil (early production), 
temporary retention improvement (bed soil mixture), easier harvest. Plastic mulch reduces weed competition, 
conserves moisture, keeps berries clean.

QUALITY IMPACTS: Moderate retention with intensive plasticulture produces good quality: medium to large 
berries (12-18 g), good firmness, acceptable flavor, 2-4 day shelf life. Not premium quality (20-25 g berries, 
5-7 day shelf life) but commercially viable. Adequate for local/regional markets, farmers markets, pick-
your-own operations. Premium long-distance shipping markets more challenging.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes traditional strawberry production 
extremely difficult. Strawberries' heavy demands (100-120 lb N/ac, 140-160 lb K₂O/ac) and shallow roots 
(6-12 inches) particularly challenged by low retention. Only viable approach: annual plasticulture system 
with raised beds using improved soil mix + intensive fertigation. Matted row system not recommended.

MANAGEMENT OPTIONS: Raised bed plasticulture only viable system: 1) Construct beds 8-10 inches high with 
imported soil mix (20-30% compost + native soil improving retention). 2) Pre-plant: 80 lb P₂O₅/ac incorporated 
into beds. 3) Fertigation: twice-weekly injections 15-20 lb N/ac, 18-25 lb K₂O/ac for 24-28 weeks. 4) Plastic 
mulch, drip irrigation mandatory. Single-season intensive production avoids multi-year fertility management.

SOIL MIX CRITICAL: Native low-retention soil insufficient for strawberry root zone. Amended beds with 20-
30% compost by volume provide: temporary retention improvement, better water-holding capacity, improved 
structure, initial nutrient source. Mix thoroughly before forming beds. Compost provides 3-6 month retention 
improvement adequate for annual production cycle. Cost: $1,500-2,500/ac but essential for viability.

QUALITY-YIELD CHALLENGES: Low retention produces moderate quality and yields even with intensive system: 
yields 8,000-12,000 lb/ac (vs 15,000-25,000 optimal), medium berries (10-15 g), moderate firmness (2-3 day 
shelf life), variable flavor. Adequate for local direct markets (farmers markets, pick-your-own, CSA) but 
not wholesale shipping markets. Economics marginal - high input costs vs moderate yields.

VIABILITY: Strawberries marginally viable in low-retention soils only with plasticulture system, raised 
beds with compost amendment, and intensive fertigation. Economics marginal - high establishment costs 
($4,000-7,000/ac including drip, plastic, compost, plants), intensive management, moderate returns. Better 
opportunities: local direct sales (farmers markets, pick-your-own - premium prices offset costs), or choose 
less demanding crops. Among berries, strawberries MORE viable than brambles at low retention (brambles even 
more demanding).""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes strawberry production in native 
soil non-viable. Strawberries' extreme demands (shallow roots accessing only top 6-12 inches, heavy K needs, 
extended production season) cannot be met in very-low-retention conditions even with intensive fertigation. 
Only option: complete growing media replacement in raised beds - essentially container production in ground.

MANAGEMENT REQUIREMENT: Total soil replacement raised bed system: 1) Construct beds 10-12 inches high. 2) 
Fill completely with purchased potting mix or custom blend (50% compost + 30% peat/coir + 20% native soil 
for stability). 3) Drip irrigation + fertigation (twice-weekly injections). 4) Plastic mulch. Growing entirely 
in imported media avoiding retention limitations. Cost: $3,500-6,000/ac for media alone.

FERTIGATION INTENSIVE: Twice-weekly injections mandatory through imported media: 18-25 lb N/ac, 20-30 lb 
K₂O/ac for 26-30 weeks (planting through harvest). Media chosen for good retention but still requires frequent 
fertigation due to shallow root zone and limited soil volume in beds. Total season: 230-300 lb N, 260-390 
lb K₂O/ac - higher than normal due to leaching even from improved media.

ECONOMICS CRITICAL: Total production costs extremely high: imported media ($3,500-6,000/ac), drip system 
($1,200-2,000/ac), plastic mulch ($400-800/ac), plants ($1,500-2,500/ac), fertigation ($600-1,000/ac) = 
$7,200-11,300/ac establishment. Must produce 12,000-18,000 lb/ac at $2.50-4.00/lb to break even. Only 
viable with: direct-market premium prices, excellent production skills, perfect execution. Very high risk.

ALTERNATIVE APPROACH: True container production (above-ground pots, hanging baskets, vertical systems) may 
be MORE economical than in-ground raised beds with imported media. Advantages: complete environmental control, 
movable for weather protection, easier harvesting (elevated), same media costs but better utilization. 
Consider container systems instead of in-ground if attempting strawberries in very-low-retention conditions.

VIABILITY: Strawberries not recommended in very-low-retention native soils. IF attempting: complete media 
replacement in raised beds or container production only viable approaches. Economics extremely challenging - 
requires premium pricing, direct sales, expert production. Better alternatives: choose entirely different 
crops adapted to sandy soils, or implement multi-year soil improvement program before attempting intensive 
specialty crops like strawberries. Among berry crops, strawberries WORST choice for very-low-retention 
conditions - most demanding of sustained high fertility in shallow root zone."""
    },

    "Blueberries": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100) BUT pH ABSOLUTELY CRITICAL - must be 
ACID (4.5-5.5). High CEC at proper acid pH supports vigorous productive blueberry plantings (20-30+ year 
life) with yields 12,000-18,000 lb/ac. High OM (>4%, typically amended with pine bark/peat) essential for 
moisture retention and acidity maintenance. Blueberries have LOW to MODERATE needs (50-80 lb N, 40-60 lb 
P₂O₅, 60-80 lb K₂O/ac) BUT demand specific conditions.

MANAGEMENT STRATEGY: Split N in acidifying forms only: ammonium sulfate (21-0-0-24S) preferred, supplying 
N + S maintaining acidity. Apply 40% early spring (bud break), 35% post-bloom (May), 25% early summer 
(June), total 50-80 lb N/ac depending on bush age and vigor. K as potassium sulfate (0-0-50-17S) preferred 
over KCl: 60-80 lb K₂O/ac split with N. P: 40-60 lb P₂O₅/ac annually using triple superphosphate or phosphoric 
acid (acidifying).

pH MAINTENANCE: Even with high retention and naturally acid pH, monitor pH annually - lime applications to 
adjacent crops, irrigation water alkalinity, or natural pH drift can slowly raise pH above 5.5 causing SEVERE 
Fe chlorosis. Apply elemental sulfur (200-400 lb/ac) if pH trends above 5.3. Sulfur acidifies slowly - apply 
fall before problem severe. Pine bark mulch (3-4 inches deep, replenished biannually) maintains acidity and 
adds OM.

NITROGEN FORM: Blueberries prefer/require ammonium-N (NH₄⁺), cannot efficiently use nitrate-N (NO₃⁻). Use 
ONLY ammonium or urea forms: ammonium sulfate, urea (will convert to NH₄⁺ in acid soil), or specialty 
blueberry fertilizers. Never use calcium nitrate, sodium nitrate, or other nitrate sources - blueberries 
cannot take up these forms efficiently.""",
        
        "High": """Good nutrient retention (SQ2: 60-79) IF pH 4.5-5.5 (CRITICAL). Moderate to high CEC at 
proper acid pH supports excellent blueberry production (10,000-15,000 lb/ac) over 20-25 year planting life. 
Many premium blueberry regions have soils in this retention range with naturally acid pH or careful 
acidification management. High OM (pine bark mulch/amendments) essential for shallow fibrous root systems.

MANAGEMENT STRATEGY: Standard split N program using acidifying fertilizers: 50-80 lb N/ac split 40% spring 
+ 35% post-bloom + 25% early summer, all as ammonium sulfate. K as potassium sulfate: 60-80 lb K₂O/ac split 
with N. P annually: 40-60 lb P₂O₅/ac as triple superphosphate or rock phosphate (gradually available in 
acid conditions). Annual soil test monitors pH - maintain 4.5-5.5 with sulfur as needed.

ORGANIC MATTER: Blueberries require high OM (>3%) for moisture and nutrient retention in shallow root zone 
(top 18-24 inches). Pine bark mulch (3-4 inches deep) provides: acidity maintenance, moisture conservation, 
OM addition as decomposes, weed suppression, cooler soil (blueberries benefit from cool roots). Replenish 
mulch every 2-3 years. If native OM low, pre-plant incorporation of pine bark or peat (20-30% by volume to 
2 ft depth) improves long-term conditions.

YOUNG-BUSH ESTABLISHMENT: Blueberries slow to establish (3-5 years to full production) requiring sustained 
proper conditions. Good retention at proper pH supports steady establishment. Years 1-2: light N only (0.25-
0.5 lb/bush), focus on root development. Years 3-4: increase to 0.75-1.0 lb N/bush. Year 5+: full per-acre 
rates as planting reaches maturity.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59) IF pH 4.5-5.5 managed carefully. Moderate CEC 
acceptable for blueberries with intensive pH management - blueberries' LOW to MODERATE nutrient needs more 
easily met than high-demand crops. However, pH maintenance MORE CHALLENGING at moderate retention - buffering 
capacity lower, pH can shift more easily. Annual sulfur applications likely needed.

MANAGEMENT STRATEGY: Split N: 60-90 lb N/ac in three applications (all as ammonium sulfate), higher than 
high-retention to compensate for leaching. K split: 70-90 lb K₂O/ac as potassium sulfate. P annually: 50-
70 lb P₂O₅/ac. Sulfur for pH: apply 300-600 lb elemental sulfur/ac annually to maintain pH <5.5 in moderate-
retention soils (they buffer less, acidify more easily than high-retention but also lose acidity faster).

pH-ACIDIFICATION CHALLENGE: If native pH >6.0, acidification to 4.5-5.5 requires 2-4 tons sulfur/ac applied 
over 2-3 years before planting. Moderate-retention soils acidify relatively quickly (6-18 months per ton 
sulfur vs 12-24 months in high retention) but also lose acidity faster requiring annual maintenance. Consider 
raised beds with acid mix if native pH >7.0 - field acidification uncertain at moderate retention with 
alkaline starting point.

PINE BARK ESSENTIAL: Heavy pine bark mulch (4-6 inches deep) more critical in moderate retention than high 
- provides temporary retention improvement in root zone plus acidity maintenance. Replenish annually vs 
biennial in high retention. Consider pre-plant pine bark incorporation (30-40% by volume to 2 ft depth) for 
long-term improvement - significant cost ($2,000-4,000/ac) but improves retention and acidity simultaneously.

VARIETY SELECTION: All blueberry types viable if pH managed: highbush (northern, southern), rabbiteye, 
half-high. Southern highbush and rabbiteye somewhat more tolerant of marginal conditions - consider these 
if region appropriate. Rabbiteye generally more vigorous and adapted to challenging conditions including 
moderate retention, though still requires acid pH.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes blueberry production challenging 
primarily due to pH management difficulty not nutrient supply - blueberries' LOW nutrient needs manageable 
even in low retention, but maintaining stable acid pH extremely difficult. If naturally acid pH (4.5-5.5), 
blueberries VIABLE with proper management. If alkaline pH (>6.5), DO NOT ATTEMPT - acidification cost-
prohibitive and unstable.

MANAGEMENT STRATEGY: If naturally acid: three to four-split N (70-100 lb N/ac total, all ammonium sulfate), 
K split similarly (80-100 lb K₂O/ac as potassium sulfate), P annually (60-80 lb P₂O₅/ac). Monitor pH 
quarterly - low retention allows rapid pH shifts. Apply sulfur at first indication of pH rise (>5.3). Pine 
bark mulch (4-6 inches, replenished annually) essential for retention improvement and acidity.

NATURALLY ACID ADVANTAGE: Low-retention soils are typically sandy and frequently NATURALLY ACID (pH 4.5-
5.5 common in pine-forested sandy soils of Southeast). If so, blueberries excellent choice - pH already 
optimal, low retention manageable for low-demand crop. Southeast has extensive blueberry industry on sandy 
acid soils (low retention but naturally ideal pH). Blueberries better adapted to low-retention acid sands 
than most fruit crops.

ALKALINE SOIL: If pH >6.5 (alkaline), blueberries NOT RECOMMENDED. Acidification extremely difficult: 
requires 3-6 tons sulfur/ac applied over 3-5 years, even then pH stability questionable in low-buffering 
soil (can shift back toward alkaline). Cost $1,500-3,000/ac for acidification alone with uncertain success. 
Better to choose crops adapted to alkaline rather than extreme modification attempts.

RAISED BEDS: Consider raised beds (8-12 inches high) filled with acid mix (40% pine bark + 40% peat + 20% 
sand) if native pH unsuitable. Provides complete control of root environment. Cost $3,500-6,000/ac for 
materials but ensures proper conditions for 20-25 year planting life. Economics viable for blueberries' 
high value ($2-4/lb wholesale) and long productivity.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC but blueberries STILL VIABLE if pH 
naturally acid (4.5-5.5). Blueberries unique among fruit crops - LOW nutrient demands manageable even in 
very-low-retention IF acid conditions exist naturally. Very sandy acid pine forest soils (common Southeast 
US) ideal for blueberries despite minimal retention. If alkaline pH, production non-viable.

MANAGEMENT OPTIONS: If naturally acid sandy soil: intensive split fertigation strongly recommended. Drip 
irrigation + biweekly injections 8-12 lb N/ac (as ammonium sulfate solution), 8-12 lb K₂O/ac (as potassium 
sulfate solution) for 15-20 weeks (April-August). P pre-plant: 60-80 lb P₂O₅/ac incorporated. Pine bark 
mulch (6 inches deep, replenished annually) provides critical retention improvement in root zone.

SOUTHEASTERN MODEL: Extensive commercial blueberry industry thrives on very-low-retention acid sandy soils 
of North Carolina, Georgia, Florida, Mississippi. These soils (pH 4.5-5.5 naturally, essentially pure sand, 
CEC <5) produce excellent blueberries (12,000-15,000 lb/ac) with proper irrigation and fertigation. Proof 
that blueberries well-adapted to extreme sandy conditions IF acid pH present.

DEEP ROOTS: Mature blueberry bushes develop surprisingly deep roots (4-6 ft) for shallow-rooted reputation. 
Deep rooting helps access moisture and nutrients below surface in very sandy soils. Takes 4-6 years to 
develop deep system - critical to maintain plants through establishment with intensive shallow-fertigation 
until deep roots develop.

ALKALINE SOIL: If pH >7.0, blueberries IMPOSSIBLE. Acidification of very-low-retention alkaline soil not 
viable - requires enormous sulfur quantities (5-10+ tons/ac) applied over many years with uncertain success. 
Even with acidification, pH will fluctuate rapidly (minimal buffering). Costs prohibitive relative to any 
possible returns. Choose entirely different crops or construct raised bed systems with complete soil 
replacement.

VIABILITY: Blueberries highly viable in very-low-retention soils IF naturally acid pH (Southeast sandy 
soils). Among BEST fruit crop choices for extreme sandy acid conditions - low nutrient demands, deep eventual 
rooting, high value, long productivity. If pH naturally acid: excellent choice with irrigation and fertigation. 
If pH neutral/alkaline: impossible without complete soil replacement in raised beds (cost-prohibitive for 
field scale). Blueberry viability entirely pH-dependent not retention-dependent."""
    },

    "Grapes": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports vigorous productive 
vineyards (25-30+ year life) BUT CAUTION - excessive fertility, especially N, promotes vegetative growth at 
expense of fruit quality. For wine grapes, MODERATE fertility often better than high. Table grapes benefit 
from high retention for maximum production (15-20 tons/ac) but wine grapes often produce best quality at 
moderate vigor (5-8 tons/ac).

MANAGEMENT STRATEGY: RESTRAINED fertility for wine grapes: 40-60 lb N/ac annually (much lower than most 
crops despite high retention), split 60% early spring (bud break) + 40% post-bloom. K: 80-100 lb K₂O/ac for 
fruit quality, color, sugar. P every 2-3 years: 30-50 lb P₂O₅/ac. High retention allows minimal inputs - 
wine grape quality improved by controlled moderate nutrition rather than maximum fertility.

TABLE vs WINE: Table grapes (fresh eating) benefit more from high retention and higher inputs: 80-120 lb 
N/ac for large attractive clusters, 120-150 lb K₂O/ac for large berries and color. Wine grapes require 
MUCH lower inputs: excess N delays ripening, reduces sugar concentration, alters wine character negatively. 
High retention excellent for table grapes, potentially problematic for wine grapes unless N carefully 
controlled.

DEEP ROOTING: Mature grapevines extremely deep-rooted (6-12+ ft) accessing nutrients throughout profile. 
High-retention subsoils maintain nutrients below surface for deep roots. This allows minimal surface 
fertilization - roots forage widely and deeply. Over-fertilization produces excessive vegetative growth 
(canopy density, delayed maturity, reduced fruit quality) rather than improved yield/quality.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC often IDEAL for wine grape 
production - provides adequate nutrition without excess vigor that reduces quality. Many premier wine regions 
(Napa, Sonoma, Bordeaux, Burgundy) have soils in this retention range balancing vine vigor and fruit quality. 
Table grape production also excellent with proper management.

MANAGEMENT STRATEGY: Wine grapes: restrained program of 40-80 lb N/ac split 60% spring + 40% post-bloom, 
80-120 lb K₂O/ac for quality, P every 2-3 years (30-50 lb P₂O₅/ac). Table grapes: heavier program of 100-
140 lb N/ac split similarly, 120-160 lb K₂O/ac for size and appearance, P annually or alternate years. Good 
retention allows somewhat flexible scheduling - less precision required than low retention.

WINE QUALITY: This retention level produces excellent wine grapes: moderate vine vigor (balanced vegetative/
reproductive growth), good crop load (3-6 tons/ac), high sugar accumulation (22-26 Brix), concentrated 
flavors, balanced acids. Excessive fertility (high-retention with heavy fertilization) produces: large 
clusters, dilute flavors, lower sugar, herbaceous character - poor wine quality despite high yields. Good 
retention with moderate inputs optimal.

SUSTAINABILITY: Grapes' deep roots, perennial nature, and moderate needs make viticulture sustainable in 
good-retention soils with minimal inputs. Cover crops (legumes, grasses) between rows provide: N contribution 
(30-60 lb N/ac from legumes), OM addition, erosion control, improved soil structure. Well-managed vineyard 
improves retention over time through OM additions from cover crops and pruning residues.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC acceptable to preferred for many 
wine grape varieties - grapes relatively TOLERANT of moderate fertility. Deep rooting (6-12 ft when established) 
accesses nutrients from large soil volume. Wine quality can be excellent at moderate fertility - some premium 
wine regions have moderate-retention soils producing outstanding wines from controlled moderate vigor.

MANAGEMENT STRATEGY: Wine grapes: 60-100 lb N/ac split 50% spring + 30% post-bloom + 20% mid-summer (three 
splits vs two in higher retention), 100-140 lb K₂O/ac split 70% spring + 30% mid-summer. P annually: 40-60 
lb P₂O₅/ac (moderate retention requires annual vs alternate-year). Table grapes: 120-160 lb N/ac in three 
splits, 140-180 lb K₂O/ac split similarly.

VINE SPACING: Consider higher-density planting (closer vine spacing) in moderate-retention soils. Benefits: 
1) Smaller vines better supplied by limited retention. 2) Easier to manage uniform ripening. 3) Higher per-
acre productivity from more vines. 4) Labor-efficient modern trellising (vertical shoot positioning). Density 
1,200-1,800 vines/ac vs 700-1,000 traditional wider spacing.

VARIETY-ROOTSTOCK: All wine grape varieties viable. However, less-vigorous varieties (Pinot Noir, Merlot) 
may be better suited than extremely vigorous types (Concord, some hybrids). Rootstock selection critical - 
choose moderate-vigor rootstocks (3309C, 101-14) rather than high-vigor (110R, 1103P). Rootstock-scion 
combination determines vine vigor more than soil fertility - proper selection compensates for moderate 
retention.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes grape production challenging 
but VIABLE - grapes among more adaptable fruit crops to difficult conditions. Deep rooting when established 
(6-10 ft) helps access nutrients below poor surface. Wine grape quality can be acceptable to good at low 
fertility - vine stress from limited nutrients sometimes improves concentration and character. Table grapes 
more challenging - appearance and size requirements difficult.

MANAGEMENT STRATEGY: Wine grapes: four-split N (35 + 30 + 25 + 20 = 110 lb N/ac at bud break, post-bloom, 
mid-season, late season), K split quarterly (35 + 35 + 30 + 30 = 130 lb K₂O/ac), P annually (50-70 lb 
P₂O₅/ac banded if possible). Table grapes: similar splits but higher rates (140-180 lb N, 160-200 lb K₂O). 
Fertigation recommended if drip irrigation installed - biweekly injections provide more consistent nutrition.

ESTABLISHMENT CHALLENGE: Young vines struggle more in low-retention than established mature vines - takes 
4-6 years to develop deep root systems accessing nutrients below surface. First 3-4 years critical: monthly 
fertigation or frequent light applications support establishment. Once deeply rooted (year 5+), vines better 
able to tolerate low retention accessing subsoil reserves.

WINE vs TABLE: Wine grapes MORE viable than table grapes at low retention. Wine grape quality acceptable 
to excellent from stressed low-vigor vines on poor soils (concentrated flavors, good structure, balanced). 
Table grapes struggle - small clusters, small berries, poor appearance fail market standards. If growing 
grapes in low retention, focus on wine varieties not table types.

VIABILITY: Wine grapes viable for 3-6 tons/ac in low-retention soils - some premium wine regions have low-
retention soils producing outstanding quality from low yields. Economics depend on wine type: premium wine 
varieties (Pinot Noir, Cabernet) viable at low yields if quality excellent, bulk wine varieties need higher 
yields. Table grapes marginal - quality limitations reduce marketability. Grapes reasonable choice for low-
retention if focusing on quality wine production.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes grape production extremely 
challenging but grapes MORE tolerant than most fruit crops due to deep rooting and perennial nature. Commercial 
production marginal but some historic wine regions have very-low-retention sandy soils (Médoc region Bordeaux, 
some California AVAs) producing excellent wines from stressed vines on poor soils.

MANAGEMENT OPTIONS: Intensive fertigation only viable approach: biweekly injections 12-18 lb N/ac, 15-20 
lb K₂O/ac for 20-25 weeks (bud break through véraison). P pre-plant incorporated deeply: 60-80 lb P₂O₅/ac. 
Annual P surface applications: 40-60 lb P₂O₅/ac. Drip irrigation mandatory - very sandy soils cannot support 
vines without consistent moisture management. Fertigation piggybacks on required irrigation.

ESTABLISHMENT CRITICAL: First 4-6 years most challenging - young vines with shallow roots severely stressed 
by very low retention. Intensive management (monthly fertigation or light applications, consistent irrigation, 
careful pest/disease control) essential to establish deep root systems. After establishment (year 6+), mature 
vines with 8-12 ft roots more tolerant accessing subsoil moisture/nutrients.

WINE QUALITY PARADOX: Very-low-retention soils can produce EXCELLENT wine quality from severely stressed 
low-vigor vines. Stress produces: small clusters, small berries (high skin-to-pulp ratio concentrating 
flavors/tannins), intense flavors, complex character. Yields very low (2-4 tons/ac) but wine quality can 
be outstanding. Economic viability depends on producing premium wines commanding high prices ($30-100+/bottle) 
justifying low yields.

TABLE GRAPES: Not viable in very-low-retention soils. Table grapes require: large attractive clusters, 
large berries, uniform appearance, high yields (12-20 tons/ac). None achievable in extreme sandy conditions. 
Stressed vines produce small tight clusters, tiny berries, variable appearance - completely unmarketable for 
fresh consumption. Only wine grapes have any viability.

VIABILITY: Wine grapes marginally viable for 2-5 tons/ac in very-low-retention soils with intensive 
irrigation/fertigation. Economics dependent on producing premium wines from low yields - boutique winery 
model potentially viable, commodity production impossible. Historic precedent: some famous wine regions have 
poor soils producing outstanding quality. Modern challenge: intensive management costs (irrigation, fertigation) 
may exceed traditional dry-farmed stressed-vine systems. Consider wine grapes only if: committed to premium 
quality over quantity, irrigation available, boutique marketing plan, understanding that first 5-10 years 
establishment phase before production."""
    },

    "Almonds": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports highly productive almond 
orchards (3,000-4,000 lb/ac) over 25-30 year life. Almonds have VERY HIGH annual needs - among highest of 
tree crops: 200-300 lb N, 50-80 lb P₂O₅, 200-300 lb K₂O/ac annually for mature bearing orchards. Massive 
nutrient demands for heavy nut production (mature trees can produce 60-100 lb nuts/tree). High retention 
critical for economic fertilizer efficiency.

MANAGEMENT STRATEGY: Split N through season matching tree uptake: 40% late winter/early spring (February-
March, before bloom), 30% post-bloom (April-May), 30% post-harvest (August-September for next year's bud 
development). Total 200-300 lb N/ac depending on yield goals and tree vigor. K similar timing: 200-300 lb 
K₂O/ac split 50% spring + 50% post-harvest. P annually: 50-80 lb P₂O₅/ac broadcast or banded in tree row.

POTASSIUM CRITICAL: Almonds among highest K-demanding tree crops - heavy nut production removes massive K 
(250-300 lb K₂O/ac annually at 3,000+ lb yield). Adequate K essential for: nut size, kernel quality, hull 
split timing, tree health and longevity. K deficiency produces: small nuts, poor kernel fill, delayed/poor 
hull split, premature tree decline. High retention maintains K availability through long season and heavy 
removal.

BORON ESSENTIAL: B extremely critical for almond pollination and nut set - B deficiency major yield limiter. 
Apply 2-3 lb B/ac annually: soil application (1-2 lb/ac) early spring + foliar spray (0.5-1 lb/ac) at pink/
bloom stage. Adequate B ensures good pollen viability, fruit set, embryo development. Hull rot (fungal 
disease) risk increases under B deficiency stress.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC adequate for productive almond 
orchards (2,500-3,500 lb/ac) with intensive annual fertility. Almonds' extreme demands require heavy 
fertilization even from good baseline - among most nutrient-demanding commercial tree crops. Split applications 
essential despite good retention due to massive uptake during nut development.

MANAGEMENT STRATEGY: Three-split N: 40% late winter (February-March) + 35% post-bloom (May) + 25% post-
harvest (August), total 220-320 lb N/ac (higher than high-retention to maintain adequacy). K three-split: 
40% February + 35% May + 25% August, total 220-320 lb K₂O/ac. P annually: 50-80 lb P₂O₅/ac - cannot skip 
years in almonds given high P removal. Annual soil testing plus leaf tissue analysis (July sampling) guide 
adjustments.

FERTIGATION: Increasingly common in modern almond production, especially beneficial in good-retention soils 
supporting intensive management. Microsprinkler or drip irrigation + biweekly N-K injections provide precise 
nutrition matching tree demand. Fertigation schedule: 15-20 lb N/ac + 18-25 lb K₂O/ac per injection, 12-16 
injections (March-August). Total via fertigation comparable to split granular but better timing/efficiency.

ZINC CRITICAL: Zn deficiency common and yield-limiting in almonds. Symptoms: small terminal leaves (rosette 
appearance), shortened internodes, reduced nut set. Annual Zn applications essential: 10-15 lb Zn/ac soil-
applied fall or 2-3 foliar sprays (Zn sulfate 0.25-0.5 lb Zn/100 gal) during growing season. Tissue analysis 
monitors Zn status - maintain >15 ppm leaf Zn.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC extremely challenging for almonds' 
massive nutrient demands. Among most demanding tree crops with long production cycle (25+ years), almonds 
struggle at moderate retention. Young tree establishment slow (8-12 years to full bearing vs 5-7 optimal). 
Mature productivity reduced (1,800-2,500 lb/ac). Economics marginal - decades of intensive inputs with 
uncertain returns.

MANAGEMENT STRATEGY: Intensive four-split or fertigation mandatory. Four-split: N (80 + 70 + 60 + 50 = 260 
lb N/ac at February, April, June, August), K (75 + 70 + 65 + 60 = 270 lb K₂O/ac similarly split), P annually 
(60-80 lb P₂O₅/ac banded). Fertigation preferable: biweekly injections 18-25 lb N/ac + 20-30 lb K₂O/ac for 
16-20 weeks. Fertigation provides more consistent nutrition reducing stress from moderate retention.

ESTABLISHMENT CHALLENGES: Young almonds extremely vulnerable in moderate retention - slow growth, poor vigor, 
delayed bearing extend non-productive period to 8-12 years (vs 5-7 years optimal). Extended establishment 
increases financial burden - carrying costs accumulate over extra years before revenue. Many growers cannot 
sustain 8-12 year non-productive investment - orchards abandoned before reaching productivity.

NUT-QUALITY IMPACTS: Moderate retention affects marketable quality: smaller nuts (<18-20 mm kernel length, 
below premium size), lower kernel percentage (kernel weight as % of in-shell, <35% vs 40-45% optimal), 
poor fill (shriveled kernels), increased blanks (no kernel development). Quality problems reduce value - 
price differential 20-40% for small/poor-quality vs premium large well-filled nuts.

VIABILITY: Almond production marginal to non-viable in moderate-retention soils. Almonds require excellent 
fertility for economic production over 25+ year cycle. Better alternatives: tree crops better adapted to 
moderate fertility (apples, peaches - lower demands, shorter cycles, more forgiving) or avoid permanent 
orchards (focus on annual/short-lived crops). If considering almonds: understand economics marginal, expect 
reduced yields/quality, intensive management decades, uncertain profitability.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes almond production economically 
IMPOSSIBLE. Almonds' extreme demands (200-300 lb N, 200-300 lb K₂O/ac annually) over 25-30 year orchard 
life cannot be sustained from poor baseline despite any fertilization intensity. Young trees fail to establish 
- orchards never reach viable productivity. DO NOT attempt almond production in low-retention soils.

ESTABLISHMENT FAILURE: Young almond trees require 5-8 years intensive care (optimal conditions) to reach 
bearing. In low-retention soils, trees: remain severely stunted (<4 ft vs 12-18 ft optimal), develop multiple 
persistent deficiency symptoms (N, K, Zn, B, Fe), experience high mortality (30-60% vs <5%), never develop 
adequate framework for nut production. Decade+ of investment with zero return - financial disaster.

MATURE-TREE IMPOSSIBILITY: Even if trees somehow survive establishment, cannot produce commercial nut crop. 
Almonds require massive sustained nutrition during nut development (April-July): inadequate nutrition produces 
blanks (no kernel), hull rot (disease from stress), early drop, tiny nuts. Low retention cannot buffer these 
demands even with intensive fertigation. Attempted orchards produce <1,000 lb/ac (vs 2,500-3,500 viable) 
of poor-quality unmarketable nuts.

ECONOMIC CATASTROPHE: Almond orchard establishment costs $8,000-15,000/ac (trees, irrigation, trellising, 
land preparation). Carrying costs during non-bearing years (8-12+ in low retention) accumulate to $15,000-
25,000/ac. Revenue from poor production (<1,000 lb/ac at $2-3/lb) = $2,000-3,000/ac annually. Cannot recover 
establishment costs over any reasonable timeframe. Among worst agricultural investments possible.

ALTERNATIVES: Absolutely DO NOT attempt almond production in low-retention soils. Choose: 1) Crops adapted 
to low fertility (forages, certain vegetables). 2) Shorter-lived less-demanding tree fruits if committed to 
perennials (peaches, plums - still challenging but less impossible than almonds). 3) Non-agricultural land 
uses. Almonds require excellent deep fertile soils - fundamental requirement not negotiable. Among all tree 
crops, almonds one of WORST choices for low retention.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes almond production completely 
IMPOSSIBLE under any circumstances. Almonds' extreme demands over multi-decade production cycle fundamentally 
incompatible with very-low-retention conditions. Attempting almond orchard in very-low-retention soil 
guaranteed economic disaster. DO NOT ATTEMPT.

COMPLETE FAILURE: Almond trees cannot survive establishment in very-low-retention soils regardless of 
management intensity. Young trees: die within 1-3 years (60-90% mortality), show severe deficiencies of 
multiple nutrients simultaneously (N, K, Ca, Mg, Zn, B, Fe), never develop adequate root systems, remain 
<2 ft tall, never approach bearing. Mature trees: non-existent - orchards fail completely before trees 
mature.

MANAGEMENT FUTILITY: No management system provides adequate nutrition. Intensive fertigation twice-weekly 
still produces severe deficiencies - very sandy soils cannot buffer nutrients for large trees with extensive 
root zones and long seasonal demands. Attempting to fertigate entire orchard (acres of trees) economically 
impossible - labor and materials costs exceed any possible returns by orders of magnitude.

INVESTMENT DISASTER: Complete loss of entire establishment investment ($10,000-15,000+/ac). No revenue 
ever generated - trees die before bearing any nuts. Worse agricultural investment than even attempting annual 
vegetables in very low retention - at least vegetables might produce something first year. Almonds require 
5+ years before any production - those years never reached. Total economic catastrophe.

IMPOSSIBILITY: Almond production not merely difficult but COMPLETELY IMPOSSIBLE in very-low-retention soils. 
Physical/biological impossibility not just economic challenge. No amount of inputs, technology, or management 
enables almond survival and production. Almonds require excellent deep fertile soils as absolute prerequisite 
- most soil-demanding common tree crop in temperate agriculture. If soil has very low retention, choose 
literally any other crop - all better choices than almonds."""
    },

    "Walnuts": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports vigorous productive 
walnut orchards (3,500-4,500 lb in-shell/ac) over extremely long life (50-75+ years). Walnuts have VERY 
HIGH annual needs: 200-250 lb N, 40-60 lb P₂O₅, 150-200 lb K₂O/ac for mature bearing trees. These massive 
long-lived trees (can reach 60-80 ft tall, 50-60 ft wide, living 100+ years) demand sustained excellent 
fertility over multi-decade to century-scale production.

MANAGEMENT STRATEGY: Split N matching walnut's uptake pattern: 50-60% early spring (March-April, catkin/
leaf emergence), 40-50% early summer (May-June, nut sizing). Total 200-250 lb N/ac for mature bearing 
orchards. K annually: 150-200 lb K₂O/ac, can apply entirely spring or split 60% spring + 40% summer. P 
every 2-3 years: 40-60 lb P₂O₅/ac (high retention allows biennial applications). Deep rooting (12-20 ft) 
allows trees to access subsoil nutrients.

ZINC ABSOLUTELY CRITICAL: Walnuts THE most Zn-responsive tree crop - Zn deficiency major yield limiter. 
Deficiency symptoms: stunted terminals, rosette appearance, bronzed small leaves, very small nuts, poor 
kernel development. Annual Zn applications mandatory: 15-25 lb Zn/ac soil-applied (fall/winter) OR 3-4 
foliar sprays (Zn sulfate 3-5 lb Zn/100 gal) during growing season. Many walnut soils naturally Zn-deficient 
- supplementation essential regardless of retention.

LONGEVITY: High-retention soils support walnuts' extremely long productive life - 50-75+ years common, some 
orchards 100+ years continuously productive. This makes soil quality absolutely critical - decisions regarding 
retention/fertility affect production for multiple human generations. Walnut orchard planting multi-
generational investment requiring best possible soils.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC supports productive long-lived 
walnut orchards (3,000-4,000 lb/ac) for 40-60 years. Standard intensive fertility program: 200-250 lb N/ac 
split 50% spring + 50% early summer, 150-200 lb K₂O/ac split or entirely spring, P 40-60 lb P₂O₅/ac annually 
or alternate years depending on soil test.

MANAGEMENT STRATEGY: Two-split N standard: 100-125 lb at catkin emergence (March-April) + 100-125 lb at 
nut sizing (May-June). Good retention maintains N through nut development period but splits optimize uptake 
during peak demand windows. K application timing less critical - can broadcast 150-200 lb K₂O/ac entirely 
spring or split 60% spring + 40% summer. Annual soil tests plus leaf analysis (mid-July sampling) guide 
fertility adjustments.

YOUNG-TREE ESTABLISHMENT: Walnuts extremely slow to bearing (8-12 years first crop, 15-20 years full 
production). Long non-productive period demands sustained fertility supporting tree development. Good retention 
maintains fertility through establishment years. Years 1-3: 0.25-0.5 lb N per tree, monthly April-July. 
Years 4-6: 0.75-1.5 lb N per tree monthly. Years 7-10: 2-4 lb N per tree monthly. Year 10+: transition to 
per-acre rates as orchard matures.

ZINC PROGRAMS: Annual Zn applications essential - walnuts extremely Zn-responsive. Two approaches: 1) Soil 
application: 15-25 lb Zn/ac (zinc sulfate) broadcast fall/winter, incorporated by rain/irrigation. 2) Foliar 
program: 3-4 sprays (3-5 lb Zn/100 gal as zinc sulfate) April-June, timed for new growth stages. Foliar 
often more effective but requires specialized equipment (high-volume sprayers reaching 40-60 ft canopy).""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC marginal for walnut production. 
Walnuts' extreme demands, extremely long production cycle (50+ years), and massive tree size make moderate 
retention highly challenging. Young tree establishment very slow (12-18 years to bearing, 20-30 years full 
production). Mature productivity reduced (2,200-3,000 lb/ac). Economics questionable - multi-decade intensive 
inputs before significant returns.

MANAGEMENT STRATEGY: Intensive three-split or fertigation. Three-split: N (85 + 80 + 60 = 225 lb N/ac at 
March, May, July), K (80 + 70 + 50 = 200 lb K₂O/ac similarly split), P annually (50-70 lb P₂O₅/ac - cannot 
skip years). Fertigation through micro-sprinklers: biweekly injections 15-20 lb N/ac + 15-20 lb K₂O/ac for 
14-18 weeks (March-July). Fertigation provides more consistent nutrition for these massive long-lived trees.

ESTABLISHMENT CHALLENGE: Young walnuts extremely vulnerable in moderate retention. Takes 12-18 years to 
reach initial bearing (vs 8-12 optimal), 20-30 years for full production (vs 15-20). Extended non-productive 
period massive financial burden - decades of land occupation, annual maintenance costs, intensive fertilization, 
irrigation, pest management with zero revenue. Many growers cannot sustain 15-20+ year investment before 
returns - orchards abandoned before reaching productivity.

ORCHARD LONGEVITY: Reduced productive life in moderate retention - 30-45 years vs 50-75+ years optimal. 
While still multi-decade, shortened life combined with delayed bearing severely impacts economics. Total 
productive years (life minus establishment years) may be only 15-25 years vs 40-60 in good soils. Insufficient 
productive period to recover establishment and carrying costs at reduced yield levels.

VIABILITY: Walnut production marginal to non-viable in moderate-retention soils. Walnuts among most soil-
demanding tree crops - require excellent sustained fertility for multi-generational production. Economics 
rarely favorable - decades of intensive inputs, extended non-productive period, reduced productivity, shortened 
life. Not recommended for new orchard establishment. Better alternatives: shorter-lived less-demanding tree 
crops (peaches, apples) or avoid permanent orchards entirely. Walnut orchard planting is 50-100 year decision 
- requires best possible soils.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes walnut production economically 
IMPOSSIBLE. Walnuts among THE most nutrient-demanding tree crops with longest production cycle (50-75+ 
years). Cannot establish or maintain viable orchards from poor baseline despite any management intensity. 
Young trees fail to develop - orchards never reach productivity. DO NOT attempt walnut production in low-
retention soils.

ESTABLISHMENT IMPOSSIBLE: Young walnuts require 8-15 years optimal care to reach bearing. In low-retention 
soils, trees: remain severely stunted (<6 ft vs 15-25 ft optimal by year 10), develop multiple chronic 
deficiency symptoms, experience high mortality (40-70%), never develop adequate framework for nut production. 
15-25+ years investment (if trees somehow survive) with zero returns - not economically feasible for any 
agricultural operation.

MATURE-TREE FAILURE: If trees somehow survive establishment (unlikely), cannot produce commercial nut crop. 
Walnuts require massive sustained nutrition during nut development and shell hardening (May-September). Low 
retention cannot buffer these demands for large trees with extensive root zones (12-20 ft deep, 30-50 ft 
diameter). Trees produce minimal nuts (<1,500 lb/ac vs 3,000-4,000 viable) of extremely poor quality (small, 
poorly filled, thin shells, low kernel percentage).

MULTI-GENERATIONAL DISASTER: Walnut orchard planting multi-generational investment - orchards passed through 
families for 50-100+ years. Establishment in low-retention soil commits multiple generations to failure. 
Parents plant orchards that never produce adequately, children inherit struggling trees generating losses 
not profits. Attempting walnuts in poor soils is multi-generational economic disaster affecting families for 
decades.

ALTERNATIVES: Absolutely DO NOT plant walnut orchards in low-retention soils. Walnuts require excellent 
deep fertile soils as fundamental prerequisite. Better alternatives: 1) Any crop other than walnuts. 2) If 
committed to tree crops, choose shortest-lived least-demanding types (peaches, plums - still challenging 
but less catastrophic than walnuts). 3) Non-agricultural land uses preserving capital for better opportunities. 
Among all possible crops, walnuts one of absolute WORST choices for low-retention soils.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes walnut production COMPLETELY 
IMPOSSIBLE under any circumstances. Walnuts' extreme demands over century-scale production fundamentally 
incompatible with very-low-retention conditions. Attempting walnut orchard guaranteed multi-generational 
economic catastrophe. DO NOT ATTEMPT UNDER ANY CIRCUMSTANCES.

ABSOLUTE IMPOSSIBILITY: Walnut trees cannot survive in very-low-retention soils. Young trees: die within 
2-5 years (70-95+ mortality), show every possible deficiency symptom simultaneously, never exceed 3-4 ft 
height, never develop adequate root systems. Mature bearing trees: do not exist - 100% orchard failure 
before any trees reach bearing age. Walnut production not merely difficult but physically/biologically 
impossible.

MANAGEMENT IRRELEVANCE: No management system enables walnut survival. Intensive fertigation three times 
weekly still produces tree death from multiple deficiencies. Very sandy soils cannot buffer nutrients for 
massive trees requiring sustained nutrition over 8-12 month growing season and multi-decade establishment 
period. Cost of attempting adequate fertigation (labor, materials, equipment) would exceed $5,000-10,000/
ac annually - orders of magnitude beyond any possible returns.

INVESTMENT CATASTROPHE: Complete loss of massive establishment investment ($12,000-20,000+/ac for trees, 
irrigation, trellising). Zero returns ever generated - trees die before bearing any nuts. Worse investment 
than virtually any other agricultural enterprise - even failed annual vegetable crops produce something 
first year and allow learning/adjustment. Walnut failure is complete, expensive, and teaches only to never 
attempt walnuts in poor soils.

IMPOSSIBILITY ABSOLUTE: Walnut production THE single worst crop choice for very-low-retention soils. More 
impossible than even almonds (also extremely unsuitable but slightly less so than walnuts). No amount of 
technology, inputs, or management enables walnut survival. Walnuts require the absolute highest quality deep 
fertile soils - most soil-demanding temperate tree crop. Attempting walnuts in very-low-retention soil is 
guaranteed failure - choose literally any other crop or land use."""
    },

    "Pecans": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports highly productive pecan 
orchards (2,000-2,500+ lb in-shell/ac) over extremely long life (75-100+ years, some trees 150+ years). 
Pecans have THE HIGHEST annual nutrient needs among tree nut crops: 200-300 lb N, 50-80 lb P₂O₅, 150-250 
lb K₂O/ac for mature bearing trees. These massive trees (60-100 ft tall, 60-80 ft spread, living 100-150+ 
years) demand sustained excellent fertility over century-scale production.

MANAGEMENT STRATEGY: Multiple split N through long season: 30% early spring (April, bud break/catkin), 35% 
late spring (May-June, nut sizing), 35% summer (July-August, kernel fill). Total 200-300 lb N/ac for mature 
bearing orchards depending on yield level and tree size. K similarly split: 150-250 lb K₂O/ac in 2-3 
applications. P every 2-3 years: 50-80 lb P₂O₅/ac (high retention allows biennial). Extremely deep rooting 
(15-20+ ft) accesses nutrients throughout profile.

ZINC ABSOLUTELY ESSENTIAL: Pecans THE most Zn-responsive crop in all agriculture - more responsive than 
walnuts. Zn deficiency universal problem causing "rosette" disease: stunted terminals, tiny clustered leaves, 
dieback, no nut production. Annual Zn applications MANDATORY: 20-30 lb Zn/ac soil-applied (late fall/winter) 
plus 3-5 foliar sprays (4-6 lb Zn/100 gal zinc sulfate) during growing season. Even high-retention soils 
rarely supply adequate Zn - supplementation essential always.

NICKEL REQUIRED: Pecans unique among tree crops - require nickel (Ni) for nut fill. Ni deficiency produces 
"mouse ear" (small misshapen leaves) and poor kernel development (kernels fail to fill properly). Foliar Ni 
sprays (0.1-0.2 lb Ni/ac as nickel sulfate) 2-3 times during kernel fill (June-August) ensure adequate Ni. 
Relatively new discovery (1990s) but now recognized as essential for quality nut production.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC supports productive long-lived 
pecan orchards (1,800-2,500 lb/ac) for 60-80+ years. Intensive annual fertility mandatory - pecans THE most 
nutrient-demanding tree crop. Standard program: 200-300 lb N/ac in three splits (April, June, July-August), 
150-250 lb K₂O/ac split similarly, P 50-80 lb P₂O₅/ac annually or alternate years.

MANAGEMENT STRATEGY: Three-split N critical: 80-100 lb at bud break (April), 85-100 lb at nut sizing (late 
May-June), 85-100 lb during kernel fill (July-August). Three splits maintain N availability through extremely 
long pecan season (March-October). K three-split: 60-80 lb spring + 60-80 lb early summer + 40-80 lb late 
summer, total 160-240 lb K₂O/ac. Good retention maintains availability between splits but pecans' massive 
uptake demands frequent applications.

YOUNG-TREE ESTABLISHMENT: Pecans EXTREMELY slow to bearing - 8-15 years first nuts, 20-30 years full 
production. Longest non-productive period of any common tree crop. Demands sustained fertility through 
decades-long establishment. Good retention critical for supporting development. Years 1-5: 0.25-1.0 lb N per 
tree monthly April-August. Years 6-10: 1.0-3.0 lb N per tree monthly. Years 11-20: 3-8 lb N per tree monthly. 
Year 20+: transition to per-acre rates as orchard matures.

ZINC-NICKEL PROGRAMS: Pecans require the most intensive micronutrient program of any crop. Zn annually: 
20-30 lb Zn/ac soil-applied (fall/winter) AND 3-5 foliar sprays (4-6 lb Zn/100 gal) during growing season. 
Ni for kernel fill: 2-3 foliar sprays (0.1-0.2 lb Ni/ac) June-August. Mg often deficient: 1-2 foliar sprays 
magnesium sulfate (Epsom salt 15-20 lb/100 gal) if symptoms appear. Micronutrient program costs $150-300/
ac annually but essential.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC marginal to unsuitable for pecan 
production. Pecans have THE highest nutrient demands of any tree crop, longest production cycle (75-100+ 
years), and largest tree size. Moderate retention fundamentally insufficient for multi-generational production. 
Young tree establishment extremely slow (15-25+ years to bearing, 30-40 years full production). Mature 
productivity severely reduced (1,200-1,800 lb/ac). Economics poor - not recommended.

MANAGEMENT STRATEGY: Intensive four-split or fertigation mandatory. Four-split: N (80 + 75 + 70 + 65 = 290 
lb N/ac at April, May-June, July, August), K (70 + 65 + 60 + 55 = 250 lb K₂O/ac similarly split), P annually 
(60-80 lb P₂O₅/ac - cannot skip years). Fertigation through micro-sprinklers: biweekly injections 18-25 lb 
N/ac + 20-28 lb K₂O/ac for 18-22 weeks (April-September). Fertigation provides most consistent nutrition 
for these extremely demanding trees.

ESTABLISHMENT DISASTER: Young pecans extremely vulnerable in moderate retention. Takes 15-25 years to reach 
initial bearing (vs 8-15 optimal), 30-40+ years for full production (vs 20-30). Extended non-productive 
period enormous financial burden - literally decades of land occupation, annual costs, intensive inputs with 
zero revenue. This is multi-generational commitment - parents plant orchards, children wait for bearing, 
maybe grandchildren see full production. Economics almost never viable at moderate retention.

ORCHARD LONGEVITY: Shortened productive life in moderate retention - 40-60 years vs 75-100+ years optimal. 
While still very long, this drastically impacts economics when combined with 20-30 year non-productive 
establishment. Total productive years may be only 20-40 years vs 60-90 in good soils. Insufficient to recover 
massive cumulative establishment and carrying costs.

VIABILITY: Pecan production NOT RECOMMENDED in moderate-retention soils. Pecans require the absolute best 
soils for century-scale production. Economics almost never favorable at moderate retention - decades of 
intensive inputs before production, reduced yields when finally bearing, shortened overall life. Pecan 
orchard planting is 75-150 year multi-generational decision - requires the best possible soils. Choose 
different crops or different land use.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes pecan production COMPLETELY 
IMPOSSIBLE economically. Pecans have THE highest nutrient demands of any tree crop over longest production 
cycle (75-100+ years). Cannot establish or maintain viable orchards from poor baseline under any management. 
Young trees fail to develop - orchards never reach productivity after decades of investment. DO NOT ATTEMPT 
PECAN PRODUCTION IN LOW-RETENTION SOILS.

ESTABLISHMENT IMPOSSIBLE: Young pecans require 8-20 years optimal care to reach bearing. In low-retention 
soils, trees: remain extremely stunted (<8 ft vs 20-35 ft optimal by year 15), develop severe chronic 
deficiencies of all nutrients (especially Zn causing universal rosette disease), experience very high mortality 
(50-80%), never develop adequate crown for nut production. 20-30+ years attempted establishment (if trees 
survive at all) with zero returns - economic catastrophe.

MATURE-TREE IMPOSSIBILITY: If trees somehow survive establishment (extremely unlikely), cannot produce 
commercial nut crop. Pecans require the most massive sustained nutrition of any crop during nut development 
and kernel fill (May-October). Low retention cannot buffer these demands for enormous trees with very extensive 
root zones (15-20+ ft deep, 40-70 ft spread). Attempted production: minimal nuts (<1,000 lb/ac vs 2,000-
2,500 viable), extremely poor quality (small nuts, very poor kernel fill, blanks, thin shells), unmarketable 
commercially.

MULTI-GENERATIONAL CATASTROPHE: Pecan orchards are THE ultimate multi-generational agricultural investment 
- grandparents plant for grandchildren's production continuing great-grandchildren's lifetime. Establishment 
in low-retention soil commits multiple generations to complete failure and financial loss. Parents plant and 
maintain struggling trees for 20+ years with no production, children inherit failing orchard generating only 
costs, grandchildren must remove failed orchard. Multi-generational disaster affecting family economically 
for 50-75 years.

ALTERNATIVES: ABSOLUTELY DO NOT plant pecan orchards in low-retention soils under any circumstances. Pecans 
require THE best soils among all tree crops - fundamental prerequisite not negotiable. Better alternatives: 
1) Literally any other crop - all better choices than pecans. 2) If committed to tree crops despite poor 
soil, choose least-demanding shortest-lived (peaches, plums - still poor choices but less catastrophic). 3) 
Non-agricultural land use. Among all possible crops in all agriculture, pecans THE single worst choice for 
low-retention soils.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes pecan production THE MOST 
IMPOSSIBLE agricultural enterprise imaginable. Pecans' extreme demands over century-plus production cycle 
absolutely incompatible with very-low-retention conditions. Attempting pecan orchard is multi-generational 
guaranteed economic and agricultural catastrophe of the highest order. DO NOT ATTEMPT UNDER ABSOLUTELY ANY 
CIRCUMSTANCES WHATSOEVER.

ABSOLUTE COMPLETE IMPOSSIBILITY: Pecan trees CANNOT survive establishment in very-low-retention soils 
regardless of any management. Young trees: die within 2-5 years (80-99% mortality), show severe deficiencies 
of every nutrient simultaneously, develop universal rosette disease (Zn deficiency), never exceed 3-5 ft 
height, never develop root systems adequate for tree survival. Mature bearing pecan trees in very-low-
retention: DO NOT EXIST - 100% complete orchard failure before any trees reach bearing. Not merely difficult 
but physically/biologically/absolutely impossible.

MANAGEMENT COMPLETE FUTILITY: No management system imaginable enables pecan survival. Intensive fertigation 
three times weekly with every nutrient known still produces rapid tree death from multiple deficiencies and 
disorders. Very sandy soils absolutely cannot buffer nutrients for massive trees requiring sustained high 
nutrition over 8-10 month season and multi-decade establishment. Cost of attempting adequate management 
would exceed $8,000-15,000/ac annually - absurdly beyond any possible returns from crop that never produces 
nuts.

INVESTMENT COMPLETE DISASTER: Total complete loss of enormous establishment investment ($15,000-25,000+/
ac for trees, irrigation, infrastructure). Absolutely zero returns ever generated - 100% tree death before 
bearing any nuts. THE WORST possible agricultural investment imaginable - worse than any other crop attempt 
in any conditions. Even attempting vegetables in desert without irrigation would be better investment - at 
least fails quickly rather than 5-10 year tree death prolonging losses.

IMPOSSIBILITY BEYOND ABSOLUTE: Pecan production THE SINGLE ABSOLUTE WORST crop choice for very-low-retention 
soils. THE MOST IMPOSSIBLE agricultural enterprise possible in such conditions. More impossible than walnuts 
(also completely impossible), more impossible than almonds (also completely impossible), THE MOST IMPOSSIBLE. 
No technology, no amount of inputs, no management enables pecan survival. Pecans require THE absolute highest 
quality deepest most fertile soils among ALL crops in temperate agriculture. Attempting pecans in very-low-
retention soil is GUARANTEED multi-generational catastrophe. Choose any other crop, any other land use, any 
other agricultural enterprise - ALL infinitely better choices than pecans."""
    },
    
    # ========================================================================
    # SPECIALTY CROPS
    # ========================================================================

    "Hops": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports intensive hop production 
(2,500-3,000 lb/ac) over 20-25 year yard life. Hops are EXTREMELY HEAVY feeders with unique growth habit - 
massive annual vegetative growth from perennial crown (bines climbing 18-20 ft annually). Annual requirements 
among highest of specialty crops: 200-250 lb N, 100-150 lb P₂O₅, 200-300 lb K₂O/ac for mature productive 
yards. High retention essential for buffering nutrients through rapid growth phase.

MANAGEMENT STRATEGY: Multiple split N matching hop growth stages: 30% early spring (emergence, March-April), 
35% rapid bine growth (May, climbing period), 35% cone development (June-July, flowering and cone formation). 
Total 200-250 lb N/ac for mature yards. K similarly critical: split 40% spring + 35% rapid growth + 25% 
cone development, total 200-300 lb K₂O/ac. P annually: 100-150 lb P₂O₅/ac broadcast or banded in rows - 
hops have very high P needs.

POTASSIUM-QUALITY: K critical for hop quality - affects alpha acid content (brewing value), cone size, cone 
density, aromatic oil production. Adequate K (250-300 lb K₂O/ac) produces: 12-16% alpha acids (premium 
brewing quality), large dense cones, excellent aromatic profile. K deficiency severely reduces alpha acids 
(8-10%) and cone quality - unmarketable for premium brewing. High retention maintains K through heavy removal 
in harvested cones.

SULFUR ESSENTIAL: Hops have high S requirement (30-50 lb S/ac annually) for aromatic compound synthesis - 
S-containing compounds critical for hop aroma and brewing characteristics. Use S-containing fertilizers 
(ammonium sulfate, potassium sulfate, gypsum) to supply S with N or K. S deficiency reduces aromatic oils 
making hops unsuitable for craft brewing applications requiring specific aroma profiles.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC supports productive hop yards 
(2,000-2,500 lb/ac) with intensive annual fertility program. Hops' extreme demands require heavy inputs even 
from good baseline. Standard program: 200-250 lb N/ac in three splits (spring, rapid growth, cone development), 
200-300 lb K₂O/ac split similarly, P 100-150 lb P₂O₅/ac annually.

MANAGEMENT STRATEGY: Three-split N: 70 lb early spring + 80 lb rapid bine growth + 70 lb cone development, 
total 220 lb N/ac. K three-split: 80 lb spring + 90 lb rapid growth + 80 lb cone development, total 250 lb 
K₂O/ac. P annually: 100-150 lb P₂O₅/ac broadcast fall or early spring. Good retention maintains availability 
between splits but hops' rapid uptake during bine growth (May: 2-6 inches/day, accumulating 70% annual 
biomass) requires frequent replenishment.

FERTIGATION OPTION: Drip or overhead fertigation increasingly common in modern hop production. Biweekly 
injections 18-25 lb N/ac + 20-30 lb K₂O/ac during active growth (April-July, 14-16 weeks). Fertigation 
provides precise nutrition timing matching rapid growth phases. Particularly beneficial for alpha acid 
optimization - consistent nutrition produces more uniform alpha acid levels meeting brewing contracts.

ALPHA ACID MANAGEMENT: Alpha acid content (10-16%) determines hop value and use in brewing. Adequate balanced 
nutrition (especially N-K-S) during cone development (June-July) critical for alpha acid synthesis. Good 
retention with proper timing produces 12-15% alpha acids - premium quality for craft brewing. Deficiencies 
or imbalances during cone development permanently reduce alpha acids in that year's crop.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC challenging for hops' extreme 
demands. Hops among most nutrient-demanding specialty crops - massive annual vegetative growth (18-20 ft 
bines) from perennial crown requires sustained heavy nutrition. Yields limited to 1,500-2,000 lb/ac. Four-
split program or fertigation essential.

MANAGEMENT STRATEGY: Four-split N: 55 lb spring + 60 lb early rapid growth + 55 lb late rapid growth + 50 
lb cone development, total 220 lb N/ac. K four-split: 60 lb spring + 70 lb early growth + 65 lb late growth 
+ 60 lb cone, total 255 lb K₂O/ac. P annually: 100-150 lb P₂O₅/ac - cannot reduce P despite moderate retention 
given hops' very high P needs. More frequent splits compensate for moderate retention during intensive growth 
phase (April-July).

BINE-VIGOR IMPACTS: Moderate retention reduces bine vigor: shorter bines (14-18 ft vs 18-20 ft optimal), 
thinner diameter, slower growth rate, delayed cone development. Reduced vigor decreases yield (fewer cones 
per bine) and can affect cone quality. Still produces marketable hops but not premium quality - alpha acids 
10-13% vs 12-16% optimal.

PERENNIAL MAINTENANCE: Hops' perennial crowns (root systems surviving 20+ years) require sustained fertility 
across years. Moderate retention makes multi-year maintenance challenging - crowns gradually weaken if 
nutrition inadequate season after season. Expect yard life 12-18 years vs 20-25 in high retention. Plan for 
earlier replanting increasing long-term costs.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes hop production extremely 
challenging. Hops' massive demands (200-250 lb N, 200-300 lb K₂O/ac annually) for enormous annual vegetative 
growth from perennial crowns very difficult to sustain in low retention. Yields limited to 1,000-1,500 lb/ac. 
Fertigation strongly recommended - five-split conventional program marginal.

MANAGEMENT OPTIONS: Fertigation (RECOMMENDED): biweekly injections 20-30 lb N/ac + 25-35 lb K₂O/ac for 16-
20 weeks (April-July), total 160-300 lb N and 200-350 lb K₂O through season. P pre-plant incorporated: 120-
150 lb P₂O₅/ac plus annual surface: 80-100 lb P₂O₅/ac. Five-split alternative: N-K applications every 3 
weeks during growing season - labor intensive and less effective than fertigation.

CROWN-VIGOR DECLINE: Low retention severely impacts perennial crown health. First-second year acceptable 
production from crown reserves. Third-fourth year declining as reserves deplete. Fifth+ year poor - weak 
emergence, thin bines, reduced cones, low alpha acids. Yard life 8-12 years vs 20-25 optimal. Frequent 
replanting (every 8-10 years) dramatically increases costs - replanting $12,000-18,000/ac including trellis, 
plants, establishment.

ALPHA-ACID PROBLEMS: Low retention produces quality issues: low alpha acids (8-11% vs 12-16%), variable 
cone size, reduced aromatic oils, inconsistent quality year-to-year. Premium craft brewing contracts (requiring 
12-15% alpha acids) difficult to meet consistently. Better suited for bittering varieties (lower alpha 
requirements) than aroma varieties (demand consistent high quality).

VIABILITY: Hops marginally viable for 1,000-1,500 lb/ac in low-retention soils with intensive fertigation. 
Economics marginal - high establishment costs ($15,000-20,000/ac including trellis, irrigation, plants), 
intensive annual inputs ($1,500-2,500/ac), shortened yard life, moderate yields. Only viable if: craft 
brewing contracts secured, premium pricing achieved, fertigation installed. Not recommended without guaranteed 
markets and intensive management commitment.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes hop production non-viable. Hops' 
extreme demands (massive annual vegetative growth, heavy cone production, perennial crown maintenance over 
20 years) absolutely incompatible with very-low-retention conditions. Even intensive fertigation cannot 
sustain adequate nutrition for hops' rapid growth phases. DO NOT attempt hop production.

MANAGEMENT IMPOSSIBILITY: No fertility system supports viable hop production in very-low-retention. Intensive 
fertigation twice-weekly still produces deficiencies during rapid bine growth (May: 2-6 inches/day, accumulating 
60-80 lb N/ac weekly). Very sandy soils cannot buffer nutrients for these extreme uptake rates. Attempting 
adequate fertigation requires application every 2-3 days - economically and practically impossible for field-
scale hop yards.

CROWN FAILURE: Perennial hop crowns require sustained multi-year nutrition for 15-20+ year productive life. 
Very-low-retention soils cannot sustain crowns - first year marginal, second year poor, third+ year crown 
death. Replanting every 2-3 years economically catastrophic - establishment costs ($15,000-20,000/ac) cannot 
be recovered over 2-3 year production. Hops require sustained perennial production for economic viability - 
impossible in very low retention.

QUALITY DISASTER: Very-low-retention hops produce unmarketable quality: alpha acids <8% (unusable for most 
brewing), small sparse cones, minimal aromatic oils, extreme variability. Even craft brewers with low quality 
tolerance cannot use such poor hops. No market exists for very-low-quality hops - product has no commercial 
value.

ALTERNATIVES: DO NOT attempt hops in very-low-retention soils. Hops among most demanding specialty crops - 
require good to excellent soils for economic production. Better alternatives: 1) Hemp (somewhat similar plant 
but annual, much lower demands). 2) Annual vegetable crops (avoid perennial investment). 3) Improved pasture 
or hay. 4) Different land use entirely. Among specialty crops, hops one of WORST choices for very-low-
retention conditions - massive demands over long perennial cycle make success impossible."""
    },

    "Hemp": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports all hemp production 
systems excellently: fiber hemp (8-10 tons/ac dry biomass, 12-14 ft height), grain hemp (1,500-2,000 lb/ac 
seed), CBD hemp (1,500-2,000 lb/ac floral material). Hemp has MODERATE to HIGH needs depending on type: 
fiber (highest, 120-150 lb N/ac), CBD (intermediate, 100-140 lb N/ac), grain (lowest, 80-120 lb N/ac). 
Fast-growing crop (90-120 days) accumulates nutrients rapidly.

MANAGEMENT STRATEGY: Split N by hemp type. Fiber: 50% pre-plant + 50% at 30-40 days (rapid vegetative 
growth), total 120-150 lb N/ac. CBD: 45% pre-plant + 35% at flowering initiation + 20% early flowering, 
total 100-140 lb N/ac. Grain: 60% pre-plant + 40% at 30 days, total 80-120 lb N/ac. K: 100-150 lb K₂O/ac 
mostly pre-plant. P: 60-80 lb P₂O₅/ac pre-plant. High retention supports hemp's rapid nutrient scavenging 
through deep tap root (4-6 ft when mature).

HEMP TYPE SELECTION: Production goal determines nutrient needs. Fiber hemp: tallest, most vegetative growth, 
highest N demand, densest planting (300-400 plants/m²), harvested at early flowering. CBD hemp: moderate 
height (4-6 ft), focus on floral biomass, intermediate N, sparse planting (1,500-2,500 plants/ac), harvested 
at peak cannabinoid. Grain hemp: moderate height (5-8 ft), focus on seed production, lowest N, moderate 
planting (20,000-30,000 plants/ac), harvested at seed maturity. High retention supports all types.

SCAVENGING EFFICIENCY: Hemp legendary for nutrient scavenging efficiency - deep tap roots access nutrients 
throughout profile, rapid growth exploits available nutrients quickly. However, this reputation sometimes 
overstated - commercial hemp still requires adequate fertility for economic yields/quality. High retention 
provides nutrients for hemp's efficient uptake system to exploit.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC supports productive hemp: fiber 
(6-8 tons/ac), grain (1,200-1,500 lb/ac), CBD (1,200-1,500 lb/ac). Standard split programs by type: fiber 
(120-150 lb N/ac split 60% pre-plant + 40% at 30 days), CBD (100-130 lb N/ac split 50% pre-plant + 30% 
flowering + 20% early flower), grain (80-120 lb N/ac split 60% pre-plant + 40% at 30 days).

MANAGEMENT STRATEGY: Two-split N adequate for most hemp types in good retention. K: 100-140 lb K₂O/ac pre-
plant. P: 60-80 lb P₂O₅/ac pre-plant. Hemp's deep rooting (4-6 ft mature tap root) and rapid growth allow 
efficient nutrient uptake from good-retention soils. Annual soil testing guides fertility - hemp's nutrient 
removal varies greatly by type and yield level.

CBD-QUALITY CONSIDERATION: CBD hemp quality (cannabinoid content, terpene profile) affected by nutrition. 
Balanced moderate fertility produces best cannabinoid levels (8-12% CBD). Excessive N can reduce CBD percentage 
and alter terpene profiles - better slightly deficient than excessive. Good retention with moderate N rates 
(100-120 lb N/ac) produces premium CBD flower quality.

GRAIN-HEMP VIABILITY: Grain hemp (for seed/oil) most tolerant of moderate fertility among hemp types. Lower 
N requirement (80-120 lb N/ac), moderate demands, and seed market flexibility make grain hemp excellent 
choice for good-retention soils. Seed yields 1,200-1,500 lb/ac produce acceptable returns with moderate 
inputs.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC acceptable for hemp production - 
hemp reasonably adapted to moderate fertility compared to many crops. Deep tap root development (3-5 ft even 
in moderate retention) allows access to nutrients below surface. Fiber hemp most challenging (highest demands), 
grain hemp most successful (lowest demands), CBD intermediate. Three-split program recommended.

MANAGEMENT STRATEGY: Three-split N: fiber (50 + 45 + 40 = 135 lb N/ac), CBD (45 + 40 + 35 = 120 lb N/ac), 
grain (40 + 35 + 30 = 105 lb N/ac). Timing: pre-plant, 30 days, 50-60 days. K split: 70% pre-plant + 30% 
at 30 days, total 120 lb K₂O/ac. P annually: 60-80 lb P₂O₅/ac pre-plant or banded.

TYPE-SELECTION CRITICAL: Grain hemp MOST viable at moderate retention - lowest demands, most forgiving, 
acceptable markets. CBD hemp intermediate - moderate demands, quality acceptable if N not excessive. Fiber 
hemp LEAST viable - high demands for massive vegetative growth difficult to meet, fiber quality (length, 
strength) reduced at moderate retention. Prioritize grain hemp for moderate-retention conditions.

QUALITY IMPACTS: Moderate retention affects hemp quality by type. Fiber: shorter fibers (reduced stem height), 
lower strength, acceptable for paper/textiles but not premium textile applications. CBD: cannabinoid content 
acceptable (7-10% CBD), but variability higher - some plants <6%, some >10%. Grain: minimal quality impact 
- seed size and oil content largely unaffected, yields modest but quality acceptable.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes hemp production challenging 
but HEMP MORE VIABLE than most crops at this fertility level. Hemp's reputation for thriving on marginal 
land has some basis - deep rooting, rapid growth, and efficient nutrient scavenging provide advantages. 
However, commercial production requires reasonable fertility - subsistence-level hemp on poor land not same 
as economic modern production.

MANAGEMENT STRATEGY: Three to four-split N compensates for low retention. Grain hemp (RECOMMENDED): 40 + 
35 + 30 = 105 lb N/ac split pre-plant, 30 days, 60 days. CBD hemp: 45 + 40 + 35 + 30 = 150 lb N/ac split 
pre-plant, 25 days, 45 days, 65 days (more splits due to higher demand). Fiber hemp: not recommended (demands 
too high for low retention). K split: 80 lb pre-plant + 40 lb at 30 days = 120 lb K₂O/ac. P: 70-80 lb 
P₂O₅/ac banded.

GRAIN-HEMP FOCUS: Grain hemp BEST choice for low-retention conditions. Advantages: lowest N requirement 
(80-120 lb N/ac), moderate total demands, forgiving of variable fertility, acceptable quality even at moderate 
yields (800-1,200 lb/ac), diverse markets (food, oil, feed). Grain hemp reasonable economic production 
possible in low retention where most crops struggle.

DEEP-ROOT ADVANTAGE: Hemp's deep tap root (3-5 ft even in challenging conditions) major advantage in low-
retention soils. Roots access nutrients and moisture below poor surface layer. This makes hemp better adapted 
than shallow-rooted crops (vegetables, small grains) to low-retention conditions. Historic use on poor land 
reflects this adaptation.

VIABILITY: Grain hemp viable for 800-1,200 lb/ac in low-retention soils - among better specialty crop 
choices. CBD hemp marginal (1,000-1,200 lb/ac, quality variable). Fiber hemp not recommended (inadequate 
biomass and quality). Economics moderate - acceptable grain yields with moderate inputs viable for seed/oil 
markets. Hemp reasonable choice for low-retention specialty crop production.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes commercial hemp production 
marginal but HEMP STILL AMONG BETTER OPTIONS for very-low-retention conditions. Hemp's adaptation to marginal 
land (deep rooting, rapid growth, efficient scavenging) provides some advantage. However, modern commercial 
hemp (fiber, CBD, grain) requires adequate fertility - extremely low retention challenges all types.

MANAGEMENT OPTIONS: Grain hemp only viable type - focus exclusively on seed production. Three to four-split 
N: 35 + 30 + 25 + 20 = 110 lb N/ac split every 3 weeks during season. K split: 70 + 40 = 110 lb K₂O/ac. P 
banded: 70-80 lb P₂O₅/ac. Expect yields 600-1,000 lb/ac seed - modest but potentially economic if markets 
favorable. CBD and fiber hemp not recommended - demands exceed very-low-retention capacity.

DEEP-ROOT CRITICAL: Hemp's deep tap root (2-4 ft even in extreme conditions) essential for accessing nutrients 
below very poor surface. Allow adequate time for root development - hemp establishes slowly first 3-4 weeks 
then grows rapidly weeks 4-10. Deep rooting makes hemp better adapted than shallow-rooted crops to very 
sandy conditions.

COVER-CROP ALTERNATIVE: Consider hemp as cover crop / green manure rather than commercial production in 
very-low-retention. Hemp planted late spring, grows rapidly despite poor fertility (biomass accumulation 
even at low retention), terminated mid-summer before seed. Adds 3-5 tons/ac biomass, improves soil structure, 
deep roots break up compaction, residues add OM. Single-season soil improvement use may be more viable than 
attempting commercial production.

HISTORICAL CONTEXT: Hemp historically grown on poor land was low-quality fiber for rope/cordage, not modern 
high-value products (CBD, food-grade grain). Subsistence hemp production on marginal land produced 2-4 tons/
ac poor-quality fiber - not economically comparable to modern production requiring 6-10 tons/ac quality 
fiber or 1,200-1,800 lb/ac food-grade seed or 1,200-1,500 lb/ac premium CBD flower.

VIABILITY: Grain hemp marginally viable for 600-1,000 lb/ac in very-low-retention soils with intensive 
management. Among better specialty crop options for extreme conditions - moderate demands, deep rooting, 
reasonable adaptation to poor soils. Economics marginal - modest yields require premium seed markets ($0.50-
1.00/lb) for viability. CBD and fiber hemp not recommended. Alternative: cover crop use may be more practical 
than commercial production."""
    },

    "Herbs": {
        "Very High": """Excellent nutrient retention (SQ2: 80-100). High CEC supports vigorous herb growth 
but CAUTION - many culinary herbs (basil, rosemary, lavender, thyme, oregano, sage) produce BEST flavor and 
essential oils at MODERATE fertility not maximum fertility. High retention can promote excessive vegetative 
growth reducing oil concentration and altering flavor profiles. Leafy herbs (parsley, cilantro, chives, dill) 
benefit from high fertility for foliage production.

MANAGEMENT STRATEGY: RESTRAINED fertility for aromatic herbs: 50-80 lb N/ac split 60% spring + 40% mid-
season (much lower than most crops). K: 60-100 lb K₂O/ac. P: 40-60 lb P₂O₅/ac. High retention with low 
inputs produces concentrated essential oils and intense flavors. HIGHER fertility for leafy herbs: 100-140 
lb N/ac split 50% spring + 50% mid-season for maximum foliage. K: 80-120 lb K₂O/ac. P: 60-80 lb P₂O₅/ac.

ESSENTIAL-OIL PRODUCTION: Aromatic herbs (basil, oregano, thyme, rosemary, sage, lavender) grown for essential 
oil content. Moderate fertility stress promotes oil synthesis - plants allocate resources to defensive 
compounds (essential oils) rather than vegetative growth. Excessive N reduces oil concentration (plants grow 
large but with dilute oils). High retention requires deliberate N restriction for premium aromatic quality.

HERB CATEGORIES: Two main groups with opposite fertility needs. 1) AROMATIC herbs (Mediterranean types): 
prefer moderate fertility, concentrated oils, intense flavor - basil, oregano, thyme, rosemary, sage, 
lavender, marjoram. 2) LEAFY herbs (northern European types): benefit from higher fertility, maximum foliage, 
mild flavor - parsley, cilantro, chives, dill, fennel. High retention excellent for leafy herbs, potentially 
excessive for aromatic herbs unless N restricted.""",
        
        "High": """Good nutrient retention (SQ2: 60-79). Moderate to high CEC often OPTIMAL for most culinary 
herbs - provides adequate nutrition without excess that dilutes essential oils. Many premium herb production 
regions have soils in this retention range balancing plant vigor and oil/flavor quality. This retention 
level produces excellent quality for both aromatic and leafy herbs with proper management.

MANAGEMENT STRATEGY: Aromatic herbs (basil, oregano, thyme, rosemary, lavender): moderate program of 60-
100 lb N/ac split 60% spring + 40% mid-season, K 70-100 lb K₂O/ac, P 50-70 lb P₂O₅/ac annually. Good 
retention with moderate inputs produces concentrated oils and excellent flavor. Leafy herbs (parsley, cilantro, 
chives): higher program of 100-130 lb N/ac split 50% spring + 50% mid-season, K 90-120 lb K₂O/ac, P 60-80 
lb P₂O₅/ac.

HARVEST TIMING: Essential oil concentration varies with plant development stage and nutrition. Aromatic 
herbs: harvest at early flowering when oil concentration peaks. Good retention with balanced moderate nutrition 
produces maximum oil content at harvest. Too early (vegetative): lower oil content. Too late (full flower): 
declining oil content. Proper nutrition supports optimal harvest timing.

PERENNIAL HERBS: Many herbs are perennial (thyme, oregano, sage, rosemary, lavender, chives). Good retention 
supports multi-year stands (3-5+ years) with annual maintenance fertility: 50-80 lb N/ac, 60-80 lb K₂O/ac, 
P every 2-3 years. Perennial nature allows amortizing establishment costs over multiple years improving 
economics.""",
        
        "Medium": """Moderate nutrient retention (SQ2: 40-59). Moderate CEC acceptable to PREFERRED for many 
aromatic Mediterranean herbs - these species evolved on thin rocky soils of Mediterranean region with moderate 
fertility. Thyme, oregano, lavender, rosemary, sage all thrive at moderate retention producing concentrated 
oils. Leafy herbs and basil require more intensive management but still viable.

MANAGEMENT STRATEGY: Mediterranean aromatic herbs: light program of 50-80 lb N/ac split 60% spring + 40% 
summer, K 70-100 lb K₂O/ac, P 50-70 lb P₂O₅/ac annually. Moderate retention with light inputs produces 
excellent oil concentration and flavor - often BETTER quality than high-fertility conditions. Leafy herbs / 
basil: three-split program (40 + 35 + 30 = 105 lb N/ac), K 90-120 lb K₂O/ac, P 60-80 lb P₂O₅/ac.

MEDITERRANEAN ADVANTAGE: Mediterranean herbs (thyme, oregano, rosemary, sage, lavender, marjoram) naturally 
adapted to moderate-fertility dry soils. Moderate retention mimics native conditions producing authentic 
flavor profiles and concentrated oils. Many consider these herbs produce BEST quality at moderate fertility 
- plants under mild stress allocate resources to defensive compounds (essential oils) creating intense 
flavors. Premium herb production often on moderate-retention soils.

ANNUAL vs PERENNIAL: Annual herbs (basil, cilantro, dill) require more intensive fertility in moderate 
retention - three splits maintain adequacy through season. Perennial herbs (thyme, oregano, sage, rosemary, 
lavender) better adapted - annual light fertilization adequate for multi-year stands. Consider perennials 
for moderate-retention herb production.""",
        
        "Low": """Below-average nutrient retention (SQ2: 20-39). Low CEC makes most culinary herb production 
challenging. However, Mediterranean aromatic herbs (thyme, oregano, lavender, rosemary, sage) STILL VIABLE 
- among most tolerant specialty crops of low fertility. These species evolved on poor rocky Mediterranean 
soils - reasonably adapted to challenging conditions. Leafy herbs (parsley, cilantro, basil) more difficult.

MANAGEMENT STRATEGY: Mediterranean herbs: 50-80 lb N/ac split 50% spring + 30% mid-season + 20% late season, 
K 80-100 lb K₂O/ac split 60% spring + 40% summer, P 60-80 lb P₂O₅/ac annually. Three splits maintain adequacy 
through season despite low retention. Leafy herbs / basil: four-split (30 + 30 + 25 + 20 = 105 lb N/ac), K 
100-120 lb K₂O/ac split similarly, intensive management required.

SPECIES SELECTION: Focus on most tolerant species for low-retention production. BEST: thyme (extremely 
tolerant, authentic quality at low fertility), oregano (very tolerant, concentrated flavor), sage (tolerant, 
perennial). ACCEPTABLE: rosemary (tolerant if pH suitable), lavender (tolerant, prefers well-drained low-
retention). CHALLENGING: basil (annual, moderate demands), cilantro (struggles in poor conditions), parsley 
(requires reasonable fertility).

QUALITY ACCEPTABLE: Low-retention Mediterranean herbs produce acceptable to excellent quality - sometimes 
BETTER than high-fertility conditions. Stress from limited nutrients promotes concentrated essential oils. 
Yields lower (30-50% of optimal) but oil concentration often higher (20-40% more concentrated). For premium 
essential oil production or dried herb sales, quality more important than yield - low retention can produce 
premium product.

VIABILITY: Mediterranean aromatic herbs (thyme, oregano, sage, lavender) viable in low-retention soils - 
among best specialty crop choices for poor conditions. Yields modest but quality acceptable to excellent. 
Leafy herbs marginal. Economics depend on market - premium dried herbs or essential oils can be viable even 
at lower yields due to quality concentration. Fresh market leafy herbs difficult due to low yields.""",
        
        "Very Low": """Poor nutrient retention (SQ2: 0-19). Minimal CEC makes most herb production non-viable. 
However, most drought/stress-tolerant Mediterranean herbs (thyme, oregano) STILL MARGINALLY VIABLE - among 
few specialty crops with any success potential in extreme conditions. These evolved on extremely poor rocky 
soils - have adaptation to severe stress. All other herbs not recommended.

MANAGEMENT OPTIONS: Thyme and oregano only: three to four-split N (20 + 20 + 15 + 15 = 70 lb N/ac), K split 
(30 + 25 + 20 = 75 lb K₂O/ac), P annually (60-80 lb P₂O₅/ac banded). Or small-scale raised bed production 
with compost-amended mix (30% compost + 70% native soil) providing temporary retention improvement for 4-6 
month season.

THYME-OREGANO FOCUS: Only these two herbs have reasonable viability. Thyme: extremely stress-tolerant, 
authentic concentrated flavor even at low fertility, perennial (3-5 year stands possible). Oregano: very 
stress-tolerant, intense flavor from stress-promoted oils, perennial (2-4 years). Both produce lower yields 
(20-40% optimal) but often MORE concentrated oils than high-fertility conditions - premium quality from 
extreme stress.

NATIVE SPECIES: Consider native wild species adapted to local very-low-retention conditions rather than 
cultivated Mediterranean herbs. Native thyme, oregano, sage species (if region has them) better adapted 
than imported cultivars. Or entirely different native aromatic plants adapted to local poor soils - these 
may have untapped culinary or essential oil potential.

SMALL-SCALE ONLY: Commercial production marginal in very-low-retention. Small-scale specialty production 
potentially viable: artisan essential oils, premium dried herbs, niche culinary markets willing to pay premium 
for authentic stress-concentrated flavors. Field-scale production not economically viable - yields too low, 
quality too variable.

VIABILITY: Only thyme and oregano marginally viable in very-low-retention soils. All other herbs not 
recommended. Even thyme/oregano marginal - small-scale specialty production only. Better alternatives: choose 
crops better adapted to extreme sandy conditions (certain vegetables, grain crops) or implement soil improvement 
before attempting specialty herbs."""
    }
}


def get_sq2_interpretation(crop: str, rating: str) -> str:
    """
    Get the enhanced interpretation for a specific crop and SQ2 rating.
    
    Parameters:
    -----------
    crop : str
        The name of the crop (must match keys in SQ2_INTERPRETATIONS)
    rating : str
        The SQ2 rating (Very High, High, Medium, Low, or Very Low)
    
    Returns:
    --------
    str
        The interpretation text for the specified crop and rating
    
    Raises:
    -------
    KeyError
        If the crop or rating is not found in the lookup table
    """
    if crop not in SQ2_INTERPRETATIONS:
        available_crops = ", ".join(sorted(SQ2_INTERPRETATIONS.keys()))
        raise KeyError(f"Crop '{crop}' not found. Available crops: {available_crops}")
    
    if rating not in SQ2_INTERPRETATIONS[crop]:
        available_ratings = ", ".join(SQ2_INTERPRETATIONS[crop].keys())
        raise KeyError(f"Rating '{rating}' not found for crop '{crop}'. Available ratings: {available_ratings}")
    
    return SQ2_INTERPRETATIONS[crop][rating]


def get_all_crops() -> list:
    """
    Get a list of all available crops in the interpretation table.
    
    Returns:
    --------
    list
        Sorted list of all crop names
    """
    return sorted(SQ2_INTERPRETATIONS.keys())


def get_all_ratings() -> list:
    """
    Get a list of all rating categories.
    
    Returns:
    --------
    list
        List of rating categories in order from best to worst
    """
    return ["Very High", "High", "Medium", "Low", "Very Low"]


# Example usage
if __name__ == "__main__":
    # Example: Get enhanced interpretation for Corn with High rating
    crop_name = "Corn"
    rating_value = "High"
    interpretation = get_sq2_interpretation(crop_name, rating_value)
    print(f"\n{crop_name} - {rating_value} SQ2 Rating:")
    print(interpretation)
    print("\n" + "="*80)
    
    # Show all available crops
    print(f"\nTotal crops in database: {len(get_all_crops())}")
    print("\nAll crops with comprehensive nutrient retention interpretations:")
    for i, crop in enumerate(get_all_crops(), 1):
        print(f"{i:2d}. {crop}")
    
    print("\n" + "="*80)
    print("Comprehensive features include:")
    print("  • Specific SQ2 score ranges (retention capacity: 0-100 scale)")
    print("  • Detailed nutrient management for each retention level")
    print("  • Split application timing and rates (N-P-K lb/ac)")
    print("  • Fertigation recommendations and schedules")
    print("  • Quality impacts of retention level")
    print("  • Economic viability at each retention level")
    print("  • Crop-specific management strategies")
    print("  • Alternative approaches for challenging conditions")
