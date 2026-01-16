import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

"""Utility action file that store all the function that we will use multiple times in different test scripts"""


#Click element: Wait for 10 seconds until element is clickable, then click it
def click_element(driver,by, locator, timeout=10):
    el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    el.click()


#Find element like textbox and input fields, then send keys to it
def enter_text(driver, by, locator, text, timeout=10):
    try:
        # 1. Wait and Find
        el = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        
        # 2. Click to focus (Crucial for PIN fields)
        el.click()
        
        # 3. Try to Clear (Ignore errors if it's not clearable)
        try:
            el.clear()
        except:
            pass

        # 4. Try Standard Typing
        el.send_keys(text)
    except Exception as e:
        print(f"Standard input failed, trying ADB Keyboard... ({e})")
        #if fail switch to use ADB keyboard
        try:
            driver.execute_script("mobile: type", {"text": text})
            print(f"Entered text via ADB: {text}")
        except Exception as adb_error:
            print(f"Critical Error: Could not enter text. {adb_error}")
            raise adb_error


#Check if there is a password keypad displayed, if yes, enter the password, if not then skip
def enter_password_if_displayed(driver, wait, digits=["6","2","7","8"]):
    try:
        # Try to find the first digit with a short timeout (1 seconds)
        el3 = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, digits[0]))
        )
        # If found, click all digits in order
        for digit in digits:
            el = wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, digit))
            )
            el.click()
        print("Password entered")
    except TimeoutException:
        # Keypad not visible, skip
        print("Password keypad not displayed, skipping")


#Check and wait till Home button is clickable, then click it
def click_home_button(driver):
    try:
        # Custom wait logic: Wait until at least 2 images exist
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")) >= 2
        )
        
        images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        if len(images) >= 2:
            images[-2].click()
            print("Clicked Home Button")
        else:
            print("Error: Could not find Home button images")
            
    except TimeoutException:
        print("Error: Timed out waiting for Home button")


#Check and wait until there is more or equal to 2 images, then click the middle navigation button
def click_nav_middle(driver):
    try:
        # Wait for the navigation bar to likely be loaded (Wait for at least 2 images)
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")) >= 2
        )
        
        # Find all images
        images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        
        if len(images) > 0:
            # Click the VERY LAST image (Index -1)
            print("Found images, clicking the last one (Middle Nav).")
            images[-3].click()
        else:
            print("Error: No images found for navigation.")
            
    except Exception as e:
        print(f"Error clicking middle nav button: {e}")


#Generate random 4 digit code and check to not have same as current pin
def generate_random_pin(exclude_pin=None):

    while True:
        new_pin = [str(random.randint(0, 9)) for _ in range(4)]
        
        if exclude_pin and new_pin == exclude_pin:
            continue # Try again
            
        return new_pin
    

#For entering default OTP 1,2,3,4,5,6
def enter_OTP(driver, digits=None):

    if digits is None:
        digits = ["1", "2", "3", "4", "5", "6"]

    print(f"Entering PIN sequence: {digits}")

    for digit in digits:
        try:
            #uses click element so it still try to find the digit withtin 2 seconds
            click_element(driver, AppiumBy.ACCESSIBILITY_ID, digit, timeout=2)
        except Exception:
            print(f"Stopped at digit '{digit}' (Element not found or screen changed).")
            break


#To find the element, get the bound of it and move from left to right within the element
def swipe_element_right(driver, element, duration_ms=300):
    # 1. Get Element Coordinates
    location = element.location
    size = element.size
    
    # 2. Calculate Start (Left) and End (Right) Points
    # Y is always the middle of the element
    center_y = int(location['y'] + (size['height'] / 2))
    
    # Start at 15% width (Left side)
    start_x = int(location['x'] + (size['width'] * 0.15))
    
    # End at 90% width (Right side)
    end_x = int(location['x'] + (size['width'] * 0.90))
    
    print(f"Swiping from {start_x} to {end_x} at Y={center_y}")

    # 3. Perform Swipe Action (W3C Standard)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    
    # Move to Start
    actions.w3c_actions.pointer_action.move_to_location(start_x, center_y)
    actions.w3c_actions.pointer_action.pointer_down()
    
    # Drag to End (Simulating the swipe duration)
    actions.w3c_actions.pointer_action.pause(duration_ms / 300) # Pause to simulate hold/drag
    actions.w3c_actions.pointer_action.move_to_location(end_x, center_y)
    
    # Release
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()


#To locate the switch that is next to the "element_text" and click it, for example, button in the same row as "Hide Account"
def click_switch_next_to_text(driver, element_text):
    try:
        # 1. Find the Text Element (Anchor)
        # We look for any element that contains the text/content-desc
        xpath = f"//*[contains(@text, '{element_text}') or contains(@content-desc, '{element_text}')]"
        element = driver.find_element(AppiumBy.XPATH, xpath)
        
        # 2. Calculate Coordinates
        # Y: The exact vertical center of the text element
        element_y = element.location['y'] + (element.size['height'] / 2)
        
        # X: 90% of the screen width (to ensure we hit the switch on the right)
        window_size = driver.get_window_size()
        target_x = window_size['width'] * 0.90
        
        print(f"Clicking switch for '{element_text}' at [{target_x}, {element_y}]")

        # 3. Perform Tap
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(target_x, int(element_y))
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()
        
    except Exception as e:
        print(f"Error clicking switch for '{element_text}': {e}")


#Identify the first account row by checking for "USD" or "KHR" in content-desc and ignoring "Summary" in title, and click on the 3 dots icon in the first account row
def click_first_account_menu(driver, timeout=10):
    """
    Finds the first valid account row (ignoring 'Summary' header) 
    and clicks the 3-dot menu icon (the last image in that row).
    """
    print("Attempting to find first account and open menu...")
    
    # 1. Complex Locator: Find rows with Currency but NOT 'Summary'
    account_rows_locator = (AppiumBy.XPATH, "//android.view.View[(contains(@content-desc, 'USD') or contains(@content-desc, 'KHR')) and not(contains(@content-desc, 'Summary'))]")

    try:
        # Wait for rows to appear
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(account_rows_locator)
        )
        
        # Find all matching rows
        account_list = driver.find_elements(*account_rows_locator)

        if len(account_list) > 0:
            first_row = account_list[0]
            print(f"Found Account Row: {first_row.get_attribute('content-desc').split('|')[0]}") # Log just the ID part if possible

            # 2. Find ALL images inside this specific row
            images = first_row.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            
            if len(images) >= 2:
                # Click the LAST image (Standard UI: Profile is first, Menu is last)
                print("Clicking the 3-dot menu icon...")
                images[-1].click()
                return True
            else:
                print("Error: Row found, but it didn't have enough images (Profile + Menu).")
                return False
        else:
            print("Error: No account rows found.")
            return False

    except Exception as e:
        print(f"Failed to click first account menu: {e}")
        return False