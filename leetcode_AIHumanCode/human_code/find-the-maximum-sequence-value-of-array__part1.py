# Time:  O(n * r + r^2)
# Space: O(r)

# bitmasks, prefix sum, dp
class Solution(object):
    def maxValue(self, nums, k):
        """
        """
        INF = float("inf")
        MAX_MASK = 127
        def is_submask(a, b):
            return (a|b) == b

        def dp(direction, npos):
            result = [npos]*(MAX_MASK+1)
            dp = [INF]*(MAX_MASK+1)
            cnt = [0]*(MAX_MASK+1)
            for i in direction(range(len(nums))):
                dp[nums[i]] = 1
                for mask in range(MAX_MASK+1):
                    if is_submask(nums[i], mask):
                        cnt[mask] += 1
                    dp[mask|nums[i]] = min(dp[mask|nums[i]], dp[mask]+1)
                for mask in range(MAX_MASK+1):
                    if cnt[mask] >= k and dp[mask] <= k and result[mask] == npos:
                        result[mask] = i
            return result

        left = dp(lambda x: x, len(nums))
        right = dp(reversed, -1)
        return next(result for result in reversed(range(MAX_MASK+1)) for l in range(1, MAX_MASK+1) if left[l] < right[result^l])


