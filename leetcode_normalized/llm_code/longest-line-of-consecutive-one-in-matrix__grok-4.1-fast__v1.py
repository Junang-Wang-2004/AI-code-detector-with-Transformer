class C1:

    def longestLine(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [0] * v2
        v5 = [0] * v2
        v6 = [0] * v2
        for v7 in range(v1):
            v8 = [0] * v2
            v9 = [0] * v2
            v10 = [0] * v2
            v11 = 0
            for v12 in range(v2):
                if a1[v7][v12] == 0:
                    v11 = 0
                    v8[v12] = 0
                    v9[v12] = 0
                    v10[v12] = 0
                    continue
                v11 += 1
                v3 = max(v3, v11)
                v8[v12] = v4[v12] + 1 if v7 > 0 else 1
                v3 = max(v3, v8[v12])
                v9[v12] = v5[v12 - 1] + 1 if v7 > 0 and v12 > 0 else 1
                v3 = max(v3, v9[v12])
                v10[v12] = v6[v12 + 1] + 1 if v7 > 0 and v12 < v2 - 1 else 1
                v3 = max(v3, v10[v12])
            v4[:] = v8
            v5[:] = v9
            v6[:] = v10
        return v3
