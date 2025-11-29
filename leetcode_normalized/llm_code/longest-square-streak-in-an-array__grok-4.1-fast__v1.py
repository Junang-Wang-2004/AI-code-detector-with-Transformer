class C1:

    def longestSquareStreak(self, a1):
        v1 = sorted(set(a1))
        v2 = {}
        v3 = 0
        for v4 in v1:
            v5 = int(v4 ** 0.5)
            v6 = v2.get(v5, 0) if v5 * v5 == v4 else 0
            v2[v4] = v6 + 1
            v3 = max(v3, v2[v4])
        return v3 if v3 > 1 else -1
