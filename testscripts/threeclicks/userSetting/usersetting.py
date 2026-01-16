from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle

def run_test(driver):
    try:

        click_nav_middle(driver)

        # User Settings
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "User Settings")
        enter_password_if_displayed(
            driver,
            WebDriverWait(driver, 10),
            digits=["6", "2", "7", "8"]
        )

        click_home_button(driver)

    finally:
        print("User Settings test completed")
