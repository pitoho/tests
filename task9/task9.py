from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'browserName': 'Chrome',
    'noReset': True,
    'fullReset': False
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.get('https://m.youtube.com')


wait = WebDriverWait(driver, 10)


def test_search_video():
    search_field = wait.until(EC.presence_of_element_located((By.NAME, 'search_query')))
    search_field.send_keys('Appium Automation')
    search_field.send_keys(Keys.ENTER)


def test_play_video():
    video = wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
    video.click()


def test_pause_play_video():
    video = wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
    video.click()
    # Пауза
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-play-button'))).click()
    # Воспроизведение
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-play-button'))).click()


def test_add_watch_later():
    video_options = wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
    video_options.click()
    add_to_watch_later = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'save-button')))
    add_to_watch_later.click()


def test_change_video_quality():
    video = wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
    video.click()
    settings_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-settings-button')))
    settings_button.click()
    quality = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ytp-quality-menu')))
    quality.click()
    p720 = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "720p")]')))
    p720.click()


test_search_video()
test_play_video()
test_pause_play_video()
test_add_watch_later()
test_change_video_quality()


driver.quit()
