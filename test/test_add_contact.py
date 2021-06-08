# -*- coding: utf-8 -*-
from contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("firstname", "secondname", "lastname", "nickname", "company", "title"))
    app.logout()
