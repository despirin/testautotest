# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group("test2GR", "testdfgdfg", "ertret"))


def test_add_empt_group(app):
    app.group.create(Group("", "", ""))