from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_image():
    driver = webdriver.Chrome()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # Ожидание загрузки третьего изображения
        image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        )
        src = image.get_attribute("src")
        print(src)
    finally:
        driver.quit()


if name == "__main__":
    wait_for_image()
    