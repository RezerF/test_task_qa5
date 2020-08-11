from .base_page import BasePage
from .locators import SignPageLocators, MainPageLocators

class SignPage(BasePage):
    def auth(self):
        self.go_to_auth_form()
        self.input_email()
        self.input_pass()
        self.submit_button()

    def go_to_auth_form(self):
        self.browser.find_element(*SignPageLocators.SIGN_IN_BUTTON).click()

    def input_email(self):
        email_input = self.browser.find_element(*SignPageLocators.EMAIL_INPUT)
        email_input.send_keys(self.email)

    def input_pass(self):
        pass_input = self.browser.find_element(*SignPageLocators.PASS_INPUT)
        pass_input.send_keys(self.password)

    def submit_button(self):
        self.browser.find_element(*SignPageLocators.SUBMINT_BUTTON).click()

    def should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.PROFILE_ICON), "Login link is not present"

    def should_be_invalid_message(self):
        assert self.is_element_present(*SignPageLocators.LOGIN_OR_PASS_INCORRECT),\
            'Login or pass invalid message not present'

    def should_be_invalid_login(self):
        assert self.is_element_present(*SignPageLocators.LOGIN_INCORRECT),\
            'Login invalid message not present'



