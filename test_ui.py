from testpage import OperationsHelper
from postpage import OperationsAddPost
from contactpage import OperationsContact
import yaml
import logging
import time


with open("HW3/config.yaml") as f:
    testdata = yaml.safe_load(f)
    login = testdata["login"]
    password = testdata["pass"]
    title = testdata["title"]
    description = testdata["description"]
    contest = testdata["contest"]
    email = testdata["email"]
    message = testdata["message"]
def test_step1(browser):
    logging.info("test_1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("test_2 starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_auth_text() == f"Hello, {login}"

def test_step3(browser):
    logging.info("test_3 starting")
    testpage = OperationsAddPost(browser)
    testpage.click_create_new_post_button()
    testpage.enter_title(title)
    testpage.enter_description(description)
    testpage.enter_contest(contest)
    testpage.click_create_post_button()
    time.sleep(3)
    assert testpage.check_title_new_post() == title

def test_step4(browser):
    logging.info("test_4 starting")
    testpage = OperationsContact(browser)
    testpage.click_contact_button()
    testpage.enter_name_contact_us(login)
    testpage.enter_email_contact_us(email)
    testpage.enter_contact_us(message)
    time.sleep(3)
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.alert() == "Form successfully submitted"
