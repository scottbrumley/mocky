import unittest
import requests
from integrations.palo_alto_networks.panorama.panorama import panorama_url, user, pw
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SERVER = "https://localhost:5000"


class TestPanorama(unittest.TestCase):
    def test_http_response_status_200(self):
        test_url = SERVER + panorama_url + "/api"
        response = requests.get(test_url, auth=(user,pw), verify=False)
        assert response.status_code == 200

