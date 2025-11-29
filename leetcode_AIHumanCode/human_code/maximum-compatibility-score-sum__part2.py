# Time:  O(m * (n + 2^m))
# Space: O(2^m)
# dp solution
class Solution2(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        """
        def popcount(n):  # Time: O(logn) ~= O(1) if n is a 32-bit number
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        def masks(vvi):
            result = []
            for vi in vvi:
                mask, bit = 0, 1
                for i in range(len(vi)):
                    if vi[i]:
                        mask |= bit
                    bit <<= 1
                result.append(mask)
            return result

        nums1, nums2 = masks(students), masks(mentors)
        dp = [(0, 0)]*(2**len(nums2))
        for mask in range(len(dp)):
            bit = 1
            for i in range(len(nums2)):
                if (mask&bit) == 0:
                    dp[mask|bit] = max(dp[mask|bit], (dp[mask][0]+(len(students[0])-popcount(nums1[dp[mask][1]]^nums2[i])), dp[mask][1]+1))
                bit <<= 1
        return dp[-1][0]
