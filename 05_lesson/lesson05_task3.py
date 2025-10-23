from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Открыть браузер FireFox
driver = webdriver.Firefox()

# 2. Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Небольшая пауза, чтобы страница успела загрузиться
time.sleep(2)

# 3. Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# 4. Ввести текст "Sky"
input_field.send_keys("Sky")

time.sleep(1)

# 5. Очистить поле
input_field.clear()

time.sleep(1)

# 6. Ввести текст "Pro"
input_field.send_keys("Pro")

time.sleep(2)

# 7. Закрыть браузер
driver.quit()
