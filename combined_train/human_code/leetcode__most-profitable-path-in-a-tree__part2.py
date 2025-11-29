class C1(object):

    def mostProfitablePath(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            lookup[a1] = True
            v1 = 0 if len(adj[a1]) + (a1 == 0) == 1 else float('-inf')
            v2 = 0 if a1 == a2 else float('inf')
            for v3 in adj[a1]:
                if lookup[v3]:
                    continue
                v4, v5 = dfs(v3, a2 + 1)
                v1 = max(v1, v4)
                v2 = min(v2, v5)
            if a2 == v2:
                v1 += a3[a1] // 2
            elif a2 < v2:
                v1 += a3[a1]
            return (v1, v2 + 1)
        v1 = [[] for v2 in range(len(a1) + 1)]
        v3 = [False] * len(v1)
        for v4, v5 in a1:
            v1[v4].append(v5)
            v1[v5].append(v4)
        return dfs(0, 0)[0]
