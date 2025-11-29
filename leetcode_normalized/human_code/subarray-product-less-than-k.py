class C1(object):

    def numSubarrayProductLessThanK(self, a1, a2):
        """
        """
        if a2 <= 1:
            return 0
        v1, v2, v3 = (0, 0, 1)
        for v4, v5 in enumerate(a1):
            v3 *= v5
            while v3 >= a2:
                v3 /= a1[v2]
                v2 += 1
            v1 += v4 - v2 + 1
        return v1
