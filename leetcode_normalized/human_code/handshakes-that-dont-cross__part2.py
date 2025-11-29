class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 // 2 + 1)
        v2[0] = 1
        for v3 in range(1, a1 // 2 + 1):
            for v4 in range(v3):
                v2[v3] = (v2[v3] + v2[v4] * v2[v3 - 1 - v4]) % v1
        return v2[a1 // 2]
