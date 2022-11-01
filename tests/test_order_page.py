import pytest
import allure
from pages.order_page import OrderPage

link = 'https://qa-scooter.praktikum-services.ru/'
data_for_tests = [('Серёжа', 'Котов', 'Санкт-Петербург, ул. Циолковского 35 кв.17', '89999111122', '11.11.22'),
                  ('Владимир', 'Вовин', 'Москва, Чёрная площадь, д.66-1', '66666666666', '01.01.23')]

@allure.title('Оформление заказа через кнопку Заказать в хедере приложения')
@allure.description(
'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
@pytest.mark.parametrize('name,surname,address,phone,date', data_for_tests)
def test_make_order_via_order_button_in_header(driver, name, surname, address, phone, date):
    driver.get(link)
    page = OrderPage(driver)
    page.get_cookies()
    page.make_order_via_button_in_header(name, surname, address, phone, date)

@allure.title('Оформление заказа через кнопку Заказать внутри главной страницы')
@allure.description(
'Открытие и заполнение формы заказа, проверка, что появляется всплывающее окно с сообщением об успешном создании заказа')
@pytest.mark.parametrize('name,surname,address,phone,date', data_for_tests)
def test_make_order_via_big_order_button_on_page(driver, name, surname, address, phone, date):
    driver.get(link)
    page = OrderPage(driver)
    page.get_cookies()
    page.make_order_via_button_on_page(name, surname, address, phone, date)