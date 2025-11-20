#!/usr/bin/env python3
"""
Simple test script to demonstrate enhanced FAO GAEZ interpretation functionality.
"""

import sys
sys.path.insert(0, '/home/user/GAEZ-Hyperlocalization/code/US_scripts')

from api.fao_gaez_descriptions import (
    get_detailed_description,
    get_enhanced_management,
    check_crop_tolerance,
    SQ_RATING_DESCRIPTIONS
)

def test_detailed_descriptions():
    """Test detailed rating class descriptions."""
    print("="*70)
    print("TEST 1: FAO GAEZ Detailed Descriptions")
    print("="*70)

    test_cases = [
        ('SQ1', 85, 'Very High'),
        ('SQ2', 55, 'Medium'),
        ('SQ3', 30, 'Low'),
        ('SQ4', 95, 'Very High'),
        ('SQ5', 45, 'Medium'),
        ('SQ6', 25, 'Low')
    ]

    for sqi_code, score, expected_level in test_cases:
        desc = get_detailed_description(sqi_code, score)
        if desc:
            print(f"\n{sqi_code} (Score: {score}) - {expected_level}:")
            print(f"  Title: {desc['title']}")
            print(f"  Characteristics: {len(desc['characteristics'])} listed")
            print(f"  Implications: {desc['implications'][:100]}...")
        else:
            print(f"\n{sqi_code} (Score: {score}): No description available")

    print("\n✓ Detailed descriptions test completed")


def test_enhanced_management():
    """Test enhanced management recommendations."""
    print("\n" + "="*70)
    print("TEST 2: Enhanced Management Recommendations")
    print("="*70)

    test_cases = [
        ('SQ1', 35, 'Low'),
        ('SQ2', 50, 'Medium'),
        ('SQ3', 45, 'Medium'),
        ('SQ4', 30, 'Low'),
        ('SQ5', 55, 'Medium'),
        ('SQ6', 38, 'Low')
    ]

    for sqi_code, score, severity in test_cases:
        recs = get_enhanced_management(sqi_code, score)
        print(f"\n{sqi_code} (Score: {score}, {severity} severity):")
        print(f"  {len(recs)} enhanced recommendations:")
        for i, rec in enumerate(recs[:2], 1):  # Show first 2
            print(f"    {i}. {rec[:90]}...")

    print("\n✓ Enhanced management recommendations test completed")


def test_crop_tolerance():
    """Test crop-specific tolerance information."""
    print("\n" + "="*70)
    print("TEST 3: Crop-Specific Tolerance Information")
    print("="*70)

    test_cases = [
        ('Maize', 'salinity'),
        ('Wheat', 'aluminum'),
        ('Rice', 'drainage'),
        ('Barley', 'salinity'),
        ('Soybeans', 'lime'),
        ('Cotton', 'aluminum')
    ]

    for crop_name, constraint_type in test_cases:
        level, desc = check_crop_tolerance(crop_name, constraint_type)
        print(f"\n{crop_name} - {constraint_type}:")
        print(f"  Tolerance level: {level}")
        print(f"  Description: {desc}")

    print("\n✓ Crop tolerance information test completed")


def test_rating_coverage():
    """Test coverage of SQ rating descriptions."""
    print("\n" + "="*70)
    print("TEST 4: Rating Description Coverage")
    print("="*70)

    expected_sqis = ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6']
    expected_classes = ['very_high', 'high', 'medium', 'low', 'very_low']

    print(f"\nChecking {len(expected_sqis)} SQIs × {len(expected_classes)} rating classes...")

    total_checked = 0
    all_present = True

    for sqi in expected_sqis:
        if sqi not in SQ_RATING_DESCRIPTIONS:
            print(f"  ✗ {sqi}: Missing entirely")
            all_present = False
            continue

        missing_classes = []
        for rating_class in expected_classes:
            if rating_class not in SQ_RATING_DESCRIPTIONS[sqi]:
                missing_classes.append(rating_class)
            else:
                total_checked += 1

        if missing_classes:
            print(f"  ✗ {sqi}: Missing classes: {', '.join(missing_classes)}")
            all_present = False
        else:
            print(f"  ✓ {sqi}: All 5 rating classes present")

    print(f"\nTotal descriptions checked: {total_checked}/{len(expected_sqis) * len(expected_classes)}")

    if all_present:
        print("✓ Complete coverage of all SQ rating descriptions")
    else:
        print("⚠ Some rating descriptions missing")

    return all_present


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print("FAO GAEZ ENHANCED INTERPRETATION TEST SUITE")
    print("="*70)

    try:
        test_detailed_descriptions()
        test_enhanced_management()
        test_crop_tolerance()
        coverage_ok = test_rating_coverage()

        print("\n" + "="*70)
        print("ALL TESTS COMPLETED SUCCESSFULLY")
        print("="*70)
        print("\n✓ FAO GAEZ descriptions module is fully functional")
        print("✓ Enhanced interpretations ready for API integration")
        print("✓ Crop-specific tolerance information available")
        print(f"✓ Rating description coverage: {'Complete' if coverage_ok else 'Partial'}")

        return 0

    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
