# Time:  O(n^2 * k)
# Space: O(n)

# dp, prefix sum
class Solution(object):
    def minXor(self, nums, k):
        """
        """
        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]^nums[i]
        dp = prefix[:]
        dp[0] = INF
        for l in range(2, k+1):
            for i in reversed(range(l-1, len(dp))):
                mn = INF
                for j in range(l-1, i):
                    v = prefix[i]^prefix[j]
                    mx = dp[j] if dp[j] > v else v
                    if mx < mn:
                        mn = mx
                dp[i] = mn
        return dp[-1]


