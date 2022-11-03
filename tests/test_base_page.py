import pytest
import allure
from pages import env
from pages.base_page import BasePage


@allure.title('Проверка клика на логотип Яндекса c разных страниц приложения')
@allure.description(
'На странице ищем логотоип "Яндекса" в хедере страницы и проверяем, что в новой вкладке открывается Дзен')
@pytest.mark.parametrize('link', [env.base_pase_link, env.order_page_link, env.track_page_link])
def test_click_on_logo_open_dzen_in_new_window(driver, link):
    driver.get(link)
    page = BasePage(driver)
    page.check_click_on_yandex_logo_open_dzen()

@allure.title('Проверка клика на логотип "Самоката" c разных страниц приложения')
@allure.description(
'На странице ищем логотоип "Самокат" в хедере страницы и проверяем редирект на главную при клику по нему')
@pytest.mark.parametrize('link', [env.base_pase_link, env.order_page_link, env.track_page_link])
def test_click_on_app_logo_open_base_page(driver, link):
    driver.get(link)
    page = BasePage(driver)
    page.check_click_on_app_logo_open_base_page()