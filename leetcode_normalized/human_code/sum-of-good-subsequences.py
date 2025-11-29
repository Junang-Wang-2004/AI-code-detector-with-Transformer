import collections
from functools import reduce

class C1(object):

    def sumOfGoodSubsequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = collections.defaultdict(int)
        v3 = collections.defaultdict(int)
        for v4 in a1:
            v5 = v3[v4 - 1] + v3[v4 + 1] + 1
            v3[v4] = (v3[v4] + v5) % v1
            v2[v4] = (v2[v4] + (v2[v4 - 1] + v2[v4 + 1] + v4 * v5)) % v1
        return reduce(lambda accu, x: (accu + v4) % v1, iter(v2.values()))
