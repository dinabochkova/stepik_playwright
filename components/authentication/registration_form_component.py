from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = Input(page,'registration-form-email-input', 'Email')
        self.username_field = Input(page,'registration-form-username-input', 'Username')
        self.password_field = Input(page,'registration-form-password-input', 'Password')

    @allure.step('Fill registration form')
    def fill(self, email, username, password):
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)

    @allure.step('Check that registration form is visible')
    def check_visible(self, email, username, password):
        self.email_field.check_have_value(email)
        self.username_field.check_have_value(username)
        self.password_field.check_have_value(password)

