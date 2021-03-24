from model.contact import ContactInfo
from random import randrange
import re


def test_contact_info_on_main_page(app):
    if app.contact.amount() == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="700-01-11",
                        mobile="", work="7(00)0113", fax="7000114", email="em1@t.com",
                        email2="", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))
    random_index = randrange(app.contact.amount())
    contact_from_home_page = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_info_on_main_page_db(app, ormdb):
    # ЗАДАНИЕ: нужно реализовать сравнение для всех записей, а не для одной случайно выбранной. А сравнивать -- с
    # информацией, загруженной из базы данных.
    if len(ormdb.get_contact_list()) == 0:
        app.contact.create(
            ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                        title="mr", company="Deutsche Telekom", address="Piter", home="700-01-11",
                        mobile="", work="7(00)0113", fax="7000114", email="em1@t.com",
                        email2="", email3="em3@t.com", homepage="www.spb.com", bday="26",
                        bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                        address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))

    # взять все контакты с главной страницы
    contacts_ui = app.contact.get_contact_list()
    # взять все записи конатктов из бд
    contacts_db = ormdb.get_contact_list()
    # сравниваем списки, сортируя
    assert sorted(contacts_ui, key=ContactInfo.id_or_max) == sorted(contacts_db, key=ContactInfo.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
