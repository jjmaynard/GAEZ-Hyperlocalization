"""
SQ3 (Rooting Conditions) Enhanced Interpretations - COMPLETE
Comprehensive Crop-Specific Rooting Requirements and Adaptations

Based on FAO GAEZ methodology which evaluates:
- Effective soil depth (0-150cm to restricting layers)
- Bulk density and compaction
- Soil structure development
- Coarse fragment content
- Physical barriers to root penetration
- Mechanical resistance

RATING SCALE:
- Very High: 80-100 (Excellent rooting conditions)
- High: 60-79 (Good rooting conditions)
- Medium: 40-59 (Moderate rooting conditions)
- Low: 20-39 (Poor rooting conditions)
- Very Low: 0-19 (Very poor rooting conditions)

ROOTING DEPTH CATEGORIES BY CROP:
- Very Shallow (<30cm): Lettuce, onions, radish, leafy herbs
- Shallow (30-60cm): Potatoes, cabbage, beans, most vegetables
- Medium (60-100cm): Wheat, maize, soybeans, cotton, tomatoes
- Deep (100-150cm): Sorghum, sunflower, peanuts, melons
- Very Deep (>150cm): Alfalfa, sugar beets, tree crops, grapes
"""

SQ3_INTERPRETATIONS = {
    # ========================================================================
    # FIELD CROPS
    # ========================================================================
    
    "Corn": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil (>150cm) supports 
corn's extensive root system: primary seminal roots (0-30cm), crown roots (15-30cm origin penetrating to 
100-180cm), and brace roots (stabilization). Corn develops 6-8 ft deep roots in excellent conditions accessing 
large soil volume for water and nutrients. Low bulk density (<1.4 g/cm³), good structure, no physical barriers 
allow maximum root exploration.

ROOT SYSTEM CHARACTERISTICS: Corn is medium to deep-rooted (60-150cm effective depth). Develops dual root 
system: shallow crown roots (80% of total root mass in top 30cm) for nutrient uptake, and deep anchor roots 
(to 150-180cm) for water access and stability. Root spread 30-40 inches from stalk. Critical root development 
stages: V6-V8 (rapid lateral spread), V10-V12 (deep root penetration), VT-R1 (maximum depth reached).

MANAGEMENT ADVANTAGES: Excellent rooting allows efficient nutrient scavenging throughout profile - reduced 
fertilizer needs compared to restricted soils. Deep roots access subsoil moisture providing 7-10 day drought 
buffer between irrigations vs 3-5 days in restricted soils. Strong anchorage resists lodging even in high 
winds. Uniform root distribution supports consistent nutrient uptake and stable yields. Can delay irrigation 
timing, reduce frequency, and use deficit irrigation strategies.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) adequate for corn's root system 
though some minor restrictions present (moderate bulk density 1.4-1.5 g/cm³, or few coarse fragments 15-35%, 
or moderate structure). Corn develops 4-6 ft effective rooting depth - adequate for good production. Most 
root mass still in top 60cm with reasonable deep root development for water access.

ROOT DEVELOPMENT: Crown roots penetrate to 100-120cm in good conditions - sufficient for most situations. 
May encounter minor resistance in subsoil (compact layer, higher bulk density) slowing but not preventing 
deep root growth. Lateral spread 24-36 inches from stalk. Root system adequate for: nutrient uptake from 
profile, moderate drought buffering (5-7 days between irrigations), good plant stability, efficient water 
use.

MANAGEMENT IMPLICATIONS: Occasional deep tillage (subsoiling every 3-5 years) may improve deep rooting if 
traffic pan or natural compaction present at 30-45cm. Standard fertilizer placement effective - both broadcast 
and banded options work well. Irrigation scheduling moderate frequency - not as flexible as excellent conditions 
but much better than restricted soils. Expect minimal lodging in normal weather; severe storms may cause some 
lodging if root plate shallow. Yields 95-100% of optimum with proper management.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or moderate 
restrictions (bulk density 1.5-1.6 g/cm³, common coarse fragments 35-60%, compact subsoil, or abrupt textural 
change) limit corn root development. Effective rooting depth 30-60cm - adequate for crown roots but limited 
deep root penetration. Roots concentrated in upper profile creating drought vulnerability and reduced nutrient 
access from subsoil.

ROOT LIMITATIONS: Crown roots may penetrate to only 60-80cm before encountering resistance (compact layer, 
rock, dense clay). Shallow effective rooting reduces: soil volume explored (50-70% of potential), water 
available to crop (60-70% of deep-rooted corn), drought buffering (3-5 days between irrigations vs 7-10 days 
optimal), anchorage strength (increased lodging risk). Lateral root spread reduced to 18-24 inches.

MANAGEMENT REQUIREMENTS: Deep tillage before planting (subsoiling, deep ripping to 18-24 inches) can 
temporarily improve rooting if compaction near surface. Won't help if restriction is rock, dense clay B-horizon, 
or cemented layer. Place fertilizer in rooting zone - banded applications 4-6 inches deep better than broadcast 
since roots can't access deep nutrients. Irrigation critical - frequent applications (every 3-5 days peak 
season) necessary. Reduced plant population (26,000-30,000 plants/ac vs 32,000-36,000 optimal) reduces 
competition for limited rooting volume. Consider lodging-resistant hybrids. Yields 75-90% of optimum.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm to restricting layer) or severe 
restrictions (high bulk density >1.6 g/cm³, many coarse fragments >60%, hardpan, bedrock, or very poor 
structure) severely limit corn production. Effective rooting depth <30cm - roots cannot access adequate soil 
volume for corn's moderate to high demands. Corn requires minimum 36-48 inch rooting depth for viable production 
- shallow conditions fundamentally inadequate.

ROOT FAILURE: Crown roots encounter barrier at 30-50cm halting downward growth. Roots forced to grow laterally 
in restricted surface zone creating: extreme drought susceptibility (requires irrigation every 2-3 days), 
inadequate nutrient access (heavy fertilization needed but inefficient), severe lodging risk (shallow root 
plate cannot anchor tall plants), water stress during peak demand (R1-R3 silking/pollination). Root spread 
only 12-18 inches - insufficient for stability or resource acquisition.

VIABILITY ASSESSMENT: Corn production marginal to non-viable in poor rooting conditions. Economics rarely 
favorable - high input costs (frequent irrigation, intensive fertilization) versus reduced yields (50-70% of 
optimal) and quality problems (kernel abortion from water stress). Better alternatives: 1) Sorghum (more 
drought-tolerant, better suited to shallow soils). 2) Short-season crops avoiding late-season drought. 3) 
Soil modification (remove hardpan, deep till) if restriction mechanical not geologic. If attempting corn: 
drip irrigation mandatory, short-season hybrids (95-105 day), reduced populations (22,000-26,000 plants/ac), 
intensive management. Expect yields <120 bu/ac.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
(bedrock, continuous hardpan, dominant coarse fragments >90%, extreme compaction) make corn production impossible. 
Corn's minimum rooting requirement (36 inches effective depth) cannot be met. Root system development inadequate 
for plant survival through grain-filling period.

IMPOSSIBILITY: Corn cannot establish functional root system in very shallow conditions. Plants: remain stunted 
(<3 ft vs 6-8 ft normal), experience continuous water stress even with daily irrigation, show chronic nutrient 
deficiencies, lodge universally (no anchorage), abort silks or fail pollination, produce no grain or <20 bu/ac 
unmarketable corn. Growing season water requirement (20-30 inches) cannot be supplied through irrigation to 
<12 inch root zone - water stress inevitable despite extreme irrigation frequency.

ALTERNATIVES: DO NOT plant corn in very poor rooting conditions. Corn among worst crop choices for shallow 
soils - tall stature requires deep anchorage, moderate-high water needs require deep rooting, grain production 
demands stable adequate moisture. Better alternatives: 1) Very shallow-rooted crops (lettuce, onions, radish 
- if irrigated). 2) Perennial sod (some grasses tolerate shallow soil). 3) Soil reconstruction (import soil, 
deep till with amendment, remove rock) before attempting row crops. 4) Alternative land use (not suitable 
for conventional agriculture)."""
    },

    "Soybeans": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports soybeans' 
taproot system: strong central taproot (to 100-150cm) with extensive lateral branches (concentrated 0-30cm). 
In excellent conditions, soybeans develop 4-6 ft deep taproot with lateral roots spreading 18-24 inches. Good 
structure and low bulk density allow excellent nodulation throughout rooting zone - critical for N-fixation.

ROOT-NODULE RELATIONSHIP: Excellent rooting conditions support prolific nodulation. Nodules form on lateral 
roots primarily in top 12-18 inches but can occur to 36 inches in unrestricted soil. More extensive root 
system = more nodulation sites = greater N-fixation (100-200 lb N/ac). Deep rooting accesses moisture during 
pod-fill (R3-R6) - most critical water-sensitive period. Drought stress during pod-fill drastically reduces 
yields; deep roots provide buffering against stress.

TAPROOT ADVANTAGES: Soybeans' taproot system more efficient than fibrous-rooted crops at exploiting deep 
subsoil moisture and nutrients. Taproot penetrates restrictive layers better than fibrous roots. In excellent 
conditions, taproots reach 5-6 ft accessing moisture unavailable to shallow-rooted crops. This provides 7-10 
day irrigation intervals vs 3-5 days in restricted soils. Excellent rooting supports maximum yield potential 
(60-80 bu/ac), consistent performance, and efficient resource use.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 3-5 ft. Some resistance in subsoil (moderate bulk density, moderate structure, 
few coarse fragments) may slow but doesn't prevent deep rooting. Soybean taproots have strong penetrating 
ability - can push through moderately dense layers that stop fibrous roots.

ROOT SYSTEM DEVELOPMENT: Taproot penetrates to 80-120cm with well-developed lateral branches in top 30cm. 
Nodulation excellent in upper profile where structure good. May have reduced nodulation in compacted subsoil 
zones but most nodules form in top 18 inches anyway. Root system provides: adequate N-fixation (80-180 lb 
N/ac), good drought buffering (5-7 days between irrigations during pod-fill), sufficient anchorage (lodging 
minimal), efficient nutrient uptake.

MANAGEMENT: Deep tillage every 3-5 years can improve taproot penetration if traffic pan present. Ensure 
proper inoculation (Bradyrhizobium japonicum) at planting - excellent rooting magnifies benefits of good 
nodulation. Standard row spacing and populations effective. Irrigation needed during R3-R6 (pod development 
and fill) especially - schedule based on soil moisture monitoring at 24-36 inch depth. Yields 90-100% of 
optimal. Generally excellent performance.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or moderate 
restrictions limit taproot penetration to 2-4 ft. Soybean taproots have advantage over fibrous-rooted crops 
- can penetrate moderately resistant layers fairly well. However, restrictions still reduce effective rooting 
depth and lateral root development. Nodulation may be reduced in compacted or poorly structured zones.

ROOT CHALLENGES: Taproot reaches 60-100cm before encountering significant resistance (compact B-horizon, 
gravelly layer, clay pan). This reduces: subsoil moisture access (increased drought sensitivity during pod-
fill R3-R6), total nodulation (limited lateral root development = fewer nodulation sites), deep nutrient 
scavenging, anchorage (some lodging risk in tall varieties or wet conditions). Lateral roots concentrated in 
top 24 inches.

MANAGEMENT STRATEGIES: Deep tillage (subsoiling 18-24 inches) before planting can significantly improve 
taproot penetration through mechanical restrictions. Won't help with geologic barriers (rock, dense clay). 
Ensure excellent nodulation through proper inoculation - especially critical when rooting limited. May benefit 
from starter N (20-30 lb N/ac) if nodulation uncertain. Irrigation essential during R3-R6 pod-fill period - 
frequent applications (every 4-6 days). Narrow rows (15-20 inches vs 30 inches) capture more water in root 
zone. Shorter-season varieties (Group III-IV vs V-VI) reduce late-season drought exposure. Yields 70-85% of 
optimal.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
taproot to <2 ft effective depth. Even soybeans' penetrating taproot cannot overcome severe physical barriers 
(shallow bedrock, hardpan, extreme compaction). Shallow rooting severely limits water and nutrient access. 
Nodulation reduced by limited root volume - N-fixation may be only 40-80 lb N/ac requiring supplemental N 
fertilization (unusual for soybeans).

ROOT SYSTEM FAILURE: Taproot encounters impenetrable barrier at 30-60cm. Forced to branch laterally in 
restricted surface zone creating: extreme drought sensitivity (especially R3-R6 pod-fill - most critical 
period), inadequate nodulation (limited lateral roots = few nodulation sites), poor N-fixation (may need 
60-100 lb fertilizer N/ac), lodging susceptibility (weak anchorage), continuous nutrient stress. Root system 
cannot support plant through reproductive period without intensive inputs.

VIABILITY: Soybeans more viable than corn in poor rooting conditions (lower water requirement, more drought-
tolerant) but still marginal. Economics questionable - intensive irrigation plus possible N fertilization 
(expensive for soybeans normally requiring no N) versus moderate yields (30-50 bu/ac). Better alternatives: 
1) Edamame (vegetable soybeans, shorter season, higher value). 2) Dry beans (some types more drought-tolerant). 
3) Soil modification before planting. If attempting soybeans: drip irrigation mandatory, very short-season 
varieties (Group I-II, 90-100 days), narrow rows (7-15 inches), intensive inoculation, supplemental N if 
nodulation poor. Yields typically 40-60% optimal.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
prevent functional taproot development. Soybeans' minimum rooting requirement (24-36 inches effective depth) 
cannot be met. Taproot system essential for soybean success - plants cannot survive to maturity with <12 inch 
effective rooting.

ROOT SYSTEM IMPOSSIBILITY: Taproot hits barrier at <12 inches forcing all growth lateral in surface crust. 
Plants: remain stunted (<12 inches tall vs 24-36 normal), lodge immediately (no taproot anchor), show severe 
drought stress daily, cannot nodulate effectively (essentially zero N-fixation), drop flowers/pods continuously, 
produce <10 bu/ac if any seed at all. Pod-fill period (R3-R6) requires consistent adequate moisture - impossible 
to supply with <12 inch root zone even with multiple daily irrigations.

ALTERNATIVES: DO NOT plant soybeans in very poor rooting conditions. Soybeans require functional taproot 
system - fundamental to species biology. Without taproot: no deep moisture access, no adequate anchorage, no 
effective nodulation, no viable yields. Better alternatives: 1) Extremely shallow-rooted crops only (lettuce, 
radish, onions). 2) Complete soil reconstruction before attempting grain crops. 3) Alternative non-agricultural 
land use. Among grain legumes, soybeans actually WORSE choice than some others for very shallow soils - peas, 
lentils have shallower more fibrous roots better suited to thin soils."""
    },

    "Winter Wheat": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports winter 
wheat's extensive fibrous root system: seminal roots (developing from seed through fall and early spring) 
penetrating to 60-120cm, and crown roots (emerging in spring, bulk of root mass) concentrated 0-60cm. In 
excellent conditions, winter wheat develops 4-5 ft deep roots with remarkable efficiency - highest root:shoot 
ratio among small grains.

WINTER ROOT DEVELOPMENT: Critical advantage of winter wheat over spring types is fall root establishment. 
After September/October planting, seminal roots develop during mild fall weather penetrating to 30-60cm 
before winter dormancy. This gives winter wheat: deeper rooting than spring crops (established before soil 
freezes), better spring drought tolerance (existing deep roots access moisture), more efficient nutrient 
scavenging (roots in place when spring mineralization begins), excellent anchorage (early establishment 
prevents lodging).

ROOT SYSTEM EFFICIENCY: Winter wheat has most extensive root system among cereals relative to shoot size. 
Root length density 2-4 cm root/cm³ soil in top 30cm - extremely efficient at extracting water and nutrients. 
Deep roots (to 120cm in excellent conditions) access subsoil moisture critical during grain-fill (Feekes 10-
11). Excellent rooting supports: high yields (80-100+ bu/ac), efficient nitrogen use (reduced leaching losses), 
drought resistance during critical spring periods, strong stems resisting lodging.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good root development to 3-4 ft. Winter wheat's fibrous root system adapts well to moderate bulk density or 
structure limitations - smaller diameter roots can exploit smaller pores than tap-rooted crops. Fall establishment 
crucial - seminal roots penetrate to 45-90cm before dormancy.

FALL ESTABLISHMENT CRITICAL: September-October planting allows 6-10 weeks root growth before winter. Mild 
falls with good rooting conditions produce deep seminal roots (24-36 inches) providing: excellent overwinter 
survival (deep roots access moisture if surface dry), rapid spring growth (existing root system supports early 
vigor), better drought tolerance heading through grain-fill, reduced spring N losses (roots throughout profile 
capture early mineralized N). Good rooting conditions maximize fall root advantage.

SPRING ROOT GROWTH: Crown roots emerge in spring (March-April) from crown just below soil surface. These 
constitute 70-80% of final root mass. Develop primarily in top 18-24 inches with some penetration to 36-48 
inches. Good structure and moderate bulk density allow efficient crown root development. Total root system 
(fall seminal + spring crown roots) provides adequate water and nutrient uptake for good yields (70-90 bu/ac), 
moderate drought buffering, strong anchorage.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
(compaction, structure, coarse fragments) limit winter wheat to 2-3 ft effective rooting. Still better than 
spring small grains - fall root establishment provides advantage even in restricted soils. However, limitations 
reduce the efficiency that makes winter wheat superior to spring types.

RESTRICTED ROOT DEVELOPMENT: Fall seminal roots may reach only 18-30 inches before encountering resistance 
(plow pan, dense B-horizon, coarse layer). This reduces winter wheat's primary advantage over spring grains. 
Spring crown roots concentrated in top 12-18 inches above restriction. Total effective rooting depth 24-36 
inches adequate for moderate production but limits: drought tolerance (spring dry periods reduce tillering 
and grain-fill), deep nutrient access (must rely on fertilization), late-season moisture (grain-fill period 
sensitive to stress).

MANAGEMENT ADAPTATIONS: Deep tillage in late summer before planting can significantly improve fall root 
establishment - critical for winter wheat's advantage. Subsoiling to 18-24 inches breaks pans allowing seminal 
roots deeper penetration. Earlier planting (early September vs late September) provides extra fall root growth 
time before cold. Slightly higher seeding rates (1.2-1.5 million seeds/ac vs 1.0-1.2 optimal) compensate for 
less-efficient rooting. Split N applications (fall, early spring, jointing) match uptake pattern with restricted 
rooting. Irrigation during Feekes 8-11 (heading through grain-fill) critical if rooting limited. Yields 55-
75 bu/ac typical.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
winter wheat to <2 ft rooting. Even winter wheat's fall-established root advantage cannot overcome severe 
physical barriers. Shallow rooting eliminates many benefits of winter wheat over spring types. Economics 
marginal - intensive management required for moderate yields.

ROOT LIMITATION IMPACTS: Fall seminal roots reach only 12-24 inches before hitting barrier. Spring crown 
roots concentrated in top 6-12 inches. Shallow combined root system creates: severe drought vulnerability 
(especially Feekes 10-11 grain-fill), poor nutrient efficiency (leaching below root zone), inadequate anchorage 
(lodging risk in tall varieties or wet conditions), low yield potential (30-50 bu/ac maximum). Winter wheat's 
advantage over spring wheat reduced - may perform similarly to spring types in poor rooting conditions.

VIABILITY ASSESSMENT: Winter wheat marginally better choice than spring wheat in poor rooting (fall roots 
provide some advantage) but both limited. Consider alternatives: 1) Spring wheat (simpler management, no 
overwinter risk, similar performance). 2) Triticale (more drought-tolerant than wheat, deeper rooting). 3) 
Winter barley (shorter season, lower water needs). 4) Soil modification before attempting cereals. If growing 
winter wheat: deep tillage before planting essential, early planting (early September) for maximum fall 
rooting, high seeding rates (1.5-1.8 million/ac), intensive split N program, irrigation mandatory Feekes 8-
11, short-straw varieties (reduce lodging), PGRs (plant growth regulators) if lodging risk. Expect yields 
35-55 bu/ac.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
prevent viable winter wheat production. Winter wheat's minimum rooting requirement (24-30 inches effective 
depth) cannot be met. Fall seminal roots cannot establish adequate depth; spring crown roots restricted to 
surface crust. Combined root system inadequate for overwintering survival and spring growth.

OVERWINTER FAILURE: Critical problem in very shallow soils is overwinter survival. Fall-seeded wheat develops 
inadequate root system (<12 inches) before winter. Shallow roots: heave out during freeze-thaw cycles (lacking 
deep anchorage), desiccate during winter dry periods (cannot access moisture), freeze damage more severe 
(surface temperature fluctuations), poor survival (30-60% winterkill vs <5% normal). Spring regrowth from 
survivors weak and patchy. Stands too thin for viable production even if plants survive.

SPRING GROWTH FAILURE: If plants survive winter, spring growth severely limited by <12 inch rooting. Plants: 
remain stunted (<12 inches tall vs 30-36 inches normal), tiller poorly (1-2 tillers vs 3-5 normal), head 
poorly (many tillers abort before heading), produce tiny heads (10-20 kernels vs 35-50 normal), yield <15 
bu/ac if anything. Grain-fill impossible without adequate moisture - very shallow roots cannot sustain even 
with daily irrigation.

ALTERNATIVES: DO NOT plant winter wheat in very poor rooting conditions. Among cereals, winter wheat actually 
WORST choice for very shallow soils - overwinter requirement adds survival challenge to rooting limitation. 
Better alternatives: 1) Spring cereals if attempting grain (no overwinter risk, similar poor performance but 
easier management). 2) Spring oats (most shallow-soil tolerant cereal, though still poor). 3) Extremely 
shallow-rooted crops only (lettuce, radish, onions). 4) Non-agricultural use. Winter wheat's fall-rooting 
advantage becomes disadvantage in very shallow soils - plants establish inadequately then face overwinter 
stress."""
    },

    "Alfalfa": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil absolutely essential 
for alfalfa - THE deepest-rooted common field crop. In excellent conditions, alfalfa develops massive taproot 
system: primary taproot penetrating 6-12+ ft (2-4 meters), lateral roots branching at multiple depths, root 
system exploring huge soil volume. Deep rooting is DEFINING characteristic of alfalfa making it uniquely 
drought-tolerant and long-lived.

EXTREME DEEP ROOTING: Alfalfa taproots can reach 15-20 ft (5-7 meters) in deep soils with multi-year stands. 
First-year seedlings establish taproot to 3-5 ft. Second year: 6-10 ft. Mature stands (3+ years): 8-15 ft 
common, some roots to 20 ft documented. This extreme rooting allows: exceptional drought tolerance (access 
moisture unavailable to all other crops), mining nutrients from deep subsoil (phosphorus, calcium from zones 
beyond fertilization), survival during extended drought (dormancy while maintaining deep roots), stand longevity 
(4-7+ year productive stands).

DEEP SOIL REQUIREMENT: Alfalfa's productivity directly proportional to effective rooting depth. Research 
shows: soil depth 0-3 ft (poor production, short stand life), 3-6 ft (moderate production, 3-4 year stands), 
6-9 ft (good production, 4-6 year stands), >9 ft (excellent production, 5-8+ year stands). Restricting layer 
at any depth severely limits alfalfa potential. Excellent rooting conditions (no barriers to 8-12+ ft) essential 
for economic alfalfa production supporting maximum yields (8-12 tons/ac), excellent stand persistence, efficient 
water use.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm = 3-5 ft) with minor restrictions 
allows good but not optimal alfalfa production. Taproot can penetrate to 4-6 ft in good conditions but this 
is LESS than alfalfa's genetic potential (8-15+ ft). Somewhat adequate for moderate production (5-8 tons/ac) 
but restricts stand longevity (3-4 years vs 5-7+ years optimal).

ROOTING DEPTH LIMITATION: Taproot reaches 4-6 ft before encountering resistance (moderate compaction, bulk 
density increasing with depth, coarse fragments, or clay B-horizon). This provides better drought tolerance 
than shallow-rooted crops but MUCH less than alfalfa's potential. Deep roots access some subsoil moisture 
but not deep reserves accessed by 10-15 ft roots. Stand productivity declines after year 3-4 as easily 
accessible resources depleted and deep subsoil reserves unavailable.

MANAGEMENT IMPLICATIONS: Good rooting conditions acceptable for: shorter rotation alfalfa (3-4 years then 
replant vs 5-7+ year stands), irrigated production (deep rooting less critical with irrigation though still 
beneficial), moderate yield expectations (6-8 tons/ac, 3-4 cuts vs 8-12 tons, 4-6 cuts optimal). NOT ideal 
for: dryland alfalfa (requires deepest possible rooting), long-term stands (will decline after 3-4 years), 
maximum production goals. Consider alternatives if rooting limited: 1) Red clover or other medium-rooted 
legumes (less demanding). 2) Irrigation to supplement limited rooting volume. 3) Plan for shorter stand life 
and earlier replanting.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm = 1.5-3 ft) or 
restrictions severely limit alfalfa - does NOT meet alfalfa's minimum rooting requirement of 3-5 ft for viable 
production. Taproot reaches only 2-4 ft before barrier. This fundamentally inadequate for crop requiring 6-
12+ ft rooting for genetic potential.

ALFALFA UNSUITABILITY: Moderate rooting conditions NOT RECOMMENDED for alfalfa. Problems: Stand establishment 
poor (first-year taproot cannot develop adequately), productivity low (3-5 tons/ac vs 8-12 optimal), stand 
longevity very short (1-2 years vs 5-7+), drought tolerance minimal (defeats purpose of deep-rooted legume), 
frequent replanting needed (high costs), poor economics (establishment costs $300-500/ac cannot be amortized 
over 1-2 year stand). Alfalfa's advantages (deep rooting, drought tolerance, longevity) lost in moderate 
rooting - becomes expensive short-lived crop with no advantages over shallow-rooted alternatives.

BETTER ALTERNATIVES: In moderate rooting conditions, choose crops better suited to limited depth: 1) Red 
clover (rooting 2-4 ft, similar forage quality, 2-3 year stands, much better adapted). 2) White clover (1-2 
ft rooting, perennial but different use). 3) Birdsfoot trefoil (2-3 ft rooting, 3-4 year stands, bloat-safe). 
4) Annual legumes (crimson clover, hairy vetch - single season, no perennial requirement). DO NOT plant alfalfa 
in moderate rooting - economically and agronomically poor choice. Alfalfa's deep rooting requirement is 
fundamental not optional.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm = 10-20 inches) absolutely 
UNSUITABLE for alfalfa production. Taproot reaches only 12-24 inches before impenetrable barrier. This is 
10-20% of alfalfa's genetic rooting potential (10-15+ ft). Attempting alfalfa in poor rooting conditions 
economic and agricultural disaster.

ALFALFA FAILURE: Establishment fails or produces unacceptable stands. First-year seedlings: develop 12-18 
inch taproot then stop (barrier encountered), plants stressed continuously (inadequate rooting volume), 
winterkill common (shallow roots heave and freeze), many plants die first year (30-60% loss vs <10% normal). 
Survivors: remain stunted and weak, produce <2 tons/ac (vs 8-12 optimal), compete poorly with weeds (stress-
weakened), die after 1 year (no second-year production). Stand completely fails before establishment costs 
recovered.

ECONOMIC DISASTER: Alfalfa establishment costs $300-500/ac (seed, inoculation, lime, fertilizer, herbicides, 
equipment). Normally amortized over 5-7 years ($50-100/ac/year). In poor rooting, stand fails after 1 year: 
full establishment cost + one year production costs ($400-700 total) versus <2 tons/ac yield ($200-400 value) 
= net loss $200-500/ac. Then must replant for second year repeating losses. Continuous disaster.

ALTERNATIVES: NEVER plant alfalfa in poor rooting conditions. Among all field crops, alfalfa has DEEPEST 
rooting requirement - absolute worst choice for shallow soils. Instead: 1) Annual forages (avoid perennial 
establishment requirement). 2) Very shallow-rooted legumes (white clover, lowest requirement). 3) Grasses 
(some tolerate shallow soils better than legumes). 4) Soil modification (deep till, remove barriers) before 
considering perennial legumes. Alfalfa in shallow soil is guaranteed failure.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm = <10 inches) or 
extreme restrictions make alfalfa production COMPLETELY IMPOSSIBLE. Alfalfa has HIGHEST rooting requirement 
of all common field crops (genetic potential 10-20+ ft, minimum viable requirement 3-5 ft). Very shallow 
soil provides <10% of minimum requirement. Attempting alfalfa is complete impossibility not just poor economics.

ABSOLUTE IMPOSSIBILITY: Alfalfa seedlings cannot survive in very shallow soil. Seeds germinate but: taproot 
hits barrier at 6-12 inches within 2-4 weeks of emergence, growth stops immediately (taproot development 
essential for alfalfa), plants wilt and die within weeks (cannot access adequate moisture), essentially 100% 
stand failure (no viable plants survive first 6-8 weeks). Even with perfect care (daily irrigation, intensive 
fertilization), alfalfa seedlings die when taproot cannot penetrate. This is biological impossibility not 
management challenge.

DEEP-ROOTING ESSENTIAL: Alfalfa evolved as deep-rooted drought-tolerant perennial legume. Deep taproot is 
FUNDAMENTAL to species biology: 1) Drought survival (dormancy supported by deep roots accessing permanent 
moisture). 2) Nutrient mining (phosphorus, calcium from deep subsoil). 3) Perennial survival (overwinter and 
summer dormancy maintained by deep carbohydrate-storing taproot). 4) Nitrogen fixation (nodules throughout 
root system to great depth). Without deep taproot, alfalfa cannot function as species evolved.

DO NOT ATTEMPT: Alfalfa in very poor rooting conditions is MOST impossible crop-soil combination in all 
agriculture. More impossible than: corn in very shallow soil (corn can at least germinate and grow weeks 
before dying), trees in very shallow soil (some dwarfed trees survive), even most deep-rooted trees in shallow 
soil (alfalfa requires DEEPEST rooting). Any other crop or land use infinitely better choice than attempting 
alfalfa in very shallow soil."""
    },

    "Spring Wheat": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports spring 
wheat's fibrous root system: seminal roots (from seed) and crown roots (from crown near surface) developing 
simultaneously through short growing season. In excellent conditions, spring wheat develops 3-4 ft roots 
rapidly (full depth reached within 60-70 days vs 90+ days for winter wheat). Speed of root establishment 
critical in short season (90-120 days vs 240+ for winter wheat).

RAPID ROOT DEVELOPMENT: Spring wheat must establish complete root system quickly - entire growth compressed 
into 3-4 months. Day 0-30: seminal roots to 18-24 inches, Day 30-60: crown roots developing rapidly in top 
12-18 inches plus seminal roots to 36-48 inches, Day 60-90: full root system 36-48 inches supporting grain-
fill. Excellent rooting conditions (low resistance, good structure) essential for rapid penetration. Any 
delay in rooting reduces yield potential in short season.

ROOT EFFICIENCY: Spring wheat has similar root architecture to winter wheat but less total root mass (shorter 
development time). Must be MORE efficient per unit root length to achieve comparable yields. Root length 
density 1.5-3 cm/cm³ in top 30cm - very efficient extraction. Deep roots (to 120cm in excellent conditions) 
provide: adequate water for grain-fill (most critical phase), nutrient scavenging throughout profile, moderate 
drought buffering (5-7 days), adequate anchorage. Excellent rooting supports 60-80 bu/ac in favorable climate.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good root development to 3-4 ft. Spring wheat's fibrous roots adapt well to moderate limitations - smaller 
diameter roots exploit smaller pores effectively. Critical difference from winter wheat: NO fall establishment 
period, must develop entire root system spring through early summer.

TIME LIMITATION: Spring wheat planted April-May must: establish seedling roots (2-3 weeks), develop full 
root system (6-8 weeks), support grain-fill (4-5 weeks), mature (2-3 weeks) - all within 90-120 days. Good 
rooting conditions allow adequate root development within tight timeline. Moderate bulk density or structure 
issues slow but don't prevent rooting - still reaches 30-40 inches effective depth adequate for moderate 
production (50-70 bu/ac).

COMPARED TO WINTER WHEAT: Spring wheat in good rooting conditions performs similarly to winter wheat in 
moderate conditions. Lacks fall-established deep seminal roots but compensates with rapid simultaneous 
development of seminal and crown roots. Good structure critical - spring root development occurs during active 
growth period when delays directly reduce yield. Adequate drought tolerance for most spring wheat regions 
(northern plains, mountain valleys) where growing season rainfall usually adequate.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
challenge spring wheat's tight development schedule. Unlike winter wheat (can establish fall roots before 
restrictions matter), spring wheat encounters barriers during critical rapid growth phase (May-June). Effective 
rooting depth limited to 24-30 inches - marginal for 90-120 day season.

ROOT DEVELOPMENT SLOWED: Restrictions (compaction, structure, barriers) delay root penetration during period 
when every week matters. Normal spring wheat timeline: Week 0-3 (germination, seedling roots), Week 4-8 
(rapid crown root development + seminal deepening), Week 9-13 (grain-fill supported by established roots). 
Moderate restrictions add 1-2 weeks to root establishment reducing grain-fill period - directly lowers yields 
(35-55 bu/ac vs 60-80 optimal).

MANAGEMENT CHALLENGES: Deep tillage before planting helps if restrictions mechanical (plow pan, traffic 
compaction) but spring wheat planted early when soil often too wet for deep tillage. Fall deep tillage 
(previous year) beneficial but rare practice for spring grains. Earlier planting (maximize growing season) 
conflicts with soil workability. Irrigation helpful during grain-fill if available. Consider: short-season 
varieties (85-95 days, less demanding rooting), higher seeding rates (compensate for less-efficient rooting), 
alternative crops (spring barley, oats more tolerant).""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions severely 
limit spring wheat viability. Effective rooting depth <24 inches inadequate for 90-120 day grain crop. Spring 
wheat's compressed development timeline makes poor rooting MORE limiting than for winter wheat - no fall 
establishment buffer, must overcome barriers during active growth when delays critical.

ROOT FAILURE IN SHORT SEASON: Roots encounter barrier at 18-30 inches within 4-6 weeks of planting. Remaining 
6-10 weeks must support: full vegetative development, heading, flowering, grain-fill, maturation - all with 
inadequate root volume. Results: stunted plants (<18 inches tall vs 30-36 normal), reduced tillering (1-2 
vs 3-4), small heads (15-25 kernels vs 35-50), continuous water stress (shallow roots cannot buffer dry 
periods), low yields (20-40 bu/ac) even with intensive management.

ALTERNATIVES BETTER SUITED: Spring wheat among POOREST choices for shallow soils. Better options: 1) Spring 
barley (more shallow-soil tolerant, lower moisture requirement, 80-90 day season vs 90-120). 2) Oats (most 
shallow-soil tolerant cereal, 90-100 days, useful as feed even if grain poor). 3) Spring peas (shorter season 
60-90 days, shallower rooting adequate). 4) Consider NO spring grain - summer annual crops allowing time for 
soil preparation. Economics rarely favorable - spring wheat grain value modest ($5-7/bu) cannot justify 
intensive inputs required.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes spring wheat 
production impossible. Spring wheat's minimum rooting requirement (24-30 inches effective depth for 90-120 
day season) cannot be met. Unlike winter wheat which at least establishes fall roots before facing restrictions, 
spring wheat encounters barriers immediately during critical seedling period.

RAPID FAILURE: Spring wheat planted into very shallow soil: germinates normally (soil depth adequate for 
germination 0-2 inches), develops seedling seminal roots to 6-12 inches (weeks 1-3), hits impenetrable 
barrier (week 3-4), root growth stops while shoot continues (imbalanced development), plants become severely 
stressed (week 5-6), stands fail or produce no grain (weeks 8-12). Growing season too short for multiple 
planting attempts - one failure means crop year lost.

IMPOSSIBILITY IN SHORT SEASON: Spring wheat must accomplish in 90-120 days what takes winter wheat 240+ 
days. Very shallow rooting removes ANY margin for stress. Plants: cannot establish adequate crown roots 
(confined to top 6-12 inches), have no deep moisture reserves (daily water stress even with irrigation), 
produce minimal biomass (<6 inches tall), abort flowering or produce empty heads, yield <10 bu/ac if anything. 
Spring weather variability (late frost, early heat, variable rainfall) compounds stress - shallow roots cannot 
buffer ANY environmental challenge.

DO NOT ATTEMPT: Spring wheat in very poor rooting conditions guaranteed failure. Among spring grains: spring 
barley slightly better (more stress-tolerant), oats more better still (most forgiving), but NONE viable in 
very shallow soil. If attempting spring grain crop in very poor rooting: complete soil reconstruction 
mandatory, or choose non-grain crops (shallow-rooted vegetables with irrigation, or non-agricultural use)."""
    },

    "Cotton": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports cotton's 
extensive taproot system: strong central taproot (to 6-10 ft) with major lateral branches at multiple depths, 
secondary laterals creating dense feeding network in top 3-4 ft. Cotton is DEEP-ROOTED crop requiring 5-8 ft 
minimum effective depth for commercial production. Excellent conditions allow maximum rooting supporting long 
season (160-190 days) and heavy boll load.

TAPROOT-BASED SYSTEM: Cotton develops powerful taproot growing 2-3 inches/day during seedling stage, reaching 
5-6 ft by first square (45-60 days), 8-10+ ft by peak bloom (90-120 days). Lateral roots develop in tiers: 
upper laterals (0-18 inches, dense feeding roots), middle laterals (18-36 inches, major water uptake), deep 
laterals (36-72+ inches, deep water access, nutrient mining). Excellent rooting essential for: long season 
water supply (20-35 inches over 160-190 days), nutrients for high yields (2+ bales/ac), anchorage for heavy 
boll load, drought tolerance during critical boll development (first square through maturity).

DEEP ROOTING ADVANTAGES: Cotton's deep taproot allows production in water-limited environments where shallow-
rooted crops fail. Accesses deep subsoil moisture unavailable to most crops. In excellent conditions: supports 
2.5-3+ bales/ac yields, provides 10-14 day irrigation intervals (vs 5-7 shallow-rooted crops), allows delayed 
final irrigation (deep roots sustain late boll maturation), gives insurance against mid-season drought stress 
(critical during flowering/boll set). Strong taproot anchorage prevents lodging even with heavy boll loads.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm = 3-5 ft) with minor restrictions 
allows good taproot development to 4-6 ft. Cotton's powerful taproot can penetrate moderately resistant layers 
- better than fibrous-rooted crops at overcoming subsoil compaction. However, 4-6 ft depth is LESS than 
cotton's genetic potential (8-12+ ft) and somewhat limits production potential.

ADEQUATE BUT LIMITED DEPTH: Taproot reaches 4-6 ft encountering moderate resistance (increasing bulk density, 
B-horizon, moderate coarse fragments). This provides: adequate rooting for 1.5-2.5 bale/ac production, 
moderate drought buffering (7-10 day irrigation intervals), sufficient deep moisture access for most seasons, 
good anchorage. However, lacks FULL drought insurance of 8-10+ ft rooting - vulnerable during extended dry 
periods or late-season stress.

MANAGEMENT IMPLICATIONS: Deep tillage (subsoiling 18-30 inches) before planting can significantly improve 
taproot penetration if restrictions are mechanical (traffic pan, plow pan, natural compaction). Benefits 
most visible in mid-late season when deep roots become critical. Irrigation scheduling moderate - more frequent 
than deep-rooted cotton but less than shallow crops. Fertility placement at multiple depths captures different 
root zones. Good rooting conditions adequate for most cotton production; excellent conditions needed only for 
maximum yields or rainfed production.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm = 20-40 inches) 
or restrictions limit cotton's taproot to 3-4 ft effective depth. This is MARGINAL for cotton production - 
barely meets minimum rooting requirement for commercial viability. Cotton requires deeper rooting than most 
annual crops due to long season (160-190 days) and high water demands (25-35 inches).

ROOT LIMITATION SEVERE: Taproot encounters significant barrier at 36-48 inches. Forced to develop extensive 
lateral system in upper 3 ft but lacks deep drought-insurance roots. Creates: moderate drought vulnerability 
(irrigation every 5-7 days during peak demand vs 10-14 optimal), reduced boll retention under stress (squares 
and young bolls shed if water-stressed), lower yields (1-1.5 bales/ac vs 2+ optimal), shortened fruiting 
period (early cutout to conserve limited resources), increased lodging risk (shallower anchorage vs heavy 
late-season boll load).

VIABILITY ASSESSMENT: Cotton marginal in moderate rooting conditions. Economics questionable: high establishment 
costs ($200-400/ac), long season risk (160-190 days), high water inputs needed (irrigation critical), versus 
moderate yields (1-1.5 bales/ac = $600-1000/ac value). Better alternatives: 1) Shorter-season crops (avoid 
late-season water stress). 2) Grain sorghum (deep-rooted but more drought-tolerant, shorter season). 3) 
Soybeans (shorter season, lower water needs). If attempting cotton: deep ripping critical, frequent irrigation 
mandatory, early-maturing varieties (reduce season length), intensive management throughout season.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm = 10-20 inches) or severe 
restrictions make cotton production non-viable. Cotton's minimum rooting requirement (48-60 inches effective 
depth) cannot be met. Taproot system fundamental to cotton's ability to produce over long season - shallow 
rooting prevents commercial production.

TAPROOT FAILURE: Taproot hits impenetrable barrier at 18-30 inches, often during first 3-5 weeks. Forced 
entirely lateral creates: shallow root plate (top 12-24 inches only), extreme drought sensitivity (irrigation 
every 3-4 days or plants shed), continuous water stress during 160-190 day season (unsustainable irrigation 
frequency), square and boll shedding (stress response), early cutout (plants go reproductive prematurely 
trying to make seed before death), severe lodging (late-season plants fall over - shallow anchorage cannot 
support boll load), yields <0.5-0.8 bales/ac (not economically viable).

ECONOMICS IMPOSSIBLE: Cotton establishment costs $200-400/ac (seed, herbicides, insecticides, equipment). 
Season-long costs another $300-600/ac (irrigation, additional pesticides, harvest). Total investment $500-
1000/ac to produce <0.5-0.8 bales/ac worth $350-550. Guaranteed loss $150-450/ac. Cannot recover costs even 
with perfect management and favorable prices.

ALTERNATIVES: NEVER plant cotton in poor rooting conditions. Cotton among WORST choices for shallow soils - 
long season, high water needs, deep rooting essential. Better alternatives: 1) Short-season crops avoiding 
late summer stress. 2) Shallow-rooted high-value crops with irrigation (vegetables). 3) Perennial forages 
(some tolerate shallow soil). 4) Grain sorghum if attempting row crop (more stress-tolerant).""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm = <10 inches) makes 
cotton production absolutely impossible. Cotton has high rooting requirement among annual crops (minimum 
48-60 inches, optimal 8-12+ ft). Very shallow soil provides <20% of minimum requirement. Cotton's long season 
(160-190 days) and taproot architecture make it completely unsuited to restricted rooting.

BIOLOGICAL IMPOSSIBILITY: Cotton seedlings emerge normally but: taproot hits barrier at 6-12 inches (week 
2-3 after planting), root growth stops while shoot continues (severe imbalance), plants become stunted (6-12 
inches tall vs 36-48 normal), water stress begins immediately (even with daily irrigation - root volume 
inadequate), plants shed continuously (squares, blooms, young bolls - stress response), cutout prematurely 
(week 6-8 vs 14-16 normal - trying to make seed before death), produce no harvestable bolls or <100 lb lint/ac 
(vs 1000+ lb/ac = 2 bales commercial production), stands collapse mid-season (lodging from shallow roots).

LONG SEASON IMPOSSIBILITY: Cotton's 160-190 day season requires sustained water supply. Water requirement 
2-3 inches/week peak season (bloom through boll development, weeks 9-16). Very shallow rooting (<10 inches 
effective depth) holds <1 inch available water. Requires irrigation every 2-3 DAYS for 4+ MONTHS - economically 
and practically impossible. Even with perfect irrigation, plants cannot sustain physiological processes without 
adequate root system.

DO NOT ATTEMPT: Cotton in very poor rooting conditions is complete impossibility. Among common field crops, 
cotton has ONE of highest rooting requirements (only alfalfa, sugar beets, sunflowers similarly demanding). 
Absolutely WORST annual crop choice for very shallow soils. Any other crop infinitely better option. Attempting 
cotton guaranteed 100% loss of all inputs."""
    },

    "Grain Sorghum": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports sorghum's 
exceptionally extensive root system - THE most efficient root system among major cereals. Develops: powerful 
taproots (to 5-8 ft), extensive laterals at multiple depths, extremely high root length density (3-5 cm root/
cm³ soil in top 30cm - highest among grain crops), dense network of fine feeding roots. Sorghum's root 
efficiency explains its superior drought tolerance and stress resistance.

SUPREME ROOT EFFICIENCY: Sorghum develops MORE extensive root system than corn in SAME conditions. Research 
shows: 40-60% greater root length density than corn, roots penetrate 20-30% deeper than corn, root:shoot 
ratio higher than any other major cereal, fine root production (absorptive surface area) exceeds corn by 50-
70%. This gives sorghum: superior water extraction (can extract water to -15 to -20 bars vs corn -12 to -15 
bars), better nutrient scavenging (especially immobile nutrients like P), enhanced stress recovery, remarkable 
drought tolerance.

EXCELLENT CONDITIONS MAXIMIZE EFFICIENCY: In excellent rooting conditions, sorghum's root advantages fully 
expressed: roots reach 6-8+ ft accessing large soil volume, lateral roots spread 24-36 inches from row, dense 
feeding roots exploit every pore. Results: yields competing with corn (150-180 bu/ac in favorable climate), 
efficient resource use (15-20% less water and N than corn for equivalent yield), wide irrigation intervals 
(10-14 days vs 7-10 corn), stress tolerance (can recover from temporary wilting). Sorghum in excellent rooting 
conditions performs exceptionally.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
very good root development to 4-6 ft. Sorghum's efficient root system adapts better than corn to moderate 
limitations - smaller diameter roots penetrate smaller pores, higher root length density compensates for 
some restrictions. This is where sorghum's advantages over corn become evident.

ROOT EFFICIENCY COMPENSATES: In good (not excellent) conditions, sorghum still develops root system superior 
to corn's: penetrates moderately dense layers more effectively (finer roots, greater penetrating force), 
develops higher root density in available soil volume (more roots per unit soil), extracts water more 
efficiently from each depth increment (can access water at lower soil moisture). Results: sorghum performs 
BETTER than corn in identical conditions, requires 10-20% less irrigation than corn, recovers faster from 
temporary drought stress, provides more reliable yields (less year-to-year variation).

PREFERRED OVER CORN: In high rooting conditions (not excellent), sorghum often economically superior to corn: 
yields comparable (120-150 bu/ac sorghum vs 140-170 bu/ac corn), but lower water requirement (18-24 inches 
vs 22-28 inches), less fertilizer need (120-140 lb N/ac vs 140-180 lb N/ac), reduced irrigation costs, better 
stress tolerance, more reliable production. Good rooting conditions ideal for demonstrating sorghum's efficiency 
advantages.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit rooting to 3-4 ft. This is where sorghum SHINES - moderate conditions where sorghum's stress tolerance 
and efficient rooting provide maximum advantage over corn and other cereals. Sorghum specifically evolved for 
marginal conditions.

SORGHUM'S SWEET SPOT: Moderate rooting conditions bring out sorghum's defining characteristics: superior 
drought tolerance (root system maintains function under stress), efficient nutrient uptake (high root density 
compensates for limited volume), water extraction ability (roots access moisture corn cannot), stress recovery 
(goes dormant during stress then resumes growth), lower input requirements (reduced N and water needs). In 
these conditions, sorghum produces 80-120 bu/ac where corn struggles for 60-90 bu/ac.

STRONGLY PREFERRED: In moderate rooting conditions, sorghum is RECOMMENDED crop over corn: more reliable 
yields (less stress-dependent), lower production costs (reduced inputs), better water use efficiency (critical 
with limited rooting), drought insurance (can survive extended dry periods), lower risk (recovers from setbacks). 
Economics strongly favor sorghum: comparable grain value ($3.50-5.50/bu both crops) but 20-30% lower input 
costs and 15-25% more reliable yields. Moderate rooting conditions are exactly what sorghum bred for.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
rooting to 2-3 ft. Even sorghum's exceptional root system and drought tolerance face challenges. However, 
sorghum remains FAR better choice than corn or most other cereals in poor rooting - this is where sorghum's 
evolution for marginal lands most evident.

SUPERIOR TO ALTERNATIVES: In poor rooting conditions, sorghum's advantages critical: root system more efficient 
than any other major cereal (maximizes limited rooting volume), extreme drought tolerance (dormancy capability 
- can shut down and resume), efficient water extraction (accesses moisture other crops cannot), lower water 
requirement (12-18 inches vs 20-30 corn), stress recovery ability (resumes growth after stress periods). 
Produces 50-80 bu/ac where corn yields 30-60 bu/ac or fails completely.

STILL VIABLE OPTION: Even in poor rooting, sorghum economically viable where other grain crops are not. 
Establishment costs low ($40-70/ac), input requirements modest (80-100 lb N/ac, limited irrigation if available), 
yields acceptable (50-80 bu/ac = $200-400/ac value). Can break even or profit where corn loses money. Management: 
reduced populations (30,000-50,000 plants/ac vs 60,000-80,000 optimal) reduces competition for limited 
resources, early-maturing hybrids (95-110 days) avoid late-season stress, irrigation if available greatly 
helps, but dryland still possible in many regions.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
challenge even sorghum. Effective rooting depth <12 inches marginal for grain production. However, sorghum 
STILL more viable than corn or other cereals - remains best grain crop option if cropping very poor rooting 
conditions (though economics questionable for any grain crop).

MOST TOLERANT GRAIN CROP: Among major cereals in very poor rooting: corn IMPOSSIBLE (fails completely), wheat 
IMPOSSIBLE (inadequate rooting for grain fill), barley MARGINAL (possible <30 bu/ac), oats MARGINAL (possible 
as feed grade), sorghum MOST VIABLE (possible 30-50 bu/ac with intensive management). Sorghum's advantages: 
highest root density compensates for minimal volume, extreme drought tolerance allows survival of severe 
stress, dormancy capability - can shut down temporarily, efficient water extraction - uses every drop available, 
lower total water need than other grains.

LIMITED VIABILITY: Even sorghum struggles in very poor rooting. Expect: much reduced stands (many plants die 
under extreme stress), stunted growth (24-36 inches tall vs 48-72 normal), small heads (reduced grain number), 
low yields (30-50 bu/ac with intensive management, 10-30 dryland), questionable economics (inputs may exceed 
value). Consider alternatives: 1) Pearl millet (even more stress-tolerant than sorghum, though less common). 
2) Forage sorghum (silage production may be more viable than grain). 3) Annual forage crops (grazing use). 
4) Non-cropping use. If attempting grain: intensive management mandatory, irrigation if available, low populations, 
expect very modest returns."""
    },

    "Barley": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports barley's 
fibrous root system: seminal roots and crown roots similar to wheat but developing slightly shallower depth 
(3-4 ft vs 4-5 ft wheat). Barley has moderate to shallow rooting compared to other small grains - typically 
20-30% shallower than wheat in same conditions. However, excellent rooting conditions maximize barley's 
efficient but shallow root system.

EFFICIENT SHALLOW ROOTING: Barley develops most root mass in top 2-3 ft with good lateral spread but limited 
deep penetration compared to wheat. Root characteristics: high root length density in top 18-24 inches (very 
efficient water and nutrient extraction), moderate crown root development (3-5 primary crowns vs 4-7 wheat), 
good lateral spread (18-24 inches from row), effective but shallow. In excellent conditions, develops adequate 
depth (36-48 inches) and maximum density supporting high yields (100-120 bu/ac feed, 80-100 bu/ac malting).

ROOTING ADVANTAGES IN EXCELLENT CONDITIONS: Excellent physical conditions allow barley's naturally shallow 
roots to develop optimally: low resistance enables rapid spring root establishment (critical for short season 
90-120 days), good structure supports dense root network in primary uptake zone (top 24 inches), no barriers 
allow maximum achievable depth (42-48 inches adequate for barley). Less dependent on deep rooting than wheat 
- compensates with efficiency in upper profile.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good root development to 30-40 inches - adequate for barley's moderate rooting requirement. Barley less 
demanding of deep rooting than wheat making it BETTER adapted to good (not excellent) conditions. Natural 
shallow rooting suits soils with surface/near-surface limitations.

BARLEY'S ROOTING ADAPTATION: Barley evolved for shorter seasons and more marginal conditions than wheat. 
Root system reflects this: efficient extraction from limited depth (root density higher than wheat in top 
24 inches), faster root establishment (reaches maximum depth in 50-60 days vs 70-90 wheat), less dependent 
on deep moisture (shorter season, lower total water need), adequate anchorage at shallower depth (shorter 
stature than wheat - less lodging risk). In good conditions, develops 30-40 inch root system supporting 80-
100 bu/ac feed barley, 60-80 bu/ac malting quality.

OFTEN PREFERRED OVER WHEAT: In good (not excellent) rooting conditions where subsoil limitations present, 
barley often better choice than wheat: adequate for barley's shallower requirement but marginal for wheat's 
deeper requirement, barley's shorter season (90-120 days vs 100-130 wheat) reduces stress exposure, lower 
water need (15-20 inches vs 18-24 wheat) suits limited rooting volume, matures earlier avoiding late-season 
stress. Economics comparable to wheat with better reliability in marginal rooting.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit rooting to 20-30 inches. This is near barley's minimum rooting requirement but still viable - barley 
MORE tolerant of moderate rooting than wheat or most other small grains. Barley specifically suited to 
shallower soils where wheat struggles.

BARLEY ADVANTAGE EVIDENT: In moderate rooting, barley's adaptation to shallow conditions valuable: rooting 
requirement lower than wheat (24-30 inches minimum vs 30-40 wheat), root efficiency compensates for limited 
depth (dense network in available volume), shorter season requires less total rooting volume (90-110 days vs 
100-130 wheat), lower water demand (12-18 inches vs 18-24 wheat) matches limited rooting capacity. Produces 
50-80 bu/ac feed, 40-60 bu/ac malting where wheat limited to 40-60 bu/ac.

MANAGEMENT FOR MODERATE CONDITIONS: Barley viable in moderate rooting if managed properly: early planting 
(maximize season length before heat/drought stress), adequate fertility in root zone (cannot access deep 
nutrients), irrigation if available during heading-grain fill (most critical water need period), consider 
feed barley vs malting (less quality stress). Economics favor barley over wheat - comparable value, lower 
water need, more reliable yields. Better adapted to moderately restricted rooting than most alternatives.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
rooting to <24 inches - at or below barley's minimum requirement. Marginal for barley production though still 
better than wheat or corn. Among small grains, only oats equally or more tolerant of poor rooting conditions.

MINIMAL VIABLE ROOTING: Barley can survive with 18-24 inch rooting but production severely limited: shallow 
roots cannot buffer drought stress (requires irrigation or favorable rainfall), limited nutrient access (heavy 
fertilization needed, shallow placement), poor anchorage (lodging risk, especially taller feed varieties), 
short season advantage critical (100-110 day varieties minimize stress exposure), yields low (30-50 bu/ac 
feed, 25-40 bu/ac malting if possible). Quality issues common - low test weights, thin kernels, high protein 
(bad for malting).

VIABILITY ASSESSMENT: Barley marginally viable in poor rooting, primarily as feed grain (malting quality 
difficult to achieve). Consider alternatives: 1) Oats (more shallow-soil tolerant, useful even poor quality). 
2) Spring peas (shorter season, shallower rooting). 3) Annual forages (avoid grain quality issues). If 
attempting barley: short-season varieties (90-100 days) critical, irrigation mandatory if available, plan for 
feed market (malting quality unlikely), expect modest economics. Among small grains for poor rooting: oats 
best, barley acceptable, wheat poor, rye possible (winter survival issue).""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
make barley production non-viable. Barley's minimum rooting requirement (18-24 inches) cannot be met. Among 
small grains, barley more tolerant than wheat or rye but less tolerant than oats. Very shallow conditions 
prevent viable grain production.

ROOT FAILURE: Barley in very shallow soil: establishes roots to 8-15 inches then stops, develops inadequate 
crown root system (confined to surface crust), experiences continuous stress (inadequate rooting volume), 
produces minimal biomass (stunted 6-12 inches tall), heads poorly (thin sparse heads, many abort), yields 
<20 bu/ac if anything (not economically viable). Even short-season varieties (85-95 days) cannot complete 
cycle with <12 inch rooting.

ALTERNATIVES BETTER: DO NOT plant barley in very poor rooting conditions. Among cereals: oats marginally 
better (most stress-tolerant but still poor), spring wheat worse (fails completely), winter grains impossible 
(overwinter failure). All grain production questionable in very poor rooting. Better alternatives: 1) Annual 
forages (grazing use if any vegetation possible). 2) Extremely shallow-rooted crops with irrigation (vegetables, 
herbs). 3) Non-agricultural use. Even barley's relative tolerance (compared to wheat) inadequate for very 
poor rooting. Grain production not viable - too shallow for any cereal."""
    },

    "Oats": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports oats' 
fibrous root system to maximum genetic potential. Oats develop moderate depth roots (3-4 ft similar to barley, 
shallower than wheat) but with HIGHEST root density among small grains. Root characteristics: extremely dense 
fibrous roots in top 18-30 inches (highest root length density - 4-6 cm/cm³ in top foot), numerous fine 
feeding roots (superior nutrient extraction), moderate deep roots (30-40 inches), excellent lateral spread.

SUPREME ROOT EFFICIENCY: Among small grains, oats have: highest root mass per unit shoot mass (best root:shoot 
ratio), greatest root length density (most efficient extraction), finest root diameters (largest absorptive 
surface area), most extensive lateral spread. This gives oats superior: nutrient scavenging ability (especially 
N and P), water extraction efficiency, stress tolerance (can extract water at lower soil moisture than other 
grains), competitive ability (excellent weed suppression from dense roots). In excellent conditions, oat root 
efficiency fully expressed supporting 100-150 bu/ac potential.

ROOTING DEPTH LESS CRITICAL: Oats compensate for moderate depth (36-42 inches max) with exceptional efficiency. 
In excellent rooting conditions, oats may actually OUTYIELD barley and approach wheat yields despite shallower 
rooting - root density compensates for limited depth. Particularly strong performance in cool climates with 
adequate moisture where efficiency matters more than drought tolerance.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good root development to 30-40 inches - adequate for oats' moderate depth requirement and excellent for oats' 
high efficiency strategy. Oats particularly well-adapted to good (not excellent) conditions where efficiency 
compensates for limitations.

OAT ADAPTATION ADVANTAGES: Oats evolved for cool, moist, marginal agricultural regions (northern Europe, 
cool mountain valleys). Root system reflects this adaptation: extremely efficient extraction from limited 
depth (highest density compensates for moderate penetration), rapid spring establishment (reaches maximum 
depth in 40-50 days - fastest small grain), efficient nutrient uptake (excels in low-fertility soils - roots 
scavenge effectively), good performance in compact soils (fine roots penetrate small pores). In good conditions, 
develops 30-36 inch root system supporting 80-120 bu/ac.

PREFERRED FOR MARGINAL CONDITIONS: In good (not excellent) rooting, oats often best small grain choice: 
superior stress tolerance (root efficiency compensates for limitations), excellent in cool climates (northern 
regions, mountain areas), performs well in moderate fertility (root scavenging ability), matures quickly (85-
110 days - avoids late stress), versatile use (grain, forage, cover crop). Good rooting conditions ideal for 
oats' strengths.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit rooting to 24-30 inches. This is where oats EXCEL - moderate conditions where root efficiency most 
valuable. Oats THE BEST small grain for moderate to marginal rooting conditions. Specifically adapted for 
soils where other grains struggle.

OATS SWEET SPOT: Moderate rooting conditions ideal for oats: root efficiency compensates for limited depth 
(dense network exploits available volume completely), fine roots penetrate restricted conditions (compact 
layers, poor structure) better than other grains, short season matches limited rooting capacity (85-100 days 
typical), low water requirement (10-15 inches) suits restricted volume, adapted to stress (evolved for marginal 
lands). Produces 60-100 bu/ac where wheat limited to 40-60 bu/ac, barley to 50-70 bu/ac.

STRONGLY RECOMMENDED: In moderate rooting conditions, oats should be FIRST choice among small grains: most 
reliable yields under stress, best performance in compact soils, excellent in cool/moist climates, versatile 
use (can harvest for grain, forage, or cover crop depending on season), low input requirements (efficient 
nutrient use), good economics even at modest yields. Management simple - plant early, adequate shallow fertility, 
harvest as grain or use as forage if stressed. Oats' adaptation to marginal conditions makes them ideal where 
rooting restricted.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
rooting to 18-24 inches. Oats MOST TOLERANT small grain for poor rooting conditions - can produce acceptable 
forage and modest grain yields where wheat and barley fail. Root efficiency provides significant advantage.

BEST CEREAL FOR POOR ROOTING: Among small grains in poor rooting: oats STRONGLY PREFERRED (can produce 40-
70 bu/ac grain, excellent forage), barley MARGINAL (30-50 bu/ac, quality issues), wheat POOR (25-40 bu/ac, 
often fails), rye VARIABLE (winter survival issues). Oats' advantages: supreme root efficiency extracts 
maximum from limited volume, extreme stress tolerance (can survive conditions fatal to other grains), versatile 
harvest options (grain, forage, hay, silage), short season limits stress exposure, continues growing under 
stress (other grains shut down).

VIABLE PRODUCTION: Oats remain economically viable in poor rooting where other grains fail. For grain: expect 
40-70 bu/ac ($2.50-3.50/bu = $100-250/ac value) versus low inputs ($30-60/ac establishment, 60-80 lb N/ac). 
For forage: 2-4 tons/ac hay or 8-12 tons/ac silage - often more valuable than marginal grain. Management: 
early planting (maximize cool season growth), modest fertility in root zone, irrigation if available (greatly 
improves production), decide grain vs forage based on season (can wait to decide - harvest for forage if 
stress threatens grain maturity). Best cereal choice for poor rooting.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
challenge even oats. However, oats remain MOST VIABLE cereal option if attempting any grain production - more 
tolerant than any other small grain. Can produce useful forage even where grain impossible.

BEST CEREAL FOR EXTREME CONDITIONS: Among all cereals in very poor rooting, oats have: highest survival rate 
(plants continue growing when others die), some grain production possible (20-40 bu/ac vs <20 other grains), 
useful forage even if grain fails (can salvage economic return), most stress-tolerant (root efficiency 
extracts maximum from minimal volume), shortest season options (75-85 day varieties exist - minimize exposure). 
Still marginal but BEST available option among grains.

FORAGE ALTERNATIVE: In very poor rooting, consider oats primarily as FORAGE not grain: plant early (March-
April), use as: spring pasture (graze at vegetative stage), hay crop (cut at boot to early heading - 1.5-3 
tons/ac possible), silage (harvest at soft dough - 6-10 tons/ac possible), cover crop/green manure (plow down 
if production inadequate). Forage use more reliable than grain in extreme conditions - can harvest successfully 
even with minimal rooting. If attempting grain: very short-season varieties, expect 20-40 bu/ac maximum, plan 
forage backup (be ready to cut for hay if grain threatens to fail). Oats' versatility provides options in 
very poor rooting where other grains impossible."""
    },

    "Rice": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports rice's 
unique root system: fibrous adventitious roots (emerging from nodes), shallow but dense network (most mass 
in top 6-12 inches), moderate deep roots (to 24-36 inches). Rice has SHALLOWEST rooting among major cereals 
- adapted for flooded conditions where deep rooting unnecessary. Excellent conditions maximize surface rooting 
efficiency.

SHALLOW SPECIALIZED ROOTING: Rice evolved in flooded paddies where: oxygen limited below water table (restricts 
deep rooting), nutrients concentrated in upper soil (flooding brings nutrients to surface), water always 
available (deep roots unnecessary for moisture access), aerenchyma tissue transports oxygen to roots (allows 
function in anaerobic conditions). Result: rice naturally shallow-rooted (80-90% roots in top 6 inches, some 
to 24-36 inches). In excellent conditions, develops maximum density in critical upper zone supporting 150-
200+ bu/ac.

FLOODED VS UPLAND: Rice grown in two distinct systems: 1) Flooded/paddy rice (traditional, 90% of production, 
extremely shallow rooting adequate due to constant water). 2) Upland/dryland rice (aerobic rice, needs somewhat 
deeper rooting 12-24 inches for dry soil conditions). Excellent rooting conditions benefit both but especially 
critical for upland rice needing deeper water access.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions provides 
more depth than rice typically uses. Rice's shallow rooting requirement (18-30 inches total, most in top 6-12 
inches) means good depth conditions often EXCEED rice needs. Surface soil physical properties more critical 
than depth for rice.

SURFACE CONDITIONS CRITICAL: For rice, rooting quality more important than quantity or depth. Good conditions 
provide: adequate surface soil structure for dense fibrous root development (top 12 inches most critical), 
low bulk density in root zone (rice roots delicate, need low resistance), good soil-water contact (especially 
flooded rice), adequate oxygen supply to roots (despite flooding - through aerenchyma). Good rooting supports 
120-180 bu/ac flooded rice, 80-120 bu/ac upland rice.

FLOOD TOLERANCE: Rice's shallow rooting ADVANTAGE in flooded conditions - deep roots unnecessary and would 
suffocate in anaerobic subsoil. Good rooting conditions (unrestricted upper 12-18 inches) provide all rice 
needs. Restrictions below 24 inches have little impact on flooded rice. However, upland rice benefits from 
good deeper rooting (to 24-36 inches) for drought periods between rainfall/irrigation.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
in lower profile have MINIMAL impact on flooded rice (operates in top 6-12 inches), MODERATE impact on upland 
rice (needs 18-24 inches). Rice's shallow rooting makes it MORE tolerant of moderate depth limitations than 
other cereals.

FLOODED RICE SUITABLE: For traditional paddy rice, moderate rooting conditions often adequate: flooding 
provides constant moisture (deep roots unnecessary), surface roots access all needed nutrients, anaerobic 
subsoil normal for flooded rice, restriction below 12-18 inches irrelevant to flooded production. Can produce 
100-150 bu/ac with proper water management regardless of subsoil conditions.

UPLAND RICE CHALLENGED: Aerobic/dryland rice MORE affected by moderate rooting: needs 18-24 inches effective 
depth for dry period survival (moderate conditions may restrict to 12-18 inches), cannot rely on standing 
water (must access soil moisture), more vulnerable to drought stress than flooded rice. Produces 60-90 bu/ac 
upland rice where 100-150 bu/ac possible flooded. Consider: flood irrigation if possible (converts to flooded 
rice system), frequent irrigation (compensate for shallow rooting), varieties bred for aerobic conditions.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
rooting to <24 inches. FLOODED RICE remains viable (adapted to shallow conditions), UPLAND RICE severely 
limited (inadequate depth for dry soil production). Rice's adaptation to flooding provides significant advantage 
in poor rooting conditions compared to other cereals.

FLOODED RICE VIABLE: Traditional paddy rice can function in poor rooting conditions: operates primarily in 
top 6-12 inches (barrier at 18-24 inches has little direct effect), standing water compensates for shallow 
rooting (moisture always available), nutrient management adapted to flooded surface application, yields 80-
120 bu/ac possible with proper flood management. Among cereals for poor rooting, flooded rice BEST option 
where water management possible.

UPLAND RICE NON-VIABLE: Aerobic rice fails in poor rooting: requires minimum 18-24 inches for dry soil 
production (poor conditions provide 12-18 inches maximum), inadequate rooting for drought periods, cannot 
compete with weeds (shallow weak roots), continuous stress (limited root volume), yields <40-60 bu/ac if 
anything. DO NOT attempt upland rice in poor rooting - use flooded system or choose different crop.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) or extreme restrictions 
limit rooting to <12 inches. Even rice's extreme shallow-rooting adaptation challenged. FLOODED RICE marginally 
possible with intensive management, UPLAND RICE completely impossible.

FLOODED RICE MARGINAL: Traditional paddy rice in very poor rooting: can establish in top 6-12 inches (minimum 
for rice), standing water essential (compensates for minimal rooting), intensive nutrient management required 
(surface applications only), levee/flood management critical, yields 50-80 bu/ac (moderate for rice), economic 
viability questionable (high water management costs). Among all cereals, only flooded rice remotely viable 
in very poor rooting - unique adaptation to shallow conditions.

REQUIREMENT: Attempting rice in very poor rooting REQUIRES: 1) Flooded/paddy system mandatory (upland impossible). 
2) Excellent water control (precision levees, consistent flooding). 3) Surface fertility management (all 
nutrients in top 6-12 inches). 4) Short-season varieties (minimize stress exposure). 5) Intensive management 
throughout season. Consider alternatives: 1) Non-agricultural use. 2) Soil reconstruction before cropping. 
3) Extremely shallow-rooted crops if not rice-suited climate (vegetables with irrigation)."""
    },

    "Sunflower": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports sunflower's 
EXCEPTIONALLY deep taproot system - among THE deepest-rooted annual crops. Develops: massive central taproot 
(penetrating to 6-10 ft), extensive lateral roots at multiple depths, deep sinker roots from laterals, extremely 
efficient root system exploring huge soil volume. Sunflower's deep rooting provides remarkable drought tolerance 
for annual crop.

EXTREME DEEP ROOTING: Sunflower rivals alfalfa for deep root development among field crops: taproot reaches 
5-6 ft by flowering (60-70 days after planting), 8-10+ ft at maturity (100-120 days), some roots documented 
to 12-15 ft in deep soils. Lateral roots develop every 6-12 inches down taproot creating three-dimensional 
network. This gives sunflower: exceptional drought tolerance (accesses deep subsoil moisture), efficient 
nutrient mining (especially N from deep profile), strong anchorage (supports heavy seed heads), remarkable 
stress recovery ability. Excellent conditions allow full expression of genetic rooting potential.

YIELD AND OIL QUALITY: Deep rooting critical for both yield and quality: adequate moisture during seed-fill 
(R5-R9) increases oil content (40-45% vs 35-40% stressed), consistent water allows complete seed development 
(full heads vs incomplete fill), stress avoidance during flowering (R5) maximizes seed set. Excellent rooting 
supports 2,500-3,500 lb/ac with high oil quality.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm = 3-5 ft) with minor restrictions 
allows good taproot development to 4-6 ft. Sunflower's powerful taproot penetrates moderately resistant layers 
better than most annual crops. However, 4-6 ft is LESS than sunflower's genetic potential (8-12+ ft) and 
somewhat limits maximum drought tolerance.

ADEQUATE DEPTH: Taproot reaches 4-6 ft encountering moderate resistance (increasing bulk density, B-horizon, 
or coarse layer). This provides: adequate drought tolerance for most environments (better than corn, wheat, 
soybeans at same depth), good nutrient access throughout profile, sufficient anchorage for large heads (sunflower 
heavy - 1-2 lb seed per head), reasonable stress buffer. Produces 2,000-2,800 lb/ac with acceptable oil 
content (38-43%).

IRRIGATION BENEFIT: In good (not excellent) rooting, sunflower benefits significantly from irrigation especially 
during: V10-R1 (rapid vegetative growth, bud formation), R5-R6 (flowering and early seed-fill - most critical 
for oil content), R7-R8 (seed-filling - determines final weight). One to three irrigations at critical stages 
can boost yields 15-25% and improve oil quality. Good rooting provides base; irrigation optimizes performance.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm = 20-40 inches) 
or restrictions limit sunflower's taproot to 3-4 ft effective depth. This is MARGINAL for sunflower - barely 
meets minimum for commercial production. Sunflower requires 4-6 ft rooting for reliable yields; moderate 
conditions restrict drought tolerance significantly.

REDUCED DROUGHT BUFFER: Taproot encounters significant barrier at 36-48 inches. This creates: moderate drought 
vulnerability (especially late-season during seed-fill), reduced nutrient access from subsoil (heavy fertilization 
needed), adequate but not strong anchorage (lodging risk with very large heads in wind), limited stress 
recovery (shallow roots cannot access deep moisture reserves). Yields 1,500-2,200 lb/ac with variable oil 
content (35-42% - stress-dependent).

MANAGEMENT CRITICAL: Sunflower in moderate rooting requires: irrigation essential (not optional), timing 
critical (R5 flowering and R7-R8 seed-fill), fertility placed in root zone (top 36 inches), earlier harvest 
(mature before late-season drought), consider confection types vs oil types (confection sunflowers more 
drought-tolerant, larger seeds, less yield-dependent). Economics marginal - high inputs (irrigation, fertility) 
versus moderate yields. Sunflower's drought tolerance advantage lost in moderate rooting.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm = 10-20 inches) or severe 
restrictions make sunflower production economically questionable. Sunflower requires minimum 3-4 ft rooting 
for viable commercial production; poor conditions provide <2 ft. Taproot system fundamental to sunflower's 
stress tolerance - shallow rooting eliminates primary advantage.

TAPROOT FAILURE: Taproot hits impenetrable barrier at 18-30 inches creating: extreme drought sensitivity 
(irrigation every 3-5 days required), inadequate anchorage (lodging common - heavy heads on shallow roots), 
continuous stress (affects all growth stages), poor seed development (incomplete head fill, low oil content 
30-38%), premature maturity (stress-induced early finish). Yields 1,000-1,500 lb/ac if successful - often 
complete failure in drought.

NOT RECOMMENDED: Sunflower among POOREST crop choices for shallow soils. Sunflower's defining characteristic 
(extreme deep rooting providing drought tolerance) becomes liability when rooting restricted - crop demands 
high but cannot meet needs. Better alternatives: 1) Grain sorghum (better shallow-soil adaptation). 2) Safflower 
(similar oilseed, more drought-tolerant at shallow depth). 3) Shorter-season crops avoiding late drought. 
DO NOT plant sunflower in poor rooting unless irrigation guaranteed - even then economics questionable.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm = <10 inches) makes 
sunflower production completely impossible. Sunflower has high rooting requirement among annuals (second only 
to alfalfa, sugar beets). Very shallow conditions provide <20% of minimum requirement. Sunflower's biology 
dependent on deep taproot - shallow restriction causes fundamental failure.

BIOLOGICAL IMPOSSIBILITY: Sunflower seedlings emerge but: taproot hits barrier at 6-12 inches (week 2-4 
after planting), growth severely stunted (plants 12-24 inches tall vs 48-72 normal), cannot support head 
development (heads 2-4 inches diameter vs 6-12 normal), lodge immediately when heads form (no anchorage), 
produce <200-500 lb/ac unmarketable seed if anything. Sunflower's massive above-ground biomass (heavy stem, 
large leaves, 1-2 lb seed head) REQUIRES deep taproot for support and resources - <12 inch rooting completely 
inadequate.

WORST ANNUAL CROP CHOICE: For very shallow soil, sunflower among absolute worst options: high water demand 
(25-30 inches over 100-120 days) cannot be met with <10 inch rooting even with daily irrigation, top-heavy 
growth habit requires deep anchorage (impossible in shallow soil), deep rooting FUNDAMENTAL to sunflower 
biology (eliminates primary adaptation). Any other crop infinitely better choice. DO NOT attempt sunflower 
in very poor rooting - guaranteed complete failure."""
    },

    "Canola": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports canola's 
deep taproot system: strong central taproot (to 4-6 ft), numerous lateral branches (concentrated 0-24 inches), 
extensive fine feeding roots. Canola develops moderately deep to deep rooting - deeper than small grains 
(wheat, barley) but shallower than sunflower or alfalfa. Excellent conditions maximize canola's efficient 
root-based nutrient and water scavenging.

EFFICIENT TAPROOT SYSTEM: Canola (rapeseed) develops: rapid early taproot growth (to 24 inches by rosette 
stage 30-40 days), deep penetration continuing (to 48-72 inches by flowering 60-80 days), dense lateral 
branches (especially 6-18 inches depth - primary nutrient uptake zone), very fine feeding roots (high surface 
area for nutrient absorption). This creates: excellent nutrient scavenging ability (especially N recycling 
from deep profile), good drought tolerance (accesses subsoil moisture during seed-fill), efficient water use, 
strong anchorage. Supports 40-60 bu/ac yields with 40-45% oil content.

WINTER VS SPRING CANOLA: Winter canola (fall-planted, similar to winter wheat) develops deeper rooting than 
spring canola due to fall establishment period. Fall roots reach 18-24 inches before winter providing: excellent 
spring vigor, deeper total rooting potential (to 6 ft vs 4 ft spring types), better drought tolerance, higher 
yield potential (45-65 bu/ac vs 30-50 spring canola). Excellent rooting conditions benefit both but especially 
valuable for winter canola's deep-rooting potential.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 3-5 ft. Canola's taproot penetrates moderately resistant layers fairly well - 
better than small grains but not as effectively as sunflower or alfalfa. Good conditions adequate for commercial 
production.

ADEQUATE ROOTING: Taproot reaches 36-60 inches encountering moderate resistance (bulk density, structure, 
coarse fragments). This provides: adequate drought tolerance for most canola regions (northern plains, Canadian 
prairies, Pacific Northwest), sufficient nutrient access (lateral roots in top 24 inches capture most nutrients), 
good anchorage (canola tall 36-48 inches but lighter than sunflower), acceptable stress buffering. Produces 
35-55 bu/ac winter canola, 25-45 bu/ac spring canola with 40-43% oil.

SPRING VS WINTER PERFORMANCE: In good (not excellent) rooting conditions: winter canola performs better 
(fall roots penetrate before restrictions matter, deeper total system), spring canola more challenged (must 
develop entire root system during growing season, encounters restrictions sooner). Winter canola preferred 
in good rooting where climate allows (requires winter hardiness). Spring canola viable but irrigation beneficial 
during flowering and early seed-fill (30-50 days after planting).""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit canola taproot to 2-3 ft effective depth. This is near canola's minimum rooting requirement - viable 
but limited. Canola requires deeper rooting than small grains for comparable yields; moderate conditions 
challenge production.

ROOT DEVELOPMENT LIMITED: Taproot encounters barrier at 24-36 inches forcing lateral development in restricted 
upper zone. Creates: moderate drought sensitivity (especially during seed-fill - most critical water demand 
period), reduced nutrient scavenging (canola benefits from deep N access), adequate but marginal anchorage, 
stress vulnerability during critical stages. Yields 25-40 bu/ac winter canola, 18-32 bu/ac spring canola with 
variable oil content (38-42%).

MANAGEMENT REQUIREMENTS: Canola in moderate rooting needs: irrigation during flowering through early pod-fill 
(days 30-65 after flowering - most critical period), fertility in root zone (top 24 inches), early planting 
(maximize season before heat stress), consider spring types over winter (simpler management, less overwinter 
risk), short-season varieties (90-110 days spring types avoid late stress). Economics marginal - canola 
moderate-value crop ($0.45-0.55/lb) requiring intensive inputs in restricted conditions. Alternative crops 
may be more profitable.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions make 
canola production marginal to non-viable. Canola requires minimum 30-36 inches rooting for commercial viability; 
poor conditions provide <24 inches. Taproot system essential for canola's water and nutrient needs - shallow 
restriction severely limits production.

INADEQUATE ROOTING: Taproot hits barrier at 18-30 inches creating: severe drought vulnerability (canola 
water-sensitive during flowering and seed-fill), limited nutrient access (particularly N - canola heavy N 
user 100-150 lb/ac), weak anchorage (lodging risk especially if fertility high), continuous stress affecting 
all growth stages, poor seed development (small seeds, low oil content 35-40%). Yields 15-28 bu/ac winter 
canola, 10-22 bu/ac spring canola - economics questionable.

NOT RECOMMENDED: Canola poor choice for shallow soils. Better alternatives: 1) Small grains (barley, oats 
better shallow-soil adaptation). 2) Shorter-season oilseeds (flax somewhat more shallow-tolerant). 3) Grain 
legumes (field peas shorter season, adequate on moderate depth). If attempting canola: irrigation mandatory, 
spring types only (simpler than winter), short-season varieties (90-100 days), expect low returns. Among 
oilseeds for poor rooting, flax or soybeans generally better choices than canola.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes canola 
production impossible. Canola requires minimum 24-30 inches effective rooting for viable production; very 
shallow conditions provide <12 inches. Taproot development essential to canola biology - severe restriction 
causes fundamental failure.

ROOT SYSTEM FAILURE: Canola seedlings emerge but: taproot hits barrier at 6-12 inches (week 2-3), rosette 
development stunted (small leaves, weak growth), bolting delayed or aborted (inadequate root resources), 
flowering sparse (few racemes, poor seed set), plants lodge or die mid-season (inadequate anchorage and 
resources), yield <500-800 lb/ac if anything (not economically viable). Canola's 100-130 day season requires 
sustained root function - <12 inch rooting cannot support full cycle.

DO NOT ATTEMPT: Canola in very poor rooting guaranteed failure. Canola among poorer choices for shallow soils 
- moderate to high rooting requirement, long season (exposes to extended stress), sensitive growth stages 
(flowering and seed-fill both water-critical), relatively high inputs for moderate returns. Better alternatives: 
1) Very shallow-rooted crops only (vegetables with irrigation, lettuce, onions). 2) Short-season crops if 
attempting field crops. 3) Soil reconstruction before attempting canola. 4) Non-agricultural use. Among oilseeds, 
canola particularly poorly adapted to very shallow conditions."""
    },

    "Dry Beans": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports dry beans' 
moderately shallow taproot system: central taproot (to 36-48 inches), lateral branches (concentrated 0-18 
inches), nodulated roots (N-fixation throughout system). Dry beans have shallower rooting than soybeans - 
more similar to bush-type garden beans. Excellent conditions maximize beans' efficient but limited root system.

MODERATE SHALLOW ROOTING: Dry beans (pinto, navy, kidney, black, etc.) develop: taproot to 36-48 inches in 
excellent conditions (shallower than soybeans 48-60 inches), most root mass in top 12-18 inches (critical 
feeding zone), lateral roots spreading 12-18 inches from plant, nodules forming on laterals (N-fixation 60-
120 lb N/ac). Shallower rooting than soybeans makes dry beans: more drought-sensitive (less deep moisture 
access), faster-maturing (shorter season 85-110 days vs 100-130 soybeans), requiring more frequent irrigation, 
better adapted to shorter growing seasons.

NODULATION IMPORTANCE: Excellent rooting conditions support prolific nodulation: nodules throughout root 
system to 24-36 inches, higher root mass = more nodulation sites, N-fixation 60-120 lb N/ac (less than 
soybeans 100-200 lb), adequate for moderate yields 2,000-3,000 lb/ac, stress-free rooting maximizes fixation 
efficiency. Low bulk density and good structure critical for nodule formation and function.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 30-40 inches - adequate for dry beans' moderate shallow rooting requirement. Dry 
beans less demanding than soybeans making them BETTER adapted to good (not excellent) conditions with some 
subsoil limitations.

ADEQUATE DEPTH: Taproot reaches 30-40 inches with well-developed laterals in top 12-18 inches. This provides: 
adequate moisture access for 85-110 day season (shorter than soybeans), sufficient nodulation for moderate 
N needs (beans require less N than soybeans), acceptable drought buffering (5-7 days between irrigations), 
adequate anchorage (beans shorter than soybeans 18-24 inches vs 24-36). Produces 1,800-2,800 lb/ac with good 
nodulation and moderate irrigation.

IRRIGATION STRATEGY: Dry beans in good rooting benefit from strategic irrigation: flowering (R1-R2, most 
water-sensitive period), pod-fill (R3-R4, determines final seed size), skip vegetative stage irrigation 
(promotes root development over excessive foliage). Good rooting allows moderate irrigation frequency - more 
flexible than shallow-rooted crops but less forgiving than deep-rooted soybeans or alfalfa.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit dry bean taproot to 20-30 inches. This is near beans' minimum rooting requirement but still viable - 
beans MORE tolerant of moderate depth than soybeans due to naturally shallower rooting and shorter season.

MARGINAL BUT VIABLE: Taproot encounters barrier at 24-30 inches forcing root concentration in top 18 inches. 
Creates: moderate drought sensitivity (irrigation every 4-6 days during pod-fill), adequate nodulation if 
upper soil good quality (most nodules in top 12 inches), sufficient for short season (85-100 days), acceptable 
seed yields 1,400-2,200 lb/ac. Beans actually better adapted to moderate rooting than soybeans - lower rooting 
requirement and shorter season advantage.

MANAGEMENT ADAPTATION: Dry beans viable in moderate rooting if: irrigation available (mandatory for flowering 
and pod-fill), short-season varieties (85-95 days minimize stress exposure), proper inoculation (ensure good 
nodulation in restricted root zone), avoid high populations (20-24 inches row spacing vs 18 inch, 80,000-
100,000 plants/ac vs 120,000-150,000). Economics favorable compared to soybeans in marginal rooting - beans 
more reliable with better shallow-soil adaptation.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
dry bean taproot to <24 inches - below beans' minimum requirement for commercial production. Even beans' 
relatively shallow rooting inadequate in poor conditions. Taproot system essential for water access during 
85-110 day season.

INADEQUATE ROOTING: Taproot hits barrier at 18-24 inches creating: severe drought vulnerability (especially 
during flowering R1-R2 and pod-fill R3-R4), limited nodulation (reduced root volume = fewer nodulation sites), 
possible N deficiency (may need supplemental 40-60 lb N/ac), weak anchorage (lodging if excessive foliage), 
poor pod development (abortion under stress), low yields 800-1,500 lb/ac. Season too long (85-110 days) for 
adequate production with <24 inch rooting.

QUESTIONABLE VIABILITY: Dry beans marginally better than soybeans in poor rooting (shallower requirement) 
but still problematic. Better alternatives: 1) Field peas (shorter season 60-90 days, more shallow-tolerant). 
2) Other short-season legumes (lentils, chickpeas in suitable climates). 3) Non-legume short-season crops. 
If attempting dry beans: irrigation mandatory, very short-season varieties (85-95 days), supplemental N if 
nodulation poor, expect low returns. Economics questionable - beans moderate value crop ($0.30-0.60/lb) cannot 
justify intensive inputs required.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes dry bean 
production non-viable. Dry beans require minimum 24-30 inches rooting for 85-110 day season; very shallow 
conditions provide <12 inches. Taproot system and nodulation both severely compromised by extreme restriction.

COMPLETE FAILURE: Dry bean plants: emerge normally, develop taproot to 8-12 inches then stop, produce weak 
lateral roots in surface, nodulate poorly (few nodulation sites), remain severely stunted (<12 inches tall), 
flower sparsely or abort flowering, set few pods (high abortion rate), mature prematurely under stress, yield 
<400-800 lb/ac unmarketable. Growing season (85-110 days) requires sustained root function - <12 inch rooting 
inadequate for full cycle.

DO NOT ATTEMPT: Dry beans in very poor rooting guaranteed failure. Among grain legumes: field peas slightly 
better (shorter season 60-90 days, somewhat more shallow-tolerant), soybeans worse (higher rooting requirement 
36-48 inches minimum), other beans similar (lima, fava equally challenged). Better alternatives: 1) Extremely 
shallow-rooted crops with irrigation (vegetables). 2) Short-season cover crops (not for grain harvest). 3) 
Non-agricultural use. Dry beans require more rooting than very shallow conditions provide - fundamental biological 
mismatch."""
    },

    "Peanuts": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep loose soil supports peanuts' unique 
taproot system AND critical peg penetration: strong central taproot (to 4-6 ft), lateral roots (spreading 
24-36 inches), pegs (geocarpic structures penetrating soil to develop pods underground). Peanuts require 
BOTH deep rooting AND loose surface soil for peg penetration - excellent conditions provide both.

UNIQUE ROOTING AND PEG REQUIREMENTS: Peanuts (groundnuts) have dual below-ground needs: 1) Deep taproot 
system (48-72 inches) for water and nutrients like other legumes. 2) Loose friable soil (top 3-6 inches) for 
peg penetration after flowering - flowers pollinate then develop gynophores ("pegs") growing down into soil 
where pods develop underground. This creates unique requirements: deep unrestricted rooting (48-72+ inches 
optimal), very loose surface soil (pegs must penetrate easily), low bulk density throughout profile, good 
structure and tilth (especially surface).

EXCELLENT CONDITIONS ESSENTIAL: Peanuts evolved on deep sandy soils of South America. Excellent rooting 
conditions provide: deep water access during 140-160 day season, easy peg penetration (critical for pod 
development), large soil volume for extensive pod development, adequate nodulation throughout deep root system 
(N-fixation 100-150 lb/ac), optimum pod formation and filling. Supports 4,000-6,000 lb/ac yields with excellent 
kernel quality.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 3-5 ft AND adequate surface conditions for peg penetration. Peanuts' dual 
requirements mean high rooting must include BOTH depth and good surface structure.

ADEQUATE FOR BOTH NEEDS: Taproot reaches 36-60 inches while surface soil (top 6 inches) maintains adequate 
looseness for peg penetration. Moderate bulk density or structure issues in subsoil (below 24 inches) less 
problematic than surface compaction - pegs develop in top 4-6 inches, early lateral roots in top 12 inches. 
Produces 3,000-5,000 lb/ac with good pod set and fill.

CRITICAL SURFACE MANAGEMENT: For peanuts, surface conditions (top 6 inches) often MORE important than deep 
subsoil: pegs penetrate top 3-6 inches only (where pods develop), compacted surface prevents peg penetration 
(no pods form), crusting after rain problematic (pegs cannot break through). Good rooting conditions ideal 
if surface maintained loose through: proper tillage (avoid compaction), timely cultivation (break crusts, 
promote peg penetration), adequate calcium (surface-applied gypsum critical for pod development and quality 
- 400-800 lb/ac). Deep subsoil restrictions less limiting than surface compaction.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
present DUAL challenges for peanuts: limited deep rooting (reduces water/nutrient access) AND possibly 
restricted peg penetration (reduces pod set). Peanuts' unique requirements make them more sensitive to moderate 
restrictions than other legumes.

ROOTING AND PEG LIMITATIONS: Taproot restricted to 24-40 inches while surface may have moderate compaction 
or structure issues. Creates: moderate drought sensitivity (especially during pegging and pod-fill), difficult 
peg penetration if surface dense (many flowers fail to form pods), uneven pod development (some pegs succeed, 
others fail), lower yields 2,000-3,500 lb/ac, variable quality (some mature pods, many immature or empty). 
Peanuts' 140-160 day season plus underground pod development makes moderate conditions challenging.

SURFACE MANAGEMENT CRITICAL: In moderate rooting, surface soil management MORE important than deep tillage: 
aggressive tillage before planting (break compaction, create loose seedbed), cultivation during pegging period 
(35-75 days after planting, maintain loose surface for peg entry), gypsum application (1,000-1,200 lb/ac, 
helps overcome density issues), avoid traffic (compaction during pegging prevents pod formation). Consider 
Virginia types over Spanish/Runner (larger seeds, more drought-tolerant, better adapted to marginal conditions). 
Economics marginal - peanuts high-value crop ($0.20-0.25/lb) but intensive management costs high.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions make 
peanut production highly problematic. Peanuts require: minimum 36-48 inches rooting depth for 140-160 day 
season, loose surface soil for peg penetration and pod development. Poor conditions often provide neither.

DUAL FAILURE: Shallow rooting restricts taproot to <30 inches while surface compaction or barriers prevent 
adequate peg penetration. Results: severe drought stress over long season (140-160 days), extensive flower 
abortion (pegs cannot penetrate to form pods), poor pod set (<50% of flowers form pods vs 60-80% normal), 
incomplete pod development (many immature or "pops" - empty shells), low yields 1,000-2,200 lb/ac, poor 
kernel quality (small, immature, damaged). Peanuts' underground pod development makes them uniquely vulnerable 
to poor rooting - other crops can set seed above ground.

NOT RECOMMENDED: Peanuts among POOREST choices for poor rooting conditions. Unique requirements (deep rooting 
+ loose surface + long season) make them more sensitive than other legumes. Better alternatives: 1) Soybeans 
(no peg requirement, shorter season, simpler). 2) Dry beans (shorter season, surface production). 3) Other 
crops entirely. If attempting peanuts: Virginia types only (most stress-tolerant), irrigation mandatory (entire 
season), intensive surface management (frequent cultivation), massive gypsum (1,500-2,000 lb/ac), expect poor 
economics. Peanuts in poor rooting rarely profitable.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes peanut production 
absolutely impossible. Peanuts have among HIGHEST rooting requirements of annual legumes (36-48 inches minimum) 
plus unique requirement for loose penetrable soil for underground pod development. Very shallow conditions 
provide neither.

COMPLETE IMPOSSIBILITY: Peanut plants: emerge and grow vegetatively to flowering (30-45 days), develop flowers 
normally, form pegs after pollination BUT pegs cannot penetrate compacted/shallow soil (hit barrier at 3-6 
inches), pods fail to develop (pegs abort or form tiny immature pods), plants attempt continuous flowering 
(trying to reproduce), plants collapse from stress (inadequate roots cannot support prolonged effort), yield 
<500 lb/ac of immature unmarketable nuts if anything. Peanuts' entire reproductive strategy dependent on 
underground pod development - surface barriers cause complete reproductive failure.

ABSOLUTE WORST CHOICE: Among all field crops for very shallow soil, peanuts near absolute worst (only alfalfa 
worse). Peanuts require: deepest annual legume rooting, longest legume season (140-160 days vs 85-130 most 
beans), unique underground pod development (requires loose soil), warm climate (limits growing region options). 
Very shallow conditions violate ALL requirements. DO NOT ATTEMPT peanuts in very poor rooting - guaranteed 
complete failure with 100% loss of all inputs. Any other crop infinitely better option."""
    },

    "Sugar Beets": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports sugar 
beets' EXTREMELY deep taproot system - among THE deepest-rooted crops (rivaling alfalfa). Develops: massive 
storage taproot (12-18 inches deep,4-6 inches diameter), continuation taproot below storage root (to 6-10+ 
ft), extensive lateral feeding roots at multiple depths. Sugar beets require 6-10 ft depth for maximum production 
- equal to perennial alfalfa despite being annual crop.

EXTREME DEEP ROOTING: Sugar beets develop deepest rooting among annual crops (with sunflower): storage taproot 
to 12-18 inches (the "beet" harvested for sugar), continuation taproot below storage root to 6-10+ ft (some 
documented to 12 ft), lateral roots every 6-12 inches down profile creating extensive network. This extreme 
rooting provides: exceptional drought tolerance (rivals perennials), efficient nutrient mining from deep 
subsoil (especially N recycling), remarkable stress recovery, ability to produce through extended season (160-
200+ days). Excellent conditions essential for 30-40 ton/ac yields with 16-18% sugar content.

ROOTING CRITICAL FOR SUGAR YIELD: Deep rooting directly affects both tonnage and sugar content: adequate 
moisture during storage root expansion (80-140 days) increases tonnage, consistent water during maturation 
(140-180+ days) increases sugar concentration, stress-free rooting prevents stress-induced low sugar (12-14% 
vs 16-18% optimal), deep roots allow extended season for maximum sugar accumulation. Sugar beets' value is 
sugar content × tonnage - both depend on deep unrestricted rooting.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm = 3-5 ft) with minor restrictions 
allows good taproot development to 4-6 ft. However, this is LESS than sugar beets' genetic potential (8-12+ 
ft) and somewhat limits maximum production. Sugar beets require deeper rooting than any annual crop except 
sunflower.

ADEQUATE BUT LIMITED: Taproot reaches 4-6 ft encountering moderate resistance (bulk density, structure, coarse 
fragments). Storage root develops normally (top 12-18 inches) but continuation taproot limited. Produces 24-
35 ton/ac with 15-17% sugar content. Good conditions adequate for commercial production but not maximum yields. 
Deep rooting advantage (compared to shallow crops) partially realized.

IRRIGATION AND SEASON LENGTH: In good (not excellent) rooting, sugar beets benefit significantly from: 
irrigation during storage root development (60-120 days - size expansion), final irrigation timing critical 
(must stop 10-14 days before harvest to concentrate sugar), extended season if possible (longer season = 
higher sugar content, 180-200+ days optimal). Good rooting provides base for commercial production; management 
optimizes performance within limitations.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm = 20-40 inches) 
or restrictions severely limit sugar beets. Sugar beets require 4-6 ft minimum for viable commercial production; 
moderate conditions provide 2-3 ft. Among annual crops, sugar beets have highest rooting requirement - moderate 
conditions fundamentally inadequate.

INADEQUATE DEPTH: Taproot restricted to 24-40 inches - the storage root itself occupies 12-18 inches leaving 
only 12-24 inches of exploration depth for continuation taproot. This creates: moderate to severe drought 
vulnerability (especially during 160-200 day season), reduced nutrient access (sugar beets heavy feeders 150-
200 lb N/ac), storage root size limited (20-28 tons/ac vs 30-40 optimal), sugar content reduced (13-16% vs 
16-18% optimal), economic viability questionable. Sugar beets' defining advantage (deep rooting providing 
stress tolerance and long-season production) lost in moderate conditions.

NOT RECOMMENDED: Sugar beets among POOREST annual crop choices for moderate rooting. High rooting requirement 
(equal to perennials) makes them unsuited to restricted conditions. Better alternatives: 1) Potatoes (similar 
root crop, much shallower requirement 24-36 inches). 2) Corn or grain sorghum (moderate depth adequate, 
shorter season). 3) Annual crops better adapted to moderate depth. DO NOT plant sugar beets in moderate 
rooting - cannot achieve commercial sugar yields without 4-6+ ft depth. Economics fail - low tonnage and sugar 
content cannot justify high input costs.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm = 10-20 inches) makes sugar 
beet production completely non-viable. Sugar beets require minimum 48-60 inches (4-5 ft) effective depth for 
commercial production; poor conditions provide <24 inches. Among annual field crops, sugar beets have HIGHEST 
rooting requirement (equal to deep-rooted perennials).

FUNDAMENTAL FAILURE: Storage taproot occupies 12-18 inches leaving <12 inches for continuation taproot. 
Creates: inadequate plant survival over 160-200 day season (longest annual crop), severe drought stress 
continuously, extremely limited nutrient access, small storage roots (8-15 tons/ac, non-commercial), very low 
sugar content (10-14%, uneconomical for processing), early maturation forced by stress (prevents sugar 
accumulation). Sugar beets cannot function with <24 inch rooting - biology requires deep access.

IMPOSSIBLE ECONOMICS: Sugar beet production costs $600-1,000/ac (specialized equipment, high inputs, long 
season). Poor rooting yields: 8-15 tons/ac × 10-14% sugar × $0.045-0.055/lb sugar = $80-200/ac gross value. 
Net loss $400-800/ac guaranteed. Sugar beet contracts require minimum tonnage and sugar content - poor rooting 
cannot meet either threshold. DO NOT ATTEMPT sugar beets in poor rooting - among absolute worst crop choices 
for shallow soils. Processors will not accept beets from poor rooting conditions - insufficient quality and 
quantity.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm = <10 inches) makes 
sugar beet production absolutely impossible. Sugar beets have HIGHEST rooting requirement among annual crops 
(minimum 48-60 inches, optimal 8-12+ ft). Very shallow conditions provide <20% of minimum requirement. Among 
all annual crops for very shallow soil, sugar beets are THE WORST possible choice.

BIOLOGICAL IMPOSSIBILITY: Sugar beet plants: germinate and establish, develop small storage taproot to 6-10 
inches (hits barrier immediately), cannot expand storage root (constricted by shallow depth), continuation 
taproot blocked completely (no deep exploration possible), plants remain severely stunted throughout season, 
attempt 160-200 day season on <10 inch rooting (impossible), die or produce <3-8 ton/ac tiny inedible beets 
with <10% sugar. Storage taproot itself requires 12-18 inches - very shallow soil cannot even accommodate 
the storage organ much less supporting root system.

ABSOLUTE WORST CHOICE: Among all field crops for very shallow soil, sugar beets are THE single worst option 
(worse than alfalfa, sunflower, all others): highest annual crop rooting requirement (equal to deepest 
perennials), longest growing season (160-200+ days - most stress exposure), highest water demand over season 
(25-35 inches), specialized high-cost production system ($600-1,000/ac investment). Very shallow conditions 
violate every requirement. DO NOT ATTEMPT sugar beets in very poor rooting under ANY circumstances - guaranteed 
100% complete failure with massive financial loss. Absolutely no crop worse suited to very shallow soils than 
sugar beets."""
    },

    "Red Clover": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports red clover's 
moderately deep taproot system: central taproot (to 4-6 ft), numerous lateral branches (concentrated 0-24 
inches), extensively nodulated roots. Red clover has moderate rooting depth - shallower than alfalfa (4-6 ft 
vs 8-15+ ft) but deeper than white clover (2-3 ft vs 4-6 ft). Excellent conditions maximize productive life 
and yield potential.

MODERATE DEEP LEGUME: Red clover develops: strong taproot to 48-72 inches in excellent conditions (much less 
than alfalfa but adequate for 2-3 year stands), extensive lateral root development in top 18-24 inches (primary 
feeding zone), prolific nodulation throughout system (N-fixation 100-150 lb/ac similar to alfalfa), adequate 
depth for short-term perennial production. This provides: good drought tolerance (better than annual legumes, 
less than alfalfa), adequate water access for 2-3 productive years, good stand persistence (2-4 year stands 
typical vs 5-8+ alfalfa), efficient nutrient cycling. Excellent rooting supports 4-6 ton/ac hay yields over 
2-3 years.

RED CLOVER VS ALFALFA: Red clover better adapted than alfalfa where rooting limited: lower rooting requirement 
(4-6 ft vs 8-15+ ft), shorter stand life (2-3 years vs 5-8+ years), accepts wetter conditions (more flood-
tolerant), tolerates moderate acidity better (pH 5.8-6.5 vs 6.5-7.5). Choose red clover over alfalfa when: 
short rotation needed, deep rooting unavailable, moderate pH or drainage issues present, simpler management 
desired.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 3-5 ft - adequate for red clover's moderate rooting requirement. Red clover BETTER 
suited than alfalfa to good (not excellent) rooting conditions with subsoil limitations.

ADEQUATE FOR SHORT STANDS: Taproot reaches 36-60 inches encountering moderate resistance. This provides: 
adequate moisture access for 2-3 year production cycle (shorter than alfalfa 5-8+ years), sufficient nodulation 
for good N-fixation (90-140 lb/ac), acceptable drought buffering for temperate humid climates, enough depth 
for typical red clover use (short-rotation forage legume). Produces 3.5-5.5 ton/ac over 2-3 productive years.

PREFERRED OVER ALFALFA: In good (not excellent) rooting, red clover often BETTER choice than alfalfa: adequate 
depth for red clover (3-4 ft sufficient) vs marginal for alfalfa (6+ ft needed), shorter stand expectation 
matches limited rooting (no need for 8+ year stand life), less drought-sensitive (adapted to temperate humid 
regions with moderate rainfall), establishment costs lower (shorter commitment). Economics favor red clover 
in marginal rooting - comparable annual returns with less risk.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit red clover taproot to 2-4 ft. This is near red clover's minimum but still viable - red clover MUCH MORE 
tolerant of moderate rooting than alfalfa. Specifically adapted for moderate depth conditions where deep-
rooted perennial legumes struggle.

SUITABLE FOR SHORT-TERM USE: Taproot reaches 24-48 inches providing: adequate moisture access for 1-2 year 
stands (vs 2-4 years optimal), sufficient nodulation in upper profile (most nodules top 18 inches), acceptable 
forage production for short rotation (2.5-4 ton/ac), better adaptation than alfalfa to moderate depth. Stand 
life shortened (1-2 years vs 2-4 optimal) but still economically viable - red clover adapted for short rotations.

RECOMMENDED OVER ALFALFA: In moderate rooting conditions, red clover STRONGLY preferred over alfalfa: viable 
in moderate depth (alfalfa fails or struggles), shorter cycle matches limited rooting (1-2 year stands acceptable), 
lower establishment cost (can justify short stand), simpler management (less demanding). Red clover specifically 
bred for temperate humid regions with moderate rooting potential - this is its adapted niche. Management: 
plan 1-2 year stands (not 3-4 years), consider including with grass mix (reduces stress on clover), adequate 
surface fertility (restricted roots cannot mine deep), expect modest but profitable returns.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions limit 
red clover taproot to <30 inches - below minimum for viable perennial legume production. Even red clover's 
relatively moderate rooting requirement (vs alfalfa) inadequate in poor conditions. Stand establishment and 
persistence very poor.

MARGINAL PERENNIAL VIABILITY: Taproot reaches only 18-30 inches creating: poor first-year establishment (weak 
plants), winter injury common (shallow roots heave and freeze), stands thin rapidly (30-50% loss over winter), 
limited regrowth second year (inadequate root reserves), stand failure after 1 year typical, low production 
(1.5-3 ton/ac first year, <1.5 ton second year if survives). Red clover's perennial nature requires adequate 
rooting for overwinter survival and spring regrowth - poor conditions prevent perennial function.

ANNUAL ALTERNATIVE BETTER: In poor rooting, consider annual legumes over red clover: crimson clover (annual 
fall-planted, 6-18 inch rooting adequate, 2-3.5 ton/ac), hairy vetch (annual, similar rooting, good biomass), 
other annual clovers (berseem, Persian - summer annuals), annual medics (various species, 12-24 inch rooting). 
Annual legumes avoid overwinter challenge and perennial rooting requirement. If attempting red clover: plan 
single-season use only (no second year expectation), irrigation helpful (compensate shallow rooting), accept 
modest returns. Economics favor annuals - red clover's perennial advantage lost in poor rooting.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes perennial red 
clover production impossible. Red clover requires minimum 24-36 inches rooting for perennial survival and 
regrowth; very shallow conditions provide <12 inches. Perennial legumes fundamentally incompatible with very 
shallow rooting.

PERENNIAL FAILURE: Red clover plants: establish weakly first season (limited root development to 8-12 inches), 
produce minimal first-year growth (severely stunted), enter winter with inadequate root mass (no carbohydrate 
reserves), heave out during freeze-thaw cycles (shallow roots unanchored), suffer >80% winterkill (vs <10% 
normal), surviving plants produce no useful regrowth, stand completely fails by second spring. Perennial life 
cycle requires adequate root mass for: overwinter survival, carbohydrate storage, spring regrowth, multiple 
harvests over 2-4 years. Very shallow rooting prevents ALL perennial functions.

USE ANNUALS ONLY: DO NOT attempt red clover or any perennial legume in very poor rooting. All perennials 
require deeper rooting than very shallow conditions provide. Better alternatives: 1) Annual legumes only 
(crimson clover, hairy vetch, field peas - single season, shallow adequate). 2) Annual grasses (oats, rye, 
wheat - for cover or grazing). 3) Extremely shallow-rooted crops with irrigation (vegetables if suitable 
climate). 4) Non-agricultural use. Among legumes, red clover requires MORE rooting than annual types - perennial 
nature mandates adequate depth for overwinter survival. Very shallow soil cannot support perennial legumes."""
    },

    "Sugarcane": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports sugarcane's 
extensive fibrous root system: primary roots from sets/nodes, extensive secondary and tertiary branching, 
deep penetration (to 5-8 ft), long-term perennial ratoon system. Sugarcane develops deep moderate rooting - 
deeper than annual crops but adapted for wet/flooded tropical conditions. Excellent conditions support 4-7+ 
year ratoon cycles.

PERENNIAL RATOON ROOTING: Sugarcane unique among field crops: planted once then harvested multiple times 
(4-7+ ratoon crops over 5-8+ years), new shoots emerge from stubble after each harvest, root system partially 
remains but regenerates each cycle, cumulative root development over years creating extensive network. Deep 
unrestricted soil allows: maximum ratoon life (6-8+ harvests vs 3-5 limited), vigorous regrowth each cycle, 
deep water access during long growing season (10-24 months per crop depending on climate), strong anchorage 
for tall cane (10-15+ ft stalks). Supports 100-150 tons/ac fresh cane (15-20 tons/ac sugar) per cycle.

TROPICAL ADAPTATION: Sugarcane evolved in wet tropical conditions adapting to: seasonal flooding (tolerates 
saturated soils), high rainfall (60-100+ inches/year), warm temperatures year-round. Root system reflects 
this: functions well in wet soils (better than dryland crops), tolerates temporary shallow water tables, 
develops extensive surface laterals (top 12-24 inches in wet periods), extends deep when conditions allow 
(48-72+ inches). Excellent rooting maximizes both surface feeding and deep water access.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm = 3-5 ft) with minor restrictions 
allows good root development to 4-6 ft - adequate for sugarcane production though ratoon life may be shortened. 
Sugarcane's moderate deep rooting (vs extreme deep crops like alfalfa) makes it adaptable to good conditions.

RATOON CYCLE SHORTENED: Root system develops to 48-72 inches providing adequate water and nutrient access. 
However, minor restrictions may shorten productive ratoon life: 4-6 ratoon crops typical (vs 6-8+ excellent 
conditions), declining vigor after 4-5 years (roots cannot maintain productivity as long), more frequent 
replanting needed (increased establishment costs). Each ratoon cycle somewhat less productive than excellent 
conditions: 80-120 tons/ac fresh cane (12-18 tons/ac sugar) per cycle.

IRRIGATION BENEFIT: In good (not excellent) rooting, sugarcane benefits from irrigation especially: establishment 
year (first 3-4 months critical for root development), dry season periods (particularly in monsoon climates 
with distinct dry season), later ratoon years (as root vigor declines). Good rooting provides base for commercial 
production; irrigation optimizes ratoon longevity and individual crop yields.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm = 20-40 inches) 
or restrictions limit sugarcane rooting to 3-4 ft effective depth. This is near sugarcane's minimum for 
multi-year ratoon production - viable but ratoon system severely limited. May need to treat as replant-after-
each-harvest rather than multi-year ratoon.

RATOON SYSTEM MARGINAL: Roots restricted to 24-48 inches creating: shortened ratoon life (2-3 crops maximum 
vs 6-8+ optimal), declining productivity each cycle (first ratoon acceptable, subsequent ratoons poor), possible 
need for annual replanting (eliminates ratoon advantage), moderate drought sensitivity (especially late in 
18-24 month crop cycle). Yields: plant crop 70-100 tons/ac, first ratoon 60-90 tons, second ratoon 40-70 
tons - often uneconomical after second ratoon.

ALTERNATIVE MANAGEMENT: In moderate rooting, consider: short ratoon cycle (harvest plant crop + 1-2 ratoons 
then replant vs 6-8 cycles), annual replanting where viable (treat as annual crop, simpler but higher costs), 
shorter-cycle varieties (12-15 month vs 18-24 month), drip irrigation (compensates for limited rooting), 
alternative crops if sugarcane marginal (sorghum for syrup/biofuel, energy cane varieties more stress-tolerant 
than sugar varieties). Economics marginal - frequent replanting (every 2-3 years) increases costs substantially.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm = 10-20 inches) makes multi-year 
ratoon sugarcane production non-viable. Sugarcane's ratoon system requires minimum 36-48 inches rooting for 
economic multi-year production; poor conditions provide <30 inches. Ratoon advantage (multiple harvests from 
single planting) lost - must treat as annual crop if attempting at all.

RATOON FAILURE: Roots restricted to <30 inches creating: plant crop establishment poor (weak initial growth), 
first ratoon very poor (stubble produces weak regrowth), no viable second ratoon (stubble dies or fails to 
sprout), essentially forces annual replanting (high costs $400-600/ac/year), severe drought sensitivity 
(irrigation every 3-5 days required), low productivity (40-70 tons/ac plant crop, 20-50 tons ratoons if any). 
Sugarcane's primary economic advantage (ratoon longevity 4-7 years) completely lost.

NOT RECOMMENDED: Sugarcane poor choice for shallow soils. Sugarcane production economics depend on ratoon 
system: establishment costs $400-600/ac amortized over 5-8 years = $50-100/ac/year, annual replanting = $400-
600/ac/year (5-6× higher), cannot be economically viable with annual replanting, yields too low to justify 
costs even in tropical regions. Better alternatives: 1) Annual crops (corn, sorghum, soybeans - no perennial 
requirement). 2) Energy cane (less demanding, used for biomass/biofuel not sugar). 3) Different land use. DO 
NOT plant commercial sugar cane in poor rooting.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm = <10 inches) makes 
any sugarcane production impossible. Sugarcane requires minimum 30-36 inches effective rooting for even single 
crop production; multi-year ratoon system requires 48-60+ inches. Very shallow conditions provide neither.

BIOLOGICAL FAILURE: Sugarcane sets (seed pieces): planted 4-6 inches deep, sprout and emerge, develop roots 
to 8-15 inches maximum (hit barrier), stalks grow to 4-6 ft tall (vs 12-15+ ft normal) creating extreme 
top-heavy instability, lodge continuously (no anchorage), produce minimal sugar (<30 tons/ac fresh cane vs 
100-150+ optimal), cannot sustain 12-24 month crop cycle, stubble dies completely after harvest (no ratoon 
possible). Sugarcane's tall heavy stalks require substantial deep rooting - <12 inches completely inadequate.

IMPOSSIBLE RATOON ECONOMICS: Sugarcane viability depends entirely on ratoon system: establishment costs $400-
600/ac must be recovered over 4-7+ years, single crop production cannot recover costs (gross value 30 tons × 
$30-40/ton = $900-1,200, net loss $200-400/ac after harvest and processing costs), zero ratoon production 
(stubble dies - cannot produce second crop), attempting replant annually loses $200-400/ac every year. DO NOT 
ATTEMPT sugarcane in very poor rooting under any circumstances - among worst possible crop choices for very 
shallow soils. Total fundamental biological and economic impossibility."""
    },

    "Tobacco": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil supports tobacco's 
moderate taproot system: central taproot (to 3-5 ft), numerous lateral branches (concentrated 0-18 inches), 
extensive fine feeding roots. Tobacco has moderate rooting depth - similar to cotton but shallower than deep-
rooted crops (sunflower, alfalfa). Excellent conditions maximize leaf quality and yield potential.

MODERATE ROOTING REQUIREMENT: Tobacco develops: taproot to 36-60 inches in excellent conditions (adequate 
for 90-130 day season depending on type), extensive lateral development in top 12-18 inches (primary nutrient 
uptake zone for quality leaf), dense fine root network (supports large leaves and rapid growth), adequate 
depth for water access during critical periods (flowering, topping, curing stages on stalk). This provides: 
moderate drought tolerance (better than shallow crops, less than deep-rooted), efficient nutrient uptake (N-K-
Ca all critical for quality), adequate anchorage for large-leaf types, support for high-value quality production.

QUALITY EMPHASIS: Tobacco unique among field crops - quality MORE important than yield. Excellent rooting 
supports quality through: consistent adequate moisture (prevents stress-induced quality degradation), efficient 
nutrient uptake (balanced nutrition essential for proper curing), strong healthy plants (disease resistance, 
proper maturation), supports 2,800-3,500 lb/ac yields with premium quality (color, texture, burn characteristics, 
aroma) commanding highest prices ($1.80-2.20/lb vs $1.40-1.80 lower quality).""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Deep soil (100-150cm) with minor restrictions allows 
good taproot development to 30-48 inches - adequate for tobacco's moderate rooting requirement. Tobacco's 
modest depth needs (vs deep-rooted crops) makes it well-adapted to good conditions with some subsoil limitations.

ADEQUATE FOR QUALITY: Taproot reaches 30-48 inches with well-developed laterals in top 12-18 inches. This 
provides: sufficient moisture for quality production (critical during leaf expansion and ripening), adequate 
nutrient access (especially K in top 18 inches - most critical for quality), acceptable drought buffering 
(irrigation 5-8 days intervals), good plant vigor supporting uniform leaf development. Produces 2,400-3,200 
lb/ac with good to excellent quality ($1.60-2.00/lb).

QUALITY MANAGEMENT: In good rooting, focus on quality over yield: adequate but not excessive irrigation 
(excess promotes fast growth with poor curing quality), balanced K nutrition (400-600 lb K₂O/ac critical for 
quality - use sulfate not muriate of potash), topping and suckering (directs plant resources to quality leaves), 
timely harvest (maturity critical for quality). Good rooting allows quality production with proper management 
- tobacco's value is quality-driven not yield-driven ($1.80/lb × 2,800 lb = $5,040/ac > $1.50/lb × 3,200 lb 
= $4,800/ac).""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Moderately deep soil (50-100cm) or restrictions 
limit tobacco taproot to 24-36 inches. This is near tobacco's minimum but still viable - tobacco MORE tolerant 
of moderate depth than many field crops due to modest rooting requirement and short season (90-130 days).

QUALITY RISK: Roots restricted to 24-36 inches creating: moderate drought sensitivity (requires irrigation 
every 4-6 days), possible nutrient deficiencies (especially K if root volume limited), uneven plant growth 
(stress affects leaf quality uniformly), lower yields 2,000-2,800 lb/ac, quality concerns (thin leaves, poor 
color, uneven ripening) affecting price ($1.40-1.80/lb vs $1.80-2.20 optimal). Tobacco's value entirely 
quality-dependent - moderate stress severely impacts returns.

MANAGEMENT FOCUS: In moderate rooting, intensive management essential: frequent irrigation (never allow 
stress), split K applications (multiple times to compensate for limited uptake), fertility in root zone (top 
24 inches), varieties for stress tolerance (some types more resilient), consider type suitability (Burley more 
drought-tolerant than Bright Leaf, Dark tobacco most stress-tolerant). Economics marginal - intensive management 
costs ($2,000-3,000/ac) versus moderate returns (2,400 lb × $1.60 = $3,840/ac gross) leave thin margins.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Shallow soil (25-50cm) or severe restrictions make 
tobacco production economically questionable. Tobacco requires minimum 24-30 inches rooting for quality leaf 
production; poor conditions provide <24 inches. Quality severely compromised - reducing marketability and price.

QUALITY FAILURE: Roots restricted to <24 inches creating: severe drought stress (irrigation every 2-4 days 
required), continuous nutrient stress (especially K - critical for quality), stunted plants producing small 
thin leaves, poor leaf quality (light color, thin body, poor curing, harsh taste), low yields 1,200-2,000 
lb/ac, low quality grade (lug/trash grades vs premium) receiving minimal price ($0.80-1.20/lb vs $1.80-2.20 
premium). Tobacco contracts specify minimum quality standards - poor rooting often produces unmarketable leaf.

NOT VIABLE: Tobacco production economics fail in poor rooting: establishment costs $2,000-2,500/ac (plants, 
plastic mulch, drip, fertility, labor), harvest/curing costs $500-800/ac (labor-intensive), total investment 
$2,500-3,300/ac versus gross returns (1,600 lb × $1.00 average = $1,600/ac), net loss $900-1,700/ac. Tobacco 
buyers reject poor quality leaf - cannot market production even if grown. DO NOT attempt tobacco in poor 
rooting - high costs with no market for poor quality leaf guarantee financial disaster.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Very shallow soil (<25cm) makes quality tobacco 
production completely impossible. Tobacco requires minimum 24-30 inches rooting for marketable leaf; very 
shallow conditions provide <12 inches. No possibility of producing quality leaf meeting market standards.

UNMARKETABLE PRODUCTION: Tobacco plants in very shallow soil: grow to 18-30 inches tall (vs 48-72 normal), 
produce small narrow leaves (8-12 inches vs 18-30), experience continuous severe stress, develop poor leaf 
characteristics (thin, light-colored, harsh, poor curing, no aroma), yield <800-1,200 lb/ac if anything, grade 
as trash/no-grade (completely unmarketable), buyers reject loads (no commercial value). Tobacco industry has 
strict quality standards - very shallow soil cannot produce acceptable leaf.

FINANCIAL DISASTER: Tobacco requires highest input investment among field crops: $2,500-3,500/ac establishment 
(transplants $300-500, plastic mulch $200-300, drip irrigation $150-250, intensive fertility $300-500, pesticides 
$200-400, equipment/supplies $400-600), labor costs $500-1,000/ac (transplanting, topping, suckering, harvest), 
curing facility costs $500-800/ac (barns, energy). Total investment $3,500-5,300/ac with ZERO return (trash-
grade leaf has no market value). DO NOT ATTEMPT tobacco in very poor rooting - guaranteed total loss of massive 
investment. Tobacco worst high-input crop choice for very shallow soils - combines extreme costs with zero 
marketability."""
    },

    "Clover": {
        "Very High": """Excellent (SQ3: 80-100). Multiple clover species varying rooting: White clover (shallow 
1-2 ft fibrous), Red clover (moderate 3-5 ft taproot), Alsike clover (moderate 2-4 ft). Excellent conditions 
support all types with maximum productivity and stand persistence.""",
        "High": """Good (SQ3: 60-79). Adequate for all clover types. White clover (most shallow-tolerant), 
Alsike and Red clover perform well. 3-4 ft depth sufficient for productive stands.""",
        "Medium": """Moderate (SQ3: 40-59). White and Alsike clovers best adapted. Red clover marginal with 
shortened stand life (1-2 years). 2-3 ft adequate for annual/biennial types.""",
        "Low": """Poor (SQ3: 20-39). White clover only viable option (most shallow-tolerant legume). Annual 
clovers (crimson, berseem) better than perennials. 18-24 inches minimum.""",
        "Very Low": """Very poor (SQ3: 0-19). No perennial clovers viable. Annual clovers marginal. <12 inches 
inadequate for legume production - choose non-legume covers or non-agricultural use."""
    },

    "Grass Hay": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil supports all hay grass types: Deep-rooted (orchardgrass, 
tall fescue, switchgrass 4-6 ft), Medium (timothy, bromegrass 2-4 ft), Shallow (ryegrass, bluegrass 1-2 ft). 
Maximum forage yields 5-8 ton/ac, excellent stand longevity, superior drought tolerance.""",
        "High": """Good (SQ3: 60-79). Adequate for most hay grasses. Deep and medium-rooted types perform well 
(orchardgrass, fescue, timothy, brome). 3-4 ft depth supports 4-6 ton/ac yields with good stand persistence 
(4-6+ years).""",
        "Medium": """Moderate (SQ3: 40-59). Medium and shallow-rooted grasses best adapted. Timothy, brome, 
ryegrass viable. Orchardgrass and tall fescue marginal. 2-3 ft depth supports 3-5 ton/ac with moderate stand 
life (3-5 years).""",
        "Low": """Poor (SQ3: 20-39). Shallow-rooted grasses only (ryegrass, bluegrass, some fescues). Annual 
hay crops better than perennials (sudangrass, annual ryegrass). 18-24 inches supports 2-4 ton/ac - frequent 
reseeding needed.""",
        "Very Low": """Very poor (SQ3: 0-19). Perennial hay production non-viable. Annual forage grasses marginal 
(sudangrass, forage sorghum, annual ryegrass). <12 inches inadequate for sustained forage - consider grazing 
only or non-forage use."""
    },

    "Silage Corn": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil ideal for silage corn's extensive root 
system (60-150cm). Same rooting as grain corn but higher biomass demands (18-25 tons/ac silage vs 7-10 tons 
grain). Excellent conditions support maximum tonnage with quality (32-35% dry matter, good digestibility).""",
        "High": """Good (SQ3: 60-79). Adequate for commercial silage production. 3-5 ft rooting supports 15-22 
tons/ac silage. Slightly better adapted than grain corn due to earlier harvest (reduced late-season stress). 
Good quality achievable with proper harvest timing.""",
        "Medium": """Moderate (SQ3: 40-59). Viable for silage with irrigation. 2-3 ft rooting limits tonnage 
to 12-18 tons/ac. Earlier harvest (silage) advantage over grain corn (avoids late drought stress). Irrigation 
during vegetative growth critical for tonnage.""",
        "Low": """Poor (SQ3: 20-39). Marginal for silage corn. Better than grain corn (harvest at milk/dough 
stage avoids grain-fill stress) but still problematic. 8-14 tons/ac maximum with intensive irrigation. Consider 
forage sorghum (more stress-tolerant, 10-18 tons/ac possible).""",
        "Very Low": """Very poor (SQ3: 0-19). Silage corn non-viable. <12 inch rooting inadequate for biomass 
production. Forage sorghum or sudangrass better alternatives if attempting any silage. Generally avoid - very 
shallow soil unsuited for any corn production."""
    },

    # ========================================================================
    # VEGETABLE CROPS
    # ========================================================================

    "Tomatoes": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil ideal for tomatoes' 
moderately deep taproot system (60-90cm effective depth, potential to 100-150cm). Root architecture: Central 
taproot with extensive lateral branching in top 30-45cm (70-80% of root mass). Excellent conditions support 
40+ tons/ac fresh market or 50+ tons/ac processing tomatoes with extended harvest period (90-120 days). Deep 
rooting critical for: (1) Consistent moisture uptake preventing blossom-end rot, (2) Extended nutrient access 
throughout long season, (3) Plant stability during heavy fruit load (30-50 lb per indeterminate plant), (4) 
Drought tolerance during peak production. Staking/caging systems require deep anchorage. MANAGEMENT: Encourage 
deep rooting with initial deep watering (avoid shallow frequent irrigation establishing shallow roots). No 
physical restrictions allow optimal root penetration. Transplant establishment rapid. Multiple successive 
plantings viable. Economics: Premium production site - high investment ($2,000-4,000/ac establishment) justified 
by maximum yields and quality.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Adequate depth (60-80cm) for tomato production with 
commercial viability. Some minor restrictions (moderate compaction at depth, scattered coarse fragments) but 
doesn't significantly limit root penetration in critical 45-60cm zone. Root development: Taproot reaches 
restricting layer but extensive lateral system in top 30-45cm adequate for 30-40 tons/ac fresh market. 
CRITICAL: Maintain good tilth in upper profile where most roots concentrate. Deep tillage before planting 
breaks any moderate compaction in 30-45cm zone. IRRIGATION MANAGEMENT: More frequent than very high class - 
limited deep reserve requires monitoring. Drip irrigation optimal for precise water delivery to root zone. 
Mulching reduces moisture stress. CHALLENGES: Blossom-end rot risk higher if moisture fluctuates (less deep 
buffer than excellent soils). Ca uptake dependent on consistent moisture in restricted root volume. Staked 
systems may show instability in high winds. MANAGEMENT: Side-dress fertilization throughout season (limited 
deep nutrient scavenging). Maintain consistent soil moisture (critical with limited rooting depth). Good 
commercial production site with proper management. Economics: Viable commercial production - establishment 
costs ($1,500-3,000/ac) return adequate profit at 30-40 ton yields.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Restricted rooting depth (45-60cm effective) 
limits tomato production to 20-30 tons/ac with intensive management. Restrictions: Moderate compaction, 
fragipan, dense clay layer, or high coarse fragments restrict root penetration below 45-60cm. Taproot stunted 
or deflected; lateral roots compressed into upper profile. Root concentration in top 30cm (85-90% of mass) 
makes crop vulnerable to surface conditions. INTENSIVE MANAGEMENT REQUIRED: (1) Raised beds improve effective 
rooting depth by 15-20cm, (2) Deep ripping/subsoiling before establishment essential, (3) Drip irrigation with 
fertigation mandatory (limited root volume requires frequent precise inputs), (4) Heavy mulching maintains 
moisture in shallow root zone, (5) Windbreaks critical (shallow anchorage = lodging risk). CHALLENGES: 
Blossom-end rot severe with moisture fluctuation (shallow roots can't buffer). Poor drought tolerance - 
irrigation interruption catastrophic. Fruit quality variable - heat stress affects shallow-rooted plants more. 
Determinate varieties better adapted than indeterminate (less height/weight stress on roots). FERTILITY: 
Very frequent light applications (weekly fertigation) essential - limited root exploration volume requires 
spoon-feeding. Economics: Marginal for commercial field tomatoes ($1,200-2,500/ac establishment costs difficult 
to recover at 20-30 ton yields). Consider processing tomatoes (lower quality requirements) or high-value 
heirloom varieties (premium prices offset lower yields).""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Severely restricted rooting (<45cm effective depth) makes 
commercial tomato production non-viable. Yields <20 tons/ac with very poor quality. Severe restrictions: Shallow 
bedrock, hardpan at 30-45cm, severe compaction, very high coarse fragments (>50%), or shallow water table 
confine roots to top 30cm. Tomatoes' moderate rooting needs (60-90cm optimal) cannot be met. Root system: 
Stunted taproot, limited laterals, 90-95% mass in top 20cm - essentially growing as shallow-rooted crop. 
PROBLEMS: (1) Severe drought stress even with irrigation, (2) Blossom-end rot epidemic (Ca uptake failure), 
(3) Plant toppling/lodging despite staking, (4) Nutrient deficiencies despite fertilization (limited 
exploration), (5) Heat stress severe (shallow roots can't access cooler deeper moisture), (6) Very short 
harvest period before decline. NOT RECOMMENDED: Commercial field production economically impossible. Very 
high establishment costs ($1,500+/ac) cannot be recovered with <20 ton yields and poor quality. IF ATTEMPTING: 
Raised beds 18-24 inches tall (doubles effective rooting depth to 60cm), intensive drip fertigation, heavy 
mulching, only determinate varieties, processing tomatoes only (fresh market quality unattainable). 
ALTERNATIVE: Consider shallow-rooted vegetables (lettuce 15-20cm, onions 20-30cm, leafy greens 15-25cm) better 
adapted to severe restrictions. Or intensive soil modification (deep ripping, profile reconstruction) before 
attempting tomatoes - multi-year investment required.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Extreme restrictions (effective depth <30cm) make 
tomato production impossible. Bedrock, hardpan, or cemented layer at <30cm, or extreme compaction throughout 
profile prevent any meaningful root development. Tomatoes require minimum 45-60cm for marginal production - 
<30cm absolutely inadequate. ROOT FAILURE: Taproot hits barrier at 15-25cm, laterals cannot compensate, plant 
essentially container-grown in shallow soil volume. Complete production failure: Plants wilt despite irrigation, 
widespread blossom-end rot, severe nutrient deficiencies, extensive plant death, fruit set minimal or absent, 
quality unmarketable. DO NOT ATTEMPT field tomatoes - guaranteed economic disaster. No amount of management 
overcomes extreme physical restrictions. ALTERNATIVES: (1) Raised beds 24-36 inches tall filled with imported 
soil (creates 60-90cm rooting depth) - expensive ($5,000-10,000/ac) but viable for high-value niche production, 
(2) Container production (5-10 gallon pots) with soilless media - small-scale only, (3) Greenhouse/high tunnel 
with controlled root media - bypasses field limitations entirely, (4) Choose site better suited to vegetables - 
tomatoes high-value crop requiring good conditions. SITE RECOMMENDATION: Do not use for intensive vegetable 
production. Consider permanent pasture, forest, or extensive use not requiring deep rooting. If must grow 
vegetables, only extremely shallow-rooted types (radishes, lettuce, herbs) marginally viable."""
    },

    "Potatoes": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep, loose, friable soil ideal for potatoes' 
shallow to moderate fibrous root system (45-60cm most roots, potential to 90-120cm). ROOT ARCHITECTURE: Fibrous 
root system from underground stem sections (seed piece nodes) - no true taproot. Multiple adventitious roots 
per plant, high density in top 30cm (60-70% of mass). DUAL REQUIREMENTS: (1) Tubers form in top 15-30cm 
(require loose, friable conditions for expansion without deformation), (2) Feeding roots extend 45-90cm 
(require deep penetration for water/nutrient access). Excellent conditions support 500+ cwt/ac (25+ tons/ac) 
with superior grade and tuber quality. Deep rooting critical for: (1) Consistent moisture (tuber quality depends 
on uniform water supply), (2) Nutrient uptake throughout 100-120 day season, (3) Drought tolerance during bulking 
(75-95 days after planting), (4) Prevention of growth cracks and secondary growth from moisture stress. SOIL 
STRUCTURE: Friable, non-compacted soil throughout profile essential. Bulk density <1.4 g/cm³ ideal - allows 
both tuber expansion and root penetration. MANAGEMENT: Maintain loose tilth in 0-30cm tuber zone (hilling, 
mulching). Deep roots access subsoil moisture reducing irrigation. No restrictions = maximum production potential. 
Economics: Premium production site - establishment costs ($800-1,500/ac) justified by 500+ cwt yields at 
$8-15/cwt = $4,000-7,500/ac gross.""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Adequate depth and structure (60-80cm) for commercial 
potato production. Minor restrictions (moderate density at depth, some coarse fragments 15-35%) but tuber zone 
(0-30cm) and primary root zone (30-60cm) adequate for 400-500 cwt/ac. Root development: Fibrous roots reach 
60-80cm before encountering restrictions. Main feeding roots in top 45-60cm. TUBER ZONE CRITICAL: Top 15-30cm 
must be friable and loose regardless of subsoil conditions. Rocks/compaction below 30cm less problematic than 
in tuber zone. MANAGEMENT: (1) Deep tillage/subsoiling before planting breaks moderate compaction below tuber 
zone, (2) Hilling creates 20-25cm raised bed improving effective tuber depth, (3) Rock removal from tuber zone 
critical (causes misshapen tubers even if roots penetrate deeper), (4) Maintain friable tilth through season 
(avoid compaction during cultivation/harvest). IRRIGATION: More critical than on deep soils - moderate restrictions 
limit deep moisture reserve. Timely irrigation during tuber bulking prevents stress-related defects (growth 
cracks, knobs, second growth). FERTILITY: Nutrients must be available in upper 60cm - less deep scavenging than 
excellent soils. Side-dress applications beneficial. Good commercial site with proper management. Economics: 
Viable production - $800-1,200/ac establishment returns profit at 400-500 cwt and $8-12/cwt = $3,200-6,000/ac 
gross.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Restricted rooting depth (40-60cm effective) 
challenges potato production but 300-400 cwt/ac achievable with intensive management. Restrictions: Compacted 
layer at 40-60cm, fragipan, dense clay, coarse fragments (35-50%), or seasonal perched water limit root 
penetration. Fibrous roots compressed into top 40-50cm. TUBER ZONE ISSUES: If restrictions begin <30cm, serious 
tuber deformation problems. Minimum 25-30cm loose soil required for marketable tubers. MANAGEMENT INTENSIVE: 
(1) Raised beds/ridges 25-30cm tall essential (effectively doubles tuber zone depth), (2) Deep ripping to 45-60cm 
before bed formation critical, (3) Careful irrigation scheduling (limited root volume = high stress sensitivity), 
(4) Drip irrigation with fertigation mandatory (precise control needed), (5) Avoid varieties with deep tuber set 
(choose shallow tuber formers). CHALLENGES: Growth cracks common with moisture fluctuation (shallow roots can't 
buffer). Small tuber size. Lower specific gravity (processing quality reduced). Increased cull percentage from 
irregular shapes. Harvest difficult if wet (compaction damages shallow tubers). VARIETY SELECTION: Early 
maturing varieties better than late (less time for stress accumulation). Russets problematic (need deep roots). 
Round whites more tolerant. Fingerlings work well (shallow tuber set). Economics: Marginal profitability - 
$800-1,500/ac costs difficult to recover at 300-400 cwt yields with increased culls. Viable for high-value 
specialty potatoes ($0.50-1.50/lb retail = $25-75/cwt farm gate).""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Severely restricted rooting (<40cm effective) makes 
commercial potato production economically non-viable. Yields <300 cwt/ac with very poor grade. Severe 
restrictions: Hardpan at 25-40cm, bedrock, heavy clay, very high coarse fragments (>50%), or high water table 
compress roots into top 25-35cm. Tubers form in top 15-25cm where restrictions most severe. ROOT SYSTEM FAILURE: 
Fibrous roots unable to penetrate below 30-40cm. Plants essentially growing in very shallow soil volume (similar 
to large container). Tuber zone overlaps with restriction zone = severe quality problems. PRODUCTION PROBLEMS: 
(1) Severe moisture stress (daily irrigation required), (2) Tuber deformation epidemic (rocks, compaction deform 
developing tubers), (3) Green tubers common (inadequate soil cover), (4) Growth cracks and secondary growth 
(stress-induced), (5) Very low specific gravity (processing unsuitable), (6) Small size and poor grade (50-70% 
culls), (7) Difficult harvest (tubers near surface damaged by digger). NOT RECOMMENDED: Field potato production 
economically impossible. Establishment costs ($800+/ac) cannot be recovered with <300 cwt yields and 50-70% 
culls. Fresh market unsaleable; processing plants reject low specific gravity. IF ATTEMPTING: (1) Extremely tall 
raised beds 30-40cm (expensive and erosion-prone), (2) Very early varieties only (minimize stress exposure - 
90-100 days vs 120-140 late varieties), (3) Specialty types for niche markets only (tiny new potatoes, 
fingerlings), (4) Intensive daily irrigation/fertigation. ALTERNATIVES: Choose crops better suited to severe 
restrictions. Shallow vegetables (onions, lettuce) or intensive soil reconstruction before potatoes.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Extreme restrictions (effective depth <25cm) make 
potato production completely impossible. Bedrock, hardpan, or cemented layer at <25cm, or extreme compaction 
throughout profile prevent root development and tuber formation. Potatoes require absolute minimum 30-40cm for 
even marginal production - <25cm physically inadequate for tubers to form and expand. COMPLETE FAILURE: Root 
system cannot establish beyond 15-25cm. Tuber formation impossible or severely deformed (flattened, cracked). 
Plants show severe stress symptoms immediately. Widespread plant death despite irrigation. Tubers green from 
inadequate cover. DO NOT ATTEMPT field potatoes under any circumstances - physical impossibility, not management 
challenge. Zero return on investment guaranteed. ALTERNATIVES: (1) Raised beds 36-48 inches tall filled with 
imported soil (creates 90-120cm rooting depth) - extremely expensive ($8,000-15,000/ac) only viable for very 
high-value seed potato production or specialty niche markets, (2) Container production with soilless media - 
small scale only, not commercial field production, (3) Choose completely different site for potatoes - this soil 
physically unsuitable. SITE RECOMMENDATION: Do not use for any root/tuber crop production (potatoes, carrots, 
beets, etc.). Even extremely shallow vegetables struggle. Consider only shallow-rooted leaf crops (lettuce, 
spinach) in raised beds, or abandon intensive crop production entirely (permanent pasture, forest)."""
    },

    "Sweet Potatoes": {
        "Very High": """Excellent (SQ3: 80-100). Deep loose soil (60-100cm) ideal for sweet potato's moderate tap/storage root (45-75cm, storage roots 20-40cm deep). Supports 400+ bu/ac (25+ tons/ac). Good soil structure critical for root shape and skin quality.""",
        "High": """Good (SQ3: 60-79). Adequate 50-75cm depth for 300-400 bu/ac. Sandy loam texture ideal. Minor restrictions acceptable - less sensitive than Irish potatoes. Good root shape and quality with proper management.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-60cm adequate for 200-300 bu/ac. Better tolerance than Irish potatoes. Some root deformation on heavy soils. Early varieties preferred. Raised beds beneficial.""",
        "Low": """Poor (SQ3: 20-39). Limited to 150-200 bu/ac. More tolerant than Irish potatoes but quality suffers. Small, misshapen roots. Better choice than Irish potatoes at this level. Intensive management required.""",
        "Very Low": """Very poor (SQ3: 0-19). Production marginal (<150 bu/ac). Still more viable than Irish potatoes. Extreme restrictions cause severe root deformation. Not economically recommended."""
    },

    "Onions": {
        "Very High": """Excellent (SQ3: 80-100). Loose soil ideal for onions' very shallow fibrous roots (20-30cm, 80% in top 15cm). Supports 800+ cwt/ac. Despite shallow rooting, benefits from deep unrestricted profile (excellent drainage, tilth).""",
        "High": """Good (SQ3: 60-79). Adequate for 600-800 cwt/ac. Surface conditions (0-25cm) critical - restrictions below don't affect onions. Good bulb size and storage quality.""",
        "Medium": """Moderate (SQ3: 40-59). If restrictions >25cm: 400-600 cwt/ac viable. If restrictions <20cm: severe impact. Raised beds improve drainage. Bulb uniformity variable.""",
        "Low": """Poor (SQ3: 20-39). Restrictions in critical 0-25cm zone limit to 300-400 cwt/ac. Shallow roots cannot overcome poor surface conditions. Small bulbs, poor storage. Consider green bunching onions.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme surface restrictions make bulb onions non-viable. Very shallow roots (20-30cm) cannot establish. Green bunching onions marginally possible in raised beds."""
    },

    "Carrots": {
        "Very High": """Excellent (SQ3: 80-100). Deep loose friable soil (45-75cm) ideal for carrot taproot (30-45cm taproot + feeding roots to 60cm). Supports 30+ tons/ac with perfect root shape. No obstacles = no forking or deformation.""",
        "High": """Good (SQ3: 60-79). Adequate 50-70cm depth for 20-30 tons/ac. Minor coarse fragments acceptable if <25%. Good root shape. Top 40cm must be loose and rock-free for straight marketable carrots.""",
        "Medium": """Moderate (SQ3: 40-59). Limited 40-55cm restricts to 15-20 tons/ac. Some root deformation. Rocks cause forking. Short varieties (Chantenay, Danvers) better than long (Imperator). Quality variable.""",
        "Low": """Poor (SQ3: 20-39). Severe restrictions (<40cm) limit to 10-15 tons/ac. High forking and deformation. Only short round varieties (Paris Market, Thumbelina) viable. Processing grade only.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions (<30cm) make carrot production non-viable. Taproot cannot penetrate. Severe deformation. Baby carrots in deep raised beds only option."""
    },

    "Lettuce": {
        "Very High": """Excellent (SQ3: 80-100). Friable soil excellent for lettuce's very shallow fibrous roots (15-25cm, 90% in top 15cm). Despite being shallowest major vegetable, benefits from excellent deep conditions (perfect surface tilth, drainage). Supports 600+ cartons/ac.""",
        "High": """Good (SQ3: 60-79). Adequate for 450-600 cartons/ac. Critical: surface conditions (0-20cm) must be excellent regardless of subsoil. Lettuce cannot reach deep restrictions. Fine seedbed preparation essential.""",
        "Medium": """Moderate (SQ3: 40-59). If restrictions >20cm: 300-450 cartons/ac viable. If restrictions <15cm: severe impact. Raised beds 15-20cm mandatory. Leaf lettuce more tolerant than crisphead.""",
        "Low": """Poor (SQ3: 20-39). Surface restrictions (<20cm) catastrophic for very shallow roots (15-25cm). <300 cartons/ac. Poor germination and establishment. Only baby leaf lettuce in tall raised beds.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme surface restrictions (<15cm) make lettuce impossible. Shallowest major vegetable - if it won't grow, nothing will. Microgreens in containers only option."""
    },

    "Cabbage": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) ideal for cabbage's moderate fibrous/taproot system (45-75cm, moderate taproot with extensive laterals). Supports 30+ tons/ac (600+ cartons) with excellent head formation and storage life.""",
        "High": """Good (SQ3: 60-79). Adequate 60-80cm for 22-30 tons/ac. Moderate rooting more vigorous than lettuce/onions but less than tomatoes. Good head firmness and quality. 90-120 day season.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 45-60cm limits to 15-22 tons/ac. Head formation variable. Early varieties better than late storage types. Raised beds improve performance. Some head splitting under stress.""",
        "Low": """Poor (SQ3: 20-39). Severe restrictions (<45cm) limit to 10-15 tons/ac. Poor head formation. Small loose heads. Very demanding crop for poor conditions. Consider less demanding brassicas (kale, collards).""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make cabbage non-viable. Among most demanding vegetables. Multiple deficiencies prevent head formation. Not recommended - choose kale or collards."""
    },

    "Broccoli": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) ideal for broccoli's moderate to deep fibrous/taproot (50-75cm). Supports 8+ tons/ac (300+ cartons) with excellent head size and quality.""",
        "High": """Good (SQ3: 60-79). Adequate 60-80cm for 6-8 tons/ac. Similar rooting to cabbage. Uniform head maturity. Good conditions support quality production with proper management.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 45-60cm limits to 4-6 tons/ac. Head size smaller. Buttoning (premature tiny heads) more common under stress. Quality variable. Less demanding than cauliflower.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<45cm) severely limit to <4 tons/ac. Small heads, buttoning, irregular maturity. Not economically viable. Consider kale instead.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make broccoli non-viable. High nutrient and rooting demands cannot be met. Buttoning severe. Choose kale or collards - more tolerant brassicas."""
    },

    "Cauliflower": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (70-100cm) critical for cauliflower's moderately deep fibrous/taproot (60-90cm - deeper than cabbage/broccoli). Supports 7+ tons/ac (300+ cartons) with white, tight curds. Most demanding common brassica.""",
        "High": """Good (SQ3: 60-79). Adequate 70-90cm for 5-7 tons/ac but requires intensive management. Cauliflower more demanding than cabbage/broccoli. Uniform fertility and moisture critical during curd formation.""",
        "Medium": """Moderate (SQ3: 40-59). Marginal for cauliflower (most demanding brassica). 3-5 tons/ac maximum with very intensive management. Small curds, discoloration common. Ricey (grainy) curds from stress. Consider broccoli instead.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions make cauliflower production non-viable. Extremely high rooting and nutrient demands cannot be met. Very small curds or failure to form curds. Not recommended - grow broccoli or cabbage.""",
        "Very Low": """Very poor (SQ3: 0-19). Impossible. Most nutrient-demanding vegetable. Cannot overcome extreme restrictions. Among worst vegetable choices for poor conditions. Grow kale or collards instead."""
    },

    "Peppers": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) ideal for peppers' moderate taproot (50-75cm effective, potential to 90-120cm). Supports 30+ tons/ac (750+ bushels) with extended harvest. Critical for consistent moisture preventing blossom-end rot.""",
        "High": """Good (SQ3: 60-79). Adequate 50-70cm for 22-30 tons/ac. Somewhat less vigorous than tomatoes. Blossom-end rot risk higher with limited deep moisture. Drip irrigation and Ca management critical.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-55cm limits to 15-22 tons/ac. MORE limiting than for tomatoes. Blossom-end rot severe. Large-fruited bells non-viable. Hot peppers (Jalapeno, Serrano) more tolerant. Intensive management required.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<40cm) makes bells non-viable. Hot peppers marginally possible with intensive management (<15 tons/ac). Blossom-end rot epidemic. Only stress-tolerant hot pepper varieties.""",
        "Very Low": """Very poor (SQ3: 0-19). All pepper production impossible. Minimum 40-50cm required - <30cm inadequate for even tolerant hot pepper varieties. Raised beds 30-40 inches only viable option."""
    },

    "Cucumbers": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (50-75cm) good for cucumbers' shallow to moderate fibrous roots (30-45cm most roots, to 60cm). Supports 700+ bushels/ac (20+ tons/ac) with extended harvest 50-70 days.""",
        "High": """Good (SQ3: 60-79). Adequate 45-60cm for 500-700 bushels/ac. Shallow-rooted (30-45cm) but benefits from deeper access. Frequent irrigation suits shallow root system. Good fruit quality and yield.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 35-50cm limits to 350-500 bushels/ac. Shallow roots (30-45cm) cannot scavenge deeply. Drip fertigation mandatory. Fruit quality issues more common (misshapen, pale, bitter).""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<35cm) limit to 200-350 bushels/ac. Very shallow roots cannot effectively scavenge nutrients. Small, misshapen, bitter fruit. Short harvest period. Not economically viable.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions (<30cm) make cucumber production non-viable. Shallow root system and continuous fruiting cannot overcome extreme limitations. Raised bed production only option."""
    },

    "Squash": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) supports squash moderate to deep fibrous/taproot (45-75cm). Summer squash 800+ bushels/ac (25+ tons/ac), winter squash 30+ tons/ac. Vigorous vine growth and heavy fruit production.""",
        "High": """Good (SQ3: 60-79). Adequate 50-75cm for summer squash 600-800 bushels/ac or winter squash 22-30 tons/ac. Good conditions support vigorous vines and continuous (summer) or large fruit (winter) production.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-60cm supports summer squash 400-600 bushels/ac or winter squash 15-22 tons/ac. Zucchini most tolerant summer type. Winter squash challenging. Disease pressure increases.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<45cm) limit summer squash to 250-400 bushels/ac, winter squash 10-15 tons/ac. Poor vine vigor. Consider zucchini (most tolerant). Winter squash especially challenging.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make commercial squash non-viable. High nutrient and rooting demands cannot be met economically. Raised bed production with imported soil only option."""
    },

    "Pumpkins": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-100cm) ideal for pumpkins' moderate to deep fibrous/taproot (50-90cm). Large-fruited cultivars (40-100 lb) respond vigorously. Supports 25+ tons/ac with extensive vine growth (15-20 ft spread). Long season 100+ days.""",
        "High": """Good (SQ3: 60-79). Adequate 60-80cm for 18-25 tons/ac. Heavy supplemental fertilization for large fruit types. Multiple fruits per vine on large-fruited types. Good color and size.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 45-70cm supports 12-18 tons/ac. Favor smaller-fruited cultivars (pie pumpkins 4-8 lb) over jack-o-lantern types. Fruit size smaller, fewer fruits per vine. Miniature varieties better adapted.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<50cm) limit to 8-12 tons/ac. Poor vine vigor, limited spread. Small fruit, poor color. Large jack-o-lantern types not viable. Stick with small pie pumpkins.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make pumpkin production non-viable. High demands for extensive vine system and large fruit cannot be economically met. Even miniature varieties struggle."""
    },

    "Watermelon": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (70-100cm) excellent for watermelon's deep taproot (60-90cm effective, to 120cm+). Extensive lateral roots 30-60cm. Supports 40+ tons/ac with excellent size (20-30 lb) and sweetness (12-13° Brix). Long season 85-100 days.""",
        "High": """Good (SQ3: 60-79). Adequate 70-90cm for 30-40 tons/ac. Deep rooting critical for large fruit and sugar content. 3-4 fruits per vine typical. Good shelf life with proper K nutrition.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 50-70cm limits to 20-30 tons/ac. Fruit size smaller (15-20 lb), sugar reduced (10-11° Brix). Hollow heart more common. Consider smaller-fruited icebox types.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<55cm) limit to 12-20 tons/ac. Small fruit (8-15 lb), poor sugar (<10° Brix), pale flesh. Not recommended. Consider other melons (cantaloupe slightly less demanding).""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make watermelon production non-viable. High demands for extensive vine system and large fruit cannot be met economically. Not recommended even small-scale."""
    },

    "Cantaloupe": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) supports cantaloupe moderate taproot/fibrous system (45-75cm). Supports 900+ cartons/ac (25+ tons/ac) with excellent size (3-5 lb), sweetness (12-14° Brix), firm flesh, good shelf life.""",
        "High": """Good (SQ3: 60-79). Adequate 50-75cm for 650-900 cartons/ac. Good fruit quality - sweet (11-13° Brix), aromatic, firm flesh with good netting. 80-90 day season manageable with good rooting.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-60cm limits to 450-650 cartons/ac. Fruit size smaller (2-3 lb), sugar reduced (9-11° Brix). Less aromatic, softer flesh. Fusarium wilt pressure increases under stress.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<45cm) limit to 300-450 cartons/ac. Small fruit (1-2 lb), poor sugar (<9° Brix), soft flesh, poor shelf life. Disease pressure high. Consider honeydew (slightly less demanding).""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make cantaloupe non-viable. Multiple deficiencies prevent acceptable fruit. Fusarium wilt and soilborne diseases severe in poor soils. Not economically feasible."""
    },

    "Snap Beans": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (50-75cm) good for snap beans' moderate fibrous/taproot (40-60cm). Supports 7+ tons/ac with excellent pod quality. Despite N-fixing, benefits from good rooting for nutrient and moisture access.""",
        "High": """Good (SQ3: 60-79). Adequate 45-65cm for 5-7 tons/ac. Good pod quality - tender, straight, good color. Multiple harvests on pole types. Better nodulation than dry beans but less than soybeans.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 35-55cm supports 3-5 tons/ac. Snap beans more sensitive than dry beans to poor conditions. Pod quality variable. Bush types less demanding than pole types.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<40cm) limit to 2-3 tons/ac with poor quality. Quite sensitive to poor soil. Small, tough, poorly colored pods. Not economically viable. Lima beans slightly more tolerant.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make snap bean production non-viable. Moderately sensitive to soil conditions. Extreme limitations prevent nodulation and acceptable growth. Poor pod quality."""
    },

    "Peas": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (50-75cm) good for peas' moderate fibrous/taproot (40-60cm with moderate taproot). Cool-season crop supports 4+ tons/ac with excellent pod fill and sweetness.""",
        "High": """Good (SQ3: 60-79). Adequate 45-65cm for 3-4 tons/ac. Peas have good nodulation capacity. Good pod fill and quality. English peas, snap peas, and snow peas all respond well.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 35-55cm acceptable for 2-3 tons/ac. Peas relatively tolerant of moderate conditions - good cool-season choice at this level. Pod quality acceptable.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions limit to 1-2 tons/ac. More tolerant than many vegetables but still need reasonable conditions. Small pods with poor fill. Austrian winter peas (field type) more tolerant than garden types.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme limitations reduce production to <1 ton/ac. Even peas' moderate requirements challenged. Poor nodulation. If using legume at this level, peas among better choices."""
    },

    "Sweet Corn": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-100cm) ideal for sweet corn's fibrous root system (50-75cm most roots, to 100-150cm). Similar to field corn. Supports 250+ dozen ears/ac with full kernel fill, sweetness, and quality.""",
        "High": """Good (SQ3: 60-79). Adequate 50-80cm for 180-250 dozen ears/ac. Sweet corn has high demands similar to field corn. Good ear development (8-9 inches) with proper fertilization and moisture.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-60cm limits to 120-180 dozen ears/ac. Ear size reduced (7-8 inches), tip fill variable. Early varieties better than full-season. Standard sugary types less demanding than supersweet.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions (<45cm) limit to 80-120 dozen ears/ac. Sweet corn's high demands difficult to meet. Small ears (6-7 inches), poor tip fill. Not economically viable. Similar demands to field corn.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make sweet corn non-viable. Same high demands as field corn - among highest of vegetable crops. Multiple deficiencies produce stunted plants, mostly barren stalks."""
    },

    "Spinach": {
        "Very High": """Excellent (SQ3: 80-100). Friable soil excellent for spinach's very shallow fibrous roots (15-25cm, 90% in top 10cm). Despite very shallow rooting, benefits from excellent conditions (perfect surface tilth). Supports 8+ tons/ac with rapid growth 40-50 days.""",
        "High": """Good (SQ3: 60-79). Adequate for 6-8 tons/ac. Critical: surface conditions (0-20cm) excellent. Very shallow roots (15-25cm) cannot reach deep restrictions. Quick growth produces tender, flavorful leaves.""",
        "Medium": """Moderate (SQ3: 40-59). If restrictions >20cm: 4-6 tons/ac viable. If restrictions <15cm: severe impact. Very shallow roots sensitive to surface problems. Baby leaf more successful than large leaf.""",
        "Low": """Poor (SQ3: 20-39). Surface restrictions (<20cm) limit to 2-4 tons/ac. Very shallow roots (15-25cm) cannot scavenge. Small, pale, tough leaves. Consider less demanding leafy greens (kale, chard, collards).""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme surface restrictions make spinach non-viable. Very shallow root system and high N demands cannot overcome extreme deficiencies. Raised bed production with imported soil only option."""
    },

    "Kale": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (60-90cm) supports kale's moderate fibrous/taproot (45-70cm). Most tolerant common brassica. Supports 20+ tons/ac fresh weight with extended harvest (120+ days). Cold-hardy, continues production into winter.""",
        "High": """Good (SQ3: 60-79). Adequate 50-75cm for 15-20 tons/ac over extended harvest. More tolerant than cabbage/broccoli/cauliflower. Multiple harvests over several months. Tender leaves with excellent flavor.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 40-60cm supports 10-15 tons/ac. Kale MORE tolerant of moderate conditions than most brassicas. Good brassica choice for moderate fertility/rooting conditions. Leaves tougher, more fibrous.""",
        "Low": """Poor (SQ3: 20-39). Poor conditions limit to 6-10 tons/ac. Kale MOST tolerant of poor conditions among common brassicas - best brassica choice at low fertility. Still viable where cabbage, broccoli, cauliflower fail. Consider collards (even more tolerant).""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions reduce to <6 tons/ac. Even kale's superior tolerance has limits. Among brassicas, kale and collards most likely to survive at this level but production marginal."""
    },

    # ========================================================================
    # FRUIT & NUT CROPS
    # ========================================================================

    "Apples": {
        "Very High": """Excellent rooting conditions (SQ3: 80-100). Deep unrestricted soil (120-180cm+) ideal for apple trees' extensive deep root system (2-4 m effective depth, potential to 6+ m). ROOT ARCHITECTURE: Semi-spreading to deep system with lateral scaffolding roots 30-90cm deep and vertical sinker roots to 2-4+ m. Rootstock dramatically affects depth: Dwarf (M9, M26) 90-150cm, Semi-dwarf (M7, MM106) 150-240cm, Standard seedling 240-400cm+. Excellent conditions support productive orchards 30+ years with 600-1,000+ bu/ac. Deep rooting critical for: (1) Drought tolerance during critical periods (bloom, fruit set, sizing), (2) Winter survival (deep roots less frost damage), (3) Nutrient access from large soil volume over decades, (4) Tree stability against wind and crop load (200-400 bu mature tree), (5) Longevity (multi-decade investment). MANAGEMENT: Rootstock selection critical - match rooting vigor to soil depth. Deep ripping before planting on compacted sites. Permanent sod or ground cover between rows (roots permeate area). Economics: Premium orchard site - establishment costs ($8,000-15,000/ac) justified by 30-40 year productive life and high-value fruit ($15-30+/bu fresh market).""",
        
        "High": """Good rooting conditions (SQ3: 60-79). Adequate depth (150-240cm) for commercial apple production on appropriate rootstocks. Minor restrictions at depth (moderate compaction, fragipan, coarse fragments) manageable with proper rootstock selection. Root development: Lateral scaffolds to 60-90cm, sinker roots reach restriction at 150-240cm. Adequate for 500-800 bu/ac on semi-dwarf rootstocks. ROOTSTOCK CRITICAL: Avoid vigorous standards (need 240+ cm). Semi-dwarf (MM106, M7, G935) optimal - roots vigorous enough to penetrate moderate restrictions but not requiring extreme depth. Dwarf (M9, M26) acceptable if restrictions >120cm. MANAGEMENT: (1) Deep ripping before planting if compaction <150cm, (2) Proper site preparation (eliminate hardpans in rooting zone), (3) Irrigation more critical than on deep soils (limited drought buffer), (4) Mulching under trees maintains root zone moisture. CHALLENGES: Shorter productive life (20-30 years vs 40+ on deep soils). More irrigation dependent. Yield ceiling lower. Good commercial site with proper management. Economics: Viable with $8,000-12,000/ac establishment for 20-30 year orchard life.""",
        
        "Medium": """Moderate rooting conditions (SQ3: 40-59). Restricted rooting depth (100-180cm effective) limits apple production to dwarf/semi-dwarf rootstocks only. Standard rootstocks completely unsuitable. Restrictions: Hardpan at 100-180cm, fragipan, bedrock, dense clay, or seasonal perched water limit penetration. Expect 400-600 bu/ac with intensive management on appropriate rootstocks. ROOTSTOCK SELECTION CRITICAL: (1) Dwarf M9, M26, G16 best choices (rooting 90-150cm fits restrictions), (2) Some semi-dwarf viable if restrictions >150cm (G890, G210), (3) Absolutely avoid vigorous rootstocks (MM111, seedling) - trees will fail. INTENSIVE MANAGEMENT: High-density planting (300-500 trees/ac vs 100-200 traditional) compensates for smaller tree size. Trellis systems mandatory for dwarf rootstocks (limited anchorage in restricted soil). Very frequent irrigation (shallow roots dry quickly). Annual fertility critical (limited root exploration volume). CHALLENGES: Trees less stable (wind damage, crop load stress). Shorter productive life (15-25 years). Lower per-tree yield but high density compensates. Economics: Marginal for traditional orchards. High-density dwarf systems more viable ($15,000-20,000/ac establishment but earlier bearing, intensive production). Consider tart cherries or other less rooting-demanding tree fruits.""",
        
        "Low": """Poor rooting conditions (SQ3: 20-39). Severely restricted rooting (<100cm effective) makes traditional apple orchard establishment economically unviable. Yields <400 bu/ac with very poor tree health and short productive life. Severe restrictions limit roots to top 60-100cm. Even dwarf rootstocks struggle (normally need 90-150cm). ROOT SYSTEM FAILURE: Inadequate depth for tree stability and drought tolerance. Trees topple in wind despite staking. Severe moisture stress even with irrigation. Limited nutrient uptake from small root volume. PRODUCTION PROBLEMS: (1) Poor tree establishment (3-5 years vs 2-3 normal), (2) Stunted growth throughout life, (3) Biennial bearing severe (stress-induced), (4) Small fruit size, poor color, (5) Disease pressure extreme (stressed trees), (6) Orchard life 10-15 years maximum (vs 25-40+ normal), (7) Early tree decline and death. NOT RECOMMENDED: Standard orchard planting economically impossible. Establishment costs ($8,000+/ac) cannot be recovered over short productive life with poor yields. IF ATTEMPTING: (1) Only ultra-dwarf rootstocks (Bud9, G65) with <100cm rooting need, (2) Very high-density hedgerow systems (800-1,000+ trees/ac), (3) Permanent trellis support (trees cannot self-support), (4) Intensive daily irrigation/fertigation, (5) Accept 10-15 year replacement cycle vs 25-40+ year standard. Economics extremely questionable. ALTERNATIVES: Consider small fruits better suited to restricted rooting (blueberries 60-90cm, strawberries 30-45cm). Or intensive soil modification (deep ripping, profile reconstruction) before apple planting - multi-year expensive investment.""",
        
        "Very Low": """Very poor rooting conditions (SQ3: 0-19). Extreme restrictions (effective depth <60cm) make apple tree production completely impossible. Bedrock, hardpan, or cemented layer at <60cm prevents establishment of even ultra-dwarf rootstocks (absolute minimum 75-90cm required). Apple trees require minimum rooting depth that this soil cannot provide. COMPLETE FAILURE: Trees cannot establish functional root system. Rapid decline and death even with intensive care. No meaningful fruit production. Severe toppling despite staking. DO NOT ATTEMPT apple orchard planting under any circumstances - guaranteed total loss. Zero return on investment. Extremely expensive establishment ($8,000-15,000/ac) lost entirely. ALTERNATIVES: (1) Not viable even with raised beds (would need 4-5 ft tall beds filled with imported soil across entire orchard = $50,000-100,000/ac - completely non-economic), (2) Container production impractical for commercial orchards (tree size, yield too limited), (3) Choose completely different site for apples - tree fruits require reasonable rooting depth. SITE RECOMMENDATION: This soil fundamentally unsuitable for any tree fruit production. Apple among least tolerant tree fruits to shallow soils. Consider only shallow-rooted crops (strawberries, vegetables) or abandon fruit production entirely (permanent pasture, annual crops). Multi-year soil modification inadequate - bedrock/hardpan limits cannot be economically overcome."""
    },

    "Peaches": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil (120-180cm+) ideal for peach trees' moderately deep root system (1.5-3 m effective, potential to 4+ m). Spreading lateral scaffolds 30-60cm + deeper sinkers. Supports 300-500 bu/ac for 12-15 year orchard life. Excellent drainage critical (peaches cannot tolerate wet feet).""",
        "High": """Good (SQ3: 60-79). Adequate 150-240cm depth for 250-400 bu/ac. Peaches somewhat MORE tolerant of moderate restrictions than apples (shorter-lived, less vigorous). Excellent drainage more critical than extreme depth. Good site for standard peach production.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 100-150cm acceptable for 200-300 bu/ac. Peaches relatively tolerant - shorter productive life (12-15 years) means less cumulative rooting need than apples (25-40 years). Dwarf rootstocks available. Workable site with proper management.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<100cm) limits to 150-250 bu/ac. Poor tree health, shortened life (8-10 years). Challenging economics. Stone fruits generally require better conditions than this level provides.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions (<75cm) make peach production inadvisable. Poor tree growth and survival. Peaches sensitive to poor drainage and shallow rooting. Not recommended without major site preparation."""
    },

    "Strawberries": {
        "Very High": """Excellent (SQ3: 80-100). Friable soil ideal for strawberries' very shallow fibrous roots (15-30cm most roots, to 45cm maximum). Despite very shallow rooting, benefits greatly from deep unrestricted soil (perfect surface tilth, excellent drainage). Supports 20,000+ lb/ac over 2-4 year planting cycle.""",
        "High": """Good (SQ3: 60-79). Adequate for 15,000-20,000 lb/ac. Critical: surface conditions (0-30cm) excellent regardless of subsoil. Very shallow roots (15-30cm) don't reach deep restrictions. Raised beds with plastic mulch and drip irrigation optimal.""",
        "Medium": """Moderate (SQ3: 40-59). If restrictions >30cm: 10,000-15,000 lb/ac viable. If restrictions <25cm: severe impact despite shallow roots. Strawberries' very shallow fibrous system (15-30cm) requires excellent surface conditions. Raised beds mandatory.""",
        "Low": """Poor (SQ3: 20-39). Surface restrictions (<30cm) limit to 6,000-10,000 lb/ac. Quite demanding for shallow-rooted crop. Poor plant vigor, small berries, disease pressure. Annual hill system more successful than matted row. Economics marginal.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme surface restrictions (<20cm) make commercial production non-viable. Shallow roots and high demands cannot overcome extreme limitations. Raised bed systems with complete soil replacement only option."""
    },

    "Blueberries": {
        "Very High": """Excellent (SQ3: 80-100) IF pH 4.5-5.5. Deep soil (90-150cm) ideal for blueberries' shallow to moderate fibrous root system (45-90cm most roots, to 120cm). Very shallow fibrous roots (no taproot) but benefits from depth for drought buffer. Supports 12,000+ lb/ac over 20-30 year planting. CRITICAL: Acid pH (4.5-5.5) absolutely required regardless of rooting conditions.""",
        "High": """Good (SQ3: 60-79) IF pH 4.5-5.5. Adequate 75-120cm for 8,000-12,000 lb/ac. Shallow fibrous roots (45-90cm) don't need extreme depth but require excellent drainage and acid conditions. High organic matter (pine bark mulch) critical for shallow root moisture management.""",
        "Medium": """Moderate (SQ3: 40-59) IF pH 4.5-5.5. Restricted 60-90cm supports 6,000-8,000 lb/ac. Blueberries' shallow roots (45-90cm) fit moderate depth IF surface excellent and pH acid. If native pH >6.0, acidification required (sulfur applications 2-3 years). Raised beds with acid mix preferable if pH >7.0.""",
        "Low": """Poor (SQ3: 20-39). Poor rooting AND wrong pH make blueberries very challenging. Yields <6,000 lb/ac. If native pH >6.5, acidification extremely difficult - not recommended. If pH naturally acid (4.5-5.5), blueberries viable with fertility amendments. pH MORE critical than depth for blueberries.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions complicated by pH requirements make blueberries inadvisable. If pH >7.0 (alkaline), completely unsuitable - Fe chlorosis severe even with acidification. Not recommended without raised beds with imported acid soil mix."""
    },

    "Grapes": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil (180-300cm+) ideal for grapes' very deep root system (2-4 m effective, potential to 6-8+ m in arid regions). Deepest-rooted common fruit crop. Lateral scaffolds 30-90cm + massive vertical sinker roots to great depth. Supports 8-12 tons/ac wine or 15+ tons/ac table grapes over 25-30+ year vineyard life. Deep rooting allows: (1) Extreme drought tolerance (deep soil moisture access), (2) Large nutrient reservoir over decades, (3) "Terroir" expression (roots sample deep soil layers), (4) Minimal irrigation in many climates.""",
        "High": """Good (SQ3: 60-79). Adequate 150-240cm for 5-8 tons/ac wine or 12-15 tons/ac table grapes. Grapes very deep-rooted but adaptable. Roots reach restriction but adequate lateral development. Good viticulture site. Irrigation more important than on very deep soils. Quality wine production viable - moderate vigor sometimes enhances fruit quality.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 120-180cm acceptable for 4-6 tons/ac wine or 8-12 tons/ac table grapes. Grapes relatively TOLERANT of moderate depth due to efficient deep rooting and drought adaptation. Vines may show stress symptoms but often produce excellent wine quality - moderate vigor desirable. Table grapes require more intensive irrigation and fertility than wine grapes at this level.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<120cm) limits to 2-4 tons/ac wine or 5-8 tons/ac table grapes. Grapes normally very deep-rooted (2-4+ m). Limited to <120cm reduces vigor and yield significantly. Young vine establishment slower. Wine quality may be acceptable if vines healthy. Table grapes challenging. Consider wine varieties (more tolerant) over table types.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions (<90cm) make new vineyard establishment inadvisable. Grapes normally among deepest-rooted crops (2-6+ m). Limiting to <90cm severely compromises vigor, longevity, drought tolerance. Not recommended for viticulture without major multi-year soil improvement including deep tillage."""
    },

    "Almonds": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil (180-300cm+) ideal for almonds' very deep root system (2-4 m effective, to 6+ m in deep soils). Very similar rooting to grapes - among deepest-rooted deciduous trees. Supports 3,000+ lb/ac over 25+ year orchard. Deep rooting critical for drought tolerance in arid production regions (California Central Valley).""",
        "High": """Good (SQ3: 60-79). Adequate 180-240cm for 2,200-3,000 lb/ac. Almonds very deep-rooted and demand excellent drainage. Minor restrictions acceptable if >180cm. Irrigation management more intensive than on very deep soils. Good commercial site.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 120-180cm marginal for 1,500-2,200 lb/ac. Almonds extremely high nutrient demands AND very deep rooting needs difficult to meet from moderate depth. Young tree establishment slower. Consider economics carefully - long production cycle (25+ years) requires excellent conditions.""",
        "Low": """Poor (SQ3: 20-39). Poor rooting (<120cm) makes almond production economically unviable. Almonds among most demanding tree crops for both nutrients and rooting depth. Cannot achieve commercial yields. Not recommended for new orchard establishment. Choose different site.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make almond production completely inadvisable. Almonds require deep, well-drained soils for decades-long production. Not suitable under any circumstances. Multi-decade investment requires excellent soil resources from start."""
    },

    "Walnuts": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil (240-360cm+) ideal for walnuts' extremely deep root system (3-6 m effective, potential to 8-10+ m). Among deepest-rooted temperate trees. Massive lateral scaffolds + vertical sinkers to great depth. Supports 3,000-4,000 lb in-shell/ac over 50+ year orchard life. Deepest rooting of common nut trees.""",
        "High": """Good (SQ3: 60-79). Adequate 240-300cm for 2,500-3,500 lb/ac. Walnuts extremely deep-rooted (3-6 m) - require deeper soil than most tree crops. Good baseline for 50+ year orchard if depth >240cm. Deep rooting (12-20 ft) accesses subsoil nutrients and moisture.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 180-240cm marginal for commercial walnut production. Expect 1,800-2,500 lb/ac. Walnuts' extremely deep rooting (3-6+ m normal) and very long production life (50+ years) require excellent depth. Young tree establishment (10-15 years to bearing) demands unrestricted rooting. Economics questionable - decades of limited productivity.""",
        "Low": """Poor (SQ3: 20-39). Poor rooting (<180cm) makes walnut orchards economically unviable. Walnuts among deepest-rooted and most demanding tree crops with longest production cycle. Young trees fail to develop properly. Not recommended under any circumstances. Choose different site or crop.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make walnut production impossible. Walnuts require deep, fertile soils for 50-100+ year productive life. Multi-generational investment requires exceptional soil resources including depth >240cm minimum. Absolutely unsuitable."""
    },

    "Pecans": {
        "Very High": """Excellent (SQ3: 80-100). Deep unrestricted soil (300-450cm+) ideal for pecans' extremely deep root system (4-7 m effective, to 10+ m documented). DEEPEST-ROOTED common temperate tree crop. Massive tree (60-100 ft) requires massive root system. Supports 2,000+ lb in-shell/ac over 75+ year orchard life. Deep rooting (15-20+ ft) essential for supporting huge biomass and heavy nut crops.""",
        "High": """Good (SQ3: 60-79). Adequate 300-360cm for 1,500-2,000 lb/ac. Pecans THE deepest-rooted common nut crop (4-7+ m). Require deeper soil than walnuts. Good baseline for 75+ year orchard if depth >300cm (10 ft+). Intensive management essential for these massive, long-lived trees.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 240-300cm marginal to unsuitable. Pecans among highest rooting demands of any tree crop and longest production life (75+ years). Young tree development very slow at moderate depth. Yields <1,500 lb/ac. Not recommended for new orchard - choose site with >300cm depth.""",
        "Low": """Poor (SQ3: 20-39). Poor rooting (<240cm) makes pecan production economically impossible. Pecans THE most rooting-demanding common tree nut crop. Cannot establish viable orchard. Young trees severely stunted, may never bear nuts. Not recommended under any circumstances. Pecans require deep, fertile soils for multi-generational (75-100+ year) production.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make pecan production completely impossible. Pecans require the deepest soils (>300cm minimum, >450cm optimal) for 75-100+ year productive life. Absolutely unsuitable - among most soil-demanding crops in temperate agriculture. Multi-generational investment requires exceptional depth and fertility. Do not attempt."""
    },

    # ========================================================================
    # SPECIALTY CROPS
    # ========================================================================

    "Hops": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (150-240cm) ideal for hops' deep fibrous/taproot system (1.5-3 m roots from perennial crown). Vigorous annual bines (18-20 ft) require deep anchorage and moisture access. Supports 2,500+ lb/ac over 20+ year yard life. Deep rooting critical for: (1) Supporting massive annual biomass (removed entirely each harvest), (2) Drought tolerance during critical cone development, (3) Crown winter survival and regeneration.""",
        "High": """Good (SQ3: 60-79). Adequate 120-180cm for 1,800-2,500 lb/ac. Hops moderately deep-rooted perennial. Roots reach restriction but adequate for vigorous annual growth. Irrigation more important than on deep soils. Good commercial site with proper trellis support and management.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 90-150cm limits to 1,200-1,800 lb/ac. Intensive management required. Bine vigor reduced. Irrigation critical during cone development. Yield and quality suffer. Marginal for premium hop production meeting brewing specifications.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<90cm) makes commercial hop production unviable. Yields <1,200 lb/ac with poor cone quality. Weak bine growth. Multi-year investment in perennial crop requires good conditions. Not recommended.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make hop production impossible. Hops' deep rooting needs and massive annual growth cannot be supported. Poor crown establishment and survival. Multi-year perennial investment requires good soil. Not feasible."""
    },

    "Hemp": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (120-180cm) ideal for hemp's deep taproot (1-2 m effective, to 2-3 m potential). Fiber hemp (10+ ft) benefits most from deep rooting. Supports: Fiber 8-10 tons/ac, Grain 1,500+ lb/ac, CBD 1,500+ lb/ac. Deep taproot provides excellent drought tolerance and nutrient scavenging.""",
        "High": """Good (SQ3: 60-79). Adequate 100-150cm for all hemp types. Deep taproot reaches restriction but lateral development adequate. Fiber (6-8 tons/ac), Grain (1,200-1,500 lb/ac), CBD (1,200-1,500 lb/ac). Hemp efficient nutrient user with good rooting.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 75-120cm supports: Fiber (4-6 tons/ac), Grain (800-1,200 lb/ac), CBD (800-1,200 lb/ac). Hemp's reputation for thriving on marginal land somewhat accurate - better tolerance than many crops. Grain hemp most tolerant, fiber most demanding of depth.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<75cm) limits all types. Fiber (<4 tons/ac), Grain (<800 lb/ac), CBD (<800 lb/ac). Hemp somewhat tolerant but quality and yields suffer. Grain type best choice (shortest, least demanding). Historic marginal land production was low-value fiber, not modern high-value products.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make commercial hemp non-viable. Even hemp's tolerance has limits. Stunted plants, poor quality. Modern hemp production (fiber, grain, CBD) requires reasonable rooting for economic returns. Not recommended."""
    },

    "Herbs": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil benefits most herbs though many prefer MODERATE conditions. Rooting varies: Deep (sage, lavender, rosemary 60-120cm taproots), Moderate (oregano, thyme, mint 30-60cm), Shallow (basil, parsley, cilantro 20-40cm). CAUTION: Mediterranean herbs often produce best essential oils at moderate fertility and rooting - excessive vigor reduces oil concentration.""",
        "High": """Good (SQ3: 60-79). Often OPTIMAL for aromatic Mediterranean herbs (lavender, thyme, oregano, rosemary, sage). Adequate 60-90cm for deep-rooted types, excellent for moderate/shallow. Mediterranean herbs evolved on thin soils - moderate rooting encourages oil production. Leafy types (parsley, cilantro, basil) benefit from better conditions.""",
        "Medium": """Moderate (SQ3: 40-59). Acceptable to PREFERRED for many Mediterranean herbs. Lavender, thyme, oregano, rosemary thrive at 45-75cm depth - produce concentrated oils. Leafy types need supplemental irrigation and fertility. Many herbs BEST at this level - adapted to moderate conditions.""",
        "Low": """Poor (SQ3: 20-39). Limits most herbs though Mediterranean types tolerate better than vegetables. Thyme, oregano, lavender survive at 30-50cm but yields low. Leafy types (basil, parsley, cilantro) struggle. Small plants, reduced oil content. Still better than many crops at low rooting.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions (<30cm) make most herb production non-viable. Even drought-tolerant Mediterranean herbs severely limited. Minimal growth, poor quality. Small-scale thyme and oregano marginally possible. Not commercially viable."""
    },

    "Cut Flowers": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil ideal for diverse flower rooting: Deep (peonies, roses, dahlias 60-120cm), Moderate (lisianthus, zinnias, sunflowers 40-60cm), Shallow (annuals, bulbs 20-40cm). Premium quality stems - length, strength, bloom size, vase life. High-value crops justify excellent conditions.""",
        "High": """Good (SQ3: 60-79). Adequate 60-90cm for most cut flowers. Long stems, large blooms, good colors. Perennials (roses, peonies) establish well. Succession plantings of annuals productive. Good baseline for quality cut flower production meeting market standards.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 45-70cm acceptable for many species. Tolerant types (zinnias, sunflowers, cosmos) perform well. Demanding types (roses, lisianthus, peonies) need intensive management. Stem length and bloom size may be reduced. Select species for rooting conditions.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<45cm) limits cut flowers. Short stems, small blooms fail market standards. Only most tolerant species (sunflowers, zinnias, wildflowers) viable. Premium flowers (roses, peonies) not feasible. Not economically viable for most species.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make commercial cut flower production non-viable. Multiple deficiencies prevent acceptable stem and bloom quality. High-value crops but extreme restrictions prevent economic production. Raised bed production small-scale only."""
    },

    "Christmas Trees": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil (120-180cm+) ideal for conifers' moderately deep taproot systems (1-2 m effective, to 3+ m mature trees). Rapid growth, excellent form, dark green color over 6-10 year cycle. Different species vary: Spruce (moderate-deep 1-2 m), Fir (moderate 1-1.5 m), Pine (moderate 1-1.5 m). Deep rooting supports large tree biomass and wind resistance.""",
        "High": """Good (SQ3: 60-79). Adequate 100-150cm for most Christmas tree species. Conifers generally moderate rooting depth. Good growth rate and color. Marketable 6-7 ft trees in optimal timeframe. Most species perform well: Pines most tolerant, Spruce relatively demanding, Fir intermediate.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 75-120cm acceptable for most species. Conifers LOW to MODERATE rooting demands. Growth rate slower - production cycle extends 1-2 years. Select tolerant species: Pines (Scotch, Virginia, White) most tolerant, avoid demanding types (Blue Spruce, Fraser Fir). Form and color acceptable.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<75cm) limits tree quality. Slow growth (10-12 years for marketable size), poor color, sparse branching. Select most tolerant: Virginia Pine, Scotch Pine, White Pine. Annual fertilization essential. Economics marginal - extended production cycle increases costs.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make Christmas tree production unviable. Very slow growth, poor survival, unacceptable quality. Production cycle exceeds acceptable timeframe (15+ years). While conifers relatively low demand, extreme restrictions prevent production. Not economically feasible."""
    },

    "Nursery Stock": {
        "Very High": """Excellent (SQ3: 80-100). Deep soil supports diverse ornamental species with varying rooting: Deep-rooted trees (oaks, maples, pines 1-3 m+), Moderate shrubs (0.5-1.5 m), Shallow perennials/groundcovers (0.2-0.6 m). Rapid growth meets specifications in 1-3 year production cycle. Species-specific rooting critical for selection.""",
        "High": """Good (SQ3: 60-79). Adequate 90-150cm for most field-grown ornamentals. Well-rooted, vigorous plants ready for landscape in standard timeframe. Most shrubs, perennials, small trees perform well. Large tree production may extend cycle slightly. Good commercial field growing site.""",
        "Medium": """Moderate (SQ3: 40-59). Restricted 60-100cm acceptable for adapted species with intensive management. Many natives and less demanding ornamentals viable. Container production often preferable to field at this level (allows media control). Select species suited to moderate depth. Production time may extend.""",
        "Low": """Poor (SQ3: 20-39). Severely restricted (<60cm) makes field production of most ornamentals unviable. Very slow growth, poor quality, extended times unacceptable. Container production strongly recommended over field. If field growing, focus exclusively on shallow-rooted adapted natives. Premium ornamentals require containers.""",
        "Very Low": """Very poor (SQ3: 0-19). Extreme restrictions make field nursery production impossible. Commercial quality and timeframe not achievable. Container growing with imported media required - field production not viable. Use site for different purpose or implement container systems exclusively."""
    }
}


def get_sq3_interpretation(crop: str, rating: str) -> str:
    """
    Get the enhanced interpretation for a specific crop and SQ3 rating.
    
    Parameters:
    -----------
    crop : str
        The name of the crop (must match keys in SQ3_INTERPRETATIONS)
    rating : str
        The SQ3 rating (Very High, High, Medium, Low, or Very Low)
    
    Returns:
    --------
    str
        The interpretation text for the specified crop and rating
    
    Raises:
    -------
    KeyError
        If the crop or rating is not found in the lookup table
    """
    if crop not in SQ3_INTERPRETATIONS:
        available_crops = ", ".join(sorted(SQ3_INTERPRETATIONS.keys()))
        raise KeyError(f"Crop '{crop}' not found. Available crops: {available_crops}")
    
    if rating not in SQ3_INTERPRETATIONS[crop]:
        available_ratings = ", ".join(SQ3_INTERPRETATIONS[crop].keys())
        raise KeyError(f"Rating '{rating}' not found for crop '{crop}'. Available ratings: {available_ratings}")
    
    return SQ3_INTERPRETATIONS[crop][rating]


def get_all_crops() -> list:
    """
    Get a list of all available crops in the interpretation table.
    
    Returns:
    --------
    list
        Sorted list of all crop names
    """
    return sorted(SQ3_INTERPRETATIONS.keys())


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
    interpretation = get_sq3_interpretation(crop_name, rating_value)
    print(f"\n{crop_name} - {rating_value} SQ3 Rating:")
    print(interpretation)
    print("\n" + "="*80)
    
    # Show all available crops
    print(f"\nTotal crops in database: {len(get_all_crops())}")
    print("\nCrops with comprehensive rooting condition interpretations:")
    for i, crop in enumerate(get_all_crops(), 1):
        print(f"{i:2d}. {crop}")
    
    print("\n" + "="*80)
    print("Comprehensive rooting features include:")
    print("  • Specific SQ3 score ranges (rooting conditions: 0-100 scale)")
    print("  • Detailed root system characteristics by crop")
    print("  • Effective rooting depths and patterns")
    print("  • Root development stages and timing")
    print("  • Physical barrier impacts on root growth")
    print("  • Management strategies for each rooting condition")
    print("  • Crop-specific minimum rooting requirements")
    print("  • Alternative crop recommendations for poor conditions")
    print("  • Economic viability assessments based on rooting limitations")
