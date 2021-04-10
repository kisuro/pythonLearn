from random import randrange
import random

import pytest

from model.group import Group


# def test_delete_group_by_index(app):
#     if app.group.amount() == 0:
#         app.group.create(
#             Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
#     groups_before = app.group.get_group_list()
#     index = randrange(len(groups_before))
#     app.group.delete_group_by_index(index)
#     assert len(groups_before) - 1 == app.group.amount()
#     groups_after = app.group.get_group_list()
#     # remove from list of groups only first element (in test was deleted first group)
#     groups_before[index:index+1] = []
#     # check that list of groups after equal(redefined in Group object class) groups before without first group
#     assert groups_before == groups_after

# тест переделан для работы с БД, а также удаление не по индексу а по id
def test_delete_group_by_id(app, db, check_ui):
    with pytest.allure.step('Precondition: check that at least 1 contact exist or create'):
        if len(db.get_group_list()) == 0:
            app.group.create(
                Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    with pytest.allure.step('Given a group list from DB'):
        groups_before = db.get_group_list()
    # определяем случайную группу
    group = random.choice(groups_before)
    # удаляем группу по id
    with pytest.allure.step('When remove group %s by ID' % group):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the group %s was deleted' % group):
        assert len(groups_before) - 1 == app.group.amount()
        groups_after = db.get_group_list()
        # из списка убдет удален элемент который равен заданному, поскольку сравнение по идентификатору (уникальны)
        groups_before.remove(group)
        # check that list of groups after equal(redefined in Group object class) groups before without first group
        assert groups_before == groups_after
    if check_ui:
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
