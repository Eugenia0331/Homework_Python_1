from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Настройки (можно убрать headless, если хотите видеть браузер)
options = Options()
# options.add_argument("--headless")  # раскомментируйте, если нужно без графического интерфейса

# Укажите путь к geckodriver, если он не в PATH
service = Service()

# Запуск браузера Firefox
driver = webdriver.Firefox(service=service, options=options)

try:
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввод имени пользователя
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Ввод пароля
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Нажатие кнопки Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Небольшая пауза, чтобы страница успела обновиться
    time.sleep(1)

    # Получение текста из зелёной плашки (успешный логин)
    message = driver.find_element(By.ID, "flash").text
    print("Сообщение:", message.strip())

finally:
    # Закрытие браузера
    driver.quit()
