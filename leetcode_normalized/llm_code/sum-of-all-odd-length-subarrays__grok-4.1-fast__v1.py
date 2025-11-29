class C1:

    def sumOddLengthSubarrays(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = v3 + 1
            v5 = v1 - v3
            v6 = (v4 * v5 + 1) // 2
            v2 += a1[v3] * v6
        return v2
