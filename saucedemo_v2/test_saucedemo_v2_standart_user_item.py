from data import *
from locators import *
import time



def test_select_item_by_name(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_link).click()
    assert browser.current_url == item1_url
    iname = browser.find_element(*item_title)
    assert iname.text == item1_name
    idesc = browser.find_element(*item_desc)
    assert idesc.text == item1_descrip
    iprice = browser.find_element(*item_price)
    assert iprice.text == item1_price
    iimg = browser.find_element(*item_img)
    assert iimg.get_dom_attribute('src') == item1_image


def test_select_item_by_image(browser, auth):
    browser.get(inventory_url)
    browser.find_element(*item_img_link).click()
    assert browser.current_url == item1_url
    iname = browser.find_element(*item_title)
    assert iname.text == item1_name
    idesc = browser.find_element(*item_desc)
    assert idesc.text == item1_descrip
    iprice = browser.find_element(*item_price)
    assert iprice.text == item1_price
    iimg = browser.find_element(*item_img)
    assert iimg.get_dom_attribute('src') == item1_image