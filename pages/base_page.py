from playwright.sync_api import Page, expect
from typing import Pattern
import allure

class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f"visit url {url}"):
            self.page.goto(url, wait_until="networkidle")

    def reload(self,page):
        with allure.step("reload url"):
            self.page.reload(page)

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"check current url {expected_url.pattern}"):
            expect(self.page).to_have_url(expected_url)