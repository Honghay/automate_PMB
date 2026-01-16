import time
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from utils.actions import click_element, click_home_button, enter_password_if_displayed

"""Require to recheck and code is not stables"""




def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        account_rows_locator = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '|')]")
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

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Filter")

    
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(199, 2275)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(193, 2501)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        time.sleep(1)
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "To Date")
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(193, 2461)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(190, 2295)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Apply")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@content-desc, 'Filter')]"))
        )

        click_home_button(driver)

    finally:
        print("View account filter test completed")

