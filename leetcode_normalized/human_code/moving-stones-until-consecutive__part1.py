class C1(object):

    def numMovesStones(self, a1, a2, a3):
        """
        """
        v1 = [a1, a2, a3]
        v1.sort()
        if v1[0] + 1 == v1[1] and v1[1] + 1 == v1[2]:
            return [0, 0]
        return [1 if v1[0] + 2 >= v1[1] or v1[1] + 2 >= v1[2] else 2, v1[2] - v1[0] - 2]
