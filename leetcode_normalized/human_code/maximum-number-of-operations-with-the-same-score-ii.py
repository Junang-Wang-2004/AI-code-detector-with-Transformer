class C1(object):

    def maxOperations(self, a1):
        """
        """

        def memoization(a1, a2, a3, a4):
            if not a2 - a1 + 1 >= 2:
                return 0
            if a4[a1][a2] == -1:
                a4[a1][a2] = max(1 + memoization(a1 + 2, a2 - 0, a3, a4) if a1[a1] + a1[a1 + 1] == a3 else 0, 1 + memoization(a1 + 1, a2 - 1, a3, a4) if a1[a1] + a1[a2] == a3 else 0, 1 + memoization(a1 + 0, a2 - 2, a3, a4) if a1[a2 - 1] + a1[a2] == a3 else 0)
            return a4[a1][a2]
        return max((memoization(0, len(a1) - 1, target, [[-1] * len(a1) for v1 in range(len(a1))]) for v2 in {a1[0] + a1[1], a1[0] + a1[-1], a1[-2] + a1[-1]}))
