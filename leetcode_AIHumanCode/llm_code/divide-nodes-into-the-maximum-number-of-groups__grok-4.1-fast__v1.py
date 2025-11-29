class Solution:
    def magnificentSets(self, n, edges):
        graph = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            graph[x].append(y)
            graph[y].append(x)
        vis = [False] * n
        col = [-1] * n
        ans = 0
        for i in range(n):
            if vis[i]:
                continue
            comp = []
            q = [i]
            vis[i] = True
            col[i] = 0
            comp.append(i)
            bip = True
            qi = 0
            while qi < len(q) and bip:
                u = q[qi]
                qi += 1
                for v in graph[u]:
                    if col[v] == -1:
                        col[v] = 1 - col[u]
                        vis[v] = True
                        q.append(v)
                        comp.append(v)
                    elif col[v] == col[u]:
                        bip = False
            if not bip:
                return -1
            max_lev = 0
            for s in comp:
                lev_vis = [False] * n
                qq = [s]
                lev_vis[s] = True
                lev = 0
                while qq:
                    new_qq = []
                    for u in qq:
                        for v in graph[u]:
                            if not lev_vis[v]:
                                lev_vis[v] = True
                                new_qq.append(v)
                    qq = new_qq
                    if qq:
                        lev += 1
                max_lev = max(max_lev, lev + 1)
            ans += max_lev
        return ans
