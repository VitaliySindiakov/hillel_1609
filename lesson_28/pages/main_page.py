from lesson_28.locators.main_page_locators import MainPageLocators
from lesson_28.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self._url = self._url + "panel/garage"

    def main_content_block(self) -> WebElement:
        return self._present_element(self.locators.main_content)

    def profile_dropdown(self) -> WebElement:
        return self._present_element(self.locators.profile_dropdown)
