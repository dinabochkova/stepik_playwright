from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.navigation.sidabar_list_item_component import SideBarListItemComponent
import re

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SideBarListItemComponent(page, identifier='logout')
        self.courses_list_item = SideBarListItemComponent(page, identifier='courses')
        self.dashboard_list_item = SideBarListItemComponent(page, identifier='dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    def click_on_logout(self):
        self.logout_list_item.navigate(re.compile(r'.*/#/auth/login'))

    def click_on_courses(self):
        self.courses_list_item.navigate(re.compile(r'.*/#/courses'))

    def click_on_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r'.*/#/dashboard'))
