from selenium import webdriver
import time
import pytest

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")

def test_auth_ok():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('standart_user')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('secret_sauce')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'Not this URL'

def test_auth_not_ok():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('Abc123')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('Abc123')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Epic sadface: Username and password do not match any user in this service', 'OK'

def test_auth_empty():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Epic sadface: Username is required', 'OK'

def test_auth_ok_and_not_ok():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('standart_user')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('Abc123')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Epic sadface: Username and password do not match any user in this service', 'OK'

def test_auth_not_ok_and_empty():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('Abc123')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Epic sadface: Password is required', 'OK'

def test_auth_empty_and_ok():
    user_name = driver.find_element('xpath', '//*[@id="user-name"]')
    user_name.send_keys('')
    time.sleep(2)
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys('secret_sauce')
    time.sleep(2)
    login = driver.find_element('xpath', '//*[@id="login-button"]')
    login.click()
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Epic sadface: Username is required', 'OK'

def test_item_select_by_name():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    item = driver.find_element('xpath', '//*[@id="item_4_title_link"]')
    item.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', 'Not this URL'
    item_name = driver.find_element('xpath', '//*[@class="inventory_details_name"]')
    item_image = driver.find_element('xpath', '//*[@class="inventory_details_img"]')
    assert item_name.text == 'Sauce Labs Backpack', 'Not that name'
    assert item_image.get_dom_attribute('src') == './img/sauce-backpack-1200x1500.jpg', 'Not that image'

def test_item_select_by_image():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    item = driver.find_element('xpath', '(//*[@class="inventory_item_img"])[1]')
    item.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', 'Not this URL'
    item_name = driver.find_element('xpath', '//*[@class="inventory_details_name"]')
    item_image = driver.find_element('xpath', '//*[@class="inventory_details_img"]')
    assert item_name.text == 'Sauce Labs Backpack', 'Not that name'
    assert item_image.get_dom_attribute('src') == './img/sauce-backpack-1200x1500.jpg', 'Not that image'

def test_add1():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    item = driver.find_element('xpath', '//*[@id="item_4_title_link"]')
    item.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4'
    add = driver.find_element('xpath', '//*[@class="btn_primary btn_inventory"]')
    add.click()
    time.sleep(2)

def test_add2():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)

def test_remove1():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    item = driver.find_element('xpath', '//*[@id="item_4_title_link"]')
    item.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4'
    add = driver.find_element('xpath', '//*[@class="btn_primary btn_inventory"]')
    add.click()
    time.sleep(2)
    remove = driver.find_element('xpath', '//*[@class="btn_secondary btn_inventory"]')
    remove.click()
    time.sleep(2)

def test_remove2():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    remove = driver.find_element('xpath', '(//*[@class="btn_secondary btn_inventory"])[1]')
    remove.click()
    time.sleep(2)

def test_remove3():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    remove = driver.find_element('xpath', '(//*[@class="btn_secondary cart_button"])[1]')
    remove.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def test_filter():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    filt = driver.find_element('xpath', '//select')
    filt.click()
    time.sleep(2)
    lowhigh = driver.find_element('xpath', '//option[@value="lohi"]')
    lowhigh.click()
    time.sleep(2)
    highlow = driver.find_element('xpath', '//option[@value="hilo"]')
    highlow.click()
    time.sleep(2)
    az = driver.find_element('xpath', '//option[@value="az"]')
    az.click()
    time.sleep(2)
    za = driver.find_element('xpath', '//option[@value="za"]')
    za.click()
    time.sleep(2)

def test_sidebar_allitems():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    sidebar = driver.find_element('xpath', '//*[@class="bm-burger-button"]')
    sidebar.click()
    time.sleep(2)
    allitems = driver.find_element('xpath', '//*[@id="inventory_sidebar_link"]')
    allitems.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html'

def test_sidebar_about():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    sidebar = driver.find_element('xpath', '//*[@class="bm-burger-button"]')
    sidebar.click()
    time.sleep(2)
    about = driver.find_element('xpath', '//*[@id="about_sidebar_link"]')
    about.click()
    time.sleep(2)
    assert driver.current_url == 'https://saucelabs.com/'

def test_sidebar_logout():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    sidebar = driver.find_element('xpath', '//*[@class="bm-burger-button"]')
    sidebar.click()
    time.sleep(2)
    about = driver.find_element('xpath', '//*[@id="logout_sidebar_link"]')
    about.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/index.html'

def test_sidebar_reset():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    sidebar = driver.find_element('xpath', '//*[@class="bm-burger-button"]')
    sidebar.click()
    time.sleep(2)
    reset = driver.find_element('xpath', '//*[@id="reset_sidebar_link"]')
    reset.click()
    time.sleep(2)

def test_checkout_empty():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Error: First Name is required', 'OK'

def test_checkout_ok():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    first_name = driver.find_element('xpath', '//*[@id="first-name"]')
    first_name.send_keys('Elena')
    time.sleep(2)
    last_name = driver.find_element('xpath', '//*[@id="last-name"]')
    last_name.send_keys('Sham')
    time.sleep(2)
    zipcode = driver.find_element('xpath', '//*[@id="postal-code"]')
    zipcode.send_keys('246023 Gomel BY')
    time.sleep(2)
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-two.html'
    finish = driver.find_element('xpath', '//*[@class="btn_action cart_button"]')
    finish.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-complete.html'

def test_checkout_not_ok():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    first_name = driver.find_element('xpath', '//*[@id="first-name"]')
    first_name.send_keys('A')
    time.sleep(2)
    last_name = driver.find_element('xpath', '//*[@id="last-name"]')
    last_name.send_keys('q')
    time.sleep(2)
    zipcode = driver.find_element('xpath', '//*[@id="postal-code"]')
    zipcode.send_keys('.')
    time.sleep(2)
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-two.html'
    finish = driver.find_element('xpath', '//*[@class="btn_action cart_button"]')
    finish.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-complete.html'

def test_checkout_ok_not_ok_and_empty1():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    first_name = driver.find_element('xpath', '//*[@id="first-name"]')
    first_name.send_keys('Alina')
    time.sleep(2)
    last_name = driver.find_element('xpath', '//*[@id="last-name"]')
    last_name.send_keys('D123')
    time.sleep(2)
    zipcode = driver.find_element('xpath', '//*[@id="postal-code"]')
    zipcode.send_keys('')
    time.sleep(2)
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Error: Postal Code is required', 'OK'

def test_checkout_ok_not_ok_and_empty2():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    first_name = driver.find_element('xpath', '//*[@id="first-name"]')
    first_name.send_keys('Al123')
    time.sleep(2)
    last_name = driver.find_element('xpath', '//*[@id="last-name"]')
    last_name.send_keys('')
    time.sleep(2)
    zipcode = driver.find_element('xpath', '//*[@id="postal-code"]')
    zipcode.send_keys('246023 Gomel BY')
    time.sleep(2)
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Error: Last Name is required', 'OK'

def test_checkout_ok_not_ok_and_empty3():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    first_name = driver.find_element('xpath', '//*[@id="first-name"]')
    first_name.send_keys('')
    time.sleep(2)
    last_name = driver.find_element('xpath', '//*[@id="last-name"]')
    last_name.send_keys('Dubrovskaya')
    time.sleep(2)
    zipcode = driver.find_element('xpath', '//*[@id="postal-code"]')
    zipcode.send_keys('op.123')
    time.sleep(2)
    cont = driver.find_element('xpath', '//*[@class="btn_primary cart_button"]')
    cont.click()
    time.sleep(2)
    error_message = driver.find_element('xpath', '//h3')
    assert error_message.text == 'Error: First Name is required', 'OK'

def test_checkout_cancel_and_cont_shopping():
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)
    add = driver.find_element('xpath', '(//*[@class="btn_primary btn_inventory"])[1]')
    add.click()
    time.sleep(2)
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    checkout = driver.find_element('xpath', '//*[@class="btn_action checkout_button"]')
    checkout.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html'
    cancel = driver.find_element('xpath', '//*[@class="cart_cancel_link btn_secondary"]')
    cancel.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    cont_shopping = driver.find_element('xpath', '//*[@class="btn_secondary"]')
    cont_shopping.click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html'