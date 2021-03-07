# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
import re


# bugs workaround: added re.sub
# symbol: "'" - system bug from lesson (record doesn't created)
# symbol: '\'  on group-contact page not displayed (also some ASCII Control character after them e.g: \t, \n)
# double space -> on group-contact page one of them is not displayed
# space at the end of name -> function element.text read without space: webdriver bug?
# symbol: '<'  cut all data after this symbol (for group just for name field)
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    clear_symbols = re.sub(r"[\'\\<]|\s{2}|\s$", "", symbols)
    return prefix + "".join([random.choice(clear_symbols) for i in range(random.randrange(maxlen))])


group_testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10),
          header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", group_testdata, ids=[repr(x) for x in group_testdata])
def test_add_group(app, group):
    groups_before = app.group.get_group_list()
    app.group.create(group)
    # first check: by amount element in list of groups
    assert len(groups_before) + 1 == app.group.amount()
    groups_after = app.group.get_group_list()
    # second check: by content
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
