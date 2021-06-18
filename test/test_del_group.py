# -*- coding: utf-8 -*-

from model.group import Group

def test_del_first_group(app):
    if app.group.count () == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.test_del_first_group()
# получить новый список групп
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len (new_groups)