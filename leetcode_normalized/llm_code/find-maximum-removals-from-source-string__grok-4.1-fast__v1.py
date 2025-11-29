class C1:

    def maxRemovals(self, a1, a2, a3):
        v1 = len(a2)
        v2 = [float('inf')] * (v1 + 1)
        v2[0] = 0
        v3 = set(a3)
        for v4, v5 in enumerate(a1):
            v6 = 1 if v4 in v3 else 0
            for v7 in range(v1, 0, -1):
                if a2[v7 - 1] == v5:
                    v2[v7] = min(v2[v7], v2[v7 - 1] + v6)
        return len(a3) - v2[v1]
