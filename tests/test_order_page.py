import pytest
import allure
from selenium import webdriver
from pages import env
from pages.order_page import OrderPage
from pages.base_page import BasePage


@allure.title('Оформление заказа через кнопку Заказать в хедере приложения')
@allure.description(
'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
@pytest.mark.parametrize('name,surname,address,phone,date', env.data_for_tests)
def test_make_order_via_order_button_in_header(driver, name, surname, address, phone, date):
    driver.get(env.base_pase_link)
    page = OrderPage(driver)
    page.get_cookies()
    page.make_order_via_button_in_header(name, surname, address, phone, date)

@allure.title('Оформление заказа через кнопку Заказать внутри главной страницы')
@allure.description(
'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
@pytest.mark.parametrize('name,surname,address,phone,date', env.data_for_tests)
def test_make_order_via_big_order_button_on_page(driver, name, surname, address, phone, date):
    driver.get(env.base_pase_link)
    page = OrderPage(driver)
    page.get_cookies()
    page.make_order_via_button_on_page(name, surname, address, phone, date)
    """
class TestMakeOrderPositiveCaseOpenModalWindowAboutSuccess(OrderPage):

    driver = None
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = webdriver.Firefox()
        self.driver.get(env.base_pase_link)
        page = BasePage()
        page.get_cookies(self, driver)
        yield
        self.driver.quit()
    @pytest.mark.parametrize('name,surname,address,phone,date', env.data_for_tests)
    def test_make_order_via_big_order_button_on_page(self, name, surname, address, phone, date):
        #self.driver.get(env.base_pase_link)
        #page.get_cookies()
        page.make_order_via_button_on_page(name, surname, address, phone, date)"""