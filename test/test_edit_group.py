from model.group import Group


def test_edit_first_group(app):
    # precondition: create group if we have no groups
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    # save list of Groups before modify
    groups_before = app.group.get_group_list()
    group = Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit")
    # for modified group (first in our case) also save id because it's doesn't changed after modify
    group.id = groups_before[0].id
    app.group.edit_first_group(group)
    assert len(groups_before) == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    # replace first group , using new group data
    groups_before[0] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)

# def test_edit_first_group_name(app):
#    if app.group.amount() == 0:
#        app.group.create(
#            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
#    groups_before = app.group.get_group_list()
#    app.group.edit_first_group(Group(name="testGroupEditOnlyName"))
#    groups_after = app.group.get_group_list()
#    assert len(groups_before) == len(groups_after)
