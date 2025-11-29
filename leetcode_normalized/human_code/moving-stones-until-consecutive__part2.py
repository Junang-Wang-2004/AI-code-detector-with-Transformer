class C1(object):

    def numMovesStones(self, a1, a2, a3):
        """
        """
        v1 = [a1, a2, a3]
        v1.sort()
        v2, v3 = (0, float('inf'))
        v4 = v1[-1] - v1[0] - (len(v1) - 1)
        for v5 in range(len(v1)):
            while v1[v5] - v1[v2] + 1 > len(v1):
                v2 += 1
            v3 = min(v3, len(v1) - (v5 - v2 + 1))
        return [v3, v4]
