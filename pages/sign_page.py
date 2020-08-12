from .base_page import BasePage
from .locators import SignPageLocators, MainPageLocators


class SignPage(BasePage):

    def should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.PROFILE_ICON), "Login link is not present"

    def should_be_invalid_message(self):
        assert self.is_element_present(*SignPageLocators.LOGIN_OR_PASS_INCORRECT), \
            'Login or pass invalid message not present'

    def should_be_invalid_login(self):
        assert self.is_element_present(*SignPageLocators.LOGIN_INCORRECT), \
            'Login invalid message not present'
