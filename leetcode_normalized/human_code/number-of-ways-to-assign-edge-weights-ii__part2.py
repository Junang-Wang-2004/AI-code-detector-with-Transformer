class C1(object):

    def assignEdgeWeights(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def dfs(a1):
            for v1 in lookup2[a1]:
                if a2[v1][0] == a2[v1][1]:
                    continue
                result[v1] += dist[a1]
                for v2 in a2[v1]:
                    if lookup[v2 - 1]:
                        result[v1] -= 2 * dist[ancestor[uf.find_set(v2 - 1)]]
            lookup[a1] = True
            for v3 in adj[a1]:
                if lookup[v3]:
                    continue
                dist[v3] = dist[a1] + 1
                dfs(v3)
                uf.union_set(v3, a1)
                ancestor[uf.find_set(a1)] = a1
        v2 = [[] for v3 in range(len(a1) + 1)]
        for v4, v5 in a1:
            v2[v4 - 1].append(v5 - 1)
            v2[v5 - 1].append(v4 - 1)
        v6 = [False] * len(v2)
        v7 = [[] for v3 in range(len(v2))]
        for v8, v9 in enumerate(a2):
            for v10 in v9:
                v7[v10 - 1].append(v8)
        v11 = UnionFind(len(v2))
        v12 = list(range(len(v2)))
        v13 = [0] * len(v2)
        v14 = [0] * len(a2)
        dfs(0)
        v15 = [1] * (len(v2) - 1)
        for v8 in range(len(v15) - 1):
            v15[v8 + 1] = v15[v8] * 2 % v1
        return [v15[v10 - 1] if v10 - 1 >= 0 else 0 for v10 in v14]
