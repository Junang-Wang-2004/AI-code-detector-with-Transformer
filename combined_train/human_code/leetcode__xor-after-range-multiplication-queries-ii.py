import collections
from functools import reduce

class C1(object):

    def xorAfterQueries(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def inv(a1):
            return pow(a1, v1 - 2, v1)
        v2 = int(len(a1) ** 0.5) + 1
        v3 = collections.defaultdict(lambda: [1] * len(a1))
        for v4, v5, v6, v7 in a2:
            if v6 <= v2:
                v3[v6][v4] = v3[v6][v4] * v7 % v1
                v5 += v6 - (v5 - v4) % v6
                if v5 < len(a1):
                    v3[v6][v5] = v3[v6][v5] * inv(v7) % v1
            else:
                for v8 in range(v4, v5 + 1, v6):
                    a1[v8] = a1[v8] * v7 % v1
        for v6, v9 in v3.items():
            for v8 in range(len(v9)):
                if v8 - v6 >= 0:
                    v9[v8] = v9[v8] * v9[v8 - v6] % v1
                a1[v8] = a1[v8] * v9[v8] % v1
        return reduce(lambda accu, x: accu ^ x, a1, 0)
