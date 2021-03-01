from random import randrange

from model.group import Group


def test_delete_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    groups_before = app.group.get_group_list()
    index = randrange(len(groups_before))
    app.group.delete_group_by_index(index)
    assert len(groups_before) - 1 == app.group.amount()
    groups_after = app.group.get_group_list()
    # remove from list of groups only first element (in test was deleted first group)
    groups_before[index:index+1] = []
    # check that list of groups after equal(redefined in Group object class) groups before without first group
    assert groups_before == groups_after
