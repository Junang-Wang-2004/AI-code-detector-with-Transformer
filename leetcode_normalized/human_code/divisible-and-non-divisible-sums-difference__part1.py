class C1(object):

    def differenceOfSums(self, a1, a2):
        """
        """

        def arithmetic_progression_sum(a1, a2, a3):
            return (a1 + (a1 + (a3 - 1) * a2)) * a3 // 2
        return arithmetic_progression_sum(1, 1, a1) - 2 * arithmetic_progression_sum(a2, a2, a1 // a2)
