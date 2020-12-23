import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()

@allure.feature('Functional testing')
@allure.story('Actions')

class TestCalcMoneyCurrency:
    @allure.step('Run browser, run app')
    
    def setup_method(self, method):
        driver.maximize_window()
        driver.get('http://www.../converter')
        assert 'Calc to currency' in driver.title
        driver.implicitly_wait(15)

    @allure.step('Back and closing a browser')
    
    def teardown_method(self, method):   
        driver.quit()

    @allure.step('Input valid data and checking a result')
    def test_input_amount(self):
            amount = ['1', '10']  # a list valid data
            input_amount_field = driver.find_element_by_xpath("...")  # input field
            input_amount_field.click() # click on result button   
            
            for option in amount: 
                input_amount_field.clear()  # clear a field
                input_amount_field.send_keys(option)  
                button_convert = driver.find_element_by_xpath("...").click()

                with allure.step('Correct result if use valid data'):
                    assert driver.find_element_by_xpath("..."), 'Error for result' 

                    time.sleep(1)
                    num1 = driver.find_element_by_xpath("...").text  # Result 1
                    val1 = driver.find_element_by_xpath("...").text  # Result 2 
                    
                    if ',' not in option:
                        option = option + ',00'

                    with allure.step(''):
                        assert option == num1, 'Result is not a correct'
            
