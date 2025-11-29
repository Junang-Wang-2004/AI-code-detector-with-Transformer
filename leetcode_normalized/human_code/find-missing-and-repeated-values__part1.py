class C1(object):

    def findMissingAndRepeatedValues(self, a1):
        """
        """
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1 ** 2):
            v4, v5 = divmod(v3, v1)
            v2 ^= a1[v4][v5] ^ v3 + 1
        v6 = v2 & -v2
        v7 = [0] * 2
        for v3 in range(v1 ** 2):
            v4, v5 = divmod(v3, len(a1[0]))
            v7[1 if v3 + 1 & v6 != 0 else 0] ^= v3 + 1
            v7[1 if a1[v4][v5] & v6 != 0 else 0] ^= a1[v4][v5]
        if any((x == v7[1] for v8 in a1 for v9 in v8)):
            v7[0], v7[1] = (v7[1], v7[0])
        return v7
