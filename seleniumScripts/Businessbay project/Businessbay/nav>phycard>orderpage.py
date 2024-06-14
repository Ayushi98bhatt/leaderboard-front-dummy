import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_success(self):
        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/")

        # Find the get_started button and click on it
        get_started = self.driver.find_element(By.CLASS_NAME, "blue-button")
        get_started.click()
        time.sleep(5)

        # navigate to login page
        self.driver.get("https://uat.businessbay.io/login")

        # Find the email and password fields
        email = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")

        # Enter the username and password
        email.send_keys("fyseciwyha@yopmail.com")
        password.send_keys("Pa$$w0rd!")

        # Find the login button and click on it
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[2]/form/div[5]/button')
        login_btn.click()
        time.sleep(5)

        # Refresh the page
        self.driver.refresh()
        time.sleep(4)

        # Find the dropdown and assign it to self.click_button
        wait = WebDriverWait(self.driver, 10)
        pcards = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app_sidebarStyle_maincontainer"]/ul/li[4]/a/span')))
        pcards.click()

        # Click on the second child element
        second_child_xpath = '//*[@id="app_sidebarStyle_maincontainer"]/ul/li[4]/ul/li[1]/a'
        second_child_element = wait.until(EC.element_to_be_clickable((By.XPATH, second_child_xpath)))
        second_child_element.click()
        time.sleep(3)

        # Select an option from the dropdown
        selbus = self.driver.find_element(By.XPATH, '//*[@id="OrderNowPhysicalcardwrapper"]/div[1]/select')
        select = Select(selbus)
        select.select_by_visible_text("cxvbnfdghjk")

        # Find the order button and click on it
        order_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "PhysicalcardOrdernow")))
        order_btn.click()
        time.sleep(5)

        # Assert that the page url is expected
        # expected_url = "https://uat.businessbay.io/ordernow?"
        # actual_url = self.driver.current_url
        # self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        # Close the browser window
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))
