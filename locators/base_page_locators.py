from selenium.webdriver.common.by import By

class BasePageLocators():
    GET_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    YANDEX_lOGO = (By.XPATH, ".//img[@alt='Yandex']")
    APP_SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")