user_name = ('xpath', '//*[@id="user-name"]')
password = ('xpath', '//*[@id="password"]')
login = ('xpath', '//*[@id="login-button"]')
error_message = ('xpath', '//h3')

filter = ('xpath', '//select')
lowhigh = ('xpath', '//option[@value="lohi"]')
highlow = ('xpath', '//option[@value="hilo"]')
az = ('xpath', '//option[@value="az"]')
za = ('xpath', '//option[@value="za"]')

price1 = ('xpath', '(//*[@data-test="inventory-item-price"])[1]')
price6 = ('xpath', '(//*[@data-test="inventory-item-price"])[6]')

name1 = ('xpath', '(//*[@data-test="inventory-item-name"])[1]')
name6 = ('xpath', '(//*[@data-test="inventory-item-name"])[6]')

item_link = ('xpath', '(//*[@data-test="inventory-item-name"])[1]')

item_title = ('xpath', '//*[@data-test="inventory-item-name"]')
item_img = ('xpath', '//img[@class="inventory_details_img"]')
item_img_link = ('xpath', '(//*[@data-test="inventory-item-sauce-labs-backpack-img"])[1]')
item_desc = ('xpath', '//*[@data-test="inventory-item-desc"]')
item_price = ('xpath', '//*[@data-test="inventory-item-price"]')

add_item1 = ('xpath', '//*[@data-test="add-to-cart"]')
add_item2 = ('xpath', '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
add_item3 = ('xpath', '//*[@data-test="add-to-cart-sauce-labs-bike-light"]')
add_item4 = ('xpath', '//*[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
add_item5 = ('xpath', '//*[@data-test="add-to-cart-sauce-labs-fleece-jacket"]')
add_item6 = ('xpath', '//*[@data-test="add-to-cart-sauce-labs-onesie"]')
add_item7 = ('xpath', '//*[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

remove_item1 = ('xpath', '//*[@data-test="remove"]')
remove_item2 = ('xpath', '//*[@data-test="remove-sauce-labs-backpack"]')

cart_link = ('xpath', '//*[@data-test="shopping-cart-link"]')

sidebar_menu = ('xpath', '//*[@class="bm-burger-button"]')
sidebar_inv = ('xpath', '//*[@data-test="inventory-sidebar-link"]')
sidebar_about = ('xpath', '//*[@data-test="about-sidebar-link"]')
sidebar_logout = ('xpath', '//*[@data-test="logout-sidebar-link"]')
sidebar_reset = ('xpath', '//*[@data-test="reset-sidebar-link"]')

checkout_link = ('xpath', '//*[@data-test="checkout"]')
checkout_first_name = ('xpath', '//*[@id="first-name"]')
checkout_last_name = ('xpath', '//*[@id="last-name"]')
checkout_postal_code = ('xpath', '//*[@id="postal-code"]')

continue_link = ('xpath', '//*[@data-test="continue"]')
finish_link = ('xpath', '//*[@data-test="finish"]')
return_link = ('xpath', '//button[@id="back-to-products"]')

checkout_empty_error = ('xpath', '//*[@data-test="error"]')