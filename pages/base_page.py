from playwright.sync_api import Page, TimeoutError
import math

class BasePage:
    url = 'some url'
    link = "some links"

    def __init__(self, page:Page, link):
        self.page = page
        self.link = link


    def open_parametrize(self):
        self.page.goto(self.link)

    def open(self):
        self.page.goto(self.url)

    def handle_dialog(self, dialog):
        x = dialog.message.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))

        if dialog.type == 'prompt':
            dialog.accept(answer)
        else:
            dialog.accept()

def is_disappeared(page, locator, timeout=4):
        try:
            page.wait_for_selector(locator,state="hidden", timeout=timeout * 1000)
            return True
        except TimeoutError:
            return False




