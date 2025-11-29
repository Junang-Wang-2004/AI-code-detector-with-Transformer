class C1(object):

    def minSensors(self, a1, a2, a3):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        return ceil_divide(a1, 2 * a3 + 1) * ceil_divide(a2, 2 * a3 + 1)
