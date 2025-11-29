class C1(object):

    def waysToReachTarget(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 + 1)
        v2[0] = 1
        for v3, v4 in a2:
            for v5 in reversed(range(1, a1 + 1)):
                for v6 in range(1, min(v5 // v4, v3) + 1):
                    v2[v5] = (v2[v5] + v2[v5 - v6 * v4]) % v1
        return v2[-1]
