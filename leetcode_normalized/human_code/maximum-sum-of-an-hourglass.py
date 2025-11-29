class C1(object):

    def maxSum(self, a1):
        """
        """

        def total(a1, a2):
            return a1[a1][a2] + a1[a1][a2 + 1] + a1[a1][a2 + 2] + a1[a1 + 1][a2 + 1] + a1[a1 + 2][a2] + a1[a1 + 2][a2 + 1] + a1[a1 + 2][a2 + 2]
        return max((total(i, j) for v1 in range(len(a1) - 2) for v2 in range(len(a1[0]) - 2)))
