class C1(object):

    def sumOfSquares(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, int(len(a1) ** 0.5) + 1):
            if len(a1) % v2:
                continue
            v1 += a1[v2 - 1] ** 2
            if len(a1) // v2 != v2:
                v1 += a1[len(a1) // v2 - 1] ** 2
        return v1
