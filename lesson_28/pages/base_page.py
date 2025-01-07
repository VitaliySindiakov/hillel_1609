from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.locators.home_page_locators import HomePageLocators


class BasePage:
    def __init__(self, driver: webdriver):
        self._driver: webdriver = driver
        self._url = "https://guest:welcome2qauto@qauto2.forstudy.space/"

    def open_page(self, url=None):
        url = url or self._url
        self._driver.get(url)

    def check_is_correct_url(self):
        assert self._driver.current_url in self._url, (f'Expected urls is {self._url}, '
                                                       f'but actual url is {self._driver.current_url}')

    def _present_element(self, locator, message='', timeout=1):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)

    def _input_field(self, locator, element_name='',
                     timeout=2) -> WebElement:  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=f"Can't find Element {element_name}")

    def _button(self, locator, element_name='', timeout=1) -> WebElement:  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=f"Element {element_name} isn't clickable")
