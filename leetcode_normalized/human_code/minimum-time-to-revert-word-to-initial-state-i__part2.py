class C1(object):

    def minimumTimeToInitialState(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        for v1 in range(a2, len(a1), a2):
            if all((a1[v1 + j] == a1[j] for v2 in range(len(a1) - v1))):
                return v1 // a2
        return ceil_divide(len(a1), a2)
