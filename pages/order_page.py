from selenium import webdriver
import allure

from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from locators.questions_page_locators import QuestionsPageLocators
from .base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить имя')
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step('Заполнить фамилию')
    def fill_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step('Заполнить адрес')
    def fill_addres(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбрать станцию метро')
    def choose_undeground_station_1(self):
        self.driver.find_element(*OrderPageLocators.UNDEGROUND_INPUT).click()
        self.driver.find_element(*OrderPageLocators.UNDEGROUND_STATION_1).click()

    @allure.step('Выбрать станцию метро')
    def choose_undeground_station_2(self):
        self.driver.find_element(*OrderPageLocators.UNDEGROUND_INPUT).click()
        self.driver.find_element(*OrderPageLocators.UNDEGROUND_STATION_2).click()

    @allure.step('Заполнить телефон')
    def fill_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

    @allure.step('Нажать на кнопку Далее')
    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Выбрать дату заказа')
    def fill_date(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(date)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self):
        self.driver.find_element(*OrderPageLocators.EMPTY_PLACE).click()
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_INPUT).click()
        self.driver.find_element(*OrderPageLocators.RENT_PERION_DROPDOWN_2_DAYS).click()

    @allure.step('Выбрать цвет')
    def choose_color(self):
        self.driver.find_element(*OrderPageLocators.COLOR_CHOICE_GREY).click()

    @allure.step('Нажать кнопку Заказать')
    def click_on_make_order_button(self):
        self.driver.find_element(*OrderPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.SAY_YES_ORDER_BUTTON).click()

    @allure.step('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_order_is_processed(self): #надо найти способ, как проверить всю строку включая номер заказа, но номер заказа заменить на какие-то символы, показав питону, что мы их не знаем
        text = self.driver.find_element(*OrderPageLocators.ORDER_IS_MAID_MODAL_WINDOW).text
        assert "Заказ оформлен" in text, 'Нет подтверждения, что заказ оформлен.'

    @allure.step('Проверить, что во всплывающем окне есть кнопка Посмотреть статус')
    def check_button_to_view_status_is_presented(self):
        assert self.driver.find_element(*OrderPageLocators.VIEW_STATUS_BUTTON_IN_MODAL_WINDOW), \
            'Кнопки "Посмотреть статус" нет в модальном окне подтверждения заказа.'

    def big_order_button_on_page(self):
        return self.driver.find_element(*QuestionsPageLocators.BIG_ORDER_BUTTON)

    @allure.step('Перейти на страницу оформления заказа по кнопке Заказать внутри главной страницы')
    def go_to_oreder_page_via_big_button_on_page(self):
        self.big_order_button_on_page().click()

    def make_order_via_button_in_header(self, name, surname, address, phone, date):
        self.go_to_oreder_page_via_button_in_header()
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_addres(address)
        self.choose_undeground_station_1()
        self.fill_phone(phone)
        self.click_on_next_button()
        self.fill_date(date)
        self.choose_rent_period()
        self.choose_color()
        self.click_on_make_order_button()
        self.confirm_order()
        self.check_order_is_processed()
        self.check_button_to_view_status_is_presented()

    def make_order_via_button_on_page(self, name, surname, address, phone, date):
        self.go_to_oreder_page_via_big_button_on_page()
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_addres(address)
        self.choose_undeground_station_1()
        self.fill_phone(phone)
        self.click_on_next_button()
        self.fill_date(date)
        self.choose_rent_period()
        self.choose_color()
        self.click_on_make_order_button()
        self.confirm_order()
        self.check_order_is_processed()
        self.check_button_to_view_status_is_presented()