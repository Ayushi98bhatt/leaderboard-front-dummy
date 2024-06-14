import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()

    def test_login_success(self):
        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/")

        # Find the get_started button and click on it
        get_started = self.driver.find_element(By.CLASS_NAME, "blue-button")
        get_started.click()
        time.sleep(2)

        # Find register_here button and click on it
        register_here = self.driver.find_element(By.CLASS_NAME, "registerhere")
        register_here.click()
        time.sleep(5)


        expected_url = "https://uat.businessbay.io/register"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        # Close the browser window
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))
