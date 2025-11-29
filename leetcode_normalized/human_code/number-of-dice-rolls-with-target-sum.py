class C1(object):

    def numRollsToTarget(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0 for v3 in range(a3 + 1)] for v3 in range(2)]
        v2[0][0] = 1
        for v4 in range(1, a1 + 1):
            v2[v4 % 2] = [0 for v3 in range(a3 + 1)]
            for v5 in range(1, a2 + 1):
                for v6 in range(v5, a3 + 1):
                    v2[v4 % 2][v6] = (v2[v4 % 2][v6] + v2[(v4 - 1) % 2][v6 - v5]) % v1
        return v2[a1 % 2][a3] % v1
