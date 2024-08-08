from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Запуск Chrome с использованием webdriver-manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Клик по кнопке Add Element 5 раз
for _ in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

# Собираем список кнопок Delete
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"Количество кнопок Delete: {len(delete_buttons)}")

driver.quit()