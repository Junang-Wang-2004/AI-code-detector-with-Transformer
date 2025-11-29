class C1:

    def maximizeTheProfit(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v4].append((v3, v5))
        v6 = [0] * (a1 + 1)
        for v7 in range(a1):
            v8 = v6[v7]
            for v9, v10 in v1[v7]:
                v8 = max(v8, v6[v9] + v10)
            v6[v7 + 1] = v8
        return v6[-1]
