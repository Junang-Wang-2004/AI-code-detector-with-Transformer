class C1:

    def maxProfit(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = {}
        for v4, v5 in a2:
            if v4 not in v3:
                v3[v4] = []
            v3[v4].append(v5)
        v6 = 0
        v7 = []
        for v8, v9 in v3.items():
            v10 = sorted(v9, reverse=True)
            v11 = v1.get(v8, 0)
            v12 = min(v11, len(v10))
            v6 += sum(v10[:v12])
            if len(v10) > v11:
                v7.extend(v10[v12:])
        if v7:
            v6 += max(v7)
        return v6
