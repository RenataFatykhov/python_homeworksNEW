import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения 45 в поле delay
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие кнопок 7 + 8 =
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    # Ожидание результата
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Expected result to be 15, but got {result}"

    driver.quit()


if name == "__main__":
    pytest.main()
