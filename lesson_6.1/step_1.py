import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы, используя поиск по атрибуту name
    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "jobPosition").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля "Zip Code" на наличие ошибки
    zip_code_field = driver.find_element(By.NAME, "zip")
    assert "invalid" in zip_code_field.get_attribute("class"), (
        "Zip code field is not highlighted red"
    )

    # Поля для проверки на "valid"
    fields = [
        "firstName", "lastName", "address", "email",
        "phone", "city", "country", "jobPosition", "company"
    ]

    for field in fields:
        element = driver.find_element(By.NAME, field)
        assert "valid" in element.get_attribute("class"), (
            f"Field {field} is not highlighted green"
        )

    driver.quit()


if name == "__main__":
    pytest.main()
    