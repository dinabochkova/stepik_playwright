from playwright.sync_api import Page, expect, BrowserContext, Browser


def test_valid_registration(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()
    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('user.name@gmail.com')
    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')
    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')
    expect(registration_button).to_be_enabled()
    registration_button.click()

    expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_be_visible()
    expect(page.get_by_test_id('dashboard-toolbar-title-text')).to_have_text('Dashboard')

    context.storage_state(path='browser_state.json')

def test_course_page(browser: Browser):

    context = browser.new_context(storage_state='browser_state.json')
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header).to_be_visible()
    expect(header).to_have_text('Courses')
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()
    result_list = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_list).to_have_text('There is no results')
    description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description).to_have_text('Results from the load test pipeline will be displayed here')

