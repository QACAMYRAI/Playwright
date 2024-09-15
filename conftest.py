import pytest
from playwright.sync_api import sync_playwright, Page



@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, slow_mo=1000)
        context = browser.new_context()
        page: Page = context.new_page()
        page.set_viewport_size({'height': 1080, 'width': 1920})
        print('Browser is opened')
        yield page
        context.close()
        browser.close()
        print("Browser is closed")

