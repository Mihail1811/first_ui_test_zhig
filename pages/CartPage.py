from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/cart.html'
        self.cart_item = (By.CSS_SELECTOR, '.cart_item')
        self.item_quantity = (By.CSS_SELECTOR, '.cart_item > .cart_quantity')
        self.item_price = (
            By.XPATH,
            '//div[@class="cart_item"]//div[@class="inventory_item_price"]'
        )
        self.item_name = (
            By.XPATH,
            '//div[@class="cart_item"]//div[@class="inventory_item_name"]'
        )
        self.checkout_button = (By.ID, 'checkout')

    def get_items_number(self) -> int:
        return len(self.find_elements(*self.cart_item))

    def get_items_quantity(self) -> int:
        return int(self.find_element(*self.item_quantity).text)

    def get_items_price(self) -> float:
        return float(self.find_element(*self.item_price).text[1:])

    def get_items_name(self) -> str:
        return self.find_element(*self.item_name).text

    @allure.step(r'Нажать кнопку Checkout')
    def click_checkout_button(self) -> None:
        return self.find_element(*self.checkout_button).click()
