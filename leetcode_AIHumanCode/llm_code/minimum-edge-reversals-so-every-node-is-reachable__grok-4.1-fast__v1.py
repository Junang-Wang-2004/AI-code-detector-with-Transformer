class Solution:
    def minEdgeReversals(self, n, edges):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append((b, 0))
            g[b].append((a, 1))
        
        def get_total(u, p):
            s = 0
            for v, c in g[u]:
                if v != p:
                    s += c + get_total(v, u)
            return s
        
        res = [0] * n
        root_val = get_total(0, -1)
        res[0] = root_val
        
        def reroot(u, p, val):
            for v, c in g[u]:
                if v != p:
                    res[v] = val - c + 1 - c
                    reroot(v, u, res[v])
        
        reroot(0, -1, root_val)
        return res
