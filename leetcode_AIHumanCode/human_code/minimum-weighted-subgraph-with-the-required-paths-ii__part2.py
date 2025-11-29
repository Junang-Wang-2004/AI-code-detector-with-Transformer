# Time:  O(n + q)
# Space: O(n + q)
# dfs, Tarjan's Offline LCA Algorithm
class Solution2(object):
    def minimumWeight(self, edges, queries):
        """
        """
        def dfs(u):
            for i in lookup2[u]:
                result[i] += dist[u]
                for x in queries[i]:
                    if lookup[x]:
                        result[i] -= dist[ancestor[uf.find_set(x)]]
            lookup[u] = True
            for v, w in adj[u]:
                if lookup[v]:
                    continue
                dist[v] = dist[u]+w
                dfs(v)
                uf.union_set(v, u)
                ancestor[uf.find_set(u)] = u
            
        adj = [[] for _ in range(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        lookup = [False]*len(adj)
        lookup2 = [[] for _ in range(len(adj))]
        for i, q in enumerate(queries):
            for x in q:
                lookup2[x].append(i)
        uf = UnionFind(len(adj))
        ancestor = list(range(len(adj)))
        dist = [0]*len(adj)
        result = [0]*len(queries)
        dfs(0)
        return result
