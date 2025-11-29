class Solution:
    def treeQueries(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for a, b, c in edges:
            a -= 1
            b -= 1
            adj[a].append((b, c))
            adj[b].append((a, c))
        entry = [0] * n
        exitt = [0] * n
        depths = [0] * n
        par_edge = [0] * n
        time_counter = [0]
        def dfs(u, p, d):
            entry[u] = time_counter[0]
            time_counter[0] += 1
            depths[u] = d
            for v, w in adj[u]:
                if v == p:
                    continue
                par_edge[v] = w
                dfs(v, u, d + w)
            exitt[u] = time_counter[0]
        dfs(0, -1, 0)
        ft = [0] * (n + 2)
        def ft_update(idx, val):
            idx += 1
            while idx <= n:
                ft[idx] += val
                idx += idx & -idx
        def ft_query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res += ft[idx]
                idx -= idx & -idx
            return res
        result = []
        for q in queries:
            if q[0] == 1:
                _, uu, vv, ww = q
                u = uu - 1
                v = vv - 1
                if entry[u] > entry[v]:
                    u, v = v, u
                diff = ww - par_edge[v]
                ft_update(entry[v], diff)
                ft_update(exitt[v], -diff)
                par_edge[v] = ww
            else:
                _, x = q
                x -= 1
                result.append(depths[x] + ft_query(entry[x]))
        return result
