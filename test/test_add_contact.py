# -*- coding: utf-8 -*-
from model.contact import ContactInfo


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    contacts_before = db.get_contact_list()
    app.contact.create(contact)
    contacts_after = db.get_contact_list()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=ContactInfo.id_or_max) == sorted(contacts_after, key=ContactInfo.id_or_max)
    if check_ui:
        assert sorted(contacts_after, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                           key=ContactInfo.id_or_max)
