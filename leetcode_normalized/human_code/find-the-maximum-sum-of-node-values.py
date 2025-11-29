class C1(object):

    def maximumValueSum(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        v3 = float('inf')
        for v4 in a1:
            v5 = v4 ^ a2
            v1 += max(v4, v5)
            v2 ^= int(v4 < v5)
            v3 = min(v3, abs(v4 - v5))
        return v1 - v2 * v3
