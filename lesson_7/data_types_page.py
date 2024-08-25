from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DataTypesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(
        self, first_name, last_name, address, email, phone, city, country, job_position, company
    ):
        self.driver.find_element(By.NAME, "firstname").send_keys(first_name)
        self.driver.find_element(By.NAME, "lastname").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job").send_keys(job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_field_class(self, field_id):
        return self.driver.find_element(By.ID, field_id).get_attribute("class")
    