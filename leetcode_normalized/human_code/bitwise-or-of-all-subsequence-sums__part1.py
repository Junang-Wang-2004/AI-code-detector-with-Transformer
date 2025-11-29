class C1(object):

    def subsequenceSumOr(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v2 += v3
            v1 |= v3 | v2
        return v1
