# Time:  O(t * n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        """
        def dfs(u, p, target):
            lookup[u] += 1
            if u == target:
                return True
            for v in adj[u]:
                if v == p:
                    continue
                if dfs(v, u, target):
                    return True
            lookup[u] -= 1
            return False
    
        def dfs2(u, p):
            full, half = price[u]*lookup[u], price[u]//2*lookup[u]
            for v in adj[u]:
                if v == p:
                    continue
                f, h = dfs2(v, u)
                full += min(f, h)
                half += f
            return full, half

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*n
        for u, v in trips:
            dfs(u, -1, v)
        return min(dfs2(0, -1))
