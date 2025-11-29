class C1(object):

    def maxRunTime(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            return sum((min(b, a3) for v1 in a2)) >= a1 * a3
        v1, v2 = (min(a2), sum(a2) // a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
