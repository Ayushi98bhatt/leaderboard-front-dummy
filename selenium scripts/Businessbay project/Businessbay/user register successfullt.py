import random
import string
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


# Function to generate random phone number
def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))


class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_register_user(self):
        self.driver.get("https://uat.businessbay.io/")

        get_started = self.driver.find_element(By.CLASS_NAME, "blue-button")
        get_started.click()

        register_here = self.driver.find_element(By.CLASS_NAME, "registerhere")
        register_here.click()

        name_field = self.driver.find_element(By.NAME, "name")
        email_field = self.driver.find_element(By.NAME, "email")
        phn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[3]/div/input')
        pass_field = self.driver.find_element(By.NAME, "password")
        confpas_field = self.driver.find_element(By.NAME, "confirmPassword")

        # Generate random data
        random_name = generate_random_string(8)
        random_email = generate_random_string(8) + "@yopmail.com"
        random_phone = generate_random_phone_number()
        random_password = generate_random_string(8) + "@0000"

        name_field.send_keys(random_name)
        email_field.send_keys(random_email)
        phn.send_keys(random_phone)
        pass_field.send_keys(random_password)
        confpas_field.send_keys(random_password)

        seltyp = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[6]/select')
        select = Select(seltyp)
        select.select_by_visible_text("Individual")

        regtr = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[8]/button')
        regtr.click()
        time.sleep(4)



        prnt_pop = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[9]')
        # actual_pop = self.driver.find_element(By.CSS_SELECTOR, "div:contains('Verification email sent')")
        # Wait until the current URL changes to the login page

        expected_pop_up = "Verification email sent"
        self.assertEqual(expected_pop_up, expected_pop_up, "Toast message is not as expected")
        # Refresh the page
        self.driver.refresh()
        time.sleep(4)

        # Assert that the page url is expected
        expected_url = "https://uat.businessbay.io/register"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="."))
