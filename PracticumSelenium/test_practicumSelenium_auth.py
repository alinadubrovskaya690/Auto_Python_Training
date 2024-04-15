from data import *
from locators import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_auth_ok_time_sleep(browser):
    browser.get(base_url)
    head_1 = browser.find_element(*header)
    assert head_1.text == header_text
    time.sleep(5)
    assert browser.find_element(*test_start).is_displayed() is True
    browser.find_element(*test_start).click()
    browser.find_element(*user_name).send_keys(valid_login)
    browser.find_element(*password).send_keys(valid_password)
    browser.find_element(*agree_checkbox).click()
    assert browser.find_element(*agree_checkbox).is_selected() is True
    browser.find_element(*register).click()
    load_id = browser.find_element(*loader)
    assert load_id.is_displayed() is True
    time.sleep(5)
    message = browser.find_element(*message_1)
    assert message.text == success_message


def test_auth_ok_implicitly_wait(browser):
    browser.implicitly_wait(5)
    browser.get(base_url)
    head_1 = browser.find_element(*header)
    assert head_1.text == header_text
    time.sleep(5)
    assert browser.find_element(*test_start).is_displayed() is True
    browser.find_element(*test_start).click()
    browser.find_element(*user_name).send_keys(valid_login)
    browser.find_element(*password).send_keys(valid_password)
    browser.find_element(*agree_checkbox).click()
    assert browser.find_element(*agree_checkbox).is_selected() is True
    browser.find_element(*register).click()
    load_id = browser.find_element(*loader)
    assert load_id.is_displayed() is True
    time.sleep(5)
    message = browser.find_element(*message_1)
    assert message.text == success_message


def test_auth_ok_wait(browser):
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    browser.get(base_url)
    head_1 = browser.find_element(*header)
    assert head_1.text == header_text
    wait.until(EC.visibility_of_element_located(test_start))
    assert browser.find_element(*test_start).is_displayed() is True
    browser.find_element(*test_start).click()
    browser.find_element(*user_name).send_keys(valid_login)
    browser.find_element(*password).send_keys(valid_password)
    browser.find_element(*agree_checkbox).click()
    assert browser.find_element(*agree_checkbox).is_selected() is True
    browser.find_element(*register).click()
    load_id = browser.find_element(*loader)
    assert load_id.is_displayed() is True
    wait.until(EC.visibility_of_element_located(message_1))
    message = browser.find_element(*message_1)
    assert message.text == success_message