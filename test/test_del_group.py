from model.group import Group


def test_delete_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    groups_before = app.group.get_group_list()
    app.group.delete_first_group()
    groups_after = app.group.get_group_list()
    assert len(groups_before) - 1 == len(groups_after)
