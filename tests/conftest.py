import pytest
from utils.api_client import APIClient
from utils.data_generators import generate_property_payload

@pytest.fixture
def create_test_property():
    payload = generate_property_payload()
    response = APIClient().post("/properties", payload)
    assert response.status_code == 201
    return response.json()["id"]