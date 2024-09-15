class MainPageLocators():
    LOGIN_LINK = "#registration_link"
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

class BucketPageLocators():
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    BACKET_LINK = "#add_to_basket_form > button"
    BENEFIT_LINK = "#messages > div:nth-child(2) > div > strong"
    BOOK_PRICE = "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color"
    BENEFIT_PRICE = '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong'
    BOOK_NAME_SHOP = "#content_inner > article > div.row > div.col-sm-6.product_main > h1"
    BOOK_NAME_BENEFIT = "#messages > div:nth-child(1) > div > strong "
    BOOK_ADDED = "#messages > div:nth-child(1) > div"
