from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>:nth-child(2)")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) strong")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p:nth-child(1)")
    MESSAGE_BASKET_COST_PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3) strong")
