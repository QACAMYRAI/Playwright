from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(page, link):
     Product_Page = ProductPage(page,link)
     Product_Page.open()
     Product_Page.add_product_to_bucket()
     Product_Page.book_in_benefit()

def test_guest_should_see_login_link(page):
     Product_Page = ProductPage(page,  ProductPage.url)
     Product_Page.open()
     Product_Page.should_be_bucket_link()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(page):
     Product_Page= ProductPage(page,  ProductPage.url)
     Product_Page.open()
     Product_Page.add_product_to_bucket()
     Product_Page.book_was_added_tab()

def test_guest_cant_see_success_message(page):
    Product_Page = ProductPage(page, ProductPage.url)
    Product_Page.open()
    Product_Page.book_was_added_tab()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(page):
    Product_Page = ProductPage(page, ProductPage.url)
    Product_Page.open()
    Product_Page.add_product_to_bucket()
    Product_Page.book_tab_disappeared()