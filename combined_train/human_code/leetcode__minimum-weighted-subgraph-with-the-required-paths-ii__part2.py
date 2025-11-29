class C1(object):

    def minimumWeight(self, a1, a2):
        """
        """

        def dfs(a1):
            for v1 in lookup2[a1]:
                result[v1] += dist[a1]
                for v2 in a2[v1]:
                    if lookup[v2]:
                        result[v1] -= dist[ancestor[uf.find_set(v2)]]
            lookup[a1] = True
            for v3, v4 in adj[a1]:
                if lookup[v3]:
                    continue
                dist[v3] = dist[a1] + v4
                dfs(v3)
                uf.union_set(v3, a1)
                ancestor[uf.find_set(a1)] = a1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [False] * len(v1)
        v7 = [[] for v2 in range(len(v1))]
        for v8, v9 in enumerate(a2):
            for v10 in v9:
                v7[v10].append(v8)
        v11 = UnionFind(len(v1))
        v12 = list(range(len(v1)))
        v13 = [0] * len(v1)
        v14 = [0] * len(a2)
        dfs(0)
        return v14
