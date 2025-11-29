class C1(object):

    def maxValue(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4):
            v1 = max(a4 - a2, 0)
            v2 = (a4 + v1) * (a4 - v1 + 1) // 2
            v1 = max(a4 - (a1 - 1 - a2), 0)
            v2 += (a4 + v1) * (a4 - v1 + 1) // 2
            return v2 - a4 <= a3
        a3 -= a1
        v2, v3 = (0, a3)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if not check(a1, a2, a3, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return 1 + v3
