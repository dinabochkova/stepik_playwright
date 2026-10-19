from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
import re

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')
        self.login_button = Button(page,'registration-page-login-link', 'Login')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile('.*/#/auth/login'))

