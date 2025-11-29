class C1(object):

    def maxProduct(self, a1, a2, a3):
        v1 = sum(a1)
        if abs(a2) > v1:
            return -1
        v2 = {}
        for v3 in a1:
            v4 = v2.copy()
            if v3 <= a3:
                v5 = (1, v3)
                v4[v5] = max(v4.get(v5, 0), v3)
            for v6, v7 in v2.items():
                v8, v9 = v6
                v10 = v3 if v8 == 0 else -v3
                v11 = v9 + v10
                v12 = 1 - v8
                v13 = v7 * v3
                if v13 <= a3:
                    v14 = (v12, v11)
                    v4[v14] = max(v4.get(v14, 0), v13)
            v2 = v4
        v15 = -1
        for v5, v16 in v2.items():
            v8, v9 = v5
            if v9 == a2:
                v15 = max(v15, v16)
        return v15
