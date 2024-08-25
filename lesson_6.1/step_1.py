import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "email").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone").send_keys("+7985899998787")
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки полей
    zip_code_field = driver.find_element(By.ID, "zip")
    assert "invalid" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted red"

    fields = [
        "first-name", "last-name", "address", "email",
        "phone", "city", "country", "job-position", "company"
    ]

    for field in fields:
        element = driver.find_element(By.ID, field)
        assert "valid" in element.getAttribute("class"), f"Field {field} is not highlighted green"

    driver.quit()


if __name__ == "__main__":
    pytest.main()
