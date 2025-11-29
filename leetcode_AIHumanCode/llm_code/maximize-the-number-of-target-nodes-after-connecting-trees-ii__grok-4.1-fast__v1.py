class Solution:
    def maxTargetNodes(self, edges1, edges2):
        def build_graph(es):
            n = len(es) + 1
            g = [[] for _ in range(n)]
            for x, y in es:
                g[x].append(y)
                g[y].append(x)
            return g

        def max_partite(g):
            n = len(g)
            col = [-1] * n
            col[0] = 0
            sz_even = 1
            sz_odd = 0
            qu = [0]
            while qu:
                nxt = []
                for node in qu:
                    for nei in g[node]:
                        if col[nei] == -1:
                            col[nei] = 1 ^ col[node]
                            if col[nei] == 0:
                                sz_even += 1
                            else:
                                sz_odd += 1
                            nxt.append(nei)
                qu = nxt
            return max(sz_even, sz_odd)

        def get_parts(g):
            n = len(g)
            col = [-1] * n
            col[0] = 0
            sz_even = 1
            sz_odd = 0
            qu = [0]
            while qu:
                nxt = []
                for node in qu:
                    for nei in g[node]:
                        if col[nei] == -1:
                            col[nei] = 1 ^ col[node]
                            if col[nei] == 0:
                                sz_even += 1
                            else:
                                sz_odd += 1
                            nxt.append(nei)
                qu = nxt
            parts = []
            for i in range(n):
                if col[i] == 0:
                    parts.append(sz_even)
                else:
                    parts.append(sz_odd)
            return parts

        g2 = build_graph(edges2)
        biggest2 = max_partite(g2)
        g1 = build_graph(edges1)
        parts1 = get_parts(g1)
        return [biggest2 + p for p in parts1]
