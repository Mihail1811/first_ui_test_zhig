from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/inventory.html'
        self.cart = (By.ID, 'shopping_cart_container')
        self.t_shirt_price = (By.CSS_SELECTOR, '.inventory_item_price')
        self.t_shirt_add_to_cart_button = (
            By.ID,
            'add-to-cart-sauce-labs-bolt-t-shirt'
        )
        self.cart_counter = (By.CSS_SELECTOR, '.shopping_cart_badge')

    def check_inventory_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step(r'Найти товар(Sauce Labs Bolt T-Shirt) '
                 r'и нажать на кнопку "Add to cart"')
    def click_t_shirt_add_to_cart_button(self) -> None:
        self.click_element(self.t_shirt_add_to_cart_button)

    def get_t_shirt_price(self) -> float:
        return float(self.get_text(self.t_shirt_price)[1:])

    def get_cart_counter(self) -> int:
        return int(self.get_text(self.cart_counter))

    @allure.step(r'Нажать на иконку "Корзина"')
    def click_cart_button(self) -> None:
        self.click_element(self.cart)
