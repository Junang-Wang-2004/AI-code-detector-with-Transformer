# Time:  O(n)
# Space: O(h)
# dfs
class Solution2(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        """
        def dfs(u, ah):
            lookup[u] = True
            result = 0 if len(adj[u])+(u == 0) == 1 else float("-inf")
            bh = 0 if u == bob else float("inf")
            for v in adj[u]:
                if lookup[v]:
                    continue
                r, h = dfs(v, ah+1)
                result = max(result, r)
                bh = min(bh, h)
            if ah == bh:
                result += amount[u]//2
            elif ah < bh:
                result += amount[u]
            return result, bh+1

        adj = [[] for _ in range(len(edges)+1)]
        lookup = [False]*len(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return dfs(0, 0)[0]
