from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_button():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/ajax")
        button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        button.click()

        # Ожидание появления зеленой плашки
        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        )
        print(message.text)
    finally:
        driver.quit()


if name == "__main__":
    click_button()