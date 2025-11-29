import collections
import itertools
from functools import reduce

class C1(object):

    def similarPairs(self, a1):
        """
        """
        v1 = collections.Counter()
        v2 = 0
        for v3 in a1:
            v4 = reduce(lambda total, x: total | x, map(lambda c: 1 << ord(c) - ord('a'), v3))
            v2 += v1[v4]
            v1[v4] += 1
        return v2
