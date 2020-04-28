from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert self.browser.current_url.find("login") != -1, "No 'login' substring in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on page"

    def register_new_user(self, email, password):
        email_input_element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input_element.send_keys(email)
        password_input_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input_element.send_keys(password)
        password_input_element_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_input_element_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
