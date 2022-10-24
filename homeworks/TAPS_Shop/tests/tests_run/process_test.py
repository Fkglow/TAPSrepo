import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page, order_page, order_success_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.logo_is_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_success_page.order_received_confirmation(self.driver))

    def test2_price_is_correct(self):
        self.assertTrue(main_page.logo_is_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_success_page.price_is_correct(self.driver))

    def test3_incorrect_form(self):
        self.assertTrue(main_page.logo_is_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.wrong_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.incorrect_form_submit(self.driver))

if __name__ == '__main__':
    unittest.main()