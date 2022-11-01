from selenium import webdriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .locators import QuestionsPageLocators
from .base_page import BasePage

class QuestionsPage(BasePage):

    @allure.step('Найти первый вопрос')
    def find_question_about_cost(self):
        element = self.driver.find_element(*QuestionsPageLocators.COST_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((QuestionsPageLocators.COST_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.COST_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_cost(self):
        self.find_not_hidden_answer()
        assert self.answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.step('Найти второй вопрос')
    def find_question_about_count(self):
        element = self.driver.find_element(*QuestionsPageLocators.COUNT_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.COUNT_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.COUNT_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_count(self):
        self.find_not_hidden_answer()
        assert self.answer == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.step('Найти третий вопрос')
    def find_question_about_time_rent(self):
        element = self.driver.find_element(*QuestionsPageLocators.TIME_RENT_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.TIME_RENT_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.TIME_RENT_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_time_rent(self):
        self.find_not_hidden_answer()
        assert self.answer == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.step('Найти четвертый вопрос')
    def find_question_about_today_start(self):
        element = self.driver.find_element(*QuestionsPageLocators.START_TODAY_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.START_TODAY_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.START_TODAY_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_today_start(self):
        self.find_not_hidden_answer()
        assert self.answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.step('Найти пятый вопрос')
    def find_question_about_change_rent_time(self):
        element = self.driver.find_element(*QuestionsPageLocators.CHANGE_RENT_TIME_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.CHANGE_RENT_TIME_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.CHANGE_RENT_TIME_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_change_rent_time(self):
        self.find_not_hidden_answer()
        assert self.answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.step('Найти шестой вопрос')
    def find_question_about_charge(self):
        element = self.driver.find_element(*QuestionsPageLocators.CHARGE_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.CHARGE_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.CHARGE_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_charge(self):
        self.find_not_hidden_answer()
        assert self.answer == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.step('Найти седьмой вопрос')
    def find_question_about_cancel_order(self):
        element = self.driver.find_element(*QuestionsPageLocators.CANCEL_ORDER_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.CANCEL_ORDER_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.CANCEL_ORDER_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_cancel_order(self):
        self.find_not_hidden_answer()
        assert self.answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.step('Найти восьмой вопрос')
    def find_question_about_outside_mkad(self):
        element = self.driver.find_element(*QuestionsPageLocators.OUT_OF_MKAD_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((QuestionsPageLocators.OUT_OF_MKAD_QUESTION)))
        self.driver.find_element(*QuestionsPageLocators.OUT_OF_MKAD_QUESTION).click()

    @allure.step('Проверить, что открывается соответствующий текст')
    def check_answer_text_about_outside_mkad(self):
        self.find_not_hidden_answer()
        assert self.answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def find_not_hidden_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((QuestionsPageLocators.OPENED_ANSWER_TEXT)))
        self.answer = self.driver.find_element(*QuestionsPageLocators.OPENED_ANSWER_TEXT).text
        return self.answer