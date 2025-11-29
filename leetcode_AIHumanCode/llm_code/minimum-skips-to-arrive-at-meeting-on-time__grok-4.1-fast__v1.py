class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        INF = 10**18 + 5
        dp = [INF] * n
        dp[0] = 0
        for i in range(n):
            d = dist[i]
            next_dp = [INF] * n
            for k in range(n):
                if dp[k] == INF:
                    continue
                if i < n - 1:
                    noskip_cost = ((dp[k] + d + speed - 1) // speed) * speed
                    next_dp[k] = min(next_dp[k], noskip_cost)
                else:
                    noskip_cost = dp[k] + d
                    next_dp[k] = min(next_dp[k], noskip_cost)
                if k + 1 < n:
                    skip_cost = dp[k] + d
                    next_dp[k + 1] = min(next_dp[k + 1], skip_cost)
            dp = next_dp
        target = hoursBefore * speed
        for k in range(n):
            if dp[k] <= target:
                return k
        return -1
