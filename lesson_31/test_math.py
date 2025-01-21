import allure
import pytest


@allure.epic('Unit tests')
@allure.feature('Math')
@allure.story('check equals')
@allure.title("check number")
@pytest.mark.math
def test_math():
    assert 1 == 1

@allure.title("check number 2")
@pytest.mark.math
def test_math_2():
    assert 1 == 1