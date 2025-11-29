# Time:  O(nlogn)
# Space: O(n)
import collections


# sort, dp
class Solution2(object):
    def maxSelectedElements(self, nums):
        """
        """
        nums.sort()
        dp = collections.defaultdict(int)
        dp[nums[0]] = dp[nums[0]+1] = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dp[nums[i]+1] = dp[nums[i]]+1
            elif nums[i] == nums[i-1]+1:
                dp[nums[i]+1] = dp[nums[i]]+1
                dp[nums[i]] = dp[nums[i]-1]+1
            elif nums[i] == nums[i-1]+2:
                dp[nums[i]] = dp[nums[i]-1]+1
                dp[nums[i]+1] = 1
            else:
                dp[nums[i]] = dp[nums[i]+1] = 1
        return max(dp.values())


