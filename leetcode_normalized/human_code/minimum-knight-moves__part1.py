class C1(object):

    def minKnightMoves(self, a1, a2):
        """
        """
        a1, a2 = (abs(a1), abs(a2))
        if a1 < a2:
            a1, a2 = (a2, a1)
        v3 = {(1, 0): 3, (2, 2): 4}
        if (a1, a2) in v3:
            return v3[a1, a2]
        v4 = a1 - a2
        if a2 > v4:
            return v4 - 2 * ((v4 - a2) // 3)
        return v4 - 2 * ((v4 - a2) // 4)
