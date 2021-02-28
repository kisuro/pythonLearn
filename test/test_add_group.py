# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    groups_before = app.group.get_group_list()
    app.group.create(Group(name="testGroup", header="groupHeader", footer="groupFooter"))
    groups_after = app.group.get_group_list()
    assert len(groups_before) + 1 == len(groups_after)


def test_add_empty_group(app):
    groups_before = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    groups_after = app.group.get_group_list()
    assert len(groups_before) + 1 == len(groups_after)
