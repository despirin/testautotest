import random

from pytest_bdd import given, when, then
from model.group import Group
import pytest

step1 = None
step2 = None
step3 = None


@pytest.fixture
@given('a group with <name> <header> and <footer>')
def step_group_group(app):
    global step2
    step2 = app.group.get_group_list()
    st1 = step1
    st2 = step2
    st3 = step3
    return Group(name = "name2", header = "header2", footer = 'footer2')
    #return Group(name=name, header=header, footer=footer)

@pytest.fixture
@given('a group list')
def step_group_list(app):
    global step1
    step1 = app.group.get_group_list()
    st1 = step1
    st2 = step2
    st3 = step3

    if app.group.group_cache is None:
        return app.group.get_group_list()
    else:
        return app.group.group_cache
    #return step1

@when('I add a new group to the list')
def step_add_new_group(app, step_group_group):
    #pass
    global step3
    step3 = app.group.get_group_list()
    st1 = step1
    st2 = step2
    st3 = step3
    app.group.create(step_group_group)


@then('the new group list bi equal to the old list with the added group')
def step_verify_group_added(app, step_group_group, step_group_list):
    st1 = step1
    old_groups = step_group_list
    st2 = step2
    st3 = step3
    new_groups = app.group.get_group_list()
    # неработает нихрена
    assert len(old_groups) - 1 == len(new_groups)

##############################delgroup############

@pytest.fixture
@given('a non-empty group list')
def non_empty_group_list(app):
    if len (app.group.get_group_list()) ==0:
        app.group.create(Group(name="some name"))
    return app.group.get_group_list()

@pytest.fixture
@given ('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when ('I delete the group fom the list')
def delete_group(app, random_group):
    index=int(random_group.id)
    app.group.del_group_by_index (index)

@then ('the new group is equal to the old list without the delete group')
def verify_group_deleted(app, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)