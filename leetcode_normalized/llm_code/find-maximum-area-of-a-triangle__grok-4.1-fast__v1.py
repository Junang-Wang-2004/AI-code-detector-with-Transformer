class C1:

    def maxArea(self, a1):
        if not a1:
            return -1
        v1 = v2 = float('inf')
        v3 = v4 = float('-inf')
        v5 = {}
        v6 = {}
        v7 = {}
        v8 = {}
        for v9, v10 in a1:
            v1 = min(v1, v9)
            v3 = max(v3, v9)
            v2 = min(v2, v10)
            v4 = max(v4, v10)
            if v9 not in v5:
                v5[v9] = v10
                v6[v9] = v10
            else:
                v5[v9] = min(v5[v9], v10)
                v6[v9] = max(v6[v9], v10)
            if v10 not in v7:
                v7[v10] = v9
                v8[v10] = v9
            else:
                v7[v10] = min(v7[v10], v9)
                v8[v10] = max(v8[v10], v9)
        v11 = 0
        for v12 in v5:
            v13 = v6[v12] - v5[v12]
            v14 = max(v12 - v1, v3 - v12)
            v11 = max(v11, v13 * v14)
        for v15 in v7:
            v14 = v8[v15] - v7[v15]
            v13 = max(v15 - v2, v4 - v15)
            v11 = max(v11, v14 * v13)
        return v11 if v11 else -1
