# -*- coding: utf-8 -*-
from model.contact import ContactInfo
import pytest
from data.contacts import contact_testdata


@pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
def test_add_contact(app, contact):
    contacts_before = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(contacts_before) + 1 == app.contact.amount()
    contacts_after = app.contact.get_contact_list()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=ContactInfo.id_or_max) == sorted(contacts_after, key=ContactInfo.id_or_max)
