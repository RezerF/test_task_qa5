from .pages.sign_page import SignPage
import pytest, time

email_pass = [('testcaseqa5@gmail.com', '123456'),
              ('testcaseqa5@gmail.com', '4321'),
              ('testcaseqa5@', '123456'),
              ('testcasewtrg@gmail.com', '123456'),
              ('gsdfgsdfs@gmail.com', '432gdfgfd1')]
link = 'https://area.mtg-bi.com'

@pytest.mark.skip
def test_full_valid_auth(browser):
    page = SignPage(browser, link)
    page.open()
    page.email = email_pass[0][0]
    page.password = email_pass[0][1]
    page.auth()
    page.should_be_main_page()


def test_auth_with_short_wrong_pass(browser):
    page = SignPage(browser, link)
    page.open()
    page.email = email_pass[1][0]
    page.password = email_pass[1][1]
    page.auth()
    page.should_be_invalid_message()


def test_auth_with_wrong_format_email(browser):
    page = SignPage(browser, link)
    page.open()
    page.email = email_pass[2][0]
    page.password = email_pass[2][1]
    page.auth()
    page.should_be_invalid_login()


def test_auth_with_wrong_email(browser):
    page = SignPage(browser, link)
    page.open()
    page.email = email_pass[3][0]
    page.password = email_pass[3][1]
    page.auth()
    page.should_be_invalid_message()


def test_auth_with_wrong_email_and_pass(browser):
    page = SignPage(browser, link)
    page.open()
    page.email = email_pass[4][0]
    page.password = email_pass[4][1]
    page.auth()
    page.should_be_invalid_message()

