import collections
from functools import reduce

class C1(object):

    def countGoodSubsequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            if not 0 <= a2 <= a1:
                return 0
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1
        v6 = collections.Counter(a1)
        return reduce(lambda total, k: (total + reduce(lambda total, x: total * (1 + nCr(x, k)) % v1, iter(v6.values()), 1) - 1) % v1, range(1, max(v6.values()) + 1), 0)
