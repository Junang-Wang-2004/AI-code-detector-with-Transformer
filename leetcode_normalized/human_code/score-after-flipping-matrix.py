class C1(object):

    def matrixScore(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        for v4 in range(v2):
            v5 = 0
            for v6 in range(v1):
                v5 += a1[v6][v4] ^ a1[v6][0]
            v3 += max(v5, v1 - v5) * 2 ** (v2 - 1 - v4)
        return v3
