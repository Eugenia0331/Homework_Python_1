# Класс PageObject:
# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

# pages/main_page.py
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name):
        product_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']//ancestor::div[@class='inventory_item']//button")))
        product_button.click()

    def go_to_cart(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        cart_button.click()

# pages/cart_page.py
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']")))
        checkout_button.click()

    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [item.text for item in items]

# pages/checkout_page.py
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(zip_code)

    def click_continue(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        continue_button.click()

    def get_total_price(self):
        total_price = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total_price.text
    
# Тест:
# test/test_saucedemo.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_flow(driver):
    # Шаг 1: Открыть сайт магазина и авторизоваться
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Шаг 2: Добавить товары в корзину
    main_page = MainPage(driver)
    main_page.add_to_cart("Sauce Labs Backpack")
    main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_to_cart("Sauce Labs Onesie")

    # Шаг 3: Перейти в корзину и нажать кнопку Checkout
    main_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Шаг 4: Заполнить форму своими данными
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Иван", "Петров", "101000")
    checkout_page.click_continue()

    # Шаг 5: Проверить итоговую стоимость
    total_price = checkout_page.get_total_price()
    
    # Шаг 6: Проверить итоговую сумму
    assert total_price == "Total: $58.29"