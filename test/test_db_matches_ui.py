from model.group import Group


# передаем две фикстуры, app - чтобы получить доступ к UI методу fixture/group.py -get_group_list и db фикстуру
# fixture/db.py - get_group_list
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    # сравниваем остортировав по id (самописный метод)
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
