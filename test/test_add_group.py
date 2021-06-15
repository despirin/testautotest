# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
# сохранить старый список групп
# получение списка групп
    old_groups = app.group.get_group_list ()
    app.group.create(Group("test2GR", "testdfgdfg", "ertret"))
# получить новый список групп
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len (new_groups)


def test_add_empt_group(app):
    app.group.create(Group("", "", ""))