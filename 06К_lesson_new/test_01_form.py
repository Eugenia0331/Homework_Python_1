from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Один словарь для всех данных
    test_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
        # zip-code не заполняем
    }

    # Заполняем все поля
    for field, value in test_data.items():
        driver.find_element(By.NAME, field).send_keys(value)

    # Нажимаем Submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    # Проверяем все поля
    for field in test_data:
        element = driver.find_element(By.ID, field)
        assert "success" in element.get_attribute("class"), f"Поле {field} должно быть зеленым"

    # Проверяем отдельно zip-code (должен быть красным)
    zip_element = driver.find_element(By.ID, "zip-code")
    assert "danger" in zip_element.get_attribute("class"), "Zip code должен быть красным"

    driver.quit()
