import allure
from pages.questions_page import QuestionsPage
from pages.locators import QuestionsPageLocators

link = 'https://qa-scooter.praktikum-services.ru/'

@allure.title('Раздел «Вопросы о важном» - при клике на первый вопрос открывается соответствующий ответ')
def test_check_answer_about_cost(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_cost()
    page.check_answer_text_about_cost()

@allure.title('Раздел «Вопросы о важном» - при клике на второй вопрос открывается соответствующий ответ')
def test_check_answer_about_count(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_count()
    page.check_answer_text_about_count()

@allure.title('Раздел «Вопросы о важном» - при клике на третий вопрос открывается соответствующий ответ')
def test_check_answer_about_time_rent(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_time_rent()
    page.check_answer_text_about_time_rent()

@allure.title('Раздел «Вопросы о важном» - при клике на 4ый вопрос открывается соответствующий ответ')
def test_check_answer_about_today_start(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_today_start()
    page.check_answer_text_about_today_start()

@allure.title('Раздел «Вопросы о важном» - при клике на 5ый вопрос открывается соответствующий ответ')
def test_check_answer_about_change_rent_time(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_change_rent_time()
    page.check_answer_text_about_change_rent_time()

@allure.title('Раздел «Вопросы о важном» - при клике на 6ой вопрос открывается соответствующий ответ')
def test_check_answer_about_charge(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_charge()
    page.check_answer_text_about_charge()

@allure.title('Раздел «Вопросы о важном» - при клике на 7ой вопрос открывается соответствующий ответ')
def test_check_answer_about_cancel_order(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_cancel_order()
    page.check_answer_text_about_cancel_order()

@allure.title('Раздел «Вопросы о важном» - при клике на 8ой вопрос открывается соответствующий ответ')
def test_check_answer_about_outside_mkad(driver):
    driver.get(link)
    page = QuestionsPage(driver)
    page.get_cookies()
    page.find_question_about_outside_mkad()
    page.check_answer_text_about_outside_mkad()