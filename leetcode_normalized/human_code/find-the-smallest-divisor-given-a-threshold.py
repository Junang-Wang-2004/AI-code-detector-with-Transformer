class C1(object):

    def smallestDivisor(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            return sum(((i - 1) // a2 + 1 for v1 in a1)) <= a3
        v1, v2 = (1, max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, v3, a2):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
