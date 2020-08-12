from selenium.webdriver.common.by import By


class SignPageLocators():
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[class="btn capsbtn signin"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#signin-login')
    PASS_INPUT = (By.CSS_SELECTOR, '#signin-pass')
    SUBMINT_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-success capsbtn sign__submit"]')
    LOGIN_OR_PASS_INCORRECT = (By.XPATH, '//div[text()="Login or password is incorrect!"]')
    LOGIN_INCORRECT = (By.XPATH, '//div[text()="Please enter correct email address or phone."]')


class MainPageLocators():
    PROFILE_ICON = (By.CSS_SELECTOR, '[class="fas fa-user-circle fa-2x fa-fw text-white"]')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '[class="btn btn-primary capsbtn dropdown-toggle userdropdown"]')
    PROFILE_MENU = (By.XPATH, '//a[text()="Profile"]')
    USER_NAME_INPUT = (By.CSS_SELECTOR, '#profile-name')
    EMAIL_PROFILE_INPUT = (By.CSS_SELECTOR, '#profile-email')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#profile-country')
    PHONE_INPUT = (By.CSS_SELECTOR, '#profile-phone')
    DIAL_CODE_INPUT = (By.CSS_SELECTOR, '[placeholder="Dial code"]')
    BUSINESS_SEGMENT_DROPDOWN = (By.CSS_SELECTOR,'#profile-busseg')
    UPDATE_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-success capsbtn sign__submit"]')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '[class="alert alert-success alert-dismissible fade show"]')
    INVALID_EMAIL_MESSAGE = (By.XPATH, '//div[text()="Please enter correct email address."]')
    INVALID_PHONE_MESSAGE = (By.XPATH, '//div[contains(text(), "valid phone number")]')



