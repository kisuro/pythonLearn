# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


# workaround: added replace - BUG in testsystem for all fields
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace("'", "")


# workaround: added replace - BUG in testsystem for name field
    # double space -> on group page one of them is not displayed
    # space at the end of name -> function element.text read without space: selenium bug?
    # symbol: '\'  on group page not displayed and cut symbol after them
    # symbol: '<'  cut all data after this symbol

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10).replace(" ", "").replace("<", "").replace("\\", ""),
          header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    groups_before = app.group.get_group_list()
    app.group.create(group)
    # first check: by amount element in list of groups
    assert len(groups_before) + 1 == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
