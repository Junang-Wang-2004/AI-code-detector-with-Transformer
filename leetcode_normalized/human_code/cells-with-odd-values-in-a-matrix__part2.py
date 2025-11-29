import collections
import itertools

class C1(object):

    def oddCells(self, a1, a2, a3):
        """
        """
        v1 = lambda x: sum((count & 1 for v2 in collections.Counter(x).values()))
        v3, v4 = list(map(v1, zip(*a3)))
        return v3 * a2 + v4 * a1 - 2 * v3 * v4
