class Solution(object):
    def totalSteps(self, nums):
        stk = []
        ans = 0
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            sub_max = 0
            while stk and stk[-1][0] <= num:
                _, sub_dp = stk.pop()
                sub_max = max(sub_max, sub_dp)
            dp[i] = sub_max + 1 if stk else 0
            stk.append((num, dp[i]))
            ans = max(ans, dp[i])
        return ans
