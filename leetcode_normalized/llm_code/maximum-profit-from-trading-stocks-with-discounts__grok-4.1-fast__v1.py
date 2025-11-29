class C1:

    def maxProfit(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a4:
            v1[v3 - 1].append(v4 - 1)
        v5 = -10 ** 18

        def compute(a1):
            v1 = [v5] * (a5 + 1)
            v2 = [v5] * (a5 + 1)
            v1[0] = v2[0] = 0
            for v3 in v1[a1]:
                v4, v5 = compute(v3)
                v6 = [v5] * (a5 + 1)
                v7 = [v5] * (a5 + 1)
                for v8 in range(a5 + 1):
                    if v1[v8] == v5:
                        continue
                    for v9 in range(a5 - v8 + 1):
                        if v4[v9] == v5:
                            continue
                        v6[v8 + v9] = max(v6[v8 + v9], v1[v8] + v4[v9])
                for v8 in range(a5 + 1):
                    if v2[v8] == v5:
                        continue
                    for v9 in range(a5 - v8 + 1):
                        if v5[v9] == v5:
                            continue
                        v7[v8 + v9] = max(v7[v8 + v9], v2[v8] + v5[v9])
                v1, v2 = (v6, v7)
            v10 = [v5] * (a5 + 1)
            v11 = [v5] * (a5 + 1)
            for v8 in range(a5 + 1):
                if v1[v8] != v5:
                    v10[v8] = max(v10[v8], v1[v8])
                    v11[v8] = max(v11[v8], v1[v8])
            v12 = a2[a1]
            if v12 <= a5:
                v13 = a3[a1] - v12
                for v8 in range(a5 - v12 + 1):
                    if v2[v8] != v5:
                        v10[v8 + v12] = max(v10[v8 + v12], v2[v8] + v13)
            v14 = a2[a1] >> 1
            if v14 <= a5:
                v15 = a3[a1] - v14
                for v8 in range(a5 - v14 + 1):
                    if v2[v8] != v5:
                        v11[v8 + v14] = max(v11[v8 + v14], v2[v8] + v15)
            return (v10, v11)
        v6, v2 = compute(0)
        return max(v6)
