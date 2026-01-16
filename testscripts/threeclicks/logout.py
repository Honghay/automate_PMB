import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle


def click_element(driver, by, locator, timeout=10):
    el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    el.click()
    time.sleep(0.5)

def run_test(driver):
    try:
        
        click_nav_middle(driver)
        # Logout
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Logout")
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Confirm")   

    finally:
        print("Logout test completed")
