class C1(object):

    def minimumPushes(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        return sum(((i + 1) * min(len(a1) - i * (9 - 2 + 1), 9 - 2 + 1) for v1 in range(ceil_divide(len(a1), 9 - 2 + 1))))
