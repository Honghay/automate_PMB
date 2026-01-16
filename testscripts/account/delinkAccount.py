from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed,enter_text, click_switch_next_to_text, click_first_account_menu


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        click_first_account_menu(driver)
        click_switch_next_to_text(driver, "Delink Account")
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Confirm")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        click_home_button(driver)



    finally:
        print("Delink Account test completed")

