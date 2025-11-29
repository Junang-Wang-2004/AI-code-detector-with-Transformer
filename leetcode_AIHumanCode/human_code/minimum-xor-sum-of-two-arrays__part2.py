# Time:  O(n * 2^n)
# Space: O(2^n)
# dp solution
class Solution2(object):
    def minimumXORSum(self, nums1, nums2):
        """
        """
        dp = [(float("inf"), float("inf"))]*(2**len(nums2))
        dp[0] = (0, 0)
        for mask in range(len(dp)):
            bit = 1
            for i in range(len(nums2)):
                if (mask&bit) == 0:
                    dp[mask|bit] = min(dp[mask|bit], (dp[mask][0]+(nums1[dp[mask][1]]^nums2[i]), dp[mask][1]+1))
                bit <<= 1
        return dp[-1][0]
