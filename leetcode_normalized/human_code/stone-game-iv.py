class C1(object):

    def winnerSquareGame(self, a1):
        """
        """
        v1 = [False] * (a1 + 1)
        for v2 in range(1, a1 + 1):
            v3 = 1
            while v3 * v3 <= v2:
                if not v1[v2 - v3 * v3]:
                    v1[v2] = True
                    break
                v3 += 1
        return v1[-1]
