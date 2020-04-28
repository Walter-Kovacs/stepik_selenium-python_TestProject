from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn[name='registration_submit']")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>:nth-child(2)")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) strong")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p:nth-child(1)")
    MESSAGE_BASKET_COST_PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3) strong")
