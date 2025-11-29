class C1(object):

    def countDistinctIntegers(self, a1):
        """
        """

        def reverse(a1):
            v1 = 0
            while a1:
                v1 = v1 * 10 + a1 % 10
                a1 //= 10
            return v1
        return len({y for v1 in a1 for v2 in (v1, reverse(v1))})
