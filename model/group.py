# object for groups
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # redefine representation of results in console - because by default we see just memory address, not value
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # redefine equal function - because python by default сompare by physic place in memory (not real value)
    # also added workaround for 'None' id: self.id is None or other.id is None
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # prepare workaround for 'None' id: if id=None assign big value - that moved to end of list when will be sorted
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
