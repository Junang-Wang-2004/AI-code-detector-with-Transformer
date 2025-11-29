import bisect

class C1:

    def maxWalls(self, a1, a2, a3):
        v1 = sorted(zip(a1, a2))
        v1 = [(0, 0)] + v1 + [(float('inf'), 0)]
        v2 = sorted(a3)
        v3 = 0
        v4 = 0
        for v5 in range(1, len(v1) - 1):
            v6, v7 = v1[v5]
            v8, v9 = v1[v5 - 1]
            v10, v9 = v1[v5 + 1]
            v11 = min(v6 + v7, v10 - 1)
            v12 = bisect.bisect_right(v2, v11) - bisect.bisect_left(v2, v6)
            v13 = max(v3, v4) + v12
            v14 = max(v6 - v7, v8 + 1)
            v15 = min(v1[v5 - 1][0] + v1[v5 - 1][1], v6 - 1)
            v16 = max(v15 + 1, v14)
            v17 = bisect.bisect_right(v2, v6) - bisect.bisect_left(v2, v14)
            v18 = bisect.bisect_right(v2, v6) - bisect.bisect_left(v2, v16)
            v19 = max(v3 + v17, v4 + v18)
            v3 = v19
            v4 = v13
        return max(v3, v4)
