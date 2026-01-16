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
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle, enter_text, swipe_element_right
import random


def run_test(driver):
    try:
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Favorites")
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        # Structure: Content Root -> (Skip middle layers) -> 2nd View Section -> 2nd Image
        plusButton_xpath = '//*[@resource-id="android:id/content"]//android.view.View[2]/android.widget.ImageView[2]'
        click_element(driver, AppiumBy.XPATH, plusButton_xpath)


        click_element(driver, AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')    
        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)', "Favorite Other Transfer test")
        enter_text(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)', "000 009 819")
        driver.press_keycode(66)

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Create")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Swipe to Confirm")) 
        )

        swipe_element_right(driver, driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe to Confirm"))
        enter_password_if_displayed(driver, WebDriverWait(driver, 10))

        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "Close")


        
    finally:
        print("Create favorite test completed")

