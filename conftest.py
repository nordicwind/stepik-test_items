import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    languages_list = ['es', 'fr']
    if user_language in languages_list:
        print("\nStart browser for testing languages selection...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be set and should be <es> or <fr>")
    yield browser
    print("\nClosing browser...")
    browser.quit()
