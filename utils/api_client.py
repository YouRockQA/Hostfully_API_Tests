import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://qa-assessment.svc.hostfully.com"
DEFAULT_AUTH = HTTPBasicAuth("candidate@hostfully.com", "NaX5k1wFadtkFf")

class APIClient:
    @staticmethod
    def get(endpoint, auth=DEFAULT_AUTH):
        return requests.get(f"{BASE_URL}{endpoint}", auth=auth)

    @staticmethod
    def post(endpoint, data, auth=DEFAULT_AUTH):
        return requests.post(f"{BASE_URL}{endpoint}", json=data, auth=auth)

    @staticmethod
    def patch(endpoint, data, auth=DEFAULT_AUTH):
        return requests.patch(f"{BASE_URL}{endpoint}", json=data, auth=auth)