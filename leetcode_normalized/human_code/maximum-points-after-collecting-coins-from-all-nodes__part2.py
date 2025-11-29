class C1(object):

    def maximumPoints(self, a1, a2, a3):
        """
        """

        def memoization(a1, a2, a3):
            if a3 >= max_d:
                return 0
            if lookup[a1][a3] is None:
                lookup[a1][a3] = max((a2[a1] >> a3) - a3 + sum((memoization(v, a1, a3) for v1 in adj[a1] if v1 != a2)), (a2[a1] >> a3 + 1) + sum((memoization(v1, a1, a3 + 1) for v1 in adj[a1] if v1 != a2)))
            return lookup[a1][a3]
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = max(a2).bit_length()
        v6 = [[None] * v5 for v2 in range(len(a2))]
        return memoization(0, -1, 0)
