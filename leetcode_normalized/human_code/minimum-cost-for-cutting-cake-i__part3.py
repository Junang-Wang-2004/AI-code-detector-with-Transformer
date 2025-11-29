class C1(object):

    def minimumCost(self, a1, a2, a3, a4):
        """
        """

        def memoization(a1, a2, a3, a4):
            if (a1, a2) == (a3, a4):
                return 0
            if lookup[a1][a2][a3][a4] == -1:
                v1 = float('inf')
                for v2 in range(a1, a3):
                    v1 = min(ret, memoization(a1, a2, v2, a4) + memoization(v2 + 1, a2, a3, a4) + a3[v2])
                for v3 in range(a2, a4):
                    v1 = min(ret, memoization(a1, a2, a3, v3) + memoization(a1, v3 + 1, a3, a4) + a4[v3])
                lookup[a1][a2][a3][a4] = v1
            return lookup[a1][a2][a3][a4]
        v1 = [[[[-1] * a2 for v2 in range(a1)] for v2 in range(a2)] for v2 in range(a1)]
        return memoization(0, 0, a1 - 1, a2 - 1)
