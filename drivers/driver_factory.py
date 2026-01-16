from appium import webdriver
from appium.options.common.base import AppiumOptions

"""File where we store our driver code to always create driver instance easily in main.py, since we use appium locally we don't have to change the IP address
 or port often but if we do we just need to change it here once and also for deviceName, appium:app path"""


#For storing driver file to control devices
def create_driver():
    options = AppiumOptions()
    caps = {
        "platformName": "Android",
        "appium:deviceName": "da05313",
        "appium:automationName": "UiAutomator2",
        "appium:app": r"C:/Users/heng.honghay/Desktop/Automate APK/app-uat-release-46.apk",
        "appium:appPackage": "com.apdbank.mb.personal.uat",
        "appium:appActivity": "com.hsg.ebank.MainActivity",
        "appium:noReset": True,
        "appium:newCommandTimeout": 3600,
        "appium:autoGrantPermissions": True
    }

    options.load_capabilities(caps)
    return webdriver.Remote("http://127.0.0.1:4723", options=options)





