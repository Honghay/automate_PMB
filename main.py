from drivers.driver_factory import create_driver
from testscripts.threeclicks import THREETAP_MENU
from testscripts.account import ACCOUNT
from testscripts.favorites import FAVORITES

#Import all the test scripts from every folders and run them, will modify in the future
def main():
    driver = create_driver()
    try:
        for test_func in THREETAP_MENU:
            print(f"Running {test_func.__name__}...")
            test_func(driver)
    finally:
        driver.quit()
        print("Driver closed")

if __name__ == "__main__":
    main()

#hello