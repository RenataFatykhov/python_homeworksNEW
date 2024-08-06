from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск Chrome
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

# Ввод имени пользователя
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Ввод пароля
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Нажатие кнопки Login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

driver.quit()
