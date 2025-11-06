# test_calculator.py
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

# Укажите реальный URL вашей страницы калькулятора
CALC_URL = "http://example.com/calculator"  # <- замените на реальный адрес

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CALC_URL)
    yield driver
    driver.quit()

def test_calculator_delay_addition(driver):
    page = CalculatorPage(driver)

    # Ввод задержки 45 секунд
    page.set_delay('45')

    # Нажимаем: 7, +, 8, =
    page.click_button('7')
    page.click_button('+')
    page.click_button('8')
    page.click_button('=')

    # Ожидаем и проверяем, что результат равен 15 через 45 секунд
    page.wait_for_result('15', timeout=45)
    assert page.get_result_text() == '15'
