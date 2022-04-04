import unittest
import requests
from integrations.palo_alto_networks.panorama.panorama import panorama_url, API_KEY
import urllib3

SERVER = "https://localhost:5000"


class TestPanorama(unittest.TestCase):
    def test_http_response_status_200(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<show><system><info></info></system></show>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200


    def test_http_response_given_job_id(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<show><jobs><id>1234</id></jobs></show>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200
