"""
Interpretation framework for GAEZ soil quality indices and suitability ratings.

This module provides logic to transform raw SQI scores into meaningful
interpretations with detailed constraint analysis and management recommendations.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from .models import (
    SQIClassification,
    ConstraintSeverity,
    SQIInterpretation,
    LimitingFactor,
    PhaseInterpretation,
    ManagementRecommendation,
    SoilSuitabilityInterpretation,
    InterpretationResponse
)


# =============================================================================
# SQI Metadata and Descriptions
# =============================================================================

SQI_METADATA = {
    'SQ1': {
        'name': 'Nutrient Availability',
        'full_description': 'Natural soil nutrient supply capacity',
        'key_properties': ['Organic carbon', 'pH', 'Total exchangeable bases (TEB)', 'Texture'],
        'input_levels': ['L'],  # Only applies to Low input
        'management_categories': ['Nutrient Management', 'Soil Amendment']
    },
    'SQ2': {
        'name': 'Nutrient Retention',
        'full_description': 'Capacity to retain and supply added nutrients',
        'key_properties': ['Base saturation', 'CEC', 'pH', 'Texture', 'Clay content'],
        'input_levels': ['I', 'H'],  # Applies to Intermediate and High input
        'management_categories': ['Nutrient Management', 'Soil Amendment']
    },
    'SQ3': {
        'name': 'Rooting Conditions',
        'full_description': 'Physical conditions for root development',
        'key_properties': ['Rooting depth', 'Texture', 'Coarse fragments', 'Bulk density', 'Soil phases'],
        'input_levels': ['L', 'I', 'H'],  # Applies to all input levels
        'management_categories': ['Tillage', 'Soil Structure']
    },
    'SQ4': {
        'name': 'Oxygen Availability',
        'full_description': 'Soil aeration and drainage conditions',
        'key_properties': ['Drainage class', 'Water table depth', 'Flooding/ponding frequency'],
        'input_levels': ['L', 'I', 'H'],
        'management_categories': ['Drainage', 'Water Management']
    },
    'SQ5': {
        'name': 'Excess Salts',
        'full_description': 'Limitations from salinity and sodicity',
        'key_properties': ['Electrical conductivity (EC)', 'Exchangeable sodium percentage (ESP)', 'SAR'],
        'input_levels': ['L', 'I', 'H'],
        'management_categories': ['Salinity Management', 'Irrigation', 'Leaching']
    },
    'SQ6': {
        'name': 'Toxicities',
        'full_description': 'Limitations from calcium carbonate and gypsum',
        'key_properties': ['CaCO3 content', 'Gypsum content'],
        'input_levels': ['L', 'I', 'H'],
        'management_categories': ['Soil Amendment', 'Crop Selection']
    },
    'SQ7': {
        'name': 'Workability',
        'full_description': 'Ease of tillage and field operations',
        'key_properties': ['Texture', 'Coarse fragments', 'Bulk density', 'Vertic properties'],
        'input_levels': ['L', 'I', 'H'],
        'management_categories': ['Tillage', 'Equipment Selection']
    }
}


# =============================================================================
# Classification Functions
# =============================================================================

def classify_score(score: float) -> SQIClassification:
    """
    Classify a score (0-100) into suitability categories.

    Args:
        score: SQI or SR score (0-100)

    Returns:
        SQIClassification enum value
    """
    if score >= 80:
        return SQIClassification.EXCELLENT
    elif score >= 60:
        return SQIClassification.GOOD
    elif score >= 40:
        return SQIClassification.MODERATE
    elif score >= 20:
        return SQIClassification.POOR
    else:
        return SQIClassification.VERY_POOR


def score_to_severity(score: float) -> ConstraintSeverity:
    """
    Convert a score to constraint severity level.

    Higher scores = less severe constraints.

    Args:
        score: SQI score (0-100)

    Returns:
        ConstraintSeverity enum value
    """
    if score >= 80:
        return ConstraintSeverity.NONE
    elif score >= 60:
        return ConstraintSeverity.SLIGHT
    elif score >= 40:
        return ConstraintSeverity.MODERATE
    elif score >= 20:
        return ConstraintSeverity.SEVERE
    else:
        return ConstraintSeverity.VERY_SEVERE


def score_to_fao_class(score: float) -> str:
    """
    Convert overall soil rating to FAO suitability class.

    Args:
        score: Soil Rating (SR) score (0-100)

    Returns:
        FAO class string (S1, S2, S3, or N)
    """
    if score >= 80:
        return "S1"  # Highly suitable
    elif score >= 60:
        return "S1"  # Suitable (marginal S1)
    elif score >= 40:
        return "S2"  # Moderately suitable
    elif score >= 20:
        return "S3"  # Marginally suitable
    else:
        return "N"   # Not suitable


# =============================================================================
# Description Generation Functions
# =============================================================================

def generate_sqi_description(sqi_code: str, score: float, input_level: str) -> str:
    """
    Generate a human-readable description for an SQI score.

    Args:
        sqi_code: SQI code (SQ1-SQ7)
        score: SQI score (0-100)
        input_level: Input level (L, I, H)

    Returns:
        Description string
    """
    metadata = SQI_METADATA.get(sqi_code, {})
    name = metadata.get('name', sqi_code)
    classification = classify_score(score)

    # Base descriptions by classification
    descriptions = {
        'SQ1': {
            SQIClassification.EXCELLENT: f"Excellent natural nutrient availability. Soil provides abundant nutrients for plant growth without amendments.",
            SQIClassification.GOOD: f"Good natural nutrient availability. Soil provides adequate nutrients with minor limitations.",
            SQIClassification.MODERATE: f"Moderate natural nutrient availability. Soil requires supplemental nutrients for optimal growth.",
            SQIClassification.POOR: f"Poor natural nutrient availability. Significant nutrient deficiencies require substantial amendments.",
            SQIClassification.VERY_POOR: f"Very poor natural nutrient availability. Severe nutrient limitations significantly constrain crop production."
        },
        'SQ2': {
            SQIClassification.EXCELLENT: f"Excellent nutrient retention capacity. Added fertilizers are efficiently retained and available to crops.",
            SQIClassification.GOOD: f"Good nutrient retention. Most applied nutrients remain available with minor leaching losses.",
            SQIClassification.MODERATE: f"Moderate nutrient retention. Some nutrient losses expected; split applications may be beneficial.",
            SQIClassification.POOR: f"Poor nutrient retention. Significant fertilizer losses; requires careful nutrient management.",
            SQIClassification.VERY_POOR: f"Very poor nutrient retention. Severe leaching and nutrient losses; intensive management required."
        },
        'SQ3': {
            SQIClassification.EXCELLENT: f"Excellent rooting conditions. Deep, well-structured soil supports unrestricted root development.",
            SQIClassification.GOOD: f"Good rooting conditions. Minor physical limitations; roots can access adequate soil volume.",
            SQIClassification.MODERATE: f"Moderate rooting conditions. Physical constraints limit effective rooting depth or volume.",
            SQIClassification.POOR: f"Poor rooting conditions. Significant physical barriers restrict root development and water/nutrient uptake.",
            SQIClassification.VERY_POOR: f"Very poor rooting conditions. Severe physical limitations greatly restrict root growth and crop potential."
        },
        'SQ4': {
            SQIClassification.EXCELLENT: f"Excellent oxygen availability. Well-drained soil provides optimal aeration for root respiration.",
            SQIClassification.GOOD: f"Good oxygen availability. Adequate drainage with minor seasonal limitations.",
            SQIClassification.MODERATE: f"Moderate oxygen availability. Periodic waterlogging may limit crop growth during wet periods.",
            SQIClassification.POOR: f"Poor oxygen availability. Frequent waterlogging restricts root growth and crop selection.",
            SQIClassification.VERY_POOR: f"Very poor oxygen availability. Persistent waterlogging severely limits crop production."
        },
        'SQ5': {
            SQIClassification.EXCELLENT: f"No excess salt problems. Soil is free from salinity and sodicity constraints.",
            SQIClassification.GOOD: f"Minor salt concerns. Low levels of salinity or sodicity with minimal crop impact.",
            SQIClassification.MODERATE: f"Moderate salt problems. Salinity or sodicity affects sensitive crops; management required.",
            SQIClassification.POOR: f"Significant salt problems. High salinity or sodicity restricts crop options and requires remediation.",
            SQIClassification.VERY_POOR: f"Severe salt problems. Very high salinity or sodicity severely limits agricultural use."
        },
        'SQ6': {
            SQIClassification.EXCELLENT: f"No calcium carbonate or gypsum limitations. Optimal conditions for most crops.",
            SQIClassification.GOOD: f"Minor calcium carbonate or gypsum presence. Slight impact on nutrient availability.",
            SQIClassification.MODERATE: f"Moderate calcium carbonate or gypsum levels. May affect nutrient availability and soil structure.",
            SQIClassification.POOR: f"High calcium carbonate or gypsum content. Causes nutrient deficiencies and structural issues.",
            SQIClassification.VERY_POOR: f"Very high calcium carbonate or gypsum. Severe limitations from nutrient lockup and soil instability."
        },
        'SQ7': {
            SQIClassification.EXCELLENT: f"Excellent workability. Easy to till with wide operational window.",
            SQIClassification.GOOD: f"Good workability. Minor constraints on tillage operations.",
            SQIClassification.MODERATE: f"Moderate workability. Some limitations on timing or equipment selection for tillage.",
            SQIClassification.POOR: f"Poor workability. Significant constraints on tillage; requires specialized equipment or timing.",
            SQIClassification.VERY_POOR: f"Very poor workability. Severe constraints limit tillage operations and field access."
        }
    }

    sqi_descriptions = descriptions.get(sqi_code, {})
    return sqi_descriptions.get(classification, f"{name} score of {score:.1f} indicates {classification.value} conditions.")


def generate_management_options(sqi_code: str, score: float, input_level: str) -> List[str]:
    """
    Generate management recommendations for a specific SQI.

    Args:
        sqi_code: SQI code (SQ1-SQ7)
        score: SQI score (0-100)
        input_level: Input level (L, I, H)

    Returns:
        List of management recommendation strings
    """
    if score >= 80:
        return []  # No management needed for excellent scores

    options = {
        'SQ1': {
            'moderate': [
                "Apply organic amendments (compost, manure) to increase organic carbon",
                "Consider cover cropping to improve nutrient cycling",
                "Test soil pH and adjust if needed with lime or sulfur"
            ],
            'severe': [
                "Implement intensive organic matter building program",
                "Apply balanced NPK fertilizers based on soil tests",
                "Consider biochar application for long-term carbon building",
                "Use green manures and residue incorporation"
            ]
        },
        'SQ2': {
            'moderate': [
                "Split fertilizer applications to reduce leaching losses",
                "Apply organic matter to improve CEC",
                "Consider slow-release fertilizer formulations"
            ],
            'severe': [
                "Implement intensive CEC improvement program",
                "Apply clay-rich amendments if feasible",
                "Use frequent, small fertilizer applications",
                "Consider foliar feeding for critical nutrients"
            ]
        },
        'SQ3': {
            'moderate': [
                "Deep tillage to break compacted layers",
                "Select crops with appropriate rooting characteristics",
                "Avoid traffic on wet soils to prevent compaction"
            ],
            'severe': [
                "Implement subsoiling program",
                "Consider raised bed systems",
                "Select shallow-rooted crop varieties",
                "Apply gypsum for sodic soil structure improvement"
            ]
        },
        'SQ4': {
            'moderate': [
                "Install drainage systems where feasible",
                "Select crops tolerant of periodic waterlogging",
                "Time operations to avoid wet periods"
            ],
            'severe': [
                "Install comprehensive subsurface drainage",
                "Consider alternative water-tolerant crops",
                "Implement controlled drainage for water table management",
                "Evaluate raised bed or ridge tillage systems"
            ]
        },
        'SQ5': {
            'moderate': [
                "Apply gypsum to improve soil structure and reduce sodicity",
                "Use irrigation management to leach salts below root zone",
                "Select salt-tolerant crop varieties"
            ],
            'severe': [
                "Implement systematic leaching program",
                "Install drainage for salt removal",
                "Apply chemical amendments (gypsum, sulfur)",
                "Consider only highly salt-tolerant crops",
                "Evaluate reclamation economics"
            ]
        },
        'SQ6': {
            'moderate': [
                "Apply acidifying amendments to reduce pH effects",
                "Use chelated micronutrient fertilizers",
                "Select lime-tolerant crop varieties"
            ],
            'severe': [
                "Apply sulfur or acidifying fertilizers",
                "Use foliar micronutrient applications",
                "Select highly tolerant crops (grapes, olives)",
                "Consider economic viability of intensive amendments"
            ]
        },
        'SQ7': {
            'moderate': [
                "Time tillage operations when soil moisture is optimal",
                "Select appropriate tillage equipment",
                "Consider reduced tillage systems"
            ],
            'severe': [
                "Use specialized equipment for difficult soils",
                "Implement no-till or minimum tillage",
                "Plan operations around narrow workability windows",
                "Consider permanent raised beds"
            ]
        }
    }

    severity_key = 'severe' if score < 40 else 'moderate'
    return options.get(sqi_code, {}).get(severity_key, [])


def generate_impact_description(sqi_code: str, score: float) -> str:
    """
    Generate description of how a limiting factor impacts crop production.

    Args:
        sqi_code: SQI code
        score: SQI score

    Returns:
        Impact description string
    """
    severity = score_to_severity(score)
    name = SQI_METADATA.get(sqi_code, {}).get('name', sqi_code)

    impact_templates = {
        ConstraintSeverity.SLIGHT: f"{name} causes minor yield reduction (5-10% potential loss)",
        ConstraintSeverity.MODERATE: f"{name} moderately limits yield (20-30% potential loss)",
        ConstraintSeverity.SEVERE: f"{name} severely limits yield (40-50% potential loss)",
        ConstraintSeverity.VERY_SEVERE: f"{name} very severely limits yield (>60% potential loss)"
    }

    return impact_templates.get(severity, f"{name} constraint present")


# =============================================================================
# Input Level Interpretation
# =============================================================================

def generate_input_level_note(input_level: str) -> str:
    """
    Generate explanatory note about how input level affects interpretation.

    Args:
        input_level: Input level (L, I, H)

    Returns:
        Explanatory note string
    """
    notes = {
        'L': ("Low input interpretation: Assessment assumes subsistence farming with minimal external inputs. "
              "SQ1 (natural nutrient availability) is the primary nutrient factor. Ratings reflect natural "
              "soil fertility without amendments."),
        'I': ("Intermediate input interpretation: Assessment assumes moderate use of fertilizers and amendments. "
              "Both SQ1 and SQ2 contribute equally to nutrient assessment. Ratings reflect potential with "
              "balanced management."),
        'H': ("High input interpretation: Assessment assumes commercial farming with optimal fertilizer use. "
              "SQ2 (nutrient retention) is the primary nutrient factor. Physical constraints (SQ4, SQ7) become "
              "more limiting. Ratings reflect potential with intensive management.")
    }
    return notes.get(input_level, "Standard interpretation")


# =============================================================================
# Phase Interpretation
# =============================================================================

PHASE_IMPACTS = {
    'Stony': {
        'affected_indices': ['SQ3', 'SQ7'],
        'description': "Surface stoniness limits tillage operations and can impede root development."
    },
    'Lithic': {
        'affected_indices': ['SQ3', 'SQ7'],
        'description': "Shallow bedrock severely restricts rooting depth and water storage capacity."
    },
    'Petric': {
        'affected_indices': ['SQ3', 'SQ7'],
        'description': "High coarse fragment content in subsurface limits effective rooting volume."
    },
    'Phreatic': {
        'affected_indices': ['SQ4'],
        'description': "High water table causes waterlogging and reduces oxygen availability to roots."
    },
    'Saline': {
        'affected_indices': ['SQ5'],
        'description': "Elevated salt levels cause osmotic stress and ion toxicity to plants."
    },
    'Sodic': {
        'affected_indices': ['SQ5', 'SQ3'],
        'description': "High sodium causes poor soil structure, reduced infiltration, and crusting."
    },
    'Fragipan': {
        'affected_indices': ['SQ3', 'SQ4'],
        'description': "Dense subsurface layer restricts root penetration and water movement."
    },
    'Duripan': {
        'affected_indices': ['SQ3', 'SQ4'],
        'description': "Cemented hardpan severely restricts root growth and internal drainage."
    },
    'Vertic': {
        'affected_indices': ['SQ3', 'SQ7'],
        'description': "Shrink-swell clay behavior causes structural damage and workability problems."
    },
    'Erosion': {
        'affected_indices': ['SQ1', 'SQ3'],
        'description': "Loss of topsoil reduces nutrient availability and rooting conditions."
    }
}


def interpret_phases(soil_data: pd.DataFrame) -> List[PhaseInterpretation]:
    """
    Generate interpretations for soil phases present in the data.

    Args:
        soil_data: DataFrame with soil phase information

    Returns:
        List of PhaseInterpretation objects
    """
    interpretations = []

    # Check for phase columns in data
    phase_columns = [col for col in soil_data.columns if col.startswith('phase_') or col in PHASE_IMPACTS]

    for phase_name, info in PHASE_IMPACTS.items():
        # Check various ways phases might be indicated
        is_present = False

        # Check direct phase column
        if f'phase_{phase_name.lower()}' in soil_data.columns:
            is_present = soil_data[f'phase_{phase_name.lower()}'].any()
        elif phase_name in soil_data.columns:
            is_present = soil_data[phase_name].any()

        # Only include phases that are present
        if is_present:
            interpretations.append(PhaseInterpretation(
                phase_name=phase_name,
                is_present=True,
                affected_indices=info['affected_indices'],
                impact_description=info['description']
            ))

    return interpretations


# =============================================================================
# Main Interpretation Functions
# =============================================================================

def interpret_single_sqi(
    sqi_code: str,
    score: float,
    input_level: str
) -> SQIInterpretation:
    """
    Generate complete interpretation for a single SQI.

    Args:
        sqi_code: SQI code (SQ1-SQ7)
        score: SQI score (0-100)
        input_level: Input level (L, I, H)

    Returns:
        SQIInterpretation object
    """
    metadata = SQI_METADATA.get(sqi_code, {})

    return SQIInterpretation(
        index_name=metadata.get('name', sqi_code),
        score=score,
        classification=classify_score(score),
        constraint_severity=score_to_severity(score),
        description=generate_sqi_description(sqi_code, score, input_level),
        key_factors=metadata.get('key_properties', []),
        management_options=generate_management_options(sqi_code, score, input_level)
    )


def identify_limiting_factors(
    scores: Dict[str, float],
    input_level: str
) -> List[LimitingFactor]:
    """
    Identify and rank limiting factors from SQI scores.

    Args:
        scores: Dictionary of SQI scores (SQ1-SQ7)
        input_level: Input level (L, I, H)

    Returns:
        List of LimitingFactor objects sorted by severity
    """
    # Determine which SQIs are relevant for this input level
    relevant_sqis = []
    for code, metadata in SQI_METADATA.items():
        if input_level in metadata.get('input_levels', ['L', 'I', 'H']):
            relevant_sqis.append(code)

    # Create limiting factors for relevant SQIs below excellent threshold
    factors = []
    for code in relevant_sqis:
        score = scores.get(code, 100)
        if score < 80:  # Only include if not excellent
            factors.append(LimitingFactor(
                sqi_code=code,
                sqi_name=SQI_METADATA[code]['name'],
                score=score,
                severity=score_to_severity(score),
                impact_description=generate_impact_description(code, score),
                is_primary=False
            ))

    # Sort by score (lowest = most limiting) and mark primary
    factors.sort(key=lambda x: x.score)
    if factors:
        factors[0].is_primary = True

    return factors


def generate_recommendations(
    scores: Dict[str, float],
    limiting_factors: List[LimitingFactor],
    input_level: str
) -> List[ManagementRecommendation]:
    """
    Generate prioritized management recommendations.

    Args:
        scores: Dictionary of SQI scores
        limiting_factors: List of identified limiting factors
        input_level: Input level

    Returns:
        List of ManagementRecommendation objects
    """
    recommendations = []
    priority = 1

    for factor in limiting_factors[:3]:  # Focus on top 3 limiting factors
        options = generate_management_options(factor.sqi_code, factor.score, input_level)
        metadata = SQI_METADATA.get(factor.sqi_code, {})
        categories = metadata.get('management_categories', ['General'])

        for i, option in enumerate(options[:2]):  # Max 2 recommendations per SQI
            recommendations.append(ManagementRecommendation(
                priority=priority,
                category=categories[0] if categories else 'General',
                recommendation=option,
                target_sqi=factor.sqi_code,
                expected_improvement=f"Could improve {factor.sqi_name} by 10-20 points"
            ))
            priority += 1
            if priority > 5:
                break

        if priority > 5:
            break

    return recommendations


def generate_crop_specific_notes(
    crop_id: str,
    crop_name: str,
    scores: Dict[str, float],
    input_level: str
) -> List[str]:
    """
    Generate notes specific to the selected crop.

    Args:
        crop_id: GAEZ crop identifier
        crop_name: Crop common name
        scores: Dictionary of SQI scores
        input_level: Input level

    Returns:
        List of crop-specific note strings
    """
    notes = []

    # Notes based on crop categories
    root_crops = ['9', '10', '11', '47', '48']  # Potato, Sweet Potato, Cassava, Yam, Taro
    if crop_id in root_crops:
        if scores.get('SQ3', 100) < 60:
            notes.append(f"Root crops like {crop_name} are particularly sensitive to rooting constraints. "
                        "Consider raised beds or deep tillage.")
        if scores.get('SQ7', 100) < 60:
            notes.append(f"Workability issues may affect {crop_name} harvest quality and efficiency.")

    cereals = ['1', '2', '3', '4', '5', '6', '7', '8', '38', '39', '40', '41', '49']
    if crop_id in cereals:
        if scores.get('SQ4', 100) < 60:
            notes.append(f"Cereals like {crop_name} are sensitive to waterlogging during establishment "
                        "and grain filling.")

    legumes = ['15a', '15b', '16', '17', '18', '19']
    if crop_id in legumes:
        if scores.get('SQ5', 100) < 60:
            notes.append(f"Legumes like {crop_name} are moderately sensitive to salinity. "
                        "Consider salt-tolerant varieties.")

    # Input level specific notes
    if input_level == 'L' and scores.get('SQ1', 100) < 40:
        notes.append("Low input systems will be significantly limited by poor natural fertility. "
                    "Consider transitioning to intermediate input level with targeted amendments.")

    if input_level == 'H' and scores.get('SQ2', 100) < 60:
        notes.append("High input systems may experience significant fertilizer losses. "
                    "Implement precision nutrient management to improve efficiency.")

    return notes


def generate_suitability_summary(
    sr_score: float,
    classification: SQIClassification,
    limiting_factors: List[LimitingFactor],
    crop_name: str
) -> str:
    """
    Generate a summary statement for overall suitability.

    Args:
        sr_score: Overall soil rating
        classification: Suitability classification
        limiting_factors: List of limiting factors
        crop_name: Crop name

    Returns:
        Summary string
    """
    class_descriptions = {
        SQIClassification.EXCELLENT: f"This soil is highly suitable for {crop_name} production with no significant limitations.",
        SQIClassification.GOOD: f"This soil is suitable for {crop_name} with minor limitations that can be easily managed.",
        SQIClassification.MODERATE: f"This soil has moderate suitability for {crop_name} with constraints that require management attention.",
        SQIClassification.POOR: f"This soil has poor suitability for {crop_name} due to significant constraints requiring intensive management.",
        SQIClassification.VERY_POOR: f"This soil is not suitable for {crop_name} without major remediation or may not be economically viable."
    }

    summary = class_descriptions.get(classification, f"Soil rating: {sr_score:.1f}")

    if limiting_factors:
        primary = limiting_factors[0]
        summary += f" Primary constraint: {primary.sqi_name} ({primary.score:.0f})."

    return summary


def generate_interpretation(
    scores: Dict[str, float],
    input_level: str,
    crop_id: str,
    crop_name: str,
    soil_data: Optional[pd.DataFrame] = None
) -> InterpretationResponse:
    """
    Generate complete interpretation response for soil quality assessment.

    This is the main entry point for the interpretation framework.

    Args:
        scores: Dictionary with SQ1-SQ7 and SR scores
        input_level: Input level (L, I, H)
        crop_id: GAEZ crop identifier
        crop_name: Crop common name
        soil_data: Optional DataFrame with soil properties for phase analysis

    Returns:
        InterpretationResponse with complete interpretation
    """
    # Get overall rating
    sr_score = scores.get('SR', 0)
    overall_classification = classify_score(sr_score)

    # Generate individual SQI interpretations
    sqi_interpretations = {}
    for sqi_code in ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7']:
        score = scores.get(sqi_code, 0)
        sqi_interpretations[sqi_code] = interpret_single_sqi(sqi_code, score, input_level)

    # Identify limiting factors
    limiting_factors = identify_limiting_factors(scores, input_level)

    # Generate phase interpretations if data available
    phase_impacts = []
    if soil_data is not None and len(soil_data) > 0:
        phase_impacts = interpret_phases(soil_data)

    # Generate recommendations
    recommendations = generate_recommendations(scores, limiting_factors, input_level)

    # Generate crop-specific notes
    crop_notes = generate_crop_specific_notes(crop_id, crop_name, scores, input_level)

    # Build primary constraint description
    primary_constraint = None
    secondary_constraints = []
    if limiting_factors:
        primary = limiting_factors[0]
        primary_constraint = f"{primary.sqi_name}: {primary.impact_description}"
        secondary_constraints = [
            f"{f.sqi_name} ({f.score:.0f})"
            for f in limiting_factors[1:3]
        ]

    # Build suitability interpretation
    suitability = SoilSuitabilityInterpretation(
        overall_classification=overall_classification,
        suitability_class=score_to_fao_class(sr_score),
        summary=generate_suitability_summary(sr_score, overall_classification, limiting_factors, crop_name),
        primary_constraint=primary_constraint,
        secondary_constraints=secondary_constraints,
        input_level_note=generate_input_level_note(input_level)
    )

    return InterpretationResponse(
        suitability=suitability,
        sqi_interpretations=sqi_interpretations,
        limiting_factors=limiting_factors,
        phase_impacts=phase_impacts,
        recommendations=recommendations,
        crop_specific_notes=crop_notes
    )
