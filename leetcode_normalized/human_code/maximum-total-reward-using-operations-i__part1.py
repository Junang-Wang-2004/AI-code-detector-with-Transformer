class C1(object):

    def maxTotalReward(self, a1):
        """
        """
        v1 = max(a1)
        v2 = 1
        v3 = (1 << v1) - 1
        for v4 in sorted(set(a1)):
            v5 = v2 & (1 << v4) - 1
            v2 |= v5 << v4 & v3
        return v1 + (v2.bit_length() - 1)
