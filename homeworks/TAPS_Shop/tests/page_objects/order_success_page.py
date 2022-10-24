from tests.helpers.support_functions import *

order_confirmation_message = "//*[@id='post-8']/div/div/div/p"

order_confirmation = '//*[@id="post-8"]/header/h1'
order_product = "//*[@id='post-8']/div/div/div/section[2]/table/tbody/tr/td/a"
total_price = "//*[@id='post-8']/div/div/div/section[2]/table/tfoot/tr[5]/td/span"

def order_received_confirmation(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_confirmation_message)
    result = elem.text
    order_confirmation_text = 'Dziękujemy. Otrzymaliśmy Twoje zamówienie.'
    if result == order_confirmation_text:
        print(result)
        return True
    else:
        return False

def price_is_correct(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, total_price)
    price_amount = elem.text
    correct_amount = '€61,50'
    if price_amount == correct_amount:
        print(price_amount)
        return True
    else:
        return False


