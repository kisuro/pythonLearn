# -*- coding: utf-8 -*-
import pytest

from model.contact import ContactInfo


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        contacts_before = db.get_contact_list()
    with pytest.allure.step('When I add a contact %s to the list' % contact):
        app.contact.create(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        contacts_after = db.get_contact_list()
        contacts_before.append(contact)
        assert sorted(contacts_before, key=ContactInfo.id_or_max) == sorted(contacts_after, key=ContactInfo.id_or_max)
    if check_ui:
        assert sorted(contacts_after, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                           key=ContactInfo.id_or_max)
