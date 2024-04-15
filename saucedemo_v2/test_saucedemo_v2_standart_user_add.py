from data import *
from locators import *
import time



def test_add_item_by_name(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_link).click()
    assert browser.current_url == item1_url
    browser.find_element(*add_item1).click()


def test_add_item(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*add_item2).click()


def test_add_item_by_image(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_img_link).click()
    assert browser.current_url == item1_url
    browser.find_element(*add_item1).click()