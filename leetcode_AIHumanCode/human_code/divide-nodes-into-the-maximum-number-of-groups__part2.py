# Time:  O(n^2)
# Space: O(n)
# bfs
class Solution2(object):
    def magnificentSets(self, n, edges):
        """
        """
        def bfs(u):
            group = []
            q = [u]
            lookup[u] = True
            while q:
                new_q = []
                for u in q:
                    group.append(u)
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return group
    
        def bfs2(u):
            result = 0
            lookup = [False]*n
            q = {u}
            lookup[u] = True
            while q:
                new_q = set()
                for u in q:
                    for v in adj[u]:
                        if v in q:
                            return 0
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.add(v)
                q = new_q
                result += 1
            return result
    
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        result = 0
        lookup = [0]*n
        for u in range(n):
            if lookup[u]:
                continue
            group = bfs(u)
            mx = 0
            for u in group:
                d = bfs2(u)
                if d == 0:
                    return -1
                mx = max(mx, d)
            result += mx
        return result
