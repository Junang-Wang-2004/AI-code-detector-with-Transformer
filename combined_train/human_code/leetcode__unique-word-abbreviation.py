import collections

class C1(object):

    def __init__(self, a1):
        """
        initialize your data structure here.
        """
        self.lookup_ = collections.defaultdict(set)
        for v1 in a1:
            v2 = self.abbreviation(v1)
            self.lookup_[v2].add(v1)

    def isUnique(self, a1):
        """
        check if a word is unique.
        """
        v1 = self.abbreviation(a1)
        return self.lookup_[v1] <= {a1}

    def abbreviation(self, a1):
        if len(a1) <= 2:
            return a1
        return a1[0] + str(len(a1) - 2) + a1[-1]
