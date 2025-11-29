class C1(object):

    def smallestDistancePair(self, a1, a2):
        """
        """

        def possible(a1, a2, a3):
            v1, v2 = (0, 0)
            for v3, v4 in enumerate(a2):
                while v4 - a2[v2] > a1:
                    v2 += 1
                v1 += v3 - v2
            return v1 >= a3
        a1.sort()
        v1, v2 = (0, a1[-1] - a1[0] + 1)
        while v1 < v2:
            v3 = v1 + (v2 - v1) / 2
            if possible(v3, a1, a2):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
