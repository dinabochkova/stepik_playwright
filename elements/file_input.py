from playwright.sync_api import Page, expect
from elements.base_element import BaseElement
import allure

class FileInput(BaseElement):

    @property
    def type_of(self):
        return 'file input'

    def set_input_files(self, file_path: str, nth: int=0, **kwargs):
        with allure.step(f'Set file {file_path}'):
            locator = self.get_locator(**kwargs)
            locator.set_input_files(file_path)