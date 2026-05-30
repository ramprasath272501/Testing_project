"""Footer subscription test - exercises scrolling + a dynamic success banner."""
import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_footer_subscription_success(driver):
    home = HomePage(driver).load()
    home.subscribe("qa_subscriber@example.com")
    assert "successfully subscribed" in home.get_subscription_message().lower()
