from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service('C:\\Program Files\\Google\\chromedriver-win64\\chromedriver.exe')


driver = webdriver.Firefox(service=s)

driver.get('https://demo.opencart.com/')

product = driver.find_element(By.CSS_SELECTOR, '.product-thumb')
product.click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.thumbnails')))



driver.get('https://demo.opencart.com/')
currency = driver.find_element(By.CSS_SELECTOR, '.btn-link.dropdown-toggle')
currency.click()
driver.find_element(By.NAME, 'EUR').click()  # Смена на евро
currency.click()
driver.find_element(By.NAME, 'USD').click()  # Смена на доллары

driver.find_element(By.LINK_TEXT, 'Desktops').click()
driver.find_element(By.LINK_TEXT, 'PC').click()

assert 'No products' in driver.page_source


driver.find_element(By.LINK_TEXT, 'My Account').click()
driver.find_element(By.LINK_TEXT, 'Register').click()

driver.find_element(By.ID, 'input-firstname').send_keys('your_name')
driver.find_element(By.ID, 'input-lastname').send_keys('your_lastname')
driver.find_element(By.ID, 'input-email').send_keys('your_email')
driver.find_element(By.ID, 'input-telephone').send_keys('your_telephone')
driver.find_element(By.ID, 'input-password').send_keys('your_password')
driver.find_element(By.ID, 'input-confirm').send_keys('your_password')
driver.find_element(By.NAME, 'agree').click()
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


driver.get('https://demo.opencart.com/')
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('your_search_query')
search_field.send_keys(Keys.RETURN)

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_selector = '.product-thumb'
        self.currency_selector = '.btn-link.dropdown-toggle'
        self.search_input_selector = 'input[name=\'search\']'

    def select_product(self):
        self.driver.find_element(By.CSS_SELECTOR, self.product_selector).click()

    def change_currency(self, currency):
        self.driver.find_element(By.CSS_SELECTOR, self.currency_selector).click()
        self.driver.find_element(By.NAME, currency).click()

    def search(self, query):
        search_field = self.driver.find_element(By.CSS_SELECTOR, self.search_input_selector)
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)


main_page = MainPage(driver)
main_page.select_product()
main_page.change_currency('EUR')
main_page.search('iPhone')


def test_add_to_wishlist(driver):
    main_page = MainPage(driver)
    main_page.select_product()



def test_add_camera_to_cart(driver):
    main_page = MainPage(driver)
    main_page.search('camera')


def test_add_tablet_to_cart(driver):
    main_page = MainPage(driver)
    main_page.search('tablet')



def test_add_htc_phone_to_cart(driver):
    main_page = MainPage(driver)
    main_page.search('HTC')



def test_write_review(driver):
    main_page = MainPage(driver)
    main_page.select_product()



driver.quit()
