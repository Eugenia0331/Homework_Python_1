def test_slow_calculator():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Firefox()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
    finally:
        driver.quit()
