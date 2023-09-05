from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class ContactLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])
    # LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    # LOCATOR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    # LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    # LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    # LOCATOR_CONTACT_US_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class OperationsContact(BasePage):
    # Enter text
    def enter_name_contact_us(self, word):
        return self.enter_text_into_field(ContactLocators.ids["LOCATOR_NAME_FIELD"], word, description="enter contact name")

    def enter_email_contact_us(self, word):
        return self.enter_text_into_field(ContactLocators.ids["LOCATOR_EMAIL_FIELD"], word, description="enter contact email")

    def enter_contact_us(self, word):
        return self.enter_text_into_field(ContactLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                          description="enter content contact")

    # Click
    def click_contact_button(self):
        return self.click_button(ContactLocators.ids["LOCATOR_CONTACT_BTN"], description="button contact")

    def click_contact_us_button(self):
        return self.click_button(ContactLocators.ids["LOCATOR_CONTACT_US_BTN"], description="button contact us")

    #   GET
    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text

