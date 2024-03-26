from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")

user_name = driver.find_element('xpath', '//*[@id="user-name"]')
user_name.send_keys('standart_user')
password = driver.find_element('xpath', '//*[@id="password"]')
password.send_keys('secret_sauce')
