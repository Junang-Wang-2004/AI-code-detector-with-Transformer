class C1(object):

    def numMovesStones(self, a1, a2, a3):
        v1 = min(a1, a2, a3)
        v2 = max(a1, a2, a3)
        v3 = a1 + a2 + a3 - v1 - v2
        v4 = v2 - v1 - 2
        if v2 - v1 == 2:
            return [0, v4]
        if v3 - v1 <= 2 or v2 - v3 <= 2:
            return [1, v4]
        return [2, v4]
