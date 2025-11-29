import itertools
from functools import reduce

class C1(object):

    def minDominoRotations(self, a1, a2):
        """
        """
        v1 = reduce(set.__and__, [set(d) for v2 in zip(a1, a2)])
        if not v1:
            return -1
        v3 = v1.pop()
        return min(len(a1) - a1.count(v3), len(a2) - a2.count(v3))
