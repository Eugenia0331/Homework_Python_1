from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Страница оформления заказа.
    """

    def __init__(self, driver):
        """
        :param driver: WebDriver — драйвер браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет форму покупателя.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param zip_code: str — ZIP код.
        :return: None
        """
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(zip_code)

    def click_continue(self) -> None:
        """
        Нажимает Continue.

        :return: None
        """
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        continue_button.click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: str — текст с итоговой суммой (например 'Total: $58.29').
        """
        total_price = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_price.text
