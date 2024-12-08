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
        return self.find_element(*self.payment_info_label).text

    def get_payment_info_value(self) -> str:
        return self.find_element(*self.payment_info_value).text

    def get_shipping_info_label(self) -> str:
        return self.find_element(*self.shipping_info_label).text

    def get_shipping_info_value(self) -> str:
        return self.find_element(*self.shipping_info_value).text

    def get_total_info_label(self) -> str:
        return self.find_element(*self.total_info_label).text

    def get_subtotal_label(self) -> str:
        return self.find_element(*self.subtotal_label).text[:11]

    def get_subtotal_value(self) -> float:
        return float(self.find_element(*self.subtotal_label).text[13:])

    def get_tax_label(self) -> str:
        return self.find_element(*self.tax_label).text[:4]

    def get_tax_value(self) -> float:
        return float(self.find_element(*self.tax_label).text[6:])

    def get_total_label(self) -> str:
        return self.find_element(*self.total_label).text[:6]

    def get_total_value(self) -> float:
        return float(self.find_element(*self.total_label).text[8:])

    @allure.step(r'Нажать кнопку Finish')
    def click_finish_button(self) -> None:
        return self.find_element(*self.finish_button).click()
