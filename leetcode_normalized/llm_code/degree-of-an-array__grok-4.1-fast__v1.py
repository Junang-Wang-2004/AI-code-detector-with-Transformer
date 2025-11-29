class C1:

    def findShortestSubArray(self, a1):
        v1 = {}
        v2 = {}
        v3 = {}
        for v4 in range(len(a1)):
            v5 = a1[v4]
            v1[v5] = v1.get(v5, 0) + 1
            if v5 not in v2:
                v2[v5] = v4
            v3[v5] = v4
        v6 = max(v1.values())
        v7 = len(a1) + 1
        for v5 in v1:
            if v1[v5] == v6:
                v7 = min(v7, v3[v5] - v2[v5] + 1)
        return v7
