from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class YourInformationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout_step_one.html'
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')

    @allure.step(r'Ввести имя, фамилию и почтовый индекс '
                 r'и нажать кнопку "Continue"')
    def registration_order(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ) -> None:
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_postal_code(postal_code)
        self.click_continue_button()

    @allure.step(r'Ввести имя')
    def input_first_name(self, first_name: str) -> None:
        self.fill_field(self.first_name, first_name)

    @allure.step(r'Ввести фамилию')
    def input_last_name(self, last_name: str) -> None:
        self.fill_field(self.last_name, last_name)

    @allure.step(r'Ввести почтовый индекс')
    def input_postal_code(self, postal_code: str) -> None:
        self.fill_field(self.postal_code, postal_code)

    @allure.step(r'Нажать кнопку Continue')
    def click_continue_button(self) -> None:
        self.click_element(self.continue_button)
