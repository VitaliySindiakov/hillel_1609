import allure
import pytest


@allure.epic('Unit tests')
@allure.feature('Math')
@allure.story('check equals')
@allure.title("check number")
@pytest.mark.math
def test_math(driver):
    assert 1 == 1


@allure.title("just a failed test")
@pytest.mark.math
def test_failedtests():
    assert 1 == 2
