from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
import time


class BasketPage(BasePage):

    def should_be_basket_is_empty_message(self):
        no_item_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_MESSAGE).text
        no_item_message_text = "Your basket is empty"
        assert no_item_message_text in no_item_message, "There's no message about the basket being empty."

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)