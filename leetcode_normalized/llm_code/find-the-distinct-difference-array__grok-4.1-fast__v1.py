class C1:

    def distinctDifferenceArray(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = set()
        for v4 in range(v1):
            v3.add(a1[v4])
            v2[v4] = len(v3)
        v5 = [0] * v1
        v6 = set()
        for v4 in range(v1 - 1, -1, -1):
            v6.add(a1[v4])
            v5[v4] = len(v6)
        return [v2[v4] - (v5[v4 + 1] if v4 + 1 < v1 else 0) for v4 in range(v1)]
