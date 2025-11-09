from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SauceDemoTest:
    def __init__(self):
        self.driver = webdriver.Firefox()  # Используется Firefox WebDriver
        self.driver.implicitly_wait(10)  # Устанавливается неявное ожидание

    def open_site(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
        except Exception as e:
            print(f"Ошибка при открытии сайта: {e}")

    def login(self, username, password):
        try:
            self.driver.find_element(By.ID, "user-name").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")

    def add_items_to_cart(self):
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        try:
            for item in items:
                item_selector = f"//div[text()='{item}']//ancestor::div[@class='inventory_item']//button"
                self.driver.find_element(By.XPATH, item_selector).click()
        except Exception as e:
            print(f"Ошибка при добавлении товаров в корзину: {e}")

    def proceed_to_checkout(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
            self.driver.find_element(By.XPATH, "//button[text()='Checkout']").click()
        except Exception as e:
            print(f"Ошибка при переходе в корзину: {e}")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        try:
            self.driver.find_element(By.ID, "first-name").send_keys(first_name)
            self.driver.find_element(By.ID, "last-name").send_keys(last_name)
            self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
            self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        except Exception as e:
            print(f"Ошибка при заполнении формы: {e}")

    def verify_total(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            total_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
            assert total_text == "Total: $58.29", f"Ожидалось $58.29, получено {total_text}"
        except Exception as e:
            print(f"Ошибка при проверке итоговой суммы: {e}")

    def close_browser(self):
        self.driver.quit()

    def run_test(self):
        self.open_site()
        self.login("standard_user", "secret_sauce")
        self.add_items_to_cart()
        self.proceed_to_checkout()
        self.fill_checkout_form("Иван", "Петров", "12345")
        self.verify_total()
        self.close_browser()
