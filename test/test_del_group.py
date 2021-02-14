

def test_delete_first_group(app):
    app.session.login(username="admin", pwd="secret")
    app.group.delete_first_group()
    app.session.logout()
