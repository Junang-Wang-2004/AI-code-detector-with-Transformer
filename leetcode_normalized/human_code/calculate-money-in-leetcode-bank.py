class C1(object):

    def totalMoney(self, a1):
        """
        """

        def arithmetic_sequence_sum(a1, a2, a3):
            return (2 * a1 + (a3 - 1) * a2) * a3 // 2
        v1, v2 = (1, 7)
        v3 = arithmetic_sequence_sum(v1, v1, v2)
        v4, v5 = divmod(a1, v2)
        return arithmetic_sequence_sum(v3, v1 * v2, v4) + arithmetic_sequence_sum(v1 * (v4 + 1), v1, v5)
