from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск Firefox
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввод текста 1000
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")

# Очистка поля
input_field.clear()

# Ввод текста 999
input_field.send_keys("999")

driver.quit()