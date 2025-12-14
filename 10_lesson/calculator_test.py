# test_calculator.py
import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage

CALC_URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CALC_URL)
    yield driver
    driver.quit()


@allure.title("Проверка сложения с задержкой на медленном калькуляторе")
@allure.description("Тест вводит задержку, выполняет 7+8, ожидает результат 15 через 50 секунд")
@allure.feature("Slow Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_delay_addition(driver):
    page = CalculatorPage(driver)

    with allure.step("Установка задержки 50 секунд"):
        page.set_delay("50")

    with allure.step("Ввод выражения 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Ожидание результата 15"):
        page.wait_for_result("15", timeout=50)

    with allure.step("Проверка результата на экране"):
        assert page.get_result_text() == "15"


