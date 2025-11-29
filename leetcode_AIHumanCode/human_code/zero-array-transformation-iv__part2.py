# Time:  O(q * n * 2^n)
# Space: O(n * 2^n)
# dp
class Solution2(object):
    def minZeroArray(self, nums, queries):
        """
        """
        dp = [{0} for _ in range(len(nums))]
        for i, (l, r, v) in enumerate(queries):
            if all(nums[i] in dp[i] for i in range(len(dp))):
                return i
            for j in range(l, r+1):
                dp[j] |= set(x+v for x in dp[j])
        return len(queries) if all(nums[i] in dp[i] for i in range(len(dp))) else -1
