"""
SQ4 (Oxygen Availability to Roots) Enhanced Interpretations - FIELD CROPS
Based on FAO GAEZ Methodology

SQ4 evaluates soil drainage conditions and oxygen availability:
- Drainage class (excessively drained to very poorly drained)
- Water table depth and duration
- Redoximorphic features (mottling, gleying)
- Flooding/ponding frequency and duration
- Soil permeability and aeration

RATING SCALE:
- Very High (80-100): Excellent oxygen availability, no limitations
- High (60-79): Good oxygen availability, minor limitations
- Medium (40-59): Moderate oxygen availability, significant limitations
- Low (20-39): Poor oxygen availability, severe limitations
- Very Low (0-19): Very poor oxygen availability, extreme limitations
"""

SQ4_INTERPRETATIONS = {
    # ========================================================================
    # FIELD CROPS
    # ========================================================================
    
    "Corn": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well to moderately well drained soils with deep water table (>100 cm). No saturation in root zone during growing season. Optimal for corn's extensive root system (5-6 ft depth). No yield reduction from poor drainage. Field operations unrestricted. Planting and harvest on schedule. Excellent germination and early vigor. Root development unrestricted. Maximum nutrient uptake efficiency. Can achieve 150+ bu/ac potential in combination with adequate fertility.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained soils. Brief seasonal saturation possible in lower subsoil (50-100 cm depth). Minor limitations for corn. Occasional field operation delays during wet periods. Slight reduction in effective rooting depth. May see minor yield reduction (5-10%) in very wet years. Generally suitable for full-season hybrids. Good germination with proper timing. Root diseases minimal. Yields of 120-150 bu/ac achievable with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained soils with seasonal water table 30-90 cm. Significant limitations for corn production. Frequent planting delays - narrow planting window. Stand establishment problems in wet springs. Root system restricted - may only penetrate 2-3 ft effectively. Yield reductions of 20-40% common. Root rots and seedling diseases increase. Consider shorter-season hybrids to avoid wet fall harvest. Surface drainage improvements beneficial. Still viable but management-intensive.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained soils with water table 0-50 cm much of growing season. Severe limitations for corn. Very difficult to establish stands - often requires multiple plantings. Shallow root systems (<2 ft) limit nutrient/water uptake even when surface appears dry. Yield reductions of 50-75%. Seedling death common. Root rots severe. Field operations extremely limited. Corn not recommended without drainage installation. Consider grain sorghum (more tolerant) or alternative crops. Economics poor even with drainage.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained with water table at/near surface most of year. Extreme limitations make corn production impossible. Cannot achieve stands. Complete crop failures common. Anaerobic conditions throughout root zone. Corn absolutely requires well-aerated soils. Not suitable for corn under any circumstances without major drainage improvements. Even with drainage, other limitations likely remain. Consider rice (adapted to flooding) or permanent wetland uses."
    },
    
    "Soybeans": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained soils ideal for soybean production. Deep water table ensures good aeration for nodulation. Optimal conditions for N-fixation - rhizobia require oxygen. Root system develops to 4-5 ft depth accessing deep moisture. No waterlogging stress. Excellent stand establishment. Early-season vigor strong. Yields of 60+ bu/ac possible. Field operations unrestricted. No drainage-related diseases. Maximum benefit from biological N fixation (150-200 lb N/ac potential).",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained soils suitable for soybeans. Brief saturation deep in profile acceptable. Minor limitations. Nodulation generally good though may be slightly reduced during saturated periods. Effective rooting depth 3-4 ft. Occasional field delays during wet weather. Yields 50-60 bu/ac achievable. Root rots minimal if proper variety selection. Some yield loss (5-15%) in extremely wet years. Generally excellent for soybean production with minor management adjustments.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained soils present challenges for soybeans. Significant limitations due to reduced nodulation efficiency in saturated conditions. N-fixation severely compromised during wet periods - soybeans essentially non-nodulating crop under prolonged saturation. Shallow rooting (2-3 ft) limits access to deep moisture during dry periods. Yield reductions 25-45%. Planting delays common. Phytophthora root rot and other water-related diseases increase dramatically. Consider tolerant varieties. Surface drainage essential. Economics marginal.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained soils severely limit soybean production. N-fixation essentially fails - nodules absent or non-functional. Plants dependent on soil/fertilizer N but root system too restricted to acquire it. Yields <30 bu/ac even in good years, often <20 bu/ac. Complete failures in wet years. Severe root rots. Stand establishment very difficult. Soybeans not recommended without extensive drainage. Even with drainage, yield potential severely limited. Consider crops adapted to poor drainage or alternative land uses.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained soils completely unsuitable for soybeans. Cannot establish viable stands. No nodulation or N-fixation under anaerobic conditions. Legumes particularly sensitive to waterlogging - require aerobic conditions for symbiotic relationship. Complete crop failures. Not economically viable under any management. Drainage installation may not be sufficient given other limitations. Consider rice or wetland restoration rather than conventional field crops."
    },
    
    "Winter Wheat": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained soils optimal for winter wheat. Good fall establishment with unrestricted root development (4-5 ft potential). Excellent tillering (30+ tillers/plant possible). No winterkill from ice sheeting or saturated soil freezing. Strong spring green-up. No delays in field operations. Good air-soil exchange prevents anaerobic conditions. Yields of 80+ bu/ac possible. Disease pressure minimal. Good straw strength. Test weights typically high.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable for winter wheat. Minor limitations. Fall planting window adequate though occasionally delayed. Good fall establishment (20-30 tillers/plant). Winter survival generally good - brief saturation events not problematic if soil freezes drained. Effective rooting depth 3-4 ft. Spring operations occasionally delayed. Yields 60-80 bu/ac achievable. Some increase in root diseases in wet years. Overall very suitable for winter wheat production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained soils challenge winter wheat. Significant limitations especially for fall establishment. Fall planting often delayed - may miss optimal window. Poor root development before winter (10-20 tillers/plant). Winterkill risk increases - ice sheeting and crown rot more common in saturated soils. Weak spring growth. Spring operations frequently delayed affecting topdress timing. Yields 40-60 bu/ac. Root and crown diseases increase. Consider spring wheat to avoid fall/winter issues.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained soils severely limit winter wheat. Very difficult fall establishment. Thin stands (<10 tillers/plant) with poor vigor. High winterkill rates - saturated frozen soils cause crown suffocation and ice damage. Those that survive show weak spring growth. Severe disease pressure (especially take-all, Pythium). Yields <40 bu/ac when crop survives. Frequent complete failures. Winter wheat not recommended. Spring wheat or spring-planted small grains better options if drainage improved.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained soils completely unsuitable for winter wheat. Cannot establish fall stands - seeds rot or seedlings die. Extreme winterkill if any plants establish. Anaerobic soil conditions during dormancy period lethal. Not economically viable. Winter wheat requires well-drained soils for survival. Even with drainage, other limitations prevent successful production. Consider completely different crops adapted to wet conditions."
    },
    
    "Spring Wheat": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained soils ideal for spring wheat. Early planting possible - critical for yield in short growing season. Rapid germination and emergence. Strong early vigor allows quick canopy closure. Deep rooting (3-4 ft) accesses moisture. No field operation restrictions. Yields of 60+ bu/ac possible. Minimal disease pressure from drainage issues. Good test weights and protein content. Harvest timing flexible.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for spring wheat. Minor planting delays possible in wet springs. Generally good germination and early growth. Effective rooting depth adequate (2-3 ft). Occasional field operation delays. Yields 50-60 bu/ac achievable. Some increase in root diseases in wet conditions but generally manageable. Overall very good for spring wheat - fewer overwinter drainage issues compared to winter wheat.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained soils present challenges. Significant planting delays common - may miss optimal early planting window. This is critical for spring wheat yield potential. Slow emergence and poor early vigor. Shallow rooting limits drought tolerance later in season. Yields 35-50 bu/ac. Root rots increase. Harvest delays in wet years reduce quality. Consider early-maturing varieties. Surface drainage improvements beneficial. Still viable but challenging.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained soils severely limit spring wheat. Late planting (if field ever dry enough) drastically reduces yield potential. Poor stands and weak plants. Very shallow rooting. Yields <35 bu/ac. Severe root diseases. Often cannot harvest until late summer due to wet fields. Quality suffers. Spring wheat not recommended. Consider barley or oats which tolerate poor drainage better, or install drainage before attempting cereals.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Field never dry enough for spring planting during optimal window. If planted late, yields negligible (<20 bu/ac). Complete failures common. Harvest impossible due to wet conditions. Not economically viable. Small grains require reasonable drainage for economic production. Consider crops adapted to wet conditions or alternative land uses."
    },
    
    "Cotton": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained soils essential for cotton production. Cotton extremely sensitive to waterlogging - requires excellent aeration. Deep tap root (5-8 ft potential) develops fully. Optimal conditions for 2+ bales/ac production. No planting delays. Critical germination period protected. No seedling diseases from poor drainage. Strong vegetative growth. Flowering and boll set uninterrupted. No harvest delays - critical for quality. Fiber quality excellent. Full potential achievable.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with caution. Minor limitations. Brief saturation events tolerable if not during critical growth stages. Occasional field operation delays. Slight root restriction in lower profile. Yields 1.5-2 bales/ac possible. Some increase in seedling diseases if wet during germination. Cotton relatively sensitive - even brief waterlogging can cause square/boll shedding. Monitor closely during wet periods. Generally suitable but requires careful management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained soils very challenging for cotton. Cotton one of more waterlogging-sensitive field crops. Significant stand establishment problems. Weak plants susceptible to seedling blights. Restricted rooting severely limits water/nutrient uptake. Heavy square and boll shedding during saturated periods. Yields 1-1.5 bales/ac at best. Maturity delayed affecting harvest timing and quality. Fiber quality reduced. Economics poor. Cotton not recommended without drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained soils completely unsuitable for cotton. Cotton requires well-drained soils - cannot tolerate prolonged saturation. Severe stand losses. Surviving plants stunted with minimal fruiting. Heavy square and boll shedding. Yields <1 bale/ac if any harvestable crop. Severe disease pressure. Cotton production not viable. Even with drainage, yield potential too limited for economic production. Consider alternative crops adapted to poor drainage.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Cotton among most drainage-sensitive major field crops. Cannot establish stands. Complete failures universal. Deep tap root system requires well-aerated profile throughout depth. Anaerobic conditions lethal. Not economically viable under any circumstances. Do not attempt cotton production. Consider crops adapted to wet conditions or alternative land uses."
    },
    
    "Grain Sorghum": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained soils ideal for sorghum. Deep root system (6-8 ft potential) develops fully. Under excellent drainage, sorghum competes with corn for yield (150+ bu/ac possible). No restrictions on field operations. Strong stands. Vigorous growth. No drainage-related diseases. Full genetic potential expressed. However, sorghum's advantage is stress tolerance, not high-drainage requirements - this is 'overkill' for sorghum.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained very suitable. Minor limitations. Sorghum more tolerant of brief saturation than corn - this drainage level excellent for sorghum. Occasional field delays acceptable. Root system effective to 4-5 ft. Yields 120-150 bu/ac achievable. Sorghum begins showing its efficiency advantages over corn at this drainage level - similar yields with less stress from occasional wet periods.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained - this is where sorghum excels. Sorghum significantly MORE tolerant of poor drainage than corn. While corn struggles at this level, sorghum produces reasonable crops. Root system still functional to 3-4 ft despite limitations. Yields 80-120 bu/ac - BETTER than corn at same drainage level. Preferred over corn in marginally drained fields. Stand establishment more reliable than corn. This is sorghum's 'sweet spot' for demonstrating advantages.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits sorghum but less severely than corn. Sorghum still THE best cereal choice at poor drainage. Can achieve 50-80 bu/ac where corn completely fails. More tolerant of waterlogging stress. Better seedling vigor in wet conditions. While not ideal, sorghum economically viable where other cereals are not. Surface drainage improvements beneficial but sorghum works at this level. Clear advantage over corn/wheat.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained still limits even sorghum. Yields <50 bu/ac. Even sorghum's superior tolerance has limits. Stand establishment difficult. However, still better option than corn or wheat at extreme poor drainage. If attempting cereal production on very poorly drained soils, sorghum best choice. Consider rice (truly adapted to flooding) or alternative crops. Drainage essential for economic cereal production."
    },
    
    "Barley": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for barley. Rapid spring growth supported by good aeration. Excellent tillering and stand density. Deep rooting (3-4 ft). Yields of 100+ bu/ac possible. Test weights excellent (>48 lb/bu). For malting barley, uniform growth and maturity achievable. No drainage-related quality issues. Field operations unrestricted. Disease pressure minimal. Can achieve premium brewing quality specifications.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for barley. Minor limitations. Barley somewhat more waterlogging-tolerant than wheat - performs well at this drainage level. Occasional field delays. Good germination and establishment. Yields 80-100 bu/ac. Test weights good (45-48 lb/bu). Both feed and malting quality achievable. Some increase in diseases during wet periods but manageable. Overall excellent for barley production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for barley. Barley MORE tolerant of imperfect drainage than wheat - good choice at moderate drainage. Planting delays possible but less critical than for wheat. Yields 50-80 bu/ac. Test weights acceptable (42-45 lb/bu). Root diseases increase but barley resistance better than wheat. Feed barley quite viable. Malting barley challenging due to uniformity requirements. Consider barley over wheat at this drainage level.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits barley significantly but less than wheat. Barley better choice than wheat for poor drainage situations. Stands difficult to establish. Yields 30-50 bu/ac. Test weights poor (<42 lb/bu). Malting quality not achievable. Feed barley still possible with drainage improvements. Disease pressure high. Economics marginal. Barley among better small grain choices but still challenging. Consider oats (most tolerant) or drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for barley. Cannot establish adequate stands. Yields <30 bu/ac. Barley has moderate waterlogging tolerance but cannot overcome extreme poor drainage. Complete failures possible. Not economically viable. While better than wheat, still requires reasonable drainage for economic production. Consider rice or wetland uses."
    },
    
    "Oats": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for oats though perhaps 'over-qualified' - oats adapted to wider range. Strong stands and vigorous growth. Excellent tillering. Deep rooting for oats (2-3 ft). Yields 120+ bu/ac possible. Test weights excellent (>38 lb/bu). Good straw strength. No drainage-related diseases. Field operations unrestricted. Can achieve food-grade quality specifications.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained very suitable - actually ideal for oats. Minor limitations. Oats quite waterlogging-tolerant compared to other small grains. Occasional field delays not problematic. Good establishment. Yields 90-120 bu/ac. Test weights good (35-38 lb/bu). Oats perform very well at this drainage level - often preferred over wheat/barley. Disease pressure minimal.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained - oats BEST small grain choice at this level. Oats MOST waterlogging-tolerant major cereal. While wheat and barley struggle, oats produce reasonable crops. Yields 60-90 bu/ac - better than other small grains at same drainage. Stand establishment more reliable. Test weights acceptable (32-35 lb/bu). Root diseases less severe than wheat/barley. THIS IS OAT'S ADVANTAGE - excels where others fail. Strongly recommended over other cereals.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained still allows oat production. Oats MOST tolerant small grain to poor drainage. Can achieve 40-60 bu/ac where wheat/barley fail completely. Stand establishment possible though challenging. Test weights low (<32 lb/bu). Forage oats may be better option than grain harvest. Disease pressure increases but oats more resistant. If growing small grains on poorly drained soils, oats ONLY viable choice. Economics marginal but possible.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained limits even oats. Yields <40 bu/ac. However, oats STILL most viable small grain option. If attempting cereal on very poorly drained soil, use oats. Better suited as forage (hay/silage) than grain at this extreme. Stand establishment difficult. Even oats' superior tolerance has limits. Drainage improvements essential for economic grain production. Consider forage oats or alternative crops."
    },
    
    "Rice": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100) but UNUSUAL situation for rice. Well drained soils can grow upland rice varieties but not typical flooded production. This is DRY-LAND rice scenario. Yields limited (2,000-4,000 lb/ac) compared to flooded production. Not economically competitive with flooded rice. Under these drainage conditions, other crops (corn, soybeans) typically more profitable. Consider this only for rotation purposes or where flooding not feasible despite good drainage infrastructure.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable for rice if flooding controlled. Key is ability to MANAGE water level - good drainage allows water table control. Can alternate flooded/drained conditions as needed. This is actually OPTIMAL for modern rice production - flood during growth, drain for operations and harvest. Controlled water management maximizes yields (8,000+ lb/ac). Can practice multiple-inlet rice irrigation. Good for precision-leveled fields with water management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained GOOD for traditional flooded rice if natural drainage insufficient during operations. Challenge is draining for harvest operations. If field naturally holds water during season but drains for harvest, this is acceptable. Yields 6,000-8,000 lb/ac. However, if cannot drain adequately for field operations (planting, harvest), becomes problematic. Need sufficient drainage to operate equipment but poor enough to maintain flood without excessive water inputs.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained acceptable to GOOD for rice if permanent flooding tolerable. Rice adapted to anaerobic root zone conditions. Challenge is field operations - need access for planting and harvest even if limited. If can get on field for these operations (or use aerial seeding), poor drainage beneficial for water management. Yields 4,000-6,000 lb/ac. Permanent flooding systems work well. Issue is harvest access in very wet years.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained can be IDEAL for rice if field operations possible. Rice ONLY major field crop actually BENEFITING from poor drainage. Permanent or near-permanent flooding optimal for rice. Water management minimal - field naturally stays flooded. Challenge is planting and harvest operations. Aerial seeding possible. Harvest may require specialized equipment for wet conditions. Yields 6,000-8,000+ lb/ac if operations manageable. This drainage level ADVANTAGE for rice, DISASTER for upland crops."
    },
    
    "Sunflower": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for sunflower. Deep tap root (6-8 ft) develops fully accessing deep moisture. Sunflower tap root requires well-aerated soil for penetration. Optimal for 3,000+ lb/ac (60+ bu/ac) production. No field operation restrictions. Strong stands with vigorous early growth. No waterlogging stress during critical flowering period. Good seed fill and oil content. Harvest timing flexible - critical for quality. Disease pressure minimal.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable with minor limitations. Occasional brief saturation tolerable. Deep rooting still achieves 4-6 ft depth. Yields 2,200-3,000 lb/ac (45-60 bu/ac). Sunflower moderately sensitive to waterlogging - prefers good drainage but more tolerant than cotton. Some increase in root and stem diseases during wet periods. Field operations occasionally delayed. Overall good for sunflower production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for sunflower. Significant limitations. Tap root development severely restricted - may only penetrate 2-3 ft, losing sunflower's drought tolerance advantage. Yields 1,600-2,200 lb/ac (32-45 bu/ac). Stand establishment problems in wet soils. Increased root and stem rots (Sclerotinia, Phytophthora). Waterlogging during flowering causes significant yield loss. Head rot increases in wet conditions. Economics marginal. Surface drainage essential.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for sunflower. Tap root cannot penetrate compacted or saturated layers - sunflower loses its primary adaptation (deep rooting). Shallow root system makes plant susceptible to drought despite normally being drought-tolerant crop. Yields <1,600 lb/ac (32 bu/ac). Severe disease pressure. Stand establishment very difficult. Sunflower not recommended without extensive drainage. Consider crops adapted to poor drainage instead.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Sunflower requires well-drained soils for tap root development - fundamental to crop's biology. Cannot establish viable stands. Severe diseases. Complete failures common. Not economically viable under any circumstances. Do not attempt sunflower production. Consider crops adapted to wet conditions."
    },
    
    "Canola": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for canola. Critical for fall establishment and winter survival. Deep rooting (4-5 ft) develops during fall/spring. Yields of 60+ bu/ac possible. No waterlogging stress during fall establishment - critical period. Excellent winter survival - well-drained soils prevent crown rot and ice damage. Strong spring growth. No delays in fall planting or spring/summer operations. Disease pressure minimal.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable for canola. Minor limitations. Canola moderately sensitive to waterlogging especially during fall establishment and flowering. Occasional field delays tolerable. Fall root development good if not saturated during October-November. Winter survival generally good. Yields 45-60 bu/ac. Some increase in Sclerotinia and blackleg during wet springs. Overall suitable with proper variety selection and management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very challenging for canola. Significant fall planting delays common - may miss optimal establishment window. Poor fall root development leads to winterkill. Surviving plants show weak spring growth. Yields 30-45 bu/ac. Severe disease pressure especially Sclerotinia stem rot in wet conditions. Flowering and pod development disrupted by waterlogging. Economics poor. Canola not recommended without drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for canola. Fall establishment essentially impossible - seedlings rot or fail to develop adequate roots before winter. Winterkill rates extreme. Spring canola not viable alternative - also very waterlogging-sensitive. Yields <30 bu/ac in rare successful crops. Severe disease losses. Not economically viable. Canola requires well-drained soils for establishment and survival. Do not attempt without major drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot establish fall-planted canola - seedlings die in saturated soils. Spring canola also fails. Brassicas generally sensitive to waterlogging - canola among worst. Complete crop failures. Not viable under any circumstances. Canola requires excellent drainage for successful production. Consider entirely different crops adapted to wet conditions."
    },
    
    "Dry Beans": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for dry bean quality production. Beans very sensitive to waterlogging - require excellent aeration for nodulation and pod development. Good rooting (2-3 ft) supports nitrogen fixation. Yields 3,000+ lb/ac possible. No delays in field operations critical for harvest timing. Clean harvest with minimal staining. Disease pressure minimal. Good seed quality for market. Optimal conditions for pod fill and maturity.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with caution. Minor limitations. Beans quite waterlogging-sensitive - even brief saturation reduces yields. Nodulation affected by wet conditions. Occasional field delays acceptable if not during critical flowering/pod fill. Yields 2,200-3,000 lb/ac. Some increase in root rots and white mold. Harvest quality may suffer if wet. Careful variety selection important. Moderately suitable.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very problematic for beans. Beans MORE sensitive to poor drainage than soybeans. Significant stand establishment problems. Poor nodulation limits N-fixation. Severe disease pressure especially white mold, root rots. Yields 1,600-2,200 lb/ac. Pod quality poor - staining and discoloration. Harvest difficulties. Economics poor. Dry beans not recommended without extensive drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for dry bean production. Beans very sensitive to waterlogging. Cannot establish viable stands. No effective nodulation. Severe root rots. Yields <1,600 lb/ac if any harvestable crop. Pod quality unmarketable - heavy staining. Harvest impossible in wet conditions. Not economically viable. Dry beans require well-drained soils - non-negotiable for quality production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Dry beans among most waterlogging-sensitive field legumes. Complete crop failures. Cannot achieve stands or seed production. Not viable under any circumstances. Dry beans require excellent drainage throughout season especially during flowering and harvest. Do not attempt production. Consider crops adapted to wet conditions."
    },
    
    "Peanuts": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained absolutely essential for peanuts. Peanuts EXTREMELY sensitive to waterlogging - pegging process requires well-aerated soil. Deep rooting and pegging zone (0-6 inches) must have excellent aeration. Yields 5,000+ lb/ac possible. Optimal conditions for geocarpic pod development. Excellent grade and quality. No constraints on pegging. Disease pressure minimal. Harvest timing flexible. Can achieve premium market grades.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for peanuts. Peanuts MORE sensitive to poor drainage than most field crops. Even brief saturation during pegging drastically reduces yield. Minor limitations significant for peanuts. Yields 4,000-5,000 lb/ac but with risk. Increased disease pressure especially pod rots. Pod quality variable. Requires careful monitoring during wet periods. Many peanut regions require well-drained soils as baseline - this level considered marginal.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for peanut production. Peanuts cannot tolerate poor drainage due to pegging and pod development in soil. Saturated soil prevents pegging or rots developing pods. Yields <3,000 lb/ac. Very poor pod quality - rots and discoloration. High percentage of pops (unfilled pods). Severe disease pressure. Not economically viable. Peanuts require excellent drainage - industry standard.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable. Peanuts REQUIRE well-drained soils for geocarpic fruiting. Pegging process fails in saturated soils. Pods rot if they form. Yields negligible. Complete failures common. Not viable under any circumstances. Peanut production requires well-drained sandy loam soils as industry baseline. Poor drainage eliminates peanuts from consideration regardless of other factors.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely impossible for peanuts. Among most waterlogging-sensitive major field crops. Underground pod development requires aerobic conditions. Cannot produce crop. Not economically viable under any management. Do not attempt peanut production. Peanuts require excellent drainage - fundamental requirement of the crop's biology."
    },
    
    "Sugar Beets": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for sugar beets. Deep tap root (6-10 ft potential) requires well-aerated profile. Yields 30+ tons/ac with excellent sugar content (18%+). No field operation restrictions critical for precise planting and timely harvest. Long growing season (150-180 days) requires sustained good aeration. No waterlogging stress affecting root quality. Disease pressure minimal. Can achieve processing contract specifications.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for beets. Minor limitations. Tap root still develops to 4-6 ft. Yields 25-30 tons/ac. Occasional field delays tolerable. Sugar beets moderately sensitive to waterlogging - more so than many crops but adaptable. Some increase in root rots during wet periods. Sugar content may be slightly reduced. Overall good for commercial production with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for sugar beets. Significant limitations. Tap root development restricted to 2-3 ft reducing storage capacity and yield. Yields 18-25 tons/ac. Root quality issues - forking, surface cracking, rot. Sugar content reduced (14-16%). Increased disease pressure especially root rots. Harvest delays cause quality deterioration. Economics marginal for processing contracts. Surface drainage essential.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial sugar beet production. Tap root cannot develop properly. Very shallow rooting makes plants susceptible to lodging and drought. Yields <18 tons/ac. Poor root shape and quality - heavy forking, cracking. Low sugar content (<14%). Severe root rots. Harvest difficulties. Cannot meet processing contract specifications. Not economically viable. Sugar beets require well-drained soils for quality production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Deep tap root development fundamental to sugar beet production - impossible in saturated soils. Cannot produce marketable roots. Severe diseases. Not viable under any circumstances. Sugar beets require excellent drainage for the deep root system. Do not attempt production without major drainage improvements."
    },
    
    "Sugarcane": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained very suitable for sugarcane. Deep root system (6-8 ft) develops fully. However, sugarcane grown with irrigation in many regions, so excellent natural drainage may require supplemental water. Yields 100+ tons/ac possible. No restrictions on field operations including planting and ratoon management. Multiple productive ratoon cycles (4-7 years). Root health excellent supporting long production cycle. Disease pressure minimal.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained good for sugarcane. Minor limitations. Sugarcane moderately tolerant of occasional saturation - more so than many crops. Grows in subtropical/tropical regions with high rainfall. Occasional wet periods tolerable. Yields 80-100 tons/ac. Good ratoon longevity (3-5 crops). Some increase in root diseases during extended wet periods but manageable. Overall suitable for commercial production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for sugarcane depending on season. Sugarcane MORE tolerant of poor drainage than most field crops. In regions with distinct wet/dry seasons, poor drainage during wet season tolerable if dry season allows operations and root development. Yields 60-80 tons/ac. Ratoon decline may be accelerated (2-3 crops). Root diseases increase. Planting and harvest timing critical. Consider drainage improvements for sustained production.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits sugarcane significantly but less than most crops. Plant crop establishment difficult. Weak stools lead to poor ratoon development. Yields 40-60 tons/ac. Short ratoon life (1-2 crops) before replanting necessary. Disease pressure high especially root rots. Frequent replanting increases costs dramatically. Economics marginal. Sugarcane has moderate waterlogging tolerance but cannot overcome severe limitations.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable for commercial sugarcane. Cannot establish viable plant crop. No productive ratoon cycles. Yields <40 tons/ac. Severe root rots and stool death. While sugarcane more tolerant than many crops, extreme poor drainage still prevents economic production. Not viable for sustained commercial operations. Drainage essential."
    },
    
    "Tobacco": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for quality tobacco. Tobacco very sensitive to waterlogging - both yield and quality severely affected. Good aeration critical for root development and nutrient uptake. Yields 2,200-2,800+ lb/ac cured leaf. Excellent leaf quality - uniform ripening, good texture, proper curing characteristics. No waterlogging stress affecting leaf chemistry. Field operations unrestricted. Disease pressure minimal especially important for tobacco.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with caution. Minor limitations but tobacco quite sensitive. Even brief saturation can cause issues. Yields 1,800-2,400 lb/ac. Occasional field delays problematic for critical operations (transplanting, topping, harvest). Some increase in root and stem diseases. Leaf quality may be variable. Proper field selection critical. Many tobacco regions require well-drained soils as baseline.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for quality tobacco production. Tobacco very waterlogging-sensitive. Poor stands after transplanting. Weak plants. Yields 1,200-1,800 lb/ac. Poor leaf quality - uneven ripening, thin leaves, poor curing characteristics. Disease pressure severe especially bacterial wilt, black shank. Unmarketable grades. Economics poor. Tobacco requires well-drained soils - industry standard. Not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for tobacco. Cannot establish viable stands. Transplant failures common. Severe disease pressure. Yields <1,200 lb/ac if any crop. Leaf quality unmarketable. Not economically viable. Tobacco production requires well-drained soils - fundamental requirement. Do not attempt production without extensive drainage that brings soil to at least moderate drainage class.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Tobacco among more waterlogging-sensitive field crops. Complete crop failures. Cannot transplant or establish. Severe diseases universal. Not viable under any circumstances. Tobacco requires excellent drainage for quality production. Consider entirely different crops or alternative land uses."
    },
    
    "Alfalfa": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for alfalfa. Deep tap root (10-15+ ft) requires well-aerated profile throughout depth. Alfalfa EXTREMELY sensitive to waterlogging - will not survive poor drainage. Yields 8+ tons/ac annually. Long-lived productive stands (5+ years). Excellent winter survival. Strong spring growth. Disease pressure minimal. This drainage level non-negotiable for alfalfa - industry baseline.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for alfalfa. Even minor drainage limitations problematic. Alfalfa MORE sensitive than most crops. Brief saturation tolerable only if not prolonged or frequent. Yields 6-8 tons/ac. Stand longevity reduced (4-5 years). Winter injury increases if crown saturated. Some root rots during wet periods. Many alfalfa-growing regions consider this level marginal. Prefer well-drained sites.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for alfalfa. Alfalfa CANNOT tolerate poor drainage. Deep tap root development impossible. Shallow water tables cause stand failure. Yields <4 tons/ac if stand survives. Stand life very short (2-3 years). Severe winterkill. Heavy disease pressure especially Phytophthora root rot. Not economically viable. Alfalfa requires well-drained soils - fundamental requirement. Do not plant without drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable. Alfalfa will not survive. Stand establishment fails or plants die within first year. Waterlogging during any season lethal to alfalfa. Deep tap root system and crown location make alfalfa intolerant of saturation. Not economically viable under any circumstances. Alfalfa requires excellent drainage - among most drainage-sensitive forage crops. Consider alternative legumes (clover, lespedeza) or grasses.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely impossible for alfalfa. Among most waterlogging-sensitive commonly grown crops. Complete failures universal. Will not establish or survive even briefly. Deep tap root biology fundamentally incompatible with poor drainage. Do not attempt alfalfa production. Consider wetland-adapted forages (reed canarygrass, prairie cordgrass) or alternative land uses."
    },
    
    "Clover": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for most clover species. Red clover and white clover thrive. Good nodulation and N-fixation. Yields 5+ tons/ac dry matter. Excellent stands with good density and persistence. Can achieve pure stands or quality grass-clover mixtures. No waterlogging stress. Disease pressure minimal. All clover species perform well.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for most clovers. Minor limitations. Red clover, white clover, alsike clover all perform well. Good nodulation despite occasional saturation. Yields 4-5 tons/ac. Most clover species moderately tolerant of brief wet periods. Some increase in diseases during wet conditions. Generally excellent for clover production. Good choice for grass-clover pasture mixtures.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for adapted species. WHITE CLOVER most tolerant - best choice at this level. Alsike clover also adapted to wetter conditions. Red clover struggles - avoid. Yields 3-4 tons/ac. Nodulation reduced during saturated periods but functional. White clover excellent choice for poorly drained pastures. Mixed stands with wetland-tolerant grasses recommended. Disease pressure increases but manageable.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits most clovers. WHITE CLOVER still viable - most waterlogging-tolerant common clover. ALSIKE CLOVER specifically adapted to wet, poorly drained soils - excellent choice here. Red clover fails. Yields 2-3 tons/ac. Mixed grass-clover stands with wetland grasses work well. Pure clover stands difficult. Consider alsike clover specifically for this drainage level - one of its primary adaptations.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable for most clovers. Even white clover and alsike clover struggle at extreme poor drainage. Yields <2 tons/ac. Stand persistence poor. Most legumes require reasonable aeration for nodulation. Consider wetland-adapted species or grass monocultures instead. If using legume, alsike clover most tolerant but performance marginal."
    },
    
    "Grass Hay": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for grass hay production. Most grass species thrive. Deep rooting supports drought tolerance. Yields 8+ tons/ac with multiple cuttings (4-5). All cool-season (orchardgrass, timothy, tall fescue) and warm-season (bermudagrass, switchgrass) grasses perform well. No restrictions on harvest timing. Disease pressure minimal. High quality forage.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for most grasses. Minor limitations. Occasional harvest delays during wet periods. Most grasses moderately tolerant of brief saturation. Yields 6-8 tons/ac with 3-4 cuttings. Good quality hay. Some species (tall fescue, reed canarygrass) particularly adapted to moderate drainage. Overall excellent for grass hay production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable with species selection. TALL FESCUE and REED CANARYGRASS most adapted - excellent choices. Orchardgrass and timothy struggle. Yields 4-6 tons/ac with 2-3 cuttings. Harvest timing critical - often delayed by wet conditions. Quality variable. Select waterlogging-tolerant species. Mixed stands with wetland grasses may be beneficial.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits most traditional hay grasses. REED CANARYGRASS specifically adapted to wet conditions - best choice. Tall fescue acceptable. Orchardgrass, timothy, bermudagrass unsuitable. Yields 2-4 tons/ac. Harvest operations very difficult - often cannot access field. Quality often poor due to delayed harvest. Consider reed canarygrass for poorly drained hay fields - one of its primary adaptations.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained requires specialized species. REED CANARYGRASS most adapted hay species for very wet conditions. Other option is native wetland grasses. Yields <2 tons/ac. Harvest extremely difficult - may require specialized equipment. Quality generally poor. Consider grazing rather than hay, or wetland restoration rather than forage production."
    },
    
    "Silage Corn": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for silage corn. Same requirements as grain corn - deep rooting (5-6 ft), no saturation tolerance. Yields 30+ tons/ac fresh weight (8+ tons DM/ac). Excellent stand establishment. No restrictions on harvest operations. Can achieve optimal maturity for silage quality. Disease pressure minimal. Maximum total dry matter production.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable. Same limitations as grain corn. Minor yield reductions possible (5-10%). Yields 25-30 tons/ac fresh. Occasional harvest delays. Silage corn has same drainage requirements as grain corn - no more tolerant. Root diseases increase slightly in wet conditions. Overall suitable with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for silage corn. Same significant limitations as grain corn. Restricted rooting. Yields 20-25 tons/ac fresh (5-6 tons DM/ac). Harvest timing critical - often delayed in poor drainage. Consider FORAGE SORGHUM as alternative - much better adapted to poor drainage than corn. Economics marginal for silage corn at this level.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for silage corn. Same severe limitations as grain corn. Yields <20 tons/ac fresh. STRONGLY recommend FORAGE SORGHUM or SORGHUM-SUDANGRASS instead - much more waterlogging-tolerant than corn. Can achieve better yields and quality with adapted species. Silage corn not economically viable. Switch to adapted forages.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for any corn including silage. Cannot establish stands. Complete failures. Not viable under any circumstances. Consider alternative forages adapted to wet conditions (reed canarygrass) or different land uses. Do not attempt corn silage production."
    },
    
    # ========================================================================
    # VEGETABLE CROPS
    # ========================================================================
    
    "Tomatoes": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for tomato production. Tomatoes very sensitive to waterlogging at all growth stages. Deep rooting (4-6 ft) requires well-aerated profile. Yields 40+ tons/ac fresh market possible. No field operation restrictions. Excellent fruit set and development. Minimal disease pressure especially important for tomatoes (bacterial wilt, Phytophthora). No blossom-end rot from waterlogging stress. Premium fruit quality and shelf life.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with careful management. Tomatoes quite waterlogging-sensitive. Even brief saturation during critical periods (flowering, fruit set) causes problems. Yields 30-40 tons/ac. Occasional field delays tolerable if not during transplanting or harvest. Disease pressure increases especially bacterial diseases and late blight. Drip irrigation essential for water management. Raised beds beneficial. Moderately suitable with intensive management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very problematic for tomatoes. Significant limitations. Poor transplant survival. Weak plants. Heavy flower and fruit drop during saturated periods. Yields 20-30 tons/ac at best. Severe disease pressure - bacterial wilt, Phytophthora root/crown rot, late blight all increase dramatically. Fruit quality poor. Economics questionable. Raised beds with imported soil essential. Field production not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for field tomato production. Cannot maintain viable plants. Transplant failures common. Severe diseases universal. Yields <20 tons/ac if any harvestable crop. Fruit quality unmarketable. Not economically viable for field production. Container/greenhouse production only option. Do not attempt field tomatoes without major drainage improvements bringing soil to at least moderate drainage class.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for tomatoes. Among most waterlogging-sensitive vegetable crops. Cannot establish or survive. Complete crop failures. Tomatoes require well-drained soils for commercial production - industry standard. Not viable under any field conditions. Consider only greenhouse/container production with imported media or different crops entirely."
    },
    
    "Potatoes": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for potato production. Tuber development requires excellent aeration in tuber zone (4-12 inches). Yields 500+ cwt/ac (25+ tons/ac) possible. Excellent tuber quality - smooth skin, good shape, no defects. Minimal disease pressure especially important for potatoes (late blight, bacterial soft rot). No waterlogging-induced lenticels or secondary growth. Field operations unrestricted for hilling and harvest. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for potatoes. Minor limitations. Brief saturation tolerable if soil drains quickly. Yields 400-500 cwt/ac. Some increase in tuber defects during wet periods - enlarged lenticels, secondary growth, cracking. Disease pressure increases especially late blight and soft rot. Harvest timing critical - cannot delay in wet weather. Overall suitable with proper variety selection and management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for quality potato production. Significant tuber quality problems. Enlarged lenticels create rough appearance. Secondary growth and growth cracks common. Tuber rots increase dramatically. Yields 300-400 cwt/ac. Poor skin finish affects marketability. Storage quality reduced. Disease pressure severe. Raised beds essential. Economics marginal for commercial production. Better suited for processing than fresh market.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial potato production. Severe tuber quality defects - extensive lenticels, cracking, rots. Yields 200-300 cwt/ac. Most tubers unmarketable quality. Cannot harvest - wet soil causes damage and contaminates tubers. Storage rots universal. Not economically viable. Potatoes require well-drained soils for quality production. Do not plant without extensive drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Tubers rot in saturated soil. Cannot produce marketable crop. Complete failures common. Potatoes very sensitive to waterlogging during tuber development. Not viable under any circumstances. Potatoes require excellent drainage especially during bulking and harvest periods. Consider entirely different crops."
    },
    
    "Sweet Potatoes": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for sweet potato production. Good aeration in root development zone (4-10 inches) critical. Deep sandy loams optimal. Yields 400+ bu/ac (25+ tons/ac) possible. Excellent root shape, skin quality, and minimal defects. No wet-soil induced rots. Field operations unrestricted. Can achieve premium market grades. Disease pressure minimal especially important for sweet potatoes (black rot, soft rot).",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for sweet potatoes. Minor limitations. Sweet potatoes MORE tolerant of brief wet periods than Irish potatoes but still prefer good drainage. Yields 300-400 bu/ac. Some root quality issues if prolonged saturation - surface cracking, rough skin. Disease pressure increases. Harvest timing critical. Overall good for sweet potato production with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for sweet potatoes with intensive management. Sweet potatoes MORE tolerant than Irish potatoes of imperfect drainage. Yields 200-300 bu/ac. Root quality variable - misshapen, cracked, rough skin more common. Increased disease pressure especially soil rots. Raised beds beneficial. Still economically viable with adapted varieties. Better choice than Irish potatoes at this drainage level.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits sweet potato production significantly. More tolerant than Irish potatoes but still challenged. Yields 150-200 bu/ac. Poor root quality - small, misshapen, severe cracking. Heavy disease pressure. Harvest difficulties. Economics marginal. Sweet potatoes workable at this level where Irish potatoes fail, but requires intensive management. Raised beds essential. Consider if sweet potatoes needed but not ideal.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for sweet potatoes. Severe root rots. Cannot produce marketable roots. Yields <150 bu/ac with very poor quality. While more tolerant than Irish potatoes, sweet potatoes still require reasonable drainage for storage root development. Not economically viable. Not recommended without major drainage improvements."
    },
    
    "Onions": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for onion production. Shallow root system (8-18 inches) very sensitive to waterlogging. Excellent aeration in upper profile critical. Yields 800+ cwt/ac possible. No waterlogging stress affecting bulb development. Minimal disease pressure especially white rot and bacterial soft rot. Excellent bulb quality - firm, well-formed, good storage life. Field operations unrestricted including harvest for optimal curing.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable with careful management. Minor limitations. Onions quite waterlogging-sensitive due to shallow roots. Brief saturation tolerable if rapid drainage. Yields 600-800 cwt/ac. Some increase in diseases especially bacterial soft rot and white rot. Bulb quality good with proper management. Occasional field delays during harvest problematic for curing. Overall suitable with proper varieties and management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very challenging for onion production. Onions' shallow root system cannot tolerate poor drainage. Significant stand losses. Slow bulb development. Yields 400-600 cwt/ac. Small bulbs with poor storage quality. Severe disease pressure - soft rots increase dramatically in wet conditions. Harvest timing critical but often delayed. Economics marginal. Raised beds essential. Green bunching onions more tolerant than bulb types.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for bulb onion production. Shallow roots extremely sensitive to saturation. Poor stands. Minimal bulbing. Yields 300-400 cwt/ac if any crop. Severe diseases - rots universal. Storage impossible. Not economically viable for bulb onions. If attempting onions, consider only green bunching types with frequent harvest or intensive raised bed production. Field bulb onions not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for onion production. Onions' shallow root system among most waterlogging-sensitive of vegetables. Cannot establish or bulb. Severe rots. Complete failures. Not viable under any circumstances. Onions require well-drained soils for commercial production. Do not attempt production."
    },
    
    "Carrots": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for carrot production. Deep loose soil critical for straight, well-formed roots. Excellent aeration prevents root defects. Yields 30+ tons/ac possible. Premium root shape, color, and quality. Minimal disease pressure. No cracking or forking from waterlogging stress. Field operations unrestricted. Can achieve top market grades. Harvest timing flexible.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for carrots. Minor limitations. Brief saturation tolerable if soil structure maintains good drainage. Yields 20-30 tons/ac. Some increase in root defects - slight forking, surface cracking. Disease pressure increases slightly. Overall good for commercial carrot production with proper soil preparation and management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for quality carrots. Significant root quality issues. Heavy forking and cracking common. Roots misshapen and stunted. Yields 15-20 tons/ac. Poor color and increased fiber. Disease pressure especially cavity spot and bacterial soft rot. Marketability reduced. Economics marginal. Raised beds beneficial. Short varieties better than long types. Processing market more suitable than fresh.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial carrot production. Severe root defects - extensive forking, cracking, rot. Yields 10-15 tons/ac. Most roots unmarketable. Pale color, tough texture. Cannot harvest properly - roots break trying to pull from compacted wet soil. Not economically viable. Carrots require well-drained loose soils for quality root development. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Roots rot in saturated soil. Cannot produce marketable carrots. Complete quality failures. Carrots require excellent drainage and soil structure for straight root development. Not viable under any circumstances. Do not attempt carrot production."
    },
    
    "Lettuce": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for lettuce production. Shallow root system (12 inches) requires good surface aeration. Yields 600+ cartons/ac (25+ tons/ac) possible. Rapid growth without waterlogging stress. Excellent head formation and quality. Minimal disease pressure especially bottom rot and drop. Clean harvest conditions. Multiple succession plantings possible. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for lettuce. Minor limitations. Lettuce shallow roots fairly sensitive to waterlogging. Brief saturation tolerable if drainage rapid. Yields 450-600 cartons/ac. Some increase in bottom rot during wet periods. Head quality good with proper management. Occasional field operation delays. Overall suitable for commercial production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for lettuce. Shallow root system sensitive to poor drainage. Slow growth and poor head formation. Yields 300-450 cartons/ac. Increased disease pressure especially bottom rot. Bolting risk increases under stress. Harvest quality variable. Raised beds beneficial. Romaine and leaf types more tolerant than crisphead. Economics marginal for crisphead lettuce.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for quality lettuce production. Lettuce's shallow roots extremely sensitive. Poor stands and growth. Yields <300 cartons/ac. Severe bottom rot and drop. Poor head formation. Bitter taste. Not economically viable for commercial production. Lettuce requires well-drained soils for quality production. If attempting, use only leaf types with raised beds.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Lettuce among more waterlogging-sensitive vegetables due to shallow roots. Cannot establish or grow. Severe diseases. Complete failures. Not viable under any circumstances. Lettuce requires excellent surface drainage. Do not attempt production."
    },
    
    "Cabbage": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for cabbage production. Good rooting (2-3 ft) supports large head development. Yields 30+ tons/ac (600+ cartons) possible. Excellent head formation - large, firm, uniform. Minimal disease pressure especially black rot and clubroot. No splitting from waterlogging stress. Field operations unrestricted. Premium quality and storage life.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for cabbage. Minor limitations. Brassicas moderately tolerant of brief saturation. Yields 22-30 tons/ac. Some increase in diseases especially clubroot in wet conditions. Head splitting may increase if moisture fluctuates. Overall suitable for commercial cabbage production with proper management and variety selection.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for quality cabbage. Significant limitations. Slow head development. Yields 15-22 tons/ac. Small heads with loose formation. Increased disease pressure - clubroot severe in acid poorly drained soils, black rot increases. Head splitting common. Storage quality reduced. Economics marginal. Raised beds beneficial. Consider cole crops more tolerant of poor drainage.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial cabbage. Poor plant vigor. Minimal head formation. Yields 10-15 tons/ac. Severe clubroot in acid soils - disease devastating in wet conditions. Other diseases universal. Poor quality unmarketable heads. Not economically viable. Cabbage requires reasonable drainage for quality production. Consider most tolerant brassicas (kale, collards) or drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Brassicas sensitive to waterlogging. Cannot establish or form heads. Clubroot universal in poorly drained acid soils. Complete failures. Not viable under any circumstances. Cabbage requires well-drained soils for commercial production. Do not attempt."
    },
    
    "Broccoli": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for broccoli production. Good rooting supports uniform head development. Yields 8+ tons/ac (300+ cartons) possible. Excellent head size, quality, and uniformity. Tight dark green heads. Minimal disease pressure especially black rot and clubroot. No waterlogging stress during critical head development. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for broccoli. Minor limitations. Broccoli moderately sensitive to waterlogging during head development. Yields 6-8 tons/ac. Some increase in diseases especially clubroot in wet acid soils. Head quality good with proper management. Occasional delays tolerable. Overall suitable for commercial production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very challenging for broccoli. Significant limitations. Slow uneven head development. Yields 4-6 tons/ac. Small heads with loose formation. Hollow stem common. Disease pressure severe - clubroot, black rot. Buttoning (premature small heads) increases under stress. Economics marginal. Raised beds essential. Consider more tolerant brassicas (kale, collards).",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial broccoli. Poor plant growth. Minimal head formation or severe buttoning. Yields <4 tons/ac. Clubroot devastating in poorly drained acid soils. Other diseases universal. Unmarketable quality. Not economically viable. Broccoli requires well-drained soils for quality head production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot establish or form marketable heads. Severe clubroot in acid soils. Complete failures. Broccoli quite waterlogging-sensitive especially during head development. Not viable under any circumstances. Do not attempt production."
    },
    
    "Cauliflower": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for cauliflower production. Cauliflower MOST demanding common brassica. Good rooting supports large curd development. Yields 7+ tons/ac (300+ cartons) possible. Excellent curd quality - white, tight, uniform. No discoloration or ricey texture. Minimal disease pressure. Premium market quality achievable.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for cauliflower. Cauliflower MORE sensitive than cabbage/broccoli to imperfect conditions. Even minor drainage limitations problematic. Yields 5-7 tons/ac. Curd quality variable - discoloration and ricey texture increase. Disease pressure increases. Overall challenging but possible with intensive management and proper varieties.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for quality cauliflower. Cauliflower MOST sensitive common brassica to poor drainage. Poor curd formation. Yields 3-5 tons/ac if any marketable. Severe quality issues - discoloration, ricey texture, small size. Disease pressure extreme. Not economically viable for commercial production. Consider broccoli or cabbage (less demanding) instead.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for cauliflower. Cannot produce marketable curds. Severe buttoning or no curd formation. Yields negligible. Clubroot devastating. Other diseases universal. Cauliflower requires excellent drainage - most demanding common brassica. Not recommended under any circumstances. Choose more tolerant crops.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Cauliflower among most waterlogging-sensitive vegetable crops. Complete failures. Cannot establish or produce. Not viable under any circumstances. Requires excellent drainage for commercial production. Do not attempt."
    },
    
    "Peppers": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for pepper production. Peppers very sensitive to waterlogging at all stages. Good rooting (18-24 inches) requires excellent aeration. Yields 30+ tons/ac (750+ bushels) possible. Excellent fruit set and development. No blossom drop from waterlogging stress. Minimal disease pressure especially Phytophthora blight. Premium fruit quality, size, and wall thickness.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with careful management. Peppers quite waterlogging-sensitive. Brief saturation during flowering causes significant blossom drop. Yields 22-30 tons/ac. Some increase in Phytophthora blight and bacterial diseases. Fruit quality good with proper management. Drip irrigation and raised beds beneficial. Moderately suitable with intensive management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very problematic for peppers. Peppers highly sensitive to poor drainage. Heavy blossom and fruit drop during wet periods. Yields 15-22 tons/ac. Severe Phytophthora blight - major disease of peppers in wet conditions. Poor fruit size and quality. Sunscald increases as foliage thins from stress. Economics questionable. Raised beds essential. Field production not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for pepper production. Cannot maintain healthy plants. Severe blossom drop. Yields <15 tons/ac. Phytophthora blight universal - devastating to peppers. Other diseases severe. Poor fruit quality. Not economically viable. Peppers require well-drained soils - very waterlogging-sensitive crop. Do not attempt field production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Peppers among most waterlogging-sensitive vegetable crops. Plant death common. Cannot produce. Phytophthora blight and other water-related diseases universal. Complete failures. Not viable under any circumstances. Consider only greenhouse/container production or different crops."
    },
    
    "Cucumbers": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for cucumber production. Shallow root system (12-18 inches) requires good surface aeration. Yields 700+ bushels/ac (20+ tons/ac) possible. Excellent fruit quality and extended harvest period. No waterlogging stress. Minimal disease pressure especially Phytophthora and Pythium. Straight, uniformly colored fruit. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for cucumbers. Minor limitations. Cucumbers moderately sensitive to waterlogging due to shallow roots. Brief saturation tolerable. Yields 500-700 bushels/ac. Some increase in root and fruit rots during wet periods. Overall suitable for commercial production with proper management and disease-resistant varieties.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for cucumber production. Shallow roots sensitive to poor drainage. Slow vine growth. Yields 350-500 bushels/ac. Misshapen, pale fruit. Bitter taste increases under stress. Severe disease pressure - Phytophthora, Pythium, belly rot. Harvest period shortened. Economics marginal. Raised beds and drip irrigation essential. Field production challenging.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial cucumber production. Shallow roots extremely sensitive. Poor vine vigor. Yields 200-350 bushels/ac. Severe diseases - water molds universal. Poor fruit quality - bitter, misshapen. Short harvest period. Not economically viable. Cucumbers require well-drained soils for quality production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cucumbers' shallow root system very waterlogging-sensitive. Cannot establish vigorous vines. Severe diseases. Minimal fruit production. Complete failures common. Not viable under any circumstances. Do not attempt cucumber production."
    },
    
    "Squash": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for squash production. Good rooting supports vigorous vine growth and heavy fruit load. Summer squash yields 800+ bushels/ac (25+ tons/ac), winter squash 30+ tons/ac possible. Excellent fruit quality and production period. No waterlogging stress. Minimal disease pressure especially Phytophthora crown/fruit rot. Premium quality fruit.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for squash. Minor limitations. Squash moderately tolerant of brief saturation compared to cucumbers. Summer squash yields 600-800 bushels/ac, winter squash 22-30 tons/ac. Some increase in crown and fruit rots. Overall suitable for commercial production with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for squash. Significant limitations. Reduced vine vigor. Summer squash yields 400-600 bushels/ac, winter squash 15-22 tons/ac. Disease pressure increases - Phytophthora, bacterial wilt. Fruit quality variable. Zucchini (summer type) MORE tolerant than winter squash. Economics marginal for winter types. Raised beds beneficial.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial squash production. Poor vine development. Summer squash yields 250-400 bushels/ac, winter squash 10-15 tons/ac. Severe disease pressure. Poor fruit quality. Winter squash especially challenging - long season in poor conditions. Not economically viable. If attempting squash, use summer types with raised beds. Winter squash not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot establish vigorous vines. Severe diseases. Minimal fruit production. Cucurbits generally sensitive to waterlogging. Complete failures common. Not viable under any circumstances. Do not attempt squash production."
    },
    
    "Watermelon": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for watermelon production. Deep tap root (4-6 ft) requires excellent aeration throughout profile. Yields 40+ tons/ac possible. Excellent fruit size, sweetness, and quality. Deep sandy loams optimal. No waterlogging stress during critical flowering and fruit development. Minimal disease pressure especially Phytophthora and Fusarium wilt. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable with caution. Watermelons moderately sensitive to waterlogging. Deep roots need good aeration. Yields 30-40 tons/ac. Some increase in diseases especially Fusarium wilt and Phytophthora in wet conditions. Fruit quality good with proper management. Overall suitable with adapted varieties and careful water management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained very challenging for watermelons. Deep tap root development restricted. Yields 20-30 tons/ac. Small fruit with reduced sugar content. Hollow heart increases. Severe disease pressure - Fusarium wilt exacerbated by waterlogging, Phytophthora increases. Economics marginal. Raised beds essential. Consider smaller-fruited types or alternative melons (cantaloupe slightly more tolerant).",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for watermelon production. Tap root cannot develop properly. Yields 12-20 tons/ac. Very small, poor-quality fruit. Severe diseases - Fusarium wilt and Phytophthora devastating in wet conditions. Not economically viable. Watermelons require well-drained soils for quality production, especially deep drainage. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Deep tap root development impossible. Cannot produce marketable melons. Severe diseases universal. Complete failures. Watermelons require excellent deep drainage for the tap root system. Not viable under any circumstances. Do not attempt production."
    },
    
    "Cantaloupe": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for cantaloupe production. Good rooting (2-3 ft) supports quality fruit development. Yields 900+ cartons/ac (25+ tons/ac) possible. Excellent fruit size, sweetness, and firmness. Minimal disease pressure especially Phytophthora and Fusarium wilt. Good netting and slip characteristics. Premium market quality and shelf life.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for cantaloupes. Minor limitations. Cantaloupes moderately sensitive to waterlogging but MORE tolerant than watermelons. Yields 650-900 cartons/ac. Some increase in Fusarium wilt and Phytophthora. Overall suitable for commercial production with proper varieties and management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for cantaloupes. Significant limitations. Reduced vine vigor. Yields 450-650 cartons/ac. Small fruit with reduced sugar content and firmness. Fusarium wilt severe - disease pressure increases dramatically in wet soils. Poor shelf life. Economics marginal. Raised beds beneficial. Cantaloupes MORE viable than watermelons at this level but still challenging.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial cantaloupe production. Poor vine growth. Yields 300-450 cartons/ac. Small, poor-quality fruit. Fusarium wilt devastating. Other diseases severe. Not economically viable. While slightly more tolerant than watermelons, cantaloupes still require reasonable drainage for quality production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot establish healthy vines. Severe diseases. Minimal fruit production. Melons generally require good drainage. Complete failures common. Not viable under any circumstances. Do not attempt production."
    },
    
    "Snap Beans": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for snap bean production. Good rooting and nodulation require excellent aeration. Yields 7+ tons/ac possible. Excellent pod quality, tenderness, and color. Strong nodulation and N-fixation. Minimal disease pressure especially white mold and root rots. Multiple harvests on pole types. Premium market quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for snap beans. Minor limitations. Beans moderately sensitive to waterlogging - affects nodulation. Yields 5-7 tons/ac. Some increase in white mold and root rots during wet periods. Nodulation reduced slightly. Overall suitable for commercial production with proper varieties.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for snap beans. Snap beans MORE sensitive than dry beans to poor conditions. Poor nodulation limits N-fixation. Yields 3-5 tons/ac. Tough, poorly colored pods. White mold and root rot severe. Economics marginal. Bush types MORE tolerant than pole types. Raised beds beneficial. Consider alternative vegetables less sensitive.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for quality snap bean production. Cannot achieve good nodulation. Poor pod production and quality. Yields 2-3 tons/ac. Severe diseases. Unmarketable quality. Not economically viable. Snap beans quite waterlogging-sensitive. Require well-drained soils for quality production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Legumes require aerobic conditions for nodulation. Cannot establish or produce. Complete failures. Snap beans very sensitive to waterlogging. Not viable under any circumstances. Do not attempt production."
    },
    
    "Peas": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for pea production. Good rooting and nodulation. Yields 4+ tons/ac fresh weight possible. Excellent pod fill and sweetness. Strong N-fixation. Minimal disease pressure. Premium quality for fresh market or processing. Cool-season growth pattern benefits from good drainage.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for peas. Minor limitations. Peas moderately tolerant of brief saturation during cool season. Good nodulation. Yields 3-4 tons/ac. Some increase in root rots if prolonged wet conditions. Overall suitable for commercial production. English peas, snap peas, and snow peas all perform well.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for peas. Peas MORE tolerant than beans of imperfect drainage - good legume choice at moderate drainage. Yields 2-3 tons/ac. Nodulation adequate. Some disease increase but manageable. Pod quality acceptable. Still economically viable. Better choice than snap beans at this drainage level. Austrian winter peas (field type) very tolerant.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits pea production but less than beans. Peas among more waterlogging-tolerant legumes. Yields 1-2 tons/ac. Nodulation reduced. Disease pressure increases. Pod quality suffers. Economics marginal for garden peas. Field peas (Austrian winter peas) MORE tolerant - better choice at this level. If growing legume vegetables on poorly drained soil, peas better than beans.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for tolerant peas. Yields <1 ton/ac. Poor quality. Legumes require reasonable aeration for nodulation. While peas more tolerant than many legumes, extreme poor drainage still prevents economic production. Not recommended."
    },
    
    "Sweet Corn": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ideal for sweet corn. Same requirements as field corn - extensive root system (5-6 ft). Yields 250+ dozen ears/ac possible. Excellent germination, early vigor, and stand. No waterlogging stress. Full kernel fill and tip fill. Disease pressure minimal. Premium market quality for fresh or processing.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for sweet corn. Same limitations as field corn. Occasional delays tolerable. Yields 180-250 dozen ears/ac. Some disease increase in wet conditions. Overall suitable for commercial production. Sweet corn same drainage sensitivity as field corn.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for sweet corn. Same significant limitations as field corn. Restricted rooting. Yields 120-180 dozen ears/ac. Small ears with poor tip fill. Disease pressure increases. Economics marginal. Sweet corn has same drainage requirements as field corn - not more tolerant despite shorter season.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for sweet corn. Same severe limitations as field corn. Cannot establish good stands. Yields 80-120 dozen ears/ac. Poor ear quality. Severe diseases. Not economically viable. Sweet corn requires well-drained soils just like field corn. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot produce sweet corn. Same complete failure as field corn. Not viable under any circumstances. Sweet corn has identical drainage requirements to field corn - among highest of vegetable crops. Do not attempt production."
    },
    
    "Spinach": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for spinach production. Very shallow root system (6-12 inches) requires good surface aeration. Yields 8+ tons/ac possible. Rapid growth and tender leaves. Excellent color and quality. No waterlogging stress. Minimal disease pressure especially downy mildew. Multiple succession plantings or cut-and-come-again harvests possible.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for spinach. Minor limitations. Shallow roots fairly sensitive to waterlogging. Brief saturation tolerable during cool season. Yields 6-8 tons/ac. Some increase in diseases during wet periods. Overall suitable for commercial production with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for spinach. Very shallow roots sensitive to poor surface drainage. Slow growth. Yields 4-6 tons/ac. Disease pressure increases - downy mildew and white rust worse in wet conditions. Leaf quality variable - may be tough or yellowed. Economics marginal. Raised beds beneficial. Baby leaf production more successful than large leaf.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for quality spinach. Shallow roots extremely sensitive. Poor growth. Yields 2-4 tons/ac. Severe disease pressure. Yellowed, tough leaves. Bitter taste. Not economically viable. Spinach requires good surface drainage for quality production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Very shallow root system among most waterlogging-sensitive. Cannot establish or grow. Severe diseases. Complete failures. Not viable under any circumstances. Do not attempt spinach production."
    },
    
    "Kale": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for kale production. Good rooting supports extended harvest period. Yields 20+ tons/ac fresh weight over season possible. Excellent leaf quality, tenderness, and color. No waterlogging stress. Minimal disease pressure. Multiple harvests over several months. Premium quality for fresh market.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for kale. Minor limitations. Kale moderately tolerant of brief saturation - brassica with good waterlogging tolerance. Yields 15-20 tons/ac. Some disease increase but manageable. Overall suitable for commercial production. Good choice among brassicas for moderately well-drained soils.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for kale. Kale MOST tolerant common brassica to poor drainage. Better choice than cabbage, broccoli, cauliflower at moderate drainage. Yields 10-15 tons/ac. Leaves tougher and more fibrous. Some disease pressure but kale more resistant. Still economically viable. Strong recommendation for poorly drained brassica production. Consider collards (even more tolerant).",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits kale but less than other brassicas. Kale among MOST waterlogging-tolerant brassicas. Yields 6-10 tons/ac. Tough leaves. Disease pressure increases but kale resistant. If growing brassicas on poorly drained soils, kale or collards ONLY viable choices. Still produces where others fail. Economics marginal but possible with proper management.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for kale. Yields <6 tons/ac. While most tolerant common brassica, even kale has limits. Clubroot severe in poorly drained acid soils. Among brassicas, kale and collards last to fail but extreme poor drainage still prevents economic production. Not recommended."
    },
    
    # ========================================================================
    # FRUIT & NUT CROPS
    # ========================================================================
    
    "Apples": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for apple orchards. Apples very sensitive to waterlogging throughout 30+ year orchard life. Deep rooting (8-12 ft potential) requires well-aerated profile. Yields 600-1,000 bu/ac possible. Excellent tree vigor and longevity. No root death from saturation. Minimal disease pressure especially Phytophthora root rot. No winter injury from ice sheeting. This drainage level non-negotiable for commercial orchards.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for apples. Apples quite waterlogging-sensitive - even minor limitations problematic for long-lived orchard. Brief saturation tolerable only if infrequent. Yields 400-600 bu/ac. Tree longevity reduced (20-25 years vs 30+). Some root death during prolonged wet periods. Increased Phytophthora root rot. Winter injury risk increases if roots saturated before freezing. Many apple regions require excellent drainage as baseline.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial apple orchards. Apples cannot tolerate poor drainage. Poor tree establishment. Stunted growth. Yields <400 bu/ac. Severe Phytophthora root rot - major disease of apples in wet soils. Tree decline and death common. Orchard life shortened to 10-15 years. Not economically viable for 30-year investment. Do not establish new orchards without drainage improvements. Consider dwarfing rootstocks on raised mounds as last resort.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for apple production. Young trees fail to establish or die within few years. Mature trees show severe decline. Phytophthora root rot universal and fatal. Cannot achieve commercial production. Not viable for orchard establishment. Apple production requires well-drained soils - fundamental industry requirement. Do not attempt without major drainage bringing soil to at least moderate drainage class.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Apples among most waterlogging-sensitive tree fruits. Tree death universal. Cannot establish orchards. Multi-decade investment requires excellent soil drainage from start. Not economically feasible to attempt drainage for apples on very poorly drained sites. Consider entirely different land uses."
    },
    
    "Peaches": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for peach production. Peaches EXTREMELY waterlogging-sensitive - most sensitive common tree fruit. Deep rooting requires excellent aeration throughout profile. Yields 300-500 bu/ac possible. Excellent tree health over 12-15 year orchard life. No root asphyxiation. Minimal disease pressure especially Phytophthora and Armillaria root rots. This drainage level absolutely required for peaches.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained highly marginal for peaches. Peaches MORE sensitive than apples to any drainage imperfection. Even brief saturation can kill roots. Yields 250-400 bu/ac with risk. Tree decline accelerated (8-10 year life). Root rots severe even with minor drainage limitations. Many peach regions will not plant on anything less than well-drained soils. Extreme risk for commercial orchard investment.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained completely unsuitable for peaches. Peaches MOST waterlogging-sensitive common tree fruit. Cannot tolerate poor drainage at any growth stage. Young tree failures universal. Mature trees die rapidly. Phytophthora and Armillaria root rots immediately fatal in wet conditions. Not viable under any circumstances. Peach production absolutely requires excellent drainage - non-negotiable industry standard.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained absolutely impossible for peach production. Tree death occurs within first year or two. Peaches' extreme waterlogging sensitivity makes this combination impossible. Do not attempt peach production. Even with extensive drainage, other factors likely prevent success. Peaches require the best drained sites available - sandy loams on slopes ideal. This drainage level eliminates peaches from consideration.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely impossible. Peaches cannot survive any waterlogging. Most sensitive tree fruit crop to poor drainage. Tree death immediate. Not viable under any management or drainage improvements. Do not consider peaches on poorly drained sites under any circumstances."
    },
    
    "Strawberries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for strawberry production. Very shallow root system (6-12 inches) extremely sensitive to waterlogging. Yields 20,000+ lb/ac possible over 2-3 year planting. Excellent plant vigor and survival. No crown rot from saturation. Minimal disease pressure especially red stele and leather rot. Good winter survival - saturated crowns subject to frost heaving and suffocation. Premium fruit quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for strawberries. Strawberries very waterlogging-sensitive due to shallow roots and crown. Brief saturation causes significant problems. Yields 15,000-20,000 lb/ac. Plant survival reduced. Red stele (Phytophthora) increases - major disease in wet soils. Winter injury increases if crowns saturated. Raised beds strongly recommended. Many commercial regions require excellent drainage for strawberries.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial strawberries. Shallow roots and crown cannot tolerate poor drainage. Poor plant establishment and high mortality. Yields 10,000-15,000 lb/ac if plants survive. Red stele and other root/crown rots severe. Winter survival poor. Planting longevity reduced to 1-2 years. Not economically viable for commercial production. Raised beds with imported soil essential. Field production not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for strawberries. Very high plant mortality. Cannot maintain productive stands. Red stele and crown rots universal. Yields <10,000 lb/ac if any crop. Not economically viable. Strawberries require well-drained soils - shallow root system and crown extremely sensitive. Do not attempt field production without complete drainage transformation.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Strawberries among most waterlogging-sensitive fruit crops due to very shallow root system and crown location. Complete plant failures. Cannot establish or survive. Not viable under any circumstances. Strawberries require excellent surface drainage. Do not attempt production."
    },
    
    "Blueberries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for blueberries IF combined with proper acid pH (4.5-5.5). Fibrous shallow root system requires good aeration. Yields 12,000+ lb/ac possible over 20-30 year planting. Excellent bush vigor. No root death from saturation. Minimal Phytophthora root rot. Good winter survival. However, blueberries need consistent moisture - excellent drainage must be combined with irrigation for sustained production.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for blueberries with management. Blueberries have unique requirements - need moisture but also aeration. Shallow fibrous roots moderately sensitive to saturation. Yields 8,000-12,000 lb/ac. Some Phytophthora root rot during extended wet periods. Overall good for blueberry production IF proper acid pH maintained. This drainage level actually preferred by some growers - provides moisture retention with adequate aeration.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for blueberries IF seasonally variable. Blueberries MORE waterlogging-tolerant than most tree fruits. Can handle winter/spring wetness if summer drier. Yields 6,000-8,000 lb/ac. Increased Phytophthora during wet periods. Bush longevity may be reduced. Raised beds beneficial. Drainage improvements helpful but blueberries workable at this level where other fruits fail. Better adapted to imperfect drainage than apples, peaches, or strawberries.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits blueberries significantly but less than other fruits. Blueberries have moderate waterlogging tolerance. Poor bush vigor. Yields <6,000 lb/ac. Phytophthora root rot increases. Bush decline over time. Economics marginal. However, blueberries still among better fruit choices for poorly drained sites. Raised beds essential. Native highbush types somewhat adapted to wet sites. Consider if fruit production needed but not ideal.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for blueberries. While more tolerant than other tree fruits, extreme poor drainage still prevents economic production. Yields negligible. Severe Phytophthora. Bush death. Among fruits, blueberries most tolerant of poor drainage but still has limits. Not economically viable. Consider native wetland shrubs instead."
    },
    
    "Grapes": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for grape production. Deep rooting (10-15+ ft potential) requires well-aerated profile throughout depth. Yields 8-12 tons/ac wine grapes, 15+ tons/ac table grapes possible. Excellent vine health over 25-30+ year vineyard life. No root death from saturation. Minimal disease pressure especially crown gall and Phytophthora. No winter injury from waterlogged soils. Premium wine quality achievable.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for grapes with caution. Grapes moderately sensitive to waterlogging - less than tree fruits but still significant. Brief saturation tolerable. Yields 5-8 tons/ac wine, 12-15 tons/ac table grapes. Some root death during prolonged wet periods. Increased disease pressure especially crown gall and root rots. Vine longevity may be reduced. Many premium wine regions require excellent drainage. Overall acceptable for commercial vineyards.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained marginal for grape production. Significant limitations. Poor vine establishment. Weak growth. Yields 4-6 tons/ac wine, 8-12 tons/ac table grapes. Severe disease pressure - crown gall, Phytophthora, Armillaria increase in wet conditions. Vine decline accelerated. Wine quality suffers. Economics questionable for long-term vineyard investment. Table grapes more challenged than wine grapes. Not recommended for premium wine production.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial grape production. Cannot establish healthy vines. Severe vine decline. Yields <4 tons/ac wine, <8 tons/ac table. Crown gall and root rots severe. Vine death common. Not economically viable for 25-30 year vineyard investment. Grapes require well-drained soils for sustained production. Do not establish vineyards without major drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for grapes. Vine death universal. Cannot establish vineyards. Deep rooting system incompatible with waterlogged soils. Not viable for viticulture. Grapes require excellent drainage for multi-decade production. Do not attempt establishment."
    },
    
    "Almonds": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for almond production. Almonds very sensitive to waterlogging throughout 25+ year orchard life. Deep rooting (15-20 ft) requires well-aerated profile throughout depth. Yields 3,000+ lb/ac possible. Excellent tree health and longevity. No root asphyxiation. Minimal disease pressure especially crown and root rots. No winter injury from saturated soils. This drainage level required for commercial almond production.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for almonds. Almonds quite waterlogging-sensitive. Even brief saturation problematic. Yields 2,200-3,000 lb/ac with risk. Tree vigor reduced. Increased disease pressure especially crown rot. Tree longevity shortened. Many California almond regions (where most US production occurs) will not plant on anything less than well-drained soils. High risk for orchard investment. Excellent drainage strongly preferred.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial almond production. Almonds cannot tolerate poor drainage. Young tree failures common. Mature trees show severe decline. Crown and root rots severe. Yields <2,200 lb/ac if trees survive. Orchard life drastically shortened. Not economically viable for 25+ year investment. Do not establish almond orchards without drainage bringing soil to at least moderately well-drained class.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for almonds. Tree death occurs within first few years. Almonds very waterlogging-sensitive. Cannot establish viable orchards. Crown rot and root rots fatal. Not viable under any circumstances. Almond production requires excellent drainage - industry standard. Do not attempt establishment.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely impossible for almonds. Complete tree failures. Among most waterlogging-sensitive tree nut crops. Multi-decade investment requires excellent soil drainage from start. Not economically feasible to attempt. Do not consider almonds on poorly drained sites."
    },
    
    "Walnuts": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for walnut production. Walnuts moderately sensitive to waterlogging over 50+ year orchard life. Very deep rooting (15-20+ ft) requires aerated profile. Yields 3,000-4,000 lb in-shell/ac possible. Excellent tree health and longevity. Minimal crown and root rot. No winter injury from saturated conditions. Optimal for long-term walnut production.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable for walnuts. Walnuts LESS waterlogging-sensitive than almonds or peaches but still significant. Brief saturation tolerable if soil drains. Yields 2,500-3,500 lb/ac. Some disease increase especially crown rot on susceptible rootstocks. Tree vigor generally good. Overall suitable for commercial walnut production with proper rootstock selection (Paradox rootstock more tolerant than others).",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained marginal for walnut production. Significant limitations for 50+ year investment. Young tree establishment slower. Yields 1,800-2,500 lb/ac. Disease pressure increases - crown rot on susceptible rootstocks. Paradox rootstock somewhat tolerant but still challenged. Tree longevity may be reduced. Economics questionable for multi-generational investment. Not recommended without drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial walnut production. Poor tree establishment and growth. Severe crown rot even on tolerant rootstocks. Yields <1,800 lb/ac. Tree decline and death. Not economically viable for 50+ year orchard. Walnuts require reasonable drainage for sustained production. Do not establish orchards without extensive drainage improvements.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for walnuts. Tree death common. Cannot maintain productive orchards. Not viable for 50-75 year investment. Multi-generational crop requires good soil drainage. Do not attempt establishment on very poorly drained sites."
    },
    
    "Pecans": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for pecan production. Very deep rooting (15-20+ ft) requires excellent aeration throughout profile. Yields 2,000+ lb in-shell/ac possible over 75+ year orchard life. Excellent tree health and longevity. Minimal disease pressure. No root death from saturation. Optimal for multi-generational pecan production. Premium nut quality and fill.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for pecans with caution. Pecans moderately sensitive to waterlogging. Brief saturation tolerable especially if seasonal. Yields 1,500-2,000 lb/ac. Some disease increase during wet periods. Tree vigor generally good. Many pecan regions have seasonal flooding in bottomlands - trees adapted to brief winter flooding but require good drainage during growing season. Overall acceptable for commercial production.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained marginal for pecan production. Pecans MORE tolerant of seasonal wetness than many tree nuts (native to river bottoms in some regions) but still need good drainage during growing season. Yields 1,000-1,500 lb/ac. Disease pressure increases. Nut fill and quality reduced. Tree longevity uncertain. Economics questionable for 75+ year investment. Consider site-specific evaluation - some bottomland pecans tolerate seasonal flooding.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial pecan production. While pecans tolerate brief seasonal flooding better than almonds or walnuts, prolonged poor drainage prevents economic production. Poor tree growth. Yields <1,000 lb/ac. Disease pressure severe. Not economically viable for multi-generational 75+ year orchard. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for flood-tolerant pecans. Permanent or near-permanent saturation prevents tree establishment and survival. Cannot maintain productive orchards. While pecans more waterlogging-tolerant than many nuts, extreme poor drainage still incompatible with 75-100 year production cycle. Not viable."
    },
    
    "Citrus": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for citrus production. Citrus EXTREMELY waterlogging-sensitive - among most sensitive tree fruits. Shallow to moderate rooting (3-6 ft depending on rootstock) requires excellent aeration. Yields vary by type (oranges 400-600 boxes/ac, lemons 800-1,200 boxes/ac) possible. Excellent tree health over 25-50+ year orchard life. No root death from saturation. Minimal Phytophthora - major citrus disease in wet soils. This drainage level required.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained highly marginal for citrus. Citrus MORE waterlogging-sensitive than most tree fruits. Even minor saturation causes severe problems. Phytophthora root rot increases dramatically. Tree decline rapid. Yields significantly reduced. Many citrus regions will not plant on anything less than perfectly drained soils. Florida citrus traditionally on well-drained ridges and raised beds. High risk for commercial orchard.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained completely unsuitable for citrus. Citrus cannot tolerate poor drainage at any level. Phytophthora root rot universal and rapidly fatal in wet conditions. Young tree death within first few years. Mature trees show rapid decline. Not viable under any circumstances. Citrus production absolutely requires excellent drainage - industry standard worldwide. Do not attempt establishment.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained absolutely impossible for citrus production. Tree death occurs rapidly. Citrus' extreme waterlogging sensitivity makes this impossible. Phytophthora immediately fatal. Cannot establish orchards. Not viable under any management. Citrus requires excellent drainage - among most demanding tree fruits. Do not consider citrus on poorly drained sites.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely impossible for citrus. Among most waterlogging-sensitive commercial tree crops. Complete failures universal. Not viable under any circumstances. Multi-decade investment requires excellent drainage from start. Do not attempt."
    },
    
    "Cherries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for cherry production. Cherries EXTREMELY waterlogging-sensitive - comparable to peaches. Deep rooting requires excellent aeration throughout profile. Sweet cherry yields 8-12 tons/ac, tart cherry 4-6 tons/ac possible. Excellent tree health over 20-30 year orchard life. No root asphyxiation. Minimal disease pressure especially crown and root rots. This drainage level required for commercial cherry production.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained highly marginal for cherries. Cherries very waterlogging-sensitive - similar to peaches. Even brief saturation problematic. Tree decline rapid in imperfect drainage. Severe disease pressure - bacterial canker and crown rot increase dramatically. Many cherry regions require perfect drainage. Sweet cherries MORE sensitive than tart cherries. High risk for orchard investment. Excellent drainage strongly preferred.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained completely unsuitable for cherries. Cherries among most waterlogging-sensitive tree fruits. Cannot tolerate poor drainage. Young tree failures universal. Bacterial canker and crown rot fatal in wet conditions. Not viable under any circumstances. Cherry production absolutely requires excellent drainage. Sweet cherries especially demanding. Do not establish orchards without drainage bringing soil to well-drained class.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained absolutely impossible for cherry production. Tree death occurs within first few years. Cherries cannot survive poor drainage. Not viable under any management. Cherry production requires excellent drainage - fundamental requirement. Do not attempt establishment.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely impossible. Cherries among most waterlogging-sensitive tree fruits - comparable to peaches. Complete failures. Not viable under any circumstances. Do not consider cherries on poorly drained sites."
    },
    
    "Pears": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for pear production. Deep rooting (8-12 ft) requires good aeration. Yields 800-1,200 bu/ac possible over 30-40 year orchard life. Excellent tree health and longevity. Minimal disease pressure especially fire blight and crown rot. No winter injury from saturated soils. Premium fruit quality. However, pears MORE waterlogging-tolerant than apples on some rootstocks.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for pears. Pears MODERATELY tolerant of brief saturation - MORE so than apples on adapted rootstocks. Yields 600-1,000 bu/ac. Some disease increase but manageable. Tree longevity good (25-35 years). Overall suitable for commercial pear production. Better choice than apples for sites with minor drainage limitations. Quince rootstocks particularly tolerant.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained marginal for pear production. Pears more tolerant than apples but still challenged. Yields 400-600 bu/ac. Disease pressure increases especially fire blight (exacerbated by wet conditions) and crown rot. Tree vigor reduced. Orchard life shortened. Economics questionable. Consider drainage improvements. Pears workable where apples would fail but still not ideal.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial pear production. While more tolerant than apples, poor drainage still prevents economic production. Severe disease pressure. Tree decline. Yields <400 bu/ac. Not economically viable for long-term orchard. Pears require reasonable drainage for sustained production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for tolerant pears. Cannot maintain healthy trees. Tree death. While more waterlogging-tolerant than apples, extreme poor drainage still prevents economic production. Not viable for orchard establishment."
    },
    
    "Raspberries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained essential for raspberry production. Very shallow root system (12-18 inches) extremely sensitive to waterlogging. Yields 6,000-10,000 lb/ac possible over 8-12 year planting. Excellent cane vigor. No root or crown rot. Minimal disease pressure especially Phytophthora root rot - devastating to raspberries. Good winter survival. Premium berry quality.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for raspberries. Raspberries very waterlogging-sensitive due to shallow roots. Brief saturation causes significant problems. Yields 4,000-6,000 lb/ac. Phytophthora root rot increases - major raspberry disease in wet soils. Cane vigor reduced. Planting longevity shortened. Raised beds strongly recommended. Many commercial regions require excellent drainage for raspberries.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial raspberries. Shallow roots cannot tolerate poor drainage. Poor cane establishment. High mortality. Yields 2,000-4,000 lb/ac if plants survive. Phytophthora root rot severe and often fatal. Winter survival poor. Not economically viable for field production. Raised beds with imported soil essential. Field production not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for raspberries. Very high plant mortality. Cannot maintain productive plantings. Phytophthora root rot universal and rapidly fatal. Yields <2,000 lb/ac if any. Not economically viable. Raspberries require excellent drainage - shallow root system extremely sensitive. Do not attempt field production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Raspberries among most waterlogging-sensitive berry crops. Complete plant failures. Cannot establish or survive. Not viable under any circumstances. Raspberries require excellent surface drainage. Do not attempt production."
    },
    
    "Blackberries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for blackberry production. Good rooting (18-24 inches) requires excellent aeration. Yields 10,000-15,000 lb/ac possible over 10-15 year planting. Excellent cane vigor and productivity. Minimal disease pressure especially crown gall and root rots. Good winter survival. Premium berry quality. Thornless cultivars and erect types perform well.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for blackberries. Blackberries MODERATELY tolerant of brief saturation - MORE so than raspberries. Yields 8,000-12,000 lb/ac. Some disease increase but manageable with proper varieties. Overall suitable for commercial production. Better choice than raspberries for sites with minor drainage limitations. Trailing types somewhat more tolerant than erect types.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for blackberries with management. Blackberries MORE waterlogging-tolerant than raspberries. Can handle seasonal wetness better. Yields 6,000-10,000 lb/ac. Disease pressure increases but blackberries more resistant than raspberries. Raised beds beneficial. Still economically viable. Better choice than raspberries for moderately drained sites. Wild/native types particularly tolerant.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits blackberries but less than raspberries. Blackberries among more waterlogging-tolerant cane fruits. Yields 4,000-6,000 lb/ac. Disease pressure increases. Cane vigor reduced. Economics marginal for commercial production but better than raspberries at this level. If growing cane fruits on poorly drained soils, blackberries better choice. Wild native types found in wet areas - some tolerance present.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for blackberries. While more tolerant than raspberries, extreme poor drainage still prevents economic production. Yields <4,000 lb/ac. Severe diseases. Among cane fruits, blackberries last to fail but still not economically viable at extreme poor drainage. Not recommended."
    },
    
    "Cranberries": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100) but UNUSUAL for cranberries. Well drained soils NOT typical cranberry situation. Cranberries naturally grow in bogs and wetlands. However, for non-flooded upland culture, good drainage between flooding events beneficial. Cranberries unique among fruits - REQUIRE flooding capability but need drainage between floods. This drainage level good IF can be flooded during harvest and winter. Not typical cranberry site but workable with irrigation infrastructure.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained acceptable for cranberries IF flooding capability exists. Cranberries unique requirement - need seasonal flooding but also adequate drainage for root health during growing season. This level works well for commercial beds with water management. Can alternate flooded/drained conditions. Yields 200-300 barrels/ac (10,000-15,000 lb/ac) possible. Good for constructed cranberry beds with water control.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained GOOD for cranberries if natural water table fluctuates seasonally. Cranberries native to these conditions - wet in winter/spring, drier in summer. Yields 150-250 barrels/ac. Natural cranberry bog conditions. Challenge is controlling water level precisely for optimal production. If can manage flooding and drainage, this is acceptable to good for cranberry culture. Better than excellent drainage without flooding capability.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained acceptable for cranberries if water management possible. Cranberries ADAPTED to wet conditions - among few fruits that benefit from poor drainage. Issue is achieving drainage during growing season for root health. If can lower water table during active growth, poor natural drainage beneficial for water management. Some native bog conditions. Yields 100-200 barrels/ac. Water control critical.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained can work for cranberries IF water level controllable. Cranberries ONLY common fruit actually adapted to very wet conditions. Permanent wetness acceptable during dormancy and harvest flooding. Challenge is lowering water during growing season enough for root health. May require extensive ditching and water control. Natural bog/wetland conditions. Yields variable (80-150 barrels/ac) depending on management. Cranberries unique - poor drainage can be ADVANTAGE if managed."
    },
    
    # ========================================================================
    # SPECIALTY CROPS
    # ========================================================================
    
    "Hops": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for hop production. Hops extremely sensitive to waterlogging throughout 20+ year yard life. Deep rooting (10-15 ft) requires excellent aeration. Perennial crown very sensitive to saturation. Yields 2,500+ lb/ac possible. Excellent bine vigor and cone production. No root or crown rot. Minimal disease pressure especially downy mildew and Verticillium wilt. Premium brewing quality with optimal alpha acids and aromatic compounds.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for hops. Hops very waterlogging-sensitive. Even minor drainage limitations problematic for long-lived perennial planting. Brief saturation causes significant problems. Yields 1,800-2,500 lb/ac with risk. Increased downy mildew and root diseases. Crown rot risk increases. Cone quality and alpha acid content may be reduced. Many hop-growing regions require excellent drainage as baseline. High risk for yard investment.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial hop production. Hops cannot tolerate poor drainage. Poor crown establishment and survival. Weak bine growth. Yields <1,800 lb/ac if plants survive. Severe disease pressure - downy mildew, Verticillium wilt, crown rot. Cone quality poor - cannot meet premium brewing specifications. Not economically viable for 20+ year investment. Do not establish hop yards without drainage improvements.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for hops. Crown rot universal. Cannot maintain perennial plantings. Yields negligible. Hops very waterlogging-sensitive perennial crop. Not viable under any circumstances. Hop production requires excellent drainage - fundamental industry requirement. Do not attempt establishment.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Hops among most waterlogging-sensitive perennial crops. Complete failures. Cannot establish yards. Multi-decade investment requires excellent drainage from start. Not viable under any management. Do not consider hops on poorly drained sites."
    },
    
    "Hemp": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for all hemp types. Deep tap root (4-6 ft) accesses nutrients efficiently with good aeration. Fiber hemp yields 8-10 tons/ac, grain hemp 1,500+ lb/ac, CBD hemp 1,500+ lb/ac floral material possible. Excellent stand establishment. No waterlogging stress. Minimal disease pressure. Premium quality for all markets - fiber length, grain quality, cannabinoid content.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for hemp. Hemp moderately tolerant of brief saturation - MORE so than many crops. Tap root still develops well (3-5 ft). Fiber hemp yields 6-8 tons/ac, grain hemp 1,200-1,500 lb/ac, CBD hemp 1,200-1,500 lb/ac. Occasional field delays tolerable. Some disease increase but manageable. Overall suitable for commercial hemp production. Good crop choice for moderately well-drained soils.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for hemp with management. Hemp MORE waterlogging-tolerant than many crops due to efficient root system. Fiber hemp yields 4-6 tons/ac, grain hemp 800-1,200 lb/ac, CBD hemp 800-1,200 lb/ac. Stand establishment may be challenging. Quality variable. Grain hemp MOST tolerant type, CBD intermediate, fiber most demanding. Hemp better choice than many crops at this drainage level. Economic production still possible.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits hemp significantly but less than most crops. Hemp has reputation for tolerating marginal conditions - some truth here. Fiber hemp <4 tons/ac, grain hemp <800 lb/ac, CBD hemp <800 lb/ac. Stand establishment difficult. Quality issues - short fiber, low cannabinoids. If attempting crops on poorly drained soil, grain hemp among better choices due to tolerance. Economics marginal but hemp more viable than many alternatives.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for hemp. While hemp has moderate waterlogging tolerance, extreme poor drainage prevents economic production. Cannot establish adequate stands. Yields negligible. Quality unmarketable. Hemp's reputation for thriving on marginal land overstated for modern commercial production. Not economically viable."
    },
    
    "Lavender": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for lavender production. Mediterranean crop adapted to dry, well-drained conditions. Very sensitive to waterlogging at all stages. Deep rooting (2-3 ft) requires excellent aeration. Yields 50-100+ lb/ac dried flowers over 10-15 year planting possible. Excellent plant vigor and longevity. No root or crown rot. Minimal disease pressure. Optimal essential oil content and quality. Premium market grades achievable.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for lavender. Lavender adapted to Mediterranean climate with dry summers - very sensitive to wet conditions. Even brief saturation problematic. Yields 30-60 lb/ac. Increased root and crown rot during wet periods. Oil content and quality reduced. Plant longevity shortened (6-10 years). Many lavender regions require excellent drainage on slopes. Raised beds strongly recommended if attempting on level ground.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for lavender production. Lavender cannot tolerate poor drainage - Mediterranean crop requiring dry conditions. Poor plant establishment. High mortality especially in winter. Yields <30 lb/ac if plants survive. Root rot universal. Essential oil content very poor. Not economically viable for commercial production. Lavender requires excellent drainage - fundamental requirement. Not recommended.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for lavender. Mediterranean crops cannot survive wet conditions. Complete plant failures. Winter mortality universal. Cannot maintain perennial plantings. Not viable under any circumstances. Lavender requires well-drained soils on slopes or raised beds. Do not attempt production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Lavender among most waterlogging-sensitive herbs. Mediterranean origin makes it completely incompatible with wet soils. Complete failures. Not viable under any circumstances. Do not consider lavender on poorly drained sites."
    },
    
    "Mint": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained suitable for mint but perhaps 'over-qualified'. Mint MORE waterlogging-tolerant than most herbs. Good rooting (12-18 inches) with rhizomatous spread. Oil mint yields 80-100+ lb oil/ac, spearmint 30-40 lb oil/ac possible over multiple cuts. Excellent stand vigor. However, mint actually tolerates wetter conditions than many crops - excellent drainage not required unlike most herbs.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained OPTIMAL for mint production. Mint moderately tolerant of wet conditions - unusual among herbs. Rhizomatous spreading habit adapted to various conditions. Oil mint yields 60-80 lb oil/ac, spearmint 25-35 lb oil/ac. Good stand establishment and vigor. Disease pressure minimal. This drainage level excellent for commercial mint production. Mint good crop choice for sites too wet for other herbs.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for mint. Mint MORE waterlogging-tolerant than most culinary herbs. Natural habitat includes moist areas. Oil mint yields 40-60 lb oil/ac, spearmint 20-30 lb oil/ac. Stand establishment good. Rhizomes tolerate seasonal wetness. Better crop choice than most herbs at this drainage level. Still economically viable. Consider mint where other herbs would fail.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits mint but less severely than other herbs. Mint among MOST waterlogging-tolerant commercial herbs. Found naturally in moist stream banks and wet meadows. Oil mint yields 25-40 lb oil/ac, spearmint 15-25 lb oil/ac. Stand vigor reduced. Oil content lower. If growing herbs on poorly drained soil, mint BEST choice. Economics marginal but viable where other herbs fail completely.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for mint. While most waterlogging-tolerant commercial herb, extreme poor drainage still limits economic production. Yields <25 lb oil/ac. Stand establishment challenging. Among herbs, mint last to fail but still not economically viable at extreme poor drainage. Consider native wetland plants instead."
    },
    
    "Basil": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for basil production. Good rooting (8-12 inches) for annual herb. Yields 3,000-4,000 lb/ac fresh weight possible with multiple cuts. Excellent plant vigor and leaf quality. No waterlogging stress. Minimal disease pressure especially Fusarium wilt and Pythium. Premium essential oil content. Excellent for fresh market or processing.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for basil. Basil moderately sensitive to waterlogging. Brief saturation tolerable. Yields 2,200-3,000 lb/ac fresh. Some increase in Fusarium wilt and downy mildew during wet periods. Overall suitable for commercial basil production with proper management and disease-resistant varieties.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for basil. Significant limitations. Slow growth. Yields 1,500-2,200 lb/ac. Disease pressure increases - Fusarium wilt, Pythium, downy mildew severe in wet conditions. Leaf quality variable. Essential oil content reduced. Economics marginal for commercial production. Raised beds beneficial. Field production challenging.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for commercial basil. Cannot maintain healthy plants. Severe disease pressure - Fusarium wilt and Pythium universal. Yields <1,500 lb/ac. Poor leaf quality. Not economically viable. Basil requires reasonable drainage for quality production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable. Cannot establish or maintain basil. Severe diseases. Complete failures. Basil quite waterlogging-sensitive for an annual herb. Not viable under any circumstances. Do not attempt production."
    },
    
    "Ginseng": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for ginseng production. Ginseng very sensitive to waterlogging throughout 3-5 year production cycle. Shallow fleshy root (6-10 inches) extremely sensitive to saturation. Yields 2,000-3,000 lb/ac fresh root possible after 3-4 years. Excellent root development and quality. No root rots. Minimal disease pressure especially Phytophthora and Pythium - devastating to ginseng. Premium grades for Asian markets. This drainage level required.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for ginseng. Ginseng very waterlogging-sensitive. Even brief saturation causes severe root rot. Yields 1,500-2,500 lb/ac with high risk. Phytophthora root rot increases dramatically - major cause of ginseng failure. Root quality variable. Many ginseng growers require perfect drainage on sloping woodland sites. High risk for 4-5 year investment. Excellent drainage strongly preferred.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for ginseng production. Ginseng cannot tolerate poor drainage. Root rot universal - Phytophthora and Pythium immediately fatal in wet conditions. Cannot complete 3-5 year production cycle. Yields <1,500 lb/ac if any harvestable root. Not economically viable. Ginseng requires excellent drainage - industry standard. Do not plant without drainage bringing soil to well-drained class.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for ginseng. Complete crop failures within first year or two. Fleshy roots rot immediately in saturated conditions. Not viable under any circumstances. Ginseng among most waterlogging-sensitive specialty crops. Requires well-drained woodland sites with slopes. Do not attempt production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Ginseng cannot survive waterlogged conditions. Among most waterlogging-sensitive crops grown commercially. Complete failures. Multi-year investment requires excellent drainage from start. Not viable under any management. Do not consider ginseng on poorly drained sites."
    },
    
    "Asparagus": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained ESSENTIAL for asparagus production. Asparagus extremely sensitive to waterlogging throughout 15-20 year planting life. Deep crown and extensive root system (5-6 ft deep) require excellent aeration. Yields 3,000-4,000+ lb/ac possible in mature plantings (years 3+). Excellent crown health and longevity. No crown rot. Minimal disease pressure especially Fusarium crown rot. Premium spear quality. This drainage level required for commercial asparagus.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained marginal for asparagus. Asparagus very waterlogging-sensitive perennial. Even minor drainage limitations problematic for long-lived planting. Brief saturation causes crown damage. Yields 2,000-3,000 lb/ac with risk. Crown rot increases - major cause of asparagus decline. Planting longevity reduced (10-12 years). Many asparagus regions require excellent drainage with raised beds. High risk for multi-year investment.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained unsuitable for commercial asparagus. Asparagus cannot tolerate poor drainage. Poor crown establishment. High crown mortality. Yields <2,000 lb/ac if crowns survive. Fusarium crown rot universal - rapidly fatal in wet conditions. Planting fails within 3-5 years. Not economically viable for 15-20 year investment. Asparagus requires excellent drainage - industry standard. Do not plant without major drainage improvements and raised beds.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained completely unsuitable for asparagus. Crown rot universal. Cannot establish viable plantings. Complete failures within 1-2 years. Not viable under any circumstances. Asparagus extremely waterlogging-sensitive perennial. Requires well-drained sandy loam soils, often on raised beds. Do not attempt production.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained absolutely unsuitable. Asparagus among most waterlogging-sensitive perennial vegetables. Deep crown system incompatible with saturated soils. Complete failures. Multi-decade investment requires excellent drainage from start. Not viable under any management. Do not consider asparagus on poorly drained sites."
    },
    
    "Rhubarb": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for rhubarb but not strictly required. Rhubarb MORE waterlogging-tolerant than most perennial vegetables. Deep fleshy crown with moderate rooting (18-24 inches). Yields 12,000-15,000+ lb/ac possible in mature plantings over 10-15 year life. Excellent plant vigor. However, rhubarb actually tolerates wetter conditions than many crops - excellent drainage beneficial but not essential.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained OPTIMAL for rhubarb production. Rhubarb moderately tolerant of seasonal wetness - more so than asparagus or most perennials. Yields 10,000-13,000 lb/ac. Good crown health and productivity. Some disease increase during prolonged wet periods but manageable. Overall excellent for commercial rhubarb. Good choice for sites too wet for asparagus or other sensitive perennials.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for rhubarb. Rhubarb MORE waterlogging-tolerant than most perennial crops. Can handle seasonal wetness reasonably well. Yields 8,000-11,000 lb/ac. Some crown rot during extended wet periods. Planting longevity may be reduced (8-12 years). Still economically viable. Better choice than asparagus for moderately drained sites. Consider rhubarb where other perennials struggle.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits rhubarb but less than most perennials. Rhubarb among more waterlogging-tolerant perennial vegetables. Yields 5,000-8,000 lb/ac. Crown rot increases but rhubarb has some resistance. Plant vigor reduced. If growing perennial vegetables on poorly drained soil, rhubarb better choice than asparagus or artichokes. Economics marginal but viable where others fail.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for rhubarb. While more tolerant than most perennials, extreme poor drainage still prevents economic production. Crown rot severe. Yields <5,000 lb/ac. Among perennial vegetables, rhubarb most tolerant but still has limits. Not economically viable at extreme poor drainage."
    },
    
    "Horseradish": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for horseradish production. Deep fleshy root (12-18 inches) requires good aeration for quality development. Yields 8,000-10,000+ lb/ac possible. Excellent root size, straightness, and pungency. No root rots or defects. Premium grades for fresh market or processing. However, horseradish MORE waterlogging-tolerant than many root crops - excellent drainage beneficial but not essential.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for horseradish. Horseradish moderately tolerant of brief saturation. Yields 6,000-8,000 lb/ac. Good root quality. Some forking or cracking in prolonged wet conditions. Overall suitable for commercial production. Better choice than most root vegetables for sites with minor drainage limitations.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable for horseradish with management. Horseradish MORE waterlogging-tolerant than carrots, parsnips, or other root crops. Yields 4,000-6,000 lb/ac. Root quality variable - more forking and surface defects. Still economically viable. Good choice for root crop production on moderately drained soils where other root vegetables fail.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits horseradish significantly but less than most root crops. Horseradish among more waterlogging-tolerant root vegetables due to vigorous growth. Yields 2,500-4,000 lb/ac. Poor root quality - heavy forking, cracking, some rot. If growing root crops on poorly drained soil, horseradish better choice than carrots, beets, or parsnips. Economics marginal.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for horseradish. Root rots universal. Cannot produce marketable roots. While more tolerant than most root crops, extreme poor drainage still prevents economic production. Not viable."
    },
    
    "Artichokes": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for artichoke production. Deep rooting (3-4 ft) supports perennial crown over 5-10 year planting life. Yields 8,000-12,000 lb/ac possible in mature plantings. Excellent plant vigor and bud production. No root or crown rot. Minimal disease pressure. Premium bud quality and size. Multiple harvests per season in optimal conditions.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for artichokes. Artichokes moderately sensitive to waterlogging. Brief saturation tolerable. Yields 6,000-9,000 lb/ac. Some disease increase during wet periods. Overall suitable for commercial artichoke production. Mediterranean crop preferring good drainage but adaptable to variety of conditions with proper management.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for artichokes. Significant limitations for perennial planting. Poor crown health. Yields 4,000-6,000 lb/ac. Disease pressure increases especially crown rot. Planting longevity reduced (3-5 years). Economics marginal for perennial investment. Annual production system may be better option at this drainage level. Not ideal but possible with intensive management.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for perennial artichoke production. Crown rot severe. Cannot maintain plantings beyond 2-3 years. Yields <4,000 lb/ac. Not economically viable for perennial culture. Consider annual production system if attempting artichokes, but economics still questionable. Artichokes require reasonable drainage for sustained production. Not recommended.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained completely unsuitable for artichokes. Cannot establish or maintain perennial crowns. Crown rot universal. Complete failures. Not viable under any circumstances. Artichokes require well-drained soils for perennial production. Do not attempt."
    },
    
    "Flowers (Cut)": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained optimal for most cut flower species. Good rooting supports quality stem and bloom production. Various species have different requirements but most prefer excellent drainage. No waterlogging stress. Minimal disease pressure especially Pythium, Phytophthora, and bacterial diseases. Premium stem length, bloom size, and vase life. Can grow demanding species like roses, lisianthus, ranunculus.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for many cut flowers. Most annual cut flowers moderately tolerant of brief saturation. Some perennials more sensitive. Good baseline for commercial production. Some disease increase during wet periods but manageable with proper species selection. Overall suitable for diverse cut flower production. Avoid most sensitive species (roses, calla lilies) or use raised beds.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for many cut flowers. Select tolerant species essential. Zinnias, sunflowers, cosmos, marigolds more tolerant. Avoid sensitive species like roses, lisianthus, ranunculus. Disease pressure increases. Stem quality and vase life reduced. Economics variable depending on species selection. Raised beds beneficial for sensitive types. Still viable with appropriate crop selection.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits most cut flower production. Only most tolerant species viable - sunflowers, zinnias, some wildflowers. Premium flowers (roses, peonies, lisianthus, tulips) completely unsuitable. Stem quality poor. Severe disease pressure. Not economically viable for high-value cut flower market. If attempting flowers, focus on most tolerant annuals with raised beds.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable for commercial cut flower production. Cannot grow quality flowers. Severe diseases. Even tolerant species produce unmarketable quality. Not economically viable. Cut flowers generally require reasonable drainage for quality stem production. Not recommended."
    },
    
    "Christmas Trees": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for Christmas tree production over 6-10 year growing cycle. Deep rooting supports healthy tree development. Various species (spruce, fir, pine) perform well. Excellent growth rate, form, and color. No root diseases. Minimal mortality. However, conifers generally adaptable to range of conditions - excellent drainage beneficial but not strictly required for all species.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for most Christmas tree species. Most conifers moderately tolerant of seasonal wetness. Occasional brief saturation tolerable. Good growth and quality. Some species more tolerant than others - pines most adaptable, spruce intermediate, true firs more demanding. Overall good for commercial Christmas tree production with proper species selection.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained acceptable with species selection. PINES (Scotch, white, Virginia) MOST waterlogging-tolerant - excellent choices. Spruce acceptable. Avoid Douglas-fir and true firs (more drainage-sensitive). Slower growth extends production cycle 1-2 years. Tree quality acceptable. Disease pressure increases. Still economically viable with adapted species. Consider tolerant pines for moderately drained sites.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained limits most Christmas tree species. Only most tolerant pines (Virginia pine particularly adapted to wet sites) viable. Spruce and firs unsuitable. Very slow growth (10-12+ year production cycle). High mortality. Poor tree quality and color. Economics marginal. If growing Christmas trees on poorly drained sites, Virginia pine or white pine only choices. Consider alternative land uses.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained unsuitable even for tolerant conifers. High mortality. Cannot achieve marketable trees in reasonable timeframe. While some conifers tolerate wet conditions better than hardwoods, extreme poor drainage still prevents economic production. Consider wetland forestry species or alternative uses instead of Christmas tree production."
    },
    
    "Nursery Stock": {
        "Very High": "Excellent oxygen availability (SQ4: 80-100). Well drained excellent for field-grown nursery stock production. Diverse species have varying requirements but most benefit from good drainage. Container production less dependent on field drainage. Excellent for 1-3 year production cycles. No limitations on species selection. Can grow demanding ornamentals. Premium plant quality for landscape installation.",
        
        "High": "Good oxygen availability (SQ4: 60-79). Moderately well drained suitable for most nursery stock. Many ornamentals moderately tolerant of brief saturation. Good baseline for field production. Some limitations for very sensitive species. Container production excellent regardless of field drainage (if pots not sitting in water). Overall suitable for commercial nursery production with proper species and production system selection.",
        
        "Medium": "Moderate oxygen availability (SQ4: 40-59). Somewhat poorly drained challenging for field-grown nursery stock. Select adapted species essential - native plants and wetland-tolerant ornamentals preferred. Many premium ornamentals unsuitable for field culture. CONTAINER PRODUCTION strongly recommended over field growing at this drainage level - allows complete control of growing media. Field production limited to most tolerant species. Container production still fully viable.",
        
        "Low": "Poor oxygen availability (SQ4: 20-39). Poorly drained unsuitable for field nursery production. Most ornamentals cannot be grown in-ground. CONTAINER PRODUCTION ONLY viable option - field drainage irrelevant if containers elevated or on gravel. If field growing, only wetland-adapted natives viable. Commercial nursery can operate successfully on poorly drained site using exclusively container systems. Many successful nurseries on imperfect sites use containers exclusively.",
        
        "Very Low": "Very poor oxygen availability (SQ4: 0-19). Very poorly drained requires container production systems exclusively. Field growing not viable for any ornamental nursery stock. However, CONTAINER nursery production completely feasible - grow on raised benches, gravel, or pallets. Field drainage does not limit container nursery operations. Can produce full range of species in containers regardless of field conditions. Site preparation (gravel pads, drainage) needed but nursery production viable."
    },
}


def get_sq4_interpretation(crop: str, rating: str) -> str:
    """
    Get the enhanced interpretation for a specific crop and SQ4 rating.
    
    Parameters:
    -----------
    crop : str
        The name of the crop (must match keys in SQ4_INTERPRETATIONS)
    rating : str
        The SQ4 rating (Very High, High, Medium, Low, or Very Low)
    
    Returns:
    --------
    str
        The interpretation text for the specified crop and rating
    
    Raises:
    -------
    KeyError
        If the crop or rating is not found in the lookup table
    """
    if crop not in SQ4_INTERPRETATIONS:
        available_crops = ", ".join(sorted(SQ4_INTERPRETATIONS.keys()))
        raise KeyError(f"Crop '{crop}' not found. Available crops: {available_crops}")
    
    if rating not in SQ4_INTERPRETATIONS[crop]:
        available_ratings = ", ".join(SQ4_INTERPRETATIONS[crop].keys())
        raise KeyError(f"Rating '{rating}' not found for crop '{crop}'. Available ratings: {available_ratings}")
    
    return SQ4_INTERPRETATIONS[crop][rating]


def get_all_crops() -> list:
    """
    Get a list of all available crops in the interpretation table.
    
    Returns:
    --------
    list
        Sorted list of all crop names
    """
    return sorted(SQ4_INTERPRETATIONS.keys())


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
    # Example: Get enhanced interpretation for Corn with Medium rating
    crop_name = "Corn"
    rating_value = "Medium"
    interpretation = get_sq4_interpretation(crop_name, rating_value)
    print(f"\n{crop_name} - {rating_value} SQ4 Rating:")
    print(interpretation)
    print("\n" + "="*80)
    
    # Show all available crops
    print(f"\nTotal field crops in database: {len(get_all_crops())}")
    print("\nAll field crops with SQ4 interpretations:")
    for i, crop in enumerate(get_all_crops(), 1):
        print(f"{i:2d}. {crop}")
    
    print("\n" + "="*80)
    print("SQ4 interpretation features include:")
    print("  • Specific SQ4 score ranges (80-100, 60-79, 40-59, 20-39, 0-19)")
    print("  • Drainage class descriptions and water table depths")
    print("  • Root development limitations by drainage level")
    print("  • Expected yield impacts from poor drainage")
    print("  • Field operation restrictions and timing issues")
    print("  • Disease pressure related to waterlogging")
    print("  • Crop-specific waterlogging sensitivity")
    print("  • Alternative crop recommendations for poor drainage")
    print("  • Economic viability assessments")
    print("  • Management strategies for imperfect drainage")
