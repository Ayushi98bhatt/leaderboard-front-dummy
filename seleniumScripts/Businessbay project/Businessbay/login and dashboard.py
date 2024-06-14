import random
import string
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_success(self):
        def setUp(self):
            # Create a new instance of the Chrome driver
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/")

        # Find the get_started button and click on it
        get_started = self.driver.find_element(By.CLASS_NAME, "blue-button")
        get_started.click()
        time.sleep(5)

        # navigate to login page
        self.driver.get("https://uat.businessbay.io/login")

        # Find the email and paswrd field
        email = self.driver.find_element(By.NAME, "email")
        paswrd = self.driver.find_element(By.NAME,"password")

        # Enter the username and password
        email.send_keys("wykumywav@yopmail.com")
        paswrd.send_keys("Aishu!123")

        # Find the login button and click on it
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[2]/form/div[5]/button')
        login_btn.click()
        time.sleep(5)

        # Refresh the page
        self.driver.refresh()
        time.sleep(4)


        # Assert that the page url is expected
        expected_url = "https://uat.businessbay.io/profile"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

        def tearDown(self):
            # Close the browser window
            self.driver.close()

    if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))













