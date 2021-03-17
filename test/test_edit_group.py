from random import randrange
from conftest import random_json_testdata
from model.group import Group


def test_edit_group_by_index(app):
    # precondition: create group if we have no groups
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    # save list of Groups before modify
    groups_before = app.group.get_group_list()
    index = randrange(len(groups_before))
    group = Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit")
    # for modified group (first in our case) also save id because it's doesn't changed after modify
    group.id = groups_before[index].id
    app.group.edit_group_by_index(index, group)
    assert len(groups_before) == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    # replace first group , using new group data
    groups_before[index] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


# my personal try to use data from json (by random index, method: random_json_testdata)
def test_edit_group_by_index_loadtestdata(app):
    newgroup = random_json_testdata("groups")
    editgroup = random_json_testdata("groups")
    # precondition: create group if we have no groups
    if app.group.amount() == 0:
        app.group.create(newgroup)
    # save list of Groups before modify
    groups_before = app.group.get_group_list()
    index = randrange(len(groups_before))
    # for modified group (first in our case) also save id because it's doesn't changed after modify
    editgroup.id = groups_before[index].id
    app.group.edit_group_by_index(index, editgroup)
    assert len(groups_before) == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    # replace first group , using new group data
    groups_before[index] = editgroup
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
