import random
from model.contact import ContactInfo


def test_del_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                        mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))

    contacts_before = db.get_contact_list()
    contact = random.choice(contacts_before)
    app.contact.delete_contact_by_id(contact.id)
    assert len(contacts_before) - 1 == app.contact.amount()
    contacts_after = db.get_contact_list()
    contacts_before.remove(contact)
    assert contacts_before == contacts_after
    if check_ui:
        assert sorted(contacts_after, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                           key=ContactInfo.id_or_max)
