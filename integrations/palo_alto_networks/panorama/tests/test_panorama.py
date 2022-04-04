import unittest
import requests
from integrations.palo_alto_networks.panorama.panorama import panorama_url, user, pw
from urllib3.exceptions import InsecureRequestWarning

SERVER = "https://localhost:5000"


class TestPanorama(unittest.TestCase):
    def test_http_response_status_200(self):
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        test_url = SERVER + panorama_url
        response = requests.get(test_url, auth=(user,pw), verify=False)
        assert response.status_code == 200

