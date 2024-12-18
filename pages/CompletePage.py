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
        return self.get_text(self.title)

    def get_complete_header(self) -> str:
        return self.get_text(self.complete_header)

    def get_complete_text(self) -> str:
        return self.get_text(self.complete_text)

    def present_back_home_button(self) -> bool:
        return self.check_existence_element(self.back_home_button)
