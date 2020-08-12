import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose --browser_name"
    )



@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    if browser_name in ('ch', 'Chrome', 'chrome'):
        my_options = Options()
        my_options.add_argument("--start-maximized")
        print('\nstart chrome browser for tests...')
        browser = webdriver.Chrome(options=my_options)
    else:
        fp = webdriver.FirefoxProfile()
        print('\nstart browser firefox')
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print('\nquit browser')
    browser.quit()