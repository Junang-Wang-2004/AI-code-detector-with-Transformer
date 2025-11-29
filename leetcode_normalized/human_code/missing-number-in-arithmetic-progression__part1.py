class C1(object):

    def missingNumber(self, a1):
        """
        """

        def check(a1, a2, a3):
            return a1[a3] != a1[0] + a2 * a3
        v1 = (a1[-1] - a1[0]) // len(a1)
        v2, v3 = (0, len(a1) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(a1, v1, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return a1[0] + v1 * v2
