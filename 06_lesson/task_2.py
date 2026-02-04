from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Инициализация драйвера Chrome с автоматическим загрузчиком драйверов
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://uitestingplayground.com/textinput")

        # Найти текстовое поле и ввести "SkyPro"
        input_field = wait.until(EC.presence_of_element_located((By.ID, "newText")))
        input_field.clear()
        input_field.send_keys("SkyPro")

        # Найти синюю кнопку и нажать
        blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
        blue_button.click()

        # Дождаться изменения текста кнопки на "SkyPro"
        wait.until(lambda d: blue_button.text == "SkyPro")

        # Вывести текст кнопки в консоль
        print(blue_button.text)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
