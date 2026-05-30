# Selenium + PyTest UI Automation Framework

[![Selenium PyTest CI](https://github.com/ramprasath272501/Testing_project/actions/workflows/ci.yml/badge.svg)](https://github.com/ramprasath272501/Testing_project/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-8.x-0A9EDC?logo=pytest&logoColor=white)
![Design](https://img.shields.io/badge/Pattern-Page%20Object%20Model-orange)

A clean, scalable **UI test automation framework** built with **Selenium WebDriver + Python + PyTest** following the **Page Object Model (POM)** design pattern. It runs end-to-end against [automationexercise.com](https://automationexercise.com) — a full e-commerce demo application — and executes automatically on every push via **GitHub Actions CI**.

> Built to demonstrate real-world automation practices: maintainable Page Objects, explicit waits (no `time.sleep`), data-driven tests, config-driven environments, automatic screenshot-on-failure, HTML reporting, and continuous testing in CI/CD.

---

## Tech Stack

| Area | Tooling |
|------|---------|
| Language | Python 3.11 |
| Automation | Selenium WebDriver 4.x (Selenium Manager — no manual driver setup) |
| Test Runner | PyTest |
| Design Pattern | Page Object Model (POM) |
| Reporting | pytest-html, Allure (optional) |
| Parallel Execution | pytest-xdist |
| CI/CD | GitHub Actions |

---

## Project Structure

```
Testing_Project/
├── config/
│   └── config.ini            # base URL, browser, timeouts, test data
├── pages/                    # Page Object Model layer
│   ├── base_page.py          # shared wait-backed actions (find/click/type...)
│   ├── home_page.py
│   ├── login_page.py
│   └── products_page.py
├── tests/                    # test cases (grouped by feature)
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_subscription.py
├── utils/
│   ├── config_reader.py      # reads config.ini
│   ├── driver_factory.py     # creates Chrome/Firefox drivers
│   └── logger.py             # console + file logging
├── conftest.py               # fixtures + screenshot-on-failure hook
├── pytest.ini                # markers + run options
├── requirements.txt
└── .github/workflows/ci.yml  # runs the suite on every push
```

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- Google Chrome (or Firefox) installed

### 2. Install
```bash
git clone https://github.com/ramprasath272501/Testing_project.git
cd Testing_project
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the tests
```bash
# Run everything (headless by default, per config.ini)
pytest

# Watch it run in a real browser window
pytest --headless false

# Run a specific suite by marker
pytest -m smoke
pytest -m regression
pytest -m login

# Run on Firefox instead of Chrome
pytest --browser firefox

# Run in parallel across 4 workers
pytest -n 4

# Generate a self-contained HTML report
pytest --html=reports/report.html --self-contained-html
```

---

## Test Coverage

| Suite | What it validates | Markers |
|-------|-------------------|---------|
| `test_home.py` | Home page loads, title + banner present | `smoke` |
| `test_products.py` | Product listing renders; **data-driven search** across multiple terms | `smoke`, `regression` |
| `test_login.py` | Invalid login shows error; new-user signup navigation | `regression`, `login` |
| `test_subscription.py` | Footer subscription success (scroll + dynamic banner) | `regression` |

---

## Key Design Decisions

- **Page Object Model** keeps locators and page actions out of the tests, so UI changes are fixed in one place.
- **Explicit waits everywhere** (`WebDriverWait` + `expected_conditions`) — no flaky `time.sleep()`.
- **Config-driven** — switch URL, browser, or headless mode without touching test code.
- **Screenshot-on-failure** — every failing test auto-saves a screenshot and attaches it to the report.
- **CI-first** — the suite runs on every push and uploads the HTML report + failure screenshots as artifacts.

---

## Continuous Integration

Every push triggers the [CI workflow](.github/workflows/ci.yml):
1. Sets up Python + Chrome
2. Installs dependencies
3. Runs the full suite headless
4. Uploads the **HTML report** and any **failure screenshots** as downloadable artifacts

---

## Roadmap
- [ ] Add end-to-end "add to cart → checkout" purchase flow
- [ ] Add API tests against the site's REST endpoints (`/api`)
- [ ] Add a parallel **Playwright** branch to compare with Selenium
- [ ] Integrate Allure reporting with trend history

---

*Built and maintained by [Ramprasath](https://github.com/ramprasath272501) — QA Automation Engineer / SDET.*
