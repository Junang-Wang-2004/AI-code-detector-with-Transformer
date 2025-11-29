class C1:

    def minCost(self, a1, a2):
        v1 = sorted(zip(a1, a2))
        v2 = sum((w for v3, v4 in v1))
        v5 = 0
        v6 = (v2 + 1) // 2
        v7 = 0
        for v8, v4 in v1:
            v5 += v4
            if v5 >= v6:
                v7 = v8
                break
        return sum((abs(v8 - v7) * v4 for v8, v4 in v1))
