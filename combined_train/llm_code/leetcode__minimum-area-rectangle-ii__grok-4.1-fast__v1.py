class C1(object):

    def minAreaFreeRect(self, a1):
        v1 = set((tuple(p) for v2 in a1))
        v3 = float('inf')
        v4 = len(a1)
        for v5 in range(v4):
            v6, v7 = a1[v5]
            for v8 in range(v4):
                if v5 == v8:
                    continue
                v9, v10 = a1[v8]
                v11 = v9 - v6
                v12 = v10 - v7
                for v13 in range(v4):
                    if v13 == v5 or v13 == v8:
                        continue
                    v14, v15 = a1[v13]
                    v16 = v14 - v6
                    v17 = v15 - v7
                    if v11 * v16 + v12 * v17 != 0:
                        continue
                    v18 = v6 + v11 + v16
                    v19 = v7 + v12 + v17
                    if (v18, v19) in v1:
                        v20 = (v11 * v11 + v12 * v12) * (v16 * v16 + v17 * v17)
                        v3 = min(v3, v20 ** 0.5)
        return v3 if v3 < float('inf') else 0.0
