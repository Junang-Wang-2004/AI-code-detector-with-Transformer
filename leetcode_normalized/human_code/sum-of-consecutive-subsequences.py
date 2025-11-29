import collections
from functools import reduce

class C1(object):

    def getSum(self, a1):
        """
        """

        def count(a1):
            v1 = 0
            v2 = collections.defaultdict(int)
            v3 = collections.defaultdict(int)
            for v4 in a1:
                v5 = (v2[v4 - a1] + 1) % MOD
                v2[v4] = (v2[v4] + v5) % MOD
                v6 = (v3[v4 - a1] + v4 * v5) % MOD
                v3[v4] = (v3[v4] + v6) % MOD
                v1 = (v1 + v6) % MOD
            return v1
        v1 = 10 ** 9 + 7
        return (count(+1) + count(-1) - reduce(lambda accu, x: (accu + x) % v1, a1, 0)) % v1
