from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.login = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_btn = (By.NAME, 'login-button')

    @allure.step(r'Ввести логин и пароль и нажать кнопку "LOGIN"')
    def auth(self, login: str, password: str) -> None:
        self.input_login(login)
        self.input_password(password)
        self.login_button_click()

    @allure.step(r'Ввести логин')
    def input_login(self, login: str) -> None:
        self.fill_field(self.login, login)

    @allure.step(r'Ввести пароль"')
    def input_password(self, password: str) -> None:
        self.fill_field(self.password, password)

    @allure.step(r'Нажать кнопку "LOGIN"')
    def login_button_click(self) -> None:
        self.click_element(self.login_btn)
