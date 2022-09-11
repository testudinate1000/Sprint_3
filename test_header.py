from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import LoginPageLocators, MainPageLocators, AccountPageLocators


class TestHeader:
    driver = webdriver.Chrome()
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    main_page_url = 'https://stellarburgers.nomoreparties.site/'
    email = 'elenakuznetsova2123@yandex.ru'
    password = '123456789'

    def __int__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def test_go_to_account_for_unauthorized_user(self):
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        # Кликнуть по кнопке "Личный кабинет"
        self.driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        self.driver.quit()

    def test_go_to_account_for_authorized_user(self):
        # Открыть главную страницу
        self.driver.maximize_window()
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        # Нажать кнопку Войти в аккаунт
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Подождать пока страница авторизации загрузится
        login_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Авторизоваться
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(self.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(self.password)
        login_button.click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        # Перейти в личный кабинет
        self.driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()

        # Убедиться, что открыт аккаунт
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )

        self.driver.quit()

    def test_go_to_constructor_from_account(self):
        self.driver.get(self.login_page_url)

        # Подождать пока страница авторизации загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Нажать кнопку Конструктор
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()

    def test_logo_button(self):
        self.driver.get(self.login_page_url)

        # Подождать пока страница авторизации загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        # Нажать кнопку лого
        self.driver.find_element(*MainPageLocators.LOGO).click()

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TITLE))

        self.driver.quit()
