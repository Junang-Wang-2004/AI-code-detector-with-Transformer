# Time:  O(nlogn)
# Space: O(n)
# dfs, fenwick tree
class Solution2(object):
    def treeQueries(self, n, edges, queries):
        """
        """
        def dfs(u, p, d):
            L[u] = cnt[0]
            cnt[0] += 1
            dist[u] = d
            for v, w in adj[u]:
                if v == p:
                    continue
                lookup[v] = w
                dfs(v, u, d+w)
            R[u] = cnt[0]

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            u -= 1
            v -= 1
            adj[u].append((v, w))
            adj[v].append((u, w))
        L, R, dist, lookup = [0]*n, [0]*n, [0]*n, [0]*n
        cnt = [0]
        dfs(0, -1, 0)
        bit = BIT(n)
        result = []
        for q in queries:
            if q[0] == 1:
                _, u, v, w = q
                u -= 1
                v -= 1
                if L[u] > L[v]:
                    u, v = v, u 
                diff = w-lookup[v]
                bit.add(L[v], diff)
                bit.add(R[v], -diff)
                lookup[v] = w
            else:
                _, x = q
                x -= 1
                result.append(dist[x]+bit.query(L[x]))
        return result
