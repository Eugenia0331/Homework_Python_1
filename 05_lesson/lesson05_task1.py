from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Запуск браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Переход на страницу
driver.get("http://uitestingplayground.com/classattr")

# Небольшая задержка для загрузки
time.sleep(2)

# Поиск синей кнопки (у неё несколько классов, включая btn-primary)
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Клик по кнопке
button.click()

# Ожидание для наблюдения результата (появляется alert)
time.sleep(2)

# Закрыть alert
driver.switch_to.alert.accept()

# Закрыть браузер
driver.quit()
