from selenium.webdriver.common.by import By

class QuestionsPageLocators():
    COST_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-0' and @role='button']")
    COUNT_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-1' and @role='button']")
    TIME_RENT_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-2' and @role='button']")
    START_TODAY_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-3' and @role='button']")
    CHANGE_RENT_TIME_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-4' and @role='button']")
    CHARGE_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-5' and @role='button']")
    CANCEL_ORDER_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-6' and @role='button']")
    OUT_OF_MKAD_QUESTION = (By.XPATH, ".//div[@id='accordion__heading-7' and @role='button']")
    #OUT_OF_MKAD_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-7' and @role='region']")
    OPENED_ANSWER_TEXT = (By.XPATH, ".//div[@role='region' and not(@hidden)]/p")
    BIG_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")