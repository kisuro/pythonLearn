# -*- coding: utf-8 -*-
from model.contact import ContactInfo
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.punctuation + " " * 10
    clear_symbols = re.sub(r"[\'\\<]|\s{2}|\s$", "", symbols)
    return prefix + "".join([random.choice(clear_symbols) for i in range(random.randrange(maxlen))])


contact_testdata = [ContactInfo(firstname=random_string("fname", 10), middlename=random_string("mname", 3),
                                lastname=random_string("lname", 15))
                    for i in range(3)
                    ]


@pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
def test_add_contact(app, contact):
    contacts_before = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(contacts_before) + 1 == app.contact.amount()
    contacts_after = app.contact.get_contact_list()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=ContactInfo.id_or_max) == sorted(contacts_after, key=ContactInfo.id_or_max)
