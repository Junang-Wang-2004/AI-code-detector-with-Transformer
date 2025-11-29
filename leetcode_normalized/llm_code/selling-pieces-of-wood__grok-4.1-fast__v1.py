class C1(object):

    def sellingWood(self, a1, a2, a3):
        v1 = {}
        for v2, v3, v4 in a3:
            v5 = (v2, v3)
            v1[v5] = max(v1.get(v5, 0), v4)
        for v6 in range(1, a1 + 1):
            for v7 in range(1, a2 + 1):
                v8 = (v6, v7)
                if v8 not in v1:
                    v1[v8] = 0
                for v9 in range(1, v6 // 2 + 1):
                    v1[v8] = max(v1[v8], v1[v9, v7] + v1[v6 - v9, v7])
                for v10 in range(1, v7 // 2 + 1):
                    v1[v8] = max(v1[v8], v1[v6, v10] + v1[v6, v7 - v10])
        return v1[a1, a2]
