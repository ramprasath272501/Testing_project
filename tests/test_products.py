"""Product browsing + search tests, including a data-driven (parametrized) search."""
import pytest

from pages.products_page import ProductsPage


@pytest.mark.smoke
def test_all_products_page_loads(driver):
    products = ProductsPage(driver).load()
    assert products.is_loaded()
    assert products.product_count() > 0, "No products rendered on the listing page"


@pytest.mark.regression
@pytest.mark.parametrize("search_term", ["top", "dress", "tshirt"])
def test_search_returns_results(driver, search_term):
    products = ProductsPage(driver).load()
    products.search(search_term)
    assert products.searched_products_visible(), (
        f"'Searched Products' header not shown for term '{search_term}'"
    )
    assert products.product_count() > 0, f"No results for '{search_term}'"
