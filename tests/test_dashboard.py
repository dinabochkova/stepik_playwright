from pages.dashboard_page import DashboardPage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent

def test_dashboard_displaying(dashboard_page_with_state):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.dashboard_toolbar.check_visible()

    dashboard_page_with_state.students_chart_view.check_visible('Students')
    dashboard_page_with_state.activities_chart_view.check_visible('Activities')
    dashboard_page_with_state.scores_chart_view.check_visible('Scores')
    dashboard_page_with_state.courses_chart_view.check_visible('Courses')

    dashboard_page_with_state.navbar.check_visible_navbar('username')
    dashboard_page_with_state.sidebar.check_visible()