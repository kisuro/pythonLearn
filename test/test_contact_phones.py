from model.contact import ContactInfo
import re


def test_phones_on_home_page(app):
    if app.contact.amount() == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                        mobile="7000112", work="7-000113", fax="7000114", email="em1@t.com",
                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_details_page(app):
    if app.contact.amount() == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                        mobile="7000112", work="7-000113", fax="7000114", email="em1@t.com",
                        email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.work, contact.mobile, contact.phone2]))))
