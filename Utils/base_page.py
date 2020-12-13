import logging
from selenium.common.exceptions import (ElementNotVisibleException, StaleElementReferenceException, WebDriverException,
                                        NoSuchElementException, TimeoutException)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from Utils import logger_helper

class Page(object):

    @logger_helper.log_func_name
    def __init__(self, selenium_driver,
                 base_url='https://www.jagermeister.com/en-GB/home',
                 timeout=60):
        """Summary
        Args:
            selenium_driver (object): selenium webdriver to navigate pages with
            base_url (str, optional): url prefix for which other urls are based
            timeout (int, optional): seconds to wait for conditions to be
            satisfied
        Raises:
            Exception: Raise exception if verifiable_elements aren't verified
        """
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = timeout
        self.logged_in = False
        logger = logging.getLogger(__name__)
        logger.info("Instance created of %s", self.__class__.__name__)

    @logger_helper.log_func_name
    def find_element(self, locator, timeout=None):
        """Return the element specified with value using the `by` selector type.
        If timeout is reached without finding element in the page,
        take a screenshot and return None for the element.
        Args:
            by (object): the selenium selection type for the value.
                http://selenium-python.readthedocs.org/en/latest/api.html#selenium.webdriver.common.by.By
                for supported locator strategies
            value (str): value locator strategy uses to evaluate presence of
            element
            timeout (int, optional): seconds to wait for selector condition to
                be satisfied
        """
        if timeout is None:
            timeout = self.timeout

        element = None
        logger = logging.getLogger(__name__)
        try:
            logger_message = "Finding element with %s as locator"
            logger.info(logger_message, locator)
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
           )
        except WebDriverException:
            logger_message = "Element with %s locator not found!"
            logger.exception(logger_message, locator)
        finally:
            logger.info("this element is: %s", element)
            return element

    @logger_helper.log_func_name
    def click_element(self, locator, timeout=None):
        """Click the element specified with value using the by selector type.
        Args:
            by (object): the selenium selection type for the value.
                http://selenium-python.readthedocs.org/en/latest/api.html#selenium.webdriver.common.by.By
                for supported locator strategies
            value (str): value locator strategy uses to evaluate presence of
                element
        """

        if timeout is None:
            timeout = self.timeout

        logger = logging.getLogger(__name__)
        logger_message = "Clicking on element with %s value for locator"
        logger.info(logger_message, locator)

        try:
            element_to_click = self.find_element(
                locator, timeout)
            element_location = element_to_click.location
            logger.info("Element location: %s", element_location)
            element_to_click.click()
            logger.info("Element successfully clicked!")
        except (WebDriverException,
                ElementNotVisibleException,
                StaleElementReferenceException):
            self.scroll_to_make_element_visible_on_screen(locator)
            element_to_click = self.find_element(
                locator, timeout)
            element_to_click.click()
            logger.info("Element is enabled, displayed and clickable.")

    @logger_helper.log_func_name
    def set_field_value(self, locator, text, timeout=None):
        """Set field value in selector provided with text value supplied.
      Args:
            by (object): the selenium selection type for the value.
                http://selenium-python.readthedocs.org/en/latest/api.html#selenium.webdriver.common.by.By
                for supported locator strategies
            value (str): value locator strategy uses to evaluate presence of
            element
            text (str): text to set a field to
            timeout (int, optional): seconds to wait for selector condition to
                be satisfied
        """
        if not timeout:
            timeout = self.timeout

        try:
            logger = logging.getLogger(__name__)
            logger_message = "Entering %s on element with %s value for locator"
            logger.info(logger_message, text, locator)
            input_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator))

            input_element.clear()
            input_element.send_keys(text)
            #input_element.send_keys(Keys.ENTER)

        except:
            self.scroll_to_make_element_visible_on_screen_via_css(locator)
            input_element = self.find_element(locator)
            input_element.clear()
            input_element.send_keys(text)

