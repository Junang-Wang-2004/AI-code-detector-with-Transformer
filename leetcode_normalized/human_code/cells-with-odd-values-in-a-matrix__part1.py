class C1(object):

    def oddCells(self, a1, a2, a3):
        """
        """
        v1, v2 = ([0] * a1, [0] * a2)
        for v3, v4 in a3:
            v1[v3] ^= 1
            v2[v4] ^= 1
        v5, v6 = (sum(v1), sum(v2))
        return v5 * a2 + v6 * a1 - 2 * v5 * v6
