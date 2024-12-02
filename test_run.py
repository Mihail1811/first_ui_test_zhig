from pages import LoginPage, InventoryPage, ItemPage, CartPage
import allure


def test_est_1_login(driver):
    auth_page = LoginPage(driver)
    auth_page.auth('standard_user', 'secret_sauce')
    inventory_page = InventoryPage(driver)
    inventory_page.choose_item()
    item_page = ItemPage(driver)
    item_page.add_to_cart_btn_click()
    item_page.back_to_products_click()
    inventory_page.add_jacket_to_cart_btn_click()
    inventory_page.cart_btn_click()
    cart_page = CartPage(driver)
    assert cart_page.number_of_products() == 2


def test_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('secret_sauce')
    auth_page.login_button_click()
    with allure.step(r'Проверить, что открыта страница '
                 r'"https://www.saucedemo.com/inventory.html"'):
        assert InventoryPage(driver).get_current_url() == InventoryPage(driver).page_url, "Нужная страница не открыта"


def test_incorrect_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('123')
    auth_page.login_button_click()
    with allure.step(r'Проверить, что переход на страницу '
                 r'https://www.saucedemo.com/inventory.html не произошел"'):
        assert InventoryPage(driver).get_current_url() != InventoryPage(driver).page_url, "Url 2-х страниц совпали"
