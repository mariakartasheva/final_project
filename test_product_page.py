from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket_message()
    page.should_be_cost_of_the_basket_message()
    time.sleep(10)

