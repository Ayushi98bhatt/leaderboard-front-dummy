import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_create_business_success(self):
        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/")

        # Use WebDriverWait to wait for the get_started button to be clickable
        wait = WebDriverWait(self.driver, 10)  # Increased timeout for reliability
        try:
            get_started = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "blue-button")))
            get_started.click()
        except Exception as e:
            print(f"Exception encountered while trying to find 'get_started' button: {e}")
            self.fail("Unable to find 'get_started' button")

        #time.sleep(2)

        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/login")

        # Find the email and password fields
        email = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")

        # Enter the username and password
        email.send_keys("tytyjyna@yopmail.com")
        password.send_keys("Pa$$w0rd!")

        # Find the login button and click on it
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[2]/form/div[5]/button')
        login_btn.click()
        #time.sleep(2)

        # Refresh the page
        self.driver.refresh()
        #time.sleep(2)

        # Find the create_btn and click on it
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/header')))
        create_btn.click()

        # Click on the second child element
        second_child_xpath = '//*[@id="MobileBaarview"]/a'
        second_child_element = wait.until(EC.element_to_be_clickable((By.XPATH, second_child_xpath)))
        second_child_element.click()
        #time.sleep(5)

        # Find enter business name text field and send keys
        enterb_nam = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/input')

        # Enter the value
        enterb_nam.send_keys("autotest")

        # Find the template and click on it
        template = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[4]')))
        template.click()

        # Click on the second child element
        second_child_xpath = '//*[@id="div3"]/div/img'
        second_child_element = wait.until(EC.element_to_be_clickable((By.XPATH, second_child_xpath)))
        second_child_element.click()
        #time.sleep(3)

        # Find the create button and click on it
        create = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/header')))
        create.click()

        # Click on the second child element
        second_child_xpath = '//*[@id="CreateandNextButton"]'
        second_child_element = wait.until(EC.element_to_be_clickable((By.XPATH, second_child_xpath)))
        second_child_element.click()
        #time.sleep(3)


        # Assert that the page url is as expected
        expected_url = "https://uat.businessbay.io/business?id=634"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()  # Changed to quit() to close all browser windows


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))
