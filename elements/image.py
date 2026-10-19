from playwright.sync_api import Page, expect, Locator
from elements.base_element import BaseElement

class Image(BaseElement):
    @property
    def type_of(self):
        return 'image'

    pass
