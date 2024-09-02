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

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля "Zip Code" на наличие ошибки
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    error_message = driver.find_element(By.XPATH, "//div[@class='invalid-feedback' and @style='display: block;']")
    assert error_message.is_displayed(), "Error message for Zip Code is not displayed"

    # Поля для проверки на "valid"
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field in fields:
        success_message = driver.find_element(By.XPATH, f"//input[@name='{field}']/following-sibling::div[@class='valid-feedback' and @style='display: block;']")
        assert success_message.is_displayed(), f"Field {field} is not highlighted green"
