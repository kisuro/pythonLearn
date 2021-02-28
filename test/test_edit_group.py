from model.group import Group


def test_edit_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    groups_before = app.group.get_group_list()
    app.group.edit_first_group(Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit"))
    groups_after = app.group.get_group_list()
    assert len(groups_before) == len(groups_after)


def test_edit_first_group_name(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    groups_before = app.group.get_group_list()
    app.group.edit_first_group(Group(name="testGroupEditOnlyName"))
    groups_after = app.group.get_group_list()
    assert len(groups_before) == len(groups_after)
