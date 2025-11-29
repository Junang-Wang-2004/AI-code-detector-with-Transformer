# Time:  O(n)
# Space: O(n)
# dfs
class Solution2(object):
    def minIncrease(self, n, edges, cost):
        """
        """
        def dfs(u, p):
            mx = cnt = 0
            for v in adj[u]:
                if v == p:
                    continue
                c = dfs(v, u)
                if c < mx:
                    continue
                if c > mx:
                    mx = c
                    cnt = 0
                cnt += 1
            result[0] -= cnt
            return mx+cost[u]

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [n-1]
        dfs(0, -1)
        return result[0]
