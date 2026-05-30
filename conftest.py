"""Pytest fixtures and hooks shared across the whole suite.

Highlights:
- A function-scoped `driver` fixture (fresh browser per test = isolation).
- CLI overrides: --browser and --headless.
- A screenshot-on-failure hook that attaches the image to the HTML/Allure report.
"""
import os
from datetime import datetime

import pytest

from utils.config_reader import ConfigReader
from utils.driver_factory import DriverFactory
from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None,
        help="Browser to run against: chrome or firefox",
    )
    parser.addoption(
        "--headless", action="store", default=None,
        help="Run headless: true or false",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser") or ConfigReader.get(
        "general", "browser", "chrome"
    )
    headless_opt = request.config.getoption("--headless")
    if headless_opt is not None:
        headless = headless_opt.lower() == "true"
    else:
        headless = ConfigReader.get_bool("general", "headless", True)

    drv = DriverFactory.get_driver(browser, headless)
    yield drv
    logger.info("Tearing down driver")
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot whenever a test fails during the call phase."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if not drv:
            return
        os.makedirs("screenshots", exist_ok=True)
        file_path = os.path.join(
            "screenshots", f"{item.name}_{datetime.now():%H%M%S}.png"
        )
        try:
            drv.save_screenshot(file_path)
            logger.error("FAILED: %s | screenshot saved -> %s", item.name, file_path)
            try:
                import allure
                allure.attach(
                    drv.get_screenshot_as_png(),
                    name=item.name,
                    attachment_type=allure.attachment_type.PNG,
                )
            except ImportError:
                pass
        except Exception as exc:  # pragma: no cover - best-effort capture
            logger.error("Could not capture screenshot: %s", exc)
