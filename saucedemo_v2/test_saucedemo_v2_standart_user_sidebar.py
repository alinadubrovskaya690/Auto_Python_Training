from data import *
from locators import *
import time



def test_sidebar_inventory(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*sidebar_menu).click()
    browser.find_element(*sidebar_inv).click()
    assert browser.current_url == inventory_url

def test_sidebar_logout(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*sidebar_menu).click()
    browser.find_element(*sidebar_logout).click()
    assert browser.current_url == base_url

def test_sidebar_about(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*sidebar_menu).click()
    browser.find_element(*sidebar_about).click()
    assert browser.current_url == main_url

def test_sidebar_reset(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*sidebar_menu).click()
    browser.find_element(*sidebar_reset).click()
    assert browser.current_url == inventory_url

