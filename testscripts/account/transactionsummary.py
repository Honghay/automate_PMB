from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        account_rows_locator = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '.')]")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(account_rows_locator)
        )

        # 3. Find ONLY the account rows
        account_list = driver.find_elements(*account_rows_locator)

        # 4. Click the FIRST one (Index 0)
        # Since we filtered out the junk, Index 0 is guaranteed to be the top account.
        if len(account_list) > 0:
            account_list[0].click()
        else:
            print("Error: No accounts found.")

        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@content-desc, 'Available Balance')]"))
        )

        click_home_button(driver)

    finally:
        print("View Transaction Summary test completed")

