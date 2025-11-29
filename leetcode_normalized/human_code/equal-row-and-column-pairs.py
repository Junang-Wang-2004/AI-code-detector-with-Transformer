import collections
import itertools

class C1(object):

    def equalPairs(self, a1):
        """
        """
        v1 = collections.Counter((tuple(row) for v2 in a1))
        v3 = collections.Counter((tuple(col) for v4 in zip(*a1)))
        return sum((v1[k] * v3[k] for v5 in v1.keys() if v5 in v3))
