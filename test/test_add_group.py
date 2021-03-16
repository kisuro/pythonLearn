# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups import constant as group_testdata


@pytest.mark.parametrize("group", group_testdata, ids=[repr(x) for x in group_testdata])
def test_add_group(app, group):
    groups_before = app.group.get_group_list()
    app.group.create(group)
    # first check: by amount element in list of groups
    assert len(groups_before) + 1 == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
