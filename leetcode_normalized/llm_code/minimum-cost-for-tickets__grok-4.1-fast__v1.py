class C1:

    def mincostTickets(self, a1, a2):
        if not a1:
            return 0
        v1 = set(a1)
        v2 = a1[-1]
        v3 = [float('inf')] * (v2 + 1)
        v3[0] = 0
        v4 = [1, 7, 30]
        for v5 in range(1, v2 + 1):
            if v5 not in v1:
                v3[v5] = v3[v5 - 1]
                continue
            for v6, v7 in enumerate(v4):
                v8 = max(0, v5 - v7)
                v3[v5] = min(v3[v5], v3[v8] + a2[v6])
        return v3[v2]
