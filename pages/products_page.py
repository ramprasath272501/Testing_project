"""Page Object for the Products listing + search results."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'All Products')]")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def load(self):
        base = ConfigReader.get("general", "base_url")
        self.open(f"{base}/products")
        return self

    def is_loaded(self):
        return self.is_visible(self.ALL_PRODUCTS_TITLE)

    def search(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)

    def product_count(self):
        return self.count(self.PRODUCT_ITEMS)
