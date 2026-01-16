from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Accounts")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@content-desc, '.')]"))
        )


        click_home_button(driver)

    finally:
        print("View Account Summary test completed")

