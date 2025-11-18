"""
Tests for the interpretation framework.
"""

import pytest
import pandas as pd
from .interpretation import (
    classify_score,
    score_to_severity,
    score_to_fao_class,
    generate_sqi_description,
    generate_management_options,
    generate_impact_description,
    generate_input_level_note,
    interpret_single_sqi,
    identify_limiting_factors,
    generate_recommendations,
    generate_crop_specific_notes,
    generate_suitability_summary,
    generate_interpretation,
    interpret_phases,
    SQI_METADATA
)
from .models import (
    SQIClassification,
    ConstraintSeverity,
    SQIInterpretation,
    LimitingFactor,
    InterpretationResponse
)


class TestClassifyScore:
    """Tests for score classification function."""

    def test_excellent_score(self):
        assert classify_score(100) == SQIClassification.EXCELLENT
        assert classify_score(80) == SQIClassification.EXCELLENT
        assert classify_score(85) == SQIClassification.EXCELLENT

    def test_good_score(self):
        assert classify_score(79) == SQIClassification.GOOD
        assert classify_score(60) == SQIClassification.GOOD
        assert classify_score(70) == SQIClassification.GOOD

    def test_moderate_score(self):
        assert classify_score(59) == SQIClassification.MODERATE
        assert classify_score(40) == SQIClassification.MODERATE
        assert classify_score(50) == SQIClassification.MODERATE

    def test_poor_score(self):
        assert classify_score(39) == SQIClassification.POOR
        assert classify_score(20) == SQIClassification.POOR
        assert classify_score(30) == SQIClassification.POOR

    def test_very_poor_score(self):
        assert classify_score(19) == SQIClassification.VERY_POOR
        assert classify_score(0) == SQIClassification.VERY_POOR
        assert classify_score(10) == SQIClassification.VERY_POOR


class TestScoreToSeverity:
    """Tests for score to severity conversion."""

    def test_no_constraint(self):
        assert score_to_severity(80) == ConstraintSeverity.NONE
        assert score_to_severity(100) == ConstraintSeverity.NONE

    def test_slight_constraint(self):
        assert score_to_severity(60) == ConstraintSeverity.SLIGHT
        assert score_to_severity(79) == ConstraintSeverity.SLIGHT

    def test_moderate_constraint(self):
        assert score_to_severity(40) == ConstraintSeverity.MODERATE
        assert score_to_severity(59) == ConstraintSeverity.MODERATE

    def test_severe_constraint(self):
        assert score_to_severity(20) == ConstraintSeverity.SEVERE
        assert score_to_severity(39) == ConstraintSeverity.SEVERE

    def test_very_severe_constraint(self):
        assert score_to_severity(0) == ConstraintSeverity.VERY_SEVERE
        assert score_to_severity(19) == ConstraintSeverity.VERY_SEVERE


class TestScoreToFaoClass:
    """Tests for FAO suitability class conversion."""

    def test_s1_class(self):
        assert score_to_fao_class(80) == "S1"
        assert score_to_fao_class(100) == "S1"
        assert score_to_fao_class(60) == "S1"

    def test_s2_class(self):
        assert score_to_fao_class(40) == "S2"
        assert score_to_fao_class(59) == "S2"

    def test_s3_class(self):
        assert score_to_fao_class(20) == "S3"
        assert score_to_fao_class(39) == "S3"

    def test_not_suitable(self):
        assert score_to_fao_class(0) == "N"
        assert score_to_fao_class(19) == "N"


class TestGenerateSqiDescription:
    """Tests for SQI description generation."""

    def test_sq1_excellent(self):
        desc = generate_sqi_description('SQ1', 85, 'L')
        assert 'excellent' in desc.lower() or 'Excellent' in desc
        assert 'nutrient' in desc.lower()

    def test_sq1_poor(self):
        desc = generate_sqi_description('SQ1', 25, 'L')
        assert 'poor' in desc.lower() or 'Poor' in desc

    def test_sq4_moderate(self):
        desc = generate_sqi_description('SQ4', 50, 'I')
        assert 'moderate' in desc.lower() or 'Moderate' in desc
        assert 'oxygen' in desc.lower() or 'waterlog' in desc.lower()

    def test_all_sqis_have_descriptions(self):
        for sqi_code in ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7']:
            for score in [90, 65, 45, 25, 10]:
                desc = generate_sqi_description(sqi_code, score, 'L')
                assert isinstance(desc, str)
                assert len(desc) > 10


class TestGenerateManagementOptions:
    """Tests for management options generation."""

    def test_excellent_score_no_options(self):
        options = generate_management_options('SQ1', 85, 'L')
        assert options == []

    def test_moderate_score_has_options(self):
        options = generate_management_options('SQ1', 50, 'L')
        assert len(options) > 0
        assert all(isinstance(opt, str) for opt in options)

    def test_severe_score_has_more_options(self):
        moderate_options = generate_management_options('SQ3', 50, 'L')
        severe_options = generate_management_options('SQ3', 25, 'L')
        assert len(severe_options) >= len(moderate_options)

    def test_all_sqis_have_management_options(self):
        for sqi_code in ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7']:
            options = generate_management_options(sqi_code, 30, 'L')
            assert isinstance(options, list)


class TestInterpretSingleSqi:
    """Tests for single SQI interpretation."""

    def test_returns_sqi_interpretation_object(self):
        interp = interpret_single_sqi('SQ1', 75, 'L')
        assert isinstance(interp, SQIInterpretation)

    def test_interpretation_has_correct_fields(self):
        interp = interpret_single_sqi('SQ3', 45, 'I')
        assert interp.index_name == 'Rooting Conditions'
        assert interp.score == 45
        assert interp.classification == SQIClassification.MODERATE
        assert interp.constraint_severity == ConstraintSeverity.MODERATE
        assert len(interp.description) > 0
        assert len(interp.key_factors) > 0

    def test_management_options_included_for_low_scores(self):
        interp = interpret_single_sqi('SQ5', 30, 'H')
        assert len(interp.management_options) > 0

    def test_no_management_options_for_high_scores(self):
        interp = interpret_single_sqi('SQ2', 90, 'H')
        assert len(interp.management_options) == 0


class TestIdentifyLimitingFactors:
    """Tests for limiting factor identification."""

    def test_returns_list_of_limiting_factors(self):
        scores = {
            'SQ1': 90, 'SQ2': 80, 'SQ3': 50, 'SQ4': 60,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 70
        }
        factors = identify_limiting_factors(scores, 'L')
        assert isinstance(factors, list)
        assert all(isinstance(f, LimitingFactor) for f in factors)

    def test_sorted_by_severity(self):
        scores = {
            'SQ1': 30, 'SQ2': 50, 'SQ3': 70, 'SQ4': 40,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 60
        }
        factors = identify_limiting_factors(scores, 'L')
        if len(factors) > 1:
            for i in range(len(factors) - 1):
                assert factors[i].score <= factors[i + 1].score

    def test_primary_factor_marked(self):
        scores = {
            'SQ1': 30, 'SQ2': 50, 'SQ3': 70, 'SQ4': 40,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 60
        }
        factors = identify_limiting_factors(scores, 'L')
        primary_count = sum(1 for f in factors if f.is_primary)
        assert primary_count == 1
        assert factors[0].is_primary

    def test_excellent_scores_not_included(self):
        scores = {
            'SQ1': 85, 'SQ2': 90, 'SQ3': 80, 'SQ4': 95,
            'SQ5': 88, 'SQ6': 92, 'SQ7': 81
        }
        factors = identify_limiting_factors(scores, 'H')
        assert len(factors) == 0

    def test_input_level_filters_sqis(self):
        scores = {
            'SQ1': 30, 'SQ2': 30, 'SQ3': 70, 'SQ4': 40,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 60
        }
        # For High input, SQ1 should not be included
        factors_h = identify_limiting_factors(scores, 'H')
        sq1_in_h = any(f.sqi_code == 'SQ1' for f in factors_h)
        # SQ1 is only for Low input
        assert not sq1_in_h


class TestGenerateRecommendations:
    """Tests for recommendation generation."""

    def test_returns_recommendations(self):
        scores = {
            'SQ1': 30, 'SQ2': 50, 'SQ3': 70, 'SQ4': 40,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 60
        }
        factors = identify_limiting_factors(scores, 'L')
        recommendations = generate_recommendations(scores, factors, 'L')
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0

    def test_recommendations_have_priority(self):
        scores = {
            'SQ1': 30, 'SQ2': 50, 'SQ3': 25, 'SQ4': 40,
            'SQ5': 85, 'SQ6': 90, 'SQ7': 60
        }
        factors = identify_limiting_factors(scores, 'L')
        recommendations = generate_recommendations(scores, factors, 'L')
        priorities = [r.priority for r in recommendations]
        assert all(1 <= p <= 5 for p in priorities)

    def test_max_five_recommendations(self):
        scores = {
            'SQ1': 10, 'SQ2': 20, 'SQ3': 15, 'SQ4': 25,
            'SQ5': 30, 'SQ6': 35, 'SQ7': 40
        }
        factors = identify_limiting_factors(scores, 'L')
        recommendations = generate_recommendations(scores, factors, 'L')
        assert len(recommendations) <= 5


class TestGenerateCropSpecificNotes:
    """Tests for crop-specific note generation."""

    def test_root_crop_rooting_notes(self):
        scores = {'SQ1': 80, 'SQ2': 80, 'SQ3': 40, 'SQ4': 80, 'SQ5': 80, 'SQ6': 80, 'SQ7': 80}
        notes = generate_crop_specific_notes('9', 'White Potato', scores, 'L')
        assert any('root' in note.lower() for note in notes)

    def test_legume_salinity_notes(self):
        scores = {'SQ1': 80, 'SQ2': 80, 'SQ3': 80, 'SQ4': 80, 'SQ5': 40, 'SQ6': 80, 'SQ7': 80}
        notes = generate_crop_specific_notes('15a', 'Soybean', scores, 'L')
        assert any('salt' in note.lower() for note in notes)

    def test_low_input_fertility_notes(self):
        scores = {'SQ1': 30, 'SQ2': 80, 'SQ3': 80, 'SQ4': 80, 'SQ5': 80, 'SQ6': 80, 'SQ7': 80}
        notes = generate_crop_specific_notes('4', 'Maize', scores, 'L')
        assert any('input' in note.lower() or 'fertility' in note.lower() for note in notes)


class TestGenerateInputLevelNote:
    """Tests for input level note generation."""

    def test_low_input_note(self):
        note = generate_input_level_note('L')
        assert 'low input' in note.lower()
        assert 'SQ1' in note

    def test_intermediate_input_note(self):
        note = generate_input_level_note('I')
        assert 'intermediate' in note.lower()
        assert 'SQ1' in note and 'SQ2' in note

    def test_high_input_note(self):
        note = generate_input_level_note('H')
        assert 'high input' in note.lower()
        assert 'SQ2' in note


class TestGenerateInterpretation:
    """Tests for the main interpretation generation function."""

    @pytest.fixture
    def sample_scores(self):
        return {
            'SQ1': 65, 'SQ2': 70, 'SQ3': 45, 'SQ4': 80,
            'SQ5': 90, 'SQ6': 85, 'SQ7': 55, 'SR': 52
        }

    def test_returns_interpretation_response(self, sample_scores):
        interp = generate_interpretation(
            scores=sample_scores,
            input_level='I',
            crop_id='4',
            crop_name='Maize'
        )
        assert isinstance(interp, InterpretationResponse)

    def test_has_all_sqi_interpretations(self, sample_scores):
        interp = generate_interpretation(
            scores=sample_scores,
            input_level='L',
            crop_id='1',
            crop_name='Wheat'
        )
        assert len(interp.sqi_interpretations) == 7
        for code in ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7']:
            assert code in interp.sqi_interpretations

    def test_has_suitability_interpretation(self, sample_scores):
        interp = generate_interpretation(
            scores=sample_scores,
            input_level='H',
            crop_id='4',
            crop_name='Maize'
        )
        assert interp.suitability is not None
        assert interp.suitability.overall_classification == SQIClassification.MODERATE
        assert interp.suitability.suitability_class == "S2"

    def test_has_limiting_factors(self, sample_scores):
        interp = generate_interpretation(
            scores=sample_scores,
            input_level='L',
            crop_id='4',
            crop_name='Maize'
        )
        assert len(interp.limiting_factors) > 0
        # SQ3 should be primary limiting factor (score=45)
        primary = next(f for f in interp.limiting_factors if f.is_primary)
        assert primary.sqi_code == 'SQ3'

    def test_has_recommendations(self, sample_scores):
        interp = generate_interpretation(
            scores=sample_scores,
            input_level='I',
            crop_id='4',
            crop_name='Maize'
        )
        assert len(interp.recommendations) > 0

    def test_excellent_scores_minimal_recommendations(self):
        excellent_scores = {
            'SQ1': 90, 'SQ2': 85, 'SQ3': 88, 'SQ4': 92,
            'SQ5': 95, 'SQ6': 90, 'SQ7': 87, 'SR': 85
        }
        interp = generate_interpretation(
            scores=excellent_scores,
            input_level='H',
            crop_id='4',
            crop_name='Maize'
        )
        assert len(interp.recommendations) == 0
        assert interp.suitability.overall_classification == SQIClassification.EXCELLENT


class TestInterpretPhases:
    """Tests for soil phase interpretation."""

    def test_empty_dataframe_returns_empty_list(self):
        df = pd.DataFrame({'dummy': [1, 2, 3]})
        phases = interpret_phases(df)
        assert phases == []

    def test_detects_phase_columns(self):
        df = pd.DataFrame({
            'phase_stony': [True, True],
            'phase_lithic': [False, False]
        })
        phases = interpret_phases(df)
        # Should detect stony but not lithic (all False)
        phase_names = [p.phase_name for p in phases]
        assert 'Stony' in phase_names


class TestSqiMetadata:
    """Tests for SQI metadata completeness."""

    def test_all_sqis_have_metadata(self):
        for code in ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7']:
            assert code in SQI_METADATA
            assert 'name' in SQI_METADATA[code]
            assert 'key_properties' in SQI_METADATA[code]
            assert 'input_levels' in SQI_METADATA[code]

    def test_metadata_has_required_fields(self):
        for code, metadata in SQI_METADATA.items():
            assert isinstance(metadata['name'], str)
            assert isinstance(metadata['key_properties'], list)
            assert len(metadata['key_properties']) > 0


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_zero_score_handling(self):
        interp = interpret_single_sqi('SQ1', 0, 'L')
        assert interp.classification == SQIClassification.VERY_POOR
        assert interp.constraint_severity == ConstraintSeverity.VERY_SEVERE

    def test_hundred_score_handling(self):
        interp = interpret_single_sqi('SQ2', 100, 'H')
        assert interp.classification == SQIClassification.EXCELLENT
        assert interp.constraint_severity == ConstraintSeverity.NONE

    def test_boundary_scores(self):
        # Test exact boundaries
        assert classify_score(80) == SQIClassification.EXCELLENT
        assert classify_score(79.9) == SQIClassification.GOOD
        assert classify_score(60) == SQIClassification.GOOD
        assert classify_score(59.9) == SQIClassification.MODERATE
        assert classify_score(40) == SQIClassification.MODERATE
        assert classify_score(39.9) == SQIClassification.POOR
        assert classify_score(20) == SQIClassification.POOR
        assert classify_score(19.9) == SQIClassification.VERY_POOR

    def test_all_scores_same(self):
        scores = {
            'SQ1': 50, 'SQ2': 50, 'SQ3': 50, 'SQ4': 50,
            'SQ5': 50, 'SQ6': 50, 'SQ7': 50, 'SR': 50
        }
        interp = generate_interpretation(
            scores=scores,
            input_level='I',
            crop_id='4',
            crop_name='Maize'
        )
        assert interp.suitability.overall_classification == SQIClassification.MODERATE
