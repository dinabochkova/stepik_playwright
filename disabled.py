from playwright.sync_api import Page, expect

def test_login_disabled(page: Page):
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()