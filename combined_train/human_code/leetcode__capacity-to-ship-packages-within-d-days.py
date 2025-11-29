class C1(object):

    def shipWithinDays(self, a1, a2):
        """
        """

        def possible(a1, a2, a3):
            v1, v2 = (1, 0)
            for v3 in a1:
                if v2 + v3 > a3:
                    v1 += 1
                    v2 = 0
                v2 += v3
            return v1 <= a2
        v1, v2 = (max(a1), sum(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if possible(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
