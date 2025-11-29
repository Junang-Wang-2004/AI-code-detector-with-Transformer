# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        """
        curr = mx = mn = 0
        for num in nums:
            curr += num
            mx = max(mx, curr)
            mn = min(mn, curr)
        return mx-mn
