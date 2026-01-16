import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_OTP, enter_password_if_displayed, click_nav_middle, enter_text
from utils.actions import generate_random_pin, enter_password_if_displayed, enter_OTP

def run_test(driver):
    try:

        currentPin=["6", "2", "7", "8"]
        newPin = generate_random_pin(exclude_pin=currentPin)

        click_nav_middle(driver)

        # Change language
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "User Settings")
        enter_password_if_displayed(
            driver,
            WebDriverWait(driver, 10),
            digits=["6", "2", "7", "8"]
        )

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Change PIN")


        # --- 1. Current PIN (Standard Class Name) ---
        print("Entering Current PIN...")
        enter_text(driver, AppiumBy.CLASS_NAME, "android.widget.EditText", currentPin)
        driver.press_keycode(66)

        # --- 2. New PIN (Short ScrollView XPath) ---
        # new_pin_xpath = "//*[contains(@text, 'New PIN') or contains(@content-desc, 'New PIN')]"  
        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)', newPin)
        print(f"Entering New PIN: {newPin}")
        # instance(1) is the second box
        driver.press_keycode(66)

        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)', newPin)
        print(f"Entering New PIN: {newPin}")
        # instance(1) is the second box
        driver.press_keycode(66)

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Next")
        print(f"New PIN is {newPin}")

        enter_OTP(driver)

        click_home_button(driver)

    finally:
        print("Change PIN test completed")
