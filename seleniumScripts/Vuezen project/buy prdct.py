import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_success(self, proceed=None):
        # Navigate to the login page
        self.driver.get("https://test-vuezen.bastionex.net/login")

        # Wait for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Find the username and password fields
        username_field = self.driver.find_element(By.CLASS_NAME, "logform-input")
        password_field = self.driver.find_element(By.NAME, "password")

        # Enter the username and password
        username_field.send_keys("seltest@yopmail.com")
        password_field.send_keys("c2VsdGVz")

        # Find the submit button and click on it
        submit_button = self.driver.find_element(By.CLASS_NAME, "login-button")
        submit_button.click()
        time.sleep(5)

        # Find the dropdown and assign it to self.click_button
        click_button = self.driver.find_element(By.ID, "basic-nav-dropdown")
        click_button.click()

        # Click on the second child element
        second_child_xpath = "//*[@id='basic-navbar-nav']/div/div[2]/div/a[2]"
        second_child_element = self.driver.find_element(By.XPATH, second_child_xpath)
        second_child_element.click()
        time.sleep(3)

        # Scroll to the "Buy Now" button
        buy = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]//button[contains(text(), "Buy Now")]')
        actions = ActionChains(self.driver)
        actions.move_to_element(buy).perform()
        time.sleep(3)  # Optional: Wait for a second after scrolling

        # Click on the "Buy Now" button
        buy.click()

        # Navigate to checkout page
        # self.driver.get("https://test-vuezen.bastionex.net/checkout")
        time.sleep(2)

        # Click on address button
        address = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[1]/div[1]/div')
        address.click()
        # time.sleep(5)

        # Find the address form fields
        fullname_field = self.driver.find_element(By.NAME, "full_name")
        country_field = self.driver.find_element(By.NAME, "country")
        address_field = self.driver.find_element(By.NAME, "address")
        zipcode_field = self.driver.find_element(By.NAME, "zipcode")
        city_field = self.driver.find_element(By.NAME, "city")
        state_field = self.driver.find_element(By.NAME, "state")

        # Fix the phone number field selector
        try:
            phone_number_field = self.driver.find_element(By.CLASS_NAME, "form-control")
        except NoSuchElementException:
            print("Phone number field not found!")
            return

        # fill in the address form
        fullname_field.send_keys("Ishu sharma")
        country_field.send_keys("India")
        address_field.send_keys("bnbnuuy2232hghg")
        zipcode_field.send_keys("201301")
        city_field.send_keys("noida")
        state_field.send_keys("uttar pradesh")
        phone_number_field.send_keys("9878787878")

        # Scroll to save button
        save_button = self.driver.find_element(By.XPATH, '//*[@id="addform"]/div/div[9]')
        actions_savebtn = ActionChains(self.driver)
        actions_savebtn.move_to_element(save_button).perform()

        # Click on save button
        save_button.click()
        time.sleep(5)
        # find check_box and click on it
        # check_box = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[2]/div[6]/div[3]/input')
        # check_box.click()
        parent_div = self.driver.find_element(By.CLASS_NAME, "agree-check")

        # Find the checkbox input element within the parent div
        c = parent_div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        #c = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[2]/div[6]/div[3]/input')
        actions_chkbx = ActionChains(self.driver)
        actions_chkbx.move_to_element(c).perform()
        #time.sleep(5)
        if c.is_selected():
            print("Checkbox is selected!")
        # Check if the checkbox is already selected
        if not c.is_selected():
            # If not selected, click on it to tick the checkbox
            c.click()



        #time.sleep(5)

        # Find Proceed_to_checkout button and click on it
        proceed_to_checkout = self.driver.find_element(By.CLASS_NAME, 'proceed-button')
        action_prcd = ActionChains(self.driver)
        action_prcd.move_to_element(proceed_to_checkout).perform()
        proceed_to_checkout.click()
        time.sleep(5)

        pprnt_div = self.driver.find_element(By.CLASS_NAME, 'swal2-actions')
        # Find the checkbox input element within the parent div
        childprbt = pprnt_div.find_element(By.XPATH, "button[@class='swal2-confirm swal2-styled' and text()='Proceed']")
        childprbt.click()
        time.sleep(2)

        # Scroll to order placed successfully toast msg
        #order_plcss= self.driver.find_element(By.XPATH, "//div[contains(text(), 'Order Placed successfully')]")


            # Find the expected pop-up
               # expected_pop_up = "Order Placed Successfully"
               # actual_pop_up = self.driver.find_element(By.XPATH, '//*[@id="2"]/div[1]/div[2]')
               # self.assertEqual(expected_toast_msg, actual_toast_msg.text, "Toast message is not as expected")

         # Assert that the page url is as expected
        expected_url = "https://test-vuezen.bastionex.net/orderhistory"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Page url is not as expected")







    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
