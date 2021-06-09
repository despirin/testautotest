# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.group import Group

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group("test2GR", "testdfgdfg", "ertret"))
    app.session.logout()


def test_add_empt_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()