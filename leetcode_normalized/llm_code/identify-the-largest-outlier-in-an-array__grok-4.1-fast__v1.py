class C1:

    def getLargestOutlier(self, a1):
        v1 = 0
        v2 = {}
        for v3 in a1:
            v1 += v3
            v2[v3] = v2.get(v3, 0) + 1
        v4 = sorted(v2, reverse=True)
        for v5 in v4:
            v6 = v1 - v5
            if v6 % 2 != 0:
                continue
            v7 = v6 // 2
            v8 = 1 if v7 == v5 else 0
            if v7 in v2 and v2[v7] >= 1 + v8:
                return v5
        return float('-inf')
