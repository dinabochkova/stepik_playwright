import pytest
import allure
from tools.allure.parent_suite import AllureEpic # Импортируем enum AllureEpic
from tools.allure.suite import AllureFeature # Импортируем enum AllureFeature
from tools.allure.sub_suite import AllureStory # Импортируем enum AllureStory
from allure_commons.types import Severity


@allure.parent_suite(AllureEpic.LMS) # Добавили epic
@allure.suite(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.sub_suite(AllureStory.AUTHORIZATION) # Добавили story
@pytest.mark.regression
class TestAuth:
    @allure.severity(Severity.CRITICAL)
    @allure.title('User login with correct credentials')
    def test_successful_auth(self, registration_page,dashboard_page, login_page):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com',username='dina', password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible_navbar('dina')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_on_logout()

        login_page.login_form.fill(email='user.name@gmail.com', password='password')
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible_navbar('dina')
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize('email, password',
                             [
                                 ('user.name@gmail.com', 'password'),
                                 ('user.name@gmail.com', '  '),
                                 ('  ', 'password')
                             ]
                             )

    @allure.severity(Severity.CRITICAL)
    @allure.title('User login with invalid credentials')
    def test_wrong_email_or_password_authorization(self, login_page, email, password):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.login_form.fill(email, password)
        login_page.login_form.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_error_alert()

    @allure.title('Navigation from auth to reg')
    def test_navigate_from_auth_to_reg(self, login_page, registration_page):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email='', username='', password='')


