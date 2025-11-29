class C1(object):

    def maxIncreasingGroups(self, a1):
        """
        """

        def check(a1):
            v1 = 0
            for v2 in range(a1):
                v1 += a1[~v2] - (a1 - v2)
                v1 = min(v1, 0)
            for v2 in range(len(a1) - a1):
                v1 += a1[v2]
            return v1 >= 0
        a1.sort()
        v1, v2 = (1, len(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
