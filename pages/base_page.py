from selenium.common.exceptions import NoSuchElementException
from .locators import SignPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.email = 'testcaseqa5@gmail.com'
        self.password = '123456'

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

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