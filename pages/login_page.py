from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        password = '6yE3s8YjuWNpwVp'
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"Login" is not in the url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Login form is not present"
