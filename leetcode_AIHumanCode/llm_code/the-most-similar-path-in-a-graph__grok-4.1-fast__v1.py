class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        m = len(targetPath)
        INF = m + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        dp = [[INF] * n for _ in range(m)]
        parent = [[-1] * n for _ in range(m)]
        for v in range(n):
            dp[0][v] = 0 if names[v] == targetPath[0] else 1
        for i in range(1, m):
            for v in range(n):
                mismatch = 0 if names[v] == targetPath[i] else 1
                min_prev_cost = INF
                best_u = -1
                for u in graph[v]:
                    if dp[i - 1][u] < min_prev_cost:
                        min_prev_cost = dp[i - 1][u]
                        best_u = u
                if best_u != -1:
                    dp[i][v] = mismatch + min_prev_cost
                    parent[i][v] = best_u
        min_cost = INF
        last_node = -1
        for v in range(n):
            if dp[m - 1][v] < min_cost:
                min_cost = dp[m - 1][v]
                last_node = v
        path = []
        curr = last_node
        for i in range(m - 1, -1, -1):
            path.append(curr)
            if i > 0:
                curr = parent[i][curr]
        path.reverse()
        return path
