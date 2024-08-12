import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SlowCalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay: int):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, value: str):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_result(self) -> str:
        time.sleep(45)  # ожидание 45 секунд
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
