# Time:  O(n)
# Space: O(1)
# array
class Solution2(object):
    def findNonMinOrMax(self, nums):
        """
        """
        mx, mn = max(nums), min(nums)
        return next((x for x in nums if x not in (mx, mn)), -1)
