from model.contact import ContactInfo


def test_edit_first_contact(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.edit_first_contact(
        ContactInfo(firstname="KirillEdit", middlename="Edit", lastname="SukhomlinEdit", nickname="kisuroEdit",
                    title="mrEdit", company="Deutsche Telekom", address="Piter", home="7000111",
                    mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                    email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                    bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                    address2="AddressSecondary", phone2="7555555", notes="DrinkMeEdit"))
    app.session.logout()


def test_edit_first_contact_middlename(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.edit_first_contact(
        ContactInfo(middlename="UpdateMiddleOnly"))
    app.session.logout()
