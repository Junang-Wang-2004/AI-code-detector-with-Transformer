class C1(object):

    def findKthPositive(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            return a1[a3] - (a3 + 1) < a2
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2 + 1 + a2
