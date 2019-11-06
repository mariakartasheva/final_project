from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()
# Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    def should_be_added_to_basket_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        item_name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_IN_THE_MESSAGE).text
        assert item_name == item_name_in_alert, "The name of the product is wrong or not exist"
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    def should_be_cost_of_the_basket_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_IN_THE_MESSAGE).text
        assert price==price_in_alert
