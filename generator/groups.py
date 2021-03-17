import jsonpickle
import os.path
from model.group import Group
import random
import string
import re
import getopt
import sys


# block for read options in command line (parameters)
# n - amount of generated testdata
# f- filename where we put generated testdata
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values of parameters
n = 5
f = "data/groups.json"

# if parameters n/f specified
for o, a in opts:
    # get parameter (-n) value for amount and convert to int
    if o == "-n":
        n = int(a)
    # get parameter value filename (-f) as string without converting
    elif o == "-f":
        f = a


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
    for i in range(n)
]

# define path to file where we save testdata generated before  and join .. to jump up and filename
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# open this file
with open(file, "w") as out:
    # json lib: save to file. default added for reformat groups to dictonary (then json can reformat successfully our
    # group testData). indent=2 - reformat json file for best read format out.write(json.dumps(group_testdata,
    # default=lambda x: x.__dict__, indent=2))

    # jsonpickle lib:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(group_testdata))
