from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
from elements.input import Input
import allure

class CreateExerciseComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)
        self.delete_exercise_button = Button(page,
            "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Delete exercise"
        )
        self.subtitle = Text(page,
            "create-course-exercise-{index}-box-toolbar-subtitle-text", 'Exercise subtitle'
        )
        self.title_input = Input(page,
            "create-course-exercise-form-title-{index}-input", 'Title'
        )
        self.description_input = Input(page,
            "create-course-exercise-form-description-{index}-input", 'Description'
        )

# не добавляем название шага т.к. уже вызывается .click из base_element
    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)

    @allure.step('Check visible create exercise form')
    def check_visible(self, index: int, title: str, description: str):

        self.subtitle.check_visible()
        self.subtitle.check_have_text(f"#{index + 1} Exercise")

        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.description_input.check_visible()
        self.description_input.check_have_value(description)

    @allure.step('Fill exercise form "{index}"')
    def fill_create_exercise_form(self, index: int, title: str, description: str):

        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title)

        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description)

