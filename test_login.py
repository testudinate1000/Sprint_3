from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from locators import LoginPageLocators, MainPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators


class TestLogin:
    driver = webdriver.Chrome()
    email = 'elenakuznetsova2123@yandex.ru'
    password = '123456789'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    main_page_url = 'https://stellarburgers.nomoreparties.site/'
    registration_page_url = 'https://stellarburgers.nomoreparties.site/register'

    def __int__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def test_success_auth_on_login_page(self):
        self.driver.get(self.login_page_url)

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Заполнить email и пароль валидными данными
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)

        # Нажать кнопку авторизации
        login_button.click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()

    def test_success_auth_on_main_page(self):
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        # Кликнуть по кнопке "Личный кабинет"
        self.driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Заполнить email и пароль валидными данными
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)

        # Нажать кнопку авторизации
        login_button.click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()

    def test_success_auth_on_registration_page(self):
        self.driver.get(self.registration_page_url)
        # Подождать пока страница регистрации загрузится
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SIGN_IN_BUTTON))

        # По кнопке Войти перейти на страницу авторизации
        self.driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Заполнить email и пароль валидными данными
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)

        # Нажать кнопку авторизации
        login_button.click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()

    def test_success_auth_by_forgot_password_link(self):
        self.driver.get(self.login_page_url)
        # Подождать пока страница авторизации загрузится
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # По кнопке Восстановить пароль перейти на страницу авторизации
        self.driver.find_element(*LoginPageLocators.FORGOT_PASS_LINK).click()

        # Подождать пока страница Восстановления пароля загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(ForgotPasswordPageLocators.TITLE))
        time.sleep(3)

        # Нажать кнопку Войти
        self.driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Заполнить email и пароль валидными данными
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)

        # Нажать кнопку авторизации
        login_button.click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()

