from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

about_text_1 = "Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance."
about_text_2 = "Watch over 100 instructions and repair your car yourself."

sign_up_button = webdriver.find_element(by=By.XPATH, value='//*[text()="Sign up"]')
sign_up_button.click()
registration_name = webdriver.find_element(by=By.XPATH, value='//label[text()="Name"]')
registration_last_name = webdriver.find_element(by=By.XPATH, value='//label[text()="Last name"]')
registration_email = webdriver.find_element(by=By.XPATH, value='//label[text()="Email"]')
registration_password = webdriver.find_element(by=By.XPATH, value='//label[text()="Password"]')
registration_reenter_password = webdriver.find_element(by=By.XPATH, value='//label[text()="Re-enter password"]')
registration_close = webdriver.find_element(by=By.XPATH, value='//*[@class="close"]')
registration_register = webdriver.find_element(by=By.XPATH, value='//*[text()="Register"]')
registration_close.click()

sign_in_button = webdriver.find_element(by=By.XPATH, value='//button[@class="btn btn-outline-white header_signin"]')
sign_in_button.click()
login_email = webdriver.find_element(by=By.XPATH, value='//input[@name="email"]')
login_password = webdriver.find_element(by=By.XPATH, value='//input[@name="password"]')
login_login_button = webdriver.find_element(by=By.XPATH,
                                            value='//div[contains(@class, "modal-footer")]/button[contains(@class, "btn-primary")]')
login_close_button = webdriver.find_element(by=By.XPATH, value='//div[@class="modal-header"]/button')
login_close_button.click()

guest_log_in_button = webdriver.find_element(by=By.XPATH, value='//app-header/header//button[text()="Guest log in"]')
about_button = webdriver.find_element(by=By.XPATH, value='//app-header/header//button[text()="About"]')
contacts_button = webdriver.find_element(by=By.XPATH, value='//app-header/header//button[text()="Contacts"]')
home_button = webdriver.find_element(by=By.XPATH, value='//app-header/header//*[@href="/" and text()="Home"]')
hillel_auto_header_link = webdriver.find_element(by=By.XPATH,
                                                 value='//app-header/header//*[@xmlns="http://www.w3.org/2000/svg"]/..')
support_hillel_link = webdriver.find_element(by=By.XPATH,
                                             value='//a[contains(@class, "contacts_link") and contains(. , "support")]')
footer_home_link = webdriver.find_element(by=By.XPATH, value='//a[@href="https://ithillel.ua"]')
footer_contacts_block = webdriver.find_element(by=By.XPATH, value='//div/h2[text()="Contacts"]')
footer_contacts_facebook_link = webdriver.find_element(by=By.XPATH,
                                                       value='//a[@href="https://www.facebook.com/Hillel.IT.School"]')
footer_contacts_telegram_link = webdriver.find_element(by=By.XPATH, value='//a[@href="https://t.me/ithillel_kyiv"]')
video_title = webdriver.find_element(by=By.XPATH,
                                     value='//div[@class="ytp-title-text"]/a[contains(@class, "yt-uix-sessionlink")]')
about_block_el_1: WebElement = webdriver.find_element(by=By.XPATH, value=f'//p[contains(. , "{about_text_1}")]')
about_block_el_2: WebElement = webdriver.find_element(by=By.XPATH, value=f'//p[contains(. , "{about_text_2}")]')

footer_contacts_section = webdriver.find_element(by=By.CSS_SELECTOR, value='#contactsSection')
footer_contacts_instagram_link = webdriver.find_element(by=By.CSS_SELECTOR, value='a[href*=instagram]')
footer_contacts_youtube_link = webdriver.find_element(by=By.CSS_SELECTOR, value='a[href*="youtube"].socials_link')
footer_contacts_linkedin_link = webdriver.find_element(by=By.CSS_SELECTOR, value='a[href*="linkedin"].socials_link')
header_sign_in_button = webdriver.find_element(by=By.CSS_SELECTOR, value='.header .header_signin')
header_guest_log_in_button = webdriver.find_element(by=By.CSS_SELECTOR, value='.header .-guest')

sign_up_button = webdriver.find_element(by=By.CSS_SELECTOR, value='.section.hero button')
sign_in_button.click()
registration_name = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="name"]')
registration_last_name = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="lastName"]')
registration_email = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]')
registration_password = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
registration_reenter_password = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="repeatPassword"]')
registration_register = webdriver.find_element(by=By.CSS_SELECTOR, value='.modal-footer button')
registration_close = webdriver.find_element(by=By.CSS_SELECTOR, value='.modal-header button')
registration_close.click()

sign_in_button = webdriver.find_element(by=By.CSS_SELECTOR, value='button.header_signin')
sign_in_button.click()
login_email = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]')
login_password = webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
login_login_button = webdriver.find_element(by=By.CSS_SELECTOR, value='div.modal-footer > button.btn-primary')
login_close_button = webdriver.find_element(by=By.CSS_SELECTOR, value='div.modal-header > button')
login_close_button.click()

support_hillel_link = webdriver.find_element(by=By.CSS_SELECTOR, value='a.contacts_link[href^="https"]')
video_title = webdriver.find_element(by=By.CSS_SELECTOR, value='.ytp-title-text .yt-uix-sessionlink')
about_button = webdriver.find_element(by=By.CSS_SELECTOR, value='.btn.header-link[appscrollto=aboutSection]')
contacts_button = webdriver.find_element(by=By.CSS_SELECTOR, value='.btn.header-link[appscrollto=contactsSection]')
header_logo_link = webdriver.find_element(by=By.CSS_SELECTOR, value='.header_logo[href="/"]')
home_button = webdriver.find_element(by=By.CSS_SELECTOR, value='nav [href="/"]')
youtube_video = webdriver.find_element(by=By.CSS_SELECTOR, value='#player .ytp-title a[href*=youtube]')
about_img_1 = webdriver.find_element(by=By.CSS_SELECTOR, value='.about-picture_img[src*=info_1]')
about_img_2 = webdriver.find_element(by=By.CSS_SELECTOR, value='.about-picture_img[src*=info_2]')

about_block_all_text: list[WebElement] = webdriver.find_elements(by=By.CSS_SELECTOR, value='.about-block_descr.lead')


def find_element_by_text(elements: list[WebElement], text: str) -> WebElement:
    for el in elements:
        if text == el.text:
            return el


about_block_el_1: WebElement = find_element_by_text(about_block_all_text, about_text_1)
about_block_el_2: WebElement = find_element_by_text(about_block_all_text, about_text_2)
