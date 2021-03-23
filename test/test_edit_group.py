import random
from random import randrange
from conftest import random_json_testdata
from model.group import Group


# def test_edit_group_by_index(app):
#     # precondition: create group if we have no groups
#     if app.group.amount() == 0:
#         app.group.create(
#             Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
#     # save list of Groups before modify
#     groups_before = app.group.get_group_list()
#     index = randrange(len(groups_before))
#     group = Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit")
#     # for modified group (first in our case) also save id because it's doesn't changed after modify
#     group.id = groups_before[index].id
#     app.group.edit_group_by_index(index, group)
#     assert len(groups_before) == app.group.amount()
#     groups_after = app.group.get_group_list()
#     # second check: by content
#     # replace first group , using new group data
#     groups_before[index] = group
#     assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


def test_edit_group_by_id(app, db, check_ui):
    # precondition: create group if we have no groups
    if len(db.get_group_list()) == 0:
        app.group.create(
            Group(name="testGroupPrecondition", header="groupHeaderPrecondition", footer="groupFooterPrecondition"))
    # сохраняем исходный лист групп из БД
    groups_before = db.get_group_list()
    # определяем случайную группу
    group = random.choice(groups_before)
    # данные для изменения
    group_edit = Group(name="testGroupEdit", header="groupHeaderEdit", footer="groupFooterEdit")
    # сохраняем id редактируемой группы
    idsave = group.id
    # редактируем группу по id
    app.group.edit_group_by_id(idsave, group_edit)
    groups_after = db.get_group_list()
    # сравниваем количество групп в бд до изменений и актуальное
    assert len(groups_before) == len(groups_after)
    # сравниваем данные группы на которые меняли(group_edit) и текущие данные бд для этой группы, найдя ее по id(idsave)
    # добавлен метод get_group_by_id_from_glist(groups_list, g_id)
    assert group_edit == app.group.get_group_by_id_from_glist(groups_after, idsave)
    # проверяем полное соответсвие групп на ui и в бд (при указании параметра)
    if check_ui:
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#  personal try to use data from json (by random index, method: random_json_testdata)
def test_edit_group_by_index_loadtestdata(app):
    newgroup = random_json_testdata("groups")
    editgroup = random_json_testdata("groups")
    # precondition: create group if we have no groups
    if app.group.amount() == 0:
        app.group.create(newgroup)
    # save list of Groups before modify
    groups_before = app.group.get_group_list()
    index = randrange(len(groups_before))
    # for modified group (first in our case) also save id because it's doesn't changed after modify
    editgroup.id = groups_before[index].id
    app.group.edit_group_by_index(index, editgroup)
    assert len(groups_before) == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    # replace first group , using new group data
    groups_before[index] = editgroup
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
