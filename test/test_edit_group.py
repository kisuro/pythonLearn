from model.group import Group


def test_edit_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    app.group.edit_first_group(Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit"))


def test_edit_first_group_name(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    app.group.edit_first_group(Group(name="testGroupEditOnlyName"))
