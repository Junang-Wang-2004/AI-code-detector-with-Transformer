class C1(object):

    def findErrorNums(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v1 ^= a1[v2] ^ v2 + 1
        v3 = v1 & ~(v1 - 1)
        v4 = [0] * 2
        for v2, v5 in enumerate(a1):
            v4[bool(v5 & v3)] ^= v5
            v4[bool(v2 + 1 & v3)] ^= v2 + 1
        if v4[0] not in a1:
            v4[0], v4[1] = (v4[1], v4[0])
        return v4
