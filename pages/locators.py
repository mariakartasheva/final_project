from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR,
                   '.basket-mini .btn-group > [href="/en-gb/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')

# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_IN_THE_MESSAGE = (
        By.CSS_SELECTOR, '#messages div:first-child div strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_IN_THE_MESSAGE = (By.CSS_SELECTOR, '.alert-info  strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
