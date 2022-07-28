import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_iframe_screenshot(self):

        self.driver.find_element_by_id('iframe-header').click()

        iframe_content = self.driver.find_element_by_tag_name('iframe')

        wait = WebDriverWait(self.driver, 10)

        try:
            element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe')))
        except TimeoutException:
            print('Timeout Exception!')

        self.driver.switch_to.frame(iframe_content)

        target = self.driver.find_element_by_id('simpleButton1')
        target.location_once_scrolled_into_view
        target.click()

        self.driver.get_screenshot_as_file('iframe_button1_screenshot.png')

