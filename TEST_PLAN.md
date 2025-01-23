# Test Plan for Hostfully API

## Objective
Validate the functionality and reliability of the `/properties` and `/bookings` endpoints.

## Scenarios Covered
1. **Authentication**
   - Valid and invalid credentials

2. **/properties Endpoint**
   - Create property with valid and invalid inputs
   - Fetch property by valid and invalid IDs

3. **/bookings Endpoint**
   - Create booking with valid data
   - Handle overlapping bookings

4. **Error Handling**
   - Invalid HTTP methods
   - Incorrect authentication

## Known Issues
1. Property creation with empty `alias` returns `500 Internal Server Error` instead of `400 Bad Request`.
2. Overlapping bookings are not handled as expected (`201 Created` instead of `400 Bad Request`).

## Why These Scenarios?
These scenarios cover:
- Core functionality of the API (`/properties` and `/bookings`).
- Edge cases (invalid inputs, overlap, error handling).
- End-to-end validation of critical API workflows.