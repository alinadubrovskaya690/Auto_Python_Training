from data import *
from locators import *
import time



def test_cart_checkout_all_items(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*add_item2).click()
    browser.find_element(*add_item3).click()
    browser.find_element(*add_item4).click()
    browser.find_element(*add_item5).click()
    browser.find_element(*add_item6).click()
    browser.find_element(*add_item7).click()
    browser.find_element(*cart_link).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_link).click()
    assert browser.current_url == checkout_step1
    browser.find_element(*checkout_first_name).send_keys(valid_first_name)
    browser.find_element(*checkout_last_name).send_keys(valid_last_name)
    browser.find_element(*checkout_postal_code).send_keys(valid_postal_code)
    browser.find_element(*continue_link).click()
    assert browser.current_url == checkout_step2
    browser.find_element(*finish_link).click()
    assert browser.current_url == finish_url
    browser.find_element(*return_link).click()
    assert browser.current_url == inventory_url


def test_cart_checkout_one_item(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*add_item2).click()
    browser.find_element(*cart_link).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_link).click()
    assert browser.current_url == checkout_step1
    browser.find_element(*checkout_first_name).send_keys(invalid_first_name)
    browser.find_element(*checkout_last_name).send_keys(invalid_last_name)
    browser.find_element(*checkout_postal_code).send_keys(invalid_postal_code)
    browser.find_element(*continue_link).click()
    assert browser.current_url == checkout_step2
    browser.find_element(*finish_link).click()
    assert browser.current_url == finish_url
    browser.find_element(*return_link).click()
    assert browser.current_url == inventory_url


def test_cart_checkout_two_items(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*add_item2).click()
    browser.find_element(*add_item3).click()
    browser.find_element(*cart_link).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_link).click()
    assert browser.current_url == checkout_step1
    browser.find_element(*continue_link).click()
    message = browser.find_element(*checkout_empty_error)
    assert message.text == error_message_checkout1, 'OK'


def test_cart_checkout_empty_order(browser, auth):
    browser.get(cart_url)
    browser.find_element(*checkout_link).click()
    assert browser.current_url == checkout_step1
    browser.find_element(*checkout_first_name).send_keys(valid_first_name)
    browser.find_element(*checkout_last_name).send_keys(invalid_last_name)
    browser.find_element(*continue_link).click()
    message = browser.find_element(*checkout_empty_error)
    assert message.text == error_message_checkout3, 'OK'