from utils.api_client import APIClient

class TestErrorHandling:
    def test_invalid_http_method(self):
        """Test using an invalid HTTP method on an endpoint"""
        response = APIClient.patch("/properties", {})
        assert response.status_code == 405
        json_response = response.json()
        assert json_response["status"] == 405
        assert json_response["title"] == "Method Not Allowed"
        assert "detail" in json_response
        assert "Method 'PATCH' is not supported." in json_response["detail"]