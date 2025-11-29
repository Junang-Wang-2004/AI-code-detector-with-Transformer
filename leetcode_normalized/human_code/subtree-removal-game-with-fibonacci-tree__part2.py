class C1(object):

    def findGameWinner(self, a1):
        """
        """
        v1 = [0, 1]
        for v2 in range(2, a1):
            v1[v2 % 2] = v1[(v2 - 1) % 2] + 1 ^ v1[(v2 - 2) % 2] + 1
        return v1[(a1 - 1) % 2] > 0
