from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from components.authentication.registration_form_component import RegistrationFormComponent



def test_successful_registration(registration_page, dashboard_page):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_form.check_visible(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
