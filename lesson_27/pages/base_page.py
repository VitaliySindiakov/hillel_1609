from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver: webdriver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_page(self, url=None):
        url = url or self.url
        self.driver.get(url)
