from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml

class PostSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])
    # LOCATOR_CREATE_NEW_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    # LOCATOR_ENTER_TITLE_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    # LOCATOR_ENTER_DESCRIPTION_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    # LOCATOR_ENTER_CONTENT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    # LOCATOR_CREATE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    # LOCATOR_CHECK_CREATE_POST_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')

class OperationsAddPost(BasePage):
    # Enter text

    def enter_title(self, word):
        return self.enter_text_into_field(PostSearchLocators.ids["LOCATOR_ENTER_TITLE_FIELD"], word,
                                          description="enter title new post")

    def enter_description(self, word):
        return self.enter_text_into_field(PostSearchLocators.ids["LOCATOR_ENTER_DESCRIPTION_FIELD"], word,
                                          description="enter description new_post")

    def enter_contest(self, word):
        return self.enter_text_into_field(PostSearchLocators.ids["LOCATOR_ENTER_CONTENT_FIELD"], word,
                                          description="enter contest new_post")


    # Click
    def click_create_new_post_button(self):
        return self.click_button(PostSearchLocators.ids["LOCATOR_CREATE_NEW_POST_BTN"],
                                 description="click button create new post")

    def click_create_post_button(self):
        return self.click_button(PostSearchLocators.ids["LOCATOR_CREATE_BTN"], description="click button create")

    #   GET
    def check_title_new_post(self):
        return self.get_text_from_element(PostSearchLocators.ids["LOCATOR_CHECK_CREATE_POST_FIELD"],
                                          description="post name")
