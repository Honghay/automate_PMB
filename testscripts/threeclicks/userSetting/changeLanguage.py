from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import click_element, click_home_button, enter_password_if_displayed, click_nav_middle

def run_test(driver):

    def switch_language(current_word, radio_instance):
        # Generate XPath dynamically
        xpath = f'//android.view.View[contains(@content-desc, "{current_word}")]/android.widget.ImageView[2]'
        
        print(f"Switching from {current_word}...")
        click_element(driver, AppiumBy.XPATH, xpath)
        click_element(driver, AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.widget.RadioButton").instance({radio_instance})')

    try:

        click_nav_middle(driver)

        # Change language
        click_element(driver, AppiumBy.ACCESSIBILITY_ID, "User Settings")
        enter_password_if_displayed(
            driver,
            WebDriverWait(driver, 10),
            digits=["6", "2", "7", "8"]
        )

        switch_language("Language", 1)
        switch_language("ភាសា", 2)      
        switch_language("语言", 1)       


        click_home_button(driver)

    finally:
        print("Change Language test completed")
