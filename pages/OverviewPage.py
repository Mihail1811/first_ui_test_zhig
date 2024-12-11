from pages.CartPage import CartPage
from selenium.webdriver.common.by import By
import allure


class OverviewPage(CartPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://www.saucedemo.com/checkout_stop_two.html'
        self.payment_info_label = (
            By.CSS_SELECTOR, '[data-test="payment-info-label"]'
        )
        self.payment_info_value = (
            By.CSS_SELECTOR, '[data-test="payment-info-value"]'
        )
        self.shipping_info_label = (
            By.CSS_SELECTOR, '[data-test="shipping-info-label"]'
        )
        self.shipping_info_value = (
            By.CSS_SELECTOR, '[data-test="shipping-info-value"]'
        )
        self.total_info_label = (
            By.CSS_SELECTOR, '[data-test="total-info-label"]'
        )
        self.subtotal_label = (
            By.CSS_SELECTOR, '[data-test="subtotal-label"]'
        )
        self.tax_label = (
            By.CSS_SELECTOR, '[data-test="tax-label"]'
        )
        self.total_label = (
            By.CSS_SELECTOR, '[data-test="total-label"]'
        )
        self.finish_button = (By.ID, 'finish')

    def get_payment_info_label(self) -> str:
        return self.get_text(self.payment_info_label)

    def get_payment_info_value(self) -> str:
        return self.get_text(self.payment_info_value)

    def get_shipping_info_label(self) -> str:
        return self.get_text(self.shipping_info_label)

    def get_shipping_info_value(self) -> str:
        return self.get_text(self.shipping_info_value)

    def get_total_info_label(self) -> str:
        return self.get_text(self.total_info_label)

    def get_subtotal_label(self) -> str:
        return self.get_text(self.subtotal_label)[:11]

    def get_subtotal_value(self) -> float:
        return float(self.get_text(self.subtotal_label)[13:])

    def get_tax_label(self) -> str:
        return self.get_text(self.tax_label)[:4]

    def get_tax_value(self) -> float:
        return float(self.get_text(self.tax_label)[6:])

    def get_total_label(self) -> str:
        return self.get_text(self.total_label)[:6]

    def get_total_value(self) -> float:
        return float(self.get_text(self.total_label)[8:])

    @allure.step(r'Нажать кнопку Finish')
    def click_finish_button(self) -> None:
        return self.click_element(self.finish_button)
