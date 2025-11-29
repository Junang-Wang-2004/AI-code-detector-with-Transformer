class C1(object):

    def findMedian(self, a1, a2, a3):
        """
        """

        def dfs(a1):
            for v1 in lookup2[a1]:
                if a3[v1][0] == a3[v1][1]:
                    lca[v1] = a1
                    continue
                result[v1] += dist[a1]
                for v2 in a3[v1]:
                    if lookup[v2]:
                        lca[v1] = ancestor[uf.find_set(v2)]
                        result[v1] -= 2 * dist[lca[v1]]
            lookup[a1] = True
            for v3, v4 in adj[a1]:
                if lookup[v3]:
                    continue
                dist[v3] = dist[a1] + v4
                depth[v3] = depth[a1] + 1
                dfs(v3)
                uf.union_set(v3, a1)
                ancestor[uf.find_set(a1)] = a1

        def dfs2(a1):
            path.append(a1)
            for v1, v2 in lookup3[a1]:
                v3 = depth[a1] - depth[lca[v1]]
                if v2 == 0:
                    v4 = binary_search(0, v3, lambda x: 2 * (dist[a1] - dist[path[-(x + 1)]]) >= result[v1])
                    result2[v1] = path[-(v4 + 1)]
                else:
                    v5 = dist[a3[v1][0]] - dist[lca[v1]]
                    v4 = binary_search(0, v3 - 1, lambda x: 2 * (v5 + (dist[path[-(v3 - 1 + 1) + x]] - dist[lca[v1]])) >= result[v1])
                    result2[v1] = path[-(v3 - 1 + 1) + v4]
            for v6, v7 in adj[a1]:
                if len(path) >= 2 and path[-2] == v6:
                    continue
                dfs2(v6)
            path.pop()
        v1 = [[] for v2 in range(len(a2) + 1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [False] * len(v1)
        v7 = [[] for v2 in range(len(v1))]
        for v8, v9 in enumerate(a3):
            for v10 in v9:
                v7[v10].append(v8)
        v11 = UnionFind(len(v1))
        v12 = list(range(len(v1)))
        v13 = [0] * len(v1)
        v14 = [0] * len(v1)
        v15 = [0] * len(a3)
        v16 = [-1] * len(a3)
        dfs(0)
        v17 = [0] * len(a3)
        v18 = [[] for v2 in range(len(v1))]
        for v8, (v3, v4) in enumerate(a3):
            if 2 * (v13[v3] - v13[v16[v8]]) >= v15[v8]:
                v18[v3].append((v8, 0))
            else:
                v18[v4].append((v8, 1))
        v19 = []
        dfs2(0)
        return v17
