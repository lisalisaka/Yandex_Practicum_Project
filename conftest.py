import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart Firefox browser for test..")
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    print("\nquit browser..")
    driver.quit()