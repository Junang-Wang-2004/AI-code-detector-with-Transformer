class C1(object):

    def minEdgeReversals(self, a1, a2):
        """
        """

        def dfs1(a1, a2):
            return sum((adj[a1][v] + dfs1(v, a1) for v1 in adj[a1] if v1 != a2))

        def dfs2(a1, a2):
            result[a1] = a2
            for v1 in adj[a1]:
                if result[v1] == -1:
                    dfs2(v1, a2 - adj[a1][v1] + adj[v1][a1])
        v1 = collections.defaultdict(dict)
        for v2, v3 in a2:
            v1[v2][v3] = 0
            v1[v3][v2] = 1
        v4 = [-1] * a1
        dfs2(0, dfs1(0, -1))
        return v4
