# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    groups_before = app.group.get_group_list()
    group = Group(name="testGroup", header="groupHeader", footer="groupFooter")
    app.group.create(group)
    groups_after = app.group.get_group_list()
    # first check: by amount element in list of groups
    assert len(groups_before) + 1 == len(groups_after)
    # second check: by content
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


def test_add_empty_group(app):
    groups_before = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    groups_after = app.group.get_group_list()
    assert len(groups_before) + 1 == len(groups_after)
    # second check: by content
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
