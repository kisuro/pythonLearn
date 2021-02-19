from model.group import Group


def test_delete_first_group(app):
    if app.group.amount() == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    app.group.delete_first_group()
