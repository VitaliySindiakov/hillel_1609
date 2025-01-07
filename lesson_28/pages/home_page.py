from lesson_28.locators.home_page_locators import HomePageLocators
from lesson_28.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.pages.main_page import MainPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def sign_up_button(self) -> WebElement:
        return self._button(self.locators.sign_up_button, "Sing Up button")

    def click_sign_up_button(self):
        self.sign_up_button().click()

    def set_registration_name(self, name: str):
        return self._input_field(self.locators.registration_name, "Name").send_keys(name)

    def set_registration_last_name(self, last_name: str):
        return self._input_field(self.locators.registration_last_name, "Last Name").send_keys(last_name)

    def set_registration_email(self, email: str):
        return self._input_field(self.locators.registration_email, "Email").send_keys(email)

    def set_registration_password(self, password: str):
        return self._input_field(self.locators.registration_password, "Password").send_keys(password)

    def set_registration_reenter_password(self, reenter_password: str):
        return self._input_field(self.locators.registration_reenter_password, "reenter Password").send_keys(
            reenter_password)

    def register_button(self) -> WebElement:
        return self._button(self.locators.registration_register, "Register button")

    def click_registration(self) -> MainPage:
        self.register_button().click()
        return MainPage(self._driver)
