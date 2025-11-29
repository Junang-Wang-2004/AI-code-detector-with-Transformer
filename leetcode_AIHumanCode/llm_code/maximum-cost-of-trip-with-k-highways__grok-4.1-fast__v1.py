class Solution:
    def maximumCost(self, n, highways, k):
        if k + 1 > n:
            return -1
        graph = [[] for _ in range(n)]
        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))
        INF = float('-inf')
        dp = [[INF] * n for _ in range(1 << n)]
        for start in range(n):
            dp[1 << start][start] = 0
        res = -1
        for mask in range(1 << n):
            size = bin(mask).count('1')
            for node in range(n):
                if (mask & (1 << node)) == 0:
                    continue
                val = dp[mask][node]
                if val == INF:
                    continue
                if size == k + 1:
                    res = max(res, val)
                    continue
                for neigh, edge_cost in graph[node]:
                    if (mask & (1 << neigh)) == 0:
                        next_mask = mask | (1 << neigh)
                        dp[next_mask][neigh] = max(dp[next_mask][neigh], val + edge_cost)
        return res
