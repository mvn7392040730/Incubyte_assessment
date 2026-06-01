import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, HEADLESS

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def browser():
    # Start Playwright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()
    yield page
    context.close()
