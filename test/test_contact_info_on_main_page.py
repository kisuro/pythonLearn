import pytest

from model.contact import ContactInfo
from random import randrange
import re


def test_contact_info_on_main_page(app):
    with pytest.allure.step('Precondition: check that at least 1 contact exist or create'):
        if app.contact.amount() == 0:
            app.contact.create(
                ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                            title="mr", company="Deutsche Telekom", address="Piter", home="700-01-11",
                            mobile="", work="7(00)0113", fax="7000114", email="em1@t.com",
                            email2="", email3="em3@t.com", homepage="www.spb.com", bday="26",
                            bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                            address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))
    random_index = randrange(app.contact.amount())
    with pytest.allure.step('When I get a contact from the home page'):
        contact_from_home_page = app.contact.get_contact_list()[random_index]
    with pytest.allure.step('When I get a contact from the edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    with pytest.allure.step('Then the contact info is equal on home and edit page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_info_on_main_page_db(app, ormdb):
    # ЗАДАНИЕ: нужно реализовать сравнение для всех записей, а не для одной случайно выбранной. А сравнивать -- с
    # информацией, загруженной из базы данных.
    with pytest.allure.step('Precondition: check that at least 1 contact exist or create'):
        if len(ormdb.get_contact_list()) == 0:
            app.contact.create(
                ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                            title="mr", company="Deutsche Telekom", address="Piter", home="700-01-11",
                            mobile="", work="7(00)0113", fax="7000114", email="em1@t.com",
                            email2="", email3="em3@t.com", homepage="www.spb.com", bday="26",
                            bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                            address2="AddressSecondary", phone2="7(5)55555", notes="DrinkMe"))

    # взять все контакты с главной страницы
    with pytest.allure.step('When I get a all contacts from the home page'):
        sorted_contacts_ui = sorted(app.contact.get_contact_list(), key=ContactInfo.id_or_max)
    # взять все записи конатктов из бд
    with pytest.allure.step('When I get all contacts db'):
        sorted_contacts_db = sorted(ormdb.get_contact_list(), key=ContactInfo.id_or_max)
    # сравниваем размерность списков
    with pytest.allure.step('Then the contacts lists size are equal'):
        assert len(sorted_contacts_ui) == len(sorted_contacts_db)
    # сравниваем детали списков
    with pytest.allure.step('Then the contacts info is equal on home page and db'):
        for i in range(len(sorted_contacts_db)):
            assert sorted_contacts_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(sorted_contacts_db[i])
            assert sorted_contacts_ui[i].all_emails_from_home_page == merge_emails_like_on_home_page(sorted_contacts_db[i])
            assert sorted_contacts_ui[i].firstname == sorted_contacts_db[i].firstname
            assert sorted_contacts_ui[i].lastname == sorted_contacts_db[i].lastname
            assert sorted_contacts_ui[i].address == sorted_contacts_db[i].address


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
