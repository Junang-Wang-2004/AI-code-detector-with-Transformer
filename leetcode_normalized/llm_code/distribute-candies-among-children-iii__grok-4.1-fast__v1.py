class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        v1 = a2 + 1

        def count_ways(a1):
            return 0 if a1 < 0 else (a1 + 1) * (a1 + 2) // 2
        v2 = count_ways(a1)
        v3 = 3 * count_ways(a1 - v1)
        v4 = 3 * count_ways(a1 - 2 * v1)
        v5 = count_ways(a1 - 3 * v1)
        return v2 - v3 + v4 - v5
