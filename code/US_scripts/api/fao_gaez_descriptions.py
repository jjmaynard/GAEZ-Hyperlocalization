"""
FAO GAEZ SQ Detailed Descriptions and Crop-Specific Information.

This module provides comprehensive interpretation data derived from FAO GAEZ v4
methodology for Soil Quality Indices SQ1-SQ6.

Based on FAO GAEZ description files: SQ1-SQ6_Description.py
"""

from typing import Dict, List, Tuple

# =============================================================================
# SQ Rating Class Descriptions (0-100 scale interpretations)
# =============================================================================

SQ_RATING_DESCRIPTIONS = {
    'SQ1': {  # Nutrient Availability
        'very_high': {
            'range': (85, 100),
            'title': 'Excellent Natural Nutrient Availability',
            'characteristics': [
                'High organic matter content (>2%)',
                'Optimal or near-optimal pH (6.0-7.5)',
                'High exchangeable bases (>20 cmol(+)/kg)',
                'Favorable texture (medium loam to silt loam)',
                'Minimal nutrient deficiencies or imbalances'
            ],
            'implications': 'Suitable for intensive crop production with minimal inputs. Low fertilizer requirements. Sustainable productivity with good management. Wide range of crop options.'
        },
        'high': {
            'range': (60, 84),
            'title': 'Good Natural Nutrient Availability',
            'characteristics': [
                'Moderate to good organic matter (1.0-2.0%)',
                'Acceptable pH range (5.5-6.0 or 7.5-8.0)',
                'Moderate to high exchangeable bases (10-20 cmol(+)/kg)',
                'Generally favorable texture with minor limitations',
                'Some nutrient deficiencies possible'
            ],
            'implications': 'Suitable for most crops with modest fertilizer inputs. Good response to organic matter additions. Minor amendments may improve productivity. Reliable yields with proper management.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Natural Nutrient Availability',
            'characteristics': [
                'Low to moderate organic matter (0.5-1.0%)',
                'Suboptimal pH (5.0-5.5 or 8.0-8.5)',
                'Low to moderate exchangeable bases (5-10 cmol(+)/kg)',
                'Less favorable texture (sandy or heavy clay)',
                'Multiple moderate nutrient limitations'
            ],
            'implications': 'Requires fertilizer inputs for satisfactory yields. Soil amendments beneficial (lime, organic matter). Crop selection important. Careful nutrient management essential.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Poor Natural Nutrient Availability',
            'characteristics': [
                'Very low organic matter (<0.5%)',
                'Strongly acid or alkaline pH (<5.0 or >8.5)',
                'Low exchangeable bases (<5 cmol(+)/kg)',
                'Unfavorable texture (very sandy or very heavy clay)',
                'Severe nutrient deficiencies or toxicities'
            ],
            'implications': 'Requires intensive fertilizer programs. Major amendments needed (lime, organic matter, micronutrients). Limited crop options. High input costs relative to yields. May be suitable only for adapted species or forestry.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Extremely Poor Nutrient Availability',
            'characteristics': [
                'Essentially no organic matter',
                'Extremely acid or alkaline pH',
                'Very low or no exchangeable bases',
                'Extremely unfavorable texture',
                'Multiple severe nutrient constraints and toxicities'
            ],
            'implications': 'Not suitable for conventional agriculture. Requires major land reclamation efforts. Very high input costs. Poor economic returns. Consider non-agricultural uses.'
        }
    },
    'SQ2': {  # Nutrient Retention Capacity
        'very_high': {
            'range': (80, 100),
            'title': 'Excellent Nutrient Retention',
            'characteristics': [
                'High to very high CEC (>25 cmol(+)/kg)',
                'High clay content (>35%) with high-activity clays',
                'High organic matter (>3%)',
                'Base saturation >50%',
                'Fine to very fine texture throughout profile'
            ],
            'implications': 'Minimal leaching losses. Excellent fertilizer use efficiency. Can apply larger, less frequent fertilizer doses. Low risk of groundwater contamination. Suitable for intensive cropping systems.'
        },
        'high': {
            'range': (60, 79),
            'title': 'Good Nutrient Retention',
            'characteristics': [
                'Moderate to high CEC (15-25 cmol(+)/kg)',
                'Moderate clay content (25-35%) or adequate organic matter',
                'Medium to fine texture',
                'Base saturation 40-60%',
                'Relatively uniform retention in root zone'
            ],
            'implications': 'Good protection against leaching. Efficient fertilizer use. Standard fertilizer management practices work well. Suitable for most agricultural crops.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Nutrient Retention',
            'characteristics': [
                'Moderate CEC (10-15 cmol(+)/kg)',
                'Moderate clay content (15-25%) with low-activity clays',
                'Low to moderate organic matter (1-2%)',
                'Base saturation 30-50%',
                'Sandy loam to loam textures'
            ],
            'implications': 'Moderate leaching risk. Requires careful fertilizer management. Split applications recommended. Slow-release fertilizers beneficial. Organic matter management important.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Poor Nutrient Retention',
            'characteristics': [
                'Low CEC (5-10 cmol(+)/kg)',
                'Low clay content (<15%)',
                'Low organic matter (<1%)',
                'Sandy to sandy loam texture',
                'Often sandy throughout profile'
            ],
            'implications': 'High leaching risk. Rapid nutrient losses with rainfall. Requires intensive management. Multiple small applications necessary. Slow-release fertilizers highly beneficial. High groundwater contamination risk.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Very Poor Nutrient Retention',
            'characteristics': [
                'Very low CEC (<5 cmol(+)/kg)',
                'Very low clay content (<10%)',
                'Very low organic matter (<0.5%)',
                'Sand to loamy sand texture',
                'Often sandy throughout deep profile'
            ],
            'implications': 'Extreme leaching risk. Very rapid nutrient losses. Minimal residual effects. Very poor fertilizer efficiency. Controlled-release or fertigation essential. May not be economically viable for many crops.'
        }
    },
    'SQ3': {  # Rooting Conditions
        'very_high': {
            'range': (80, 100),
            'title': 'Excellent Rooting Conditions',
            'characteristics': [
                'Very deep soil (>150 cm to restrictions)',
                'Low to moderate bulk density (<1.4 g/cm³ in loams)',
                'Well-developed, favorable structure (granular, blocky)',
                'Low mechanical resistance',
                'No or few coarse fragments (<15%)'
            ],
            'implications': 'Unrestricted root penetration to great depth. Suitable for all crop types including deepest-rooted crops. Maximum yield potential. Excellent drought buffering.'
        },
        'high': {
            'range': (60, 79),
            'title': 'Good Rooting Conditions',
            'characteristics': [
                'Deep to very deep (100-150 cm)',
                'Moderate bulk density (1.3-1.5 g/cm³ in loams)',
                'Moderate to well-developed structure',
                'Moderate mechanical resistance',
                'Few to common coarse fragments (15-35%)'
            ],
            'implications': 'Good root penetration to depth. Suitable for most crops. May have minor limitations for deepest-rooted perennials. High yield potential. Good drought resistance.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Rooting Conditions',
            'characteristics': [
                'Moderately deep (50-100 cm to restrictions)',
                'Moderate to high bulk density (1.4-1.6 g/cm³ in loams)',
                'Weak to moderate structure development',
                'Moderate to high mechanical resistance',
                'Common coarse fragments (35-60%) or compact subsoil'
            ],
            'implications': 'Restricted depth of root penetration. Suitable for shallow to medium-rooted crops. Limitations for deep-rooted perennials. Moderate yield potential. Increased drought susceptibility.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Poor Rooting Conditions',
            'characteristics': [
                'Shallow (25-50 cm to restrictions)',
                'High bulk density (>1.6 g/cm³ in loams)',
                'Weak or massive structure',
                'High mechanical resistance',
                'Many to abundant coarse fragments (>60%) or shallow hardpan/rock'
            ],
            'implications': 'Severely restricted rooting depth. Only shallow-rooted crops suitable. Low yield potential without intensive management. High drought susceptibility. Specialized equipment may be needed.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Very Poor Rooting Conditions',
            'characteristics': [
                'Very shallow (<25 cm to restrictions)',
                'Very high bulk density (>1.7 g/cm³)',
                'Structureless, massive',
                'Very high mechanical resistance',
                'Dominant coarse fragments (>90%) or bedrock at/near surface'
            ],
            'implications': 'Rooting essentially prevented or minimal. Unsuitable for conventional agriculture. Extremely low productivity. May require complete soil reconstruction for agriculture.'
        }
    },
    'SQ4': {  # Oxygen Availability
        'very_high': {
            'range': (80, 100),
            'title': 'Excellent Oxygen Availability',
            'characteristics': [
                'Well drained or moderately well drained',
                'Deep water table (>100 cm year-round)',
                'Moderate to rapid permeability',
                'No redoximorphic features above 75 cm',
                'No flooding or ponding'
            ],
            'implications': 'All upland crops thrive. No oxygen-related stress. Maximum root development. Efficient nutrient uptake. Optimal yields achievable.'
        },
        'high': {
            'range': (60, 79),
            'title': 'Good Oxygen Availability',
            'characteristics': [
                'Moderately well drained',
                'Seasonal water table 50-100 cm',
                'Moderate permeability',
                'Few to common redox features 50-100 cm',
                'No flooding, or rare brief flooding'
            ],
            'implications': 'Most upland crops do well. Some deep-rooted crops may have minor limitations. Generally high yields. Occasional stress during wet periods.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Oxygen Availability',
            'characteristics': [
                'Somewhat poorly drained',
                'Water table 30-90 cm seasonally',
                'Slow to moderately slow permeability',
                'Common to many redox features 30-60 cm',
                'Occasional flooding or brief ponding'
            ],
            'implications': 'Moderate crop limitations. Sensitive crops severely affected. Tolerant crops grow satisfactorily. Yield reductions common (10-30%). Drainage improvement beneficial.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Poor Oxygen Availability',
            'characteristics': [
                'Poorly drained',
                'Water table 0-50 cm much of year',
                'Very slow permeability',
                'Many prominent redox features starting shallow (15-30 cm)',
                'Frequent flooding or prolonged ponding'
            ],
            'implications': 'Severe crop limitations. Only tolerant species suitable. Major yield reductions (30-60%). Drainage essential for most crops. Rice and wetland crops suitable.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Very Poor Oxygen Availability',
            'characteristics': [
                'Very poorly drained',
                'Water table at or above surface most of year',
                'Impermeable or nearly so',
                'Dominant gley matrix from surface',
                'Very frequent flooding or permanent ponding'
            ],
            'implications': 'Unsuitable for conventional crops. Only true aquatic/wetland plants. Upland crops impossible. Natural wetland vegetation. Consider wetland crops or conservation uses.'
        }
    },
    'SQ5': {  # Excess Salts
        'very_high': {
            'range': (80, 100),
            'title': 'No Salt Problems',
            'characteristics': [
                'Non-saline (ECe <2 dS/m)',
                'Non-sodic (ESP <6%, SAR <10)',
                'No visible salt accumulation',
                'Normal pH (not affected by sodium)',
                'Good soil structure'
            ],
            'implications': 'All crops suitable regarding salinity. No salt-related limitations. Optimal growing conditions. Standard practices sufficient.'
        },
        'high': {
            'range': (60, 79),
            'title': 'Minor Salt Problems',
            'characteristics': [
                'Very slightly saline (ECe 2-4 dS/m)',
                'Very slightly sodic (ESP 6-10%, SAR 10-13)',
                'Minor localized salt accumulation',
                'pH slightly elevated (7.5-8.5)',
                'Structure beginning to show effects'
            ],
            'implications': 'Most crops perform well. Very sensitive crops may show slight stress. Minor yield reductions (<10%). Monitor salt levels and maintain drainage.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Salt Problems',
            'characteristics': [
                'Moderately saline (ECe 4-8 dS/m)',
                'Moderately sodic (ESP 10-15%, SAR 13-18)',
                'Visible salt accumulation in places',
                'pH elevated (8.0-9.0)',
                'Structure degraded, crusting may occur'
            ],
            'implications': 'Sensitive crops fail or severely reduced. Moderately tolerant crops only. Yield reductions 10-50%. Salt-tolerant crops essential. Leaching and drainage critical.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Severe Salt Problems',
            'characteristics': [
                'Highly saline (ECe 8-16 dS/m)',
                'Highly sodic (ESP 15-25%, SAR 18-26)',
                'Extensive salt crusting',
                'High pH (8.5-10.0)',
                'Severe structural degradation, very poor permeability'
            ],
            'implications': 'Most crops fail. Only tolerant crops viable. Yield reductions 50-90%. Intensive reclamation often needed. May not be economically viable.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Extreme Salt Problems',
            'characteristics': [
                'Very highly saline (ECe >16 dS/m)',
                'Very highly sodic (ESP >25%, SAR >26)',
                'Thick salt crusts',
                'Very high pH (>9.5)',
                'Complete structural collapse, nearly impermeable'
            ],
            'implications': 'Essentially unsuitable for conventional agriculture. Only most extreme halophytes. Reclamation very difficult and expensive. Consider salt-tolerant vegetation or land retirement.'
        }
    },
    'SQ6': {  # Toxicity
        'very_high': {
            'range': (80, 100),
            'title': 'No Toxicity Problems',
            'characteristics': [
                'pH 5.5-8.0 (optimal range)',
                'No aluminum toxicity',
                'Low or no CaCO3 content',
                'Background heavy metal levels only',
                'No manganese toxicity'
            ],
            'implications': 'All crops suitable regarding toxicity. No toxic limitations. Wide crop selection. Optimal growing conditions.'
        },
        'high': {
            'range': (60, 79),
            'title': 'Minor Toxicity Problems',
            'characteristics': [
                'pH 5.0-5.5 or 8.0-8.5 (marginally acid or alkaline)',
                'Low aluminum saturation (<20%)',
                'Slight to moderate CaCO3 content (1-5%)',
                'Minor micronutrient deficiency risk',
                'Occasional Mn elevation'
            ],
            'implications': 'Most crops perform well. Very sensitive crops may be affected. Minor yield reductions possible (<10%). Liming or micronutrient fertilization if needed.'
        },
        'medium': {
            'range': (40, 59),
            'title': 'Moderate Toxicity Problems',
            'characteristics': [
                'pH 4.5-5.0 or >8.5 (strongly acid or alkaline)',
                'Moderate aluminum saturation (20-40%)',
                'Moderate CaCO3 content (5-15%)',
                'Elevated Mn levels (50-100 ppm)',
                'Moderately calcareous with chlorosis risk'
            ],
            'implications': 'Tolerant crops only. Yield reductions 10-40%. Visual toxicity symptoms common. Liming essential for acid soils. Fe chelates for calcareous soils.'
        },
        'low': {
            'range': (20, 39),
            'title': 'Severe Toxicity Problems',
            'characteristics': [
                'pH <4.5 or >9.5 (very strongly acid or alkaline)',
                'High aluminum saturation (40-60%)',
                'High CaCO3 content (15-25%)',
                'High Mn levels (100-200 ppm)',
                'Combined toxicities'
            ],
            'implications': 'Most crops fail or severely stunted. Only very tolerant species viable. Yield reductions 40-80%. Heavy liming or intensive micronutrient programs needed.'
        },
        'very_low': {
            'range': (0, 19),
            'title': 'Extreme Toxicity Problems',
            'characteristics': [
                'pH <4.0 or >10 (extremely acid or alkaline)',
                'Very high aluminum saturation (>60%)',
                'Extremely calcareous (>25% CaCO3)',
                'Severe heavy metal contamination',
                'Multiple severe toxicities'
            ],
            'implications': 'Essentially unsuitable for conventional agriculture. Only most adapted species survive. No economic crop production. May require complete soil removal/replacement.'
        }
    }
}


# =============================================================================
# Crop-Specific Tolerance Information
# =============================================================================

CROP_TOLERANCE = {
    # Aluminum tolerance (for acid soils, SQ6)
    'aluminum': {
        'very_sensitive': ['Alfalfa', 'Sugar beet', 'Cotton', 'Onion', 'Lettuce'],
        'moderately_sensitive': ['Maize', 'Soybeans', 'Wheat', 'Tobacco', 'Potatoes'],
        'moderately_tolerant': ['Oats', 'Rye', 'Rice'],
        'tolerant': ['Cassava', 'Tea', 'Pineapple', 'Blueberry', 'Cowpea']
    },
    # Lime/high pH tolerance (SQ6)
    'lime': {
        'very_sensitive': ['Blueberry', 'Azalea', 'Pin oak', 'Sorghum', 'Soybeans', 'Peach', 'Pear'],
        'sensitive': ['Maize', 'Dry beans', 'Citrus', 'Grape', 'Potato'],
        'moderately_tolerant': ['Wheat', 'Cotton', 'Sugar beet', 'Tomato'],
        'tolerant': ['Alfalfa', 'Barley', 'Safflower', 'Date palm', 'Pistachio', 'Asparagus']
    },
    # Salinity tolerance (SQ5)
    'salinity': {
        'sensitive': ['Beans', 'Carrots', 'Strawberry', 'Avocado', 'Lemon', 'Apple', 'Pear'],
        'moderately_sensitive': ['Maize', 'Rice', 'Soybeans', 'Citrus', 'Peach', 'Potato', 'Tomato'],
        'moderately_tolerant': ['Wheat', 'Sorghum', 'Oats', 'Safflower', 'Sunflower', 'Beet'],
        'tolerant': ['Barley', 'Sugar beet', 'Cotton', 'Date palm', 'Bermudagrass']
    },
    # Drainage/waterlogging sensitivity (SQ4)
    'drainage': {
        'very_sensitive': ['Cotton', 'Alfalfa', 'Onions', 'Carrots', 'Tomatoes', 'Peanuts'],
        'moderately_sensitive': ['Maize', 'Soybeans', 'Wheat', 'Potatoes'],
        'moderately_tolerant': ['Barley', 'Oats'],
        'tolerant': ['Rice', 'Cranberries', 'Taro', 'Willows']
    },
    # Manganese toxicity tolerance (SQ6)
    'manganese': {
        'sensitive': ['Soybeans', 'Dry beans', 'Clover', 'Cucumber', 'Lettuce'],
        'moderately_sensitive': ['Wheat', 'Barley', 'Maize', 'Potato'],
        'tolerant': ['Rice', 'Oats', 'Rye grass', 'Tea']
    }
}


# =============================================================================
# Enhanced Management Strategies
# =============================================================================

DETAILED_MANAGEMENT_STRATEGIES = {
    'SQ1': {
        'medium': [
            'Apply 2-5 tons/acre of organic amendments (compost, manure) to build organic carbon',
            'Test soil pH and apply agricultural lime if pH <5.5 (2-4 tons/acre)',
            'Implement cover cropping with legumes to fix nitrogen and improve nutrient cycling',
            'Use balanced NPK fertilizers based on soil test recommendations',
            'Consider green manures and crop residue incorporation to build organic matter'
        ],
        'low': [
            'Implement intensive organic matter building: 5-10 tons/acre compost annually',
            'Apply heavy lime if acidic: 5-10 tons/acre to raise pH to 6.0-6.5',
            'Use comprehensive fertilizer programs targeting all major nutrients',
            'Consider biochar application (10-20 tons/acre) for long-term carbon building',
            'Rotate with nutrient-accumulating cover crops',
            'May need multiple years of soil building before economic crop production'
        ]
    },
    'SQ2': {
        'medium': [
            'Split fertilizer into 3-4 applications to reduce leaching losses',
            'Apply 2-5 tons/acre organic matter annually to improve CEC',
            'Consider slow-release or coated fertilizer formulations',
            'Implement cover crops to capture leached nutrients',
            'Time applications to match crop demand peaks'
        ],
        'low': [
            'Use controlled-release fertilizers or fertigation systems',
            'Apply 5-10 tons/acre clay-rich amendments if economically feasible',
            'Implement weekly to bi-weekly small fertilizer applications',
            'Consider foliar feeding to supplement soil applications',
            'Use deep-rooted cover crops to capture deeply leached nutrients',
            'Implement conservation practices to prevent further organic matter loss'
        ]
    },
    'SQ3': {
        'medium': [
            'Conduct deep tillage (subsoiling) to break compacted layers when soil is dry',
            'Apply gypsum (1-2 tons/acre) if sodicity contributes to poor structure',
            'Select crops with appropriate rooting depth for soil conditions',
            'Avoid field traffic when soil is wet to prevent further compaction',
            'Consider raised bed systems if shallow restrictions present'
        ],
        'low': [
            'Implement systematic subsoiling program: deep rip to 18-24 inches',
            'Use biological drilling with deep-rooted crops (radish, alfalfa)',
            'Install raised bed systems (12-18 inches) for shallow soils',
            'Select only shallow-rooted crop varieties',
            'Consider rock removal if coarse fragments are the primary limitation',
            'May need specialized equipment for root zone modification'
        ]
    },
    'SQ4': {
        'medium': [
            'Install surface drainage systems: land smoothing, bedding, grassed waterways',
            'Consider subsurface tile drainage (spacing 30-50 ft) if feasible',
            'Select moderately waterlogging-tolerant crop varieties',
            'Time planting and operations to avoid wet periods',
            'Implement controlled drainage for water table management'
        ],
        'low': [
            'Install comprehensive subsurface tile drainage system (15-30 ft spacing, 3-4 ft depth)',
            'Implement extensive surface drainage network',
            'Consider raised bed systems (12-18 inches elevation)',
            'Plant only highly waterlogging-tolerant crops or wetland crops',
            'May need pumping systems if no gravity drainage outlet available',
            'Evaluate economics: drainage costs often $1,000-3,000/acre'
        ]
    },
    'SQ5': {
        'medium': [
            'Apply gypsum (2-5 tons/acre) to ameliorate sodicity and improve structure',
            'Implement 15-30% leaching fraction in irrigation to remove salts',
            'Pre-plant irrigate to leach surface salts before planting',
            'Select moderately salt-tolerant crops and varieties',
            'Ensure adequate drainage to remove leached salts',
            'Monitor soil EC every 1-2 years to track salinity trends'
        ],
        'low': [
            'Install comprehensive subsurface drainage essential for salt removal',
            'Apply 5-20 tons/acre gypsum for sodicity amelioration',
            'Implement systematic leaching: apply 1-3 ft of water annually',
            'Plant only highly salt-tolerant crops (barley, sugar beet, date palm)',
            'May need 3-5 years of reclamation before crop production',
            'Disposal of saline drainage water may be problematic',
            'Consider alternative uses if reclamation not economically viable'
        ]
    },
    'SQ6': {
        'medium': [
            'For acid soils: Apply 2-5 tons/acre agricultural limestone, target pH 6.0-6.5',
            'For calcareous soils: Apply Fe-chelates (EDDHA) at 5-10 lbs/acre',
            'Use acidifying fertilizers (ammonium sulfate) in high pH soils',
            'Apply micronutrient fertilizers based on soil tests',
            'Select crop varieties tolerant to pH extremes',
            'Consider foliar micronutrient sprays for chlorotic crops'
        ],
        'low': [
            'For severe acidity: Apply 5-10+ tons/acre lime over multiple years',
            'For severe lime: Apply 10-50 lbs/acre Fe-EDDHA annually (very expensive)',
            'Attempt acidification with sulfur (500-2000 lbs/acre), but success limited',
            'Select only most tolerant crops: cassava/tea (acid) or alfalfa/barley (lime)',
            'For heavy metal contamination: may require soil removal and replacement',
            'Reclamation may take 5-10+ years and may not be economically viable'
        ]
    },
    'SQ7': {
        'medium': [
            'Time all tillage when soil moisture is optimal (friable condition)',
            'Select tillage equipment appropriate for soil type',
            'Consider reduced tillage or no-till systems to avoid workability issues',
            'Implement controlled traffic farming to limit compaction'
        ],
        'low': [
            'Use specialized equipment designed for difficult soils',
            'Implement no-till or minimum tillage exclusively',
            'Plan all operations around very narrow workability windows',
            'Consider permanent raised bed systems to avoid in-field tillage',
            'May need track-type equipment for wet soils'
        ]
    }
}


def get_rating_class(score: float) -> str:
    """Determine rating class from score."""
    if score >= 85:
        return 'very_high'
    elif score >= 60:
        return 'high'
    elif score >= 40:
        return 'medium'
    elif score >= 20:
        return 'low'
    else:
        return 'very_low'


def get_detailed_description(sqi_code: str, score: float) -> Dict:
    """
    Get detailed FAO GAEZ description for an SQI score.

    Args:
        sqi_code: SQ1-SQ6
        score: Score value (0-100)

    Returns:
        Dictionary with detailed description information
    """
    if sqi_code not in SQ_RATING_DESCRIPTIONS:
        return {}

    rating_class = get_rating_class(score)
    return SQ_RATING_DESCRIPTIONS[sqi_code].get(rating_class, {})


def get_enhanced_management(sqi_code: str, score: float) -> List[str]:
    """
    Get enhanced management recommendations from FAO GAEZ methodology.

    Args:
        sqi_code: SQ1-SQ7
        score: Score value (0-100)

    Returns:
        List of detailed management recommendations
    """
    if score >= 60:  # High or very high - minimal management needed
        return []

    if sqi_code not in DETAILED_MANAGEMENT_STRATEGIES:
        return []

    severity = 'low' if score < 40 else 'medium'
    return DETAILED_MANAGEMENT_STRATEGIES[sqi_code].get(severity, [])


def check_crop_tolerance(crop_name: str, constraint_type: str) -> Tuple[str, str]:
    """
    Check crop tolerance for specific constraint types.

    Args:
        crop_name: Common name of crop
        constraint_type: Type of constraint (aluminum, lime, salinity, drainage, manganese)

    Returns:
        Tuple of (tolerance_level, description)
    """
    if constraint_type not in CROP_TOLERANCE:
        return ('unknown', 'Tolerance information not available')

    tolerance_data = CROP_TOLERANCE[constraint_type]

    for level, crops in tolerance_data.items():
        if any(crop.lower() in crop_name.lower() or crop_name.lower() in crop.lower() for crop in crops):
            level_descriptions = {
                'very_sensitive': f'{crop_name} is very sensitive to {constraint_type} stress',
                'sensitive': f'{crop_name} is sensitive to {constraint_type} stress',
                'moderately_sensitive': f'{crop_name} is moderately sensitive to {constraint_type} stress',
                'moderately_tolerant': f'{crop_name} is moderately tolerant to {constraint_type} stress',
                'tolerant': f'{crop_name} is tolerant to {constraint_type} stress',
                'very_tolerant': f'{crop_name} is highly tolerant to {constraint_type} stress'
            }
            return (level, level_descriptions.get(level, ''))

    return ('unknown', f'Tolerance of {crop_name} to {constraint_type} stress is not well documented')
