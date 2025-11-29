class Solution(object):
    def minCost(self, nums, k):
        n = len(nums)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            freq = [0] * n
            once = 0
            for begin in range(end - 1, -1, -1):
                val = nums[begin]
                freq[val] += 1
                if freq[val] == 1:
                    once += 1
                elif freq[val] == 2:
                    once -= 1
                length = end - begin
                cost = k + length - once
                dp[end] = min(dp[end], dp[begin] + cost)
        return dp[n]
