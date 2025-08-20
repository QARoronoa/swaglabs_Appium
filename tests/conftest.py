from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
import subprocess
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.Checkout_data import Checkout_info

@pytest.fixture(scope="function")
def setup():
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "emulator-5554"
    options.automationName = "UiAutomator2"
    options.noReset = True
    options.autoGrantPermissions = True
    options.newCommandTimeout = 60
    options.set_capability("chromedriverExecutable", r"C:\Users\Administrateur\Desktop\chromedriver.exe")
    options.appPackage = "com.android.chrome"
    options.appActivity = "com.google.android.apps.chrome.Main"

    subprocess.run([
        "adb", "-s", "emulator-5554", "shell", "am", "force-stop", "com.android.chrome"
    ])

    driver = Remote(command_executor="http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)

    subprocess.run([
        "adb", "-s", "emulator-5554", "shell", "am", "start",
        "-a", "android.intent.action.VIEW",
        "-d", "https://www.saucedemo.com/v1/index.html"
    ])
    time.sleep(5)

    WebDriverWait(driver, 30).until(lambda d: len(d.contexts) > 1)
    for ctx in driver.contexts:
        if "WEBVIEW" in ctx:
            driver.switch_to.context(ctx)
            time.sleep(2)
            break


    yield driver
    subprocess.run([
        "adb", "-s", "emulator-5554", "shell", "am", "force-stop", "com.android.chrome"
    ])

    driver.quit()

@pytest.fixture
def fill_checkout_info():
    return Checkout_info.checkoutinformation_form()
