import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from pages.courses_page import CoursePage
from pages.createCourse_page import CreateCoursePage
from pages.login_page import LoginPage

@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state):
    return DashboardPage(chromium_page_with_state)


@pytest.fixture
def courses_page(chromium_page_with_state):
    return CoursePage(chromium_page_with_state)

@pytest.fixture
def createCourse_page(chromium_page_with_state):
    return CreateCoursePage(chromium_page_with_state)
