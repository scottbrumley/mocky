import unittest
import requests
import urllib3
from integrations.ipinfo.ipinfo import INTEGRATION

SERVER = "https://localhost:5000"


class IPInfo(unittest.TestCase):
    class TestPanorama(unittest.TestCase):
        def test_http_response_status_200(self):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            test_url = SERVER + "/" + INTEGRATION + "/8.8.8.8/json"
            response = requests.get(test_url, verify=False)
            assert response.status_code == 200
