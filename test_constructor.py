import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators


class TestConstructor:
    driver = webdriver.Chrome()
    main_page_url = 'https://stellarburgers.nomoreparties.site/'

    def __int__(self, driver):
        self.driver = driver

    def test_go_to_sauce_tab(self):
        self.driver.maximize_window()
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNKS_TITLE))

        # Кликнуть Соусы
        self.driver.find_element(*MainPageLocators.SAUCE_TAB).click()

        self.driver.quit()

    def test_go_to_filling_tab(self):
        self.driver.maximize_window()
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNKS_TITLE))

        # Кликнуть Начинки
        self.driver.find_element(*MainPageLocators.FILLING_TAB).click()

        self.driver.quit()

    def test_go_to_bunks_tab(self):
        self.driver.maximize_window()
        self.driver.get(self.main_page_url)

        # Подождать пока главная страница загрузится
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNKS_TITLE))

        # Кликнуть Начинки
        self.driver.find_element(*MainPageLocators.FILLING_TAB).click()

        # Кликнуть Булки
        self.driver.find_element(*MainPageLocators.BUNKS_TAB).click()

        self.driver.quit()


