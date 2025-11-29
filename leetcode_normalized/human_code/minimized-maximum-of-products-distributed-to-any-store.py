class C1(object):

    def minimizedMaximum(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + (a2 - 1)) // a2

        def check(a1, a2, a3):
            return sum((ceil_divide(q, a3) for v1 in a2)) <= a1
        v1, v2 = (1, max(a2))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
