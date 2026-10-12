from pages.courses_page import CoursePage
from pages.createCourse_page import CreateCoursePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent

import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_page):
    courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_page.navbar.check_visible_navbar('username')
    courses_page.sidebar.check_visible()

    courses_page.toolbar_view.check_visible()
    courses_page.check_empty_view()

def test_create_course(courses_page,createCourse_page):
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

