# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Page Object Model (POM) класс для страницы медленного калькулятора.
    Содержит методы для взаимодействия с элементами интерфейса.
    """

    def __init__(self, driver):
        """
        Инициализатор страницы.

        :param driver: WebDriver — экземпляр Selenium WebDriver.
        :return: None
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.result_display = (By.CSS_SELECTOR, '.screen')
        
    def _button_by_label(self, label):
        """
        Вспомогательный метод для получения локатора кнопки по её видимому тексту.

        :param label: str — текст кнопки (например: '7', '+', '=', '8').
        :return: tuple — локатор формата (By.XPATH, xpath-string)
        """
        return (By.XPATH, f"//span[text()='{label}']")

    def set_delay(self, value):
        """
        Устанавливает задержку выполнения операций калькулятора.

        :param value: str or int — значение задержки в секундах.
        :return: None
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.delay_input))
        delay_el = self.driver.find_element(*self.delay_input)
        delay_el.clear()
        delay_el.send_keys(str(value))

    def click_button(self, label):
        """
        Нажимает кнопку калькулятора.

        :param label: str — текст кнопки.
        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._button_by_label(label))
        )
        btn.click()

    def wait_for_result(self, expected, timeout=45):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected: str or int — ожидаемый текст результата.
        :param timeout: int — максимальное время ожидания (секунды).
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, str(expected))
        )

    def get_result_text(self):
        
        """
        Получает текущий текст результата с экрана калькулятора. 
           :return: str — текст текущего результата.
        """

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.result_display))
        return self.driver.find_element(*self.result_display).text


