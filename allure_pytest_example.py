import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


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
