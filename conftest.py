import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, HEADLESS


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()