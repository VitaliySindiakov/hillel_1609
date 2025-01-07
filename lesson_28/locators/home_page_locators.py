from selenium.webdriver.common.by import By


class HomePageLocators:
    sign_up_button = (By.XPATH, '//*[text()="Sign up"]')
    registration_name = (By.ID, 'signupName')
    registration_last_name = (By.ID, 'signupLastName')
    registration_email = (By.ID, 'signupEmail')
    registration_password = (By.ID, 'signupPassword')
    registration_reenter_password = (By.ID, 'signupRepeatPassword')
    registration_close = (By.XPATH, '//*[@class="close"]')
    registration_register = (By.XPATH, '//*[text()="Register"]')
