import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=False)
def app(request):
    global fixture
    options = Options()
    user_language = request.config.getoption('--language')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    fixture = webdriver.Chrome(options=options)

    fixture.implicitly_wait(10)

    def fin():
        if fixture is not None:
            fixture.quit()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')
