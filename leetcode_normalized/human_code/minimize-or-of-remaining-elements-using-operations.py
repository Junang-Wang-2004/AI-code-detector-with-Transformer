class C1(object):

    def minOrAfterOperations(self, a1, a2):
        """
        """
        v1 = 0
        v2 = max(a1).bit_length()
        v3 = (1 << v2) - 1
        for v4 in reversed(range(v2)):
            v1 <<= 1
            v5, v6 = (v3, 0)
            for v7 in a1:
                v5 &= v7 >> v4
                if v5 & ~v1:
                    v6 += 1
                else:
                    v5 = v3
            if v6 > a2:
                v1 += 1
        return v1
