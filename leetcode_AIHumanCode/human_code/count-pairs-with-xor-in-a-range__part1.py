# Time:  O(n)
# Space: O(n)

import collections


# dp solution
class Solution(object):
    def countPairs(self, nums, low, high):
        """
        """
        def count(nums, x):
            result = 0
            dp = collections.Counter(nums)
            while x:
                if x&1:
                    result += sum(dp[(x^1)^k]*dp[k] for k in dp.keys())//2  # current limit is xxxxx1*****, count xor pair with xxxxx0***** pattern
                dp = collections.Counter({k>>1: dp[k]+dp[k^1] for k in dp.keys()})
                x >>= 1
            return result
    
        return count(nums, high+1)-count(nums, low)


