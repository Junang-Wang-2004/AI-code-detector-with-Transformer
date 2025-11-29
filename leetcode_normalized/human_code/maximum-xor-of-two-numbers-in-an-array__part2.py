class C1(object):

    def findMaximumXOR(self, a1):
        """
        """
        v1 = 0
        for v2 in reversed(range(max(a1).bit_length())):
            v1 <<= 1
            v3 = set()
            for v4 in a1:
                v3.add(v4 >> v2)
            for v5 in v3:
                if (v1 | 1) ^ v5 in v3:
                    v1 |= 1
                    break
        return v1
