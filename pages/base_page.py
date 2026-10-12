from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def reload(self,page):
        self.page.reload(page)