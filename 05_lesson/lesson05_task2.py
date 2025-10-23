from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки браузера
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Путь к chromedriver (если не в PATH)
service = Service("chromedriver.exe")

# Запуск браузера
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Явное ожидание кнопки и клик
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"))
    )
    button.click()

    print("✅ Кнопка успешно нажата!")

    time.sleep(2)  # для наглядности

finally:
    driver.quit()
