# FastAPI Tests

This directory contains comprehensive tests for the Mergington High School Activities API backend.

## Test Structure

- **test_activities.py** - Tests for GET /activities endpoint
- **test_signup.py** - Tests for POST /activities/{name}/signup endpoint
- **test_unregister.py** - Tests for DELETE /activities/{name}/unregister endpoint
- **test_root.py** - Tests for GET / redirect to static files
- **conftest.py** - Shared pytest fixtures and configuration

## Running Tests

### Run all tests
```bash
pytest
```

### Run with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_activities.py -v
```

### Run specific test
```bash
pytest tests/test_signup.py::test_signup_successful -v
```

### Run with coverage
```bash
pytest --cov=src --cov-report=html
```

## Test Coverage

The test suite includes **24 tests** covering:

### Activities Endpoint (4 tests)
- Retrieving all activities
- Verifying required fields in response
- Checking participant data accuracy
- Testing response consistency

### Signup Endpoint (8 tests)
- Successful signup
- Adding participants to activities
- Duplicate signup error handling
- Non-existent activity handling
- Multiple students for same activity
- Single student for multiple activities
- Case sensitivity verification
- Response message format

### Unregister Endpoint (9 tests)
- Successful unregistration
- Participant removal verification
- Non-existent activity handling
- Student not signed up error handling
- Empty activity error handling
- Multiple participant handling
- Signup after unregister
- Response message format
- Case sensitivity verification

### Root Endpoint (3 tests)
- Redirect to /static/index.html
- Redirect location header verification
- Following redirects

## Test Fixtures

All tests use the `reset_activities` fixture which:
- Resets the global activities database to initial state before each test
- Ensures test isolation and prevents state leakage between tests
- Restores original state after each test

The `client` fixture provides a FastAPI TestClient for making HTTP requests.

## Dependencies

Tests require:
- FastAPI
- pytest
- httpx (included with FastAPI TestClient)

Install with:
```bash
pip install -r requirements.txt pytest
```
