from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('C:\\Program Files\\Google\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://ya.ru')
driver.quit()
