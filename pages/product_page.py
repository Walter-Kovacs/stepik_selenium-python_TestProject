from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "No 'Add to basket' button"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "No message add to basket"

    def message_add_to_basket_has_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET_PRODUCT_NAME).text
        assert product_name == product_name_in_msg,\
            f"Product name in message '{product_name_in_msg}' does not match product name '{product_name}'"

    def should_be_message_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_COST_PRICE), "No message basket cost"

    def message_basket_cost_has_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_COST_PRICE).text
        assert product_price == product_price_in_msg,\
            f"Product price in message '{product_price_in_msg}' does not match product price '{product_price}'"
