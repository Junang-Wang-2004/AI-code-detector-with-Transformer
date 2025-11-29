class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        n = len(nums)
        INF = float('inf')
        costs = [[0] * (n + 1) for _ in range(n)]
        for l in range(n):
            mx = 0
            sm = 0
            for r in range(l + 1, n + 1):
                sm += nums[r - 1]
                mx = max(mx, nums[r - 1])
                costs[l][r] = mx * (r - l) - sm
        max_groups = k + 1
        dp = [[INF] * (max_groups + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for groups in range(1, max_groups + 1):
            for i in range(1, n + 1):
                for prev in range(i + 1):
                    if dp[prev][groups - 1] < INF:
                        dp[i][groups] = min(dp[i][groups], dp[prev][groups - 1] + costs[prev][i])
        return dp[n][max_groups]
