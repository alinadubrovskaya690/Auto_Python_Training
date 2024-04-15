from data import *
from locators import *
import time



def test_remove_item(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_link).click()
    assert browser.current_url == item1_url
    browser.find_element(*add_item1).click()
    browser.find_element(*remove_item1).click()


def test_remove_item_main(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*add_item2).click()
    browser.find_element(*remove_item2).click()


def test_remove_item_cart(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_img_link).click()
    assert browser.current_url == item1_url
    browser.find_element(*add_item1).click()
    browser.find_element(*cart_link).click()
    assert browser.current_url == cart_url
    browser.find_element(*remove_item2).click()