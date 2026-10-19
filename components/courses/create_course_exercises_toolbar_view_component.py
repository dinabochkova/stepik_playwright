from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.button import Button
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.title = Text(page,'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(page,'create-course-exercises-box-toolbar-create-exercise-button', 'Button')

    @allure.step('Check that exercise toolbar is visible')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

    def click_create_exercise_button(self):
        self.create_exercise_button.click()