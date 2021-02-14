from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", pwd="secret")
    app.group.edit_first_group(Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit"))
    app.session.logout()
