from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    TITLE = (By.XPATH, './/h1[text()="Соберите бургер"]')
    ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')
    LOGO = (By.CSS_SELECTOR, '#root > div > header > nav > div')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    BUNKS_TAB = (By.XPATH, './/span[text()="Булки"]')
    SAUCE_TAB = (By.XPATH, './/span[text()="Соусы"]')
    FILLING_TAB = (By.XPATH, './/span[text()="Начинки"]')
    BUNKS_TITLE = (By.XPATH, './/h2[text()="Булки"]')
    SAUCE_TITLE = (By.XPATH, './/h2[text()="Соусы"]')
    FILLING_TITLE = (By.XPATH, './/h2[text()="Начинки"]')


class RegistrationPageLocators(object):
    """A class for registration locators. All registration locators should
    come here"""
    TITLE = (By.XPATH, './/h2[text()="Регистрация"]')
    NAME_FIELD = (
        By.CSS_SELECTOR,
        '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')  # invalid selector
    EMAIL_FIELD = (By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Пароль"]')
    SIGN_IN_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    PASSWORD_ERROR = (By.XPATH, './/p[text()="Некорректный пароль"]')
    LOGIN_LINK = (By.XPATH, './/a[@href="/login"]')


class LoginPageLocators(object):
    """A class for login page locators."""
    TITLE = (By.XPATH, './/h2[text()="Вход"]')
    EMAIL_FIELD = (By.XPATH, './/input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    FORGOT_PASS_LINK = (By.XPATH, './/a[@href="/forgot-password"]')


class ForgotPasswordPageLocators(object):
    """A class for forgot password page locators."""
    TITLE = (By.XPATH, './/h2[text()="Восстановление пароля"]')
    LOGIN_LINK = (By.CSS_SELECTOR, '#root > div > main > div > div > p > a')


class AccountPageLocators(object):
    """A class for account page locators."""
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
