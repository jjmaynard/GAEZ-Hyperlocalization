"""
SQ1 (Nutrient Availability) Enhanced Interpretations - COMPLETE
All 53 Crops with Detailed Nutrient Information

Based on FAO GAEZ methodology which evaluates:
- Topsoil (0-30cm): Texture, Organic Carbon, pH, Total Exchangeable Bases  
- Subsoil (30-100cm): Texture, pH, Total Exchangeable Bases

RATING SCALE:
- Very High: 85-100 (Excellent nutrient availability)
- High: 60-84 (Good nutrient availability)  
- Medium: 40-59 (Adequate nutrient availability)
- Low: 20-39 (Below-average nutrient availability)
- Very Low: 0-19 (Poor nutrient availability)
"""

SQ1_INTERPRETATIONS = {
    # ========================================================================
    # FIELD CROPS
    # ========================================================================
    
    "Corn": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High organic matter (>2%), optimal pH (6.0-7.0), abundant exchangeable bases (>20 cmol/kg). Natural fertility supports 150+ bu/ac with minimal fertilizer. Organic matter provides 60-80 lb N/ac through mineralization. Excellent conditions for nutrient uptake throughout 120+ day season.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Moderate to good organic matter (1-2%), near-optimal pH (5.5-7.5), adequate bases (10-20 cmol/kg). Baseline fertility good, supplemental N-P-K recommended for 120-150 bu/ac. Micronutrient deficiencies unlikely. Responsive to modest fertilizer inputs.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Low organic matter (0.5-1%), suboptimal pH (5.0-5.5 or 7.5-8.0), moderate bases (5-10 cmol/kg). Balanced NPK program essential for 80-120 bu/ac. May need lime if pH <5.5 or sulfur if pH >8.0. Test for micronutrients, especially Zn in high pH soils.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Very low organic matter (<0.5%), problematic pH (<5.0 or >8.5), low bases (<5 cmol/kg). Intensive fertilization required for 50-80 bu/ac. Al toxicity risk if pH <5.0. Fe chlorosis likely if pH >8.0. Build organic matter through residue return and cover crops.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Negligible organic matter, extreme pH (<4.5 or >9.0), negligible bases. Multiple severe deficiencies and toxicities. Not economically viable for corn without major reclamation. Consider grain sorghum, millet, or non-agricultural use."
    },
    
    "Soybeans": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High organic matter and optimal pH (6.0-7.0) support vigorous nodulation with 150-200 lb N/ac fixation potential. Abundant Ca, Mg, K, micronutrients. Can achieve 60+ bu/ac with minimal fertilizer. Despite N-fixing ability, benefits from excellent P, K, S, and micronutrients for optimal production.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Moderate organic matter, favorable pH (5.5-7.5) support good nodulation. Supplemental P-K may boost yields to 50-60 bu/ac. Inoculation beneficial if field lacks established rhizobia. Mo adequate at this pH range - critical for N fixation enzyme function.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Lower organic matter and suboptimal pH may limit nodulation efficiency. Balanced P-K-S program recommended. Lime critical if pH <5.5 to improve nodulation and Mo availability. Expect 35-50 bu/ac with proper management. Inoculation essential. Foliar Mo application may help if pH <6.0.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor soil conditions limit both nodulation and overall plant vigor. Very low organic matter reduces N mineralization backup. Problematic pH severely impacts nodulation - little N fixation expected without lime or sulfur. Intensive P-K-S fertilization needed. Expect 20-35 bu/ac.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Extreme pH and nutrient deficiencies prevent effective nodulation and N fixation. Legumes particularly vulnerable to extreme acidity (Al toxicity) and alkalinity (Fe, Mn deficiency). Multiple limiting factors make soybeans non-viable. Consider grain sorghum or forage species instead."
    },
    
    "Winter Wheat": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High organic matter provides steady N release during fall establishment and spring growth. Optimal pH ensures excellent P availability. Strong fall establishment potential (>30 tillers/plant). Expect 80+ bu/ac. Natural fertility may provide 60-80 lb N/ac through mineralization, reducing fertilizer needs.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Moderate fertility supports good fall establishment and tillering (20-30 tillers/plant). Supplemental spring N recommended for 60-80 bu/ac. Split N applications optimize use efficiency. P and K adequate in most cases. Good pH range supports nutrient availability through winter dormancy.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Lower organic matter limits fall N availability. Modest fall growth (10-20 tillers/plant) requires aggressive spring N program. Expect 40-60 bu/ac with fertilization. Fall P application beneficial for root development. If pH <5.5, lime improves overwinter survival and spring vigor. Split N (fall, green-up, jointing) essential.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fall establishment due to low fertility. Weak stands (<10 tillers/plant) vulnerable to winterkill. Very low organic matter provides minimal N. Spring growth limited even with fertilizer. Expect 25-40 bu/ac. Lime critical if pH <5.0 - improves winter hardiness. Heavy fall P needed for root development. Consider spring wheat instead.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Inadequate for successful winter wheat production. Extreme pH and nutrient deficiencies prevent fall establishment. Poor overwinter survival expected. Multiple stress factors compound. Not economically viable. Consider spring-planted small grains after soil improvement."
    },
    
    "Spring Wheat": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High organic matter releases N during active spring mineralization (warm, moist conditions). Optimal pH maximizes P availability critical for rapid spring growth. Excellent conditions support 60+ bu/ac potential. Strong early vigor allows crop to outcompete weeds. Good protein levels (13-15%) achievable with balanced fertility.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline fertility supports rapid spring growth. Supplemental N at planting plus early topdressing optimizes yields (50-60 bu/ac). P availability good for early root development. Adequate K and micronutrients. Protein content 12-14% typical. Quick early growth important in short season.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Lower fertility requires careful fertilizer management. Limited organic matter means less N mineralization during short growing season. Expect 35-50 bu/ac with balanced NPK program. Starter fertilizer at planting essential for root development. If pH <5.5, lime beneficial but won't take effect until next season.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor native fertility and limited growing season time for soil improvement. Intensive starter fertilizer essential. Very low organic matter provides negligible N during season. Expect 20-35 bu/ac even with fertilization. Protein content may be low (<11%). Consider barley or oats which tolerate lower fertility better.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Extreme limitations for spring wheat production. Very short growing season doesn't allow time for plants to overcome poor fertility. Multiple nutrient deficiencies compound. Expect <20 bu/ac even with intensive inputs - not economically viable. Consider hardier small grains (barley, oats) or forage crops."
    },
    
    "Cotton": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High organic matter and optimal pH (6.0-7.0) support vigorous vegetative growth and heavy boll load. Excellent K availability (cotton K-intensive, requiring 60+ lb K₂O/bale). Natural fertility supports 2+ bales/ac potential. Good micronutrient availability, especially B and Zn critical for reproduction. Long season allows full utilization of mineralized N.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 1.5-2 bales/ac production. Supplemental N, P, and especially K needed for maximum yields. Cotton's high K demand (40-60 lb K₂O/bale) requires K fertilization even in soils with moderate native fertility. Adequate micronutrients, though B may need monitoring. Split N applications match uptake pattern.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 1-1.5 bales/ac with intensive management. Balanced NPK program essential, with emphasis on K (cotton removes more K than N). Micronutrient deficiencies possible, especially Zn if pH >7.5 or B anywhere. Consider petiole testing at first square and first bloom. Lower organic matter may limit mid-season N.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor native fertility limits economic cotton production to <1 bale/ac. Very low organic matter provides minimal N release during long season. High K requirements difficult to meet economically. If pH <5.5, Al toxicity affects rooting; if pH >8.0, Fe and Zn chlorosis. Multiple micronutrient issues likely.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Extreme limitations make cotton production non-viable. Cotton's high nutrient demands (200+ lb N, 60+ lb P₂O₅, 150+ lb K₂O per 2 bales/ac) cannot be economically met from severely depleted soil. Multiple toxicities and deficiencies. Extreme pH prevents even fertilizer from being effective. Consider less demanding crops."
    },
    
    "Grain Sorghum": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 150+ bu/ac potential. Sorghum's advantage is superior drought tolerance, not high fertility requirement - under excellent nutrition, competes well with corn. Good organic matter and pH optimize nutrient uptake. Sorghum's efficient root system fully exploits available nutrients.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 120-150 bu/ac. Modest N-P-K inputs boost yields. Sorghum's deeper and more extensive root system than corn exploits moderate fertility more efficiently. Can produce well at lower fertilizer rates than corn (about 70-80% of corn's N requirement for equivalent yield).",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). This is sorghum's 'sweet spot' - moderate fertility where its efficiency advantages shine. Expect 80-120 bu/ac with balanced fertilization. More drought and nutrient stress tolerant than corn, making it preferred choice at this fertility level. Performs better than corn under identical conditions due to superior root system.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Preferred to corn at this fertility level. Can achieve 50-80 bu/ac where corn would struggle. Still requires fertilization but more efficient use of inputs. Better adapted to low organic matter soils than corn. In this range, sorghum is often THE recommended crop due to reliability and input-use efficiency. Al tolerance better than corn if pH <5.5.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Even sorghum's superior stress tolerance has limits. Below 20-50 bu/ac even with inputs. However, still more viable than corn or most other cereals at this fertility level. If cropping this soil, sorghum is best cereal choice. Consider pearl millet (even more stress-tolerant) or improved pasture/hay crops."
    },
    
    "Barley": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 100+ bu/ac feed barley, 80+ bu/ac malting quality. Optimal conditions for achieving >48 lb/bu test weight and <13% protein (malting target). High organic matter and good pH ensure excellent micronutrient availability. Barley responds well with strong tillering and plump kernels.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good conditions for 80-100 bu/ac feed barley, 60-80 bu/ac malting quality. Moderate N inputs optimize yield without excessive protein for malting types. Good test weights (>45 lb/bu) achievable. Adequate micronutrients, especially Mn and Cu important for enzyme development in malting barley.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 50-80 bu/ac. Balanced NPK needed, but barley has lower N requirement than wheat. Test weight may be reduced (42-45 lb/bu). For malting barley, this fertility level can work well - avoiding excessive N helps keep protein <13%. Split N allows adjustment based on variety and end use.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Limited fertility restricts yields to 30-50 bu/ac. Barley somewhat more tolerant of low pH (5.0-5.5) than wheat, so may perform better on acid soils. Test weights suffer (<42 lb/bu). Low protein may seem good for malting but accompanied by thin kernels and poor enzyme levels. Consider barley over wheat if pH slightly acid.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations reduce yields <30 bu/ac. Barley has some advantage over wheat in tolerating acid soils (pH 5.0-5.5) but extreme pH (<4.5 or >8.5) still severely limits production. Poor test weights and quality. Not economically viable. Consider oats (more acid-tolerant) or soil improvement."
    },
    
    "Oats": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 120+ bu/ac with excellent test weights (>38 lb/bu). Oats respond well to good fertility with strong straw and plump groats. High organic matter provides N for vigorous growth. Good pH ensures adequate P and micronutrients. Protein content 12-15% typical, good for feed or food oats.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good conditions support 90-120 bu/ac with good test weights (35-38 lb/bu). Oats have moderate N requirements - about 70% of wheat's N needs. Adequate P and K support strong straw and good grain fill. Suitable for both feed and food-grade production with proper variety selection.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility adequate for 60-90 bu/ac. Oats more tolerant of poor fertility and acid soils than wheat or barley - often preferred cereal at this fertility level. Test weights may be reduced (32-35 lb/bu). NPK fertilization beneficial but oats make efficient use of modest inputs. Good choice for soil building rotations.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Oats MOST tolerant of low pH (5.0-5.5) among major cereals - best choice for acid soils. Moderate fertility limits yields to 40-60 bu/ac. Oats' extensive fibrous root system exploits nutrients more efficiently than other small grains. Often outperform wheat and barley at this fertility level. Test weights <32 lb/bu. Good for nurse crop or forage use.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations but oats still most viable small grain option at extreme low fertility or acid pH. Yield <40 bu/ac. Superior acid tolerance (pH 4.5-5.0 tolerable) makes oats choice for bringing very poor land into production. Consider for forage (hay or silage) rather than grain. Good soil-building crop before more demanding species."
    },
    
    "Rice": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 8,000+ lb/ac under flooded conditions. Good organic matter critical - provides slow N release under anaerobic conditions. Optimal pH (5.5-6.5 for flooded rice) maximizes P availability. Adequate micronutrients, especially Zn and Fe which can become deficient under flooding despite good native levels.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 6,000-8,000 lb/ac. Supplemental N applied in splits (pre-flood, mid-season, heading) optimizes yields. Flooding alters nutrient dynamics - some nutrients become MORE available (P, Fe, Mn), others LESS (Zn, Cu). Moderate organic matter beneficial for sustained N release.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 4,000-6,000 lb/ac with balanced fertilization. Lower organic matter limits N release under flooded conditions. Careful N management essential - split applications timed to growth stages. Zn deficiency increasingly likely - consider Zn fertilization. P availability may improve under flooding despite moderate native levels.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor baseline fertility limits yields to 2,000-4,000 lb/ac. Very low organic matter provides minimal N under flooding. Heavy N fertilization required but losses to denitrification and volatilization significant. Zn deficiency highly likely - foliar or soil Zn application essential. If pH >7.5, P fixation by calcium carbonate problematic even under flooding.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations for rice production. Extreme pH (<5.0 or >8.0) problematic even under flooding. Very acid soils (pH <4.5) may have Fe, Mn toxicity under flooded conditions. Very alkaline soils (pH >8.5) suffer severe Zn and Fe deficiency. Multiple nutrient deficiencies compound. Consider soil reclamation or alternative use."
    },
    
    "Sunflower": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 3,000+ lb/ac seed yield (60+ bu/ac) with excellent oil content (>42%). Sunflower has HIGH nutrient demands (200+ lb N, 80+ lb P₂O₅, 200+ lb K₂O/ac). Good organic matter and pH optimize uptake by extensive root system (6-8 ft depth). Adequate B critical - sunflower highly sensitive to B deficiency affecting seed set.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 2,200-3,000 lb/ac (45-60 bu/ac). Despite drought tolerance, sunflower is nutrient-demanding crop. Supplemental N-P-K recommended for maximum yield and oil content. B deficiency possible - soil or foliar B application beneficial. Deep root system accesses subsoil nutrients effectively. Excellent scavenger of residual nutrients.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 1,600-2,200 lb/ac (32-45 bu/ac) with fertilization. Sunflower's deep tap root (6-8 ft) and extensive lateral roots somewhat compensate for moderate fertility. Balanced NPK program essential. B deficiency increasingly likely - critical for seed set and head filling. Sunflower preferred over corn at moderate fertility due to drought/stress tolerance.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 1,000-1,600 lb/ac (20-32 bu/ac). Intensive fertilization required for economic production. Despite nutrient scavenging ability, sunflower's high nutrient demands difficult to meet economically from low baseline. B deficiency very likely. Oil content may be reduced. Consider alternative oilseeds with lower requirements.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations for economic production. Sunflower's high nutrient demands (similar to corn) cannot be economically met from extremely poor baseline. Multiple deficiencies likely, especially B which is critical. Extreme pH severely limits production. Despite drought tolerance reputation, sunflower is nutrient-demanding crop not suitable for very poor soils."
    },
    
    "Canola": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 60+ bu/ac with >40% oil content. Optimal pH (6.0-7.0) and high organic matter crucial for fall establishment and spring growth. Canola has HIGH nutrient demands (150-200 lb N, 80+ lb P₂O₅, 60+ lb K₂O, 40+ lb S per 60 bu/ac). Adequate B and Mo critical. S especially important for oil quality and yield.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 45-60 bu/ac. Supplemental N-P-K-S program essential. Canola is nutrient-intensive, especially N and S. Fall fertility critical for root development and winter survival. Spring N application optimizes flowering and seed set. Adequate pH range (5.5-7.5) supports nutrient availability. B deficiency possible - important for flowering.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 30-45 bu/ac with intensive fertilization. Lower organic matter limits fall N availability. Canola sensitive to pH extremes - poor growth if pH <5.5 or >8.0. Heavy S requirement (20-40 lb S/ac) difficult to meet economically at this fertility level. Fall P application beneficial for root development. Consider winter survival issues if fertility low.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor baseline fertility makes canola economically marginal. Yields <30 bu/ac even with inputs. Canola's high nutrient demands difficult to satisfy from low baseline. Poor fall establishment leads to winterkill risk. If pH <5.5, lime application essential but may not improve soil in time for fall planting. S deficiency increasingly severe.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make canola production non-viable. Canola one of more nutrient-demanding crops - requires fertile soils. Extreme pH prevents establishment - very sensitive to pH <5.0 (Al toxicity) or >8.5 (multiple micronutrient deficiencies). Small seed size makes establishment difficult in poor soils. Consider spring-planted crops less sensitive to soil conditions."
    },
    
    "Dry Beans": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 3,000+ lb/ac with excellent seed quality. Optimal pH (6.0-7.0) and high organic matter support good nodulation and N₂ fixation (50-150 lb N/ac potential). Adequate Ca, Mg, K, micronutrients. Despite N-fixing ability, beans benefit from excellent overall fertility for high yields. Mo adequate at this pH range.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good conditions for 2,200-3,000 lb/ac. Moderate fertility adequate with proper inoculation. Supplemental P and K beneficial - beans remove significant P and K in seed. Unlike soybeans, common beans have limited N-fixing ability (fixing only 30-50% of N needs), so some N fertilization beneficial. Adequate micronutrients including Mo needed for N fixation.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 1,600-2,200 lb/ac with management. Common beans more sensitive to poor fertility than soybeans. Limited N-fixing ability means substantial N fertilization needed. Balanced NPK program essential. If pH <6.0, lime application improves nodulation and Mo availability. Beans sensitive to salt (EC >2 dS/m) and high pH (>8.0).",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor soil conditions limit yields to 1,000-1,600 lb/ac. Low fertility severely reduces nodulation and N fixation. Very low organic matter provides minimal N backup. Problematic pH (<5.5 or >7.5) impacts both nodulation and overall growth. Intensive P-K fertilization needed. Seed quality may be poor. Consider improving soil before bean production.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make bean production non-viable. Extreme pH and nutrient deficiencies prevent effective nodulation. Beans moderately sensitive to soil conditions - more so than soybeans, less so than snap beans. Multiple limiting factors compound stress. Multi-year soil improvement required. Consider forage legumes (more tolerant) or non-legume crops."
    },
    
    "Peanuts": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 5,000+ lb/ac with excellent grade and kernel quality. Optimal pH (5.8-6.2, slightly acid preferred) and high organic matter support good nodulation and N₂ fixation (100-150 lb N/ac). CRITICAL: peanuts need HIGH Ca (1,000-2,000 lb/ac) in pegging zone - gypsum applications standard even in fertile soils. Adequate K for large pods.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 4,000-5,000 lb/ac. Moderate fertility adequate with Ca supplementation (gypsum). Despite N-fixing ability, peanuts need excellent K (100-150 lb K₂O/ac) and Ca availability. Adequate B critical for peg development. Slightly acid pH (5.8-6.5) preferred over neutral - reduces disease pressure and optimizes Ca availability. Mg adequate for seed quality.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 3,000-4,000 lb/ac with intensive management. Balanced NPK program plus gypsum (500-1,000 lb Ca/ac) essential. Lower Ca availability directly impacts pod fill and grade. Adequate pH (5.5-6.5) critical - peanuts sensitive to pH <5.5 (Al toxicity affects pegging) and >7.5 (Ca precipitation). Pod quality suffers without amendments.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 2,000-3,000 lb/ac. Peanuts moderately sensitive to low fertility - higher requirements than soybeans due to Ca demands for pod development. Poor nodulation at low pH or fertility. Pod fill and kernel size severely affected by low Ca. High percentage of pops and immature pods. Grade suffers significantly.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make peanut production economically non-viable. Peanuts relatively demanding crop due to specific Ca requirements for proper pegging and pod development. Extreme pH (<5.0 or >7.5) severely limits both root/peg development and Ca availability. Multiple deficiencies compound. Not suitable without multi-year soil reclamation."
    },
    
    "Sugar Beets": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 30+ tons/ac root yield with 18%+ sugar content. Optimal pH (6.5-7.5, slightly alkaline tolerated well) and high organic matter optimize nutrient uptake. Beets are HEAVY feeders (150-200 lb N, 80-120 lb P₂O₅, 200-300 lb K₂O/ac). Adequate B critical - beets highly B-sensitive, deficiency causes heart rot and reduced sugar.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 25-30 tons/ac with 16-18% sugar. Heavy fertilization required despite good native fertility. Supplemental N-P-K essential, with emphasis on K. B deficiency increasingly likely - soil or foliar B critical. Adequate Na can partially substitute for K (beets Na-responsive). Split N applications prevent excessive vegetative growth.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 18-25 tons/ac with intensive fertilization. Beets' high nutrient demands difficult to meet economically from moderate baseline. Balanced NPK program with heavy K emphasis essential. B deficiency very likely - heart rot risk. Na application (salt-tolerant crop) can reduce K requirement. Sugar content may be reduced (14-16%).",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes beets economically marginal - yields <18 tons/ac with high input costs. Beets among most nutrient-demanding crops - require high native fertility or intensive fertilization. Poor root size and shape. Low sugar content (<14%). B deficiency severe - heart rot common. If pH <6.0, heavy lime required. Not recommended at this fertility level.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make beet production non-viable. Sugar beets require fertile soils - one of most nutrient-demanding crops commercially grown. Extreme pH severely limits production - though beets somewhat alkaline-tolerant (pH 8.0), pH >8.5 causes Fe and Mn deficiency. Extreme acidity (pH <5.5) limits root development. Not suitable without major reclamation."
    },
    
    "Sugarcane": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 100+ tons/ac cane yield with 14%+ sugar content. Sustains multiple productive ratoon crops (4-7 years). High organic matter and optimal pH (5.5-7.0) provide sustained nutrient release over long ratoon cycle. Cane is EXTREMELY nutrient-demanding (200-250 lb N, 100-150 lb P₂O₅, 400-500 lb K₂O per 100 tons cane). Adequate Si beneficial for stalk strength.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 80-100 tons/ac with 12-14% sugar over 3-5 ratoon cycles. Heavy fertilization required for each ratoon. Supplemental N-P-K essential, with very high K demands. Moderate organic matter supports several ratoons. Micronutrients (Fe, Mn, Zn, Cu) adequate. Ratoon decline accelerates after 4-5 crops at this fertility level.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 60-80 tons/ac for 2-3 ratoon cycles. Lower fertility accelerates ratoon decline - replanting frequency increases. Intensive fertilization required but nutrient use efficiency decreases in later ratoons. Balanced NPK with heavy K emphasis essential. Cane quality declines faster. Consider shorter ratoon cycle (2-3 crops) before replanting.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 40-60 tons/ac with poor ratoon longevity (1-2 crops). Sugarcane's extremely high nutrient demands difficult to meet economically from low baseline. Poor stool development leads to thin stands in ratoons. Very intensive fertilization required for plant crop and each ratoon. Sugar content reduced. Frequent replanting (every 2-3 years) necessary.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial sugarcane production non-viable. Sugarcane among most nutrient-demanding crops - requires fertile soils for sustained production. Poor plant crop establishment. No viable ratoon crops. Extreme pH (<5.0 or >8.0) severely limits production. Multi-year soil building required. Consider annual crops or pasture instead."
    },
    
    "Tobacco": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility can produce 3,000+ lb/ac cured leaf BUT risks excessive vegetative growth, delayed maturity, and poor curing quality. Tobacco is unique - moderate fertility often PREFERABLE for quality. High N produces dark, thick leaves with poor burn and smoking quality. Optimal pH (5.5-6.5, slightly acid) and moderate organic matter (1-2%) support quality leaf production.",
        
        "High": "Good nutrient availability (SQ1: 60-84). OPTIMAL for quality tobacco production (2,200-2,800 lb/ac cured leaf). Moderate fertility produces best balance of yield and quality. Controlled N management critical - too much N reduces leaf quality (poor burn, harsh taste). Split applications allow precise N management. Adequate K essential for quality - affects burn characteristics. Good micronutrient availability improves leaf chemistry.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for 1,600-2,200 lb/ac. Lower organic matter reduces excessive N availability - can be advantageous for leaf quality. Balanced NPK program with controlled N rates optimizes quality/yield balance. Slightly acid pH (5.8-6.2) preferred. Adequate K critical for proper curing and burn. This fertility level often produces acceptable quality with proper management.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 1,000-1,600 lb/ac with small leaf size and reduced quality. Thin leaves with poor body. Low organic matter limits N availability during rapid growth phases. If pH <5.5, lime application essential - tobacco sensitive to Mn toxicity and Al toxicity at low pH. K deficiency common - affects curing. Poor leaf quality and low market grades.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations for tobacco production. Very poor leaf development, small size, and unmarketable quality. Multiple deficiencies produce abnormal growth. Extreme pH (<5.0 or >7.0) severely limits production. Tobacco has moderate fertility requirements but extremely poor soils cannot produce marketable crop. Not economically viable without major soil improvement."
    },
    
    "Alfalfa": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 8+ tons/ac annually for 5+ years. Optimal pH (6.5-7.5) and high organic matter critical for deep rooting (10+ ft) and long-lived stands. Despite N-fixing ability (150-250 lb N/ac), alfalfa is HEAVY feeder requiring high P (60-100 lb P₂O₅/ac) and especially K (300-400 lb K₂O/ac annually). Adequate Ca, Mg, B, Mo essential for nodulation and productivity.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 6-8 tons/ac over 4-5 years. Heavy P and K fertilization required despite good native fertility - alfalfa removes large amounts in harvested forage. Annual K applications (200-300 lb K₂O/ac) essential for stand persistence. Adequate pH (6.0-7.5) critical for nodulation and long-term productivity. Moderate organic matter supports good stand longevity.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 4-6 tons/ac for 3-4 years. Shorter stand life at this fertility level. Intensive P-K fertilization required, especially K for each cutting. If pH <6.0, heavy lime application essential - alfalfa very pH-sensitive, requires pH >6.0 for effective nodulation and longevity. Mo deficiency increasingly likely below pH 6.0. Stand decline accelerates after 3 years.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility severely limits alfalfa - yields <4 tons/ac for 2-3 years only. Alfalfa particularly sensitive to low pH (<6.0), low Ca, and low P. Poor nodulation at this fertility level limits N fixation. Stand establishment difficult. Thin stands with significant weed pressure. Very intensive lime and fertilizer program required. Consider alternative forages (clover, grass-legume mixtures) better adapted.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make alfalfa production non-viable. Alfalfa one of most soil-demanding forages - requires fertile, well-limed soils. Extreme pH (<5.5 or >8.5) prevents successful establishment. Multiple severe deficiencies prevent nodulation and stand establishment. Thin stands with poor vigor and persistence. Not suitable without multi-year soil improvement. Consider grass hay or mixed grass-clover."
    },
    
    "Clover": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports dense, vigorous stands with 5+ tons/ac dry matter production. Optimal pH (6.0-7.0) and high organic matter support excellent nodulation and N₂ fixation (100-200 lb N/ac potential). Good P and K availability critical for legume establishment and persistence. Adequate Mo for N fixation. Ca and Mg support strong growth. Various clover species (red, white, alsike) all respond well.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good conditions for 4-5 tons/ac with persistent stands. Moderate fertility adequate for good nodulation. Supplemental P and K beneficial - clovers remove significant nutrients in harvested forage or grazing. Adequate pH (5.5-7.0) supports nodulation. Mo generally adequate at this pH. White clover tolerates lower fertility better than red clover. Good for permanent pasture mixtures.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 3-4 tons/ac. Most clovers tolerate moderate fertility reasonably well - more so than alfalfa. If pH <6.0, lime application improves nodulation and Mo availability. P and K fertilization important for establishment and persistence. White clover and alsike clover more tolerant of lower fertility than red clover. Mixed grass-clover stands work well at this level.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits stands to 2-3 tons/ac with reduced persistence. Lower fertility affects nodulation and N fixation. Problematic pH (<5.5 or >7.5) severely impacts legume performance. White clover most tolerant of poor conditions - consider for low-fertility situations. Alsike clover tolerates wet, acid soils better than other clovers. Red clover struggles. Intensive P-K and lime needed.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations for clover establishment and persistence. Extreme pH and nutrient deficiencies prevent effective nodulation. Poor growth and thin stands with heavy weed competition. Most clover species fail. Consider soil improvement or alternative forage grasses more tolerant of poor conditions. If using legume, try white clover (most tolerant) with heavy lime and fertilizer."
    },
    
    "Grass Hay": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 8+ tons/ac annually with 4-5 cuttings possible. High organic matter provides sustained N release throughout season. Optimal pH and nutrient levels support responsive, high-quality forage. Cool-season grasses (orchardgrass, timothy, tall fescue) respond vigorously. Warm-season grasses (bermudagrass, switchgrass) also highly productive. Protein content 12-18% depending on maturity and N rate.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 6-8 tons/ac with 3-4 cuttings. Moderate to heavy N fertilization required (150-250 lb N/ac split over cuttings) - grasses are non-legumes requiring external N. Adequate P and especially K critical - K removed in large amounts (40-50 lb K₂O/ton hay). Good quality forage with proper harvest timing. Most grass species respond well.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 4-6 tons/ac with 2-3 cuttings. Lower organic matter limits natural N availability. Balanced NPK program essential with 100-200 lb N/ac split application. K fertilization critical after each cutting. Stand persistence reduced without adequate fertility. Consider grass-legume mixtures (e.g., orchardgrass-clover) to reduce N requirements. Quality and yield both moderate.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 2-4 tons/ac. Very low organic matter provides minimal N - heavy N fertilization required for acceptable yields. Poor stand density and persistence. Grass-legume mixtures strongly recommended to provide biological N fixation. Orchardgrass-white clover or tall fescue-clover work at this level. Pure grass stands not economical without intensive fertilization.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations for productive hay production. Yields <2 tons/ac even with fertilization. Thin, weedy stands with poor nutritive value. Extremely low organic matter provides essentially no N. Economic hay production not viable. Consider soil improvement over several years using improved pasture management, lime, and amendments before attempting hay production. Native grass mixtures or extensive grazing more appropriate."
    },
    
    "Silage Corn": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 30+ tons/ac fresh weight (extremely high biomass production). Optimal conditions for maximum total dry matter (8+ tons DM/ac) with excellent digestibility (>70% TDN). High organic matter and pH provide nutrients for both vegetative growth and grain fill. Natural fertility can provide 60-80 lb N/ac, reducing fertilizer needs. Excellent feed quality with high grain content.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 25-30 tons/ac fresh weight (6-8 tons DM/ac). Silage corn has same or higher nutrient demands as grain corn (actually higher total removal due to whole-plant harvest). Supplemental N-P-K essential. About 10-15% higher N rate than grain corn needed (due to stover removal). Good feed quality with moderate grain content. Excellent digestibility.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 20-25 tons/ac fresh (5-6 tons DM/ac) with balanced fertilization. Lower organic matter limits N availability during rapid growth. Intensive NPK program required. Feed quality variable - lower grain percentage, more stalk. Digestibility 65-70% TDN. Still produces more total feed value per acre than grain corn alone at this level. Economic silage production possible.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 15-20 tons/ac fresh (4-5 tons DM/ac). Very low organic matter provides minimal N for massive biomass production. Heavy N requirement (180-220 lb N/ac) difficult to meet economically. Poor grain fill reduces feed quality. High stalk percentage, lower digestibility (60-65% TDN). Consider forage sorghum (better adapted to lower fertility) or grass-legume hay instead.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make silage corn production non-viable. Yields <15 tons/ac fresh with very poor quality (mostly stalk, little grain, <60% TDN). Corn's high nutrient demands cannot be economically met. Multiple deficiencies produce stunted plants with poor biomass accumulation. Not economically viable. Consider alternative forage crops (sorghum-sudangrass, improved pasture) better adapted to poor soils."
    },
    
    # ========================================================================
    # VEGETABLE CROPS  
    # ========================================================================
    
    "Tomatoes": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 40+ tons/ac fresh market or 50+ tons/ac processing tomatoes. Optimal pH (6.0-6.8) and high organic matter provide sustained nutrient release over long harvest (90-120 days). Tomatoes are HEAVY feeders (200-250 lb N, 100-150 lb P₂O₅, 300-400 lb K₂O/ac). Excellent Ca prevents blossom-end rot. Adequate B, Mg, micronutrients for fruit quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 30-40 tons/ac fresh market. Heavy supplemental fertilization required - tomatoes have high nutrient demands throughout season. Split N applications (pre-plant, flowering, fruit set) optimize uptake. High K requirement for fruit quality and disease resistance. Adequate Ca critical to prevent blossom-end rot (common problem even in good soils). Mg for fruit color. B for fruit set.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 20-30 tons/ac with intensive management. Comprehensive fertilizer program essential. Side-dress N applications during season. Ca supplementation often needed to prevent blossom-end rot despite adequate pH. Lower organic matter means less sustained N release - requires more frequent applications. Micronutrient deficiencies increasingly likely. Fruit quality variable. Drip irrigation with fertigation recommended.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility severely limits tomato production to <20 tons/ac. Tomatoes very demanding crop - one of highest vegetable nutrient requirements. Multiple nutrient deficiencies common. Blossom-end rot severe in low-Ca soils. Poor fruit quality, size, and flavor. Very intensive fertilization required but economics questionable. Consider raised beds with imported soil or intensive soil building. Other less-demanding vegetables preferable.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make field tomato production non-viable. Tomatoes among most nutrient-demanding vegetables. Extreme pH (<5.5 or >7.5) causes multiple problems - Al toxicity, micronutrient deficiencies, Ca precipitation. Multiple severe deficiencies prevent acceptable production. Not economically feasible without complete soil replacement (raised beds) or multi-year intensive soil building. Consider container production with imported growing medium instead."
    },
    
    "Potatoes": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 500+ cwt/ac (25+ tons/ac) with excellent grade and tuber quality. Slightly acid pH (5.5-6.5) preferred - reduces common scab disease. High organic matter important for sustained N release and good tilth. Potatoes are HEAVY feeders (200-300 lb N, 150-200 lb P₂O₅, 300-400 lb K₂O/ac). Adequate Ca for tuber quality, B for internal quality, Mg for photosynthesis.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 400-500 cwt/ac. Heavy supplemental fertilization required despite good native fertility. Split N applications optimize tuber development. High K requirement for specific gravity, storage quality, and chip color. Slightly acid pH (5.5-6.2) optimal - liming to neutral pH increases scab risk. Adequate micronutrients for tuber quality. S important for protein and flavor.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 300-400 cwt/ac with intensive management. Potatoes' high nutrient demands difficult to meet from moderate baseline. Comprehensive NPK program essential. Careful pH management - avoid overliming (increases scab). Organic matter amendments beneficial for tilth and water-holding. Tuber quality issues more common (hollow heart, internal defects). Micronutrient deficiencies increasingly likely.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 200-300 cwt/ac with poor grade and quality. Potatoes very demanding crop - high nutrient requirements throughout season. Multiple tuber quality defects common. Small tuber size. Poor skin finish. Growth cracks from moisture stress on low-OM soils. Not economically viable at this fertility level without major soil improvement. Consider alternative root crops or build soil over multiple years.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make potato production non-viable. Potatoes have some of highest nutrient demands among field crops. Extreme pH severely problematic - <5.0 causes Al toxicity and poor tuber formation; >7.5 causes Fe/Mn deficiency and increased scab. Multiple severe deficiencies prevent tuber development. Economic potato production impossible without complete soil rehabilitation. Not recommended."
    },
    
    "Sweet Potatoes": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility can produce 400+ bu/ac (25+ tons/ac) BUT caution - excessive N produces vegetative growth with poor root formation. Sweet potatoes have MODERATE N needs (60-80 lb N/ac) - much less than Irish potatoes. Higher K needs (100-150 lb K₂O/ac) for root quality. Slightly acid pH (5.5-6.5) optimal. High organic matter improves root shape and skin quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good conditions for 300-400 bu/ac. Moderate native fertility often OPTIMAL - excessive fertility (especially N) reduces root quality and increases vegetative growth. Balanced NPK with controlled N rates produces best root shape, size, and quality. Adequate Ca for root development. K important for root quality and storage. Sandy loam soils at this fertility level ideal.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility quite acceptable for 200-300 bu/ac. Sweet potatoes adapted to moderate fertility better than Irish potatoes. Balanced fertilization with modest N rates. Emphasis on K for root quality. Lower organic matter in sandier soils can be advantageous for root shape. This fertility level often produces excellent quality roots with proper management. Good choice for moderate-fertility situations.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 150-200 bu/ac with small roots and poor quality. Sweet potatoes more tolerant than Irish potatoes but still need reasonable fertility. Limited N availability affects vine growth and root initiation. Low K reduces root quality and storability. Fertilization required but sweet potatoes more efficient than many vegetables. Still viable with proper management - better choice than Irish potatoes at this level.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations reduce yields to <150 bu/ac with very poor quality. Even sweet potatoes' moderate requirements challenged by extreme deficiencies. Poor vine growth and root formation. Small, misshapen roots. Extreme pH (<5.0 or >7.5) problematic. Multiple deficiencies affect both tops and roots. Economic production marginal. Consider soil improvement or alternative crops. Sweet potatoes still more viable than Irish potatoes at this level."
    },
    
    "Onions": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 800+ cwt/ac with excellent bulb size, quality, and storage life. Optimal pH (6.0-7.0) and high organic matter support sustained nutrient uptake over long season (120-150 days). Onions are MODERATE feeders (100-150 lb N, 60-100 lb P₂O₅, 100-150 lb K₂O/ac) but have shallow roots requiring readily available nutrients. Adequate S (onions S-responsive, 20-30 lb S/ac improves pungency and storage).",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 600-800 cwt/ac. Moderate supplemental fertilization needed. Split N applications important - onions have limited root system and need nutrients in upper soil throughout season. Adequate S for bulb quality and storage. K important for bulb firmness and storage life. Good pH range for nutrient availability. Consistent moisture and fertility produce uniform bulbs with good storage quality.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 400-600 cwt/ac with careful management. Balanced NPK program essential. Frequent light N applications suit onions' shallow roots. S supplementation beneficial. Lower organic matter means less sustained N release. Micronutrient deficiencies possible. Bulb uniformity and size more variable. Storage quality reduced. Drip irrigation with fertigation recommended for precision nutrient management.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 300-400 cwt/ac with small bulbs and poor quality. Onions' shallow root system (8-18 inches) cannot effectively scavenge nutrients from poor soils. Multiple small bulbs rather than marketable size. Poor storage quality. Bolting problems if stressed. Very intensive fertility program required for acceptable production. Consider green bunching onions (lower requirements) or soil improvement before bulb onion production.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make bulb onion production non-viable. Onions' limited root system cannot overcome extreme deficiencies. Very small bulbs or primarily tops with poor bulbing. Multiple deficiencies affect both top and bulb development. Extreme pH problematic. Economic production not feasible. If attempting onions, consider only green bunching types with intensive fertility management or raised bed production with imported soil."
    },
    
    "Carrots": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 30+ tons/ac with excellent root shape, color, and quality. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients. CAUTION: Very high N or fresh manure causes forking, hairy roots, and excessive tops. Carrots have MODERATE nutrient needs (100-150 lb N, 60-80 lb P₂O₅, 150-200 lb K₂O/ac). Good Ca for cell structure. Adequate B for root quality (prevent cracking).",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 20-30 tons/ac with quality marketable roots. Moderate fertility often OPTIMAL for carrots - avoid excessive N which reduces root quality. Well-rotted organic matter beneficial but fresh manure causes forking. Balanced NPK with controlled N rates produces best root shape, color, and sweetness. Adequate B critical. K important for flavor and storage. Good conditions for commercial production.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for 15-20 tons/ac. Lower organic matter can be advantageous - reduces forking risk. Balanced fertilization with modest N rates. P important for root development. K for flavor and color. B supplementation often needed to prevent cracking and splitting. Some root defects more common at moderate fertility but still produces marketable crop with proper management.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 10-15 tons/ac with small roots and quality issues. Pale color, poor sweetness, and excessive fiber. Root stunting and poor shape. Multiple micronutrient deficiencies affect root development. B deficiency causes cracking. Soil improvement needed for commercial production. Consider short varieties better adapted to shallow, less fertile soils or intensive raised bed production.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make carrot production non-viable. Multiple deficiencies produce stunted, misshapen, unmarketable roots. Poor color and quality. Extreme pH problematic. Carrots need reasonable fertility despite moderate requirements - unable to overcome severe limitations. Not economically feasible without major soil improvement. Consider raised beds with imported soil mix for garden production but not viable commercially."
    },
    
    "Lettuce": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 600+ cartons/ac (25+ tons/ac fresh weight) with excellent head formation and quality. Optimal pH (6.0-7.0) and high organic matter provide sustained N release during rapid growth (60-80 days). Lettuce is HEAVY N feeder (150-200 lb N/ac) despite shallow root system. Needs readily available nutrients in upper 12 inches. Adequate Ca prevents tipburn. Good fertility supports multiple succession plantings.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 450-600 cartons/ac. Heavy N fertilization required - lettuce rapid growth and high N requirement. Split or continuous applications suit shallow roots. Adequate Ca critical - tipburn common problem even in good soils. K for crispness and shelf life. Good growing conditions for quality production. Quick growth produces tender, crisp heads.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 300-450 cartons/ac with intensive management. Lower organic matter limits sustained N availability. Frequent light N applications essential for shallow-rooted crop. Ca supplementation often needed for tipburn prevention. Head formation variable. Growth slower. Bolt risk higher if stressed. Drip irrigation with fertigation recommended. Romaine and leaf types more successful than crisphead at this level.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility severely limits lettuce to <300 cartons/ac with quality problems. Lettuce highly sensitive to poor fertility - shallow roots cannot scavenge nutrients. Small heads, poor formation, bitter taste. Tipburn common. Bolting problems. Very intensive fertility program required. Not economically viable for commercial production. Consider less demanding leafy greens (kale, chard) or intensive soil improvement. Leaf lettuce more tolerant than head types.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial lettuce production non-viable. Lettuce among most fertility-demanding vegetables due to shallow roots and rapid growth requirement. Multiple deficiencies prevent acceptable head formation. Bitter, tough leaves. Extreme pH problematic. Not economically feasible. If attempting lettuce, use raised beds with imported soil or intensive container production. Field production not viable at this level."
    },
    
    "Cabbage": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 30+ tons/ac (600+ cartons) with excellent head formation, quality, and storage life. Optimal pH (6.0-7.0) and high organic matter support sustained nutrient uptake over long season (90-120 days). Cabbage is HEAVY feeder (200-250 lb N, 100-150 lb P₂O₅, 200-250 lb K₂O/ac). Brassicas particularly responsive to B, Ca, and S. High fertility reduces disease pressure and splitting problems.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 22-30 tons/ac. Heavy supplemental fertilization required. Split N applications optimize head development. Adequate S critical (brassicas S-responsive, 20-40 lb S/ac). B essential for internal quality and head formation (0.5-1.0 lb B/ac). Adequate Ca reduces storage disorders. K for head firmness and storage. Good conditions for quality production with proper management.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 15-22 tons/ac with intensive management. Comprehensive fertilizer program essential. Multiple side-dress N applications. S supplementation important for brassicas. B deficiency increasingly likely - causes internal brown heart, hollow stem. Ca for storage quality. Lower organic matter means less sustained N. Head splitting more common if moisture/fertility inconsistent. Quality variable.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 10-15 tons/ac with quality problems. Cabbage very demanding crop - high nutrient needs throughout long season. Small heads, loose formation, poor storage. Multiple deficiencies common, especially B (causes brown heart), S (yellowing), Ca (storage disorders). Very intensive fertility program required but economics questionable. Consider less demanding brassicas (collards, kale) or soil improvement.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial cabbage production non-viable. Cabbage among most nutrient-demanding vegetables. Clubroot disease risk increased in acid soils (pH <6.0). Multiple severe deficiencies prevent head formation. Poor plant vigor. Extreme pH problematic. Not economically feasible without major soil reclamation. Consider raised bed production with imported soil or alternative crops."
    },
    
    "Broccoli": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 8+ tons/ac (300+ cartons) with excellent head size, quality, and uniform maturity. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients. Broccoli is HEAVY feeder (200-250 lb N, 100-150 lb P₂O₅, 200-250 lb K₂O/ac) with high demand during rapid head development. Brassica crop very responsive to B, S, and Mo. High fertility produces tight, dark green heads with excellent quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 6-8 tons/ac with quality heads. Heavy supplemental fertilization required. Split N applications critical - broccoli sensitive to N timing during head development. S essential for brassicas (20-30 lb S/ac). B critical for head quality (0.5-1.0 lb B/ac) - deficiency causes hollow stem, brown bead. Mo adequate at good pH for proper plant development. Uniform head maturity with proper fertility.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 4-6 tons/ac with careful management. Intensive fertilizer program essential. Multiple side-dress applications. S and B supplementation important. Lower organic matter means less sustained N during rapid head development phase. Head size smaller, maturity less uniform. Button formation (premature heading) more common under stress. Quality variable. Side-shoots may not develop well.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility severely limits broccoli production to <4 tons/ac with quality problems. Small heads, poor formation, hollow stems (B deficiency common). Yellow-green color (S and/or N deficiency). Buttoning and irregular maturity. Very intensive fertility program required. Not economically viable for commercial production. Consider less demanding brassicas (collards, kale) or intensive soil building before broccoli production.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial broccoli production non-viable. Broccoli very high nutrient demands throughout season. Multiple severe deficiencies prevent acceptable head formation. Buttoning (premature tiny heads) severe. Extreme pH (<5.5 increases clubroot risk; >7.5 causes Mo deficiency and poor head quality). Not economically feasible. Consider raised bed systems with imported soil or alternative crops."
    },
    
    "Cauliflower": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 7+ tons/ac (300+ cartons) with excellent white, tight curds. Optimal pH (6.0-7.0) and high organic matter crucial for sustained nutrient supply during critical curd development. Cauliflower is VERY HEAVY feeder (250-300 lb N, 150-200 lb P₂O₅, 250-300 lb K₂O/ac) - highest among common brassicas. CRITICAL: B for curd quality (brown curd/hollow stem if deficient), Mo for uniform development, S for plant health.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 5-7 tons/ac but requires intensive supplemental fertilization. Cauliflower most demanding common brassica. Heavy, frequent N applications essential. S critical (30-40 lb S/ac). B absolutely essential (1.0-1.5 lb B/ac) - deficiency causes brown discoloration, bitter taste, hollow stems. Mo at adequate pH for proper curd development. Uniform fertility and moisture critical - cauliflower very sensitive to stress during curd formation.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility marginal for cauliflower - most demanding common brassica crop. Expect 3-5 tons/ac with very intensive management. Comprehensive fertility program essential but difficult to meet cauliflower's extremely high requirements from moderate baseline. Multiple micronutrient deficiencies likely (B, Mo, S). Small curds, discoloration, poor quality common. Ricey (grainy) curds from stress. Consider broccoli (less demanding) instead.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes cauliflower production non-viable. Cauliflower extremely high nutrient demands cannot be economically met from poor baseline. Very small, poor-quality curds or failure to form curds. Multiple severe deficiencies. Brown curd, hollow stems, ricey texture. Not recommended - consider less demanding brassicas (broccoli, cabbage, kale) or intensive multi-year soil improvement before attempting cauliflower.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make cauliflower impossible. Cauliflower among most nutrient-demanding vegetables grown commercially. Cannot overcome extreme deficiencies even with heavy fertilization. Multiple severe nutritional disorders. Clubroot risk high if pH <6.0. Extreme pH prevents acceptable production. Absolutely not recommended at this fertility level. Not viable even in raised beds without complete soil replacement."
    },
    
    "Peppers": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 30+ tons/ac (750+ bushels) with excellent fruit size, quality, and extended harvest period (90-120 days). Optimal pH (6.0-6.8) and high organic matter provide sustained nutrient release. Peppers are HEAVY feeders (150-200 lb N, 100-150 lb P₂O₅, 250-300 lb K₂O/ac). Very high K requirement for fruit quality, size, and wall thickness. Adequate Ca prevents blossom-end rot. Mg for fruit color.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 22-30 tons/ac. Heavy supplemental fertilization required throughout long harvest. Split N applications during season. Very high K needs (peppers K-intensive) for fruit quality and disease resistance. Ca critical - blossom-end rot common problem even in good soils, especially on large-fruited bell types. Mg for chlorophyll and fruit color. B for fruit set. Good fertility supports continuous production over extended period.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 15-22 tons/ac with intensive management. Peppers' high K demands difficult to meet from moderate baseline. Comprehensive NPK program with emphasis on K essential. Ca supplementation often needed for blossom-end rot prevention. Side-dress N applications during season. Lower organic matter means less sustained nutrient release over long harvest. Fruit size and quality variable. Drip irrigation with fertigation recommended.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits production to 8-15 tons/ac with significant quality problems. Peppers demanding crop - high and sustained nutrient needs throughout season. Small fruit size. Blossom-end rot severe in low-Ca soils. Poor fruit set. Reduced wall thickness. Sunscald on exposed fruit from sparse foliage. Very intensive fertility program required but economics questionable. Consider less demanding vegetables or soil improvement.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial pepper production non-viable. Peppers' high nutrient demands, especially K and Ca, cannot be met economically. Multiple deficiencies prevent acceptable fruit production. Blossom-end rot, blossom drop, poor fruit set, small size. Extreme pH (<5.5 or >7.5) compounds problems. Not economically feasible. Consider raised bed production with imported soil or intensive multi-year soil building program."
    },
    
    "Cucumbers": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 700+ bushels/ac (20+ tons/ac) with excellent fruit quality and extended harvest (50-70 days). Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients for continuous production. Cucumbers are HEAVY feeders (150-200 lb N, 80-120 lb P₂O₅, 150-200 lb K₂O/ac). Rapid growth and continuous fruit production require readily available nutrients. Good fertility produces straight, uniformly colored fruit with extended harvest.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 500-700 bushels/ac. Heavy supplemental fertilization required for continuous production. Split N applications throughout harvest period. Adequate K for fruit quality and disease resistance. Cucumbers shallow-rooted (12-18 inches) requiring readily available nutrients. Side-dress applications during flowering and harvest periods. Good conditions support quality production with proper management.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 350-500 bushels/ac with intensive management. Balanced NPK program essential. Frequent light applications suit shallow roots. Lower organic matter means less sustained nutrient release during extended harvest. Fruit quality issues more common - misshapen, pale, bitter. Harvest period shortened. Disease pressure increases under stress. Drip irrigation with fertigation recommended for precision nutrient management.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 200-350 bushels/ac with quality problems. Cucumbers' shallow roots cannot effectively scavenge nutrients from poor soils. Small, misshapen, bitter fruit. Poor vine vigor. Short harvest period. Disease problems exacerbated by stress. Very intensive fertility program required. Not economically viable for commercial production. Consider soil improvement or alternative crops less demanding.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial cucumber production non-viable. Cucumbers' shallow root system and continuous fruiting cannot overcome extreme deficiencies. Very poor vine growth and fruit production. Multiple deficiencies. Bitter fruit. Extreme pH problematic. Not economically feasible. Consider raised bed production with imported soil for garden scale or intensive multi-year soil building before commercial production."
    },
    
    "Squash": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 800+ bushels/ac summer squash (25+ tons/ac) or 30+ tons/ac winter squash with excellent fruit quality. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients for vigorous vine growth and heavy fruit production. Squash are HEAVY feeders (150-200 lb N, 100-150 lb P₂O₅, 200-250 lb K₂O/ac). Adequate Ca, Mg, and micronutrients for fruit quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 600-800 bushels/ac summer or 22-30 tons/ac winter squash. Heavy supplemental fertilization required. Split N applications during season. High K needs for fruit quality and storage (winter squash). Adequate Ca for cell structure. Good conditions support vigorous vines and continuous production (summer types) or large fruit development (winter types). Good fertility reduces disease pressure.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 400-600 bushels/ac summer or 15-22 tons/ac winter squash with proper management. Balanced NPK program essential. Side-dress applications during rapid vine growth and fruiting. Lower organic matter limits sustained nutrient release. Fruit size smaller, quality variable. Powdery mildew and other diseases more problematic under stress. Still economically viable with intensive management.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits production to 250-400 bushels/ac summer or 10-15 tons/ac winter types. Squash demanding crops - high nutrient needs throughout season. Poor vine vigor. Small fruit size. Quality problems. Disease pressure high. Very intensive fertility program required. Marginal economics for commercial production. Consider zucchini (most tolerant summer type) or intensive soil building. Winter squash especially challenging at this level.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial squash production non-viable. Squash high nutrient demands cannot be met economically. Poor vine growth, very small fruit, numerous defects. Multiple deficiencies. Heavy disease pressure. Extreme pH problematic. Not economically feasible. If attempting squash, use raised beds with imported soil for garden production. Field production not viable without major soil reclamation."
    },
    
    "Pumpkins": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 25+ tons/ac with excellent size, color, and quality. Large-fruited cultivars (40-100 lb) respond vigorously. Optimal pH (6.0-7.0) and high organic matter support extensive vine growth (15-20 ft spread) and large fruit development (100+ days). Pumpkins HEAVY feeders (150-200 lb N, 100-150 lb P₂O₅, 200-250 lb K₂O/ac). Adequate nutrients for both massive vine system and large fruit production.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 18-25 tons/ac. Heavy supplemental fertilization required for large fruit types. Split N applications support vine growth and fruit sizing. High K needs for fruit quality, color, and storage. Adequate Ca for fruit structure. P important for fruit development. Good fertility supports uniform fruit sizing and excellent orange color. Multiple fruits per vine on large-fruited types.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 12-18 tons/ac, favor smaller-fruited cultivars (pie pumpkins, 4-8 lb) which have lower nutrient demands than jack-o-lantern types. Balanced NPK program essential. Side-dress applications during vine growth and early fruit set. Lower organic matter limits sustained nutrient release over long season. Fruit size smaller, fewer fruits per vine. Consider miniature varieties better adapted to moderate fertility.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 8-12 tons/ac with small fruit and poor quality. Pumpkins' high nutrient demands for vine and fruit development difficult to meet. Poor vine vigor, limited vine spread. Small fruit size. Poor color and shape. Limited fruits per vine. Very intensive fertility program required. Large jack-o-lantern types not economically viable. Stick with small pie pumpkins or consider alternative crops.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial pumpkin production non-viable. Pumpkins' high nutrient demands for extensive vine system and large fruit cannot be economically met. Very poor vine growth, very small or no fruit development. Multiple deficiencies prevent acceptable production. Extreme pH problematic. Not economically feasible without major soil improvement. Even miniature varieties struggle at this level."
    },
    
    "Watermelon": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 40+ tons/ac with excellent size (20-30 lb average), sweetness (12-13° Brix), and quality. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients over long season (85-100 days). Watermelons are HEAVY feeders (150-200 lb N, 80-120 lb P₂O₅, 200-300 lb K₂O/ac). Very high K requirement for sugar content and fruit quality. Adequate B, Ca for fruit development.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 30-40 tons/ac with quality fruit. Heavy supplemental fertilization required, especially K (watermelons K-intensive). Split N applications during vine growth, flowering, and fruit development. High K rates improve sugar content and flesh firmness. Adequate Ca reduces hollow heart. Good fertility supports large, sweet fruit with good shelf life. 3-4 fruits per vine typical.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 20-30 tons/ac with intensive management. Watermelons' high nutrient demands difficult to meet from moderate baseline. Comprehensive NPK program with emphasis on K essential. Lower organic matter limits sustained nutrient release over long season. Fruit size smaller (15-20 lb average), sugar content reduced (10-11° Brix). Hollow heart more common. Still marketable with proper management. Consider smaller-fruited icebox types.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 12-20 tons/ac with quality problems. Watermelons demanding crop requiring good fertility. Small fruit (8-15 lb), poor sugar content (<10° Brix), pale flesh. Thick rind, hollow heart common. Poor vine vigor. Very intensive fertility program required but economics questionable. Not recommended at this fertility level. Consider other melons (cantaloupe slightly less demanding) or soil improvement.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial watermelon production non-viable. Watermelons' high nutrient demands for extensive vine system and large fruit cannot be met economically. Very poor vine growth and fruit development. Multiple deficiencies. Very small, poor-quality fruit if any. Extreme pH problematic. Not economically feasible without major soil reclamation. Not recommended even for small-scale production at this level."
    },
    
    "Cantaloupe": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 900+ cartons/ac (25+ tons/ac) with excellent size (3-5 lb), sweetness (12-14° Brix), firm flesh, and good shelf life. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients for vigorous vine growth and quality fruit (80-90 days). Cantaloupes HEAVY feeders (100-150 lb N, 80-100 lb P₂O₅, 150-200 lb K₂O/ac). High K for sugar content and firmness.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 650-900 cartons/ac. Heavy supplemental fertilization required, especially K for sugar content and fruit quality. Split N applications during vine growth, flowering, and fruit sizing. Adequate Ca for firm flesh and shelf life. B for fruit set. Good fertility produces sweet (11-13° Brix), aromatic, firm fruit with good netting and slip characteristics. Disease resistance improved with good nutrition.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 450-650 cartons/ac with proper management. Balanced NPK program with emphasis on K essential. Lower organic matter limits sustained nutrient release. Fruit size smaller (2-3 lb), sugar content reduced (9-11° Brix). Less aromatic, softer flesh. Netting quality variable. Still marketable but shelf life reduced. Fusarium wilt pressure increases under stress. Intensive management required for acceptable quality.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 300-450 cartons/ac with quality problems. Cantaloupes have moderate to high nutrient demands. Small fruit (1-2 lb), poor sugar content (<9° Brix), soft flesh, poor shelf life. Netting poor or absent. Low aroma. Disease pressure high, especially Fusarium wilt under stress. Very intensive fertility program required. Marginal economics. Consider honeydew (slightly less demanding) or soil improvement.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial cantaloupe production non-viable. Multiple severe deficiencies prevent acceptable fruit production. Very poor vine growth, very small or no fruit. Extreme pH problematic. Fusarium wilt and other soilborne diseases severe in poor soils. Not economically feasible. Consider soil improvement or alternative crops. Even raised bed production challenging at this level."
    },
    
    "Snap Beans": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 7+ tons/ac with excellent pod quality, tenderness, and color. Optimal pH (6.0-7.0) and high organic matter support good nodulation and N₂ fixation (30-60 lb N/ac potential). Despite N-fixing ability, snap beans have MODERATE nutrient needs (50-80 lb N, 60-80 lb P₂O₅, 80-100 lb K₂O/ac). Better nodulation than common dry beans but less than soybeans. Adequate Ca, Mg, B for quality pods.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 5-7 tons/ac. Moderate fertility adequate with proper inoculation. Supplemental P and K beneficial - beans remove significant nutrients in harvested pods. Snap beans have limited N-fixing ability compared to soybeans - some starter N (30-50 lb N/ac) beneficial. Adequate pH (5.8-7.0) for nodulation. Good pod quality - tender, straight, good color. Multiple harvests on pole types.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 3-5 tons/ac with management. Snap beans more sensitive to poor fertility than dry beans or soybeans. Balanced NPK program essential. Starter N recommended - limited N-fixing capacity. If pH <6.0, lime improves nodulation. Inoculation beneficial. Pod quality variable - may be tough or curved. Color may be pale. Consider bush types (less demanding than pole types) at this fertility level.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 2-3 tons/ac with poor quality. Snap beans quite sensitive to poor soil conditions - more so than dry beans. Poor nodulation at low pH or fertility. Small, tough, poorly colored pods. Low marketable yield percentage. Very intensive fertility program required. Not economically viable for commercial production. Consider soil improvement or alternative crops. Lima beans slightly more tolerant.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make snap bean production non-viable. Snap beans moderately sensitive to soil conditions. Extreme pH and severe deficiencies prevent nodulation and acceptable growth. Very poor pod production and quality. Not economically feasible. Snap beans require reasonable fertility despite legume classification. Multi-year soil improvement required before attempting snap bean production."
    },
    
    "Peas": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 4+ tons/ac fresh weight (garden peas) with excellent pod fill and sweetness. Optimal pH (6.0-7.5) and high organic matter support excellent nodulation and N₂ fixation (60-120 lb N/ac). Despite N-fixing ability, peas benefit from good overall fertility. Cool-season crop with moderate nutrient needs (40-60 lb N, 60-80 lb P₂O₅, 80-100 lb K₂O/ac). Adequate Mo for nodulation. Good conditions produce plump, sweet pods.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 3-4 tons/ac. Moderate fertility adequate for peas. Supplemental P and K beneficial but N usually not needed due to N fixation. Peas have good nodulation capacity. Adequate pH (6.0-7.5) supports nodulation - peas somewhat lime-tolerant. Inoculation recommended if field hasn't grown peas recently. Good pod fill and quality. English peas, snap peas, and snow peas all respond well.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for 2-3 tons/ac. Peas relatively tolerant of moderate fertility - good choice for cool-season production at this level. Balanced P-K fertilization beneficial. Starter N (20-30 lb N/ac) may help if nodulation slow or soil cold. If pH <6.0, lime application improves nodulation and Mo availability. Pod quality acceptable. Consider peas over more demanding vegetables at moderate fertility.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 1-2 tons/ac. Peas more tolerant than many vegetables but still need reasonable fertility. Poor nodulation reduces N fixation. Small pods with poor fill. Quality reduced. Intensive P-K fertilization needed. Lime critical if pH <5.5. Still more viable than non-legume vegetables at this level. Austrian winter peas (field type) more tolerant than garden types.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations reduce production to <1 ton/ac with very poor quality. Even peas' moderate requirements challenged by extreme deficiencies. Poor nodulation. Small, poorly filled pods. Multiple deficiencies. Extreme pH (<5.5 or >8.0) problematic. Marginal economic viability. If using legume at this level, peas among better choices but still requires fertility improvement for acceptable production."
    },
    
    "Sweet Corn": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 250+ dozen ears/ac (excellent stand) with full kernel fill, sweetness, and quality. Optimal pH (6.0-7.0) and high organic matter provide N through mineralization. Sweet corn has HIGH nutrient demands (150-180 lb N, 80-100 lb P₂O₅, 100-150 lb K₂O/ac) similar to field corn. Natural fertility can provide 50-70 lb N/ac. Adequate Zn for early growth. Good fertility produces long ears (8-9 inches) with 16-18 rows, excellent tip fill.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 180-250 dozen ears/ac. Supplemental N-P-K essential despite good native fertility. Split N applications (pre-plant, 12 inches tall, tasseling) optimize yield and quality. Adequate Zn for early growth, especially if pH >7.0. Good ear development with proper fertilization. Good tip fill and kernel quality. Modern supersweet and sugar-enhanced varieties have high fertility requirements.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 120-180 dozen ears/ac with proper management. Lower organic matter limits N mineralization. Balanced NPK program essential. Heavy N requirement (similar to field corn) difficult to meet from moderate baseline. Ear size reduced (7-8 inches), tip fill variable. Early varieties mature more reliably than full-season types at this level. Consider standard sugary types (less demanding than supersweet).",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 80-120 dozen ears/ac with quality problems. Sweet corn's high nutrient demands difficult to meet. Small ears (6-7 inches), poor tip fill, low kernel count. Barren stalks increase. Very intensive fertilization required. Not economically viable for commercial production at typical sweet corn prices. Consider alternative vegetables less demanding or intensive soil building. Sweet corn similar demands to field corn.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make sweet corn production non-viable. Sweet corn has same high nutrient demands as field corn - among highest of vegetable crops. Multiple severe deficiencies produce stunted plants, poor ear development, mostly barren stalks. Extreme pH problematic (Fe deficiency if >8.0, Al toxicity if <5.0). Not economically feasible. Not recommended without major multi-year soil improvement program."
    },
    
    "Spinach": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 8+ tons/ac with excellent leaf quality, dark green color, and rapid growth. Optimal pH (6.0-7.5, tolerates alkaline better than most vegetables) and high organic matter provide sustained N. Spinach is HEAVY N feeder (100-150 lb N/ac) despite very shallow roots (6-12 inches). Needs readily available nutrients in upper soil. Cool-season crop with rapid growth (40-50 days) requires immediate nutrient availability. Adequate Fe for dark green color.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 6-8 tons/ac. Heavy N fertilization required - spinach rapid growth and high N requirement for leaf production. Frequent light applications suit very shallow roots. Adequate Fe (dark green color), Mn, and other micronutrients at good pH. Quick growth produces tender, flavorful leaves. Multiple succession plantings or cut-and-come-again harvests possible with good fertility.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 4-6 tons/ac with intensive management. Lower organic matter limits N availability during rapid spring growth. Very frequent light N applications essential for shallow-rooted crop. Fe deficiency possible - causes pale, yellow-green leaves. Growth slower, leaves tougher. Bolt risk higher if stressed. Still viable for production but requires intensive management. Baby leaf production more successful than large leaf at this level.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 2-4 tons/ac with quality problems. Spinach's very shallow roots (6-12 inches) cannot effectively scavenge nutrients. Small, pale, tough leaves. Bitter taste. Slow growth increases bolt risk. Numerous pest and disease problems under stress. Very intensive fertility program required. Not economically viable for commercial production. Consider less demanding leafy greens (kale, chard, collards) at this fertility level.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial spinach production non-viable. Spinach's very shallow root system and high N demands cannot overcome extreme deficiencies. Very poor leaf production and quality. Multiple deficiencies produce stunted, discolored plants. Not economically feasible. Spinach requires good fertility despite shallow roots. Consider intensive raised bed production with imported soil for garden scale only."
    },
    
    "Kale": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 20+ tons/ac fresh weight with excellent leaf quality, dark color, and extended harvest (120+ days). Optimal pH (6.0-7.5) and high organic matter provide sustained nutrients. Kale is HEAVY feeder (150-200 lb N, 80-100 lb P₂O₅, 150-200 lb K₂O/ac) due to long season and continuous leaf harvest. Brassica crop responsive to B, S, and Ca. Adequate nutrients support tender, flavorful leaves with extended production period.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 15-20 tons/ac over extended harvest. Heavy supplemental fertilization required for continuous leaf production. Split N applications throughout season. S essential for brassicas (20-30 lb S/ac). B for quality (0.5-1.0 lb B/ac). Good fertility produces tender leaves with excellent flavor. Multiple harvests over several months. Very cold-hardy - continues production into winter with good fertility.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 10-15 tons/ac with proper management. Kale MORE tolerant of moderate fertility than most brassicas (cabbage, broccoli, cauliflower). Balanced NPK program with multiple side-dress applications. S and B supplementation important. Lower organic matter means less sustained N over long season. Leaves tougher, more fibrous. Still produces acceptable crop - kale good choice for moderate fertility situations. Consider over more demanding brassicas.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 6-10 tons/ac. Kale MOST tolerant of poor conditions among common brassicas - best brassica choice at low fertility. Still requires fertilization but outperforms cabbage, broccoli, cauliflower at this level. Intensive NPK program needed. Leaves quite tough and fibrous. Pest pressure increases under stress. Consider collards (even more tolerant) or soil improvement. Kale still viable where other brassicas fail.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations reduce production to <6 tons/ac. Even kale's superior tolerance has limits. Multiple deficiencies affect growth. Extreme pH (<5.5 increases clubroot risk) problematic. Small, tough, poor-quality leaves. Among brassicas, kale and collards most likely to survive at this level but production marginal. Economic viability questionable. Consider soil improvement or non-brassica crops better adapted to extreme poverty."
    },
    
    # ========================================================================
    # FRUIT & NUT CROPS
    # ========================================================================
    
    "Apples": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous tree growth, consistent annual bearing, high-quality fruit for 30+ years. Optimal pH (6.0-7.0) and high organic matter (3-5% in orchard floor) provide sustained nutrients. Despite perennial nature, apples have MODERATE annual needs (80-120 lb N, 40-60 lb P₂O₅, 100-150 lb K₂O/ac). Adequate Ca for fruit quality/storage, B for fruit set, Mg for leaf function. CAUTION: Excessive fertility promotes fire blight and reduces fruit color.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive orchards (600-1,000 bu/ac). Moderate annual fertilization maintains tree health and productivity. Split N applications (early spring, post-bloom) optimize growth and fruit quality. Adequate Ca critical for fruit quality and storage disorders prevention. K for fruit color and firmness. Good fertility balances vegetative growth and fruiting. Soil testing and leaf analysis guide annual fertility.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 400-600 bu/ac with proper annual fertilization. Lower native fertility requires more intensive nutrient management. Annual soil testing and leaf tissue analysis essential. Balanced NPK with emphasis on Ca for fruit quality. If pH <6.0, lime improves Ca availability and reduces Al. Moderate fertility workable for apples - trees access nutrients from larger soil volume than annual crops.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits production to 250-400 bu/ac with quality issues. Young tree establishment slower. Mature tree vigor reduced. Biennial bearing tendency increases. Poor fruit size, color, and storage life. Very intensive annual fertility program required. If pH <5.5, heavy lime application essential. Not ideal for orchard establishment without multi-year soil improvement. Existing orchards require intensive management.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make new orchard establishment inadvisable. Existing trees show severe deficiency symptoms, dieback, poor fruiting. Multiple nutritional disorders. Extreme pH (<5.0 or >8.0) severely limits tree health. Young trees fail to establish. Not recommended without major soil reclamation over several years before planting. Consider other land uses or intensive site preparation."
    },
    
    "Peaches": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous trees and high yields (300-500 bu/ac) for 12-15 year orchard life. Optimal pH (6.0-6.5, slightly acid preferred) and high organic matter provide sustained nutrients. Peaches have MODERATE to HIGH annual needs (80-120 lb N, 40-80 lb P₂O₅, 100-150 lb K₂O/ac). Adequate Ca for fruit quality, B for fruit set, K for fruit size/quality. CAUTION: Excessive N promotes vegetative growth, reduces fruit quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive orchards (250-400 bu/ac). Moderate annual fertilization maintains growth/fruiting balance. Peaches prefer slightly acid soil (pH 6.0-6.5) - avoid overliming. Split N in early spring optimal. Adequate K for fruit quality and cold hardiness. Ca for firmness. Good fertility with proper management produces high-quality fruit.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for 200-300 bu/ac with proper annual fertilization. Peaches somewhat more tolerant of moderate fertility than apples - shorter-lived trees with annual renewal through pruning. Balanced NPK essential. Slightly acid pH (6.0-6.5) preferred. Annual soil testing and leaf analysis guide fertility. Tree vigor may be reduced but can still produce quality fruit. Actually preferable to very high fertility.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits production to 150-250 bu/ac with quality problems. Young tree establishment challenging. Poor tree vigor and shortened orchard life (8-10 years). Small fruit size, poor color/quality. Increased disease susceptibility. Intensive annual fertility program required. If pH <5.5, lime to 6.0-6.5. Not ideal for new orchard establishment. Consider soil improvement or alternative stone fruits.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make peach orchard establishment inadvisable. Very poor tree growth and survival. Multiple nutritional disorders. Peaches sensitive to extreme pH (<5.5 or >7.5). Young trees fail to establish properly. Existing orchards show severe decline. Not recommended without major soil reclamation. Peaches require reasonably fertile, well-drained soils."
    },
    
    "Strawberries": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports 20,000+ lb/ac with excellent berry size, quality, plant vigor. Optimal pH (5.8-6.5, slightly acid preferred) and high organic matter provide sustained nutrients. Strawberries are HEAVY feeders for shallow-rooted perennial (100-120 lb N, 60-80 lb P₂O₅, 120-150 lb K₂O/ac). Very high K for fruit quality. Adequate Ca, Mg, B. CAUTION: Excessive N promotes foliage at expense of fruit, increases disease.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for 15,000-20,000 lb/ac. Moderate supplemental fertilization for high yields/quality. Split applications during season - avoid heavy N promoting excessive vegetative growth and gray mold. High K for fruit quality, firmness, flavor. Adequate B for fruit set. Slightly acid pH (5.8-6.5) optimal. Good fertility produces large, flavorful berries with good firmness and shelf life.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 10,000-15,000 lb/ac with proper management. Strawberries' shallow roots (6-12 inches) and high K needs require careful fertility. Frequent light applications of balanced fertilizer. Emphasis on K for fruit quality. If pH <5.8, light lime beneficial but avoid overliming. Berry size smaller, quality variable. Disease pressure increases. Raised beds with plastic mulch and drip irrigation recommended.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits yields to 6,000-10,000 lb/ac with quality problems. Strawberries quite demanding for shallow-rooted crop. Poor plant vigor. Small berries. Increased disease pressure (especially if stressed). Very intensive fertility program required. Raised bed production with imported soil mix preferable at this level. Annual hill system more successful than matted row. Economics marginal.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial strawberry production non-viable. Strawberries' shallow roots and high nutrient demands cannot overcome extreme deficiencies. Very poor plant establishment and survival. Minimal fruit production. Multiple deficiencies and diseases. Not economically feasible. Raised bed systems with complete soil replacement only option. Consider soil improvement for several years."
    },
    
    "Blueberries": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100) BUT pH CRITICAL - must be ACID (4.5-5.5). High fertility at proper pH supports vigorous bush growth and high yields (12,000+ lb/ac) over 20-30 year planting life. High organic matter (>4%, often amended with pine bark/peat) essential. Blueberries have LOW to MODERATE needs (50-80 lb N, 40-60 lb P₂O₅, 60-80 lb K₂O/ac) but REQUIRE acid conditions. Adequate Fe, Mn (available at low pH). NH₄-N form preferred. CAUTION: pH >5.5 causes severe Fe chlorosis.",
        
        "High": "Good nutrient availability (SQ1: 60-84) IF pH 4.5-5.5. Good baseline for 8,000-12,000 lb/ac. Moderate fertility adequate with proper pH management. Acidifying fertilizers (ammonium sulfate) maintain pH and provide N. Avoid nitrate-N forms. Adequate organic matter (amended with pine bark mulch) critical for moisture/nutrient management of shallow fibrous roots. Fe, Mn adequate at proper acid pH. Sulfur applications maintain pH if naturally neutral/alkaline.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59) IF pH 4.5-5.5. Moderate fertility supports 6,000-8,000 lb/ac with intensive pH and fertility management. Challenge is maintaining proper acid conditions - if native pH >6.0, intensive sulfur applications required (may take 2-3 years to acidify). Heavy organic matter amendments (pine bark, peat) beneficial. Use only acidifying fertilizers. If native pH >7.0, raised beds with acid soil mix preferable.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility and especially wrong pH make blueberries very challenging. Yields <6,000 lb/ac. If native pH >6.5, acidification extremely difficult and expensive - not recommended. Even at proper pH, poor fertility limits growth. Blueberries somewhat tolerant of low fertility but cannot tolerate high pH (>5.5). If pH naturally acid (4.5-5.5), blueberries viable with fertility amendments. If pH >6.5, not recommended.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations complicated by pH requirements make blueberries inadvisable. If extreme pH >7.0 (alkaline), blueberries completely unsuitable - Fe chlorosis severe even with acidification attempts. If extreme pH <4.5 (very acid), Al toxicity possible but manageable with lime to 4.5-5.0. Multiple deficiencies at any pH. Not recommended without complete site preparation including raised beds with imported acid soil mix."
    },
    
    "Grapes": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous vine growth and high yields (8-12 tons/ac wine grapes, 15+ tons/ac table grapes) over 25-30+ year vineyard life. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients. CAUTION: Excessive fertility, especially N, promotes vegetative growth, delays maturity, reduces wine quality. Grapes have LOW to MODERATE needs (40-80 lb N, 30-50 lb P₂O₅, 80-120 lb K₂O/ac). High K for fruit quality. For wine grapes, moderate fertility often OPTIMAL.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for quality wine production (5-8 tons/ac) or productive table grape production (12-15 tons/ac). Moderate fertility often IDEAL for wine grapes - balances vine vigor and fruit quality. Light annual N applications maintain vine health without excessive vigor. High K for fruit quality, color, sugar. Adequate B for fruit set, Mg for photosynthesis. Good fertility with restrained management produces excellent wine quality.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for wine grapes (4-6 tons/ac) or table grapes (8-12 tons/ac) with proper annual fertilization. Grapes relatively TOLERANT of moderate fertility - deep roots access nutrients from large soil volume. Balanced NPK with emphasis on K. If pH <5.5, lime to 6.0-6.5. Vines may show stress symptoms but often produce excellent wine quality - moderate vigor desirable. Table grapes require more intensive fertility.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits production to 2-4 tons/ac wine or 5-8 tons/ac table grapes with quality issues. Young vine establishment slower. Mature vine vigor reduced. Small berry size. Poor yield consistency. Wine quality may be acceptable if vines healthy - low vigor sometimes enhances concentration. Table grape production challenging - fruit size and appearance suffer. Intensive fertility program required. Consider wine varieties over table types.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make new vineyard establishment inadvisable without major soil improvement. Very poor vine growth and survival. Multiple nutritional disorders. Grapes relatively tolerant but cannot overcome extreme deficiencies. Extreme pH (<5.0 or >8.5) severely problematic. Young vines fail to establish. Not recommended for viticulture without multi-year soil building including deep tillage, lime/sulfur, organic matter incorporation."
    },
    
    "Almonds": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous tree growth and high yields (3,000+ lb/ac) over 25+ year orchard life. Optimal pH (6.0-7.5, tolerates slight alkalinity) and high organic matter provide sustained nutrients. Almonds have MODERATE to HIGH annual needs (200-300 lb N, 50-80 lb P₂O₅, 200-300 lb K₂O/ac) - among highest of tree nuts. Very high N and K demands for heavy nut loads. Adequate B for pollination/nut set, Zn for tree health, Ca for nut quality.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive orchards (2,200-3,000 lb/ac). Heavy annual fertilization required despite good native fertility - almonds very demanding. Split N applications (early spring, post-harvest) optimize tree response. Very high K requirement for nut quality and tree health. Adequate B critical for pollination (1-2 lb B/ac). Zn for shoot growth. Almonds relatively alkaline-tolerant (pH to 8.0) but Fe chlorosis risk increases above 7.5.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 1,500-2,200 lb/ac with very intensive annual fertilization. Almonds' extremely high nutrient demands difficult to meet economically from moderate baseline. Comprehensive NPK with high application rates essential. Young tree establishment slower. Hull rot risk increases under nutrient stress. Leaf analysis and soil testing guide intensive programs. Marginal economic viability - input costs high. Consider economics carefully before establishing orchard.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes almond production economically unviable. Yields <1,500 lb/ac with high input costs. Almonds among most nutrient-demanding tree crops - cannot achieve commercial yields from poor baseline despite intensive fertilization. Young trees fail to establish properly. Mature trees show severe deficiency symptoms and dieback. Multiple nut quality problems. Not recommended for new orchard establishment. Existing orchards require extraordinary management.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make almond production completely inadvisable. Almonds very high nutrient demands cannot be met economically. Extreme pH problematic. Multiple severe deficiencies prevent tree establishment and survival. Not suitable for almond production under any circumstances without complete site rehabilitation over many years - not economically feasible. Consider entirely different land uses."
    },
    
    "Walnuts": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous tree growth and high yields (3,000-4,000 lb in-shell/ac) over 50+ year orchard life. Optimal pH (6.0-7.5) and high organic matter provide sustained nutrients. Walnuts have HIGH annual needs (200-250 lb N, 40-60 lb P₂O₅, 150-200 lb K₂O/ac). Very high N demands for large trees and heavy nut production. Adequate Zn critical (walnuts very Zn-responsive), B for pollination, K for nut quality. Deep rooting allows access to nutrients throughout profile.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive orchards (2,500-3,500 lb/ac). Heavy annual fertilization required for these large, long-lived trees. Split N applications (early spring, summer) meet high seasonal demands. Very high Zn requirement - annual applications essential. Adequate K for nut quality and storage. B for pollination and nut fill. Deep rooting (12-20 ft) accesses subsoil nutrients but topsoil fertility still critical.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility marginal for commercial walnut production. Expect 1,800-2,500 lb/ac with very intensive management. Walnuts' extremely high nutrient demands and very long production life (50+ years) require excellent native fertility. Young tree establishment (10-15 years to bearing) demands sustained fertility. Comprehensive annual fertility with high rates essential. Zn deficiency very common - annual applications required. Economics questionable - decades of high input costs.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes walnut orchards economically unviable. Walnuts among most nutrient-demanding tree crops with longest production cycle. Young trees fail to develop properly - may take 20+ years to reach bearing instead of 10-12. Mature production <1,800 lb/ac. Multiple severe deficiencies. Hull rot, kernel quality problems. Not recommended for new orchard establishment under any circumstances. Not economically feasible. Consider alternative crops or different land use.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make walnut production completely inadvisable. Walnuts require excellent soils for 50+ year productive life. Cannot establish or maintain trees at this fertility level. Extreme pH, multiple severe deficiencies prevent survival. Absolutely not suitable for walnuts. Multi-decade investment requires excellent soil resources from start - soil improvement for walnuts not economically feasible given extremely long production cycle. Choose different land use."
    },
    
    "Pecans": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous tree growth and high yields (2,000+ lb in-shell/ac) over 75+ year orchard life. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients. Pecans have VERY HIGH annual needs (200-300 lb N, 50-80 lb P₂O₅, 150-250 lb K₂O/ac) for massive trees. Very high Zn requirement (pecans extremely Zn-responsive, 3-5 lb Zn/ac annually). Adequate Ni for nut fill (unique requirement). Deep rooting (15-20+ ft) requires fertility throughout profile.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive orchards (1,500-2,000 lb/ac). Very heavy annual fertilization required for these massive, long-lived trees. Multiple split N applications during season meet high demands. Zinc critical - pecans most Zn-responsive of tree crops, annual applications (foliar and soil) essential. Nickel for nut fill (foliar sprays). K for nut quality. Adequate B, Mg for tree health. Intensive management essential for commercial production of high-quality nuts.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility marginal to unsuitable for commercial pecan production. Pecans have among highest nutrient demands of any tree crop and longest production life (75+ years). Young tree development very slow at moderate fertility - may never reach full production potential. Yields <1,500 lb/ac. Zn deficiency severe and persistent. Multiple nut quality problems (poor fill, low kernel percentage). Economics poor - not recommended for new orchard establishment.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes pecan production economically impossible. Pecans THE most nutrient-demanding common tree nut crop. Cannot establish viable orchard - young trees severely stunted, may never bear nuts. Multiple severe deficiencies (especially Zn - rosette disease universal). Not recommended under any circumstances. Pecans require excellent, deep, fertile soils for multi-generational production. Not economically feasible to build soil for pecan production given extremely long payback period.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make pecan production completely impossible. Pecans require the highest quality soils for 75-100+ year productive life. Extreme pH and multiple severe deficiencies prevent even survival. Absolutely unsuitable - among the most soil-demanding crops in temperate agriculture. Multi-generational investment (orchards often passed through families) requires exceptional soil resources. Soil improvement for pecans not remotely economically feasible. Do not attempt pecan production."
    },
    
    # ========================================================================
    # SPECIALTY CROPS
    # ========================================================================
    
    "Hops": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous bine growth (18-20 ft) and high yields (2,500+ lb/ac) over 20+ year yard life. Optimal pH (6.0-7.0) and high organic matter provide sustained nutrients. Hops are VERY HEAVY feeders (200-250 lb N, 100-150 lb P₂O₅, 200-300 lb K₂O/ac). Extreme N demands for massive annual vegetative growth from perennial crown. Very high K for cone quality and alpha acid content. Adequate S for aroma compounds, Mg for photosynthesis.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive yards (1,800-2,500 lb/ac). Very heavy annual fertilization required. Split N applications (spring growth, pre-flowering, cone development) match uptake pattern. Very high K for cone quality and alpha acid levels. S for aromatic oils. Adequate micronutrients for vigorous growth. Intensive nutrient management essential for quality hop production. Leaf analysis at key growth stages guides fertility programs for premium brewing quality.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports 1,200-1,800 lb/ac with very intensive management. Hops' extremely high nutrient demands for massive annual growth difficult to meet from moderate baseline. Comprehensive fertility with high N and K rates essential. Cone quality and alpha acid content suffer at lower fertility - premium brewing market requirements difficult to meet. Reduced bine vigor affects yield. Economics questionable for premium hop production. Consider alternative crops.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes commercial hop production economically unviable. Yields <1,200 lb/ac with poor cone quality. Hops among most nutrient-demanding specialty crops. Weak bine growth, poor cone development, low alpha acids. Multiple deficiencies. Premium brewing market requirements cannot be met. Very high production costs relative to poor baseline. Not recommended for hop yard establishment. Existing yards require extraordinary management with questionable profitability.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make hop production impossible. Hops' extreme nutrient demands (similar to heavy-feeding vegetables but perennial) cannot be met. Poor crown establishment and survival. Minimal growth. No commercial cone production. Not suitable for hops under any circumstances. Multi-year investment in perennial crop requires excellent soil resources from start. Consider different land use - soil building for hops not economically feasible."
    },
    
    "Hemp": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports: Fiber hemp (8-10 tons/ac dry matter, 10+ ft height), Grain hemp (1,500+ lb/ac seed), CBD hemp (1,500+ lb/ac floral material). Optimal pH (6.0-7.5) and high organic matter provide nutrients. Hemp has MODERATE to HIGH needs depending on type: Fiber (100-150 lb N/ac), Grain (80-120 lb N/ac), CBD (120-180 lb N/ac). Fast-growing crop scavenges nutrients efficiently. All types respond vigorously to good fertility.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for productive hemp: Fiber (6-8 tons/ac), Grain (1,200-1,500 lb/ac), CBD (1,200-1,500 lb/ac). Supplemental fertilization needed for maximum yields. Hemp relatively efficient nutrient user - deep tap root accesses nutrients effectively. Balanced NPK program. Fiber hemp highest N demand, CBD intermediate, grain lowest. Adequate micronutrients for all types. Good fertility produces quality product meeting market specifications.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility supports: Fiber (4-6 tons/ac), Grain (800-1,200 lb/ac), CBD (800-1,200 lb/ac) with proper fertilization. Hemp's reputation for thriving on marginal land somewhat overstated - commercial production requires reasonable fertility. Balanced NPK essential. Grain hemp most tolerant of moderate fertility, CBD intermediate, fiber most demanding. Hemp still better choice than many crops at this level due to efficient nutrient uptake.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits: Fiber (<4 tons/ac), Grain (<800 lb/ac), CBD (<800 lb/ac). Hemp somewhat tolerant of lower fertility compared to many crops but quality and yields suffer significantly. Stunted growth, reduced fiber length (fiber type), low seed yields (grain), reduced cannabinoid levels (CBD). Historic use on marginal land was for low-value fiber, not modern high-value products. Intensive fertility required for economically viable production. Consider grain type (most tolerant).",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial hemp production non-viable. Even hemp's tolerance has limits. Multiple deficiencies produce stunted plants with poor quality. Modern hemp production (fiber, grain, CBD) requires reasonable fertility for economic returns. While hemp grown historically on poor land, this was subsistence production of low-quality fiber - not viable for modern markets requiring quality standards. Not recommended without major soil improvement."
    },
    
    "Herbs (General)": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous growth and high essential oil yields. Optimal pH (varies by species: 6.0-7.5 most herbs) and high organic matter beneficial. CAUTION: Many herbs (basil, rosemary, lavender, thyme, oregano) produce BEST flavor and essential oils at MODERATE fertility - excessive N reduces oil concentration and alters flavor profiles. High fertility most beneficial for leafy herbs (parsley, cilantro, chives) grown for foliage not oils.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline often OPTIMAL for many culinary herbs. Moderate fertility produces best essential oil concentration and flavor intensity for: basil, oregano, thyme, rosemary, sage, lavender. Higher fertility better for leafy types: parsley, cilantro, chives, dill. Most herbs have LOW to MODERATE needs (50-100 lb N, 30-60 lb P₂O₅, 60-100 lb K₂O/ac depending on species). Balanced nutrition without excess N produces premium quality. This fertility level ideal for aromatic herbs.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable to preferred for many herbs, especially Mediterranean types adapted to lower fertility soils. Lavender, thyme, oregano, rosemary, sage all thrive at moderate fertility - often produce more concentrated oils than at higher fertility. Leafy herbs (parsley, cilantro, basil) benefit from supplemental fertilization. Balanced, modest fertility programs. Many herbs actually BEST at this fertility level - Mediterranean climate species evolved on thin, moderate-fertility soils.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits most culinary herbs though some Mediterranean types tolerate low fertility reasonably well. Thyme, oregano, lavender survive but yields low. Leafy types (parsley, cilantro, basil) struggle significantly. Small plant size, reduced yields, lower oil content. Most herb production not economically viable. However, Mediterranean herbs still among better choices for low fertility compared to vegetables. Consider native species better adapted to poor soils.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make most herb production non-viable. Even drought and low-fertility tolerant Mediterranean herbs severely limited. Minimal growth, poor quality, negligible oil content. Not economically feasible for commercial herb production. Small-scale garden production possible for most tolerant types (thyme, oregano) with intensive management and amendments, but not viable commercially. Consider soil improvement or alternative land uses."
    },
    
    "Flowers (Cut)": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports vigorous plant growth, long stems, large blooms, and brilliant colors. Optimal pH (6.0-7.0 for most species) and high organic matter provide sustained nutrients. Cut flowers have MODERATE to HIGH needs varying by species: 100-200 lb N, 60-120 lb P₂O₅, 100-200 lb K₂O/ac. High fertility produces premium quality stems meeting exacting market standards for length, stem strength, bloom size, color intensity, and vase life.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for quality cut flower production. Most species respond well to supplemental fertilization. Balanced NPK program tailored to specific crops. High-value flowers justify intensive fertility management. Adequate micronutrients for color intensity and post-harvest quality. Split applications during season maintain nutrition for continuous production. Good fertility supports multiple cuts from perennial types and successive plantings of annuals. Premium quality flowers for wholesale markets achievable.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for many cut flowers with proper management. Some species (zinnias, sunflowers, cosmos) relatively tolerant of moderate fertility. Others (roses, lisianthus, peonies) require intensive supplementation. Balanced fertility program essential. Stem length, bloom size, and color intensity may be reduced. Select species appropriate for fertility level - avoid most demanding types (roses, calla lilies, specialty bulbs). Still viable for commercial production of adapted species.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility severely limits cut flower production. Short stems, small blooms, poor colors fail to meet market standards. Most commercial cut flowers have moderate to high nutrient demands for quality production. Very intensive fertility program required but economics questionable. Only most tolerant species (sunflowers, zinnias, some wildflowers) viable. Premium flowers (roses, peonies, lisianthus) not economically feasible. Consider less demanding alternative crops or soil improvement.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make commercial cut flower production non-viable. Multiple deficiencies prevent acceptable stem and bloom quality. Cut flowers high-value crops justifying high inputs, but extreme soil poverty makes economic production impossible. Even tolerant species produce unmarketable quality. Not recommended for cut flower production. Consider intensive raised bed production with imported soil for small-scale only, or focus on soil improvement for several years."
    },
    
    "Christmas Trees": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports rapid growth, excellent form, and dark green color over 6-10 year production cycle. Optimal pH (5.5-6.5 for most species) and high organic matter provide sustained nutrients. Christmas trees have LOW to MODERATE annual needs (50-80 lb N, 30-50 lb P₂O₅, 40-60 lb K₂O/ac) but CUMULATIVE needs over many years. Adequate Mg for needle color, B for terminal bud development. CAUTION: Excessive N can promote rapid growth with poor form and weak branches.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for quality tree production. Moderate annual fertilization maintains good growth rate and color. Most conifers prefer slightly acid soil (pH 5.5-6.5). Balanced NPK with moderate N rates promotes good form without excessive growth. Adequate micronutrients for dark green needle color. Different species have varying tolerances: Spruce relatively demanding, Fir intermediate, Pine most tolerant. Good fertility produces marketable 6-7 ft trees in optimal time frame.",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for most Christmas tree species with proper management. Conifers generally LOW fertility demand compared to agricultural crops. Modest annual fertilization adequate. Growth rate may be slower - production cycle extends 1-2 years. Tree form and color acceptable with proper shearing and management. Select species suited to moderate fertility: Pines most tolerant, Spruce most demanding, Fir intermediate. Scotch Pine, Virginia Pine, White Pine excellent choices.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility limits tree quality and extends production cycle significantly. Slow growth (may require 10-12 years for marketable size), poor color (yellow-green needles from N deficiency), sparse branching. Most Christmas tree species relatively tolerant of lower fertility but quality and economics suffer. Annual fertilization essential. Select most tolerant species (Virginia Pine, Scotch Pine, White Pine) and least demanding (avoid Blue Spruce, Fraser Fir). Consider multi-year soil building.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make Christmas tree production economically unviable. Very slow growth, poor survival, unacceptable quality. Multiple nutritional disorders. Extreme pH problematic for most species. Production cycle extends beyond acceptable timeframe (15+ years for 6 ft tree). Not economically feasible - carrying costs exceed returns. While conifers relatively low fertility demand, extreme deficiencies still prevent acceptable production. Consider alternative forestry use or intensive soil improvement."
    },
    
    "Nursery Stock": {
        "Very High": "Excellent nutrient availability (SQ1: 85-100). High fertility supports rapid growth of diverse ornamental species for 1-3 year production cycles. Optimal pH (6.0-7.0 for most species, some acid-lovers need pH 5.0-6.0) and high organic matter provide sustained nutrients. Nursery stock has MODERATE to HIGH needs varying widely by species: 100-200 lb N, 60-100 lb P₂O₅, 100-150 lb K₂O/ac. High fertility produces quality plants meeting specification for size, form, and vigor in shortest time frame - critical for economic production.",
        
        "High": "Good nutrient availability (SQ1: 60-84). Good baseline for quality field-grown nursery stock. Supplemental fertilization tailored to specific crops. Most ornamentals respond well to balanced fertility. Adequate nutrients produce well-rooted, vigorous plants ready for landscape installation. Different species have varying requirements - select species suited to soil conditions or adjust fertility accordingly. Good fertility produces marketable plants in standard production timeframe (1-3 years depending on species and size).",
        
        "Medium": "Adequate nutrient availability (SQ1: 40-59). Moderate fertility acceptable for field production of adapted species with intensive management. Many natives and less demanding ornamentals acceptable at this level. Intensive species (roses, some perennials) require heavy supplementation or better grown in containers. Balanced fertility program essential. Production time may extend for some species. Select species appropriate for fertility level - focus on adapted natives and less demanding cultivars. Container production often preferable to field.",
        
        "Low": "Below-average nutrient availability (SQ1: 20-39). Poor fertility makes field production of most ornamental nursery stock economically unviable. Very slow growth, poor quality, extended production times unacceptable for commercial nursery. Only most tolerant native species viable in field. Container production strongly recommended over field production at this level - allows complete control of growing media and fertility. If field growing, focus exclusively on adapted native species tolerant of low fertility. Premium ornamentals require container production.",
        
        "Very Low": "Poor nutrient availability (SQ1: 0-19). Severe limitations make field nursery production impossible. Multiple deficiencies prevent acceptable plant growth. Commercial nursery production requires container growing with imported media - field production not viable. While some native species survive poor soils in natural settings, commercial nursery quality and timeframe not achievable. Use site for different purpose or implement container growing systems exclusively. Field production not recommended under any circumstances."
    }
}


def get_sq1_interpretation(crop: str, rating: str) -> str:
    """
    Get the enhanced interpretation for a specific crop and SQ1 rating.
    
    Parameters:
    -----------
    crop : str
        The name of the crop (must match keys in SQ1_INTERPRETATIONS)
    rating : str
        The SQ1 rating (Very High, High, Medium, Low, or Very Low)
    
    Returns:
    --------
    str
        The interpretation text for the specified crop and rating
    
    Raises:
    -------
    KeyError
        If the crop or rating is not found in the lookup table
    """
    if crop not in SQ1_INTERPRETATIONS:
        available_crops = ", ".join(sorted(SQ1_INTERPRETATIONS.keys()))
        raise KeyError(f"Crop '{crop}' not found. Available crops: {available_crops}")
    
    if rating not in SQ1_INTERPRETATIONS[crop]:
        available_ratings = ", ".join(SQ1_INTERPRETATIONS[crop].keys())
        raise KeyError(f"Rating '{rating}' not found for crop '{crop}'. Available ratings: {available_ratings}")
    
    return SQ1_INTERPRETATIONS[crop][rating]


def get_all_crops() -> list:
    """
    Get a list of all available crops in the interpretation table.
    
    Returns:
    --------
    list
        Sorted list of all crop names
    """
    return sorted(SQ1_INTERPRETATIONS.keys())


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
    interpretation = get_sq1_interpretation(crop_name, rating_value)
    print(f"\n{crop_name} - {rating_value} SQ1 Rating:")
    print(interpretation)
    print("\n" + "="*80)
    
    # Show all available crops
    print(f"\nTotal crops in database: {len(get_all_crops())}")
    print("\nAll 53 crops with enhanced interpretations:")
    for i, crop in enumerate(get_all_crops(), 1):
        print(f"{i:2d}. {crop}")
    
    print("\n" + "="*80)
    print("Enhanced features include:")
    print("  • Specific SQ1 score ranges (e.g., 85-100, 60-84, etc.)")
    print("  • Detailed nutrient requirements (N-P-K rates in lb/ac)")
    print("  • Expected yield ranges for each fertility level")
    print("  • pH preferences and organic matter targets")
    print("  • Critical nutrient deficiency warnings")
    print("  • Economic viability assessments")
    print("  • Comparative crop recommendations")
    print("  • Management-specific guidance")
