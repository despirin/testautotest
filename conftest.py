import json
import os.path
import pytest
import importlib

from fixture.application import Application


fixture = None
taget = None

@pytest.fixture #(scope = "session")
def app(request):
    global fixture
    global taget
    browser = request.config.getoption("--browser")
    if taget is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
            base_url = target['baseUrl']
            username = target['username']
            password = target['password']
    #base_url = request.config.getoption("--baseUrl")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)

    fixture.session.ensure_login(username, password)
    return fixture

@pytest.fixture (scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()


    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/index.php")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests (metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata