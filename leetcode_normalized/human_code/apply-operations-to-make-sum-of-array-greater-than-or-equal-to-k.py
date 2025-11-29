class C1(object):

    def minOperations(self, a1):
        """
        """

        def isqrt(a1):
            v1, v2 = (a1, (a1 + 1) // 2)
            while v2 < v1:
                v1, v2 = (v2, (v2 + a1 // v2) // 2)
            return v1

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = isqrt(a1)
        return v1 - 1 + (ceil_divide(a1, v1) - 1)
