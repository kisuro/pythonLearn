import pytest

from model.contact import ContactInfo
from model.group import Group
import random


def test_del_contact_from_group(app, ormdb):
    group = None
    # проверить есть ли контакты
    with pytest.allure.step('Precondition: check that at least 1 contact exist or create'):
        if len(ormdb.get_contact_list()) == 0:
            app.contact.create(
                ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                            title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                            mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                            email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                            bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                            address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))
    # проверить есть ли группы
    with pytest.allure.step('Precondition: check that at least 1 group exist or create'):
        if len(ormdb.get_group_list()) == 0:
            app.group.create(
                Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    # берем случайный контакт из бд
    with pytest.allure.step('Given a contact'):
        contact = random.choice(ormdb.get_contact_list())
        # для выбранного контакта проверяем, что есть связь с группой, если нет - добавляем
    with pytest.allure.step('When check that contact in group OR add'):
        list_of_groups_for_contact = ormdb.get_groups_for_contact(contact)
        if (len(list_of_groups_for_contact)) == 0:
            group = random.choice(ormdb.get_group_list())
            app.contact.add_to_group(contact, group)
        else:
            # определяем список групп, в которых находится контакт и выбираем одну случайную
            index = random.randrange(len(list_of_groups_for_contact))
            group = list_of_groups_for_contact[index]
    with pytest.allure.step('When remove contact %s from group %s' % (contact, group)):
        app.contact.remove_from_group(contact, group)
    # проверяем, что после удаления, контакт не входит в группу из которой удалили(бд)
    with pytest.allure.step('Then check that contact %s removed from group %s' % (contact, group)):
        assert group not in ormdb.get_groups_for_contact(contact)


def test_add_contact_to_group(app, ormdb):
    exception_group_list = []
    # проверить есть ли контакты
    with pytest.allure.step('Precondition: check that at least 1 contact exist or create'):
        if len(ormdb.get_contact_list()) == 0:
            app.contact.create(
                ContactInfo(firstname="KirillPrecondition", middlename="", lastname="Sukhomlin", nickname="kisuro",
                            title="mr", company="Deutsche Telekom", address="Piter", home="7000111",
                            mobile="7000112", work="7000113", fax="7000114", email="em1@t.com",
                            email2="em2@t.com", email3="em3@t.com", homepage="www.spb.com", bday="26",
                            bmonth="June", byear="1982", aday="3", amonth="April", ayear="1990",
                            address2="AddressSecondary", phone2="7555555", notes="DrinkMe"))
    # проверить есть ли группы
    with pytest.allure.step('Precondition: check that at least 1 group exist or create'):
        if len(ormdb.get_group_list()) == 0:
            app.group.create(
                Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    # берем случайный контакт из бд
    with pytest.allure.step('Given a contact'):
        contact = random.choice(ormdb.get_contact_list())
    # для выбранного контакта определяем группу в которую он не входит:
    # берем список групп в которые входит контакт
    with pytest.allure.step('When define group for contact'):
        list_of_groups_for_contact = ormdb.get_groups_for_contact(contact)
        # берем список всех групп
        list_of_all_groups = ormdb.get_group_list()
        # составляем список групп в которые контакт не входит
        # (идем по списку всех групп и если встречаем отсутсвующую в list_of_groups_for_contact заносим в новый list)
        for gr in list_of_all_groups:
            if gr not in list_of_groups_for_contact:
                exception_group_list.append(gr)
        # дополнительно проверяем, что контакт, не находится во всех существующих группах
        if len(exception_group_list) == 0:
            # если это так, удаляем его из одной случайной группы
            group = list_of_groups_for_contact[random.randrange(len(list_of_groups_for_contact))]
            app.contact.remove_from_group(contact, group)
        else:
            # из списка групп в которые контакт не входит, выбираем случайную
            index = random.randrange(len(exception_group_list))
            group = list_of_all_groups[index]
    # добавляем контакт в группу
    with pytest.allure.step('When add contact %s to group %s' % (contact, group)):
        app.contact.add_to_group(contact, group)
    # проверяем что после добавления, контакт входит в группу
    with pytest.allure.step('Then check that contact %s added to group %s' % (contact, group)):
        assert group in ormdb.get_groups_for_contact(contact)
