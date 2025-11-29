class C1(object):

    def maxTotalReward(self, a1):
        """
        """
        v1 = 1
        for v2 in sorted(set(a1)):
            v3 = v1 & (1 << v2) - 1
            v1 |= v3 << v2
        return v1.bit_length() - 1
