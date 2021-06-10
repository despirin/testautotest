# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group("test2GR", "testdfgdfg", "ertret"))
    app.session.logout()


def test_add_empt_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()