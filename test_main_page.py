from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(page):
    Main_Page = MainPage(page, MainPage.url)
    Main_Page.open()
    Main_Page.go_to_login_page()


def test_guest_should_see_login_link(page):
    Main_Page = MainPage(page, MainPage.url)
    Main_Page.open()
    Main_Page.should_be_login_link()

