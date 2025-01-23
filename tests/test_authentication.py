from utils.api_client import APIClient

class TestAuthentication:
    def test_valid_credentials(self):
        """Test API access with valid credentials"""
        response = APIClient.get("/properties")
        assert response.status_code == 200  # Authorization is correct

    def test_invalid_credentials(self):
        """Test API access with invalid credentials"""
        from requests.auth import HTTPBasicAuth
        invalid_auth = HTTPBasicAuth("candidate@hostfully.com", "wrongpassword")
        response = APIClient.get("/properties", auth=invalid_auth)

        # Checking HTTP status
        assert response.status_code == 401  # Unauthorized

        # Checking response structure
        json_response = response.json()
        assert "error" in json_response
        assert json_response["error"] == "Unauthorized"
        assert "message" in json_response
        assert json_response["message"] == "Error while authenticating your access"
        assert "exception" in json_response
        assert json_response["exception"] == "Bad credentials"

