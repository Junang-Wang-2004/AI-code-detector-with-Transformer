# Time:  O(nlogn)
# Space: O(n)
import collections


# sort, dp
class Solution3(object):
    def maxSelectedElements(self, nums):
        """
        """
        nums.sort()
        dp = collections.defaultdict(int)
        for x in nums:
            dp[x+1] = dp[x]+1
            dp[x] = dp[x-1]+1
        return max(dp.values())
