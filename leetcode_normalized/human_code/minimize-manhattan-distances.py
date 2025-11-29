class C1(object):

    def minimumDistance(self, a1):
        """
        """

        def max_distance(a1):
            v1 = max(((x + y, i) for v2, (v3, v4) in enumerate(a1) if v2 != a1))
            v5 = min(((v3 + v4, v2) for v2, (v3, v4) in enumerate(a1) if v2 != a1))
            v6 = max(((v3 - v4, v2) for v2, (v3, v4) in enumerate(a1) if v2 != a1))
            v7 = min(((v3 - v4, v2) for v2, (v3, v4) in enumerate(a1) if v2 != a1))
            return max((v1[0] - v5[0], v1[1], v5[1]), (v6[0] - v7[0], v6[1], v7[1]))
        v1, v2, v3 = max_distance(-1)
        return min(max_distance(v2)[0], max_distance(v3)[0])
