# -*- coding: utf-8 -*-
from model.group import Group
import pytest


# annotation removed and changed to method pytest_generate_tests in confest.py @pytest.mark.parametrize("group",
# group_testdata, ids=[repr(x) for x in group_testdata])
# json_groups- fixture get data from json file and test use it
# like testdata parameter (json_groups - 'groups' its name of json file)
# data_groups- fixture get data from
# data/groups.py file (module) and test use it like testdata parameter
# first test work with UI data, reworked for DB

# def test_add_group(app, json_groups):
#     group = json_groups
#     groups_before = app.group.get_group_list()
#     app.group.create(group)
#     # first check: by amount element in list of groups
#     assert len(groups_before) + 1 == app.group.amount()
#     groups_after = app.group.get_group_list()
#     # second check: by content
#     groups_before.append(group)
#     assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        groups_before = db.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        groups_after = db.get_group_list()
        groups_before.append(group)
        assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
    if check_ui:
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
