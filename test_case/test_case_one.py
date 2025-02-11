import logging
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from  function_public import object
from time import sleep
import pytest
obj = object

longger = logging.getLogger(__name__)


@pytest.mark.selenium
def test(browser):
        ob = object.input_element
        # Get page title
        # title = driver.title
        sleep(3)
        textbox = browser.find_element(By.ID, "item-0")
        textbox.click()
        sleep(5)

        username = browser.find_element(By.ID, "userName")
        logging.info(f"set text:[{ob.usernameInput}] to element:[{username}]")    
        username.send_keys(ob.usernameInput)
        sleep(3)
        useremail = browser.find_element(By.ID, "userEmail")
        logging.info(f"set text:[{ob.userEmailInput}] to element:[{useremail}]")
        useremail.send_keys(ob.userEmailInput)
        sleep(3)
        address = browser.find_element(By.ID , "currentAddress")
        logging.info(f"set text:[{ob.currentAddressInput}] to element:[{address}]")
        address.send_keys(ob.currentAddressInput)
        sleep(3)
        addreselse = browser.find_element(By.ID, "permanentAddress")
        logging.info(f"set text:[{ob.permanentAddressInput}] to element:[{addreselse}]")
        addreselse.send_keys(ob.permanentAddressInput)
        sleep(3)
        submit = browser.find_element(By.ID, "submit")
        submit.click() 

        sleep(3)
        checkbox = browser.find_element(By.ID, "item-1")
        checkbox.click()

        sleep(3)
        plus = browser.find_element(By.CSS_SELECTOR, "button.rct-option:nth-child(1)")
        plus.click()

        sleep(3)
        allhome = browser.find_element(By.CSS_SELECTOR, "#tree-node > ol:nth-child(2) > li:nth-child(1) > span:nth-child(1) > label:nth-child(2) > span:nth-child(2)")
        allhome.click()

        sleep(3)
        minus = browser.find_element(By.CSS_SELECTOR, "button.rct-option:nth-child(2)")
        minus.click()

        sleep(3)

        logging.info("This is an info message")

if __name__ == "__main__":
    pytest.main()