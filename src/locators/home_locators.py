
from selenium.webdriver.common.by import By


class HomePageLocators(object):

    date_selector = {
        'month':    (By.XPATH, "//input[@id='MM']"),
        'day':      (By.XPATH, "//input[@id='DD']"),
        'year':     (By.XPATH, "//input[@id='YYYY']")
    }

    country_selector = {

        'logout':   (By.XPATH, "//button[contains(@class,'countryselectorbutton_button__2W2_d-')]/div"),
        'country':  (By.XPATH, "//span[contains(text(),'Germany')]/../a")
    }

    labels = {
        'invalid_day':      (By.XPATH, "//div[contains(text(),'Invalid day input')]"),
        'invalid_month':    (By.XPATH, "//div[contains(text(),'Invalid month input')]"),
        'invalid_year':     (By.XPATH, "//div[contains(text(),'Invalid year input')]"),
        'invalid_message':  (By.XPATH, "//div[contains(@class,'verificationError_message__12kUk-')]"),
        'valid':            (By.XPATH, "//div[contains(@class,'connectButton_icon__3jQ8x-')]")
    }
