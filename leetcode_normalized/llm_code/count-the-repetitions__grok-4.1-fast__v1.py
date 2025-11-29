class C1:

    def getMaxRepetitions(self, a1, a2, a3, a4):
        v1 = len(a3)
        v2 = [0] * v1
        v3 = [0] * v1
        for v4 in range(v1):
            v5 = v4
            v6 = 0
            for v7 in a1:
                if v7 == a3[v5]:
                    v5 = (v5 + 1) % v1
                    if v5 == 0:
                        v6 += 1
            v2[v4] = v5
            v3[v4] = v6
        v5 = 0
        v8 = 0
        v9 = {}
        v10 = 0
        while v10 < a2:
            if v5 in v9:
                v11, v12 = v9[v5]
                v13 = v10 - v11
                v14 = v8 - v12
                v15 = (a2 - v11) // v13
                v8 = v12 + v15 * v14
                v16 = (a2 - v11) % v13
                for v17 in range(v16):
                    v8 += v3[v5]
                    v5 = v2[v5]
                return v8 // a4
            v9[v5] = (v10, v8)
            v8 += v3[v5]
            v5 = v2[v5]
            v10 += 1
        return v8 // a4
