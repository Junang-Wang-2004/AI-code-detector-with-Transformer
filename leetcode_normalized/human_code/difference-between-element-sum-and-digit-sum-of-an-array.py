class C1(object):

    def differenceOfSum(self, a1):
        """
        """

        def total(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1
        return abs(sum(a1) - sum((total(x) for v1 in a1)))
