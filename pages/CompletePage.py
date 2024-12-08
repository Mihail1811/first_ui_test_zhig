from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout_complete.html'
        self.title = (By.CSS_SELECTOR, '.title')
        self.complete_header = (By.CSS_SELECTOR, '.complete-header')
        self.complete_text = (By.CSS_SELECTOR, '.complete-text')
        self.back_home_button = (By.ID, 'back-to-products')

    def get_title(self) -> str:
        return self.find_element(*self.title).text

    def get_complete_header(self) -> str:
        return self.find_element(*self.complete_header).text

    def get_complete_text(self) -> str:
        return self.find_element(*self.complete_text).text

    def present_back_home_button(self) -> bool:
        return self.assert_that_present(*self.back_home_button)
