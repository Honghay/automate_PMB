import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains

def click_element(driver, by, locator, timeout=10):
    el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    el.click()
    time.sleep(0.5)

def enter_password_if_displayed(driver, wait, digits=["6","2","7","8"]):
    """
    Clicks the PIN/password digits only if the keypad is visible on the screen.
    """
    try:
        # Try to find the first digit with a short timeout (2 seconds)
        el3 = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, digits[0]))
        )
        # If found, click all digits in order
        for digit in digits:
            el = wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, digit))
            )
            el.click()
        print("Password entered")
    except TimeoutException:
        # Keypad not visible, skip
        print("Password keypad not displayed, skipping")


def run_test(driver):
    try:
        # FIRST CLICK — replace with touch action at (713, 3034)
        time.sleep(3)
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(193, 3053)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1301, 1768)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        # Future Transfer
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Future Transfer")
        enter_password_if_displayed(
            driver,
            WebDriverWait(driver, 10),
            digits=["6", "2", "7", "8"]
        )
        click_element(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)')    
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Own Account Transfer")
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "From Account")

    finally:
        print("Future Transfer test completed")