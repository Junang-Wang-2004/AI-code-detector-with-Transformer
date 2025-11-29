class Solution:
    def longestSubsequence(self, nums):
        mx = max(nums)
        dp = [[0] * mx for _ in range(mx)]
        res = 2
        for num in nums:
            i = num - 1
            cur_max = 0
            for delta in range(mx):
                prev_max = 0
                if i - delta >= 0:
                    prev_max = max(prev_max, dp[i - delta][delta])
                if i + delta < mx:
                    prev_max = max(prev_max, dp[i + delta][delta])
                dp[i][delta] = max(dp[i][delta], prev_max + 1)
                cur_max = max(cur_max, dp[i][delta])
            res = max(res, cur_max)
        return res
