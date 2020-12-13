import logging

from src.locators.home_locators import HomePageLocators as hpl
from Utils.base_page import Page
import requests
from Utils import base_page


class ValidateDate(Page):

    def enter_text(self, container, locator, text):
        logger = logging.getLogger(__name__)
        logger.info("Enter text %s in text field",text)
        self.set_field_value(hpl.__dict__[container][locator],text)
        logger.info("Successfully set the text field with %s",text)

    def get_element_present(self,container,locator):
        element = self.find_element(hpl.__dict__[container][locator])
        return element

    def open(self, url):
        """open the page to the url using webdriver's get function.
        Args:
        url (str): url of page to append to page base url
        """
        logger = logging.getLogger(__name__)
        logger.info("Opening page with url %s", url)
        self.driver.get(url)


