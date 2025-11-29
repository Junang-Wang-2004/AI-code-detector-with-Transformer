class C1(object):

    def minimumOperations(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = max(a1)
        v2 = [0] * v1
        for v3 in reversed(range(len(a1))):
            v2[a1[v3] - 1] += 1
            if v2[a1[v3] - 1] == 2:
                return ceil_divide(v3 + 1, 3)
        return 0
