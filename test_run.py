from pages import LoginPage, InventoryPage, ItemPage, CartPage
import time


def test_est_1_login(driver):
    auth_page = LoginPage(driver)
    time.sleep(2)
    auth_page.auth('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    time.sleep(2)
    inventory_page.choose_item()

    item_page = ItemPage(driver)
    time.sleep(2)
    item_page.add_to_cart_btn_click()
    time.sleep(2)
    item_page.back_to_products_click()
    time.sleep(2)
    inventory_page.add_jacket_to_cart_btn_click()
    time.sleep(2)
    inventory_page.cart_btn_click()

    cart_page = CartPage(driver)
    time.sleep(2)
    assert cart_page.number_of_products() == 2
