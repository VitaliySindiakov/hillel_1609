import allure
import pytest
from selenium.webdriver import Chrome, ChromeOptions
from lesson_31.pages.home_page import HomePage


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.close()


@allure.epic('UI tests')
@allure.feature('Nova Posta')
@allure.story('Track package')
@allure.title("check track number")
@pytest.mark.posta
def test_nova_poshta_tracking(driver):
    home_page = HomePage(driver)

    home_page.open_page()

    tracking_number: str = "123435566758769"

    track_form_input = home_page.track_form_input()
    track_form_input.send_keys(tracking_number)

    submit_button = home_page.search_submit_button()
    assert submit_button.is_enabled()
    submit_button.click()

    assert "Ми не знайшли посилку за таким номером" in home_page.tracking_row_text().text


@allure.title("just a failed test")
@pytest.mark.posta
def test_failedtests():
    assert 1 == 2
