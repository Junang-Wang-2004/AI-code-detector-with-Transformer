class C1(object):

    def sumIndicesWithKSetBits(self, a1, a2):
        """
        """

        def next_popcount(a1):
            v1 = a1 & -a1
            v2 = a1 + v1
            v3 = a1 ^ v2
            v4 = v3 // v1 >> 2
            return v2 | v4
        v1 = 0
        v2 = (1 << a2) - 1
        while v2 < len(a1):
            v1 += a1[v2]
            if v2 == 0:
                break
            v2 = next_popcount(v2)
        return v1
