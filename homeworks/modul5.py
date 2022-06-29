import unittest
from selenium import webdriver

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_create_screenshot(self):
        self.driver.find_element_by_id('checkbox-header').click()
        self.driver.find_element_by_xpath("//*[@id = 'checkboxes']/input[2]").click()
        self.driver.get_screenshot_as_file('screenshot.png')
