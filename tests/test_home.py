"""Smoke tests for the home page - the most critical 'is the app up?' checks."""
import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_loads(driver):
    home = HomePage(driver).load()
    assert "Automation Exercise" in home.get_title()
    assert home.is_loaded(), "Home page banner/slider was not displayed"
