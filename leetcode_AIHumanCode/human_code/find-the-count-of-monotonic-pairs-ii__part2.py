from functools import reduce
# Time:  O(n * r), r = max(nums)
# Space: O(r)
# dp, prefix sum
class Solution2(object):
    def countOfPairs(self, nums):
        """
        """
        MOD = 10**9+7
        dp = [int(i <= nums[0]) for i in range(max(nums)+1)]  # dp[j]: numbers of arr1, which is of length i+1 and arr1[i] is j
        for i in range(1, len(nums)):
            # arr1[i-1] <= arr1[i]
            # => arr1[i]-arr1[i-1] >= 0 (1)
            #
            # arr2[i-1] >= arr2[i]
            # => nums[i-1]-arr1[i-1] >= nums[i]-arr1[i] 
            # => arr1[i]-arr1[i-1] >= nums[i]-nums[i-1] (2)
            #
            # (1)+(2): arr1[i]-arr1[i-1] >= max(nums[i]-nums[i-1], 0)
            new_dp = [0]*len(dp)
            diff = max(nums[i]-nums[i-1], 0)
            for j in range(diff, nums[i]+1):
                new_dp[j] = (new_dp[j-1]+dp[j-diff])%MOD
            dp = new_dp
        return reduce(lambda accu, x: (accu+x)%MOD, dp, 0)
