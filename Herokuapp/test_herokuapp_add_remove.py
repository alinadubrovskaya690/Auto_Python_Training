from data import *
from locators import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_add_remove(browser):
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    browser.get(add_remove_url)
    wait.until(EC.element_to_be_clickable(add_button)).click()
    assert browser.find_element(*delete_button).is_displayed()
    wait.until(EC. element_to_be_clickable(delete_button)).click()
    assert wait.until(EC. invisibility_of_element(delete_button))