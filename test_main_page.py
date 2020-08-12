from .pages.main_page import MainPage
import time

link = 'https://area.mtg-bi.com'


def test_change_username(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.change_username()
    page.should_be_success_message()


def test_change_phonenumber(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.change_phonenumber()
    page.should_be_success_message()

def test_change_valid_email(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.change_valid_email()
    page.should_be_success_message()

def test_change_invalid_email(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.change_invalid_email()
    page.should_be_invalid_message()

def test_set_country_ru(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.set_country_ru()
    page.should_be_success_message()

def test_set_finance_segment(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.set_finance_dropdown()
    page.should_be_success_message()

def test_change_invalid_phonenumber(browser):
    page = MainPage(browser, link)
    page.open()
    page.auth()
    page.change_invalid_phonenumber()
    page.should_be_invalid_phone_message()

