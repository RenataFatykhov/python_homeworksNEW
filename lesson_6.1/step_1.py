import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы, используя правильные локаторы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone").send_keys("+7985899998787")
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля "Zip Code" на наличие ошибки
    zip_code_field = driver.find_element(By.ID, "zip")
    assert "invalid" in zip_code_field.get_attribute("class"), (
        "Zip code field is not highlighted red"
    )

    # Поля для проверки на "valid"
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field in fields:
        element = driver.find_element(By.ID, field)
        assert "valid" in element.get_attribute("class"), (
            f"Field {field} is not highlighted green"
        )
          