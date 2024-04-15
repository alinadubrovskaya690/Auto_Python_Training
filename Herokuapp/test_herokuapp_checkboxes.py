from data import *
from locators import *



def test_checkboxes(browser):
    browser.get(checkboxes_url)
    browser.find_element(*checkbox_1).click()
    assert browser.find_element(*checkbox_1).is_selected() is True
    browser.find_element(*checkbox_2).click()
    assert browser.find_element(*checkbox_2).is_selected() is False
    browser.find_element(*checkbox_1).click()
    assert browser.find_element(*checkbox_1).is_selected() is False
    browser.find_element(*checkbox_2).click()
    assert browser.find_element(*checkbox_2).is_selected() is True