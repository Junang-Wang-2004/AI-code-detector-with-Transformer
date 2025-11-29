class C1(object):

    def finalPositionOfSnake(self, a1, a2):
        """
        """
        v1 = {'UP': (-1, 0), 'RIGHT': (0, 1), 'DOWN': (1, 0), 'LEFT': (0, -1)}
        v2 = v3 = 0
        for v4 in a2:
            v5, v6 = v1[v4]
            v2, v3 = (v2 + v5, v3 + v6)
        return v2 * a1 + v3
