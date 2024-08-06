from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def rename_button():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/textinput")
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys("SkyPro")
        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        # Ожидание изменения текста кнопки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
        )
        print(button.text)
    finally:
        driver.quit()


if name == "__main__":
    rename_button()
    