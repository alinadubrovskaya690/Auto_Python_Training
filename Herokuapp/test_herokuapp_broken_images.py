import requests
from data import *
from locators import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_broken_images(browser):
    browser.get(broken_img_url)
    images = browser.find_elements(By.TAG_NAME, "img")
    broken_images = []
    for image in images:
        src = image.get_attribute("src")
        if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f"Broken image found")
    if broken_images:
        print("list of broken images:")
        for broken_image in broken_images:
            print(broken_image)
    else:
        print("No broken images found")