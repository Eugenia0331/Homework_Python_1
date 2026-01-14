from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_sauce_demo_checkout():
    # Запуск Firefox
    driver = webdriver.Firefox()
    
    try:
        # Открываем сайт
        driver.get("https://www.saucedemo.com/")
        
        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавляем товары в корзину
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()

        # Переходим в корзину
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

        # Нажимаем Checkout
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        # Заполняем форму
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        # Ждем загрузки страницы итоговой стоимости
        time.sleep(2)

        # Читаем итоговую стоимость
        total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        print(f"Total Price: {total_price}")

        # Проверяем, что итоговая стоимость равна $58.29
        assert total_price == "Total: $58.29", f"Expected $58.29, but got {total_price}"

    finally:
        # Закрываем браузер
        driver.quit()

