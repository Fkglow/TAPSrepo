import unittest
from selenium import webdriver

import tests.page_objects.login_page
from config.test_settings import TestSettings
from tests.page_objects import main_page
from tests.page_objects import login_page
from tests.page_objects import my_account_page

# przetestuj opcje kilka razy zły TEN SAM email, inny blad?!!!!


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_logo_visible(self):
        self.assertTrue(main_page.logo_is_visible(self.driver))

    def test2_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(tests.page_objects.my_account_page.my_account_header_visible(self.driver))

    def test3_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login(self.driver))

if __name__ == '__main__':
    unittest.main()
