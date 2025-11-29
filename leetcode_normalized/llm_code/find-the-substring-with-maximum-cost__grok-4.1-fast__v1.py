class C1:

    def maximumCostSubstring(self, a1, a2, a3):
        v1 = dict(zip(a2, a3))
        v2 = [v1.get(chr(ord('a') + i), i + 1) for v3 in range(26)]
        v4 = 0
        v5 = 0
        for v6 in a1:
            v3 = ord(v6) - ord('a')
            v5 = max(v5 + v2[v3], 0)
            v4 = max(v4, v5)
        return v4
