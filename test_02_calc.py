from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def _wait_for_result_text(driver, text="15", timeout=60):
    # Попробуем несколько возможных локаторов элемента с результатом
    result_locators = [
        (By.ID, "result"),
        (By.ID, "display"),
        (By.CSS_SELECTOR, ".display"),
        (By.CSS_SELECTOR, ".result"),
        (By.CSS_SELECTOR, "#output"),
        (By.CSS_SELECTOR, ".screen"),
    ]
    for by, value in result_locators:
        try:
            WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element((by, value), text)
            )
            el = driver.find_element(by, value)
            return el
        except Exception:
            continue
    raise AssertionError("Не удалось обнаружить элемент с ожидаемым текстом результата")

def test_slow_calculator_chrome():
    driver = webdriver.Chrome()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Данные теста
        test_data = {
            "delay": "45"
        }

        # Установка задержки через поле #delay
        for field, value in test_data.items():
            input_el = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"#{field}"))
            )
            input_el.clear()
            input_el.send_keys(value)

        # Нажимаем кнопки: '7', '+', '8', '='
        for btn_text in ["7", "+", "8", "="]:
            driver.find_element(By.XPATH, f"//button[text()='{btn_text}']").click()

        # Ожидание и проверка результата "15" через до 60 секунд
        result_el = _wait_for_result_text(driver, text="15", timeout=60)
        assert result_el.text.strip() == "15", f"Ожидалось '15', получено '{result_el.text.strip()}'"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_slow_calculator_chrome()