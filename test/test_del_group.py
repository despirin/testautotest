# -*- coding: utf-8 -*-
import random

from model.group import Group

def test_del_first_group(app, db):
    if app.group.count () == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_group_by_id(group.id)
#    app.group.del_group_by_index(old_groups)
#    app.group.del_first_group()
# получить новый список групп
    old_groups.remove(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len (new_groups)