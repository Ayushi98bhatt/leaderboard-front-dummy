import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_success(self, expected_toast_msg=None, actual_toast_msg=None):
        # Navigate to the login page
        self.driver.get("https://uat.businessbay.io/")

        # Find the get_started button and click on it
        get_started = self.driver.find_element(By.CLASS_NAME, "blue-button")
        get_started.click()
        #time.sleep(2)

        # Find register_here button and click on it
        register_here = self.driver.find_element(By.CLASS_NAME, "registerhere")
        register_here .click()
        #time.sleep(5)

        # Find the registration form
        name_field = self.driver.find_element(By.NAME, "name")
        email_field = self.driver.find_element(By.NAME, "email")
        phn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[3]/div/input')
        pass_field = self.driver.find_element(By.NAME,"password")
        confpas_field = self.driver.find_element(By.NAME, "confirmPassword")

        # fill the registration form

        name_field.send_keys("autotest")
        email_field.send_keys("nmn677nnm@yopmail.com")
        phn.send_keys("9898989898")
        pass_field.send_keys("Aishu@0000")
        confpas_field.send_keys("Aishu@0000")

        seltyp = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[6]/select')
        seltyp.click()
        select = Select(seltyp)
        # Select an option by its text
        select.select_by_visible_text("Individual")
        #indv = seltyp.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[6]/select/option[2]')
        #indv.click()
        #time.sleep(3)




        # click  on the regtr_button
        regtr = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[8]/button')
        action = ActionChains(self.driver)
        action.move_to_element(regtr).perform()
        regtr.click()
        time.sleep(5)

        # Find the expected pop-up
        expected_pop_up = "Verification email sent"
        prnt_pop = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[9]')
        time.sleep(4)
        actual_pop = self.driver.find_element(By.CSS_SELECTOR, "div:contains('Verification email sent')")

        print("Actual toast message:", actual_pop.text)  # Add this line to print the actual toast message


        self.assertEqual(expected_pop_up, actual_pop.text, "Toast message is not as expected")

        expected_url = "https://uat.businessbay.io/login"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")

    def tearDown(self):
        # Close the browser window
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./test-reports"))
