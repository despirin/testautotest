# -*- coding: utf-8 -*-
from application import Application
import pytest
from group import Group

@pytest.fixture()
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group("test2GR", "testdfgdfg", "ertret"))
    app.logout()


def test_add_empt_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()