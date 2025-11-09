# test_saucedemo.py
import pytest
from selenium import webdriver
from saucedemo_page import LoginPage
from saucedemo_page import MainPage
from saucedemo_page import CartPage
from saucedemo_page import CheckoutPage

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