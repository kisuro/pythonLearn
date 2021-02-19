from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="testGroupEditOnlyName"))
