
def test_del_first_contact(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.delete_first_contact()
    app.session.logout()
