from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'browserName': 'Chrome',
    'noReset': True,
    'fullReset': False
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get('https://the-internet.herokuapp.com/')

wait = WebDriverWait(driver, 10)


def test_ab_testing():
    driver.find_element(By.LINK_TEXT, 'A/B Testing').click()
    assert 'A/B Test' in driver.title
    driver.back()


def test_add_remove_elements():
    driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
    driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    driver.find_element(By.CLASS_NAME, 'added-manually').click()
    driver.back()


def test_checkboxes():
    driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
    driver.back()


def test_dropdown():
    driver.find_element(By.LINK_TEXT, 'Dropdown').click()
    dropdown = driver.find_element(By.ID, 'dropdown')
    dropdown.find_element(By.XPATH, '//option[text()="Option 2"]').click()
    driver.back()


def test_dynamic_controls():
    driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
    driver.find_element(By.XPATH, '//button[text()="Remove"]').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'message')))
    driver.find_element(By.XPATH, '//button[text()="Add"]').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'message')))
    driver.back()


def test_javascript_alerts():
    driver.find_element(By.LINK_TEXT, 'JavaScript Alerts').click()
    driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]').click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    driver.back()


def test_file_upload():
    driver.find_element(By.LINK_TEXT, 'File Upload').click()
    driver.find_element(By.ID, 'file-upload').send_keys('/documents/file.txt')
    driver.find_element(By.ID, 'file-submit').click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'uploaded-files'), 'file.txt'))
    driver.back()


def test_floating_menu():
    driver.find_element(By.LINK_TEXT, 'Floating Menu').click()
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    assert driver.find_element(By.ID, 'menu').is_displayed()
    driver.back()


def test_key_presses():
    driver.find_element(By.LINK_TEXT, 'Key Presses').click()
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)
    result = wait.until(EC.text_to_be_present_in_element((By.ID, 'result'), 'You entered: SPACE'))
    assert result
    driver.back()


def test_wysiwyg_editor():
    driver.find_element(By.LINK_TEXT, 'WYSIWYG Editor').click()
    driver.switch_to.frame('mce_0_ifr')
    editor_body = driver.find_element(By.ID, 'tinymce')
    editor_body.clear()
    editor_body.send_keys('Hello, World!')
    driver.switch_to.default_content()
    driver.back()


test_ab_testing()
test_add_remove_elements()
test_checkboxes()
test_dropdown()
test_dynamic_controls()
test_javascript_alerts()
test_file_upload()
test_floating_menu()
test_key_presses()
test_wysiwyg_editor()


driver.quit()
