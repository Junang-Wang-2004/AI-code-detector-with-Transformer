class C1:

    def countWays(self, a1):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = 0
        for v4 in range(v2 + 1):
            v5 = v4 == 0 or v1[v4 - 1] < v4
            v6 = v4 == v2 or v1[v4] > v4
            if v5 and v6:
                v3 += 1
        return v3
