# -*- coding: utf-8 -*-
import random

from model.group import Group

def test_del_first_group(app, db, check_ui):
    if app.group.count () == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_group_by_id(group.id)
    new_groups = db.get_group_list()
#    app.group.del_group_by_index(old_groups)
#    app.group.del_first_group()
# получить новый список групп
    old_groups.remove(group)
    assert old_groups == new_groups
###
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)