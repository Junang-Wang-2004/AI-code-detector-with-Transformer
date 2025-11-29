class C1(object):

    def maximizeSquareHoleArea(self, a1, a2, a3, a4):
        """
        """

        def max_gap(a1):
            v1 = v2 = 1
            v3 = set(a1)
            while v3:
                v4 = next(iter(v3))
                v5 = v4
                while v5 - 1 in v3:
                    v5 -= 1
                v6 = v4
                while v6 + 1 in v3:
                    v6 += 1
                for v7 in range(v5, v6 + 1):
                    v3.remove(v7)
                v1 = max(v1, v6 - v5 + 1 + 1)
            return v1
        return min(max_gap(a3), max_gap(a4)) ** 2
