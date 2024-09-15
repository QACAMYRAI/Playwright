from playwright.sync_api import expect
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    url = MainPageLocators.MAIN_PAGE_URL

    def go_to_login_page(self):
        expect(self.page.locator(MainPageLocators.LOGIN_LINK)).to_be_visible()
        self.page.locator(MainPageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        login_link = self.page.locator(MainPageLocators.LOGIN_LINK)
        try:
            expect(login_link).to_be_visible()
        except Exception as e:
            raise AssertionError("Page hasn't login link")
