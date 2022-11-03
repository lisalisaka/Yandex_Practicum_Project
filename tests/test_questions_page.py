import pytest
import allure
from pages import env
from pages.questions_page import QuestionsPage


@allure.title('Раздел «Вопросы о важном» - при клике на вопрос открывается соответствующий ответ')
@pytest.mark.parametrize('question_locator, expectable_answer', QuestionsPage.QUESTIONS_AND_ANSWERS)
def test_fact_answer_is_equal_expectable(driver, question_locator, expectable_answer):
    driver.get(env.base_pase_link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question(question_locator)
    page.compare_fact_and_expectable_answer(expectable_answer)