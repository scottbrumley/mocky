import unittest
import requests
import urllib3
from integrations.tufin.tufin import INTEGRATION, user, pw
from integrations.tufin.tufin import QueryEntity, harvest_args
from integrations.tufin.dataset import applications_info, devices_info

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

SERVER = "https://localhost:5000"


class TestTufin(unittest.TestCase):
    def test_get_devices_given_device_name(self):
        devices = QueryEntity(devices_info)
        name = {"name": "asa"}
        devices_dict = devices.get_ents('devices', 'device', name)
        self.assertIsInstance(devices_dict, dict)

    def test_get_applications_given_app_name(self):
        applications = QueryEntity(applications_info)
        name = {"name": "Service Now"}
        applications_dict = applications.get_ents('applications', 'application', name)
        self.assertIsInstance(applications_dict, dict)

    def test_get_devices_not_given_device_name(self):
        devices = QueryEntity(devices_info)
        name = {"name": ""}
        devices_dict = devices.get_ents('devices', 'device', name)
        self.assertIsInstance(devices_dict, dict)

    def test_get_applications_not_given_app_name(self):
        applications = QueryEntity(applications_info)
        name = {"name": ""}
        applications_dict = applications.get_ents('applications', 'application', name)
        self.assertIsInstance(applications_dict, dict)

    def test_get_devices_not_given_group_name(self):
        devices = QueryEntity(devices_info)
        name = {"name": "asa"}
        devices_dict = devices.get_ents('', 'device', name)
        self.assertIsInstance(devices_dict, dict)

    def test_get_devices_not_given_entity_name(self):
        devices = QueryEntity(devices_info)
        name = {"name": "asa"}
        devices_dict = devices.get_ents('devices', '', name)
        self.assertIsInstance(devices_dict, dict)

    def test_harvest_args(self):
        my_args = {'name':'fred'}
        args_vars = harvest_args(my_args)
        self.assertIsInstance(args_vars, dict)

    class TestPanorama(unittest.TestCase):
        def test_http_response_status_200(self):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            test_url = SERVER + "/" + INTEGRATION
            response = requests.get(test_url, auth=(user,pw), verify=False)
            assert response.status_code == 200
