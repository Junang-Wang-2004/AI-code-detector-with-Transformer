class C1(object):

    def getMaximumXor(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        v2 = 2 ** a2 - 1
        for v3 in range(len(a1)):
            v2 ^= a1[v3]
            v1[-1 - v3] = v2
        return v1
