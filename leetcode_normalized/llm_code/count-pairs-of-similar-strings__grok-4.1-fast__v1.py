class C1:

    def similarPairs(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = frozenset(v2)
            v1[v3] = v1.get(v3, 0) + 1
        v4 = 0
        for v5 in v1.values():
            v4 += v5 * (v5 - 1) // 2
        return v4
