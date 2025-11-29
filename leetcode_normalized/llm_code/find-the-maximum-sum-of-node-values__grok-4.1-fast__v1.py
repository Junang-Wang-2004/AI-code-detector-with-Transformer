class C1:

    def maximumValueSum(self, a1, a2, a3):
        v1 = 0
        v2 = 0
        v3 = float('inf')
        for v4 in a1:
            v5 = v4 ^ a2
            if v5 > v4:
                v1 += v5
                v2 = 1 - v2
            else:
                v1 += v4
            v3 = min(v3, abs(v4 - v5))
        if v2:
            v1 -= v3
        return v1
