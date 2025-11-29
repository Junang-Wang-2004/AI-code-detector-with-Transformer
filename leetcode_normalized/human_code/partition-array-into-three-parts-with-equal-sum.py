class C1(object):

    def canThreePartsEqualSum(self, a1):
        """
        """
        v1 = sum(a1)
        if v1 % 3 != 0:
            return False
        v2, v3 = (0, 0)
        for v4 in a1:
            v3 += v4
            if v3 == v1 // 3:
                v2 += 1
                v3 = 0
        return v2 >= 3
