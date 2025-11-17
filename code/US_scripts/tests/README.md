# GAEZ US Scripts Test Suite

This directory contains a comprehensive unit and integration testing framework for the GAEZ US Scripts soil quality assessment system.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Organization](#test-organization)
- [Test Coverage](#test-coverage)
- [Writing New Tests](#writing-new-tests)
- [Continuous Integration](#continuous-integration)
- [Troubleshooting](#troubleshooting)

## Overview

The test suite provides comprehensive coverage of the GAEZ soil quality index calculation system, including:

- **Unit tests**: Test individual functions in isolation
- **Integration tests**: Test workflows and component interactions
- **Fixtures**: Reusable test data and mock objects
- **Parametrized tests**: Test multiple input combinations efficiently

### Test Modules

| Test File | Module Tested | Description |
|-----------|---------------|-------------|
| `test_GAEZ_SQI_functions.py` | `GAEZ_SQI_functions.py` | Tests for all 7 SQI calculators and helper functions |
| `test_GAEZ_crop_req.py` | `GAEZ_crop_req.py` | Tests for crop requirement data retrieval |
| `test_GAEZ_SSURGO_data.py` | `GAEZ_SSURGO_data.py` | Tests for SSURGO data access and processing |
| `test_GAEZ_US_phase_calc.py` | `GAEZ_US_phase_calc.py` | Tests for soil phase classification (22 phases) |
| `test_GAEZ_soil_data_processing.py` | `GAEZ_soil_data_processing.py` | Tests for user data integration |
| `conftest.py` | N/A | Shared fixtures and test utilities |

## Installation

### 1. Install Test Dependencies

From the `code/US_scripts` directory:

```bash
pip install -r requirements-test.txt
```

This will install:
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `pytest-mock` - Mocking utilities
- `responses` / `requests-mock` - HTTP mocking
- `black`, `flake8`, `mypy` - Code quality tools

### 2. Verify Installation

```bash
pytest --version
```

You should see pytest version 7.0.0 or higher.

## Running Tests

### Run All Tests

```bash
cd code/US_scripts
pytest
```

### Run Specific Test File

```bash
pytest tests/test_GAEZ_SQI_functions.py
```

### Run Specific Test Class

```bash
pytest tests/test_GAEZ_SQI_functions.py::TestConstraintCurve
```

### Run Specific Test Function

```bash
pytest tests/test_GAEZ_SQI_functions.py::TestConstraintCurve::test_constraint_curve_monotonic_increasing
```

### Run Tests by Marker

```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Skip slow tests
pytest -m "not slow"

# Skip tests requiring network
pytest -m "not requires_network"
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Coverage Report

```bash
pytest --cov=. --cov-report=html
```

This generates an HTML coverage report in `htmlcov/index.html`.

### Run with Coverage and Missing Lines

```bash
pytest --cov=. --cov-report=term-missing
```

### Run Failed Tests Only

```bash
# Run tests, then re-run only failures
pytest --lf

# Run failures first, then rest
pytest --ff
```

## Test Organization

### Test Markers

Tests are organized using pytest markers:

| Marker | Description | Usage |
|--------|-------------|-------|
| `@pytest.mark.unit` | Fast, isolated unit tests | Default, run frequently |
| `@pytest.mark.integration` | Tests multiple components | Run before commits |
| `@pytest.mark.slow` | Tests taking >1 second | Skip during development |
| `@pytest.mark.requires_data` | Needs external data files | May fail if data missing |
| `@pytest.mark.requires_network` | Needs network access | Skip in offline environments |

### Test Naming Conventions

- Test files: `test_<module_name>.py`
- Test classes: `Test<FeatureName>`
- Test functions: `test_<what_is_tested>`

Example:
```python
class TestConstraintCurve:
    def test_constraint_curve_monotonic_increasing(self):
        ...
```

## Test Coverage

### Current Coverage Goals

- **Overall**: >80% line coverage
- **Critical modules** (SQI calculators): >90%
- **Utility functions**: >85%

### Generate Coverage Report

```bash
pytest --cov=. --cov-report=html --cov-report=term
```

View the HTML report:
```bash
# Linux/Mac
open htmlcov/index.html

# Windows
start htmlcov/index.html
```

### Coverage by Module

```bash
pytest --cov=. --cov-report=term-missing
```

This shows which lines are not covered by tests.

## Writing New Tests

### Test Structure

```python
import pytest
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

import GAEZ_SQI_functions as sqi


class TestNewFeature:
    """Tests for new feature."""

    def test_basic_functionality(self):
        """Test basic behavior."""
        result = sqi.new_function(10)
        assert result == 20, "Should double the input"

    def test_edge_case(self):
        """Test edge case handling."""
        with pytest.raises(ValueError):
            sqi.new_function(-1)
```

### Using Fixtures

Fixtures are defined in `conftest.py` and can be used in any test:

```python
def test_with_sample_data(sample_soil_horizon_data):
    """Use fixture for test data."""
    result = sqi.calculate_depth_weights(sample_soil_horizon_data)
    assert len(result) == 3
```

### Creating New Fixtures

Add to `conftest.py`:

```python
@pytest.fixture
def my_custom_fixture():
    """Create custom test data."""
    data = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6]
    })
    return data
```

### Parametrized Tests

Test multiple inputs efficiently:

```python
@pytest.mark.parametrize("input_val,expected", [
    (0, 0),
    (10, 20),
    (50, 100),
])
def test_multiple_inputs(input_val, expected):
    result = my_function(input_val)
    assert result == expected
```

### Mocking External Dependencies

Use `pytest-mock` for mocking:

```python
def test_with_mock(mocker):
    """Mock external API call."""
    mock_response = {'data': [1, 2, 3]}
    mocker.patch('GAEZ_SSURGO_data.sda_return', return_value=mock_response)

    result = fetch_data()
    assert result == mock_response
```

### Testing Exceptions

```python
def test_raises_error():
    """Test that function raises expected error."""
    with pytest.raises(ValueError, match="Invalid input"):
        sqi.constraint_curve([], pd.DataFrame())
```

## Best Practices

### 1. Test Independence

Each test should be independent and not rely on other tests:

```python
# Good
def test_feature():
    data = create_test_data()
    result = process(data)
    assert result == expected

# Bad - depends on previous test state
global_data = None
def test_setup():
    global global_data
    global_data = create_test_data()

def test_feature():  # Depends on test_setup running first!
    result = process(global_data)
```

### 2. Clear Assertions

Use descriptive assertion messages:

```python
# Good
assert result > 0, f"Score {result} should be positive"

# Bad
assert result > 0
```

### 3. Test One Thing

Each test should verify one specific behavior:

```python
# Good - single responsibility
def test_constraint_curve_handles_empty_data():
    with pytest.raises(ValueError):
        sqi.constraint_curve(50, pd.DataFrame())

# Bad - tests multiple things
def test_constraint_curve():
    # Tests empty data
    with pytest.raises(ValueError):
        sqi.constraint_curve(50, pd.DataFrame())

    # Tests normal operation
    result = sqi.constraint_curve(50, data)
    assert result > 0

    # Tests another edge case
    ...
```

### 4. Use Fixtures for Setup

Don't repeat setup code:

```python
# Good - use fixture
@pytest.fixture
def soil_data():
    return pd.DataFrame({...})

def test_with_fixture(soil_data):
    result = process(soil_data)

# Bad - repeated setup
def test_1():
    soil_data = pd.DataFrame({...})
    result = process(soil_data)

def test_2():
    soil_data = pd.DataFrame({...})  # Duplicated!
    result = process(soil_data)
```

## Continuous Integration

### GitHub Actions Example

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          cd code/US_scripts
          pip install -r requirements-test.txt
      - name: Run tests
        run: |
          cd code/US_scripts
          pytest --cov=. --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

## Troubleshooting

### Import Errors

If you get import errors:

```bash
# Ensure you're in the correct directory
cd code/US_scripts

# Run pytest from the US_scripts directory
pytest

# Or add the path explicitly
PYTHONPATH=. pytest
```

### Missing Dependencies

```bash
# Reinstall test dependencies
pip install -r requirements-test.txt --upgrade
```

### Fixture Not Found

Make sure `conftest.py` is in the `tests/` directory and the fixture is defined there.

### Tests Running Slowly

```bash
# Skip slow tests during development
pytest -m "not slow"

# Run tests in parallel (requires pytest-xdist)
pip install pytest-xdist
pytest -n auto
```

### Coverage Not Working

```bash
# Reinstall coverage plugin
pip install --upgrade pytest-cov

# Verify coverage is enabled in pytest.ini
cat pytest.ini | grep cov
```

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [Testing Python Applications with Pytest](https://realpython.com/pytest-python-testing/)
- [GAEZ v4 Documentation](https://openknowledge.fao.org/items/039f7ec9-98af-49e1-8d24-850122c69bef)

## Contributing

When adding new features to the codebase:

1. Write tests first (TDD approach recommended)
2. Ensure tests pass: `pytest`
3. Check coverage: `pytest --cov=.`
4. Run code quality checks:
   ```bash
   black .
   flake8 .
   mypy .
   ```
5. Update this README if needed

## Contact

For questions about the test suite, please open an issue in the repository.

---

**Last Updated**: 2025-11-17
