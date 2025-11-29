class C1:

    def minimumRelativeLosses(self, a1, a2):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = [0]
        for v4 in v1:
            v3.append(v3[-1] + v4)
        v5 = []
        for v6, v7 in a2:
            v8 = 0
            v9 = v7
            while v8 < v9:
                v10 = (v8 + v9) // 2
                v11 = v2 - (v7 - v10)
                if v1[v10] + v1[v11] >= 2 * v6:
                    v9 = v10
                else:
                    v8 = v10 + 1
            v12 = v8
            v13 = v7 - v12
            v14 = v3[v12]
            v15 = v3[v2] - v3[v2 - v13]
            v16 = v14 + v13 * v6 - (v15 - v13 * v6)
            v5.append(v16)
        return v5
