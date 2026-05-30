"""Login / signup tests demonstrating positive-navigation and negative paths."""
import time

import pytest

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


@pytest.mark.regression
@pytest.mark.login
def test_login_with_invalid_credentials_shows_error(driver):
    login = LoginPage(driver).load()
    login.login(
        ConfigReader.get("test_data", "invalid_email"),
        ConfigReader.get("test_data", "invalid_password"),
    )
    assert "incorrect" in login.get_login_error().lower()


@pytest.mark.regression
@pytest.mark.login
def test_new_user_signup_navigates_to_account_info(driver):
    login = LoginPage(driver).load()
    unique_email = f"qa_auto_{int(time.time())}@example.com"
    login.start_signup("QA Tester", unique_email)
    assert login.is_account_info_displayed(), (
        "Signup did not navigate to the 'Enter Account Information' page"
    )
