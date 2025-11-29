class C1(object):

    def reconstructMatrix(self, a1, a2, a3):
        """
        """
        v1, v2 = ([0] * len(a3), [0] * len(a3))
        for v3 in range(len(a3)):
            v1[v3] = int(a1 > 0 and a3[v3] != 0)
            v2[v3] = a3[v3] - v1[v3]
            a1 -= v1[v3]
            a2 -= v2[v3]
        return [v1, v2] if a1 == a2 == 0 else []
