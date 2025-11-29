import collections
import bisect

class C1:

    def gcdValues(self, a1, a2):
        v1 = max(a1)
        v2 = collections.Counter(a1)
        v3 = [0] * (v1 + 1)
        for v4 in range(1, v1 + 1):
            v5 = v4
            while v5 <= v1:
                v3[v4] += v2[v5]
                v5 += v4
        v6 = [0] * (v1 + 1)
        for v4 in range(v1, 0, -1):
            v7 = v3[v4] * (v3[v4] - 1) // 2
            v8 = 0
            v9 = v4 * 2
            while v9 <= v1:
                v8 += v6[v9]
                v9 += v4
            v6[v4] = v7 - v8
        v10 = [0]
        for v4 in range(1, v1 + 1):
            v10.append(v10[-1] + v6[v4])
        v11 = []
        for v12 in a2:
            v11.append(bisect.bisect_left(v10, v12))
        return v11
