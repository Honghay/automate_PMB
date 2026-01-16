import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle


def run_test(driver):
    
    try:

        #Terms & Conditions
        # FIRST CLICK — replace with touch action at (713, 3034)
        click_nav_middle(driver)
        
        click_element(driver,AppiumBy.ACCESSIBILITY_ID, "Terms & Conditions")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10), digits=["6","2","7","8"])

        click_home_button(driver)


    finally:
        print("Terms and Conditions test completed")

