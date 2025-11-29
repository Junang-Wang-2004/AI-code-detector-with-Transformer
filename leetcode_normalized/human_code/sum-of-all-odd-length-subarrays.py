class C1(object):

    def sumOddLengthSubarrays(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + (a2 - 1)) // a2
        return sum((x * ceil_divide((i - 0 + 1) * (len(a1) - 1 - i + 1), 2) for v1, v2 in enumerate(a1)))
