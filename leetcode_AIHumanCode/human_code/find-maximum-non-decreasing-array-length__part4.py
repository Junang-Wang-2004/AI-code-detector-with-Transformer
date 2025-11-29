# Time:  O(nlogn)
# Space: O(n)
import bisect


# dp, greedy, prefix sum, binary search
class Solution4(object):
    def findMaximumLength(self, nums):
        """
        """
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        dp = [float("inf")]*(len(nums)+1)
        dp[0] = 0
        prev = [-1]*(len(nums)+1)
        left = -1
        for right in range(len(nums)):
            left = max(left, prev[right])
            dp[right+1] = dp[left+1]+1
            next_right = bisect.bisect_left(prefix, prefix[right+1]+(prefix[right+1]-prefix[left+1]))-1
            prev[next_right] = right
        return dp[-1]
