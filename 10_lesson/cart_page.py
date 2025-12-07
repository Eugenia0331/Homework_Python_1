from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Страница корзины.
    """

    def __init__(self, driver):
        """
        :param driver: WebDriver — драйвер браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self) -> None:
        """
        Нажимает кнопку Checkout.

        :return: None
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()

    def get_cart_items(self) -> list[str]:
        """
        Возвращает список товаров в корзине.

        :return: list[str] — список текстов товаров.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [item.text for item in items]
