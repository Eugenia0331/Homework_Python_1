from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс-страница авторизации на сайте SauceDemo.
    """

    def __init__(self, driver):
        """
        Конструктор класса.

        :param driver: WebDriver — драйвер браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открывает страницу авторизации сайта.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя.

        :param username: str — имя пользователя.
        :return: None
        """
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля.

        :param password: str — пароль пользователя.
        :return: None
        """
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажатие кнопки входа.

        :return: None
        """
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
