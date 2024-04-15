from data import *
from locators import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import *
from selenium.webdriver.support import expected_conditions as EC



def test_auth_alert(browser, exp_wait):
    browser.get(auth_url)
    try:
        exp_wait.until(EC.alert_is_present())
        browser.switch_to.alert.accept()
    except (NoAlertPresentException, TimeoutException):
        pass
    else:
        print('No alert is displayed')


def test_auth_dialog_window(browser):
    browser.get(user_url)
    head = browser.find_element(*head_1)
    assert head.text == head_line
    message = browser.find_element(*message_1)
    assert message.text == message_line