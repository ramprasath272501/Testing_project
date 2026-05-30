"""Creates WebDriver instances.

Uses Selenium Manager (built into Selenium 4.6+) to auto-resolve the correct
driver binary - so there is no webdriver-manager dependency or manual setup.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.logger import get_logger

logger = get_logger(__name__)


class DriverFactory:
    @staticmethod
    def get_driver(browser: str = "chrome", headless: bool = True):
        browser = (browser or "chrome").lower().strip()
        logger.info("Launching '%s' driver (headless=%s)", browser, headless)

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            # Flags required for stable runs in CI / containers
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(
                f"Unsupported browser '{browser}'. Use 'chrome' or 'firefox'."
            )

        driver.maximize_window()
        return driver
