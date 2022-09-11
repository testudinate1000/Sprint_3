from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import LoginPageLocators, MainPageLocators, AccountPageLocators


class TestLogout:
    driver = webdriver.Chrome()
    email = 'elenakuznetsova2123@yandex.ru'
    password = '123456789'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    main_page_url = 'https://stellarburgers.nomoreparties.site/'

    def __int__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def test_logout(self):
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

        # Разлогиниться
        logout_button = WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        self.driver.quit()

