import json
import os.path
import pytest
import importlib

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None

def load_config (file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
#
#             base_url = target['baseUrl']
#             username = target['username']
#             password = target['password']
    return target


@pytest.fixture #(scope = "session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    base_url = web_config['baseUrl']
    username = web_config['username']
    password = web_config['password']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username, password)
    return fixture


@pytest.fixture(scope = "session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


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