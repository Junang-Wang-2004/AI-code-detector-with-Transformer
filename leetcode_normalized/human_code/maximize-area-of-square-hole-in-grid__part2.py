class C1(object):

    def maximizeSquareHoleArea(self, a1, a2, a3, a4):
        """
        """

        def max_gap(a1):
            a1.sort()
            v1 = v2 = 1
            for v3 in range(len(a1)):
                v2 += 1
                v1 = max(v1, v2)
                if v3 + 1 != len(a1) and a1[v3 + 1] != a1[v3] + 1:
                    v2 = 1
            return v1
        return min(max_gap(a3), max_gap(a4)) ** 2
