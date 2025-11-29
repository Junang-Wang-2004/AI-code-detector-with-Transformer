# Time:  O(n + q)
# Space: O(n + q)
# dfs, Tarjan's Offline LCA Algorithm, combinatorics
class Solution2(object):
    def assignEdgeWeights(self, edges, queries):
        """
        """
        MOD = 10**9+7
        def dfs(u):
            for i in lookup2[u]:
                if queries[i][0] == queries[i][1]:
                    continue
                result[i] += dist[u]
                for x in queries[i]:
                    if lookup[x-1]:
                        result[i] -= 2*dist[ancestor[uf.find_set(x-1)]]
            lookup[u] = True
            for v in adj[u]:
                if lookup[v]:
                    continue
                dist[v] = dist[u]+1
                dfs(v)
                uf.union_set(v, u)
                ancestor[uf.find_set(u)] = u
            
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        lookup = [False]*len(adj)
        lookup2 = [[] for _ in range(len(adj))]
        for i, q in enumerate(queries):
            for x in q:
                lookup2[x-1].append(i)
        uf = UnionFind(len(adj))
        ancestor = list(range(len(adj)))
        dist = [0]*len(adj)
        result = [0]*len(queries)
        dfs(0)
        POW2 = [1]*(len(adj)-1)
        for i in range(len(POW2)-1):
            POW2[i+1] = (POW2[i]*2)%MOD
        return [POW2[x-1] if x-1 >= 0 else 0 for x in result]
