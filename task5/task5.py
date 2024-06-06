from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('путь_к_вашему_драйверу')


driver.get('http://opencart/admin/')
driver.find_element(By.ID, 'input-username').send_keys('ваш_логин')
driver.find_element(By.ID, 'input-password').send_keys('ваш_пароль')
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


driver.find_element(By.CSS_SELECTOR, 'li#menu-catalog a').click()
driver.find_element(By.LINK_TEXT, 'Categories').click()
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
driver.find_element(By.ID, 'input-name1').send_keys('Devices')
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


def add_product(name, category, description):
    driver.find_element(By.LINK_TEXT, 'Products').click()
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    driver.find_element(By.ID, 'input-name1').send_keys(name)
    driver.find_element(By.LINK_TEXT, 'Data').click()
    driver.find_element(By.ID, 'input-model').send_keys('SKU-001')
    driver.find_element(By.LINK_TEXT, 'Links').click()
    driver.find_element(By.ID, 'input-category').send_keys(category)
    driver.find_element(By.CSS_SELECTOR, 'a[id^="category"]').click()
    driver.find_element(By.LINK_TEXT, 'Description').click()
    driver.find_element(By.CLASS_NAME, 'note-editable').send_keys(description)
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


add_product('Компьютерная мышь 1', 'Devices', 'Описание мыши 1')
add_product('Компьютерная мышь 2', 'Devices', 'Описание мыши 2')
add_product('Клавиатура 1', 'Devices', 'Описание клавиатуры 1')
add_product('Клавиатура 2', 'Devices', 'Описание клавиатуры 2')


driver.get('http://opencart/')
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('Компьютерная мышь 1')
search_field.send_keys(Keys.RETURN)
assert 'Компьютерная мышь 1' in driver.page_source


driver.get('http://opencart/admin/')
driver.find_element(By.LINK_TEXT, 'Products').click()
driver.find_element(By.CSS_SELECTOR, 'input[name^="selected"]').click() # Выбор первого товара в списке
driver.find_element(By.CSS_SELECTOR, '.btn-danger').click()
driver.switch_to.alert.accept()


driver.get('http://opencart/')
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('Компьютерная мышь 1')
search_field.send_keys(Keys.RETURN)
assert 'Компьютерная мышь 1' not in driver.page_source


driver.quit()
