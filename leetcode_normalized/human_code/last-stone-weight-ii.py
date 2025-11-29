class C1(object):

    def lastStoneWeightII(self, a1):
        """
        """
        v1 = {0}
        for v2 in a1:
            v1 |= {v2 + i for v3 in v1}
        v4 = sum(a1)
        return min((abs(v3 - (v4 - v3)) for v3 in v1))
