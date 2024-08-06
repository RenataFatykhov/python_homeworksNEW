from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск Chrome
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Нажатие на кнопку Close в модальном окне
close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p")
close_button.click()

driver.quit()
