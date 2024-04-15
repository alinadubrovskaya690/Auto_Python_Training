import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import *
from locators import *

@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--window-size=1200,800')

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(7)

    yield browser
    browser.quit()