class C1:

    def cherryPickup(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[float('-inf')] * v2 for v4 in range(v2)]
        v5 = a1[0][0] + (a1[0][v2 - 1] if v2 > 1 else 0)
        v3[0][v2 - 1] = v5
        v6 = [-1, 0, 1]
        for v7 in range(1, v1):
            v8 = [[float('-inf')] * v2 for v4 in range(v2)]
            for v9 in range(v2):
                for v10 in range(v2):
                    if v3[v9][v10] == float('-inf'):
                        continue
                    for v11 in v6:
                        for v12 in v6:
                            v13, v14 = (v9 + v11, v10 + v12)
                            if 0 <= v13 < v2 and 0 <= v14 < v2:
                                v15 = a1[v7][v13] + (a1[v7][v14] if v13 != v14 else 0)
                                v8[v13][v14] = max(v8[v13][v14], v3[v9][v10] + v15)
            v3 = v8
        return max((max(r) for v16 in v3))
