import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from components.authentication.login_form_component import LoginFormComponent


@pytest.mark.parametrize('email, password',
    [
        ('user.name@gmail.com', 'password'),
        ('user.name@gmail.com', '  '),
        ('  ', 'password')
    ]
)
def test_wrong_email_or_password_authorization(login_page, email, password):

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.login_form.fill(email, password)
        login_page.login_form.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_error_alert()