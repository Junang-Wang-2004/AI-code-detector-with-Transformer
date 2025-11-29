class C1(object):

    def waysToReachTarget(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 + 1)
        v2[0] = 1
        for v3, v4 in a2:
            v5 = [0] * (a1 + 1)
            for v6 in range(a1 + 1):
                for v7 in range(min((a1 - v6) // v4, v3) + 1):
                    v5[v6 + v7 * v4] = (v5[v6 + v7 * v4] + v2[v6]) % v1
            v2 = v5
        return v2[-1]
