class C1(object):

    def maxScore(self, a1):
        """
        """

        def dfs(a1):
            if not adj[a1]:
                return (0, 0)
            v1 = [dfs(v) for v2, v3 in adj[a1]]
            v4 = sum((max(with_v, without_v) for v5, v6 in v1))
            v7 = max((v4 - max(v5, v6) + (v6 + adj[a1][i][1]) for v8, (v5, v6) in enumerate(v1)))
            return (v7, v4)
        v1 = [[] for v2 in range(len(a1))]
        for v3, (v4, v5) in enumerate(a1):
            if v3 == 0:
                continue
            v1[v4].append((v3, v5))
        return max(dfs(0))
