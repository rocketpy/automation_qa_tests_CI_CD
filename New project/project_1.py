import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='C:\\...')  # Firefox
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()
    

@allure.description("Validating a login form")
@allure.severity(severity_level=CRITICAL)
def test_valid_login(test_setup):
    driver.get("https://")
