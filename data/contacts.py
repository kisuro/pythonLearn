from model.contact import ContactInfo
import random
import string
import re
import jsonpickle
import os.path
import getopt
import sys

# block for read options in command line (parameters)
# n - amount of generated testdata
# f- filename where we put generated testdata
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values of parameters
n = 5
f = "data/contacts.json"

# if parameters n/f specified
for o, a in opts:
    # get parameter (-n) value for amount and convert to int
    if o == "-n":
        n = int(a)
    # get parameter value filename (-f) as string without converting
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.punctuation + " " * 10
    clear_symbols = re.sub(r"[\'\\<]|\s{2}|\s$", "", symbols)
    return prefix + "".join([random.choice(clear_symbols) for i in range(random.randrange(maxlen))])


contact_testdata = [ContactInfo(firstname=random_string("fname", 10), middlename=random_string("mname", 3),
                                lastname=random_string("lname", 15))
                    for i in range(n)
                    ]

# define path to file where we save testdata generated before  and join .. to jump up and filename
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# open this file and save testdata
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(contact_testdata))
