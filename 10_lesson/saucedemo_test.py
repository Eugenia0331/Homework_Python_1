import pytest
import allure
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


@allure.title("Полный тест оформления заказа на SauceDemo")
@allure.description("Авторизация, добавление товаров в корзину, оформление заказа и проверка итоговой суммы.")
@allure.feature("SauceDemo — оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_flow(driver):

    login_page = LoginPage(driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    main_page = MainPage(driver)

    with allure.step("Добавить товары в корзину"):
        main_page.add_to_cart("Sauce Labs Backpack")
        main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        main_page.add_to_cart("Sauce Labs Onesie")

    with allure.step("Перейти в корзину и нажать Checkout"):
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнить форму покупателя"):
        checkout_page.fill_checkout_info("Иван", "Петров", "101000")
        checkout_page.click_continue()

    with allure.step("Получить итоговую стоимость"):
        total_price = checkout_page.get_total_price()

    with allure.step("Проверить итоговую сумму"):
        assert total_price == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено '{total_price}'"
