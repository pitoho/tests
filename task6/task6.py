from appium import webdriver
import unittest

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10.0',
            'deviceName': 'Android Emulator',
            'app': 'C:\\Program Files\\Documents\\apk.apk',
            'noReset': True,
            'fullReset': False
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_addition(self):
        self.driver.find_element_by_id('digit_2').click()
        self.driver.find_element_by_accessibility_id('plus').click()
        self.driver.find_element_by_id('digit_2').click()
        self.driver.find_element_by_accessibility_id('equals').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '4')



    def test_subtraction(self):
        self.driver.find_element_by_id('digit_5').click()
        self.driver.find_element_by_accessibility_id('minus').click()
        self.driver.find_element_by_id('digit_3').click()
        self.driver.find_element_by_accessibility_id('equals').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '2')

    def test_multiplication(self):
        self.driver.find_element_by_id('digit_9').click()
        self.driver.find_element_by_accessibility_id('multiply').click()
        self.driver.find_element_by_id('digit_9').click()
        self.driver.find_element_by_accessibility_id('equals').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '81')

    def test_division(self):
        self.driver.find_element_by_id('digit_8').click()
        self.driver.find_element_by_accessibility_id('divide').click()
        self.driver.find_element_by_id('digit_2').click()
        self.driver.find_element_by_accessibility_id('equals').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '4')


    def test_division_by_zero(self):
        self.driver.find_element_by_id('digit_7').click()
        self.driver.find_element_by_accessibility_id('divide').click()
        self.driver.find_element_by_id('digit_0').click()
        self.driver.find_element_by_accessibility_id('equals').click()
        result = self.driver.find_element_by_id('result').text
        self.assertIn('Error', result or 'Infinity')



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
