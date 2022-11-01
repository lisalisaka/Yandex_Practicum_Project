import allure
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from .locators import BasePageLocators

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принять куки')
    def get_cookies(self):
        self.driver.find_element(*BasePageLocators.GET_COOKIE_BUTTON).click()

    def order_button(self):
        return self.driver.find_element(*BasePageLocators.ORDER_BUTTON)

    @allure.step('Нажать на кнопку Заказать в хедере страницы')
    def go_to_oreder_page_via_button_in_header(self):
        self.order_button().click()

    @allure.step('Нажать на логотип Яндекса в хедере страницы')
    def yandex_logo(self):
        return self.driver.find_element(*BasePageLocators.YANDEX_lOGO)

    @allure.step('Нажать на логотип "Самокат" в хедере страницы')
    def app_logo(self):
        return self.driver.find_element(*BasePageLocators.APP_SCOOTER_LOGO)

    @allure.step('Перейти на открывшуюся вкладку браузера и сравнить url с ожидаемым')
    def check_click_on_yandex_logo_open_dzen(self):
        self.yandex_logo().click()
        self.new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(self.new_window)
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'), 'Dzen URL not found')
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', 'URL of redirected page does not match expextable result'

    @allure.step('Кликнуть на лого приложения и сравнить url с ожидаемым')
    def check_click_on_app_logo_open_base_page(self):
        self.app_logo().click()
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/'))
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/', 'URL does not match expextable result'
