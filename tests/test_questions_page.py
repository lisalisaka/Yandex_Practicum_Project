import pytest
import allure
from pages import env
from selenium import webdriver
from pages.questions_page import QuestionsPage

@allure.suite('Test suite to check answers')
class TestQuestionPage:

    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get(env.base_pase_link)
        yield
        self.driver.quit()

    @allure.title('Раздел «Вопросы о важном» - при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator, expectable_answer', QuestionsPage.QUESTIONS_AND_ANSWERS)
    def test_fact_answer_is_equal_expectable(self, question_locator, expectable_answer):
        page = QuestionsPage(self.driver)
        page.get_cookies()
        page.find_question(question_locator)
        page.compare_fact_and_expectable_answer(expectable_answer)
