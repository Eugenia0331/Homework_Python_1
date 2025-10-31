import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorTest(unittest.TestCase):
    def setUp(self):
        # Если нужно, можно заменить на: webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def tearDown(self):
        self.driver.quit()

    def test_add_with_delay(self):
        drv = self.driver
        drv.get(self.url)

        # Шаг 2: введите значение 45 в поле с локатором #delay
        delay_input = WebDriverWait(drv, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: нажмите кнопки: '7', '+', '8', '='
        def click_button(text):
            btn = WebDriverWait(drv, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{text}']"))
            )
            btn.click()

        click_button("7")
        click_button("+")
        click_button("8")
        click_button("=")

        # Шаг 4: проверить, что через 45 секунд в окне отображается 15
        # Попробуем несколько возможных локаторов окна результата
        locators = [
            (By.ID, "result"),
            (By.ID, "display"),
            (By.CSS_SELECTOR, "#result"),
            (By.CSS_SELECTOR, "#display"),
            (By.CLASS_NAME, "screen"),
            (By.CSS_SELECTOR, ".screen"),
            (By.CSS_SELECTOR, "output"),
        ]

        result_el = None
        for by, value in locators:
            try:
                el = WebDriverWait(drv, 5).until(EC.visibility_of_element_located((by, value)))
                result_el = el
                break
            except Exception:
                continue

        self.assertIsNotNone(result_el, "Не найден элемент отображения результата.")

        # Ожидаем, пока текст элемента станет "15"
        WebDriverWait(drv, 60).until(lambda d: result_el.text.strip() == "15")

        self.assertEqual(result_el.text.strip(), "15")

if __name__ == "__main__":
    unittest.main()
