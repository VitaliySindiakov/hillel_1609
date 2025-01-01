from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = Chrome()


def check_frame(frame: str):
    driver.switch_to.frame(driver.find_element(By.ID, frame.lower()))
    text_input: WebElement = driver.find_element(By.ID, f"input{frame[-1]}")
    check_button: WebElement = driver.find_element(By.XPATH,
                                                   f'//body[contains(. , "{frame}")]//button[. = "Перевірити"]')
    text_input.send_keys(f"{frame}_Secret")
    check_button.click()
    alert = Alert(driver)
    sleep(1)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    text_input.send_keys("Not Secret")
    check_button.click()
    sleep(1)
    assert alert.text == "Введено неправильний текст!"
    alert.accept()
    driver.switch_to.default_content()


try:
    driver.get("http://localhost:8000/html_pages/dz.html")
    driver.fullscreen_window()
    sleep(5)
    check_frame("Frame1")
    sleep(2)
    check_frame("Frame2")
finally:
    driver.close()
