from model.contact import ContactInfo


def test_edit_first_contact(app):
    if app.contact.amount() == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                        mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))
    contacts_before = app.contact.get_contact_list()
    contact = ContactInfo(firstname="KirillEdit", middlename="Edit", lastname="SukhomlinEdit", nickname="kisuroEdit",
                          title="mrEdit", company="Deutsche Telekom", address="Piter", home="7000111",
                          mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                          email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                          bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                          address2="AddressSecondary", phone2="7555555", notes="DrinkMeEdit")
    contact.id = contacts_before[0].id
    app.contact.edit_first_contact(contact)
    assert len(contacts_before) == app.contact.amount()
    contacts_after = app.contact.get_contact_list()
    contacts_before[0] = contact
    assert sorted(contacts_before, key=ContactInfo.id_or_max) == sorted(contacts_after, key=ContactInfo.id_or_max)

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
