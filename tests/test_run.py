from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.OverviewPage import OverviewPage
from pages.CompletePage import CompletePage
from pages.YouInformationPage import YourInformationPage
import allure


def test_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('secret_sauce')
    auth_page.login_button_click()
    with allure.step(r'Проверить, что открыта страница '
                     r'https://www.saucedemo.com/inventory.html'):
        assert InventoryPage(driver).get_current_url() == \
               InventoryPage(driver).page_url, "Нужная страница не открыта"


def test_incorrect_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('123')
    auth_page.login_button_click()
    with allure.step(r'Проверить, что вместо ожидаемой страницы '
                     r'https://www.saucedemo.com/inventory.html открыта '
                     r'страница https://www.saucedemo.com'):
        assert InventoryPage(driver).get_current_url() != \
               InventoryPage(driver).page_url, "Url 2-х страниц совпали"


def test_item_buy(driver):
    LoginPage(driver).auth(
        login='standard_user',
        password='secret_sauce'
    )
    inventory_page = InventoryPage(driver)
    inventory_page.click_t_shirt_add_to_cart_button()
    with allure.step(r'Проверить, что рядом с иконкой '
                     r'корзины появилась цифра 1'):
        assert inventory_page.get_cart_counter() == 1, \
            'Рядом с иконкой корзины цифра не равная 1'
    inventory_page.click_cart_button()
    cart_page = CartPage(driver)
    with allure.step(r'Проверить, что количество контейнеров - 1'):
        assert cart_page.get_items_quantity() == 1, \
            'Количество контейнеров не равно 1'
    with allure.step(r'Проверить, что название товара '
                     r'- Sauce Labs Bolt T-Shirt'):
        assert cart_page.get_items_name() == 'Sauce Labs Bolt T-Shirt', \
            'Название товара не Sauce Labs Bolt T-Shirt'
    with allure.step(r'Проверить, что цена совпадает с '
                     r'указанной на странице со списком товаров'):
        assert cart_page.get_items_price() == \
               inventory_page.get_t_shirt_price(), 'Цены отличаются!'
    cart_page.click_checkout_button()
    you_information_page = YourInformationPage(driver)
    you_information_page.registration_order(
        first_name='Masha',
        last_name='Smirnova',
        postal_code='432001'
    )
    with allure.step(r'Проверить, что количество товаров - 1'):
        assert cart_page.get_items_number() == 1, \
            'Количество товаров не равно 1'
    with allure.step(r'Проверить, что название товара '
                     r'- Sauce Labs Bolt T-Shirt'):
        assert cart_page.get_items_name() == 'Sauce Labs Bolt T-Shirt', \
            'Название товара не Sauce Labs Bolt T-Shirt'
    with allure.step(r'Проверить, что цена совпадает с '
                     r'указанной на странице со списком товаров'):
        assert cart_page.get_items_price() == \
               inventory_page.get_t_shirt_price(), 'Цены отличаются!'
    overview_page = OverviewPage(driver)
    with allure.step(r'Проверить, что присутствует '
                     r'заголовок "Payment Information:" '):
        assert overview_page.get_payment_info_label() == \
               'Payment Information:', 'Заголовка "Payment Information:" нет!'
    with allure.step(r'Проверить, что присутствует '
                     r'значение "SauceCard #31337"'):
        assert overview_page.get_payment_info_value() == \
               'SauceCard #31337', 'Значения "SauceCard #31337" нет!'
    with allure.step(r'Проверить, что присутствует '
                     r'заголовок "Shipping Information:"'):
        assert overview_page.get_shipping_info_label() == \
               'Shipping Information:', \
               'Заголовка "Shipping Information:" нет!'
    with allure.step(r'Проверить, что присутствует значение'
                     r' "Free Pony Express Delivery!"'):
        assert overview_page.get_shipping_info_value() == \
               'Free Pony Express Delivery!', \
               'Значения "Free Pony Express Delivery!" нет!'
    with allure.step(r'Проверить, что присутствует '
                     r'заголовок "Price Total:"'):
        assert overview_page.get_total_info_label() == \
               'Price Total', 'Заголовка "Price Total:" нет!'
    with allure.step(r'Проверить, что присутствует '
                     r'поле "Item total:"'):
        assert overview_page.get_subtotal_label() == \
               'Item total:', 'Поля "Item total:" нет!'
    with allure.step(r'Проверить, что цена совпадает с указанной'
                     r' на странице со списком товаров'):
        assert overview_page.get_subtotal_value() == \
               inventory_page.get_t_shirt_price(), 'Цены отличаются!'
    with allure.step(r'Проверить, что присутствует поле "Tax:"'):
        assert overview_page.get_tax_label() == 'Tax:', 'Поля "Tax:" нет!'
    tax = 1.28
    with allure.step(r'Проверить, что поле "Tax:" '
                     r'имеет значение "1.28"'):
        assert overview_page.get_tax_value() == tax, \
            'Поле "Tax:" не равно "1.28"'
    with allure.step(r'Проверить, что присутствует '
                     r'поле "Total:"'):
        assert overview_page.get_total_label() == 'Total:', 'Поля "Total:" нет'
    with allure.step(r'Проверить, что поле "Total:" имеет значение, '
                     r'соответствующее сумме "Item total" и "Tax"'):
        assert overview_page.get_total_value() == \
               inventory_page.get_t_shirt_price() + tax, \
               'значение не соответствуюет сумме "Item total" и "Tax"'
    overview_page.click_finish_button()
    complete_page = CompletePage(driver)
    with allure.step(r'Проверить, что присутствует поле'
                     r' "Checkout: Complete!"'):
        assert complete_page.get_title() == 'Checkout: Complete!', \
            'Поля "Checkout: Complete!" нет'
    with allure.step(r'Проверить, что присутствует заголовок'
                     r' "Thank you for your order!"'):
        assert complete_page.get_complete_header() == \
               'Thank you for your order!', \
               'Заголовка "Thank you for your order!" нет'
    with allure.step(r'Проверить, что присутствует '
                     r'заголовок "Your order has been '
                     r'dispatched, and will arrive just '
                     r'as fast as the pony can get there!"'):
        assert complete_page.get_complete_text() == \
               ('Your order has been dispatched, and will arrive '
                'just as fast as the pony can get there!'), \
               ('Заголовка "Your order has been dispatched, and will '
                'arrive just as fast as the pony can get there!" нет')
    with allure.step(r'Проверить, что на странице '
                     r'присутствует кнопка "Back Home"'):
        assert complete_page.present_back_home_button() is True, \
            'Кнопки "Back Home" нет'
