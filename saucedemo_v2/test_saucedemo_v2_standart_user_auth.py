from data import *
from locators import *
import time



def test_auth_ok(browser, auth):
    assert browser.current_url == inventory_url, 'Not this URL'


def test_auth_not_ok(browser):
    browser.get(base_url)
    browser.find_element(*user_name).send_keys(invalid_login)
    browser.find_element(*password).send_keys(invalid_password)
    browser.find_element(*login).click()
    assert browser.current_url == base_url, 'Not this URL'
    message = browser.find_element(*error_message)
    assert message.text == error_message_auth1, 'OK'


def test_auth_empty(browser):
    browser.get(base_url)
    browser.find_element(*login).click()
    assert browser.current_url == base_url, 'Not this URL'
    message = browser.find_element(*error_message)
    assert message.text == error_message_auth2, 'OK'


def test_auth_ok_and_not_ok(browser):
    browser.get(base_url)
    browser.find_element(*user_name).send_keys(valid_login)
    browser.find_element(*password).send_keys(invalid_password)
    browser.find_element(*login).click()
    assert browser.current_url == base_url, 'Not this URL'
    message = browser.find_element(*error_message)
    assert message.text == error_message_auth1, 'OK'


def test_auth_not_ok_and_empty(browser):
    browser.get(base_url)
    browser.find_element(*user_name).send_keys(invalid_login)
    browser.find_element(*login).click()
    assert browser.current_url == base_url, 'Not this URL'
    message = browser.find_element(*error_message)
    assert message.text == error_message_auth3, 'OK'


def test_auth_empty_and_ok(browser):
    browser.get(base_url)
    browser.find_element(*password).send_keys(valid_password)
    browser.find_element(*login).click()
    assert browser.current_url == base_url, 'Not this URL'
    message = browser.find_element(*error_message)
    assert message.text == error_message_auth2, 'OK'