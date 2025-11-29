class C1:

    def minSumSquareDiff(self, a1, a2, a3, a4):
        v1 = len(a1)
        v2 = sorted((abs(a1[i] - a2[i]) for v3 in range(v1)))[::-1]
        v4 = min(a3 + a4, sum(v2))

        def cost_to_cap(a1):
            v1 = 0
            for v2 in v2:
                v1 += max(0, v2 - a1)
            return v1
        v5, v6 = (0, v2[0] if v2 else 0)
        while v5 < v6:
            v7 = v5 + (v6 - v5) // 2
            if cost_to_cap(v7) <= v4:
                v6 = v7
            else:
                v5 = v7 + 1
        v8 = v5
        v9 = cost_to_cap(v8)
        v10 = v4 - v9
        v11 = 0
        for v3 in range(v1):
            v12 = min(v2[v3], v8)
            if v3 < v10:
                v12 -= 1
            v11 += v12 * v12
        return v11
