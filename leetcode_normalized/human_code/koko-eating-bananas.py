class C1(object):

    def minEatingSpeed(self, a1, a2):
        """
        """

        def possible(a1, a2, a3):
            return sum(((pile - 1) // a3 + 1 for v1 in a1)) <= a2
        v1, v2 = (1, max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if possible(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
