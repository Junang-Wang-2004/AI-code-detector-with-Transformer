# Time:  O(nlogn)
# Space: O(n)
# dp
class Solution2(object):
    def longestSquareStreak(self, nums):
        """
        """
        dp = collections.defaultdict(int)
        nums.sort()
        result = -1
        for x in nums:
            sqrt_x = int(x**0.5)
            if sqrt_x**2 == x:
                dp[x] = dp[sqrt_x]+1
            else:
                dp[x] = 1
            result = max(result, dp[x])
        return result if result != 1 else -1
