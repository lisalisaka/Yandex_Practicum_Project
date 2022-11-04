import pytest
import allure
from selenium import webdriver
from pages import env
from pages.order_page import OrderPage
from pages.base_page import BasePage

@allure.suite('E2E positive test suite about making an order')
class TestMakeOrderPositiveCaseOpenSuccessModalWindow:

    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(env.base_pase_link)
        yield
        self.driver.quit()

    @allure.title('Оформление заказа через кнопку Заказать в хедере приложения')
    @allure.description(
        'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('name,surname,address,phone,date', env.data_for_tests)
    def test_make_order_via_order_button_in_header(self, name, surname, address, phone, date):
        page = OrderPage(self.driver)
        page.get_cookies()
        page.make_order_via_button_in_header(name, surname, address, phone, date)

    @allure.title('Оформление заказа через кнопку Заказать внутри главной страницы')
    @allure.description(
        'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('name,surname,address,phone,date', env.data_for_tests)
    def test_make_order_via_big_order_button_on_page(self, name, surname, address, phone, date):
        page = OrderPage(self.driver)
        page.get_cookies()
        page.make_order_via_button_on_page(name, surname, address, phone, date)
