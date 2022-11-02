from selenium import webdriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .locators import QuestionsPageLocators
from .base_page import BasePage

class QuestionsPage(BasePage):

    @allure.step('Найти первый вопрос')
    def find_question(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти раскрытый вопрос')
    def find_not_hidden_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((QuestionsPageLocators.OPENED_ANSWER_TEXT)))
        self.answer = self.driver.find_element(*QuestionsPageLocators.OPENED_ANSWER_TEXT).text
        return self.answer

    @allure.step('Проверить, что открывается текст вопроса соответствует ожидаемому')
    def compare_fact_and_expectable_answer(self, expectable_answer):
        self.find_not_hidden_answer()
        assert self.answer == expectable_answer