from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
import time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'app': 'C:\\Users\\User\\Downloads\\YouTube_19.23.33_APKPure.apk',
    'noReset': True,
    'fullReset': False
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.implicitly_wait(10)


def test_tap():
    element = driver.find_element(By.ID, 'element_id')
    TouchAction(driver).tap(element).perform()


def test_long_press():
    element = driver.find_element(By.ID, 'element_id')
    TouchAction(driver).long_press(element, duration=2000).perform()

def test_swipe():
    start_element = driver.find_element(By.ID, 'start_element_id')
    end_element = driver.find_element(By.ID, 'end_element_id')
    TouchAction(driver).press(start_element).move_to(end_element).release().perform()


def test_multi_tap():
    element = driver.find_element(By.ID, 'element_id')
    actions = TouchAction(driver)
    actions.tap(element).perform()
    time.sleep(1)
    actions.tap(element).perform()


def test_pinch_zoom():
    element = driver.find_element(By.ID, 'element_id')
    actions = TouchAction(driver)
    actions.press(element).move_to(x=0, y=-100).release().perform()
    time.sleep(1)
    actions.press(element).move_to(x=0, y=100).release().perform()


test_tap()
test_long_press()
test_swipe()
test_multi_tap()
test_pinch_zoom()


driver.quit()
