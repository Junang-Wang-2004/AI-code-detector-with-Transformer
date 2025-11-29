import collections
from functools import reduce

class C1(object):

    def numberOfGoodSubsets(self, a1):
        """
        """

        def sieve_of_eratosthenes(a1):
            if a1 < 2:
                return []
            v1 = [2]
            v2 = [True] * ((a1 + 1) // 2)
            for v3 in range(1, len(v2)):
                if not v2[v3]:
                    continue
                v1.append(2 * v3 + 1)
                for v4 in range(2 * v3 * (v3 + 1), len(v2), 2 * v3 + 1):
                    v2[v4] = False
            return v1

        def to_mask(a1, a2):
            v1, v2 = (0, 1)
            for v3 in a1:
                if a2 % v3 == 0:
                    v1 |= v2
                v2 <<= 1
            return v1
        v1 = 10 ** 9 + 7
        v2 = sieve_of_eratosthenes(max(a1))
        v3 = [0] * (1 << len(v2))
        v3[0] = 1
        v4 = collections.Counter(a1)
        for v5, v6 in v4.items():
            if v5 == 1 or any((v5 % (p * p) == 0 for v7 in v2 if v7 * v7 <= v5)):
                continue
            v8 = to_mask(v2, v5)
            for v9 in range(len(v3) - 1):
                if v9 & v8:
                    continue
                v3[v9 | v8] = (v3[v9 | v8] + v6 * v3[v9]) % v1
        return pow(2, v4[1], v1) * (reduce(lambda total, x: (total + v5) % v1, v3, 0) - 1) % v1
