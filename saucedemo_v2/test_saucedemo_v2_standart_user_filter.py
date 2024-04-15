from data import *
from locators import *
import time



def test_filter_lowhigh(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*filter).click()
    browser.find_element(*lowhigh).click()
    p1 = browser.find_element(*price1)
    assert p1.text == price1_lowhigh
    p6 = browser.find_element(*price6)
    assert p6.text == price6_lowhigh


def test_filter_highlow(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*filter).click()
    browser.find_element(*highlow).click()
    p1 = browser.find_element(*price1)
    assert p1.text == price1_highlow
    p6 = browser.find_element(*price6)
    assert p6.text == price6_highlow


def test_filter_az(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*filter).click()
    browser.find_element(*az).click()
    n1 = browser.find_element(*name1)
    assert n1.text == name1_az
    n6 = browser.find_element(*name6)
    assert n6.text == name6_az


def test_filter_za(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*filter).click()
    browser.find_element(*za).click()
    n1 = browser.find_element(*name1)
    assert n1.text == name1_za
    n6 = browser.find_element(*name6)
    assert n6.text == name6_za