import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_purchase():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item in items:
        driver.find_element(By.ID, item).click()

    # Переход в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()

    # Нажатие Checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # Нажатие кнопки Continue
    driver.find_element(By.ID, "continue").click()

    # Проверка итоговой суммы
    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total == "Total: $58.29", f"Expected total to be $58.29, but got {total}"

    driver.quit()


if __name__ == "__main__":
    pytest.main()
