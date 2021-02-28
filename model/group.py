# object for groups

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
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
