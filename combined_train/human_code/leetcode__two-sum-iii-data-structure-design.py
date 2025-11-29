from collections import defaultdict

class C1(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.lookup = defaultdict(int)

    def add(self, a1):
        """
        Add the number to an internal data structure.
        """
        self.lookup[a1] += 1

    def find(self, a1):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for v1 in self.lookup:
            v2 = a1 - v1
            if v2 in self.lookup and (v2 != v1 or self.lookup[v1] > 1):
                return True
        return False
