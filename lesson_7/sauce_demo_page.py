from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SauceDemoPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, product_id: str):
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
