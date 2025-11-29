import bisect

class C1:

    def maxDepthBST(self, a1):
        v1 = {}
        v2 = []
        v3 = 0
        for v4 in a1:
            v5 = bisect.bisect_left(v2, v4)
            v6 = v1[v2[v5 - 1]] if v5 > 0 else 0
            v7 = v1[v2[v5]] if v5 < len(v2) else 0
            v8 = 1 + max(v6, v7)
            v1[v4] = v8
            v3 = max(v3, v8)
            bisect.insort_left(v2, v4)
        return v3
