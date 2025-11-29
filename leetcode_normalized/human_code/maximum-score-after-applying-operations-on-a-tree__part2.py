class C1(object):

    def maximumScoreAfterOperations(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if len(adj[a1]) == (1 if a1 else 0):
                return a2[a1]
            return min(sum((dfs(v, a1) for v1 in adj[a1] if v1 != a2)), a2[a1])
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return sum(a2) - dfs(0, -1)
