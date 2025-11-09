from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Используется Chrome WebDriver
        self.driver.implicitly_wait(10)  # Установлено неявное ожидание

    def open_calculator_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def enter_delay(self, delay):
        try:
            delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
            delay_input.send_keys(delay)
        except Exception as e:
            print(f"Ошибка при вводе задержки: {e}")

    def perform_calculation(self):
        try:
            for btn_text in ["7", "+", "8", "="]:
                self.driver.find_element(By.XPATH, f"//span[text()='{btn_text}']").click()
        except Exception as e:
            print(f"Ошибка при выполнении вычислений: {e}")

    def verify_result(self, expected_result):
        try:
            # Явное ожидание результата
            WebDriverWait(self.driver, 46).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), str(expected_result))
            )
            result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
            assert result == str(expected_result), f"Ожидалось '{expected_result}', получено '{result}'"
        except Exception as e:
            print(f"Ошибка при проверке результата: {e}")

    def run_test(self):
        self.open_calculator_page()
        self.enter_delay(45)
        self.perform_calculation()
        self.verify_result(15)
        self.driver.quit()
