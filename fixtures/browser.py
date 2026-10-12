from typing import Any, Generator

import pytest
from playwright.sync_api import Page, expect, Browser

@pytest.fixture(scope='session')
def initialize_browser_state(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.wait_for_load_state('networkidle')

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('user.name@gmail.com')
    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')
    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    page.wait_for_load_state('networkidle')

    context.storage_state(path='tests/browser_state.json')
    context.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, browser: Browser) -> Generator[Page, Any, None]:
    context = browser.new_context(storage_state='tests/browser_state.json')
    page = context.new_page()
    yield page
    context.close()
