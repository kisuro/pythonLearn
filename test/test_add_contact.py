# -*- coding: utf-8 -*-
import pytest
from model.contact import ContactInfo
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", pwd="secret")
    app.create_contact(ContactInfo(firstname="Kirill", middlename="", lastname="Sukhomlin", nickname="kisuro",
                                   title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                                   mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                                   email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                                   bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                                   address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))
    app.session.logout()
