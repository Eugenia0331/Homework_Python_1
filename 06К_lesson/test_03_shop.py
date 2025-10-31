# test_saucedemo_checkout.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def test_sauce_demo_checkout_total():
    # Шаг 1: Открыть сайт в Firefox
    driver = webdriver.Firefox()  # убедитесь, что geckodriver в PATH
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизоваться как standard_user
        username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Шаг 3: Добавить в корзину нужные товары
        # Sauce Labs Backpack
        backpack_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack_btn.click()

        # Sauce Labs Bolt T-Shirt
        bolt_tshirt_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        bolt_tshirt_btn.click()

        # Sauce Labs Onesie
        onesie_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie_btn.click()

        # Шаг 4: Перейти в корзину
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link")))
        cart_link.click()

        # Шаг 5: Нажать Checkout
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()

        # Шаг 6: Заполнить форму именем, фамилией, индексом
        first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Ivan")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Petrov")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("12345")

        # Шаг 7: Нажать Continue
        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()

        # Шаг 8: Прочитать итоговую стоимость (Total)
        total_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_label.text  # например: "Total: $58.29"

        # Извлечь число из текста
        match = re.search(r"\$([0-9]+(?:\.[0-9]{2}))", total_text)
        assert match is not None, f"Не удалось распознать сумму из текста: '{total_text}'"
        total_amount = float(match.group(1))

        # Шаг 10: Проверка суммы
        assert abs(total_amount - 58.29) < 0.001, f"Ожидано 58.29, получено {total_amount}"

    finally:
        # Шаг 9: Закрыть браузер
        driver.quit()

if __name__ == "__main__":
    # Можно запустить напрямую как скрипт
    test_sauce_demo_checkout_total()
