from collections import Counter
from bisect import bisect_left, bisect_right

class C1:

    def maxFrequency(self, a1, a2, a3):
        a1.sort()
        v1 = len(a1)
        v2 = Counter(a1)
        v3 = sorted(v2)
        v4 = 0
        v5 = 0
        v6 = 0
        for v7 in range(v1):
            while a1[v7] - a1[v5] > 2 * a2:
                v5 += 1
            v6 = max(v6, v7 - v5 + 1)
        v4 = max(v4, min(v6, a3))
        for v8 in v3:
            v9 = bisect_left(a1, v8 - a2)
            v10 = bisect_right(a1, v8 + a2) - 1
            v11 = v10 - v9 + 1 if v9 <= v10 else 0
            v12 = v2[v8]
            v13 = v11 - v12
            v4 = max(v4, v12 + min(v13, a3))
        return v4
