from playwright.sync_api import Page, expect


def test_js(page: Page):
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle')
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New title'

        """
    )
    expect(page.get_by_test_id('authentication-ui-course-title-text')).to_have_text('New title')
