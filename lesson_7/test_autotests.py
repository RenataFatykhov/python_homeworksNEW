chrome import ChromeDriverManager

from data_types_page import DataTypesPage
from slow_calculator_page import SlowCalculatorPage
from sauce_demo_page import SauceDemoPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form_submission(driver):
    page = DataTypesPage(driver)
    page.open()
    page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )
    page.submit()

    assert "invalid" in page.get_field_class("zip"), "Zip code field is not highlighted red"
    fields = [
        "first-name", "last-name", "address", "email",
        "phone", "city", "country", "job-position", "company"
    ]
    for field in fields:
        assert "valid" in page.get_field_class(field), f"Field {field} is not highlighted green"


def test_calculator(driver):
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(45)

    for button in ["7", "+", "8", "="]:
        page.click_button(button)

    assert page.get_result() == "15", "Expected result to be 15"


def test_purchase(driver):
    page = SauceDemoPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    for item in [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]:
        page.add_to_cart(item)

    page.go_to_cart()
    page.checkout()
    page.fill_checkout_info("Иван", "Петров", "123456")
    page.continue_checkout()

    assert page.get_total() == "Total: $58.29", "Expected total to be $58.29"
