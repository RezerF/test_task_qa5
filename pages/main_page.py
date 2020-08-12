from selenium.webdriver.common.keys import Keys
from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.support.select import Select
import random

class MainPage(BasePage):

    def change_username(self):
        self.go_to_profile_form()
        self.input_new_name()
        self.input_dial_code()
        self.input_phone_number()
        self.update_form()

    def change_phonenumber(self):
        self.go_to_profile_form()
        self.input_dial_code()
        self.input_phone_number()
        self.update_form()

    def change_invalid_phonenumber(self):
        self.go_to_profile_form()
        self.input_dial_code()
        self.input_invalid_phone_number()
        self.update_form()

    def change_valid_email(self):
        self.go_to_profile_form()
        self.set_valid_email()
        self.input_dial_code()
        self.input_phone_number()
        self.update_form()

    def change_invalid_email(self):
        self.go_to_profile_form()
        self.set_invalid_email()
        self.input_dial_code()
        self.input_phone_number()
        self.update_form()

    def set_country_ru(self):
        self.go_to_profile_form()
        self.country_ru()
        self.input_phone_number()
        self.update_form()

    def set_finance_dropdown(self):
        self.go_to_profile_form()
        self.set_finance_segment()
        self.input_dial_code()
        self.input_phone_number()
        self.update_form()

    def go_to_profile_form(self):
        menu = self.browser.find_element(*MainPageLocators.DROPDOWN_MENU)
        menu.click()
        select = self.browser.find_element(*MainPageLocators.PROFILE_MENU)
        select.click()

    def input_new_name(self):
        rand = random.randint(1, 10)
        input_name = self.browser.find_element(*MainPageLocators.USER_NAME_INPUT)
        input_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_name.send_keys('Alex_323' + str(rand))

    def input_dial_code(self):
        code = self.browser.find_element(*MainPageLocators.DIAL_CODE_INPUT).send_keys('+7')

    def input_phone_number(self):
        rand = random.randint(10, 100)
        phone = self.browser.find_element(*MainPageLocators.PHONE_INPUT)
        phone.send_keys('49535243' + str(rand))

    def input_invalid_phone_number(self):
        rand = random.randint(10, 100)
        phone = self.browser.find_element(*MainPageLocators.PHONE_INPUT)
        phone.send_keys('33435243' + str(rand))

    def set_valid_email(self):
        rand = random.randint(1, 10)
        email_input = self.browser.find_element(*MainPageLocators.EMAIL_PROFILE_INPUT)
        email_input.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        email_input.send_keys('Alex_323' + str(rand) + '@gmail.com')

    def set_invalid_email(self):
        rand = random.randint(1, 10)
        email_input = self.browser.find_element(*MainPageLocators.EMAIL_PROFILE_INPUT)
        email_input.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        email_input.send_keys('Alex_323' + str(rand) + '.com')

    def country_ru(self):
        select = Select(self.browser.find_element(*MainPageLocators.COUNTRY_DROPDOWN))
        select.select_by_visible_text('Russia')

    def set_finance_segment(self):
        select = Select(self.browser.find_element(*MainPageLocators.BUSINESS_SEGMENT_DROPDOWN))
        select.select_by_visible_text('Finance')

    def update_form(self):
        self.browser.find_element(*MainPageLocators.UPDATE_BUTTON).click()

    def should_be_success_message(self):
        message = self.browser.find_element(*MainPageLocators.ALERT_SUCCESS)
        assert 'Success! Account data successfully updated.' in message.text,\
            'Success message not present'

    def should_be_invalid_message(self):
        message = self.browser.find_element(*MainPageLocators.INVALID_EMAIL_MESSAGE)
        assert 'Please enter correct email address.' in message.text, \
            'Warning message not preset but should be'

    def should_be_invalid_phone_message(self):
        message = self.browser.find_element(*MainPageLocators.INVALID_PHONE_MESSAGE)
        assert 'Enter a valid phone' in message.text, \
            "Warning message not preset but should be"
