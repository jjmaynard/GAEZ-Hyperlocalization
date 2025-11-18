# CLI Testing Framework Guide

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Initial Setup](#initial-setup)
4. [Running Tests](#running-tests)
5. [Coverage Analysis](#coverage-analysis)
6. [Advanced Test Execution](#advanced-test-execution)
7. [Debugging Tests](#debugging-tests)
8. [Continuous Integration Workflows](#continuous-integration-workflows)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)
11. [Common CLI Workflows](#common-cli-workflows)

---

## Overview

This guide provides comprehensive instructions for using the GAEZ-Hyperlocalization testing framework from the command line. The framework is built on **pytest** and includes 130+ test cases covering the US_scripts modules.

**Framework Statistics:**
- **Test Files:** 5 modules + shared fixtures
- **Test Cases:** 130+
- **Current Coverage:** 53% (baseline)
- **Target Coverage:** 80%+
- **Python Version:** 3.11.14
- **pytest Version:** 9.0.1

---

## Prerequisites

### System Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support (recommended)
- Git (for version control)

### Verify Python Installation
```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

**Expected Output:**
```
Python 3.11.14
pip 24.x.x from /path/to/pip (python 3.11)
```

---

## Initial Setup

### Step 1: Navigate to Project Directory
```bash
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**Verification:**
```bash
# Your prompt should now show (venv)
(venv) user@host:~/GAEZ-Hyperlocalization/code/US_scripts$
```

### Step 3: Install Testing Dependencies
```bash
# Install all testing dependencies
pip install -r requirements-test.txt

# Verify pytest installation
pytest --version
```

**Expected Output:**
```
pytest 9.0.1
```

### Step 4: Verify Test Discovery
```bash
# List all discoverable tests without running them
pytest --collect-only
```

**Expected Output:**
```
collected 130+ items
<Module test_GAEZ_SQI_functions.py>
  <Function test_constraint_curve_monotonic>
  <Function test_constraint_curve_bell_shaped>
  ...
```

---

## Running Tests

### Basic Test Execution

#### Run All Tests
```bash
# Run all tests with default settings
pytest

# Run with verbose output
pytest -v

# Run with extra verbose output (shows individual test names)
pytest -vv
```

**Sample Output:**
```
========================= test session starts =========================
platform linux -- Python 3.11.14, pytest-9.0.1, pluggy-1.5.0
rootdir: /home/user/GAEZ-Hyperlocalization/code/US_scripts
configfile: pytest.ini
collected 130 items

tests/test_GAEZ_SQI_functions.py ........x.x.x................  [ 23%]
tests/test_GAEZ_crop_req.py .................               [ 36%]
tests/test_GAEZ_SSURGO_data.py .......................      [ 53%]
tests/test_GAEZ_US_phase_calc.py .............             [ 63%]
tests/test_GAEZ_soil_data_processing.py .......................[ 100%]

==================== 90 passed, 8 skipped, 43 failed in 2.50s ============
```

#### Run Specific Test File
```bash
# Run tests for a single module
pytest tests/test_GAEZ_SQI_functions.py

# Run with verbose output
pytest tests/test_GAEZ_SQI_functions.py -v
```

#### Run Specific Test Function
```bash
# Run a single test function
pytest tests/test_GAEZ_SQI_functions.py::test_constraint_curve_monotonic

# Run multiple specific tests
pytest tests/test_GAEZ_SQI_functions.py::test_constraint_curve_monotonic \
       tests/test_GAEZ_SQI_functions.py::test_constraint_curve_bell_shaped
```

#### Run Tests by Pattern Matching
```bash
# Run all tests with "constraint" in the name
pytest -k constraint

# Run all tests with "depth" in the name
pytest -k depth

# Run tests matching multiple patterns (OR logic)
pytest -k "constraint or depth"

# Run tests excluding a pattern (NOT logic)
pytest -k "not network"
```

---

## Coverage Analysis

### Generate Coverage Reports

#### Terminal Coverage Report
```bash
# Run tests with coverage and display missing lines
pytest --cov=. --cov-report=term-missing

# Run with branch coverage
pytest --cov=. --cov-report=term-missing --cov-branch
```

**Sample Output:**
```
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
GAEZ_SQI_functions.py                 450    382    15%   50-100, 120-450
GAEZ_crop_req.py                      120      2    98%   45, 67
GAEZ_soil_data_processing.py          200     36    82%   150-185
gaez_config.py                         15      0   100%
-----------------------------------------------------------------
TOTAL                                 785    420    53%
```

#### HTML Coverage Report
```bash
# Generate interactive HTML coverage report
pytest --cov=. --cov-report=html

# Open the report in a browser
# On Linux with GUI:
xdg-open htmlcov/index.html

# On macOS:
open htmlcov/index.html

# On Windows:
start htmlcov/index.html

# Or manually navigate to:
# file:///home/user/GAEZ-Hyperlocalization/code/US_scripts/htmlcov/index.html
```

#### Coverage for Specific Module
```bash
# Coverage for single module
pytest --cov=GAEZ_SQI_functions --cov-report=term-missing tests/test_GAEZ_SQI_functions.py

# Coverage for multiple modules
pytest --cov=GAEZ_SQI_functions --cov=GAEZ_crop_req --cov-report=html
```

#### XML Coverage Report (for CI/CD)
```bash
# Generate XML report for integration with CI tools
pytest --cov=. --cov-report=xml

# This creates coverage.xml in the current directory
```

### Coverage Configuration

The `.coveragerc` or `pytest.ini` configuration controls:
- **Omitted files:** Tests, __pycache__, surgo_data.py
- **Report formats:** HTML, terminal, XML
- **Branch coverage:** Enabled for conditional logic testing
- **Precision:** 2 decimal places

---

## Advanced Test Execution

### Running Tests by Markers

Test markers allow selective test execution. Markers are defined in `pytest.ini`:

#### Available Markers
- `@pytest.mark.unit` - Fast, isolated unit tests
- `@pytest.mark.integration` - Multi-component integration tests
- `@pytest.mark.slow` - Tests taking >1 second
- `@pytest.mark.requires_data` - Tests needing external data files
- `@pytest.mark.requires_network` - Tests requiring network access

#### Marker-Based Execution
```bash
# Run only unit tests (fast)
pytest -m unit

# Run only integration tests
pytest -m integration

# Skip slow tests (for quick validation)
pytest -m "not slow"

# Skip tests requiring network (for offline work)
pytest -m "not requires_network"

# Run unit tests that don't require data
pytest -m "unit and not requires_data"

# Run integration or slow tests
pytest -m "integration or slow"
```

### Test Output Control

#### Minimal Output
```bash
# Quiet mode (only show summary)
pytest -q

# Only show failed tests
pytest --tb=short

# No traceback
pytest --tb=no
```

#### Detailed Output
```bash
# Show local variables in tracebacks
pytest -l

# Show full traceback
pytest --tb=long

# Show print statements from tests
pytest -s

# Show print statements and verbose
pytest -s -v
```

#### Progressive Output
```bash
# Show test results as they complete
pytest -v --tb=line

# Show percentage progress
pytest --no-header -q
```

### Parallel Test Execution

```bash
# Install pytest-xdist for parallel execution
pip install pytest-xdist

# Run tests in parallel (auto-detect CPU cores)
pytest -n auto

# Run on specific number of workers
pytest -n 4

# Parallel with coverage
pytest -n auto --cov=. --cov-report=html
```

### Controlling Test Execution Flow

#### Stop on First Failure
```bash
# Stop after first failure
pytest -x

# Stop after N failures
pytest --maxfail=3
```

#### Rerun Failed Tests
```bash
# Run only previously failed tests
pytest --lf

# Run failed first, then remaining tests
pytest --ff
```

#### New Tests First
```bash
# Run new tests (modified files) first
pytest --nf
```

---

## Debugging Tests

### Interactive Debugging

#### Drop into Debugger on Failure
```bash
# Use Python's built-in debugger (pdb)
pytest --pdb

# Drop into debugger on first failure
pytest --pdb -x
```

**PDB Commands:**
- `l` (list) - Show current code
- `n` (next) - Execute next line
- `s` (step) - Step into function
- `c` (continue) - Continue execution
- `p variable` - Print variable value
- `q` (quit) - Exit debugger

#### Trace Test Execution
```bash
# Show execution trace
pytest --trace

# Show fixture setup/teardown
pytest --setup-show
```

### Verbose Assertion Information

```bash
# Show detailed assertion information
pytest -vv

# Show full diff for failed assertions
pytest -vv --tb=short
```

### Capturing Output

```bash
# Show print() statements during test execution
pytest -s

# Show captured logs
pytest --log-cli-level=DEBUG

# Show warnings
pytest -W all
```

### Profiling Test Performance

```bash
# Show slowest N tests
pytest --durations=10

# Show all test durations
pytest --durations=0

# Profile with cProfile
pytest --profile

# Profile with profiling output
pytest --profile --profile-svg
```

---

## Continuous Integration Workflows

### Pre-commit Checks

Create a pre-commit test script:

```bash
#!/bin/bash
# File: run_precommit_tests.sh

echo "Running pre-commit tests..."

# Navigate to project directory
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts

# Activate virtual environment
source venv/bin/activate

# Run fast tests only
pytest -m "unit and not slow" -v

# Check exit code
if [ $? -eq 0 ]; then
    echo "✓ All pre-commit tests passed"
    exit 0
else
    echo "✗ Pre-commit tests failed"
    exit 1
fi
```

Make executable and run:
```bash
chmod +x run_precommit_tests.sh
./run_precommit_tests.sh
```

### Full CI Pipeline

```bash
#!/bin/bash
# File: run_ci_tests.sh

echo "=== CI Test Pipeline ==="

# Set strict error handling
set -e

# Activate environment
source venv/bin/activate

# Step 1: Code quality checks
echo "Step 1: Running code quality checks..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Step 2: Type checking
echo "Step 2: Running type checks..."
mypy --ignore-missing-imports *.py

# Step 3: Run all tests with coverage
echo "Step 3: Running test suite..."
pytest --cov=. --cov-report=xml --cov-report=term-missing -v

# Step 4: Check coverage threshold
echo "Step 4: Checking coverage threshold..."
coverage report --fail-under=50

echo "=== CI Pipeline Complete ==="
```

### GitHub Actions Example

Create `.github/workflows/test.yml`:

```yaml
name: Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        cd code/US_scripts
        pip install -r requirements-test.txt

    - name: Run tests with coverage
      run: |
        cd code/US_scripts
        pytest --cov=. --cov-report=xml --cov-report=term-missing

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./code/US_scripts/coverage.xml
```

---

## Best Practices

### 1. Test-Driven Development Workflow

```bash
# Step 1: Write failing test
pytest tests/test_new_feature.py::test_new_function -v
# Expected: FAILED

# Step 2: Implement minimal code to pass
# ... edit source files ...

# Step 3: Run test again
pytest tests/test_new_feature.py::test_new_function -v
# Expected: PASSED

# Step 4: Refactor and verify
pytest tests/test_new_feature.py -v

# Step 5: Run full suite
pytest
```

### 2. Watch Mode for Active Development

```bash
# Install pytest-watch
pip install pytest-watch

# Auto-run tests on file changes
ptw -- -v

# Watch specific directory
ptw --runner "pytest -v tests/test_GAEZ_SQI_functions.py"
```

### 3. Regular Coverage Audits

```bash
# Weekly coverage check
pytest --cov=. --cov-report=html
firefox htmlcov/index.html  # Review uncovered code

# Identify critical gaps
pytest --cov=. --cov-report=term-missing | grep "GAEZ_SQI_functions"
```

### 4. Performance Monitoring

```bash
# Baseline performance
pytest --durations=10 > baseline_performance.txt

# After changes, compare
pytest --durations=10 > new_performance.txt
diff baseline_performance.txt new_performance.txt
```

### 5. Incremental Testing Strategy

```bash
# Morning routine - quick sanity check
pytest -m "unit and not slow" -q

# Before commit - comprehensive check
pytest -m "not requires_network" -v

# Before merge - full suite
pytest -v --cov=. --cov-report=html
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Module Import Errors

**Symptom:**
```
ImportError: No module named 'GAEZ_SQI_functions'
```

**Solution:**
```bash
# Ensure you're in the correct directory
cd /home/user/GAEZ-Hyperlocalization/code/US_scripts

# Verify PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or install package in development mode
pip install -e .
```

#### Issue 2: Missing Dependencies

**Symptom:**
```
ModuleNotFoundError: No module named 'pytest'
```

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements-test.txt

# Verify installation
pip list | grep pytest
```

#### Issue 3: Tests Fail with Data File Errors

**Symptom:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/crop_requirements.csv'
```

**Solution:**
```bash
# Check if test requires external data
pytest -m "not requires_data" -v

# Or create mock data fixtures in conftest.py
# See tests/conftest.py for examples
```

#### Issue 4: Coverage Report Not Generated

**Symptom:**
```
coverage: No data to report.
```

**Solution:**
```bash
# Ensure pytest-cov is installed
pip install pytest-cov

# Run with explicit coverage source
pytest --cov=. --cov-report=html

# Check .coverage file exists
ls -la .coverage
```

#### Issue 5: Slow Test Execution

**Solution:**
```bash
# Identify slow tests
pytest --durations=0

# Skip slow tests during development
pytest -m "not slow" -v

# Run parallel tests
pip install pytest-xdist
pytest -n auto
```

#### Issue 6: Tests Pass Locally but Fail in CI

**Debugging Steps:**
```bash
# Check Python version consistency
python --version

# Verify dependencies match CI environment
pip freeze > local_requirements.txt
# Compare with CI logs

# Run with same markers as CI
pytest -m "not requires_network" -v

# Check for platform-specific issues
pytest --verbose --capture=no
```

### Debugging Commands Reference

```bash
# Get detailed pytest help
pytest --help

# List all available markers
pytest --markers

# List all available fixtures
pytest --fixtures

# Show pytest configuration
pytest --showlocals

# Validate pytest.ini
pytest --collect-only --quiet
```

---

## Common CLI Workflows

### Workflow 1: Quick Validation (< 30 seconds)

```bash
# For rapid feedback during active development
pytest -m "unit and not slow" -q
```

**Use Case:** After making small code changes, before committing

---

### Workflow 2: Module-Specific Testing

```bash
# When working on a specific module
MODULE=GAEZ_SQI_functions

# Run module tests
pytest tests/test_${MODULE}.py -v

# With coverage
pytest --cov=${MODULE} --cov-report=term-missing tests/test_${MODULE}.py

# Watch for changes (requires pytest-watch)
ptw -- tests/test_${MODULE}.py -v
```

**Use Case:** Focused development on one module

---

### Workflow 3: Pre-Commit Validation (1-2 minutes)

```bash
# Comprehensive pre-commit check
pytest -m "not requires_network" -v --tb=short && \
pytest --cov=. --cov-report=term --cov-fail-under=50
```

**Use Case:** Before committing code to version control

---

### Workflow 4: Full Test Suite (2-5 minutes)

```bash
# Complete test execution with coverage
pytest -v --cov=. --cov-report=html --cov-report=term-missing

# Open coverage report
xdg-open htmlcov/index.html  # Linux
# or
open htmlcov/index.html      # macOS
```

**Use Case:** Before pull request, weekly audits

---

### Workflow 5: Continuous Feedback Loop

```bash
# Terminal 1: Watch mode
ptw -- -v -m "unit"

# Terminal 2: Development
# ... edit code ...
# Tests auto-run in Terminal 1
```

**Use Case:** Test-driven development sessions

---

### Workflow 6: Debugging Specific Failure

```bash
# Run failed test with debugger
pytest tests/test_GAEZ_SQI_functions.py::test_failing_function --pdb -s

# Or with verbose output
pytest tests/test_GAEZ_SQI_functions.py::test_failing_function -vv -s --tb=long
```

**Use Case:** Investigating test failures

---

### Workflow 7: Performance Profiling

```bash
# Identify performance bottlenecks
pytest --durations=20 -v

# Profile specific slow test
pytest tests/test_slow_function.py --profile --profile-svg

# View profile results
xdg-open prof/combined.svg
```

**Use Case:** Optimizing test suite performance

---

### Workflow 8: Coverage Improvement

```bash
# Step 1: Generate coverage report
pytest --cov=. --cov-report=html

# Step 2: Identify low-coverage modules
open htmlcov/index.html

# Step 3: Write tests for uncovered code
# ... add tests ...

# Step 4: Verify coverage improvement
pytest --cov=. --cov-report=term-missing

# Step 5: Compare coverage
# Before: 53% | After: 65% ✓
```

**Use Case:** Systematic coverage improvement

---

## Advanced Tips

### Custom Test Execution Scripts

Create `run_tests.py`:

```python
#!/usr/bin/env python3
"""Custom test runner with enhanced reporting"""

import sys
import pytest

def main():
    """Run tests with custom configuration"""
    args = [
        '-v',                                    # Verbose
        '--tb=short',                           # Short traceback
        '--cov=.',                              # Coverage
        '--cov-report=html',                    # HTML report
        '--cov-report=term-missing',            # Terminal report
        '-m', 'not requires_network',           # Skip network tests
        '--durations=10',                       # Show slowest 10
    ]

    # Add any CLI arguments
    args.extend(sys.argv[1:])

    # Run pytest
    exit_code = pytest.main(args)

    if exit_code == 0:
        print("\n✓ All tests passed!")
    else:
        print(f"\n✗ Tests failed with exit code {exit_code}")

    return exit_code

if __name__ == '__main__':
    sys.exit(main())
```

Run with:
```bash
chmod +x run_tests.py
./run_tests.py
./run_tests.py tests/test_GAEZ_SQI_functions.py
```

### Environment-Specific Testing

```bash
# Development environment
export TESTING_ENV=dev
pytest -m "unit"

# Staging environment
export TESTING_ENV=staging
pytest -m "integration"

# Production validation
export TESTING_ENV=prod
pytest -m "smoke"
```

### Conditional Test Execution

```bash
# Run tests based on changed files
git diff --name-only | grep "GAEZ_SQI" && pytest tests/test_GAEZ_SQI_functions.py

# Run all tests if core files changed
if git diff --name-only | grep -E "(GAEZ_SQI|GAEZ_crop)"; then
    pytest -v
fi
```

---

## Summary

### Quick Reference Commands

| Task | Command |
|------|---------|
| Run all tests | `pytest` |
| Run with coverage | `pytest --cov=. --cov-report=html` |
| Run specific file | `pytest tests/test_MODULE.py` |
| Run specific test | `pytest tests/test_MODULE.py::test_function` |
| Run by marker | `pytest -m unit` |
| Skip slow tests | `pytest -m "not slow"` |
| Debug on failure | `pytest --pdb -x` |
| Show coverage gaps | `pytest --cov=. --cov-report=term-missing` |
| Run failed tests | `pytest --lf` |
| Show slowest tests | `pytest --durations=10` |
| Parallel execution | `pytest -n auto` |
| Verbose output | `pytest -vv` |
| Quiet mode | `pytest -q` |

### Testing Checklist

- [ ] Virtual environment activated
- [ ] Dependencies installed (`requirements-test.txt`)
- [ ] Tests discoverable (`pytest --collect-only`)
- [ ] Unit tests passing (`pytest -m unit`)
- [ ] Integration tests passing (`pytest -m integration`)
- [ ] Coverage >50% (`pytest --cov=. --cov-fail-under=50`)
- [ ] No slow tests blocking workflow (`pytest --durations=10`)
- [ ] Coverage report reviewed (`htmlcov/index.html`)

---

## Additional Resources

### Documentation
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Python unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

### Project-Specific Docs
- `TESTING.md` - Testing framework overview
- `tests/README.md` - Detailed test documentation
- `README.md` - US_scripts module documentation

### Getting Help

```bash
# pytest help
pytest --help

# List markers
pytest --markers

# List fixtures
pytest --fixtures

# Show configuration
pytest --version --version
```

---

## Conclusion

This CLI testing guide provides comprehensive workflows for running, debugging, and maintaining the GAEZ-Hyperlocalization test suite. By following these practices, you'll ensure code quality, catch regressions early, and maintain high test coverage.

**Key Takeaways:**
1. Use markers for selective test execution
2. Leverage coverage reports to identify gaps
3. Run fast tests frequently, comprehensive tests before commits
4. Use debugging tools (`--pdb`, `-vv`) to investigate failures
5. Automate testing in CI/CD pipelines

**Happy Testing! 🧪**

---

*Last Updated: 2025-11-17*
*Framework Version: pytest 9.0.1*
*Test Coverage: 53% → Target: 80%+*
