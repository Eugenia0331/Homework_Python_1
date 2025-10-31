from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def all_images_loaded(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    if not images:
        return False
    for img in images:
        # проверяем, что изображение загружено: complete и naturalWidth > 0
        if not driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0", img
        ):
            return False
    return True

# Опционально: вместо webdriver.Chrome() можно использовать ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()  # Убедитесь, что chromedriver доступен в PATH
try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Дождаться загрузки всех изображений
    WebDriverWait(driver, 60).until(all_images_loaded)

    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        src3 = images[2].get_attribute("src")
        print(src3)
    else:
        print("Найдено меньше 3 изображений.")
finally:
    driver.quit()
