class C1(object):

    def minimumWhiteTiles(self, a1, a2, a3):
        """
        """
        v1 = [[0] * (a2 + 1) for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(v1)):
            v1[v3][0] = v1[v3 - 1][0] + int(a1[v3 - 1])
            for v4 in range(1, a2 + 1):
                v1[v3][v4] = min(v1[v3 - 1][v4] + int(a1[v3 - 1]), v1[max(v3 - a3, 0)][v4 - 1])
        return v1[-1][-1]
