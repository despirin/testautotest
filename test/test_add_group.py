# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
from data.add_group import constant as testdata

# testdata = [
#     Group (name=name, header=header, footer=footer)
#     for name in ["", random_string('name', 10)]
#     for header in ["", random_string('header', 20)]
#     for footer in ["", random_string('footer', 20)]
# ]

@pytest.mark.parametrize ("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list ()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len (new_groups)
    old_groups.append(group)
    assert sorted (old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empt_group(app):
#     app.group.create(Group("", "", ""))