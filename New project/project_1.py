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
    driver.find_element_by_id("").clear()
    driver.find_element_by_id("").send_keys("login_name")
    driver.find_element_by_id("").clear()
    driver.find_element_by_id("").send_keys("password")
    driver.find_element_by_id("").click()
    assert ...
