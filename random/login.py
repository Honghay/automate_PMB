import os
import shutil
from datetime import datetime
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- User Information ----------
PHONE = "8888833333"
PASSWORD = "Honghay2303!"


# ---------- Screenshot setup ----------
SCREENSHOT_DIR = os.path.join(os.getcwd(), "Login screenshot")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def create_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "da05313",
        "appium:automationName": "UiAutomator2",
        "appium:app": r"C:\Users\heng.honghay\Desktop\Automate APK\app-uat-release (15).apk",
        "appium:noReset": True,
        "appium:newCommandTimeout": 3600,
        "appium:appWaitDuration": 30000,
        "appium:autoGrantPermissions": True
    })

    return webdriver.Remote("http://127.0.0.1:4723", options=options)


# ---------- Screenshot helpers ----------
def take_temp_screenshot(driver):
    temp_path = os.path.join(
        SCREENSHOT_DIR,
        f"temp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )
    driver.save_screenshot(temp_path)
    return temp_path


def finalize_screenshot(temp_path, name):
    final_path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    shutil.move(temp_path, final_path)
    print(f"Saved screenshot: {final_path}")


# ---------- Element helpers ----------
def click_element(driver, by, locator, timeout=15):
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )
    el.click()


def enter_text(driver, by, locator, text, timeout=15):
    el = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )
    try:
        el.clear()
    except:
        pass
    el.send_keys(text)


# ---------- Error popup detection ----------
def detect_error_popup(driver, timeout=5):
    error_keywords = [
        "incorrect", "blocked", "system", "abnormal", "failed",
        "invalid", "unauthorized", "error", "denied", "password"
    ]

    locators = [(AppiumBy.XPATH, "//android.widget.Toast")]

    for keyword in error_keywords:
        locators.extend([
            (AppiumBy.XPATH, f"//*[contains(@text, '{keyword}')]"),
            (AppiumBy.XPATH, f"//*[contains(@content-desc, '{keyword}')]"),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{keyword}")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{keyword}")')
        ])

    end_time = datetime.now().timestamp() + timeout
    while datetime.now().timestamp() < end_time:
        for by, locator in locators:
            try:
                return driver.find_element(by, locator)
            except:
                continue
    return None


# ---------- MAIN LOGIN FUNCTION ----------
def run_login(driver):
    """
    Runs login flow.
    Returns True if login succeeds, False if login fails.
    """
    driver = None

    try:
        driver = create_driver()
        wait = WebDriverWait(driver, 15)

        # Step 1: Language & Existing Customer
        temp = take_temp_screenshot(driver)
        finalize_screenshot(temp, "1. Language page")

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "English")
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Existing Customer")

        # Step 2: Phone number
        phone_locator = 'new UiSelector().className("android.widget.EditText").instance(0)'
        click_element(driver, AppiumBy.ANDROID_UIAUTOMATOR, phone_locator)
        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, phone_locator, PHONE)

        # Step 3: Password
        pass_locator = 'new UiSelector().className("android.widget.EditText").instance(1)'
        click_element(driver, AppiumBy.ANDROID_UIAUTOMATOR, pass_locator)
        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, pass_locator, PASSWORD)

        temp = take_temp_screenshot(driver)
        finalize_screenshot(temp, "2. User info")

        # Step 4: Confirm
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Confirm")
        temp = take_temp_screenshot(driver)

        popup = detect_error_popup(driver, timeout=2)
        if popup:
            try:
                print("Login error detected:", popup.text)
            except:
                print("Login error popup detected (text unreadable)")
            finalize_screenshot(temp, "3_error_detected")
            return False
        else:
            finalize_screenshot(temp, "3. OTP Screen")

        # Step 5: PIN entry (if exists)
        for digit in ["1", "2", "3", "4", "5", "6"]:
            try:
                click_element(driver, AppiumBy.ACCESSIBILITY_ID, digit, timeout=2)
            except:
                break

        print("Login successful")
        return True

    except Exception as e:
        print(f"Login failed: {e}")
        return False

