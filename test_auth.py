from playwright.sync_api import Page, expect
import time
import pytest

def test_valid_registration(page: Page):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('user.name@gmail.com')
    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')
    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_be_visible()
    expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_have_text('Dashboard')

