class C1(object):

    def distinctPoints(self, a1, a2):
        """
        """
        v1 = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        v2 = v3 = 0
        v4 = {(v2, v3)}
        for v5 in range(a2, len(a1)):
            v2 += v1[a1[v5]][0] - v1[a1[v5 - a2]][0]
            v3 += v1[a1[v5]][1] - v1[a1[v5 - a2]][1]
            v4.add((v2, v3))
        return len(v4)
