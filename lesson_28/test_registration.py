import pytest
from selenium.webdriver import Chrome, ChromeOptions
from lesson_28.pages.home_page import HomePage
import random

from lesson_28.pages.main_page import MainPage


@pytest.fixture(scope='session')
def driver_session():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='session')
def home_page_session(driver_session):
    home_page: HomePage = HomePage(driver_session)
    home_page.open_page()
    home_page.check_is_correct_url()
    return home_page


def test_registration(driver_session, home_page_session):
    home_page_session.click_sign_up_button()
    rnd = random.randint(0, 1000)
    home_page_session.set_registration_name("Vitalii")
    home_page_session.set_registration_last_name("Sindiakov")
    home_page_session.set_registration_email("Vitalii" + str(rnd) + "@gmail.com")
    home_page_session.set_registration_password("Ab!123456" + str(rnd))
    home_page_session.set_registration_reenter_password("Ab!123456" + str(rnd))

    main_page: MainPage = home_page_session.click_registration()
    main_page.check_is_correct_url()

    # можливо краще було б загорнути в методи, але залишив для наглядності
    assert "Garage" in main_page.main_content_block().text
    assert main_page.profile_dropdown().is_displayed()
