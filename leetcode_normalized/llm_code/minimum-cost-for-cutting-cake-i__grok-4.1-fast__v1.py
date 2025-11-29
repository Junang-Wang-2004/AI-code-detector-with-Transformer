class C1:

    def minimumCost(self, a1, a2, a3, a4):
        v1 = [(c, 0) for v2 in a3] + [(v2, 1) for v2 in a4]
        v1.sort(reverse=True)
        v3 = v4 = 0
        v5 = 0
        for v2, v6 in v1:
            if v6 == 0:
                v5 += v2 * (v4 + 1)
                v3 += 1
            else:
                v5 += v2 * (v3 + 1)
                v4 += 1
        return v5
