import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_field_by_label(driver, label_text: str, value: str):
    """
    Находит поле по тексту лейбла и заполняет его значением.
    Попытка использовать атрибут for у label, иначе поиск через вложенный input.
    """
    # ищем label по тексту
    label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//label[normalize-space(text())='{label_text}']"))
    )
    input_id = label.get_attribute("for")

    if input_id:
        field = driver.find_element(By.ID, input_id)
    else:
        # иногда input может быть внутри label
        field = label.find_element(By.TAG_NAME, "input")

    field.clear()
    field.send_keys(value)


def get_field_by_label(driver, label_text: str):
    """
    Возвращает field (input) по тексту label.
    """
    label = driver.find_element(By.XPATH, f"//label[normalize-space(text())='{label_text}']")
    input_id = label.get_attribute("for")
    if input_id:
        return driver.find_element(By.ID, input_id)
    else:
        return label.find_element(By.TAG_NAME, "input")


def color_is_red(border_color_value: str) -> bool:
    red_values = {"rgb(255, 0, 0)", "rgba(255, 0, 0, 1)"}
    return border_color_value in red_values


def color_is_green(border_color_value: str) -> bool:
    green_values = {"rgb(0, 128, 0)", "rgb(0, 255, 0)", "rgba(0, 128, 0, 1)"}
    return border_color_value in green_values


@pytest.mark.parametrize("browser", ["edge", "safari"])
def test_form_validation(browser):
    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        pytest.skip("Unsupported browser")

    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение полей
    fields = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55-3",
        "Email": "test@skypro.com",
        "Phone number": "+7985899998787",
        "Zip code": "",       # оставить пустым
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro",
    }

    for label_text, value in fields.items():
        fill_field_by_label(driver, label_text, value)

    # Нажать Submit
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' or contains(translate(text(),'SUBMIT','Submit'), 'Submit')]"))
    )
    submit_btn.click()

    # Проверка: Zip code подсвечено красным
    zip_field = get_field_by_label(driver, "Zip code")
    # Ждём изменения цвета после сабмита
    WebDriverWait(driver, 5).until(
        lambda d: zip_field.value_of_css_property("border-color") != ""
    )
    zip_border = zip_field.value_of_css_property("border-color")
    assert color_is_red(zip_border), f"Zip code должен подсвечиваться красным. Получено: {zip_border}"

    # Проверка: остальные поля подсвечены зелёным
    for label in fields:
        if label == "Zip code":
            continue
        f = get_field_by_label(driver, label)
        border_color = f.value_of_css_property("border-color")
        WebDriverWait(driver, 5).until(lambda d: border_color != "")
        assert color_is_green(border_color), f"{label} должен подсвечиваться зелёным. Цвет: {border_color}"

    driver.quit()
