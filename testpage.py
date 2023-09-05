from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml

class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])

    # LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    # LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    # LOCATOR_ERR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    # LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    # LOCATOR_AUTH_FIELD = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')

class OperationsHelper(BasePage):

    # Enter text
    def enter_login(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"], word,
                                          description="password form")


    #Click
    def click_login_button(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="button login")

    #   GET
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERR_FIELD"], description="error text")


    def get_auth_text(self):
        auth_check = self.find_element(TestSearchLocators.ids["LOCATOR_AUTH_FIELD"], time=3)
        return auth_check.text
