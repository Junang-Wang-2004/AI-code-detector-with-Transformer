class C1:

    def bestCoordinate(self, a1, a2):
        v1 = [t[0] for v2 in a1]
        v3 = [v2[1] for v2 in a1]
        v4, v5 = (min(v1), max(v1))
        v6, v7 = (min(v3), max(v3))
        v8 = -1
        v9 = [0, 0]
        for v10 in range(v4, v5 + 1):
            for v11 in range(v6, v7 + 1):
                v12 = 0
                for v13, v14, v15 in a1:
                    v16 = v13 - v10
                    v17 = v14 - v11
                    v18 = (v16 * v16 + v17 * v17) ** 0.5
                    if v18 <= a2:
                        v12 += int(v15 / (1 + v18))
                if v12 > v8:
                    v8 = v12
                    v9 = [v10, v11]
        return v9
