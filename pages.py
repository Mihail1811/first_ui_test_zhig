from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(
            expected_conditions.visibility_of_element_located(
                (by, value)
            ), message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (by, value)
            ), message=f'Элементы {by, value} не найдены')

    def get_current_url(self) -> str:
        return self.driver.current_url



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.login = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_btn = (By.NAME, 'login-button')

    @allure.step(r'Ввести логин и пароль и нажать кнопку "LOGIN"')
    def auth(self, login: str, password: str) -> None:
        self.find_element(*self.login).send_keys(login)
        self.find_element(*self.password).send_keys(password)
        self.find_element(*self.login_btn).click()

    @allure.step(r'Ввести логин')
    def input_login(self, login: str) -> None:
        self.find_element(*self.login).send_keys(login)

    @allure.step(r'Ввести пароль"')
    def input_password(self, password: str) -> None:
        self.find_element(*self.password).send_keys(password)

    @allure.step(r'Нажать кнопку "LOGIN"')
    def login_button_click(self) -> None:
        self.find_element(*self.login_btn).click()


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/inventory.html'
        self.item = (By.ID, 'item_4_title_link')
        self.add_jacket_to_catr_btn = (
            By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
        self.cart_btn = (By.XPATH, "//*[@id='shopping_cart_container']")

    @allure.step(r'Кликнуть на нужный товар')
    def choose_item(self) -> None:
        self.find_element(*self.item).click()

    @allure.step(r'Найти другой товар(Fleece Jacket) '
                 r'и нажать на кнопку "Add to cart"')
    def add_jacket_to_cart_btn_click(self) -> None:
        self.find_element(*self.add_jacket_to_catr_btn).click()

    @allure.step(r'Нажать на иконку "Корзина"')
    def cart_btn_click(self) -> None:
        self.find_element(*self.cart_btn).click()


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.add_to_cart_btn = (By.XPATH, "//*[@id='add-to-cart']")
        self.back_to_products = (By.XPATH,
                                 "//*[@name='back-to-products']")

    @allure.step(r'Нажать на кнопку "Add to cart"')
    def add_to_cart_btn_click(self) -> None:
        self.find_element(*self.add_to_cart_btn).click()

    @allure.step(r'Нажать на кнопку "Back to products"')
    def back_to_products_click(self) -> None:
        self.find_element(*self.back_to_products).click()


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.item_list = (By.XPATH,
                          "//*[@class='inventory_item_price']")

    @allure.step(r'Проверить, что количество товаров в корзине равно двум')
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))
    