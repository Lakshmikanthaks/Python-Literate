class IntSet(object):
    """An IntSet is a set of integers"""
    # Information about the implementation

    def __init__(self):
        """Create the empty set of integers"""
        self.vals= []

    def insert(self, e):
        """Assumes e as an integer and inserts into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer  Returns true if e is in self"""
        return e in self.vals

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' 

    
