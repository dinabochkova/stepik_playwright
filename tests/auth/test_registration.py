import pytest
import allure

@pytest.mark.regression
class TestRegistration:
    @allure.title('Registration with valid credentials')
    def test_successful_registration(self, registration_page, dashboard_page):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.registration_form.check_visible(email='user.name@gmail.com', username='username',
                                                          password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()





