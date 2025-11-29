import collections
import math

class C1:

    def countPairs(self, a1, a2):
        v1 = collections.Counter((math.gcd(num, a2) for v2 in a1))
        v3 = list(v1)
        v4 = 0
        v5 = len(v3)
        for v6 in range(v5):
            v7 = v3[v6]
            for v8 in range(v6, v5):
                v9 = v3[v8]
                if v7 * v9 % a2 == 0:
                    if v6 == v8:
                        v4 += v1[v7] * (v1[v7] - 1) // 2
                    else:
                        v4 += v1[v7] * v1[v9]
        return v4
