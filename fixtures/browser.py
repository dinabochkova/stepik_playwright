from typing import Any, Generator
import pytest
from playwright.sync_api import Page, Playwright, Browser
from pages.auth.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
import allure
from allure_commons.types import AttachmentType
from config import settings


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright):  # Добавили аргумент request
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(record_video_dir=settings.videos_dir)  # Создаем контекст для новой сессии браузера и запись видео теста
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг
    page = context.new_page() # Открываем новую страницу в контексте
    yield page

    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))  # Сохраняем трейсинг в файл
    settings.tracing_dir.joinpath(f'{request.node.name}.zip')
    browser.close()  # Закрываем браузер

    allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'), name="trace", extension='zip')
    allure.attach.file(page.video.path(), name="video", attachment_type=AttachmentType.WEBM)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=settings.test_user.email,
                                             username=settings.test_user.username,
                                             password=settings.test_user.password)
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state=settings.browser_state_file, record_video_dir='./video')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name="trace", extension='zip')
    allure.attach.file(page.video.path(), name="video", attachment_type=AttachmentType.WEBM)