import unittest
from integrations.tufin.tufin import QueryEntity
from integrations.tufin.dataset import applications_info, devices_info

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class TestMocky(unittest.TestCase):
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

"""
class TestMocky(unittest.TestCase):

    def test_count_equals_total_given_empty_string(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://localhost:5000/securetrack/api/devices")
        print(driver.title)

        dict = json.dump(devices)
        self.assertEquals(dict.count, dict.total, 'Total Records equals Count Returned')
"""


"""
def test_home_page_with_fixture(test_client):

    with flask_app.test_client() as testing_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Welcome to the" in response.data
        assert b"Flask User Management Example!" in response.data
        assert b"Need an account?" in response.data
        assert b"Existing user?" in response.data
"""