import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import os
class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_create_business_success(self):
        # Navigate to the login page
        #self.driver.get("https://uat.businessbay.io/")

        #time.sleep(2)

        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/login")

        # Find the email and password fields
        email = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")

        # Enter the username and password
        email.send_keys("fyseciwyha@yopmail.com")
        password.send_keys("Pa$$w0rd!")
        time.sleep(2)
        # Find the login button and click on it
        lb = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[5]')
        lb.click()
        #time.sleep(2)

        # Refresh the page
        #self.driver.refresh()
        #time.sleep(2)

        # Find the create_btn and click on it
        create_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MobileBaarview"]/a')))
        create_btn.click()

        # Find enter business name text field and send keys
        ebn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/input')
        ebn.send_keys("nbnbn")

        # select category and select one option
        category = self.driver.find_element(By.XPATH,
                                            '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]')
        category.click()
        option = self.driver.find_element(By.XPATH,
                                          '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/select/option[2]')
        option.click()
        theme = self.driver.find_element(By.XPATH,
                                         '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[1]/div/div[1]/div[3]')
        theme.click()

        #  logo = self.driver.find_element(By.XPATH, '')

        createbtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div[5]/div/div')
        createbtn.click()
        time.sleep(10)
        # savandprev = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div/div[2]/div/div/p')
        # savandprev.click()
        # time.sleep(10)

        expected_toast_msg = "Business created successfully"
        actual_toast_msg = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]')

        self.assertEqual(expected_toast_msg, actual_toast_msg.text, "Business created successfully")


    def test_add_businessdetails_success(self):
        # Find the details 
        designation = self.driver.find_element(By.CLASS_NAME, "form-control")
        des = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/main/div[3]/div/div/div/div[2]/div[1]/div[1]/div/form/div[3]/textarea')

        # Enter the details
        designation.send_keys("QA")
        des.send_keys("Hey I am using this for testing experience")









        # Assert that the page url is as expected
        expected_url = "https://uat.businessbay.io/business?id=634"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()  # Changed to quit() to close all browser windows


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))
