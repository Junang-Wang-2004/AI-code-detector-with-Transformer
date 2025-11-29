class C1:

    def minimumCost(self, a1, a2, a3, a4):
        v1 = sorted(a3, reverse=True)
        v2 = sorted(a4, reverse=True)
        v3 = 0
        v4 = v5 = 0
        v6 = v7 = 1
        while v4 < len(v1) or v5 < len(v2):
            if v5 == len(v2) or (v4 < len(v1) and v1[v4] > v2[v5]):
                v3 += v1[v4] * v7
                v4 += 1
                v6 += 1
            else:
                v3 += v2[v5] * v6
                v5 += 1
                v7 += 1
        return v3
