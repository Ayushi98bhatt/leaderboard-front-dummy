from selenium.webdriver.common.by import By

class RegstrPageLocators:
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PHN_FIELD = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/form/div[3]/div/input')
    PASS_FIELD = (By.NAME, "password")
    CONFIRM_PASS_FIELD = (By.NAME, "confirmPassword")

class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
