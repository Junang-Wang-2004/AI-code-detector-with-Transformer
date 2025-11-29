# Time:  O(k * n)
# Space: O(n)

# dp, greedy, kadane's algorithm
class Solution(object):
    def maximumStrength(self, nums, k):
        """
        """
        dp = [0]*(len(nums)+1)
        for i in range(k):
            new_dp = [float("-inf")]*(len(nums)+1)
            for j in range(len(nums)):
                new_dp[j+1] = max(new_dp[j], dp[j])+nums[j]*(k-i)*(1 if i%2 == 0 else -1)
            dp = new_dp
        return max(dp)


