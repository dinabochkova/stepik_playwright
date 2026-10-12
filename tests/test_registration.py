from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent


def test_successful_registration(registration_page, dashboard_page):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_form.check_visible(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar.check_visible()
