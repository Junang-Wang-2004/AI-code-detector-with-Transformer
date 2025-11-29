class C1(object):

    def findMinMoves(self, a1):
        """
        """
        v1 = sum(a1)
        if v1 % len(a1):
            return -1
        v2, v3, v4 = (0, v1 / len(a1), 0)
        for v5 in a1:
            v4 += v5 - v3
            v2 = max(v2, max(v5 - v3, abs(v4)))
        return v2
