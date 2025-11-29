class C1(object):

    def minOperations(self, a1, a2, a3):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def check(a1):
            return sum((ceil_divide(max(v - min(ceil_divide(v, a3), a1) * a3, 0), a2 - a3) for v1 in a1)) <= a1
        v1, v2 = (1, ceil_divide(max(a1), a3))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
