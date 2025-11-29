class C1(object):

    def minimumSum(self, a1, a2):
        """
        """

        def arithmetic_progression_sum(a1, a2, a3):
            return (a1 + (a1 + (a3 - 1) * a2)) * a3 // 2
        v1 = min(a2 // 2, a1)
        v2 = a1 - v1
        return arithmetic_progression_sum(1, 1, v1) + arithmetic_progression_sum(a2, 1, v2)
