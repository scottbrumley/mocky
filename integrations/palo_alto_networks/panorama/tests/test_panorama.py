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

    def test_http_response_download_content_upgrade(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        my_params = {"type": "op", "cmd": "<request><content><upgrade><download><latest/>", "key": API_KEY}
        response = requests.post(test_url, data=my_params, verify=False)
        assert response.status_code == 200

    def test_http_response_install_content_upgrade(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<request><content><upgrade><install><version>"
                                                                       "latest</version></install></upgrade></content>"
                                                                       "</request>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200

    def test_http_response_pan_os_upgrade_check(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<request><system><software><check></check>"
                                                                       "</software></system></request>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200

    def test_http_response_pan_os_upgrade_install(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<request><restart><system>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200

    def test_http_response_test_security_policy(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        test_url = SERVER + panorama_url + "/api/"
        response = requests.get(test_url, params={"type": "op", "cmd": "<test><security-policy-match>",
                                                  "key": API_KEY}, verify=False)
        assert response.status_code == 200
