class Solution(object):
    def minRunesToAdd(self, n, crystals, flowFrom, flowTo):
        out_adj = [[] for _ in range(n)]
        for idx in range(len(flowFrom)):
            out_adj[flowFrom[idx]].append(flowTo[idx])
        in_adj = [[] for _ in range(n)]
        for src in range(n):
            for dst in out_adj[src]:
                in_adj[dst].append(src)
        visited = [False] * n
        post_order = []
        def dfs_first(u):
            visited[u] = True
            for v in out_adj[u]:
                if not visited[v]:
                    dfs_first(v)
            post_order.append(u)
        for i in range(n):
            if not visited[i]:
                dfs_first(i)
        visited = [False] * n
        scc_map = [-1] * n
        scc_cnt = 0
        def dfs_second(u, cid):
            visited[u] = True
            scc_map[u] = cid
            for v in in_adj[u]:
                if not visited[v]:
                    dfs_second(v, cid)
        for i in post_order[::-1]:
            if not visited[i]:
                dfs_second(i, scc_cnt)
                scc_cnt += 1
        needs_crystal = [True] * scc_cnt
        for c in crystals:
            needs_crystal[scc_map[c]] = False
        for u in range(n):
            for v in out_adj[u]:
                if scc_map[u] != scc_map[v]:
                    needs_crystal[scc_map[v]] = False
        return sum(needs_crystal)
