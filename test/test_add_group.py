# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", pwd="secret")
    app.group.create(Group(name="testGroup", header="groupHeader", footer="groupFooter"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", pwd="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
