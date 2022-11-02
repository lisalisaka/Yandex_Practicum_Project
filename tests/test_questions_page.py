import pytest
import allure
from pages.questions_page import QuestionsPage
from pages.locators import QuestionsPageLocators

answer1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
answer2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
answer3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
answer4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
answer5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
answer6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
answer7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
answer8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
link = 'https://qa-scooter.praktikum-services.ru/'
QUESTIONS_AND_ANSWERS = [(QuestionsPageLocators.COST_QUESTION, answer1),
                         (QuestionsPageLocators.COUNT_QUESTION, answer2),
                         (QuestionsPageLocators.TIME_RENT_QUESTION, answer3),
                         (QuestionsPageLocators.START_TODAY_QUESTION, answer4),
                         (QuestionsPageLocators.CHANGE_RENT_TIME_QUESTION, answer5),
                         (QuestionsPageLocators.CHARGE_QUESTION, answer6),
                         (QuestionsPageLocators.CANCEL_ORDER_QUESTION, answer7),
                         (QuestionsPageLocators.OUT_OF_MKAD_QUESTION, answer8)]
@allure.title('Раздел «Вопросы о важном» - при клике на вопрос открывается соответствующий ответ')
@pytest.mark.parametrize('question_locator, expectable_answer', QUESTIONS_AND_ANSWERS)
def test_fact_answer_is_equal_expectable(driver, question_locator, expectable_answer):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question(question_locator)
    page.compare_fact_and_expectable_answer(expectable_answer)