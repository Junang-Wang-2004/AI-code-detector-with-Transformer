class C1:

    def zeroFilledSubarray(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            if v3 == 0:
                v2 += 1
            else:
                v1 += v2 * (v2 + 1) // 2
                v2 = 0
        v1 += v2 * (v2 + 1) // 2
        return v1
