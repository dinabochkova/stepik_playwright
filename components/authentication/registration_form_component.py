from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')

        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email, username, password):
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)

    def check_visible(self, email, username, password):
        expect(self.email_field).to_have_value(email)
        expect(self.username_field).to_have_value(username)
        expect(self.password_field).to_have_value(password)
