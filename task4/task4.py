from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
from allure_commons.types import AttachmentType


logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

s = Service('C:\\Program Files\\Google\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Firefox(service=s)

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_selector = '.product-thumb'
        self.currency_selector = '.btn-link.dropdown-toggle'
        self.search_input_selector = 'input[name=\'search\']'

    @allure.step('Выбор продукта')
    def select_product(self):
        logging.info('Выбор продукта')
        self.driver.find_element(By.CSS_SELECTOR, self.product_selector).click()

    @allure.step('Смена валюты на {currency}')
    def change_currency(self, currency):
        logging.info(f'Смена валюты на {currency}')
        self.driver.find_element(By.CSS_SELECTOR, self.currency_selector).click()
        self.driver.find_element(By.NAME, currency).click()

    @allure.step('Поиск {query}')
    def search(self, query):
        logging.info(f'Поиск {query}')
        search_field = self.driver.find_element(By.CSS_SELECTOR, self.search_input_selector)
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

@allure.feature('Тестирование функционала вишлиста')
def test_add_to_wishlist(driver):
    main_page = MainPage(driver)
    with allure.step('Добавление товара в вишлист'):
        main_page.select_product()


@allure.feature('Тестирование добавления товаров в корзину')
def test_add_camera_to_cart(driver):
    main_page = MainPage(driver)
    with allure.step('Добавление камеры в корзину'):
        main_page.search('camera')



driver.quit()
