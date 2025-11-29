class C1(object):

    def subsequenceSumOr(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(64):
            v2 >>= 1
            for v4 in a1:
                v2 += v4 >> v3 & 1
            if v2:
                v1 |= 1 << v3
        return v1
