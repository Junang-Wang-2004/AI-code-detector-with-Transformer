class C1(object):

    def minimumFuelCost(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def dfs(a1, a2, a3):
            v1 = 1 + sum((dfs(v, a1, a3 + 1) for v2 in adj[a1] if v2 != a2))
            if a3:
                result[0] += ceil_divide(v1, a2)
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]
        dfs(0, -1, 0)
        return v5[0]
