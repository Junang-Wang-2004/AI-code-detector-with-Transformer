class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def findMedian(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        qcnt = len(queries)
        node_queries = [[] for _ in range(n)]
        for qi, (a, b) in enumerate(queries):
            node_queries[a].append(qi)
            node_queries[b].append(qi)
        uf = UF(n)
        anc = list(range(n))
        dst = [0] * n
        dep = [0] * n
        pathlen = [0] * qcnt
        lca_arr = [0] * qcnt
        vis = [False] * n

        def first_dfs(node):
            for qi in node_queries[node]:
                qa, qb = queries[qi]
                if qa == qb:
                    lca_arr[qi] = node
                    continue
                pathlen[qi] += dst[node]
                other = qa if node == qb else qb
                if vis[other]:
                    rep = uf.find(other)
                    lca_arr[qi] = anc[rep]
                    pathlen[qi] -= 2 * dst[lca_arr[qi]]
            vis[node] = True
            for nxt, wt in adj[node]:
                if vis[nxt]:
                    continue
                dst[nxt] = dst[node] + wt
                dep[nxt] = dep[node] + 1
                first_dfs(nxt)
                uf.unite(nxt, node)
                anc[uf.find(node)] = node

        first_dfs(0)

        heavy_queries = [[] for _ in range(n)]
        for qi in range(qcnt):
            u, v = queries[qi]
            du = dst[u] - dst[lca_arr[qi]]
            if 2 * du >= pathlen[qi]:
                heavy_queries[u].append((qi, 0))
            else:
                heavy_queries[v].append((qi, 1))

        res = [0] * qcnt
        cpath = []

        def bs(lo, hi, cond):
            while lo <= hi:
                md = lo + (hi - lo) // 2
                if cond(md):
                    hi = md - 1
                else:
                    lo = md + 1
            return lo

        def sec_dfs(nd):
            cpath.append(nd)
            for qi, sd in heavy_queries[nd]:
                lc = lca_arr[qi]
                ddiff = dep[nd] - dep[lc]
                D = pathlen[qi]
                if sd == 0:
                    def cond(j):
                        upnd = cpath[-(j + 1)]
                        dfrom = dst[nd] - dst[upnd]
                        return 2 * dfrom >= D
                    jpos = bs(0, ddiff, cond)
                    res[qi] = cpath[-(jpos + 1)]
                else:
                    duv = dst[queries[qi][0]] - dst[lc]
                    def cond(x):
                        nxnd = cpath[-ddiff + x]
                        dlxt = dst[nxnd] - dst[lc]
                        totcum = duv + dlxt
                        return 2 * totcum >= D
                    jpos = bs(0, ddiff - 1, cond)
                    res[qi] = cpath[-ddiff + jpos]
            for nx, _ in adj[nd]:
                if len(cpath) >= 2 and cpath[-2] == nx:
                    continue
                sec_dfs(nx)
            cpath.pop()

        sec_dfs(0)
        return res
