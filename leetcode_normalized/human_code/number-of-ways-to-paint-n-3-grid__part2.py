class C1(object):

    def numOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (6, 6)
        for v4 in range(a1 - 1):
            v2, v3 = ((3 * v2 % v1 + 2 * v3 % v1) % v1, (2 * v3 % v1 + 2 * v2 % v1) % v1)
        return (v2 + v3) % v1
