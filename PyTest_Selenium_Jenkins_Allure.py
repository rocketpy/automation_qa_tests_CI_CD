import pytest
import allure
from selenium import seleniumwebdriver


@pytest.fixture()
def test_setup():
    driver = webdriver.Chrome(executable_path="C:\\...")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.quit()

    
@allure.description("Valid data") 
@allure.severity(severity_level="Critical")
def test_valid_login(test_setup):    
    driver.get("https://www...")
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys("admin")  # login field
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys("password")  # password field
    driver.find_element_by_id("id_name").click()  # button
    assert "page_name" in driver.current_url
    
    
def test_invalid_login(test_setup):    
    driver.get("https://www...")
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys("admin")  # login field
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys("password")  # password field
    driver.find_element_by_id("id_name").click()  # button
    assert "page_name" in driver.current_url    
    
    
def test_teardown():    
    driver.quit()


