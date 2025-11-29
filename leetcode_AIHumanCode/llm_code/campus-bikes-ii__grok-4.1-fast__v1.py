class Solution:
    def assignBikes(self, workers, bikes):
        n = len(workers)
        m = len(bikes)
        INF = float('inf')
        dist = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dist[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        dp = [[INF] * (1 << m) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for mask in range(1 << m):
                if dp[i][mask] == INF:
                    continue
                for j in range(m):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + dist[i][j])
        return min(dp[n])
