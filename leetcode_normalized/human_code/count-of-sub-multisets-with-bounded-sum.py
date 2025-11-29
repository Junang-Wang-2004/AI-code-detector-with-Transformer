import collections
from functools import reduce

class C1(object):

    def countSubMultisets(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = collections.Counter(a1)
        v3 = [0] * (a3 + 1)
        v3[0] = 1
        for v4, v5 in v2.items():
            for v6 in reversed(range(max(a3 - v4 + 1, 1), a3 + 1)):
                v7 = reduce(lambda x, y: (v4 + y) % v1, (v3[v6 - v4 * j] for v8 in range(min(v5, v6 // v4 + 1))))
                for v8 in reversed(range((v6 - 1) % v4 + 1, v6 + 1, v4)):
                    v7 = (v7 + (v3[v8 - v4 * v5] if v8 - v4 * v5 >= 0 else 0) - v3[v8]) % v1
                    v3[v8] = (v3[v8] + v7) % v1
        return reduce(lambda x, y: (v4 + y) % v1, (v3[v6] for v6 in range(a2, a3 + 1))) * (v2[0] + 1) % v1
