import random
from model.contact import ContactInfo


def test_edit_contact_by_index(app, db, check_ui):
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
    contact_edit = ContactInfo(firstname="KirillEdit", middlename="Edit", lastname="SukhomlinEdit", nickname="kisuroEdit",
                          title="mrEdit", company="Deutsche Telekom", address="Piter", home="7000111",
                          mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                          email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                          bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                          address2="AddressSecondary", phone2="7555555", notes="DrinkMeEdit")
    idsave = contact.id
    app.contact.edit_contact_by_id(idsave, contact_edit)
    contacts_after = db.get_contact_list()
    assert len(contacts_before) == len(contacts_after)
    assert contact_edit == app.contact.get_contact_by_id_from_clist(contacts_after, idsave)
    if check_ui:
        assert sorted(contacts_after, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                           key=ContactInfo.id_or_max)

# def test_edit_first_contact_middlename(app):
#    if app.contact.amount() == 0:
#        app.contact.create(
#            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
#                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
#                        mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
#                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
#                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
#                        address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))
#    app.contact.edit_first_contact(
#        ContactInfo(middlename="UpdateMiddleOnly"))
