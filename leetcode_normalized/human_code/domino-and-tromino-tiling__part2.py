class C1(object):

    def numTilings(self, a1):
        """
        """
        v1 = int(1000000000.0 + 7)
        v2 = [1, 1, 2]
        for v3 in range(3, a1 + 1):
            v2[v3 % 3] = (2 * v2[(v3 - 1) % 3] % v1 + v2[(v3 - 3) % 3]) % v1
        return v2[a1 % 3]
