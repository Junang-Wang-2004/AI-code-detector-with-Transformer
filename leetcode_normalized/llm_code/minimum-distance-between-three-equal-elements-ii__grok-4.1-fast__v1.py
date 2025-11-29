class C1:

    def minimumDistance(self, a1):
        v1 = {}
        for v2, v3 in enumerate(a1):
            if v3 not in v1:
                v1[v3] = []
            v1[v3].append(v2)
        v4 = float('inf')
        for v5 in v1.values():
            v6 = len(v5)
            if v6 >= 3:
                for v7 in range(2, v6):
                    v4 = min(v4, 2 * (v5[v7] - v5[v7 - 2]))
        return v4 if v4 != float('inf') else -1
