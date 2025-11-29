import collections
from functools import reduce

class C1(object):

    def subsequencePairCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v2 = collections.defaultdict(int)
        v2[0, 0] = 1
        for v3 in a1:
            v4 = collections.defaultdict(int)
            for (v5, v6), v7 in list(v2.items()):
                v8, v9 = (gcd(v5, v3), gcd(v6, v3))
                v4[v5, v6] = (v4[v5, v6] + v7) % v1
                v4[v8, v6] = (v4[v8, v6] + v7) % v1
                v4[v5, v9] = (v4[v5, v9] + v7) % v1
            v2 = v4
        return reduce(lambda accu, x: (accu + v3) % v1, (v7 for (v5, v6), v7 in v2.items() if v5 == v6 > 0), 0)
