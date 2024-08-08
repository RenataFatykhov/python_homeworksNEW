from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск Chrome
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Клик по синей кнопке
button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button.click()

driver.quit()
