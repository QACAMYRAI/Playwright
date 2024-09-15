from .base_page import BasePage, is_disappeared
from playwright.sync_api import expect, Dialog
from .locators import BucketPageLocators


class ProductPage(BasePage):
    url = BucketPageLocators.PRODUCT_PAGE_URL


    def add_product_to_bucket(self):
        self.page.on("dialog", self.handle_dialog)
        bucket_link = self.page.locator('css='+BucketPageLocators.BACKET_LINK)
        bucket_link.click()

    def should_be_bucket_link(self):
        expect(self.page.locator('css='+BucketPageLocators.BACKET_LINK)).to_be_visible(), "Bucket link is not presented"


    def book_in_benefit(self):
        assert (self.page.text_content('css=' + BucketPageLocators.BENEFIT_PRICE))[:-1] >= (self.page.text_content('css='+BucketPageLocators.BOOK_PRICE))[:-1], "Wrong benefit price"
        expect(self.page.locator(BucketPageLocators.BACKET_LINK)).to_be_visible(), "Bucket benefit is not presented"
        assert (self.page.text_content('css=' + BucketPageLocators.BOOK_NAME_SHOP)) == (self.page.text_content('css=' + BucketPageLocators.BOOK_NAME_BENEFIT))

    def book_was_added_tab(self):
         expect(self.page.locator(BucketPageLocators.BOOK_ADDED)).not_to_be_visible(), "Guest doesn't see add's tab"

    def book_tab_disappeared(self):
        if is_disappeared(self.page, BucketPageLocators.BOOK_ADDED):
            print("Add's tab doesn't disappeared")
        else:
            print("Add's tab disappears")


