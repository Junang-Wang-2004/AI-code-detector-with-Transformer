class Solution:
    def minCost(self, nums, costs):
        n = len(nums)
        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0
        dec = []
        inc = []

        def update(stk, i, nums, dp, costs, cond):
            while stk and cond(nums[stk[-1]], nums[i]):
                prev = stk.pop()
                dp[i] = min(dp[i], dp[prev] + costs[i])

        for i in range(n):
            update(dec, i, nums, dp, costs, lambda x, y: x <= y)
            dec.append(i)
            update(inc, i, nums, dp, costs, lambda x, y: x > y)
            inc.append(i)
        return dp[-1]
