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
from utils.actions import click_element, click_home_button, enter_password_if_displayed,enter_text, click_switch_next_to_text, click_first_account_menu


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        # --- REPLACED MESSY CODE WITH ONE LINE ---
        click_first_account_menu(driver)
        
        # Now the menu is open, just toggle the switch
        click_switch_next_to_text(driver, "Hide Account")

        click_home_button(driver)

    finally:
        print("Hide Account test completed")

