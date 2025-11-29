class C1:

    def pathSum(self, a1):
        if not a1:
            return 0
        v1 = {}
        for v2 in a1:
            v3 = v2 // 100 - 1
            v4 = v2 % 100 // 10 - 1
            v5 = v2 % 10
            v1[v3, v4] = v5
        v6 = {}
        v7 = list(v1)
        v7.sort(key=lambda x: x[0], reverse=True)
        for v3, v4 in v7:
            v8 = (v3 + 1, 2 * v4)
            v9 = (v3 + 1, 2 * v4 + 1)
            v10 = 0
            if v8 in v1:
                v10 += v6[v8]
            if v9 in v1:
                v10 += v6[v9]
            v6[v3, v4] = v10 if v10 > 0 else 1
        v11 = 0
        for v12, v5 in v1.items():
            v11 += v5 * v6[v12]
        return v11
