from venv import logger
from selenium import webdriver
import pytest

@pytest.fixture
def browser():
     logger.info("Starting Test")
    # Setup : Create a new instance of the Chrome driver
     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/elements")
     driver.maximize_window()
    

     yield driver

     driver.quit
           