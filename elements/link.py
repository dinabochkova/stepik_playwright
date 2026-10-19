from playwright.sync_api import Page, expect, Locator
from elements.base_element import BaseElement

class Link(BaseElement):

    @property
    def type_of(self):
        return 'link'

    pass