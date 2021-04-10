import pytest

from model.group import Group


# передаем две фикстуры, app - чтобы получить доступ к UI методу fixture/group.py -get_group_list и db фикстуру
# fixture/db.py - get_group_list
def test_group_list(app, db):
    with pytest.allure.step('Given a group list from UI'):
        ui_list = app.group.get_group_list()
    with pytest.allure.step('Given a group list from DB'):
        db_list = db.get_group_list()
    # сравниваем остортировав по id (самописный метод)
    with pytest.allure.step('Then check db/ui groups is equals'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
