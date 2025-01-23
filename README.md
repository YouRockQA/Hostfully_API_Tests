
# Hostfully API Test Suite

## Overview
This repository contains an automated test suite for the Hostfully API to validate its functionality and reliability. It includes tests for the `/properties` and `/bookings` endpoints, covering both positive and negative test cases.

---

## Steps to Execute the Tests

### Prerequisites
1. Install Python (3.8 or higher).
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Tests
1. To run all tests:
   ```bash
   pytest
   ```
2. To run a specific test file:
   ```bash
   pytest tests/test_properties.py
   ```

---

## Dependencies

The following Python libraries are required and are listed in the `requirements.txt` file:
- `pytest`: For running test cases.
- `requests`: For making HTTP requests to the API.

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Structure of the Test Cases

### Folder Structure
```
Hostfully_project_test/
├── tests/
│   ├── test_authentication.py        # Tests for authentication
│   ├── test_bookings.py              # Tests for booking functionality
│   ├── test_error_handling.py        # Tests for error handling
│   ├── test_properties.py            # Tests for property management
│   ├── conftest.py                   # Shared fixtures for the tests
├── utils/
│   ├── api_client.py                 # Helper functions for API calls
│   ├── data_generators.py            # Functions to generate test data
├── .venv/                            # Virtual environment (ignored by git)
├── requirements.txt                  # Dependencies
├── pytest.ini                        # Pytest configuration
├── README.md                         # Project documentation
├── TEST_PLAN.md                      # Test Plan documentation
```

### Description of Tests

1. **Authentication Tests (`test_authentication.py`)**
   - Valid and invalid authentication.

2. **Property Tests (`test_properties.py`)**
   - Creating properties with valid and invalid inputs.
   - Fetching properties by valid and invalid IDs.

3. **Booking Tests (`test_bookings.py`)**
   - Creating bookings with valid inputs.
   - Validating that bookings do not overlap.

4. **Error Handling Tests (`test_error_handling.py`)**
   - Handling incorrect HTTP methods.
   - Testing API behavior with invalid credentials.

---

## Known Issues

- **Property creation with invalid input:** API returns `500 Internal Server Error` instead of `400 Bad Request`.
- **Booking overlap validation:** API allows overlapping bookings instead of returning an error.
