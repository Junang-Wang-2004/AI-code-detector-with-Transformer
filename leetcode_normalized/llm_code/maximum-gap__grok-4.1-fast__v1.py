class C1:

    def maximumGap(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = min(a1)
        v3 = max(a1)
        v4 = max(1, (v3 - v2) // (v1 - 1))
        v5 = (v3 - v2) // v4 + 1
        v6 = [float('inf')] * v5
        v7 = [float('-inf')] * v5
        for v8 in a1:
            if v8 == v2 or v8 == v3:
                continue
            v9 = (v8 - v2) // v4
            v6[v9] = min(v6[v9], v8)
            v7[v9] = max(v7[v9], v8)
        v10 = 0
        v11 = v2
        for v12 in range(v5):
            if v6[v12] == float('inf'):
                continue
            v10 = max(v10, v6[v12] - v11)
            v11 = v7[v12]
        v10 = max(v10, v3 - v11)
        return v10
