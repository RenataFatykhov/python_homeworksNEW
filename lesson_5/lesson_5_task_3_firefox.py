from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск Firefox
driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/classattr")

# Клик по синей кнопке
button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button.click()

# Обработка алерта
driver.switch_to.alert.accept()

driver.quit()