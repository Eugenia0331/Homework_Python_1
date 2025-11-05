from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sauce_demo_checkout_total():
    # 1. Откройте сайт магазина в Firefox
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # 2. Авторизуйтесь как пользователь standard_user
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавьте в корзину товары:
    #    Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейдите в корзину
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # 5. Нажмите Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс
    test_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "postal-code": "12345"
    }
    for field, value in test_data.items():
        driver.find_element(By.ID, field).send_keys(value)

    # 7. Нажмите кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитайте со страницы итоговую стоимость (Total)
    total_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_value_label"))).text
    assert total_text == "$58.29", f"Ожидалось $58.29, получено {total_text}"

    # 9. Закройте браузер
    driver.quit()