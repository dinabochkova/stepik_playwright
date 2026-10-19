import pytest
import time
import allure

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    @allure.title('Check displaying of empty course list')
    def test_empty_courses_list(self, courses_page):
        courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_page.navbar.check_visible_navbar('dina')
        courses_page.sidebar.check_visible()

        courses_page.toolbar_view.check_visible()
        courses_page.check_empty_view()

    @allure.title('Creation of the course')
    def test_create_course(self, courses_page, createCourse_page):
        createCourse_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        createCourse_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        createCourse_page.image_upload_widget.check_visible(is_image_uploaded=False)

        createCourse_page.create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0',
        )
        createCourse_page.create_course_exercises_toolbar.check_visible()
        createCourse_page.check_visible_exercises_empty_view()
        createCourse_page.image_upload_widget.upload_image('./testdata/files/image.png')
        createCourse_page.image_upload_widget.check_visible(True)
        createCourse_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        createCourse_page.create_course_toolbar.click_create_course_button()
        courses_page.toolbar_view.check_visible()
        courses_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    @allure.title('Edit the course')
    def test_edit_course(self,createCourse_page,courses_page):
        createCourse_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        createCourse_page.image_upload_widget.upload_image('./testdata/files/image.png' )
        createCourse_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        createCourse_page.create_course_toolbar.click_create_course_button()
        courses_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_page.course_view.menu.click_edit(index=0)
        time.sleep(5)
        createCourse_page.create_course_form.fill(
            title="Playwright-new",
            estimated_time="5 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        time.sleep(5)
        createCourse_page.create_course_toolbar.click_create_course_button()
        courses_page.course_view.check_visible(
            index=0,
            title="Playwright-new",
            max_score="100",
            min_score="10",
            estimated_time="5 weeks"
        )