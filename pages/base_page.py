"""BasePage - shared building blocks for every Page Object.

All interactions go through explicit waits (WebDriverWait) instead of
time.sleep(), which is what keeps a Selenium suite fast and non-flaky.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.config_reader import ConfigReader
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_int("general", "explicit_wait", 15)
        self.wait = WebDriverWait(self.driver, self.timeout)

    # --- navigation ---------------------------------------------------------
    def open(self, url):
        logger.info("Navigating to %s", url)
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    # --- element interactions (all wait-backed) -----------------------------
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Return True/False instead of raising - handy for assertions."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            logger.warning("Element not visible within %ss: %s", self.timeout, locator)
            return False

    def count(self, locator):
        self.wait.until(lambda d: len(d.find_elements(*locator)) > 0)
        return len(self.driver.find_elements(*locator))

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element
