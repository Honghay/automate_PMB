from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed,enter_text, click_switch_next_to_text


def run_test(driver):
    try:
        # 1. Login and Navigate
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        # Locator for account rows (matches anything with a pipe '|')
        account_rows_locator = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '.')]")
        
        # Wait for list to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(account_rows_locator)
        )

        account_list = driver.find_elements(*account_rows_locator)

        if len(account_list) > 0:
            # --- STEP 1: EXTRACT DATA ---
            # Get the full text, e.g., "000 000 001 | Savings Account"
            full_text = account_list[1].get_attribute("content-desc")
            
            # Split by '|' and take the first part to get just the number
            # "000 000 001 | Savings" -> ["000 000 001 ", " Savings"] -> "000 000 001"
            target_account_num = full_text.split('|')[0].strip()

            print(f"Total Accounts Found: {len(account_list)}")
            
            print(f"Target Account Extracted: {target_account_num}")



        click_home_button(driver)

    finally:
        print("Main Account test completed")

