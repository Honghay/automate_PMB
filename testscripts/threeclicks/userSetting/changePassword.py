from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle, enter_OTP, enter_text
from utils.actions import generate_random_pin, enter_password_if_displayed

def run_test(driver):
    try:

        currentPassword="Honghay2303!"
        newPin = generate_random_pin()

        click_nav_middle(driver)

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "User Settings")
        enter_password_if_displayed(
            driver,
            WebDriverWait(driver, 10),
            digits=["6", "2", "7", "8"]
        )

        

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Change Password")

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Forgot Password?")

        print("Entering Current Password...")
        enter_text(driver, AppiumBy.CLASS_NAME, "android.widget.EditText", currentPassword)
        driver.press_keycode(66)

        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)', "Honghay2303@")
        print(f"Entering New Password: Honghay2303@")
        # instance(1) is the second box
        driver.press_keycode(66)

        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)', "Honghay2303@")
        print(f"Re-Entering New Password: Honghay2303@")
        # instance(1) is the second box
        driver.press_keycode(66)

        enter_OTP(driver)


    finally:
        print("Change Password test completed")
