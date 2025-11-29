class C1(object):
    v1 = [0]

    def numSquares(self, a1):
        """
        """
        v1 = self._num
        while len(v1) <= a1:
            v1 += (min((v1[-i * i] for v2 in range(1, int(len(v1) ** 0.5 + 1)))) + 1,)
        return v1[a1]
