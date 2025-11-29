import collections
from functools import reduce

class C1(object):

    def sumOfFlooredPairs(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = ([0] * (max(a1) + 1), collections.Counter(a1))
        for v4, v5 in v3.items():
            for v6 in range(v4, len(v2), v4):
                v2[v6] += v3[v4]
        for v7 in range(len(v2) - 1):
            v2[v7 + 1] += v2[v7]
        return reduce(lambda total, num: (total + v2[v4]) % v1, a1, 0)
