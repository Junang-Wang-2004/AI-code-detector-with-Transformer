import collections
import math
v1 = 1000000
v2 = [True] * v1
v2[0] = v2[1] = False
for v3 in range(2, math.isqrt(v1) + 1):
    if v2[v3]:
        for v4 in range(v3 * v3, v1, v3):
            v2[v4] = False

class C1:

    def mostFrequentPrime(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        v4 = collections.Counter()
        for v5 in range(v1):
            for v6 in range(v2):
                for v7, v8 in v3:
                    v9 = 0
                    v10 = v5
                    v11 = v6
                    while 0 <= v10 < v1 and 0 <= v11 < v2:
                        v9 = v9 * 10 + a1[v10][v11]
                        if v9 > 10 and v9 < v1 and v2[v9]:
                            v4[v9] += 1
                        v10 += v7
                        v11 += v8
        return max(v4, key=lambda p: (v4[p], p)) if v4 else -1
