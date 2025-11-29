import bisect

class C1:

    def minAbsoluteSumDiff(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = sorted(a1)
        v4 = sum((abs(a1[k] - a2[k]) for v5 in range(v2))) % v1
        v6 = 0
        for v7 in range(v2):
            v8 = a2[v7]
            v9 = abs(a1[v7] - v8)
            v10 = bisect.bisect_left(v3, v8)
            v11 = float('inf')
            if v10 < v2:
                v11 = min(v11, abs(v3[v10] - v8))
            if v10 > 0:
                v11 = min(v11, abs(v3[v10 - 1] - v8))
            v12 = v9 - v11
            if v12 > v6:
                v6 = v12
        return (v4 - v6) % v1
