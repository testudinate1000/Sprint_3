from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from locators import RegistrationPageLocators, LoginPageLocators


class TestRegistration:
    driver = webdriver.Chrome()
    url = 'https://stellarburgers.nomoreparties.site/register'

    def __int__(self, driver, url):
        self.driver = driver
        self.url = url

    def test_success_registration(self):
        self.driver.get(self.url)
        # Подождать пока страница регистрации загрузится
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SIGN_IN_BUTTON))

        # Заполнить обязательные поля
        self.driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys('ekuznetsova5')
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys('elenakuznetsova2125@yandex.ru')
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys('123456789')

        self.driver.find_element(*RegistrationPageLocators.SIGN_IN_BUTTON).click()

        # Подождать пока страница входа загрузится
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.TITLE))

        self.driver.quit()

    def test_password_error(self):
        self.driver.get(self.url)
        # Подождать пока страница регистрации загрузится
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SIGN_IN_BUTTON))

        # Заполнить имя и email
        self.driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys('ekuznetsova1')
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys('elenakuznetsova2124@ya.ru')

        # Ввести пароль длиной в 1 символ
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys('1')

        # Нажать кнопку регистрации
        self.driver.find_element(*RegistrationPageLocators.SIGN_IN_BUTTON).click()

        # Убедиться, что ошибка отображается корректно
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_ERROR)

        self.driver.quit()
