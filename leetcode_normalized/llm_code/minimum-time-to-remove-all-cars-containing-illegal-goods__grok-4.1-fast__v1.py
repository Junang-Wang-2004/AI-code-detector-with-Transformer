class C1:

    def minimumTime(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = float('inf')
        v4 = 0
        for v5 in a1:
            v4 += v5 == '1'
        v6 = 0
        for v7 in range(v1 + 1):
            v8 = min(v7, 2 * v6)
            v9 = min(v1 - v7, 2 * (v4 - v6))
            v3 = min(v3, v8 + v9)
            if v7 < v1:
                v6 += a1[v7] == '1'
        return v3
