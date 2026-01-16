from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        account_rows_locator = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '|')]")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(account_rows_locator)
        )

        el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(4)")
        el1.click()
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Share Account Details")


    finally:
        print("Share details test completed")

