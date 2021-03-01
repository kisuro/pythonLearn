from random import randrange

from model.contact import ContactInfo


def test_del_contact_by_index(app):
    if app.contact.amount() == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                        mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))

    contacts_before = app.contact.get_contact_list()
    index = randrange(len(contacts_before))
    app.contact.delete_contact_by_index(index)
    assert len(contacts_before) - 1 == app.contact.amount()
    contacts_after = app.contact.get_contact_list()
    contacts_before[index:index+1] = []
    assert contacts_before == contacts_after
