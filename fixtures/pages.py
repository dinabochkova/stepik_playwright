import pytest
from pages.dashboard.dashboard_page import DashboardPage
from pages.auth.registration_page import RegistrationPage
from pages.courses.courses_page import CoursePage
from pages.courses.createCourse_page import CreateCoursePage
from pages.auth.login_page import LoginPage

@pytest.fixture
def registration_page(chromium_page):
    return RegistrationPage(chromium_page)

@pytest.fixture
def login_page(chromium_page):
    return LoginPage(chromium_page)

@pytest.fixture
def dashboard_page(chromium_page):
    return DashboardPage(chromium_page)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state):
    return DashboardPage(chromium_page_with_state)


@pytest.fixture
def courses_page(chromium_page_with_state):
    return CoursePage(chromium_page_with_state)

@pytest.fixture
def createCourse_page(chromium_page_with_state):
    return CreateCoursePage(chromium_page_with_state)
