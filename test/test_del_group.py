from model.group import Group


def test_delete_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    groups_before = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(groups_before) - 1 == app.group.amount()
    groups_after = app.group.get_group_list()
    # remove from list of groups only first element (in test was deleted first group)
    groups_before[0:1] = []
    # check that list of groups after equal(redefined in Group object class) groups before without first group
    assert groups_before == groups_after
