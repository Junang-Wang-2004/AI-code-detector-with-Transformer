class C1(object):

    def smallestIndex(self, a1):
        """
        """

        def total(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1
        return next((i for v1, v2 in enumerate(a1) if total(v2) == v1), -1)
