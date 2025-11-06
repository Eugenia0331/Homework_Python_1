# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        # Локатор поля задержки
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        # Локатор поля вывода результата
        self.result_display = (By.CSS_SELECTOR, '#result')

    # Вспомогательный локатор кнопки по тексту/lable
    def _button_by_label(self, label):
        return (By.XPATH, f"//button[normalize-space()='{label}']")

    # Открыто/установка задержки
    def set_delay(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.delay_input))
        delay_el = self.driver.find_element(*self.delay_input)
        delay_el.clear()
        delay_el.send_keys(str(value))

    # Нажатие кнопки калькулятора
    def click_button(self, label):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._button_by_label(label))
        )
        btn.click()

    # Ожидание ожидаемого текста в окне результата
    def wait_for_result(self, expected, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, str(expected))
        )

    # Получение текущего текста результата
    def get_result_text(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.result_display))
        return self.driver.find_element(*self.result_display).text
