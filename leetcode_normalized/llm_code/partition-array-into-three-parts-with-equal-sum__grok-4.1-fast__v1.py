class C1:

    def canThreePartsEqualSum(self, a1):
        v1 = sum(a1)
        if v1 % 3 != 0:
            return False
        v2 = v1 // 3
        v3 = 0
        v4 = False
        for v5 in a1:
            v3 += v5
            if v3 == v2:
                v4 = True
            if v3 == 2 * v2 and v4:
                return True
        return False
