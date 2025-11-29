class C1:

    def maximumBags(self, a1, a2, a3):
        v1 = sorted((capacity - stone for v2, v3 in zip(a1, a2)))
        v4 = 0
        v5 = 0
        for v6 in v1:
            v4 += v6
            if v4 > a3:
                return v5
            v5 += 1
        return v5
