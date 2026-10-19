from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
from elements.textarea import TextArea
import allure

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.title_input = Input(page,'create-course-form-title-input', 'Title')
        self.estimated_time_input = Input(page,'create-course-form-estimated-time-input', 'Time')
        self.description_textarea =TextArea(page,'create-course-form-description-input', 'Desc')
        self.max_score_input = Input(page,'create-course-form-max-score-input', 'Max Score')
        self.min_score_input = Input(page,'create-course-form-min-score-input', 'Min Score')

    @allure.step('Fill create course form')
    def fill(self,title: str,estimated_time: str,description: str,max_score: str,min_score: str):
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    @allure.step('Create visible course form with param')
    def check_visible(self,title, estimated_time, description, max_score, min_score):
        self.title_input.check_have_value(title)
        self.estimated_time_input.check_have_value(estimated_time)
        self.description_textarea.check_have_value(description)
        self.max_score_input.check_have_value(max_score)
        self.min_score_input.check_have_value(min_score)
