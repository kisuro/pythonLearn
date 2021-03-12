import json
import os.path
import pytest
from fixture.application import Application

# define default value for variables
fixture = None
target = None


@pytest.fixture
def app(request):
    # define variables as global
    global fixture
    global target
    # get browser data as option (defined in run configuration "additional parameters", eg:--browser=chrome.
    # default=firefox)
    browser = request.config.getoption("--browser")
    # check if data from target.json not loaded - load it
    if target is None:
        # find path to file and join with filename (from option "target")
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        # open file only while load, then autoClose
        with open(config_file) as f:
            target = json.load(f)
    # check if fixture not loaded - load it
    if fixture is None or not fixture.is_valid():
        # load base url from target.json
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    # load user/password from target.json
    fixture.session.ensure_login(username=target['user'], pwd=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
