# Time:  O(n)
# Space: O(n)

# mono stack, dp
class Solution(object):
    def totalSteps(self, nums):
        """
        """
        dp = [0]*len(nums)  # dp[i]: number of rounds for nums[i] to remove all the covered elements
        stk = []
        for i in reversed(range(len(nums))):
            while stk and nums[stk[-1]] < nums[i]:
                dp[i] = max(dp[i]+1, dp[stk.pop()])
            stk.append(i)
        return max(dp)


