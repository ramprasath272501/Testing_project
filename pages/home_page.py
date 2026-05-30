"""Page Object for the Automation Exercise home page (and global footer)."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class HomePage(BasePage):
    # Navigation
    PRODUCTS_NAV = (By.XPATH, "//a[@href='/products']")
    LOGIN_NAV = (By.XPATH, "//a[@href='/login']")
    CART_NAV = (By.XPATH, "//a[@href='/view_cart']")
    SLIDER = (By.ID, "slider")

    # Footer subscription (NOTE: the site's input id is intentionally
    # misspelled as 'susbscribe_email' - a well-known quirk of this app)
    SUBSCRIBE_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")
    SUBSCRIBE_SUCCESS = (By.CSS_SELECTOR, "#success-subscribe .alert-success")

    def load(self):
        self.open(ConfigReader.get("general", "base_url"))
        return self

    def is_loaded(self):
        return self.is_visible(self.SLIDER)

    def go_to_products(self):
        self.click(self.PRODUCTS_NAV)

    def go_to_login(self):
        self.click(self.LOGIN_NAV)

    def subscribe(self, email):
        self.scroll_into_view(self.SUBSCRIBE_EMAIL)
        self.type(self.SUBSCRIBE_EMAIL, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def get_subscription_message(self):
        return self.get_text(self.SUBSCRIBE_SUCCESS)
