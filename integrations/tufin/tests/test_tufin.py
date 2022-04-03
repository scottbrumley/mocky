import unittest
from integrations.tufin.tufin import QueryEntity

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

devices_info = {
    "devices":
        {
            "device": [
                {
                    "id": 553,
                    "name": "asa",
                    "ip": "9.9.9.9",
                    "model": "5520",
                    "vendor": "Cisco",
                    "device_type": "asa"
                },
                {
                    "id": 2,
                    "name": "cisco_device_name",
                    "ip": "7.7.7.7",
                    "model": "2940",
                    "vendor": "Cisco",
                    "device_type": "router"
                }
            ]
        }
}

class TestMocky(unittest.TestCase):
    def test_get_devices_given_term(self):
        devices = QueryEntity(devices_info)
        devices_dict = devices.get_ents('devices', 'device', 'asa')
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