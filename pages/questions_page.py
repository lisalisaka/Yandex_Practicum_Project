import allure
from pages import env
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_page_locators import QuestionsPageLocators
from .base_page import BasePage

class QuestionsPage(BasePage):

    QUESTIONS_AND_ANSWERS = [(QuestionsPageLocators.COST_QUESTION, env.answer1),
                             (QuestionsPageLocators.COUNT_QUESTION, env.answer2),
                             (QuestionsPageLocators.TIME_RENT_QUESTION, env.answer3),
                             (QuestionsPageLocators.START_TODAY_QUESTION, env.answer4),
                             (QuestionsPageLocators.CHANGE_RENT_TIME_QUESTION, env.answer5),
                             (QuestionsPageLocators.CHARGE_QUESTION, env.answer6),
                             (QuestionsPageLocators.CANCEL_ORDER_QUESTION, env.answer7),
                             (QuestionsPageLocators.OUT_OF_MKAD_QUESTION, env.answer8)]
    @allure.step('Найти вопрос в аккордионе')
    def find_question(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти раскрытый вопрос и его ответ')
    def find_not_hidden_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((QuestionsPageLocators.OPENED_ANSWER_TEXT)))
        self.answer = self.driver.find_element(*QuestionsPageLocators.OPENED_ANSWER_TEXT).text
        return self.answer

    @allure.step('Проверить, что текст ответа открытого вопроса соответствует ожидаемому')
    def compare_fact_and_expectable_answer(self, expectable_answer):
        self.find_not_hidden_answer()
        assert self.answer == expectable_answer