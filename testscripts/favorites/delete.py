from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle, enter_text, swipe_element_right
import random


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Favorites")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

    # Clicks the 2nd Image inside the 1st Row (The green/right icon)
        xpath = '//android.view.View[@content-desc="Favorite Other Trans 000 009 819"]'
        
    finally:
        print("Delete favorite test completed")

