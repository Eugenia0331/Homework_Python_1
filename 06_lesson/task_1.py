from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Настройка драйвера Chrome с автоматической загрузкой драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Шаг 1: перейти на страницу
        driver.get("http://uitestingplayground.com/ajax")

        # Шаг 2: нажать на синюю кнопку (Bootstrap btn-primary)
        blue_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        blue_btn.click()

        # Шаг 3: дождаться появления зелёной плашки с нужным текстом
        locator = (By.XPATH, "//*[contains(normalize-space(text()), 'Data loaded with AJAX get request.')]")
        el = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        # Шаг 4: вывести текст плашки
        print(el.text.strip())

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
