from lesson_27.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def track_form_input(self) -> WebElement:
        return (WebDriverWait(self.driver, 1)
                .until(EC.presence_of_element_located((By.CLASS_NAME, 'track__form-group-input'))))

    def search_submit_button(self) -> WebElement:
        return (WebDriverWait(self.driver, 1)
                .until(EC.presence_of_element_located((By.ID, 'np-number-input-desktop-btn-search-en'))))

    def tracking_row_text(self) -> WebElement:
        return (WebDriverWait(self.driver, 1)
                .until(EC.presence_of_element_located((By.CLASS_NAME, 'tracking__row'))))
