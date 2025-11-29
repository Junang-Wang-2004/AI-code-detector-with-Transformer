# Time:  O(n^2)
# Space: O(n^2)
class Solution(object):
    def numOfWays(self, nums):
        """
        """
        def dfs(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            result = dp[len(left)+len(right)][len(left)]
            result = result*dfs(left) % MOD
            result = result*dfs(right) % MOD
            return result

        return (dfs(nums)-1)%MOD
