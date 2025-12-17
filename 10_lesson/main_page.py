from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Главная страница товаров.
    """

    def __init__(self, driver):
        """
        :param driver: WebDriver — драйвер браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину.

        :param product_name: str — название товара.
        :return: None
        """
        product_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{product_name}']//ancestor::div[@class='inventory_item']//button")
            )
        )
        product_button.click()

    def go_to_cart(self) -> None:
        """
        Переход в корзину.

        :return: None
        """
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        )
        cart_button.click()
