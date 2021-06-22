from pytest_bdd import given, when, then
from model.group import Group
import pytest

@pytest.fixture
@given('a group with <name> <header> and <footer>')
def step_group_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@pytest.fixture
@given('a group list')
def step_group_list(app):
    return app.group.get_group_list()

@pytest.fixture
@when('I add a new group to the list')
def step_add_new_group(app, step_group_group):
    app.group.create(step_group_group)

@pytest.fixture
@then('the new group list bi equal to the old list with the added group')
def step_verify_group_added (app, step_group_list, step_group_group):
    old_groups = step_group_list
    new_groups = app.group.get_group_list()
    old_groups.append(step_group_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)