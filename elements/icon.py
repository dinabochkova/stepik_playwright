from playwright.sync_api import Page, expect, Locator
from elements.base_element import BaseElement

class Icon(BaseElement):

    @property
    def type_of(self):
        return 'icon'


    pass