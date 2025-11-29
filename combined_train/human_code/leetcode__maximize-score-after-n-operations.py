import itertools
from fractions import gcd

class C1(object):

    def maxScore(self, a1):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def bits(a1):
            v1 = []
            v2 = 0
            while a1:
                if a1 & 1:
                    v1.append(v2)
                v2 += 1
                a1 >>= 1
            return v1
        v1 = [0] * 2 ** len(a1)
        for v2 in range(3, len(v1)):
            v3 = popcount(v2)
            if v3 % 2:
                continue
            for v4, v5 in itertools.combinations(bits(v2), 2):
                v1[v2] = max(v1[v2], v3 // 2 * gcd(a1[v4], a1[v5]) + v1[v2 ^ 1 << v4 ^ 1 << v5])
        return v1[-1]
