from collections import Counter
import bisect

class C1:

    def maxFrequency(self, a1, a2, a3):
        if not a1:
            return 0
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = Counter(a1)
        v4 = 0
        for v5 in v3:
            v6 = bisect.bisect_left(v1, v5 - a2)
            v7 = bisect.bisect_right(v1, v5 + a2) - 1
            v8 = v7 - v6 + 1 if v6 <= v7 else 0
            v9 = v3[v5]
            v4 = max(v4, v9 + min(v8 - v9, a3))
        v10 = 0
        for v11 in range(v2):
            while v1[v11] - v1[v10] > 2 * a2:
                v10 += 1
            v4 = max(v4, min(v11 - v10 + 1, a3))
        return v4
